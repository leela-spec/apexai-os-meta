#!/usr/bin/env python3
"""
show_blocked.py

Identify tasks that are blocked because their dependencies are not complete.

This script scans Markdown files under `apex-meta/epics/` for YAML
front‑matter.  For each task with a non‑empty `depends_on` list, it checks
whether any referenced task has a status other than `done` (or if the
dependency cannot be found).  Tasks meeting this criterion are reported as
blocked along with the IDs of the tasks that are causing the block.

Output:
    A table to stdout with columns: id | blocked_by ids | title

This script never modifies any files.
"""
import os
import sys
import yaml

def read_frontmatter(md_path):
    """Read YAML front‑matter from a Markdown file and return it as a dict."""
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
    yaml_text = ''.join(lines[start+1:end])
    try:
        data = yaml.safe_load(yaml_text) or {}
    except Exception as exc:
        print(f"Warning: failed to parse YAML in {md_path}: {exc}", file=sys.stderr)
        return None
    return data

def scan_tasks(epics_root):
    """Traverse the epics directory to collect tasks into a dict."""
    tasks = {}
    for root, _dirs, files in os.walk(epics_root):
        for fname in files:
            if not fname.endswith('.md'):
                continue
            path = os.path.join(root, fname)
            fm = read_frontmatter(path)
            if not fm:
                continue
            # Determine ID: from front‑matter 'id' if possible, otherwise from filename
            task_id = None
            if 'id' in fm:
                try:
                    task_id = int(fm['id'])
                except Exception:
                    pass
            if task_id is None:
                stem = os.path.splitext(fname)[0]
                try:
                    task_id = int(stem)
                except Exception:
                    task_id = abs(hash(path)) % (10**6)
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

def find_blocked_tasks(tasks):
    """Return a list of blocked tasks with lists of blocker IDs."""
    blocked = []
    for task_id, record in tasks.items():
        deps = record['depends_on']
        if not deps:
            continue  # no dependencies -> not blocked
        blockers = []
        for dep_id in deps:
            dep = tasks.get(dep_id)
            # blocked if dependency missing or status not 'done'
            if not dep or dep['status'] != 'done':
                blockers.append(dep_id)
        if blockers:
            blocked.append({
                'id': task_id,
                'title': record['title'],
                'blocked_by': blockers,
            })
    # Sort by number of blockers descending, then id ascending
    blocked.sort(key=lambda r: (-len(r['blocked_by']), r['id']))
    return blocked

def print_blocked(blocked_tasks):
    if not blocked_tasks:
        print("No blocked tasks found.")
        return
    print(f"{'ID':<6} | {'Blocked By':<20} | Title")
    print("-" * 60)
    for rec in blocked_tasks:
        blockers_str = ', '.join(str(b) for b in rec['blocked_by'])
        print(f"{rec['id']:<6} | {blockers_str:<20} | {rec['title']}")

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