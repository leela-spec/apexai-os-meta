---
name: project-kb-manager
description: Use this skill when the operator asks Claude to query, update, or intake project knowledge through the Apex project KB using "run project-kb", "update project-kb", or "add project [NAME]".
---

# Project KB Manager

## Skill Contract

This skill maintains the Apex project knowledge base as a compact, schema-governed source for project status, milestone state, FlowRecap consumption, and PreCapNextDay context.

Modes:
- query_mode: answer project KB questions without mutating files.
- update_mode: merge operator-provided updates or FlowRecap packets into project records.
- intake_mode: create a new project record from the project-record template.

Boundaries:
- Do not execute project work.
- Do not create daily or weekly plans.
- Do not run FlowRecap.
- Do not mutate calendars.
- Do not define schema fields outside `references/project-schema.md`.

## Supporting Files

```yaml
supporting_files:
  - path: references/project-schema.md
    read_when: always
  - path: references/domain-overlay-rules.md
    read_when: before_domain_specific_interpretation
  - path: references/milestone-logic.md
    read_when: before_milestone_state_changes
  - path: references/write-rules.md
    read_when: before_any_write
  - path: templates/project-record-template.md
    read_when: intake_mode
  - path: examples/project-record-example.md
    read_when: examples_needed
  - path: package-manifest.md
    read_when: package_audit
```

## Procedure

1. Detect query_mode, update_mode, or intake_mode from the operator trigger and input scope.
2. Read the schema owner and the supporting files required for the selected mode.
3. Load the registry and any existing project record needed for identity, recency, or write checks.
4. Apply domain overlay, milestone, and write rules without adding schema fields.
5. Return the KB answer or write the project record, registry, recap registry, and next PreCap context required by the mode.
6. Run the completion gate and surface every unresolved operator_review_needed condition.

## Failure Modes

```yaml id="1tonae"
failure_modes:
  - trigger: stale_write_attempt
    correction: Preserve the existing record and ask for fresher dated evidence.
  - trigger: duplicate_flow_recap_merge
    correction: Skip the merge and report the previously consumed recap_id.
  - trigger: legacy_state_path_conflict
    correction: Surface the migration note and do not write until KB registry exists.
  - trigger: schema_field_drift
    correction: Move unrecognized information to domain overlay notes or request schema revision.
  - trigger: unsupported_domain_type
    correction: Ask the operator to choose one supported domain_type.
  - trigger: milestone_cycle_detected
    correction: Halt milestone changes and ask the operator to remove the circular dependency.
  - trigger: missing_operator_confirmation
    correction: Keep operator_review_needed true and describe the confirmation needed.
  - trigger: ambiguous_project_identity
    correction: Stop the write and ask the operator to identify the target project.
```

## Output Requirements

Return one of these outputs:
- query_result: compact project KB answer with source paths used.
- update_result: files changed, records skipped, flags raised, and next PreCap context status.
- intake_result: new project record path, registry status, and operator review requirements.
- error_result: trigger, correction, preserved files, and missing evidence.

## Completion Gate

```yaml id="48f8oo"
completion_gate:
  mode_detected: false
  schema_owner_loaded: false
  required_support_files_loaded: false
  existing_state_checked: false
  no_schema_defined_outside_project_schema: false
  write_rules_applied: false
  registry_synced_when_write_occurs: false
  flow_recap_idempotency_checked: false
  operator_review_flags_preserved: false
  next_precap_context_written_when_update_occurs: false
```