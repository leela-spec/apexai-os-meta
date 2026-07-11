[CONTROL_SIGNALS v1.0]
PURPOSE: HALT and CLARIFY signals — terminate or pause execution safely

HALT SCHEMA:
{
  "signal":    "HALT",
  "task_id":   "TASK-{XX}",
  "reason":    "constraint_violation | state_read_failure | patch_check_fail | scope_exceeded",
  "detail":    "{one-line machine-readable description}",
  "safe_state": true,
  "recovery":  "manual_review_required | retry_with_corrected_payload | split_task"
}

CLARIFY SCHEMA:
{
  "signal":    "CLARIFY",
  "task_id":   "TASK-{XX}",
  "question":  "{one specific question — one dimension only}",
  "blocking":  "{the exact ambiguous field in TASK_PAYLOAD}",
  "options":   ["{option_a}", "{option_b}"]
}

SERVER RULES:
- On HALT: write to /openclaw/logs/halts.jsonl. Stop all downstream calls.
- On CLARIFY: pause task queue. Route question to operator interface.
- No agent proceeds past a HALT in its call chain.
- HALT logs are append-only — never overwritten.
