#!/usr/bin/env python3
"""
Automatically updates index.html with the latest post
Usage: python update-index.py
"""

import os
import re
from datetime import datetime

def get_latest_post():
    """Find the most recently created post file"""
    posts_dir = "posts"
    post_files = [f for f in os.listdir(posts_dir) if f.endswith('.html') and f != 'post-template.html']

    if not post_files:
        print("No posts found!")
        return None

    # Sort by modification time
    post_files.sort(key=lambda x: os.path.getmtime(os.path.join(posts_dir, x)), reverse=True)
    return post_files[0]

def extract_post_info(post_file):
    """Extract title, date, and excerpt from the post HTML"""
    with open(f"posts/{post_file}", 'r') as f:
        content = f.read()

    # Extract title
    title_match = re.search(r'<h1>(.*?)</h1>', content)
    title = title_match.group(1) if title_match else "Untitled"

    # Extract date
    date_match = re.search(r'<time datetime="(.*?)">(.*?)</time>', content)
    date_str = date_match.group(1) if date_match else datetime.now().strftime("%Y-%m-%d")
    date_display = date_match.group(2) if date_match else datetime.now().strftime("%B %d, %Y")

    # Create excerpt from first paragraph
    excerpt_match = re.search(r'<h2>Problem</h2>\s*<p>(.*?)</p>', content)
    excerpt = excerpt_match.group(1) if excerpt_match else "New AI use case"
    if len(excerpt) > 100:
        excerpt = excerpt[:100] + "..."

    return {
        'file': post_file,
        'title': title,
        'date': date_str,
        'date_display': date_display,
        'excerpt': excerpt
    }

def update_index(post_info):
    """Add the post to index.html"""
    with open('index.html', 'r') as f:
        content = f.read()

    # Create new post entry
    new_entry = f"""                <article class="post-preview">
                    <time datetime="{post_info['date']}">{post_info['date_display']}</time>
                    <h2><a href="posts/{post_info['file']}">{post_info['title']}</a></h2>
                    <p class="excerpt">{post_info['excerpt']}</p>
                </article>

                <!-- Your posts will appear here. Add them as you write daily -->"""

    # Replace the placeholder comment
    updated_content = content.replace(
        '                <!-- Your posts will appear here. Add them as you write daily -->',
        new_entry
    )

    # Write back
    with open('index.html', 'w') as f:
        f.write(updated_content)

    print(f"✓ Updated index.html with: {post_info['title']}")

if __name__ == "__main__":
    latest_post = get_latest_post()
    if latest_post:
        post_info = extract_post_info(latest_post)
        update_index(post_info)
        print(f"\n✓ Done! Your blog is updated.")
        print(f"  Open index.html to see the new post.")
