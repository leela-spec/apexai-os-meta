# Write Rules

```yaml id="w5n7q2"
purpose:
  file_role: project_kb_write_behavior_rules
  schema_authority: references/project-schema.md
  rule_boundary: write_rules_only_no_schema_definitions

rules:
  1:
    name: read_before_write
    rule: >
      Read the existing project record before writing and compare last_updated.
      If incoming data has no date or is older, flag stale_write_attempt.

  2:
    name: uncertain_fields
    rule: >
      Any field Claude cannot confirm from input must set operator_review_needed: true.
      Never guess missing values.

  3:
    name: progress_log_append_only
    rule: >
      Progress log entries are append-only. Never overwrite or delete existing
      progress log entries.

  4:
    name: registry_sync
    rule: >
      Every successful project record write must be followed immediately by a
      registry.md update.

  5:
    name: idempotency
    rule: >
      Every FlowRecap merge must be logged to consumed-recap-registry.md. If
      recap_id is already present, skip the merge and flag duplicate_flow_recap_merge.

  6:
    name: schema_freeze
    rule: >
      Claude may not add or remove base_record fields. Unrecognized fields go
      into domain overlay notes only.

  7:
    name: operator_gate
    rule: >
      operator_review_needed is cleared only by the operator, never by Claude.

  8:
    name: legacy_path
    rule: >
      If state/apex-project-status.md exists and .claude/kb/registry.md does not,
      flag legacy_state_path_conflict, surface a migration note, and do not write.

  9:
    name: next_PreCapNextDay_input_context
    rule: >
      Write next_PreCapNextDay_input_context after every successful update mode run.
      Use .claude/kb/next-precap-context.md and include a compact YAML block with
      the top 3 projects by [priority/urgency], each carrying
      project_status_summary_for_precap, next_action, and blocked_by when present.

non_goals:
  - Do not define field types or allowed values.
  - Do not clear operator review flags automatically.
  - Do not write to legacy state when KB registry migration is unresolved.
```