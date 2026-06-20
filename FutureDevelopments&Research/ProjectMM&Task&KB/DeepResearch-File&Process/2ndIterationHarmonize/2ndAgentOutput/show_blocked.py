#!/usr/bin/env python3
"""
show_blocked.py

Identify tasks that are blocked because their dependencies are missing or not
complete.

The script scans Markdown files under ``apex-meta/epics/`` for YAML front‑
matter, as defined by the Apex field schema.  For each task with a non‑empty
``depends_on`` list, it checks each referenced task ID:

- If the dependency does not exist in the scanned tasks, the task is blocked
  by that missing dependency.
- If the dependency exists but its status is not ``done``, the task is blocked
  by an incomplete dependency.

Dependencies are reported separately as missing or incomplete so that
operators can distinguish configuration errors (missing files) from work in
progress (incomplete dependencies).

Output:
    A table to stdout with columns: id | Missing Deps | Incomplete Deps | title

Notes:
    This script requires the ``PyYAML`` package (via ``yaml.safe_load``) to
    parse YAML front‑matter.  Install it with ``pip install pyyaml`` if not
    already available.

This script never modifies any files.
"""

import os
import sys
import yaml


def read_frontmatter(md_path: str):
    """Read YAML front‑matter from a Markdown file and return it as a dict.

    Returns ``None`` on error.
    """
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Warning: file not found: {md_path}", file=sys.stderr)
        return None
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
        print(f"Warning: no valid YAML front‑matter in {md_path}", file=sys.stderr)
        return None
    yaml_text = ''.join(lines[start + 1:end])
    try:
        data = yaml.safe_load(yaml_text) or {}
        return data
    except Exception as exc:
        print(f"Warning: failed to parse YAML in {md_path}: {exc}", file=sys.stderr)
        return None

def scan_tasks(epics_root: str):
    """Traverse the epics directory to collect tasks into a dict.

    Only tasks with a numeric ``id`` from front‑matter or a purely numeric
    filename are included.  Tasks lacking a numeric identifier are skipped.

    Returns a mapping from task id to a record dict with keys:
        'id', 'title', 'status', 'depends_on'
    """
    tasks: dict[int, dict] = {}
    for root, _dirs, files in os.walk(epics_root):
        for fname in files:
            if not fname.endswith('.md'):
                continue
            path = os.path.join(root, fname)
            fm = read_frontmatter(path)
            if not fm:
                continue
            # Determine ID: from front‑matter 'id' if possible, otherwise from filename
            task_id: int | None = None
            if 'id' in fm:
                try:
                    task_id = int(fm['id'])
                except Exception:
                    pass
            if task_id is None:
                stem = os.path.splitext(fname)[0]
                if stem.isdigit():
                    task_id = int(stem)
            if task_id is None:
                print(
                    f"Warning: could not determine numeric id for {path}; skipping",
                    file=sys.stderr,
                )
                continue
            status = (fm.get('status') or '').strip().lower()
            depends_raw = fm.get('depends_on', [])
            if depends_raw is None:
                depends_raw = []
            if isinstance(depends_raw, int):
                depends_list = [depends_raw]
            elif isinstance(depends_raw, list):
                depends_list = []
                for dep in depends_raw:
                    try:
                        depends_list.append(int(dep))
                    except Exception:
                        continue
            else:
                depends_list = []
            title = fm.get('name') or fm.get('title') or f"Task {task_id}"
            tasks[task_id] = {
                'id': task_id,
                'title': title,
                'status': status,
                'depends_on': depends_list,
            }
    return tasks

def find_blocked_tasks(tasks: dict[int, dict]):
    """Return a list of blocked tasks with missing and incomplete blocker lists.

    Each returned record has keys:
        'id': int
        'title': str
        'missing': list[int]    # dependency IDs that are missing from tasks
        'incomplete': list[int] # dependency IDs whose status is not 'done'
    """
    blocked: list[dict] = []
    for task_id, record in tasks.items():
        deps = record['depends_on']
        if not deps:
            continue  # no dependencies -> not blocked
        missing: list[int] = []
        incomplete: list[int] = []
        for dep_id in deps:
            dep = tasks.get(dep_id)
            if dep is None:
                missing.append(dep_id)
            else:
                if dep['status'] != 'done':
                    incomplete.append(dep_id)
        if missing or incomplete:
            blocked.append(
                {
                    'id': task_id,
                    'title': record['title'],
                    'missing': sorted(missing),
                    'incomplete': sorted(incomplete),
                }
            )
    # Sort deterministically: tasks with more total blockers first, then by id
    blocked.sort(key=lambda r: (-(len(r['missing']) + len(r['incomplete'])), r['id']))
    return blocked

def print_blocked(blocked_tasks: list[dict]):
    """Print the blocked tasks in a table format."""
    if not blocked_tasks:
        print("No blocked tasks found.")
        return
    print(f"{'ID':<6} | {'Missing Deps':<15} | {'Incomplete Deps':<20} | Title")
    print("-" * 80)
    for rec in blocked_tasks:
        missing_str = ', '.join(str(d) for d in rec['missing']) if rec['missing'] else '-'  # dash if none
        incomplete_str = ', '.join(str(d) for d in rec['incomplete']) if rec['incomplete'] else '-'
        print(
            f"{rec['id']:<6} | {missing_str:<15} | {incomplete_str:<20} | {rec['title']}"
        )

def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    epics_root = os.path.join(repo_root, 'apex-meta', 'epics')
    if not os.path.isdir(epics_root):
        print(f"No epics directory found at {epics_root}", file=sys.stderr)
        print("No blocked tasks found.")
        return
    tasks = scan_tasks(epics_root)
    blocked_tasks = find_blocked_tasks(tasks)
    print_blocked(blocked_tasks)


if __name__ == '__main__':
    main()
