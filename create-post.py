#!/usr/bin/env python3
"""
Simple blog post generator for 0-2-1
Usage: python create-post.py
"""

from datetime import datetime
import os

def create_post():
    print("=== 0-2-1 - New Post Creator ===\n")

    # Get post details
    post_number = input("Post number (e.g., 001, 002): ").strip()
    title = input("Post title: ").strip()
    date_str = input("Date (press Enter for today): ").strip()

    if not date_str:
        date_obj = datetime.now()
        date_str = date_obj.strftime("%Y-%m-%d")
        date_display = date_obj.strftime("%B %d, %Y")
    else:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        date_display = date_obj.strftime("%B %d, %Y")

    excerpt = input("Brief excerpt (1 sentence): ").strip()

    print("\n--- Now write your content ---")
    print("(Type your content for each section)\n")

    problem = input("PROBLEM: ").strip()
    architecture = input("ARCHITECTURE: ").strip()
    solution = input("SOLUTION: ").strip()

    print("\nExamples (one per line, type 'done' when finished):")
    examples = []
    while True:
        ex = input("  - ").strip()
        if ex.lower() == 'done':
            break
        if ex:
            examples.append(ex)

    # Optional diagram
    diagram = input("\nDiagram filename (in images/, or press Enter to skip): ").strip()

    # Create filename
    filename_slug = title.lower().replace(' ', '-').replace(':', '')
    post_filename = f"posts/{post_number}-{filename_slug}.html"

    # Generate HTML content
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - 0-2-1</title>
    <link rel="stylesheet" href="../styles.css">
</head>
<body class="post-page">
    <div class="post-content">
        <div class="post-header">
            <a href="../index.html" class="back-link">← Back to all posts</a>
            <time datetime="{date_str}">{date_display}</time>
            <h1>{title}</h1>
        </div>

        <div class="post-body">
            <h2>Problem</h2>
            <p>{problem}</p>

            <h2>System Architecture</h2>
            <p>{architecture}</p>
            {"<img src='../images/" + diagram + "' alt='System Architecture Diagram'>" if diagram else ""}

            <h2>Solution</h2>
            <p>{solution}</p>

            <h2>Examples</h2>
            <ul>
{"".join(f"                <li>{ex}</li>\n" for ex in examples)}            </ul>
        </div>
    </div>
</body>
</html>
"""

    # Write the post file
    with open(post_filename, 'w') as f:
        f.write(html_content)

    print(f"\n✓ Post created: {post_filename}")

    # Generate index.html entry
    index_entry = f"""                <article class="post-preview">
                    <time datetime="{date_str}">{date_display}</time>
                    <h2><a href="{post_filename.replace('posts/', 'posts/')}">{title}</a></h2>
                    <p class="excerpt">{excerpt}</p>
                </article>
"""

    print("\n--- Add this to index.html (in the <section class='posts'> section) ---")
    print(index_entry)
    print("\nOr run: python update-index.py")

if __name__ == "__main__":
    create_post()
