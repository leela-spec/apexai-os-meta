#!/usr/bin/env python3
"""
drift_check.py

Detect registry drift between the current index and the expected index
generated from scanning the repository.  The script imports and reuses
functions from `update_index.py` to compute the expected set of files
that should appear in `apex-meta/registry/index.md`.  It then compares
this set against the files referenced in the existing index file.

Output:
    A report printed to stdout listing missing entries (files that should
    appear in the index but are absent) and orphan entries (paths listed
    in the index that do not exist in the repository).

This script never modifies any files.
"""
import os
import re
import sys
from typing import Set

try:
    # Import scan_repository from update_index in the same package
    from update_index import scan_repository
except Exception:
    # When executed directly, adjust sys.path to include script directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, current_dir)
    from update_index import scan_repository  # type: ignore

def expected_file_set(repo_root: str) -> Set[str]:
    """Compute the set of relative file paths expected to be listed in the index."""
    epics, handoff = scan_repository(repo_root)
    files: Set[str] = set()
    # tasks
    for slug, tasks in epics.items():
        for task in tasks:
            fname = task['filename']
            files.add(os.path.join('epics', slug, fname))
    # handoff
    for hf in handoff:
        files.add(os.path.join('handoff', hf))
    return files

def index_file_set(index_path: str) -> Set[str]:
    """Parse the existing index.md to extract referenced file paths."""
    files: Set[str] = set()
    if not os.path.isfile(index_path):
        return files
    with open(index_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    in_handoff_section = False
    in_tasks_section = False
    for line in lines:
        stripped = line.strip()
        # detect section headings
        if stripped.lower().startswith('## '):
            heading = stripped[3:].strip().lower()
            in_handoff_section = heading.startswith('handoff')
            in_tasks_section = heading.startswith('tasks')
            continue
        # parse handoff entries
        if in_handoff_section:
            m = re.match(r'^-\s*(\S+\.md)', stripped)
            if m:
                files.add(os.path.join('handoff', m.group(1)))
        # parse task table rows
        if in_tasks_section and stripped.startswith('|'):
            # expected format: | epic | id | title | status | priority |
            parts = [p.strip() for p in stripped.strip('|').split('|')]
            if len(parts) >= 2:
                slug = parts[0]
                tid = parts[1]
                # Derive file name
                # Accept numeric or string IDs; ensure md extension
                fname = f"{tid}.md"
                files.add(os.path.join('epics', slug, fname))
    return files

def print_report(missing: Set[str], orphan: Set[str]):
    """Print the drift report."""
    print("Drift report:")
    if not missing and not orphan:
        print("No drift detected. Index matches repository files.")
        return
    if missing:
        print("Missing from index:")
        for path in sorted(missing):
            print(f"- {path}")
    if orphan:
        print("Orphan entries in index:")
        for path in sorted(orphan):
            print(f"- {path}")

def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    index_path = os.path.join(repo_root, 'apex-meta', 'registry', 'index.md')
    expected = expected_file_set(repo_root)
    index_files = index_file_set(index_path)
    missing = expected - index_files
    orphan = index_files - expected
    print_report(missing, orphan)

if __name__ == '__main__':
    main()