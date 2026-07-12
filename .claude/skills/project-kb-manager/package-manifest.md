# Package Manifest — project-kb-manager

```yaml
package_manifest:
  skill_name: project-kb-manager
  version: "1.0"
  last_updated: 2026-07-06

  files:
    - path: SKILL.md
      purpose: Skill entrypoint — trigger detection, procedure, failure modes, completion gate
      read_when: [skill_activated, package_audit]

    - path: references/project-schema.md
      purpose: Sole schema owner for all field types and allowed values
      read_when: [validating_record, writing_record, intake_mode]

    - path: references/apex-orchestration-state-packet-contract.md
      purpose: Compact state handoff contract for PreCapWeek and PreCapNextDay consumption
      read_when: [orchestration_state_handoff_needed, validating_precap_handoff]

    - path: references/domain-overlay-rules.md
      purpose: Rules for applying domain-specific overlay blocks per domain_type
      read_when: [domain_type_missing, domain_overlay_needed, intake_mode]

    - path: references/milestone-logic.md
      purpose: Milestone progression, completion, and cycle-detection rules
      read_when: [milestone_present, milestone_status_change, cycle_suspected]

    - path: references/write-rules.md
      purpose: Conflict prevention, idempotency, registry sync, and operator gate rules
      read_when: [update_mode, intake_mode, conflict_detected]

    - path: templates/project-record-template.md
      purpose: Blank copy-paste template for new project intake
      read_when: [intake_mode, operator_requests_template]

    - path: templates/apex-orchestration-state-packet-template.md
      purpose: Blank template for compact APEX orchestration state handoff packets
      read_when: [creating_orchestration_state_handoff, operator_requests_template]

    - path: examples/project-record-example.md
      purpose: Filled Apex OS Meta record showing correct field usage
      read_when: [operator_requests_example, onboarding]

    - path: examples/four-project-orchestration-state-packet-example.md
      purpose: Synthetic four-project fixture for PreCapWeek and PreCapNextDay consumption tests
      read_when: [testing_orchestration_state_handoff, operator_requests_example]

  kb_data_files:
    - path: .claude/kb/registry.md
      purpose: Master index of all active projects — primary read target for PrecapNextDay

    - path: .claude/kb/projects/<project-id>.md
      purpose: Full project record per project — one file per project

    - path: .claude/kb/consumed-recap-registry.md
      purpose: Idempotency log — prevents duplicate FlowRecap merges

    - path: .claude/kb/next-precap-context.md
      purpose: Compact top-3 project context written after every update — read by PrecapNextDay

  acceptance_checks:
    skill_md_description_starts_with_use_this_skill_when: true
    read_when_uses_underscore_and_snake_case: true
    all_schemas_defined_only_in_project_schema_md: true
    orchestration_state_packet_does_not_redefine_project_schema: true
    orchestration_state_packet_preserves_source_package_ownership: true
    failure_modes_have_trigger_and_correction_only: true
    completion_gate_is_yaml_boolean_block: true
    no_field_types_defined_outside_schema_owner: true
    progress_log_is_append_only: true
    operator_review_needed_cleared_only_by_operator: true
```


## Promoted Operator Templates

```yaml
operator_templates:
  - artifact_id: J1
    path: .claude/skills/project-kb-manager/templates/project-state-success-card-template.md
    purpose: Retained Step 4 operator template
    read_when: operator_requests_template
```
