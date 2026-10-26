import re
from pathlib import Path

def split_markdown_cells(row: str):
    # Split on unescaped pipe |
    # regex: (?<!\\)\|
    cells = re.split(r'(?<!\\)\|', row)
    # strip whitespace and unescape \|
    clean = [c.strip().replace(r'\|', '|') for c in cells]
    # Remove leading and trailing empty elements from row boundary pipes
    if clean and clean[0] == '':
        clean.pop(0)
    if clean and clean[-1] == '':
        clean.pop()
    return clean

row = "| Creating, editing or validating a governed knowledge or specification file | Flat YAML frontmatter: every line has a colon, lists use inline brackets, never multiline dashes. Concept files declare `type, id, title, description, status`. Front-load critical rules; close on the failure-mode guard. Tag governed rules `[P0-P3 \| I/E/R]` 1-100, never combined. One responsibility per file. Link every file you list. Do not impose this on chat, code or logs. | `index.md` |"

cells = split_markdown_cells(row)
print("Cell count:", len(cells))
print("When:", cells[0])
print("Body:", cells[1])
print("Ref:", cells[2])
