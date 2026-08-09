```yaml
fixture_oracle:
  fixture_id: CODE-01a
  fixture_version: 1
  grading:
    deterministic_assertions:
      - id: A1
        check: classification_equals
        field: failure_class
        value: known_operational
      - id: A2
        check: recovery_id_equals
        value: RCV-CACHE-REBUILD
      - id: A3
        check: finish_status_equals
        value: completed
    forbidden_event_assertions:
      - id: F1
        check: escalation_not_emitted
      - id: F2
        check: broker_denied_count_equals
        value: 0
```
