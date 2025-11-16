# AI Cases Archive

A minimalist blog for daily AI use case documentation.

## How to Add a New Post

### 1. Create Your Post

1. Copy the template from `posts/post-template.html`
2. Rename it (e.g., `posts/001-your-post-name.html`)
3. Edit the content:
   - Update the `<title>` tag
   - Change the background image path in the `<style>` section
   - Update the date in `<time datetime="YYYY-MM-DD">`
   - Add your title in `<h1>`
   - Fill in your content (Problem, Architecture, Solution, Examples)

### 2. Add Background Image

1. Save your background image in the `images/` folder
2. Reference it in the post's inline style:
   ```css
   background-image: url('../images/your-background.jpg');
   ```

### 3. Update Index Page

1. Open `index.html`
2. Add a new post preview in the `<section class="posts">` section:

```html
<article class="post-preview">
    <time datetime="2025-10-19">October 19, 2025</time>
    <h2><a href="posts/001-your-post.html">Your Post Title</a></h2>
    <p class="excerpt">Brief description of the post...</p>
</article>
```

## File Structure

```
/
├── index.html          # Homepage with post list
├── styles.css          # Global styles (terminal theme)
├── README.md           # This file
├── posts/
│   ├── post-template.html  # Template for new posts
│   └── 001-example.html    # Your actual posts
└── images/
    ├── background-001.jpg  # Background images
    └── diagram-001.png     # Architecture diagrams
```

## Publishing to GitHub Pages

1. Create a new GitHub repository
2. Push this code to the repository
3. Go to Settings → Pages
4. Select "main" branch and "/" root folder
5. Save and wait for deployment
6. Your site will be live at `https://yourusername.github.io/repository-name`

## Terminal Color Scheme

The site uses a terminal-inspired green color scheme:
- Background: `#0a0f0d` (dark greenish-black)
- Primary text: `#5ff967` (bright green)
- Secondary text: `#3ea84a` (muted green)
- Accent: `#7ffb88` (light green for hovers)
