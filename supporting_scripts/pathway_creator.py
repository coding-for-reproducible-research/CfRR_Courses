import os
import re
import nbformat
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='Combine multiple Jupyter notebooks and Markdown files into a single notebook.')
parser.add_argument('files', nargs='+', help='List of notebook and markdown file paths to combine.')
parser.add_argument('--dest_dir', type=str, required=True, help='Destination directory where the combined notebook will be saved.')
parser.add_argument('--output_name', type=str, required=True, help='Name of the output combined notebook file.')

# Parse arguments
args = parser.parse_args()

# Create a list of dictionaries for the file paths
notebooks_info = [{'path': path} for path in args.files]

# Define the destination directory and output file name
dest_dir = args.dest_dir
output_name = args.output_name

# Create a new notebook
combined_notebook = new_notebook()

# Load a notebook or markdown file
def load_notebook(path):
    with open(path, 'r', encoding='utf-8') as f:
        return nbformat.read(f, as_version=4)

# Add markdown from a .md file
def add_markdown_from_file(path, original_dir):
    with open(path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    modified_md = adjust_paths_in_text(md_content, original_dir)
    combined_notebook.cells.append(new_markdown_cell(modified_md))

# Adjust file paths in text (code or markdown)
def adjust_paths_in_text(text, original_dir):
    # Regular expressions to find file paths
    file_path_patterns = [
        r'(!\[[^\]]*\]\((?!http)(.*?)\))',  # Markdown image paths
        r'(\[[^\]]*\]\((?!http)(.*?)\))',   # Markdown link paths
        r'(\"(.*?)\")'                     # General paths in quotes
    ]

    # Function to replace path
    def replace_path(match):
        full_match = match.group(0)
        path = match.group(2)
        if os.path.isfile(os.path.join(original_dir, path)):  # Check if the path is a file
            relative_path = os.path.relpath(os.path.join(original_dir, path), dest_dir)
            return full_match.replace(path, relative_path)
        return full_match

    # Replace all found paths using the patterns
    for pattern in file_path_patterns:
        text = re.sub(pattern, replace_path, text, flags=re.IGNORECASE)

    return text

# Iterate over the files
for item in notebooks_info:
    path = item['path']
    dir_path = os.path.dirname(path)
    if path.endswith('.ipynb'):
        nb = load_notebook(path)
        for cell in nb.cells:
            if cell.cell_type == 'code':
                modified_code = adjust_paths_in_text(cell.source, dir_path)
                combined_notebook.cells.append(new_code_cell(modified_code))
            elif cell.cell_type == 'markdown':
                modified_markdown = adjust_paths_in_text(cell.source, dir_path)
                combined_notebook.cells.append(new_markdown_cell(modified_markdown))
    elif path.endswith('.md'):
        add_markdown_from_file(path, dir_path)

# Write the combined notebook to a new file
combined_path = os.path.join(dest_dir, output_name)
with open(combined_path, 'w', encoding='utf-8') as f:
    nbformat.write(combined_notebook, f)

print(f"Notebook combined successfully into '{combined_path}'")
