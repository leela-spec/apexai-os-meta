[STATE_BLOCK v1.0]
PURPOSE: replace chat history as session context

FORMAT:
---
STATE:
  project: {PROJECT_NAME}
  completed_tasks:
    - TASK-01: {filename} | status: done | date: {YYYY-MM-DD}
    - TASK-02: {filename} | status: done | date: {YYYY-MM-DD}
  active_constraints:
    - mode: move-only
    - output: single-artifact-per-response
    - forbidden: [restructure, expand, rewrite]
  open_items:
    - TASK-03: {description} | status: pending
  last_written_file: {FILENAME.md}
  next_task: TASK-03
---

USAGE:
- Paste at top of every new chat before task instruction
- Update manually after each completed task
- Never rely on model to reconstruct this from history
