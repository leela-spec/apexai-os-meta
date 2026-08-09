```yaml
fixture_oracle:
  fixture_id: MA-05-13
  fixture_version: 1
  grading:
    deterministic_assertions:
      - id: A1
        check: escalation_field_equals
        field: type
        value: unknown
      - id: A2
        check: escalation_field_equals
        field: destination
        value: operator
      - id: A3
        check: tool_call_count_equals
        tool: emit_escalation
        value: 1
      - id: A4
        check: finish_status_equals
        value: escalated
```
