# 0-2-1 Admin Panel Guide

## Web-Based Content Management System

Edit your blog posts through a beautiful web interface!

---

## Setup (One-Time)

### Install Flask:
```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install Flask
```

---

## Usage

### Start the Admin Server:
```bash
python admin.py
```

You'll see:
```
  0-2-1 Admin Panel
  📝 Admin URL: http://localhost:5000
  🔧 Edit your blog posts through your browser
```

### Open Your Browser:
Navigate to: **http://localhost:5000**

---

## Features

### Dashboard
- **View all posts** in a table
- **Edit button** for each post
- **View button** to preview the published post

### Edit Interface
- **Web form** with all post fields:
  - Title
  - Date
  - Problem
  - System Architecture
  - Diagram (optional)
  - Solution
  - Examples (one per line)
- **Save** to update the HTML file
- **Cancel** to discard changes

### Example Workflow

**Scenario:** Google releases "Grounding with Maps" for Gemini

1. Run `python admin.py`
2. Open http://localhost:5000
3. Click **Edit** on your "Travel Agent" post
4. Update the **System Architecture** section:
   ```
   An AI travel agent using Gemini with grounding via Google Maps API
   to provide real-time location data and recommendations.
   ```
5. Add to **Examples**:
   ```
   Using Maps grounding for restaurant recommendations
   Real-time traffic updates for trip planning
   ```
6. Click **Save**
7. Refresh your blog to see changes!

---

## Publishing Changes

After editing posts:

```bash
# Stop the admin server (Ctrl+C)

# Commit changes
git add posts/
git commit -m "Update: Added Gemini Maps grounding"

# Push to GitHub Pages
git push
```

Your changes are now live!

---

## Tips

- **Keep admin.py running** while editing multiple posts
- **Diagrams**: Upload images to `images/` folder first, then reference filename
- **Examples**: One example per line in the textarea
- **Preview**: Save and open the post in a new tab to see how it looks
- **Backup**: Git tracks all changes, so you can always revert

---

## Troubleshooting

**Port 5000 already in use?**
```bash
# Kill any process on port 5000
lsof -ti:5000 | xargs kill -9
```

**Flask not found?**
```bash
pip install Flask
```

**Changes not showing?**
- Hard refresh your browser (Cmd+Shift+R on Mac)
- Check the HTML file was actually updated in `posts/`

---

## Next Steps

Want to add more features?

- **Password protection** for admin panel
- **Live preview** while editing
- **Image upload** directly from browser
- **Markdown support** for easier writing

Let me know what you'd like!
