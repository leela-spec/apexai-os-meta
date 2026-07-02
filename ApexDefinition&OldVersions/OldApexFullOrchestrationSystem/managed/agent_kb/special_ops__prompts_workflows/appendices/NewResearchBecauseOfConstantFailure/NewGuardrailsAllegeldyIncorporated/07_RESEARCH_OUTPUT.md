[RESEARCH_OUTPUT v1.0]
TRIGGER: task_type = research_block

JSON OUTPUT SCHEMA:
{
  "output_type":  "research_block",
  "task_id":      "TASK-{XX}",
  "topic":        "{bounded topic string}",
  "format":       "bullets | table | numbered | prose",
  "depth":        "surface | standard | exhaustive",
  "content":      "{output in declared format — no additional structure}",
  "sources":      [{"label": "{name}", "ref": "{url or filename}"}],
  "scope_respected": true,
  "recommendations_included": false
}

RULES:
- recommendations_included must be false unless task explicitly requested them
- content key contains only the declared format — no mixed formats
- sources array empty if no external refs used — never omit key
- If depth=exhaustive and content approaches 8192 tokens:
    set "split_required": true, "part": 1, "parts_total": {n}
    server triggers continuation call automatically
