#!/usr/bin/env python3
"""Clinic Insight Bank — dependency-free local app."""
import json, os, random, re, sqlite3, sys, time, webbrowser, zipfile, xml.etree.ElementTree as ET
from threading import Timer
from datetime import datetime, timezone
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
DB = ROOT / "clinic_insights.sqlite3"
NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"

def now(): return datetime.now(timezone.utc).isoformat(timespec="seconds")
def conn():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    return c
def init():
    c=conn(); c.executescript('''
    CREATE TABLE IF NOT EXISTS insights (
      id INTEGER PRIMARY KEY, core TEXT NOT NULL, application TEXT NOT NULL DEFAULT '',
      category TEXT NOT NULL DEFAULT '', cta TEXT NOT NULL DEFAULT '', used_times INTEGER NOT NULL DEFAULT 0,
      trashed INTEGER NOT NULL DEFAULT 0, created_at TEXT NOT NULL, source TEXT NOT NULL DEFAULT 'manual');
    CREATE TABLE IF NOT EXISTS history (
      id INTEGER PRIMARY KEY, insight_id INTEGER, action TEXT NOT NULL, detail TEXT, created_at TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS drafts (
      id INTEGER PRIMARY KEY, core TEXT NOT NULL, application TEXT NOT NULL, category TEXT NOT NULL, cta TEXT NOT NULL, created_at TEXT NOT NULL);
    CREATE UNIQUE INDEX IF NOT EXISTS insight_unique ON insights(core, application);
    '''); c.commit();
    if c.execute('SELECT count(*) FROM insights').fetchone()[0] == 0:
        xlsx=next(ROOT.glob('*.xlsx'), None)
        if xlsx: import_xlsx(c, xlsx)
    c.close()

def cell_value(c):
    text=''.join(x.text or '' for x in c.iter(NS+'t'))
    if text: return text
    v=c.find(NS+'v'); return v.text if v is not None else ''
def import_xlsx(c, path):
    with zipfile.ZipFile(path) as z: root=ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
    rows=[]
    for row in root.findall('.//'+NS+'row'):
        vals=[cell_value(x) for x in row.findall(NS+'c')]
        if vals: rows.append(vals)
    for r in rows[1:]:
        r=(r+['']*5)[:5]
        if r[0].strip():
            try: used=int(float(r[4] or 0))
            except ValueError: used=0
            c.execute('INSERT OR IGNORE INTO insights(core,application,category,cta,used_times,created_at,source) VALUES(?,?,?,?,?,?,?)', (*r[:4],used,now(),'excel'))
    c.commit()

def record(c, action, insight_id=None, detail=None):
    c.execute('INSERT INTO history(insight_id,action,detail,created_at) VALUES(?,?,?,?)',(insight_id,action,detail,now()))
def insight(row): return dict(row) if row else None
def filter_sql(q, active=True):
    cats=q.get('categories',[]); ctas=q.get('ctas',[]); where=[]; vals=[]
    if active is not None: where.append('trashed=?'); vals.append(0 if active else 1)
    if cats: where.append('category IN (%s)' % ','.join('?'*len(cats))); vals+=cats
    if ctas: where.append('cta IN (%s)' % ','.join('?'*len(ctas))); vals+=ctas
    return (' WHERE '+' AND '.join(where) if where else ''), vals
def choose(c, q):
    where, vals=filter_sql(q); rows=c.execute('SELECT * FROM insights'+where,vals).fetchall()
    if not rows: return None
    weights=[1/(1+row['used_times'])**1.35 for row in rows]
    return insight(random.choices(rows, weights=weights, k=1)[0])

class App(SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args): print(fmt % args)
    def send_json(self, data, code=200):
        raw=json.dumps(data, ensure_ascii=False).encode(); self.send_response(code); self.send_header('Content-Type','application/json; charset=utf-8'); self.send_header('Content-Length',str(len(raw))); self.end_headers(); self.wfile.write(raw)
    def body(self):
        n=int(self.headers.get('Content-Length','0')); return json.loads(self.rfile.read(n) or b'{}')
    def do_GET(self):
        p=urlparse(self.path)
        if p.path.startswith('/api/'):
            q=parse_qs(p.query); c=conn()
            try:
                if p.path=='/api/random': out={'insight':choose(c,q)}
                elif p.path=='/api/options':
                    out={'categories':[x[0] for x in c.execute("SELECT DISTINCT category FROM insights WHERE category<>'' ORDER BY category")], 'ctas':[x[0] for x in c.execute("SELECT DISTINCT cta FROM insights WHERE cta<>'' ORDER BY cta")]}
                elif p.path=='/api/insights':
                    active=None if q.get('state',['all'])[0]=='all' else q.get('state',['active'])[0]!='trash'
                    wh,vs=filter_sql(q,active); search=q.get('search',[''])[0].strip();
                    if search: wh += (' AND ' if wh else ' WHERE ') + '(core LIKE ? OR application LIKE ? OR category LIKE ? OR cta LIKE ?)'; vs += ['%'+search+'%']*4
                    sort={'new':'created_at DESC','old':'created_at','used':'used_times DESC','least':'used_times, created_at DESC','category':'category, core'}.get(q.get('sort',['new'])[0],'created_at DESC')
                    out={'insights':[insight(x) for x in c.execute('SELECT * FROM insights'+wh+' ORDER BY '+sort,vs)]}
                elif p.path=='/api/history': out={'history':[dict(x) for x in c.execute('''SELECT h.*, i.core FROM history h LEFT JOIN insights i ON i.id=h.insight_id ORDER BY h.id DESC LIMIT 150''')]}
                elif p.path=='/api/drafts': out={'drafts':[dict(x) for x in c.execute('SELECT * FROM drafts ORDER BY id DESC')]}
                else: return self.send_json({'error':'Not found'},404)
                self.send_json(out)
            finally: c.close()
        else:
            self.path='/index.html' if p.path=='/' else p.path; return super().do_GET()
    def do_POST(self):
        p=urlparse(self.path); data=self.body(); c=conn()
        try:
            if p.path=='/api/action':
                iid=int(data['id']); action=data['action']
                if action=='used': c.execute('UPDATE insights SET used_times=used_times+1 WHERE id=?',(iid,))
                elif action=='trash': c.execute('UPDATE insights SET trashed=1 WHERE id=?',(iid,))
                elif action=='restore': c.execute('UPDATE insights SET trashed=0 WHERE id=?',(iid,))
                elif action!='skipped': return self.send_json({'error':'Bad action'},400)
                record(c,action,iid); c.commit(); return self.send_json({'ok':True})
            if p.path in ('/api/insights','/api/drafts'):
                fields=[str(data.get(k,'')).strip() for k in ('core','application','category','cta')]
                if not fields[0]: return self.send_json({'error':'Core insight is required'},400)
                table='drafts' if p.path.endswith('drafts') else 'insights'
                if table=='drafts': c.execute('INSERT INTO drafts(core,application,category,cta,created_at) VALUES(?,?,?,?,?)',(*fields,now()))
                else:
                    c.execute('INSERT INTO insights(core,application,category,cta,created_at,source) VALUES(?,?,?,?,?,?)',(*fields,now(),'manual')); record(c,'added',c.execute('SELECT last_insert_rowid()').fetchone()[0])
                c.commit(); return self.send_json({'ok':True})
            if p.path.startswith('/api/insights/'):
                iid=int(p.path.rsplit('/',1)[1]); fields=[str(data.get(k,'')).strip() for k in ('core','application','category','cta')]
                c.execute('UPDATE insights SET core=?,application=?,category=?,cta=? WHERE id=?',(*fields,iid)); c.commit(); return self.send_json({'ok':True})
            if p.path=='/api/bulk':
                items=data.get('items',[]); added=0
                for x in items:
                    fields=[str(x.get(k,'')).strip() for k in ('core','application','category','cta')]
                    if fields[0]:
                        c.execute('INSERT OR IGNORE INTO insights(core,application,category,cta,created_at,source) VALUES(?,?,?,?,?,?)',(*fields,now(),'bulk')); record(c,'added',c.execute('SELECT last_insert_rowid()').fetchone()[0]); added+=1
                c.commit(); return self.send_json({'ok':True,'added':added})
            if p.path=='/api/drafts/approve':
                ids=data.get('ids',[]); n=0
                for iid in ids:
                    x=c.execute('SELECT * FROM drafts WHERE id=?',(iid,)).fetchone()
                    if x:
                        c.execute('INSERT OR IGNORE INTO insights(core,application,category,cta,created_at,source) VALUES(?,?,?,?,?,?)',(x['core'],x['application'],x['category'],x['cta'],now(),'ai')); c.execute('DELETE FROM drafts WHERE id=?',(iid,)); n+=1
                c.commit(); return self.send_json({'ok':True,'added':n})
            if p.path=='/api/generate': return self.generate(c,data)
            return self.send_json({'error':'Not found'},404)
        except sqlite3.IntegrityError: return self.send_json({'error':'That insight already exists.'},409)
        except Exception as e: return self.send_json({'error':str(e)},500)
        finally: c.close()
    def generate(self,c,data):
        key=os.environ.get('OPENAI_API_KEY')
        if not key: return self.send_json({'error':'To enable generation, start the app with OPENAI_API_KEY set. Nothing is sent anywhere until then.'},400)
        topic=str(data.get('topic','')).strip(); category=str(data.get('category','')).strip(); count=min(max(int(data.get('count',5)),1),12)
        samples=c.execute('SELECT core,application,category,cta FROM insights WHERE trashed=0 ORDER BY RANDOM() LIMIT 12').fetchall()
        prompt=f'''Create {count} highly specific video IDEA BANK entries for small/medium Indian doctor clinics. Topic: {topic or category or 'choose useful gaps'}. Return ONLY a JSON array with objects core, application, category, cta. Each core must be an original, sharp, counterintuitive claim. Application must explain a concrete economic, operational or patient-behaviour mechanism in Indian clinic context. No generic business advice, no hooks/scripts/captions, no invented statistics. Match specificity of these examples: {json.dumps([dict(x) for x in samples],ensure_ascii=False)}'''
        req=Request('https://api.openai.com/v1/responses',data=json.dumps({'model':os.environ.get('OPENAI_MODEL','gpt-4.1-mini'),'input':prompt}).encode(),headers={'Authorization':'Bearer '+key,'Content-Type':'application/json'})
        result=json.loads(urlopen(req,timeout=60).read()); text=result.get('output_text','')
        match=re.search(r'\[.*\]',text,re.S)
        if not match: raise ValueError('Generator did not return a usable review list.')
        items=json.loads(match.group()); n=0
        for x in items:
            if x.get('core'):
                c.execute('INSERT INTO drafts(core,application,category,cta,created_at) VALUES(?,?,?,?,?)',(x['core'],x.get('application',''),x.get('category',category),x.get('cta',''),now())); n+=1
        c.commit(); return self.send_json({'ok':True,'drafts_added':n})

if __name__=='__main__':
    init(); port=int(os.environ.get('PORT','8765'))
    address=f'http://127.0.0.1:{port}'
    print(f'\nClinic Insight Bank is ready: {address}\nPress Ctrl+C to stop it.\n', flush=True)
    if '--open' in sys.argv: Timer(.7, lambda: webbrowser.open(address)).start()
    ThreadingHTTPServer(('0.0.0.0',port),App).serve_forever()
