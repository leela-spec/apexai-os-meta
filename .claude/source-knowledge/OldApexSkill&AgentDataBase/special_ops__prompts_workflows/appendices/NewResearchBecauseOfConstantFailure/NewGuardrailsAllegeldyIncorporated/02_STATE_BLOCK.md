[STATE_BLOCK v1.0]
PURPOSE: replaces chat history — injected at top of every user message

FORMAT (JSON — parsed server-side before injection):
{
  "state": {
    "project":          "{PROJECT_NAME}",
    "session_id":       "{YYYY-MM-DD}-{seq}",
    "active_agent":     "{executor | planner | verifier}",
    "active_task_id":   "TASK-{XX}",
    "completed_tasks":  ["TASK-01", "TASK-02"],
    "last_written_file": "{FILENAME.ext | null}",
    "active_constraints": [
      "mode:move-only",
      "output:single-artifact-per-call",
      "forbidden:restructure,expand,rewrite"
    ],
    "open_items":       [{"id": "TASK-03", "description": "{...}"}],
    "repo_path":        "{/absolute/server/path/to/repo}",
    "next_task":        "TASK-03"
  }
}

SERVER RULES:
- State file lives at: /openclaw/state/{PROJECT_NAME}.json
- Updated by STATE_KEEPER agent after every successful TASK_CLOSURE
- Never updated by executor agent directly
- On state read failure: HALT. Do not proceed with stale state.
