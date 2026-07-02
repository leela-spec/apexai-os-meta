[TASK_CLOSURE v1.0]
TRIGGER: after every completed artifact

OUTPUT (exactly this, nothing else):
---
TASK_CLOSED:
  task_id: {TASK-XX}
  output_type: {file | diff | research | manifest}
  filename: {FILENAME.ext or N/A}
  scope_respected: yes | no
  additions_beyond_scope: none | {describe if any}
  next_suggested_task: {TASK-XX description or "none"}
---

RULES:
- This block is the ONLY text after an artifact
- Do not add congratulations, notes, or caveats
- If scope_respected=no: describe violation. Do not justify it.
