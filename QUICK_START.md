# 🚀 Quick Start Guide

## Get Started in 3 Steps

### 1️⃣ Open the App
Double-click `index.html` in your browser

### 2️⃣ Import Your Ideas
1. Click **Import/Export** in the menu
2. Select `doctor_content_bank.xlsx`
3. Click **Import File**

### 3️⃣ Discover Ideas
1. Click **Discover** in the menu
2. Click **Give Me an Idea**
3. Use the action buttons (USE, TRASH, SAVE, SKIP, EDIT)

## 🔧 If Excel Import Doesn't Work

**Check the browser console:**
1. Press `F12` to open Developer Tools
2. Click the **Console** tab
3. Try importing again
4. Look for messages like:
   - "Excel workbook loaded: [Sheet1, Sheet2]"
   - "Sheet 'Sheet2' has X rows"
   
**What you should see:**
- A preview of your ideas before importing
- Success message: "✓ Imported: X ideas"

**If you see "No ideas found":**
1. Open `test-excel.html` in your browser
2. Select your Excel file
3. Check what gets parsed
4. Or save your Excel as CSV and import that instead

## 📊 Debug Commands

Open browser console (F12) and try:

```javascript
// Check if ideas loaded
console.log(ideaBank.ideas);

// Check stats
console.log(ideaBank.getStats());

// Add a test idea
ideaBank.addIdea({
    title: 'Test Idea',
    description: 'This is a test',
    category: 'Testing',
    evidence: 'Manual test'
});
ui.updateStats();
```

## ✅ Quick Test Checklist

- [ ] App loads without errors
- [ ] Import shows preview of ideas
- [ ] Import succeeds with count message
- [ ] Stats show correct numbers
- [ ] "Give Me an Idea" button works
- [ ] Action buttons work (USE, TRASH, etc.)
- [ ] Refresh page → data persists
- [ ] Export creates downloadable file

## 🆘 Need Help?

1. See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for detailed help
2. See [README.md](README.md) for full documentation
3. Use `test-excel.html` to debug Excel parsing
4. Check browser console (F12) for error messages

## 🌐 Want to Host Online?

Follow the GitHub Pages instructions in [README.md](README.md) - takes about 5 minutes!

---

**Everything working? Start discovering your ideas! 💡**
