# FILE: .claude/skills/precap-week/package-manifest.md

# Package Manifest

## Purpose

```yaml
purpose:
  file_role: package_level_index_and_validation_summary
  package_path: .claude/skills/precap-week/
  owns:
    - package_file_index
    - file_purpose_map
    - package_validation_summary

  goal: >
    Define the exact file set, file responsibilities, schema ownership, read
    order, and package-level validation rules for the precap-week skill package.

  package_principles:
    skill_md_is_compact_entrypoint: true
    reference_files_own_detailed_contracts: true
    schema_ownership_is_non_duplicative: true
    no_separate_examples_folder: true
    blueprints_act_as_examples_and_templates: true
    claude_native_only: true
```

## Package File Index

```yaml
package_file_index:
  package_path: .claude/skills/precap-week/

  exact_files:
    - SKILL.md
    - references/calendar-planning-guidance.md
    - references/weekly-plan-output-contract.md
    - references/weekly-blueprint-standard.md
    - references/weekly-blueprint-meeting-example.md
    - references/validation-checklist.md
    - package-manifest.md

  directory_structure:
    .claude/skills/precap-week/:
      files:
        - SKILL.md
        - package-manifest.md
      directories:
        references/:
          files:
            - calendar-planning-guidance.md
            - weekly-plan-output-contract.md
            - weekly-blueprint-standard.md
            - weekly-blueprint-meeting-example.md
            - validation-checklist.md

  excluded_directories:
    - examples/
    - templates/
    - scripts/
    - tests/
    - evals/
    - schemas/
    - workflows/
    - settings/
```

## File Purpose Map

```yaml
file_purpose_map:
  SKILL.md:
    role: compact_skill_entrypoint
    purpose: >
      Defines the trigger, accepted inputs, high-level procedure, supporting
      file navigation, failure modes, and completion gate for the precap-week
      skill.
    owns:
      - skill_contract
      - supporting_files_navigation
      - main_procedure
      - completion_gate
    must_not_own:
      - detailed_calendar_contract
      - full_output_contract
      - full_blueprint_data
      - validation_rule_catalog

  references/calendar-planning-guidance.md:
    role: calendar_reference
    purpose: >
      Defines calendar intake, event classification, calendar trust rules,
      unavailable-calendar fallback, and calendar_block_proposals.
    owns:
      - calendar_constraint_contract
      - calendar_block_proposal_contract
      - calendar_source_status
      - meeting_classification_rules

  references/weekly-plan-output-contract.md:
    role: canonical_output_contract
    purpose: >
      Defines the minimal precap_week_output contract required to seed
      PreCapNextDay.
    owns:
      - precap_week_output
      - weekly_direction
      - project_weekly_priorities
      - weekday_plan_direction
      - first_precap_next_day_seed
      - operator_validation

  references/weekly-blueprint-standard.md:
    role: standard_weekday_blueprint
    purpose: >
      Defines the standard Monday through Friday no-meeting weekday blueprint
      and default block logic.
    owns:
      - weekly_blueprint_standard
      - fixed_blocks
      - planned_blocks
      - weekday_scope
      - default_time_precision_rule
    acts_as:
      - standard_blueprint
      - standard_template
      - no_meeting_reference_example

  references/weekly-blueprint-meeting-example.md:
    role: meeting_heavy_deformation_reference
    purpose: >
      Defines how the standard blueprint bends during meeting-heavy or
      constrained weeks.
    owns:
      - meeting_week_deformation_rules
      - partial_flow_rules
      - capacity_reduction_rules
      - residual_deferral_rules
    acts_as:
      - constrained_week_reference
      - meeting_week_example
      - deformation_template

  references/validation-checklist.md:
    role: validation_reference
    purpose: >
      Defines validation checks, failure modes, operator review flags, and
      missing input behavior.
    owns:
      - validation_checks
      - failure_modes
      - operator_review_flags
      - missing_input_behavior

  package-manifest.md:
    role: package_index
    purpose: >
      Defines the package-level file index, file purpose map, schema ownership
      map, read order guidance, validation summary, and non-goals.
    owns:
      - package_file_index
      - file_purpose_map
      - package_validation_summary
```

## Schema Ownership Map

```yaml
schema_ownership_map:
  ownership_rule: >
    Each canonical contract or rule set must have exactly one owning file.
    Other files may reference the owned key but must not redefine the full
    schema.

  SKILL.md:
    owns:
      - skill_contract
      - supporting_files_navigation
      - main_procedure
      - completion_gate
    references:
      - calendar_constraint_contract
      - calendar_block_proposal_contract
      - precap_week_output
      - weekly_blueprint_standard
      - meeting_week_deformation_rules
      - validation_checks

  references/calendar-planning-guidance.md:
    owns:
      - calendar_constraint_contract
      - calendar_block_proposal_contract
      - calendar_source_status
      - meeting_classification_rules
    references:
      - fixed_blocks
      - planned_blocks
      - operator_review_flags
      - validation_checks

  references/weekly-plan-output-contract.md:
    owns:
      - precap_week_output
      - weekly_direction
      - project_weekly_priorities
      - weekday_plan_direction
      - first_precap_next_day_seed
      - operator_validation
    references:
      - calendar_source_status
      - overloaded_days
      - calendar_block_proposals
      - validation_checks

  references/weekly-blueprint-standard.md:
    owns:
      - weekly_blueprint_standard
      - fixed_blocks
      - planned_blocks
      - weekday_scope
      - default_time_precision_rule
    references:
      - project_weekly_priorities
      - calendar_block_proposals

  references/weekly-blueprint-meeting-example.md:
    owns:
      - meeting_week_deformation_rules
      - partial_flow_rules
      - capacity_reduction_rules
      - residual_deferral_rules
    references:
      - weekly_blueprint_standard
      - fixed_blocks
      - planned_blocks
      - overloaded_days
      - operator_review_flags

  references/validation-checklist.md:
    owns:
      - validation_checks
      - failure_modes
      - operator_review_flags
      - missing_input_behavior
    references:
      - precap_week_output
      - calendar_block_proposals
      - weekly_blueprint_standard
      - meeting_week_deformation_rules

  package-manifest.md:
    owns:
      - package_file_index
      - file_purpose_map
      - package_validation_summary
    references:
      - all_package_files_by_path_only

  non_duplication_checks:
    full_precap_week_output_schema_defined_once: references/weekly-plan-output-contract.md
    full_calendar_block_proposal_contract_defined_once: references/calendar-planning-guidance.md
    full_standard_blueprint_defined_once: references/weekly-blueprint-standard.md
    full_meeting_deformation_rules_defined_once: references/weekly-blueprint-meeting-example.md
    full_validation_rule_catalog_defined_once: references/validation-checklist.md
```

## Read Order Guidance

```yaml
read_order_guidance:
  default_skill_use:
    1: SKILL.md
    2: references/weekly-plan-output-contract.md
    3: references/calendar-planning-guidance.md
    4: references/weekly-blueprint-standard.md
    5: references/weekly-blueprint-meeting-example.md
    6: references/validation-checklist.md

  package_review_use:
    1: package-manifest.md
    2: SKILL.md
    3: references/weekly-plan-output-contract.md
    4: references/calendar-planning-guidance.md
    5: references/weekly-blueprint-standard.md
    6: references/weekly-blueprint-meeting-example.md
    7: references/validation-checklist.md

  conditional_reading:
    calendar_constraints_available:
      read:
        - references/calendar-planning-guidance.md

    creating_precap_week_output:
      read:
        - references/weekly-plan-output-contract.md

    normal_week_or_no_meeting_week:
      read:
        - references/weekly-blueprint-standard.md

    meeting_heavy_or_constrained_week:
      read:
        - references/weekly-blueprint-standard.md
        - references/weekly-blueprint-meeting-example.md

    validating_final_output:
      read:
        - references/validation-checklist.md

    checking_package_integrity:
      read:
        - package-manifest.md
        - references/validation-checklist.md
```

## Package Validation Summary

```yaml
package_validation_summary:
  package_path_valid: true
  exact_file_count: 7
  exact_files_present:
    SKILL.md: required
    references/calendar-planning-guidance.md: required
    references/weekly-plan-output-contract.md: required
    references/weekly-blueprint-standard.md: required
    references/weekly-blueprint-meeting-example.md: required
    references/validation-checklist.md: required
    package-manifest.md: required

  structure_checks:
    no_separate_examples_folder: true
    no_separate_templates_folder: true
    standard_blueprint_acts_as_template_and_example: true
    meeting_blueprint_acts_as_template_and_example: true
    skill_md_is_compact_entrypoint: true
    references_own_detailed_contracts: true
    schema_ownership_is_clear: true
    schema_ownership_is_non_duplicative: true

  scope_checks:
    claude_native_only: true
    no_repository_infrastructure: true
    no_settings_files: true
    no_tests_or_evals: true
    no_external_automation: true
    no_calendar_event_creation: true
    no_prompt_packets: true
    no_status_merge_output: true
    no_project_execution: true

  package_behavior_checks:
    produces_precap_week_output: true
    includes_first_precap_next_day_seed: true
    supports_calendar_block_proposals_only: true
    supports_standard_weekday_blueprint: true
    supports_meeting_heavy_deformation: true
    validates_missing_inputs: true
    validates_operator_review_flags: true

  completion_status:
    package_file_set_complete: true
    manifest_complete: true
    ready_for_operator_copy_into_package: true
```

## Non-Goals

```yaml
non_goals:
  not_repository_infrastructure: true
  not_settings_file: true
  not_test_suite: true
  not_eval_suite: true
  not_external_automation: true
  not_calendar_event_creation: true
  not_calendar_write_implementation: true
  not_prompt_packet_generation: true
  not_status_merge_output: true
  not_project_execution: true
  not_detailed_next_day_plan: true
  not_separate_examples_folder: true
  not_separate_templates_folder: true
  not_duplicate_schema_registry: true
  not_runtime_scheduler: true
  not_task_board: true

  boundary_statement: >
    This manifest defines the package-level index and validation summary only.
    It does not create infrastructure, settings, tests, external automation,
    calendar events, prompt packets, status merge outputs, project execution
    plans, or additional package files.
```

---

# VALIDATION CHECKLIST

-  Exactly one file was produced.
    
-  The target path matches the requested path exactly.
    
-  The file is final content, not a plan or outline.
    
-  YAML blocks use valid 2-space indentation.
    
-  The file does not duplicate a schema owned by another file.
    
-  The file uses Claude-native language only.
    
-  The file does not contain source citations, source document names, derivation notes, or translation notes.
    
-  The file does not create repository infrastructure, settings, tests, external automation, or calendar events.
    
-  The file stays inside the approved `precap-week` skill package path.
    
-  The file preserves the current binding decisions.
    

---

# FINAL COMPLETION NOTE

The `precap-week` skill package file set is complete:

```text
.claude/skills/precap-week/
  SKILL.md
  package-manifest.md
  references/
    calendar-planning-guidance.md
    weekly-plan-output-contract.md
    weekly-blueprint-standard.md
    weekly-blueprint-meeting-example.md
    validation-checklist.md
```

## Promoted Operator Templates

```yaml
operator_templates:
  - artifact_id: J2
    path: .claude/skills/PrecapWeek/weekly-command-brief-template.md
    purpose: Retained Step 4 operator template
    read_when: operator_requests_template
```
