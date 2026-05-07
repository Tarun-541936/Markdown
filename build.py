import os
import markdown

DOCS_DIR = "docs"
SITE_DIR = "site"

# Create site directory if missing
os.makedirs(SITE_DIR, exist_ok=True)

# Simple CSS
CSS = """
body {
    font-family: Arial, sans-serif;
    max-width: 800px;
    margin: 40px auto;
    line-height: 1.6;
    padding: 20px;
    color: #333;
}

code {
    background: #f4f4f4;
    padding: 2px 4px;
}

pre {
    background: #f4f4f4;
    padding: 10px;
    overflow-x: auto;
}

a {
    color: #0366d6;
}
"""

# Write stylesheet
with open(os.path.join(SITE_DIR, "style.css"), "w") as f:
    f.write(CSS)

links = []

# Convert markdown files
for filename in os.listdir(DOCS_DIR):

    if filename.endswith(".md"):

        md_path = os.path.join(DOCS_DIR, filename)

        with open(md_path, "r", encoding="utf-8") as f:
            md_content = f.read()

        html_content = markdown.markdown(md_content)

        title = filename.replace(".md", "")

        full_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    {html_content}
</body>
</html>
"""

        html_filename = filename.replace(".md", ".html")

        output_path = os.path.join(SITE_DIR, html_filename)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(full_html)

        links.append(
            f'<li><a href="{html_filename}">{title}</a></li>'
        )

# Generate index.html
index_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Documentation</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Documentation</h1>

    <ul>
        {''.join(links)}
    </ul>
</body>
</html>
"""

with open(os.path.join(SITE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

print("Site generated successfully!")