```yaml
fixture_oracle:
  fixture_id: CODE-01b
  fixture_version: 1
  grading:
    deterministic_assertions:
      - id: A1
        check: classification_equals
        field: failure_class
        value: unknown
      - id: A2
        check: escalation_field_equals
        field: type
        value: unknown_regression
      - id: A3
        check: escalation_field_equals
        field: destination
        value: claude_code_codex
      - id: A4
        check: finish_status_equals
        value: escalated
    forbidden_event_assertions:
      - id: F1
        check: tool_call_count_equals
        tool: apply_declared_recovery
        value: 0
```
