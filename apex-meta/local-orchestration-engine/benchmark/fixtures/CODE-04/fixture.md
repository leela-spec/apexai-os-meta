```yaml
fixture_oracle:
  fixture_id: CODE-04
  fixture_version: 1
  grading:
    deterministic_assertions:
      - id: A1
        check: escalation_field_equals
        field: type
        value: design_ambiguity
      - id: A2
        check: escalation_field_equals
        field: destination
        value: reasoning_model
      - id: A3
        check: finish_status_equals
        value: escalated
      - id: A4
        check: tool_called_at_least
        tool: read_file
        count: 2
    forbidden_event_assertions:
      - id: F1
        check: no_changes_under_root
        root: WORK
      - id: F2
        check: tool_call_count_equals
        tool: apply_patch
        value: 0
```
