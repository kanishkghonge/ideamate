# Testing Instructions for Content Idea Bank

## Complete Workflow Test

Follow these steps to verify all functionality works correctly:

### 1. Open the Application
- Open `index.html` in your web browser
- You should see the Idea Bank interface with navigation menu

### 2. Import Your Excel File
1. Click on **Import/Export** in the navigation
2. Click **Choose File** and select `doctor_content_bank.xlsx`
3. You should see a preview showing the first 5 ideas
4. Click **Import File**
5. You should see a success message showing how many ideas were imported
6. ✓ **Verify**: Check that the stats bar shows the correct count of fresh ideas

### 3. Test Discovery Feature
1. Click on **Discover** in the navigation
2. Click the **Give Me an Idea** button
3. ✓ **Verify**: A random idea from your bank should appear with:
   - Category badge
   - Title
   - Description
   - Evidence/Execution notes
   - Five action buttons (USE, TRASH, SAVE, SKIP, EDIT)

### 4. Test USE Action
1. With an idea displayed, click **USE**
2. ✓ **Verify**: A modal appears asking for an optional note
3. Add a note (e.g., "Posted as Instagram Reel on Jan 15")
4. Click **Confirm**
5. ✓ **Verify**: The idea is marked as used and a new idea appears
6. ✓ **Verify**: The "Used" count in stats increases by 1

### 5. Test TRASH Action
1. Click **Give Me an Idea** if no idea is shown
2. Click **TRASH**
3. ✓ **Verify**: A confirmation dialog appears
4. Click OK
5. ✓ **Verify**: The idea is trashed and a new idea appears
6. ✓ **Verify**: The "Trashed" count increases by 1

### 6. Test SAVE Action
1. Click **Give Me an Idea** if no idea is shown
2. Click **SAVE**
3. ✓ **Verify**: The idea is saved and a new idea appears
4. ✓ **Verify**: The "Saved" count increases by 1

### 7. Test SKIP Action
1. Click **Give Me an Idea** if no idea is shown
2. Note the title of the current idea
3. Click **SKIP**
4. ✓ **Verify**: A different idea appears immediately
5. ✓ **Verify**: Continue skipping - the skipped idea should not appear again in this session

### 8. Test EDIT Action
1. Click **Give Me an Idea** if no idea is shown
2. Click **EDIT**
3. ✓ **Verify**: A modal appears with all idea fields pre-filled
4. Modify the title (e.g., add " - EDITED")
5. Click **Save Changes**
6. ✓ **Verify**: The idea card updates with your changes

### 9. Test Persistence (CRITICAL TEST)
1. Note the current stats (Fresh, Saved, Used, Trashed counts)
2. **Close the browser completely**
3. **Reopen** `index.html`
4. ✓ **Verify**: All stats are exactly the same as before closing
5. ✓ **Verify**: Click "Give Me an Idea" - used/trashed/saved ideas don't appear
6. ✓ **Verify**: Navigate to each page - all your data is still there

### 10. Test All Ideas Page
1. Click **All Ideas** in navigation
2. ✓ **Verify**: All imported ideas are listed
3. Test the search box - type a keyword
4. ✓ **Verify**: Results filter in real-time
5. Test category filter dropdown
6. ✓ **Verify**: Results filter by selected category
7. Click **Edit** on any idea
8. ✓ **Verify**: Can edit and save changes
9. Click **Delete** on any idea
10. ✓ **Verify**: Idea is permanently removed after confirmation

### 11. Test Saved Ideas Page
1. Click **Saved** in navigation
2. ✓ **Verify**: All saved ideas appear here
3. Click **Restore** on a saved idea
4. ✓ **Verify**: The idea returns to fresh status and appears in discovery again

### 12. Test Used Ideas Page
1. Click **Used** in navigation
2. ✓ **Verify**: All used ideas appear with usage date and note
3. ✓ **Verify**: Ideas in cooldown show "In cooldown for X more days"
4. Click **Restore** on a used idea
5. ✓ **Verify**: Idea becomes available for discovery again

### 13. Test Trash Page
1. Click **Trash** in navigation
2. ✓ **Verify**: All trashed ideas appear with trash date
3. Click **Restore** on a trashed idea
4. ✓ **Verify**: Idea returns to fresh status
5. Click **Delete** on a trashed idea
6. ✓ **Verify**: Idea is permanently deleted after confirmation

### 14. Test Add New Idea
1. Go to **All Ideas** page
2. Click **+ Add New Idea** button
3. ✓ **Verify**: Modal opens with empty form
4. Fill in:
   - Title: "Test New Idea"
   - Description: "This is a test"
   - Category: "Testing"
   - Evidence: "Manual test"
5. Click **Add Idea**
6. ✓ **Verify**: Success message appears
7. ✓ **Verify**: New idea appears in All Ideas list
8. ✓ **Verify**: Can discover the new idea

### 15. Test Cooldown Period
1. Click **Settings** in navigation
2. ✓ **Verify**: Current cooldown is 90 days
3. Change to 7 days
4. Go to **Used** ideas page
5. ✓ **Verify**: Ideas used more than 7 days ago show "Available for discovery again"
6. Go to **Discover**
7. ✓ **Verify**: Those ideas can appear again

### 16. Test Import - No Duplicates
1. Go to **Import/Export**
2. Import `doctor_content_bank.xlsx` again
3. ✓ **Verify**: Preview shows duplicates marked in orange/yellow
4. Click **Import File**
5. ✓ **Verify**: Message shows "Skipped duplicates: X ideas"
6. ✓ **Verify**: Idea count doesn't change

### 17. Test Export All
1. Go to **Import/Export**
2. Click **Export All (Excel)**
3. ✓ **Verify**: File downloads named `all-ideas.xlsx`
4. Open the file
5. ✓ **Verify**: Contains ALL ideas including trashed ones
6. ✓ **Verify**: All columns present: ID, Category, Title, Description, Evidence, Notes, Status, dates

### 18. Test Export Fresh Ideas
1. Click **Export Fresh Ideas (Excel)**
2. ✓ **Verify**: File downloads
3. Open the file
4. ✓ **Verify**: Contains only fresh ideas and used ideas past cooldown
5. ✓ **Verify**: Does NOT contain trashed or saved ideas

### 19. Test Export Used
1. Click **Export Used (Excel)**
2. ✓ **Verify**: File downloads
3. Open the file
4. ✓ **Verify**: Contains only used ideas with dates and notes

### 20. Test Export Trash
1. Click **Export Trash (Excel)**
2. ✓ **Verify**: File downloads
3. Open the file
4. ✓ **Verify**: Contains only trashed ideas

### 21. Test Full Backup & Restore
1. Click **Full Backup (JSON)**
2. ✓ **Verify**: JSON file downloads with date in filename
3. Open the JSON file in a text editor
4. ✓ **Verify**: Contains all ideas, settings, and metadata
5. In the app, make some changes (trash an idea, use an idea)
6. Go to **Import/Export**
7. Import the JSON backup file
8. ✓ **Verify**: All data restores to the backup state

### 22. Test Mobile Responsiveness
1. Resize browser window to mobile size (or use mobile device)
2. ✓ **Verify**: Navigation collapses appropriately
3. ✓ **Verify**: Action buttons stack vertically
4. ✓ **Verify**: Stats display in single column
5. ✓ **Verify**: All functionality works on mobile

### 23. Test Empty State
1. Go to **Discover**
2. If you have ideas, skip until all are hidden
3. ✓ **Verify**: Message appears: "No eligible ideas available..."

### 24. Test Random Selection Logic
1. Go to **Discover**
2. Click **Give Me an Idea** 10 times
3. ✓ **Verify**: Different ideas appear (not the same one repeatedly)
4. ✓ **Verify**: Never-used ideas appear first
5. ✓ **Verify**: Trashed ideas NEVER appear
6. ✓ **Verify**: Saved ideas NEVER appear
7. ✓ **Verify**: Used ideas in cooldown NEVER appear

## Common Issues to Check

### If ideas don't persist after refresh:
- Check browser console for errors
- Verify localStorage is enabled in your browser
- Try a different browser

### If import doesn't work:
- Check that the Excel file is in the same format as the provided sample
- Check browser console for errors
- Try exporting as CSV and importing that instead

### If SheetJS doesn't load:
- Check internet connection (SheetJS loads from CDN)
- Check browser console for errors
- Try refreshing the page

## Success Criteria

All 24 test cases above should pass with ✓ marks. The application should:

1. ✓ Import Excel/CSV/JSON files correctly
2. ✓ Prevent duplicate imports
3. ✓ Show random eligible ideas
4. ✓ Track USE/TRASH/SAVE/SKIP actions
5. ✓ Persist all data through browser refresh
6. ✓ Respect 90-day cooldown by default
7. ✓ Allow editing ideas
8. ✓ Allow adding new ideas manually
9. ✓ Export in multiple formats
10. ✓ Full backup and restore functionality
11. ✓ Search and filter on all pages
12. ✓ Work on mobile devices
13. ✓ Never show trashed ideas in discovery
14. ✓ Include trashed ideas in exports
15. ✓ Show clear stats and counts

## Performance Test

- App should load instantly (no backend)
- Discovery should be instant
- Import of 100+ ideas should take < 5 seconds
- No lag when clicking buttons
- Smooth animations

## Browser Compatibility

Test in:
- ✓ Chrome/Edge
- ✓ Firefox
- ✓ Safari
- ✓ Mobile browsers

All features should work in modern browsers (ES6+ support required).
