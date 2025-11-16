#!/usr/bin/env python3
"""
Web-based admin panel for 0-2-1 blog
Run: python admin.py
Access: http://localhost:5000
"""

from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import re
from datetime import datetime
from pathlib import Path

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'images'

def parse_post_html(filepath):
    """Extract content from HTML post file"""
    with open(filepath, 'r') as f:
        content = f.read()

    # Extract title
    title_match = re.search(r'<h1>(.*?)</h1>', content)
    title = title_match.group(1) if title_match else ""

    # Extract date
    date_match = re.search(r'<time datetime="(.*?)">(.*?)</time>', content)
    date = date_match.group(1) if date_match else ""

    # Extract sections
    problem_match = re.search(r'<h2>Problem</h2>\s*<p>(.*?)</p>', content, re.DOTALL)
    problem = problem_match.group(1).strip() if problem_match else ""

    arch_match = re.search(r'<h2>System Architecture</h2>\s*<p>(.*?)</p>', content, re.DOTALL)
    architecture = arch_match.group(1).strip() if arch_match else ""

    solution_match = re.search(r'<h2>Solution</h2>\s*<p>(.*?)</p>', content, re.DOTALL)
    solution = solution_match.group(1).strip() if solution_match else ""

    # Extract examples (list items)
    examples = []
    examples_section = re.search(r'<h2>Examples</h2>\s*<ul>(.*?)</ul>', content, re.DOTALL)
    if examples_section:
        li_items = re.findall(r'<li>(.*?)</li>', examples_section.group(1))
        examples = [item.strip() for item in li_items]

    # Extract diagram if exists
    diagram_match = re.search(r'<img src="../images/(.*?)"', content)
    diagram = diagram_match.group(1) if diagram_match else ""

    return {
        'title': title,
        'date': date,
        'problem': problem,
        'architecture': architecture,
        'solution': solution,
        'examples': examples,
        'diagram': diagram
    }

def get_all_posts():
    """Get list of all blog posts"""
    posts = []
    posts_dir = Path('posts')

    for html_file in posts_dir.glob('*.html'):
        if html_file.name == 'post-template.html':
            continue

        try:
            data = parse_post_html(html_file)
            posts.append({
                'filename': html_file.name,
                'title': data['title'],
                'date': data['date']
            })
        except Exception as e:
            print(f"Error parsing {html_file}: {e}")

    # Sort by date (newest first)
    posts.sort(key=lambda x: x['date'], reverse=True)
    return posts

def save_post_html(filename, data):
    """Save updated post data back to HTML file"""
    filepath = f"posts/{filename}"

    # Build examples HTML
    examples_html = "\n".join([f"                <li>{ex}</li>" for ex in data['examples']])

    # Build diagram HTML
    diagram_html = f'<img src="../images/{data["diagram"]}" alt="System Architecture Diagram">' if data['diagram'] else ''

    date_obj = datetime.strptime(data['date'], "%Y-%m-%d")
    date_display = date_obj.strftime("%B %d, %Y")

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data['title']} - 0-2-1</title>
    <link rel="stylesheet" href="../styles.css">
</head>
<body class="post-page">
    <div class="post-content">
        <div class="post-header">
            <a href="../index.html" class="back-link">← Back to all posts</a>
            <time datetime="{data['date']}">{date_display}</time>
            <h1>{data['title']}</h1>
        </div>

        <div class="post-body">
            <h2>Problem</h2>
            <p>{data['problem']}</p>

            <h2>System Architecture</h2>
            <p>{data['architecture']}</p>
            {diagram_html}

            <h2>Solution</h2>
            <p>{data['solution']}</p>

            <h2>Examples</h2>
            <ul>
{examples_html}
            </ul>
        </div>
    </div>
</body>
</html>
"""

    with open(filepath, 'w') as f:
        f.write(html_content)

@app.route('/')
def index():
    """Admin dashboard - list all posts"""
    posts = get_all_posts()
    return render_template('admin.html', posts=posts)

@app.route('/edit/<filename>')
def edit_post(filename):
    """Edit a specific post"""
    filepath = f"posts/{filename}"
    if not os.path.exists(filepath):
        return "Post not found", 404

    data = parse_post_html(filepath)
    data['filename'] = filename
    return render_template('edit-post.html', post=data)

@app.route('/save/<filename>', methods=['POST'])
def save_post(filename):
    """Save edited post"""
    data = {
        'title': request.form['title'],
        'date': request.form['date'],
        'problem': request.form['problem'],
        'architecture': request.form['architecture'],
        'solution': request.form['solution'],
        'examples': [ex.strip() for ex in request.form['examples'].split('\n') if ex.strip()],
        'diagram': request.form.get('diagram', '')
    }

    save_post_html(filename, data)
    return redirect(url_for('index'))

@app.route('/view/<filename>')
def view_post(filename):
    """View a post by serving the HTML file with fixed paths"""
    filepath = f"posts/{filename}"
    if not os.path.exists(filepath):
        return "Post not found", 404

    with open(filepath, 'r') as f:
        content = f.read()

    # Fix relative paths to work with Flask routing
    content = content.replace('href="../styles.css"', 'href="/styles.css"')
    content = content.replace('href="../index.html"', 'href="/"')  # Back to admin dashboard
    content = content.replace('src="../images/', 'src="/images/')

    return content

@app.route('/view-site')
def view_site():
    """View the main site with fixed links"""
    with open('index.html', 'r') as f:
        content = f.read()

    # Fix post links to use Flask routes
    content = content.replace('href="posts/', 'href="/view/')
    content = content.replace('href="index.html"', 'href="/view-site"')

    return content

@app.route('/styles.css')
def serve_styles():
    """Serve the main CSS file"""
    with open('styles.css', 'r') as f:
        content = f.read()
    return content, 200, {'Content-Type': 'text/css'}

@app.route('/images/<path:filename>')
def serve_image(filename):
    """Serve images"""
    from flask import send_from_directory
    return send_from_directory('images', filename)

@app.route('/upload', methods=['POST'])
def upload_image():
    """Upload diagram image"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No filename'}), 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    return jsonify({'filename': file.filename})

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)

    print("\n" + "="*50)
    print("  0-2-1 Admin Panel")
    print("="*50)
    print("\n  📝 Admin URL: http://localhost:8080")
    print("  🔧 Edit your blog posts through your browser")
    print("\n  Press Ctrl+C to stop the server\n")

    app.run(debug=True, port=8080, host='127.0.0.1')
