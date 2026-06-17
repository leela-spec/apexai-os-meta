[GATE_CHECK v1.0]
TRIGGER: first output of every agent call — before any task execution

JSON OUTPUT SCHEMA:
{
  "gate_check": {
    "task_id":              "TASK-{XX}",
    "agent_role":           "{executor | planner | verifier}",
    "task_type_understood": "{file_write | diff_patch | ...}",
    "scope_understood":     "{repeat scope from payload verbatim}",
    "target_file":          "{filename | null}",
    "active_constraints":   ["{list from state}"],
    "ambiguity_detected":   false,
    "ready_to_execute":     true
  }
}

SERVER RULES:
- Server parses gate_check BEFORE allowing agent to produce task output
- If ambiguity_detected=true: server triggers CLARIFY flow (TEMPLATE_09)
- If ready_to_execute=false: server triggers HALT (TEMPLATE_09)
- Gate check max_tokens: 256 — agent must be concise
- Gate check is a separate API call — not prepended to task output call
