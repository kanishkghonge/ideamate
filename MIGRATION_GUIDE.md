# Migration Guide: Fixing "Default Insights" Tab

## Problem
If you already have ideas loaded in your browser's localStorage, they won't have the `isDefault` or `isUserCreated` flags, so the "Default Insights" tab will be empty.

## Solution Options

### Option 1: Automatic Migration (Easiest)
The app will automatically migrate your existing ideas when you reload the page:

1. **Refresh your browser** (press F5 or Ctrl+R)
2. Open browser console (F12) and look for:
   ```
   Migrating existing ideas to add source flags...
   Migration complete! Processed XXX ideas.
   ```
3. Navigate to "Default Insights" tab
4. You should now see all 143 default insights

### Option 2: Manual Migration Button
If automatic migration doesn't work:

1. Navigate to **Settings** page
2. Scroll down to **Data Migration** section
3. Click **"Migrate Existing Ideas"** button
4. You'll see a success message: "✅ Migration complete! X ideas migrated..."
5. Navigate to "Default Insights" tab

### Option 3: Clear and Reload (Nuclear Option)
If nothing else works, you can start fresh:

1. Open browser console (F12)
2. Type: `localStorage.clear()`
3. Press Enter
4. Refresh the page (F5)
5. The app will reload all 143 default insights from scratch

⚠️ **Warning**: This will delete any custom ideas you've created!

## How It Works

The migration script:
1. Checks each idea in your localStorage
2. Compares the title with the list of 143 default ideas from the Excel file
3. If it matches → marks as `isDefault: true`
4. If it doesn't match → marks as `isUserCreated: true`

## Verifying It Worked

After migration, check:
- **Default Insights** tab should show ~143 ideas with 📚 blue badge
- **My Ideas** tab should show only your custom ideas with ✍️ green badge
- **All Ideas** tab should show everything mixed together

## Checking Console Logs

Open browser console (F12) and look for these messages:

✅ **Good signs:**
```
Migrating existing ideas to add source flags...
Migration complete! Processed 143 ideas.
```

❌ **Problem signs:**
```
Migration needed but DEFAULT_IDEAS not loaded yet
```
If you see this, the default-data.js file might not be loading properly.

## Still Not Working?

If the Default Insights tab is still empty after trying all options:

1. Check browser console (F12) for errors
2. Make sure `default-data.js` is loading (check Network tab)
3. Verify the file path in index.html:
   ```html
   <script src="default-data.js"></script>
   ```
4. Try hard refresh: Ctrl+Shift+R (or Cmd+Shift+R on Mac)

## Prevention

For new installations:
- The app will automatically mark ideas correctly from the start
- No migration needed if starting with a fresh localStorage
