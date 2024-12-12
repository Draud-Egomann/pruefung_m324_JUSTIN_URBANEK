import markdown
import os

def markdown_to_html(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()

    html_content = markdown.markdown(md_content)

    full_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{os.path.splitext(os.path.basename(input_file))[0]}</title>
    <link rel="stylesheet" href="main.css">
</head>
<body>
    {html_content}
</body>
</html>
"""
    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(full_html)

    print(f"HTML file '{output_file}' successfully created or updated.")

if __name__ == "__main__":
    markdown_to_html('task-3.md', 'task-3.html')