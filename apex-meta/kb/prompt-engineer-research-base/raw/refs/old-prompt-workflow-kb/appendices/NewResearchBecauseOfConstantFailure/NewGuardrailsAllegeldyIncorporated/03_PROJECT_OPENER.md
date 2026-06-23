[PROJECT_OPENER v1.0]
TRIGGER: start of new project session

STRUCTURE (paste as first message in every new chat):

---
PROJECT: {PROJECT_NAME}
SESSION_ID: {YYYY-MM-DD}-{sequential_id}
TASK_ID: {TASK-XX}
TASK: {one-line atomic task description}
OUTPUT_TYPE: [single_file | diff | manifest | research_block]
CONSTRAINTS: [list active constraints or reference BOOTSTRAP]
STATE_REF: {paste STATE block here or write "none"}
---

RULES:
- No task proceeds until this block is accepted
- Model must echo: PROJECT_LOADED | TASK: {TASK_ID} | READY
- If OUTPUT_TYPE is missing: model asks for it. Does not assume.
