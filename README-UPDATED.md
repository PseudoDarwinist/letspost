# 0-2-1 Blog

A minimalist blog for daily AI use case documentation with a web-based admin panel.

---

## Features

✅ **Terminal-inspired design** with mustard yellow on dark gradient background
✅ **Web-based CMS** - Edit posts through your browser
✅ **Theater-mode reading** - Wide, cinematic content layout
✅ **Easy publishing** - Simple Python scripts or web interface
✅ **GitHub Pages ready** - Static hosting, no server needed

---

## Quick Start

### View Your Blog
```bash
open index.html
```

### Edit Posts (Web Interface)
```bash
python3 admin.py
# Opens at http://localhost:5000
```

### Create New Post (Command Line)
```bash
python3 create-post.py
python3 update-index.py
```

---

## Admin Panel

Your new web-based editor is ready!

### Start Editing:
```bash
python3 admin.py
```

Then open: **http://localhost:5000**

### Features:
- 📝 **Dashboard** - See all your posts
- ✏️ **Web Editor** - Edit posts in your browser
- 💾 **Auto-save** - Updates HTML files directly
- 🎨 **Matches your theme** - Same mustard/green aesthetic

### Example Use Case:
Google releases "Grounding with Maps" for Gemini:

1. Open admin panel
2. Click "Edit" on your travel agent post
3. Update architecture section with new Maps grounding feature
4. Add new examples
5. Click "Save"
6. Push to GitHub Pages

Done! Your blog is updated.

---

## File Structure

```
/
├── index.html              # Homepage
├── styles.css              # Main styles (mustard yellow theme)
├── admin.py                # Web-based admin panel ⭐ NEW
├── create-post.py          # CLI post creator
├── update-index.py         # Update homepage with new posts
├── posts/
│   ├── 001-example.html    # Your blog posts
│   └── post-template.html  # Template for new posts
├── images/
│   └── site-background.jpg # Main background gradient
├── templates/              # Admin panel templates ⭐ NEW
│   ├── admin.html
│   └── edit-post.html
└── static/                 # Admin panel styles ⭐ NEW
    └── admin.css
```

---

## Workflows

### Method 1: Web Interface (Recommended for Editing)
```bash
python3 admin.py              # Start admin server
# Edit posts at http://localhost:5000
git add . && git commit -m "Updated posts" && git push
```

### Method 2: Command Line (Quick for New Posts)
```bash
python3 create-post.py        # Create new post
python3 update-index.py       # Add to homepage
git add . && git commit -m "New post" && git push
```

---

## Publishing to GitHub Pages

### First Time Setup:
```bash
git init
git add .
git commit -m "Initial commit: 0-2-1 blog"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO.git
git push -u origin main
```

Then:
1. Go to GitHub repo → Settings → Pages
2. Source: "main" branch, "/" root
3. Save
4. Your blog will be live at: `https://YOUR-USERNAME.github.io/YOUR-REPO`

### Updating:
```bash
git add .
git commit -m "Update: [what you changed]"
git push
```

---

## Customization

### Change Colors:
Edit [styles.css](styles.css):
- Main text: `#e6b800` (mustard yellow)
- Background: `images/site-background.jpg`

### Change Site Name:
Currently: **0-2-1**
Edit in: `index.html`, `admin.py`, `create-post.py`

### Add Features:
See [ADMIN-GUIDE.md](ADMIN-GUIDE.md) for ideas:
- Password protection
- Live preview
- Markdown support
- Image uploads

---

## Support

**Admin Guide:** [ADMIN-GUIDE.md](ADMIN-GUIDE.md)
**Quick Start:** [QUICK-START.md](QUICK-START.md)

---

## Tech Stack

- **Frontend:** HTML, CSS (no framework needed!)
- **Admin Panel:** Python Flask
- **Hosting:** GitHub Pages (static)
- **Version Control:** Git

Simple, fast, and under your control. 🚀
