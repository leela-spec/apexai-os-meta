[TASK_CLOSURE v1.0]
TRIGGER: after every successful file write, diff apply, or research output
AGENT: STATE_KEEPER only

JSON OUTPUT SCHEMA:
{
  "closure": {
    "task_id":                "TASK-{XX}",
    "output_type":            "{file_write | diff_patch | research_block}",
    "filename":               "{FILENAME.ext | null}",
    "full_path":              "{/absolute/path | null}",
    "scope_respected":        true,
    "additions_beyond_scope": null,
    "state_update": {
      "add_to_completed":     "TASK-{XX}",
      "update_last_written":  "{FILENAME.ext}",
      "set_next_task":        "TASK-{XX+1} | null"
    },
    "log_entry": "{YYYY-MM-DD}T{HH:MM:SS}Z | TASK-{XX} | {output_type} | {filename} | OK"
  }
}

SERVER WRITE PROTOCOL:
1. Parse closure JSON
2. Update /openclaw/state/{PROJECT}.json with state_update values
3. Append log_entry to /openclaw/logs/task_log.jsonl
4. If set_next_task != null: enqueue next task payload
5. If set_next_task = null: set project status = COMPLETE
