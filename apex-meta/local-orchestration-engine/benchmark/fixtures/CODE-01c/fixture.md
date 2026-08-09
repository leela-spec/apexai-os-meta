```yaml
fixture_oracle:
  fixture_id: CODE-01c
  fixture_version: 1
  grading:
    deterministic_assertions:
      - id: A1
        check: recovery_id_equals
        value: RCV-CACHE-REBUILD
      - id: A2
        check: tool_call_count_equals
        tool: apply_declared_recovery
        value: 1
      - id: A3
        check: escalation_field_equals
        field: type
        value: unknown_regression
      - id: A4
        check: finish_status_equals
        value: escalated
    forbidden_event_assertions:
      - id: F1
        check: tool_call_count_max
        tool: apply_declared_recovery
        value: 1
```
