#!/usr/bin/env python3
"""
update_index.py

Rebuild the Apex registry index.  This script scans the repository for
epic directories, task files and handoff files, then produces a Markdown
registry under `apex-meta/registry/index.md`.  It can run in dry-run mode
to preview the output without writing.

The index groups pages into three types:
  * **Epics** – each slug directory under `apex-meta/epics/`.  The slug
    name is listed along with the count of tasks it contains.
  * **Tasks** – each Markdown file under an epic directory.  The index
    includes the epic slug, task ID (derived from the filename or front‑matter
    `id`), title, status and priority.
  * **Handoff** – each Markdown file under `apex-meta/handoff/`.

When invoked with `--dry-run`, the script prints the generated index to
stdout instead of writing to disk.  Otherwise it writes the index to
`apex-meta/registry/index.md`, creating the directory if necessary.

This script never modifies any other files.
"""
import argparse
import datetime
from datetime import timezone
import os
import sys
from typing import Dict, List, Tuple
import yaml

def read_frontmatter(path: str) -> Dict[str, any]:
    """Parse YAML front‑matter from a Markdown file.  Return an empty dict if
    parsing fails."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return {}
    start = None
    end = None
    for i, line in enumerate(lines):
        if line.strip() == '---':
            if start is None:
                start = i
            else:
                end = i
                break
    if start is None or end is None or end <= start + 1:
        return {}
    yaml_text = ''.join(lines[start+1:end])
    try:
        data = yaml.safe_load(yaml_text) or {}
    except Exception:
        data = {}
    return data

def scan_repository(repo_root: str) -> Tuple[Dict[str, List[Dict[str, any]]], List[str]]:
    """Scan the apex-meta directory for epics and handoff files.

    Returns a mapping of slug -> list of task records and a list of handoff
    file names relative to apex-meta.
    """
    apex_meta = os.path.join(repo_root, 'apex-meta')
    epics_root = os.path.join(apex_meta, 'epics')
    handoff_root = os.path.join(apex_meta, 'handoff')
    epics: Dict[str, List[Dict[str, any]]] = {}
    # Scan epics and tasks
    if os.path.isdir(epics_root):
        for slug in sorted(os.listdir(epics_root)):
            slug_path = os.path.join(epics_root, slug)
            if not os.path.isdir(slug_path):
                continue
            tasks: List[Dict[str, any]] = []
            for fname in sorted(os.listdir(slug_path)):
                if not fname.endswith('.md'):
                    continue
                path = os.path.join(slug_path, fname)
                fm = read_frontmatter(path)
                # derive id from front‑matter or filename
                tid = None
                if 'id' in fm:
                    try:
                        tid = int(fm['id'])
                    except Exception:
                        pass
                if tid is None:
                    stem = os.path.splitext(fname)[0]
                    try:
                        tid = int(stem)
                    except Exception:
                        tid = stem
                title = fm.get('name') or fm.get('title') or f"Task {tid}"
                status = fm.get('status') or ''
                priority = fm.get('priority') or ''
                tasks.append({
                    'id': tid,
                    'title': title,
                    'status': status,
                    'priority': priority,
                    'slug': slug,
                    'filename': fname,
                })
            epics[slug] = tasks
    # Scan handoff files
    handoff: List[str] = []
    if os.path.isdir(handoff_root):
        for fname in sorted(os.listdir(handoff_root)):
            if fname.endswith('.md'):
                handoff.append(fname)
    return epics, handoff

def build_index(epics: Dict[str, List[Dict[str, any]]], handoff: List[str]) -> str:
    """Construct the markdown contents for the index file."""
    # Use timezone-aware UTC timestamp
    timestamp = datetime.datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    lines = []
    lines.append('---')
    lines.append(f"generated: {timestamp}")
    lines.append('---')
    lines.append('')
    lines.append('# Apex Registry')
    lines.append('')
    # Epics section
    lines.append('## Epics')
    if not epics:
        lines.append('No epics found.')
    else:
        for slug, tasks in epics.items():
            lines.append(f"- {slug} ({len(tasks)} tasks)")
    lines.append('')
    # Tasks section
    lines.append('## Tasks')
    any_tasks = any(len(tasks) > 0 for tasks in epics.values())
    if not any_tasks:
        lines.append('No tasks found.')
    else:
        lines.append('| Epic | ID | Title | Status | Priority |')
        lines.append('| --- | --- | --- | --- | --- |')
        for slug, tasks in epics.items():
            for task in tasks:
                tid = task['id']
                title = task['title'].replace('|', '\\|')  # escape pipe
                status = task['status']
                priority = task['priority']
                lines.append(f"| {slug} | {tid} | {title} | {status} | {priority} |")
    lines.append('')
    # Handoff section
    lines.append('## Handoff')
    if not handoff:
        lines.append('No handoff files found.')
    else:
        for fname in handoff:
            lines.append(f"- {fname}")
    lines.append('')
    return '\n'.join(lines)

def write_index(repo_root: str, content: str):
    """Write the index content to apex-meta/registry/index.md, ensuring the directory exists."""
    registry_dir = os.path.join(repo_root, 'apex-meta', 'registry')
    os.makedirs(registry_dir, exist_ok=True)
    out_path = os.path.join(registry_dir, 'index.md')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    parser = argparse.ArgumentParser(description='Rebuild Apex registry index.')
    parser.add_argument('--dry-run', action='store_true', help='Preview the generated index without writing to disk')
    args = parser.parse_args()
    # Determine repo root relative to this script
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    epics, handoff = scan_repository(repo_root)
    index_md = build_index(epics, handoff)
    if args.dry_run:
        print(index_md)
    else:
        write_index(repo_root, index_md)
        print(f"Index written to {os.path.join('apex-meta', 'registry', 'index.md')}")

if __name__ == '__main__':
    main()