#!/usr/bin/env python3
"""
stall_detect.py

Detect tasks that have not had a status change across multiple consecutive
session entries in `apex-meta/handoff/progress.md`.  A task is considered
stalled if its status remains unchanged for two or more consecutive sessions
at the end of the progress log.

The expected structure of `progress.md` is a series of session sections
introduced by headings (lines beginning with "## ").  Within each session,
task updates are listed in bullet form (lines starting with '-' or '*'),
including a task identifier, status and optional updated timestamp.  The
script attempts to extract these fields using simple pattern matching.

Output:
    A table printed to stdout with columns:
        id | last_updated | sessions_stalled | title
    If no stalled tasks are found, prints "No stalled tasks found.".

The script never modifies any files.
"""
import os
import re
import sys
from typing import Dict, List

SESSION_HEADER_RE = re.compile(r'^##\s+(.*)')
TASK_LINE_RE = re.compile(r'^[\-\*]\s*(?:\[?(\d+)\]?\s*[-:]\s*)?(.*?)\s*(?:status[:=]\s*(\w+))?\s*(?:updated[:=]\s*([^\s]+))?', re.IGNORECASE)

def parse_progress(path: str):
    """Parse the progress.md file into a list of sessions.

    Returns a list where each element is a dict mapping task_id to a tuple
    (status, updated, title).  Sessions are ordered as they appear in the file.
    """
    sessions: List[Dict[str, tuple]] = []
    if not os.path.isfile(path):
        return sessions
    with open(path, 'r', encoding='utf-8') as f:
        current: Dict[str, tuple] = {}
        for line in f:
            line = line.strip()
            if not line:
                continue
            header_match = SESSION_HEADER_RE.match(line)
            if header_match:
                # Start a new session
                if current:
                    sessions.append(current)
                    current = {}
                continue
            # Match task lines
            m = TASK_LINE_RE.match(line)
            if m:
                task_id, title, status, updated = m.groups()
                if not task_id:
                    # cannot determine id, skip
                    continue
                tid = task_id.strip()
                title = title.strip() if title else f"Task {tid}"
                status = status.strip().lower() if status else ''
                updated = updated.strip() if updated else ''
                current[tid] = (status, updated, title)
        if current:
            sessions.append(current)
    return sessions

def detect_stalled(sessions: List[Dict[str, tuple]]):
    """Return a dict of stalled tasks with (last_updated, sessions_stalled, title)."""
    stalled: Dict[str, tuple] = {}
    if not sessions or len(sessions) < 2:
        return stalled
    # Build status timeline per task
    timeline: Dict[str, List[str]] = {}
    updated_map: Dict[str, str] = {}
    title_map: Dict[str, str] = {}
    for session in sessions:
        for tid, (status, updated, title) in session.items():
            timeline.setdefault(tid, []).append(status)
            if updated:
                updated_map[tid] = updated
            if title:
                title_map[tid] = title
        # For tasks not mentioned in this session, append None to maintain alignment
        for tid in list(timeline.keys()):
            if tid not in session:
                timeline[tid].append(None)
    # Examine each task's status timeline from the end backwards
    for tid, statuses in timeline.items():
        # Skip tasks with only one session
        if len(statuses) < 2:
            continue
        # Count consecutive identical status values from the end (ignore None)
        count = 0
        last_status = None
        for st in reversed(statuses):
            if st is None:
                # no update in this session, break chain
                break
            if last_status is None:
                last_status = st
                count = 1
            elif st == last_status:
                count += 1
            else:
                break
        if count >= 2 and last_status:
            stalled[tid] = (updated_map.get(tid, ''), count, title_map.get(tid, f"Task {tid}"))
    return stalled

def print_stalled(stalled: Dict[str, tuple]):
    if not stalled:
        print("No stalled tasks found.")
        return
    print(f"{'ID':<6} | {'Last Updated':<20} | {'Sessions':<8} | Title")
    print("-" * 70)
    for tid, (updated, count, title) in sorted(stalled.items(), key=lambda x: x[0]):
        print(f"{tid:<6} | {updated:<20} | {count:<8} | {title}")

def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    progress_path = os.path.join(repo_root, 'apex-meta', 'handoff', 'progress.md')
    if not os.path.isfile(progress_path):
        print("No progress.md found. No stalled tasks.")
        return
    sessions = parse_progress(progress_path)
    stalled = detect_stalled(sessions)
    print_stalled(stalled)

if __name__ == '__main__':
    main()