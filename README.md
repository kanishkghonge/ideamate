# 💡 Content Idea Bank

A client-side web application for managing and discovering content ideas. Perfect for Instagram Reels, TikTok, YouTube Shorts, or any content creation workflow.

## ✨ Features

- 🎲 **Random Idea Discovery** - Get random eligible ideas with one click
- 💾 **Persistent Storage** - All data saved in browser localStorage
- 📊 **Import/Export** - Excel (.xlsx), CSV, and JSON support
- 🗂️ **Smart Organization** - Track ideas as Fresh, Used, Saved, or Trashed
- ⏰ **Cooldown System** - Automatically hide used ideas for a configurable period (default 90 days)
- 🔍 **Search & Filter** - Find ideas by keyword or category
- ✏️ **Easy Editing** - Edit ideas inline or add new ones manually
- 📱 **Mobile Responsive** - Works on desktop, tablet, and mobile
- 🚀 **No Backend Required** - Runs entirely in your browser
- 🔒 **Privacy First** - Your data never leaves your device

## 🚀 Quick Start

### Option 1: Local Usage (Simplest)

1. Download all files to a folder on your computer
2. Double-click `index.html` to open in your browser
3. Go to Import/Export and import your Excel file
4. Start discovering ideas!

### Option 2: GitHub Pages Hosting (Recommended)

Host your idea bank online so you can access it from any device:

#### Step 1: Create a GitHub Repository

1. Go to [GitHub](https://github.com) and sign in (or create an account)
2. Click the `+` icon in the top right → **New repository**
3. Name it `idea-bank` (or anything you like)
4. Set it to **Public** (required for free GitHub Pages)
5. Click **Create repository**

#### Step 2: Upload Your Files

**Option A: Using GitHub Web Interface**
1. Click **uploading an existing file** link
2. Drag and drop these files:
   - `index.html`
   - `styles.css`
   - `app.js`
   - `import-export.js`
   - `doctor_content_bank.xlsx` (optional - your initial data)
3. Click **Commit changes**

**Option B: Using Git Command Line**
```bash
cd path/to/your/folder
git init
git add index.html styles.css app.js import-export.js
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/idea-bank.git
git push -u origin main
```

#### Step 3: Enable GitHub Pages

1. In your repository, click **Settings**
2. Scroll down to **Pages** section in the left sidebar
3. Under **Source**, select:
   - Branch: `main`
   - Folder: `/ (root)`
4. Click **Save**
5. Wait 1-2 minutes for deployment
6. Your site will be live at: `https://YOUR-USERNAME.github.io/idea-bank/`

#### Step 4: Access Your App

Visit your GitHub Pages URL and bookmark it! You can now access your idea bank from any device.

## 📖 How to Use

### First Time Setup

1. **Import Your Ideas**
   - Click **Import/Export** in the navigation
   - Click **Choose File** and select your Excel file
   - Review the preview
   - Click **Import File**
   - Your ideas are now loaded!

2. **Check Your Stats**
   - See counts for Fresh, Saved, Used, and Trashed ideas
   - These update in real-time as you interact with ideas

### Discovering Ideas

1. Click **Discover** in the navigation
2. Click **Give Me an Idea**
3. A random eligible idea appears with:
   - Category badge
   - Title
   - Description
   - Evidence/Execution notes
   - Five action buttons

### Action Buttons

- **USE** - Mark the idea as used (asks for optional note). Hidden for 90 days by default.
- **TRASH** - Permanently exclude from discovery (can be restored from Trash page)
- **SAVE** - Move to saved collection for later (won't appear in discovery)
- **SKIP** - See another idea (hidden only for current session)
- **EDIT** - Modify any field and save changes

### Managing Ideas

#### All Ideas Page
- View all ideas in your bank
- Search by keyword
- Filter by category
- Edit or delete any idea
- Add new ideas manually

#### Saved Ideas Page
- View ideas you've saved for later
- Restore them to make them available for discovery again
- Edit saved ideas

#### Used Ideas Page
- See all ideas you've marked as used
- View usage dates and notes
- See cooldown status (how many days until available again)
- Restore ideas to make them discoverable again

#### Trash Page
- View all trashed ideas
- Restore ideas if you change your mind
- Permanently delete ideas

### Settings

Configure the **cooldown period** (how long used ideas stay hidden):
- Default: 90 days
- Set to 0 to make used ideas immediately available again
- Set to 365 for annual rotation

### Import & Export

#### Importing
Supports three formats:
- **Excel (.xlsx)** - Recommended
- **CSV** - Simple alternative
- **JSON** - For backups and data migration

**Excel Format:**
Your Excel file should have these columns:
- `Category` - The category/tag
- `Insight` or `Title` - The main idea
- `Insight description` or `Description` - Detailed description
- `Evidence / execution note` or `Evidence` - Supporting notes

The app automatically handles different column names and trailing spaces.

#### Exporting
- **Export All** - Every idea including trashed (Excel)
- **Export Fresh Ideas** - Only eligible ideas (Excel)
- **Export Used** - Used ideas with dates and notes (Excel)
- **Export Trash** - Trashed ideas only (Excel)
- **Full Backup** - Complete backup with all data (JSON)

**Important:** Always keep trashed ideas in exports! They're included in "Export All" and "Full Backup" so you never lose data.

## 🔄 Data Persistence

Your data is stored in your browser's localStorage:

✅ **Persists through:**
- Page refreshes
- Closing and reopening browser
- Computer restarts

❌ **Does NOT persist:**
- Clearing browser data/cookies
- Using Private/Incognito mode
- Switching browsers or devices

### Backing Up Your Data

To preserve your data across devices or browser changes:

1. Go to **Import/Export**
2. Click **Full Backup (JSON)**
3. Save the JSON file somewhere safe (cloud storage, USB drive, etc.)
4. To restore: Import the JSON file on any device

**Recommended:** Export a backup weekly if you're actively using the app.

## 📱 Using on Multiple Devices

Since data is stored locally in each browser:

**Option 1: Separate Banks Per Device**
- Use the app independently on each device
- Export/import to sync occasionally

**Option 2: Manual Sync**
1. On Device A: Export Full Backup
2. Transfer JSON file to Device B (email, cloud, etc.)
3. On Device B: Import the JSON file

**Option 3: Cloud Bookmark**
- Host on GitHub Pages
- Each device has its own data
- Export/import to sync when needed

## 🛠️ Technical Details

### Technology Stack
- Pure HTML5, CSS3, and Vanilla JavaScript
- [SheetJS (XLSX.js)](https://sheetjs.com/) for Excel support (loaded from CDN)
- localStorage API for data persistence
- No frameworks, no build process, no backend

### Browser Requirements
- Modern browser with ES6+ support
- localStorage enabled
- JavaScript enabled
- Internet connection (only for SheetJS CDN on first load)

### File Structure
```
idea-bank/
├── index.html           # Main application
├── styles.css          # Styling
├── app.js              # Core logic and data management
├── import-export.js    # Import/Export functionality
├── README.md           # This file
├── TROUBLESHOOTING.md  # Help guide
├── TEST_INSTRUCTIONS.md # Testing checklist
└── test-excel.html     # Debug tool for Excel parsing
```

### Data Model
Each idea contains:
```javascript
{
  id: "unique_id",
  title: "Idea title",
  description: "Detailed description",
  category: "Category name",
  evidence: "Supporting notes",
  notes: "Personal notes",
  status: "fresh|used|saved|trashed",
  createdAt: "ISO date",
  usedAt: "ISO date",
  trashedAt: "ISO date",
  savedAt: "ISO date",
  useNote: "Note from when marked as used"
}
```

## 🐛 Troubleshooting

### Import Issues
If your Excel import isn't working:
1. Press F12 to open browser console
2. Try importing again
3. Check console for error messages
4. See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for detailed help

### Data Not Persisting
- Make sure you're not in Private/Incognito mode
- Check that localStorage is enabled
- Try a different browser
- Export a backup before clearing browser data

### No Ideas Appearing
- Check stats - do you have fresh ideas?
- All ideas might be used and in cooldown
- Check Saved/Trashed pages - might need to restore some
- Try adding a new idea manually to test

For more help, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

## 📝 Tips & Best Practices

### For Content Creators
1. **Import your content calendar** - Use this to store all your ideas
2. **Use categories** - Tag ideas by platform, topic, or series
3. **Add evidence** - Link to successful examples or research
4. **Track usage** - Note when and where you used each idea
5. **Regular exports** - Backup your data weekly

### Workflow Suggestions
1. **Morning routine:** Click "Give Me an Idea" to pick your content for the day
2. **After posting:** Mark the idea as USED with a note about performance
3. **Research sessions:** Add new ideas in batches using "Add New Idea"
4. **Monthly review:** Check Used ideas, restore successful ones, trash underperformers
5. **Quarterly cleanup:** Export data, clear out trash, re-import fresh ideas

### Category Examples
- Platform: Instagram, TikTok, YouTube, Twitter
- Type: Tutorial, Story, Behind-the-scenes, Tip
- Topic: Health, Fitness, Nutrition, Wellness
- Series: Monday Motivation, Friday Facts, Weekend Wisdom

## 🔒 Privacy & Security

- **No data collection:** This app doesn't send data anywhere
- **No tracking:** No analytics or cookies
- **Local storage only:** Your data stays on your device
- **Open source:** All code is visible and inspectable
- **No login required:** No accounts, no passwords

## 📄 License

This project is free to use, modify, and distribute. No attribution required.

## 🤝 Contributing

Feel free to:
- Fork the repository
- Modify for your needs
- Share improvements
- Report issues

## 💬 Support

If you encounter issues:
1. Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. Open browser console (F12) to see error messages
3. Use `test-excel.html` to debug Excel imports
4. Export your data before making major changes

## 🎯 Use Cases

Perfect for:
- 📸 Content creators planning social media posts
- 📝 Writers managing story ideas
- 🎨 Designers tracking creative concepts
- 🎥 Video creators organizing content calendars
- 📱 Social media managers planning campaigns
- 💡 Anyone who needs to organize and rediscover ideas

## ⚡ Quick Reference

| Action | Result |
|--------|--------|
| USE | Marks as used, hides for cooldown period |
| TRASH | Excludes from discovery, can restore |
| SAVE | Moves to saved collection, excluded from discovery |
| SKIP | Shows another idea, hides only for current session |
| EDIT | Modify and save changes |

## 🔮 Future Ideas

Potential enhancements (not currently implemented):
- Cloud sync option
- Collaboration features
- Analytics dashboard
- Calendar integration
- API for automation
- Mobile app versions

---

**Made for content creators who want a simple, reliable way to manage and discover their ideas. No fluff, just functionality.**

Enjoy creating! 🚀
