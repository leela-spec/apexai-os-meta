# PreCap Week Package Manifest

```yaml
package_manifest:
  package_name: PrecapWeek
  package_path: .claude/skills/PrecapWeek/
  entrypoint: Skill_Precap-Week.md
  primary_output: precap_week_output
  first_downstream_seed: first_precap_next_day_seed
  files:
    - path: Skill_Precap-Week.md
      role: skill_entrypoint
    - path: calendar-planning-guidance.md
      role: calendar_constraint_contract
    - path: weekly-plan-output-contract.md
      role: canonical_weekly_output_contract
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
    first_precap_next_day_seed_required: true
```
