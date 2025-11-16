# Quick Start Guide - AI Cases Archive

## Writing a New Blog Post (Super Simple!)

### Method 1: Use the Python Script (Easiest)

```bash
# Run the post creator
python create-post.py
```

It will ask you questions:
- Post number (001, 002, etc.)
- Title
- Date (or press Enter for today)
- Problem description
- Architecture description
- Solution
- Examples
- Background image name
- Diagram name (optional)

Then automatically run:
```bash
python update-index.py
```

Done! Your blog post is live.

---

## Adding Images & Diagrams

### Step 1: Save Your Images

Put all images in the `images/` folder:

```
images/
  ├── background-001.jpg    (your background images)
  ├── background-002.jpg
  ├── diagram-001.png       (your architecture diagrams)
  └── diagram-002.png
```

### Step 2: Reference in Your Post

**For background images:**
- The script asks for the filename
- It will automatically add it as background

**For diagrams in your post:**
- Save diagram as `diagram-001.png` in `images/` folder
- The script asks for the diagram filename
- It automatically adds it to your post

---

## Example Workflow

```bash
# Day 1
python create-post.py
# Answer questions...
# Post number: 001
# Title: RAG-based Customer Support Agent
# Background: background-retro.jpg
# Diagram: rag-architecture.png

python update-index.py

# Open in browser
open index.html
```

---

## Creating Diagrams

You can create diagrams using:

1. **Draw.io** (diagrams.net) - Free online tool
2. **Excalidraw** - Simple sketching tool
3. **Figma** - Professional design tool
4. **Mermaid** - Text-based diagrams
5. **Screenshot** - Just draw on paper and take a photo!

Save as PNG or JPG in the `images/` folder.

---

## File Structure

```
/
├── create-post.py          ← Run this to create posts
├── update-index.py         ← Run this to update homepage
├── index.html              ← Your homepage (auto-updated)
├── styles.css              ← Don't touch this
├── posts/
│   ├── 001-my-post.html    ← Generated automatically
│   └── 002-next-post.html
└── images/
    ├── background-001.jpg  ← Your backgrounds
    └── diagram-001.png     ← Your diagrams
```

---

## Even Simpler: One Command

Want to make it even easier? Run this:

```bash
python create-post.py && python update-index.py && open index.html
```

This will:
1. Create your post
2. Update the homepage
3. Open it in your browser

All in one command!
