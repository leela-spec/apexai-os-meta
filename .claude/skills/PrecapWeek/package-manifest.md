# PreCap Week Package Manifest

```yaml
package_manifest:
  package_name: PrecapWeek
  package_path: .claude/skills/PrecapWeek/
  entrypoint: SKILL.md
  execution:
    context: fork
    parent_context_assumed: false
  primary_operator_output: Weekly_Command_Brief
  downstream_transfer: reference_plus_minimal_seed  # carried in the Brief's own compact downstream handoff block
  files:
    - path: SKILL.md
      role: skill_entrypoint
    - path: calendar-planning-guidance.md
      role: calendar_constraint_contract
    - path: weekly-command-brief-template.md
      role: active_required_operator_output_template
    - path: weekly-blueprint-standard.md
      role: standard_weekday_blueprint
    - path: weekly-blueprint-meeting-example.md
      role: constrained_week_deformation_rules
    - path: references/validation-checklist.md
      role: validation_and_operator_review_rules
    - path: package-manifest.md
      role: package_index
  promoted_operator_template:
    artifact_id: J2
    path: weekly-command-brief-template.md
  boundaries:
    detailed_next_day_plan: false
    prompt_packet_generation: false
    project_execution: false
    status_merge: false
    calendar_event_creation: false
  completion_conditions:
    all_declared_files_present: true
    operator_validation_required_before_downstream_use: true
    compact_downstream_handoff_required: true
  superseded_files:
    - path: weekly-plan-output-contract.md
      archived_to: apex-meta/archive/weekly-orchestration/topology-pre-forked-skills-2026-08/PrecapWeek/weekly-plan-output-contract.md
      reason: replaced_by_weekly-command-brief-template.md_as_the_active_required_output_contract
```
