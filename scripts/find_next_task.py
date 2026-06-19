#!/usr/bin/env python3
"""
find_next_task.py

Scan Apex task files and produce a ranked list of actionable tasks.  An
actionable task is one whose dependencies (if any) are all marked as done.

The script searches for Markdown files under `apex-meta/epics/` with YAML
front‑matter containing the fields described in the Apex field schema.  It
expects each file to define at least a name/title, status, priority, and
depends_on list.  If a file is missing or its front‑matter cannot be parsed,
the script logs a warning and skips it.

Output:
    A table to stdout with columns: id | priority | dep_count | title

This script never modifies any files.
"""
import os
import sys
import yaml

# Map textual priority to numeric weight
PRIORITY_WEIGHTS = {
    'high': 3,
    'medium': 2,
    'low': 1,
}

def read_frontmatter(md_path):
    """Extract YAML front‑matter from a Markdown file.

    Returns a dictionary of front‑matter keys, or None if parsing fails.
    """
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Warning: file not found: {md_path}", file=sys.stderr)
        return None
    # Find the first two '---' lines to delimit front‑matter
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
        return data
    except Exception as exc:
        print(f"Warning: failed to parse YAML in {md_path}: {exc}", file=sys.stderr)
        return None

def scan_tasks(epics_root):
    """Traverse epics_root for Markdown task files and return a task dict.

    Returns a dict mapping task id (int) to a task record dict with keys:
        'id': int
        'title': str
        'status': str
        'priority': str
        'depends_on': list of ints
    """
    tasks = {}
    for root, _dirs, files in os.walk(epics_root):
        for filename in files:
            if not filename.endswith('.md'):
                continue
            md_path = os.path.join(root, filename)
            fm = read_frontmatter(md_path)
            if not fm:
                continue
            # derive id: use front‑matter 'id' if present, else filename stem
            task_id = None
            if 'id' in fm:
                try:
                    task_id = int(fm['id'])
                except Exception:
                    pass
            if task_id is None:
                stem = os.path.splitext(os.path.basename(filename))[0]
                try:
                    task_id = int(stem)
                except Exception:
                    # derive numeric ID by hashing path
                    task_id = abs(hash(md_path)) % (10**6)
            # fetch other fields
            status = (fm.get('status') or '').strip().lower()
            priority = (fm.get('priority') or 'medium').strip().lower()
            depends_raw = fm.get('depends_on', [])
            if depends_raw is None:
                depends_raw = []
            if isinstance(depends_raw, int):
                depends_list = [depends_raw]
            elif isinstance(depends_raw, list):
                # filter ints only
                depends_list = []
                for d in depends_raw:
                    try:
                        depends_list.append(int(d))
                    except Exception:
                        continue
            else:
                depends_list = []
            title = fm.get('name') or fm.get('title') or f"Task {task_id}"
            tasks[task_id] = {
                'id': task_id,
                'title': title,
                'status': status,
                'priority': priority,
                'depends_on': depends_list,
            }
    return tasks

def compute_actionable_tasks(tasks):
    """Return a list of actionable tasks with computed metrics.

    A task is actionable if all its dependencies (if any) exist in `tasks` and
    have status equal to 'done'.
    Each returned record has:
        'id', 'title', 'priority', 'priority_weight', 'dep_count'
    """
    actionable = []
    for task_id, record in tasks.items():
        deps = record['depends_on']
        # Check dependencies
        blocked = False
        for dep_id in deps:
            dep = tasks.get(dep_id)
            if not dep or dep['status'] != 'done':
                blocked = True
                break
        if blocked:
            continue
        weight = PRIORITY_WEIGHTS.get(record['priority'], 2)
        actionable.append({
            'id': task_id,
            'title': record['title'],
            'priority': record['priority'],
            'priority_weight': weight,
            'dep_count': len(deps),
        })
    # Sort: highest weight first (descending), then by dep_count ascending, then id ascending
    actionable.sort(key=lambda r: (-r['priority_weight'], r['dep_count'], r['id']))
    return actionable

def print_table(records):
    """Print the ranked table to stdout."""
    if not records:
        print("No actionable tasks found.")
        return
    print(f"{'ID':<6} | {'Priority':<7} | {'Deps':<4} | Title")
    print("-" * 60)
    for r in records:
        print(f"{r['id']:<6} | {r['priority']:<7} | {r['dep_count']:<4} | {r['title']}")

def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    epics_root = os.path.join(repo_root, 'apex-meta', 'epics')
    if not os.path.isdir(epics_root):
        print(f"No epics directory found at {epics_root}", file=sys.stderr)
        print("No actionable tasks found.")
        return
    tasks = scan_tasks(epics_root)
    records = compute_actionable_tasks(tasks)
    print_table(records)

if __name__ == '__main__':
    main()