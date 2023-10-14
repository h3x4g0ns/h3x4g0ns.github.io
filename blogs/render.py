import markdown
import sys
from bs4 import BeautifulSoup

def parse_md_metadata(md_content):
    # Split the content based on '---' which indicates start/end of metadata
    parts = md_content.split('---')

    # If there's no '---' then assume no metadata is provided
    if len(parts) < 3:
        return None, md_content

    # The part between the first two '---' is considered metadata
    metadata_str = parts[1].strip()
    metadata = {}
    for line in metadata_str.split('\n'):
        key, value = line.split(':', 1)
        metadata[key.strip()] = value.strip()

    content_without_metadata = '---'.join(parts[2:]).strip()

    return metadata, content_without_metadata

def convert_md_to_html(md_file_path):
    with open(md_file_path, 'r', encoding="utf-8") as md_file:
        md_content = md_file.read()

    metadata, md_content_without_metadata = parse_md_metadata(md_content)
    title = metadata.get('title', 'Default Title')
    description = metadata.get('description', 'Default Description')
    date = metadata.get('date', 'Beginning of Time')

    html_content = markdown.markdown(md_content_without_metadata, extensions=["fenced_code", "codehilite", "meta", "nl2br"])

    # Post-process to add custom class to elements
    soup = BeautifulSoup(html_content, 'html.parser')
    for ul in soup.find_all('ul'):
        ul['class'] = 'mb-6 list-disc pl-5'
    for container in soup.find_all('h1'):
        container['class'] = 'text-2xl font-bold mb-2'
    for container in soup.find_all('h2'):
        container['class'] = 'text-xl font-bold mb-2'
    for container in soup.find_all('h3'):
        container['class'] = 'text-l font-bold mb-2'

    html_content = str(soup)

    # Updated template to include the parsed title and some formatting
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Blog Title</title>
        <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
        <script src="https://kit.fontawesome.com/a076d05399.js" crossorigin="anonymous"></script>
        <link href="https://cdn.jsdelivr.net/npm/prismjs@1.27.0/themes/prism.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/prismjs@1.27.0/prism.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.17.1/components/prism-python.min.js"></script>
    </head>
    <body class="min-h-screen flex items-center justify-center bg-gray-200 font-mono">

        <div class="bg-white p-8 rounded-lg shadow-md w-2/3">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-800">{title}</h1>
            <a href="../index.html" class="text-blue-400 hover:underline">Home</a>
        </div>
    
        <div class="mt-6">
            <h2 class="text-2xl font-bold mb-2 text-blue-600">{description}</h2>
            <h2 class="text-md font-bold mb-4 text-blue-400">{date}</h2>
            <div>
                {content}
            </div>

            <!-- Additional content, images, etc. can be added below. -->
        </div>

            <div class="mt-8">
                <h2 class="text-lg font-semibold mb-4 text-blue-600">Related Posts:</h2>
                <ul class="list-disc pl-5">
                    <li class="mb-2">
                        <a href="#" class="text-blue-400 hover:underline">Related Post 1</a>
                    </li>
                    <li class="mb-2">
                        <a href="#" class="text-blue-400 hover:underline">Related Post 2</a>
                    </li>
                </ul>
            </div>

            <div class="flex space-x-4 mt-8">
                <a href="https://github.com/yourusername" class="text-blue-500 hover:text-blue-600">
                <i class="fab fa-github fa-2x"></i>
                </a>
                <a href="https://linkedin.com/in/yourusername" class="text-blue-500 hover:text-blue-600">
                <i class="fab fa-linkedin fa-2x"></i>
                </a>
                <a href="https://twitter.com/yourusername" class="text-blue-500 hover:text-blue-600">
                <i class="fab fa-twitter fa-2x"></i>
                </a>
            </div>
            </div>

        </body>
        </html>
    """
    return html_template.format(title=title, 
                                description=description, 
                                date=date,
                                content=html_content)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python render.py input_markdown_file_path output_html_file_path")
        sys.exit(1)

    md_file_path = sys.argv[1]
    output_html_path = sys.argv[2]

    html_output = convert_md_to_html(md_file_path)
    soup = BeautifulSoup(html_output, 'html.parser')
    beautified_html = soup.prettify()

    with open(output_html_path, 'w', encoding="utf-8") as html_file:
        html_file.write(beautified_html)

    print(f"HTML file saved to {output_html_path}.")

