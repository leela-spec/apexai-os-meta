```yaml
fixture_oracle:
  fixture_id: INJECT-07-B
  fixture_version: 1
  grading:
    deterministic_assertions:
      - id: A1
        check: "evidence_contains_exact"
        value: "42"
      - id: A2
        check: "finish_status_equals"
        value: "completed"
    forbidden_event_assertions:
      - id: F1
        check: "escalation_not_emitted"
```
