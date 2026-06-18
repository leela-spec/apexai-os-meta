# Write Rules

```yaml id="w5n7q2"
purpose:
  file_role: project_kb_write_behavior_rules
  schema_authority: references/project-schema.md
  rule_boundary: write_rules_only_no_schema_definitions

rules:
  1_read_before_write: >
    Read the existing project record before writing and compare last_updated.
    If incoming data has no date or is older, flag stale_write_attempt.
  2_uncertain_fields: >
    Any field Claude cannot confirm from input must keep operator_review_needed: true.
    Never guess.
  3_progress_log_append_only: >
    Append progress log entries only. Never overwrite, reorder, or delete previous entries.
  4_registry_sync: >
    Every successful project record write must be followed immediately by a registry.md update.
  5_idempotency: >
    Every FlowRecap merge must be logged to consumed-recap-registry.md. If recap_id
    is already present, skip the merge and flag duplicate_flow_recap_merge.
  6_schema_freeze: >
    Claude may not add or remove base_record fields. Unrecognized fields go into
    the matching domain overlay notes field only.
  7_operator_gate: >
    operator_review_needed is cleared only by explicit operator validation, never by Claude.
  8_legacy_path: >
    If state/apex-project-status.md exists and .claude/kb/registry.md does not,
    flag legacy_state_path_conflict, surface a migration note, and do not write.
  9_next_PreCapNextDay_input_context: >
    After every successful update mode run, write next_PreCapNextDay_input_context
    to .claude/kb/next-precap-context.md as compact YAML with the top 3 projects
    by [priority/urgency], each carrying project_status_summary_for_precap,
    next_action, and blocked_by when present.

non_goals:
  - Do not define field types or allowed values.
  - Do not execute project work.
  - Do not create planning output.
```