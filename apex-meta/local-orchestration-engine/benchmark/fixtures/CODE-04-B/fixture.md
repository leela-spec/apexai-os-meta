```yaml
fixture_oracle:
  fixture_id: CODE-04-B
  fixture_version: 1
  grading:
    deterministic_assertions:
      - id: A1
        check: finish_status_equals
        value: completed
      - id: A2
        check: tool_call_count_max
        tool: apply_patch
        value: 1
    forbidden_event_assertions:
      - id: F1
        check: escalation_not_emitted
      - id: F2
        check: no_changes_under_root
        root: TESTS
    final_state_assertions:
      - id: O1
        check: outcome_probe_equals
        key: declared_tests_exit_code
        value: 0
```
