# Troubleshooting Guide

## Excel Import Issues

### Problem: No ideas appear after importing Excel file

**Solution Steps:**

1. **Open Browser Console**
   - Press `F12` in your browser
   - Click on the "Console" tab
   - Try importing again
   - Look for error messages or warnings

2. **Check Console Output**
   You should see messages like:
   ```
   Excel workbook loaded: ["Sheet1", "Sheet2"]
   Sheet "Sheet1" has 0 rows
   Sheet "Sheet2" has 42 rows
   First row sample: {Category: "...", Insight: "...", ...}
   ```

3. **Common Issues:**

   **Issue: "Sheet has 0 rows"**
   - The Excel file might have headers but no data
   - Check that your Excel file has data rows below the header row

   **Issue: "No ideas found in file"**
   - The column names don't match expected format
   - Try opening the Excel file and checking the exact column names
   - Expected columns: Category, Insight, Insight description, Evidence / execution note

   **Issue: Ideas have "(No title)" in preview**
   - The "Insight" column is not being read correctly
   - Check for typos or extra spaces in the column header

4. **Quick Fix: Export and Re-import**
   - Open your Excel file
   - Save it as CSV (File > Save As > CSV)
   - Try importing the CSV file instead

5. **Alternative: Manual Entry**
   - Go to "All Ideas" page
   - Click "+ Add New Idea"
   - Manually add your ideas

### How to Check Your Excel File Format

Your Excel file should look like this:

| Category | Insight | Insight description | Evidence / execution note |
|----------|---------|---------------------|---------------------------|
| Health   | Tip 1   | Description 1       | Evidence 1                |
| Wellness | Tip 2   | Description 2       | Evidence 2                |

### Still Having Issues?

1. Open `test-excel.html` in your browser
2. Select your Excel file
3. Check the console output to see exactly what's being parsed
4. Share the console output if you need help

## Browser Console Commands for Debugging

Open the console (F12) and try these commands:

```javascript
// Check if ideas are stored
console.log(ideaBank.ideas);

// Check stats
console.log(ideaBank.getStats());

// Check localStorage
console.log(localStorage.getItem('ideaBank_ideas'));

// Manually add a test idea
ideaBank.addIdea({
    title: 'Test Idea',
    description: 'Test description',
    category: 'Testing',
    evidence: 'Test evidence'
});

// Refresh the UI
ui.updateStats();
```

## localStorage Issues

### Problem: Data doesn't persist after closing browser

**Check:**
1. Are you in Private/Incognito mode? (localStorage is disabled)
2. Is your browser storage full?
3. Are browser cookies/storage disabled?

**Solution:**
- Use regular browsing mode (not private)
- Clear old data: Go to browser settings > Clear browsing data > Cookies and site data
- Enable cookies in browser settings

### Clear All Data and Start Fresh

If you want to reset everything:

```javascript
// Open browser console (F12) and run:
localStorage.clear();
location.reload();
```

## SheetJS/XLSX Library Issues

### Problem: "XLSX is not defined"

**Solution:**
1. Check your internet connection (library loads from CDN)
2. Hard refresh the page (Ctrl+F5 or Cmd+Shift+R)
3. Try a different browser
4. Check if your firewall/antivirus is blocking the CDN

### Alternative: Offline SheetJS

If you need to work offline:
1. Download SheetJS from: https://cdn.sheetjs.com/xlsx-0.20.1/package/dist/xlsx.full.min.js
2. Save it in your project folder
3. Update index.html line with SheetJS script to:
   ```html
   <script src="xlsx.full.min.js"></script>
   ```

## Import Preview Not Showing

If the preview doesn't appear when you select a file:

1. Check browser console for errors
2. Make sure the file is .xlsx, .csv, or .json format
3. Try a smaller file first (to rule out size issues)
4. Make sure the file isn't corrupted

## Export Not Working

### Problem: Nothing happens when clicking export buttons

**Check:**
1. Do you have ideas to export? (Check stats counts)
2. Is your browser blocking downloads?
3. Check browser console for errors

**Solution:**
- Allow downloads in browser settings
- Check downloads folder
- Try a different export format

## Performance Issues

### App is slow with many ideas

**Solutions:**
1. Export your data first (backup)
2. Clear old used ideas past cooldown
3. Delete test/duplicate ideas
4. Export and reimport only fresh ideas

## Mobile Issues

### Problem: App doesn't work well on mobile

**Solutions:**
1. Use landscape orientation for better layout
2. Zoom out if buttons are cut off
3. Use a tablet for better experience
4. Consider using desktop for initial setup

## GitHub Pages Issues

### Problem: App doesn't work after deploying to GitHub Pages

**Check:**
1. Are all files committed and pushed?
2. Is GitHub Pages enabled in repository settings?
3. Is the CDN URL accessible (not blocked by CORS)?

**Solution:**
- Make sure all files (HTML, CSS, JS) are in the repository root
- Check GitHub Pages settings: Settings > Pages > Source: main branch, / (root)
- Wait a few minutes for GitHub to deploy

## Need More Help?

1. Open browser console (F12)
2. Take a screenshot of any error messages
3. Note which browser and version you're using
4. Check if the test-excel.html file works with your Excel file
