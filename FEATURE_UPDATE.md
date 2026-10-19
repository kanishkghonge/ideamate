# Feature Update: Default Insights & User Ideas Separation

## Overview
This update adds functionality to distinguish between default insights (from the Excel file) and user-created ideas, with separate pages to view each type.

## Changes Made

### 1. **Data Model Updates** (`app.js`)
- Added `isDefault` flag to track insights from the Excel file
- Added `isUserCreated` flag to track ideas created by the user
- Updated `addIdea()` method to accept these flags
- Updated `searchIdeas()` method to filter by source (default/user)
- Updated `getStats()` to count default and user-created ideas separately

### 2. **New Pages Added** (`index.html`)
- **Default Insights** page (`/default-insights`): Shows all 143 insights from doctor_content_bank.xlsx
- **My Ideas** page (`/user-ideas`): Shows only ideas created by the user
- Both pages have their own search and filter functionality

### 3. **Navigation Updates**
Added new navigation links:
- "Default Insights" - View all default insights from Excel
- "My Ideas" - View and manage your own ideas

### 4. **Visual Indicators**
Added source badges to idea cards:
- 📚 **Default Insight** (blue badge) - Ideas from the Excel file
- ✍️ **User Created** (green badge) - Ideas you created

### 5. **Functionality Improvements**
- **Delete Protection**: Default insights cannot be deleted, only user-created ideas can be deleted
- **Separate Add Buttons**: 
  - "Add New Idea" button on All Ideas page
  - "Add New Idea" button on My Ideas page
- **Filtering**: Can filter ideas by source (default vs user-created)

### 6. **Default Data Loading** (`default-data.js`)
- Updated to mark all loaded ideas as `isDefault: true`
- Ensures proper tracking of Excel-sourced insights

## How to Use

### Viewing Default Insights
1. Click "Default Insights" in the navigation
2. Browse all 143 insights from doctor_content_bank.xlsx
3. Search and filter by category
4. You can edit or use these insights, but cannot delete them

### Adding Your Own Ideas
1. Click "My Ideas" in the navigation
2. Click "Add New Idea" button
3. Fill in the form and save
4. Your ideas will be marked as user-created

### Viewing Separately
- **Default Insights** page shows only Excel insights
- **My Ideas** page shows only your created ideas
- **All Ideas** page shows everything mixed together

## Stats Dashboard
The stats bar now tracks:
- Fresh Ideas (total available)
- Saved Ideas
- Used Ideas
- Trashed Ideas
- Default Ideas count (internal)
- User-Created Ideas count (internal)

## Technical Details

### Data Structure
Each idea now has:
```javascript
{
  id: "unique_id",
  title: "...",
  description: "...",
  category: "...",
  evidence: "...",
  notes: "...",
  status: "fresh|used|saved|trashed",
  createdAt: "ISO date",
  usedAt: null,
  trashedAt: null,
  savedAt: null,
  useNote: "",
  isDefault: true/false,      // NEW
  isUserCreated: true/false   // NEW
}
```

### Backward Compatibility
- Existing ideas in localStorage will continue to work
- Old ideas without flags will be treated as regular ideas (neither default nor user-created)
- You can clear localStorage and reload to get proper flags on all ideas

## Testing the Features

1. **Open the app** in your browser
2. **Check Default Insights**: Navigate to "Default Insights" to see all 143 insights
3. **Create a new idea**: Go to "My Ideas" and click "Add New Idea"
4. **Verify badges**: Check that ideas show the correct source badge
5. **Test deletion**: Try to delete a default insight (should not have delete button)
6. **Test user idea deletion**: Delete a user-created idea (should work)

## Notes
- All 143 default insights from the Excel file are preserved
- User-created ideas are clearly separated
- The "Discover" page will show both types mixed together (by design)
- Importing from Excel will mark all imported ideas as default insights

Enjoy your enhanced idea management system! 🎉
