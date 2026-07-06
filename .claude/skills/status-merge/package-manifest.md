# status-merge Package Manifest

```yaml
package_manifest:
  package_name: status-merge
  package_path: .claude/skills/status-merge/
  package_role: minimal_interface_package
  lifecycle_status: interface_package_in_progress
  created_for: APEX orchestration loop
  artifact_family:
    - status_merge_packet
    - merge_proposal
    - conflict_notes
    - next_PreCapNextDay_input_context

  intent: >
    Provide the minimal interface package for reviewing validated recap-derived
    candidate deltas, surfacing conflicts, proposing owner-safe project status
    updates, and preparing compact context for a later PreCapNextDay run.

  non_intent: >
    This package does not implement runtime automation, scheduler behavior,
    autonomous state overwrite, direct project KB mutation, or replacement of
    project-kb-manager, ProjectStatus, FlowRecap, PreCapNextDay, PreCapWeek,
    model-usage-log, apex-plan, apex-sync, or apex-session.
```

## File Inventory

```yaml
files:
  - path: .claude/skills/status-merge/references/status-merge-packet-contract.md
    role: primary_packet_contract
    status: created
    commit: 3eaa1da9d6c49a8b6dc966fa43899f1d9f70c5c4
    loaded_by_default: false
    read_when:
      - defining_status_merge_packet_schema
      - validating_status_merge_packet_fields
      - checking_merge_scope_or_validation_status_values
      - auditing_project_kb_manager_boundary

  - path: .claude/skills/status-merge/references/next-precaphandoff-context-contract.md
    role: downstream_context_contract
    status: created
    commit: c1f8edbea08ae0cd2e345f36751e2d3b9550a969
    loaded_by_default: false
    read_when:
      - defining_next_PreCapNextDay_input_context
      - validating_daily_planning_seed_boundaries
      - separating_context_seed_from_next_day_plan
      - checking_usage_summary_reference_handling

  - path: .claude/skills/status-merge/templates/status-merge-packet-template.md
    role: operator_facing_template
    status: created
    commit: e3bf1e892e4b211cbb8fad022a83c6a83386c67c
    loaded_by_default: false
    read_when:
      - producing_operator_review_packet
      - drafting_merge_proposal_cards
      - surfacing_conflict_notes
      - preparing_next_PreCapNextDay_input_context_section

  - path: .claude/skills/status-merge/examples/apex-minimal-status-merge-example.md
    role: minimal_apex_example
    status: created
    commit: fdad73f34183c4ce43a970bb1592aa78a9efa0fe
    loaded_by_default: false
    read_when:
      - checking_minimal_valid_example
      - demonstrating_one_accepted_delta_and_one_conflict
      - confirming_no_actual_project_kb_mutation
      - showing_next_PreCapNextDay_input_context_seed

  - path: .claude/skills/status-merge/package-manifest.md
    role: package_inventory_and_boundary_manifest
    status: created
    commit: pending_current_commit
    loaded_by_default: false
    read_when:
      - auditing_package_contents
      - checking_source_gaps
      - validating_file_roles
      - confirming_non_runtime_scope

  - path: .claude/skills/status-merge/SKILL.md
    role: skill_entrypoint
    status: pending
    commit: null
    loaded_by_default: true
    read_when:
      - invoking_status_merge_skill
      - deciding_whether_to_use_package
      - following_default_procedure
      - checking_completion_gate
```

## Source Authority Register

```yaml
source_authority_register:
  inspected_sources:
    - path: .claude/Claude.md
      status: inspected
      relevance:
        - declares_StatusMerge_as_missing_in_APEX_loop
        - defines_manual_operator_trigger_expectation
        - forbids_automatic_state_overwrite
        - forbids_auto_triggering_skills_or_batch_writes_without_confirmation

    - path: .claude/skills/project-kb-manager/SKILL.md
      status: inspected
      relevance:
        - identifies_project_kb_manager_as_durable_project_kb_boundary
        - distinguishes_query_update_and_intake_modes
        - forbids_project_work_daily_planning_and_schema_drift

    - path: .claude/skills/project-kb-manager/references/project-schema.md
      status: inspected
      relevance:
        - owns_project_kb_schema_fields_and_allowed_values
        - provides_base_record_milestone_progress_registry_and_consumed_recap_shapes

    - path: .claude/skills/project-kb-manager/references/apex-orchestration-state-packet-contract.md
      status: inspected
      relevance:
        - defines_compact_state_handoff_role
        - preserves_existing_package_ownership_boundaries
        - excludes_status_merge_runtime_and_next_day_plan_creation

    - path: .claude/skills/project-kb-manager/templates/apex-orchestration-state-packet-template.md
      status: inspected
      relevance:
        - demonstrates_operator_first_review_cards
        - demonstrates_compact_weekly_and_next_day_planning_views

    - path: .claude/skills/ProjectStatus/project-status-overview_SKILL_v3.md
      status: inspected
      relevance:
        - owns_current_project_status_overview_output
        - explicitly_excludes_status_merge_and_next_day_plans

    - path: .claude/skills/flow-recap/references/flow-recap-packet-contract.md
      status: inspected
      relevance:
        - defines_flow_recap_outputs_as_candidate_only
        - forbids_project_kb_mutation_and_status_merge_execution
        - separates_candidate_deltas_from_accepted_state

    - path: .claude/skills/model-usage-log/references/model-usage-delta-contract.md
      status: inspected
      relevance:
        - defines_model_usage_delta_as_advisory_non_blocking
        - prevents_status_merge_from_owning_usage_metering_or_runtime_claims

    - path: apex-meta/kb/claude-code-orchestration-design/wiki/concepts/status-merge-packet.md
      status: inspected
      relevance:
        - gives_status_merge_concept
        - says_conflicts_are_exposed_before_acceptance
        - says_no_status_merge_runtime_is_implemented

    - path: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-skill-design/sources/operator-supplied/notes/Claude_Skill_Package_BestPractice_Handover.md
      status: inspected
      relevance:
        - defines_skill_package_anatomy
        - allows_references_templates_examples_and_manifest
        - forbids_runtime_scheduler_test_files_for_interface_packages
        - restricts_SKILL_md_frontmatter

    - path: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-skill-design/sources/operator-supplied/notes/Claude_Skill_PromptFlow_Design_Guidance_v1.md
      status: inspected
      relevance:
        - requires_Use_this_skill_when_description_start
        - recommends_5_to_8_step_procedures
        - keeps_failure_modes_compact
        - warns_against_yaml_indentation_collapse
```

## Source Gap Register

```yaml
source_gap_register:
  - path: .claude/skills/flow-recap/references/project-status-delta-contract.md
    status: missing
    impact: medium
    handling: >
      Do not infer or redefine project_status_delta schema. StatusMerge may carry
      recap-derived delta summaries only as candidates, references, conflict
      notes, or proposal views until the owning contract exists.

  - path: .claude/skills/model-usage-log/references/usage-summary-contract.md
    status: missing
    impact: medium
    handling: >
      Keep usage_summary_ref opaque and nullable where needed. Do not define the
      usage_summary schema in status-merge.
```

## Ownership Boundary

```yaml
ownership_boundary:
  owns:
    - status_merge_packet
    - merge_proposal
    - accepted_delta_register_view
    - conflict_notes
    - consumed_recap_candidate_list
    - next_PreCapNextDay_input_context
    - operator_conflict_review_gate

  must_not_own:
    - project_kb_durable_schema
    - direct_project_record_mutation_without_project_kb_manager
    - current_project_status_overview_schema
    - flow_recap_packet_schema
    - model_usage_delta_schema
    - usage_summary_schema
    - apex_orchestration_state_packet_schema
    - weekly_plan_packet_schema
    - next_day_plan_schema
    - calendar_write_schema
    - runtime_execution
    - automatic_status_overwrite
```

## Package Validation Status

```yaml
package_validation_status:
  source_files_inspected_or_gaps_recorded: true
  package_path_created: true
  status_merge_packet_contract_created: true
  next_precap_context_contract_created: true
  template_created: true
  apex_minimal_example_created: true
  manifest_created: true
  SKILL_md_created_with_valid_frontmatter: false
  project_kb_manager_boundary_preserved: true
  conflicts_are_surfaced_before_acceptance: true
  no_automatic_status_overwrite_created: true
  next_PreCapNextDay_input_context_is_clear: true

  overall_status: incomplete_until_SKILL_md_created
```

## Non-Runtime Assurance

```yaml
non_runtime_assurance:
  no_scripts_created: true
  no_tests_created: true
  no_scheduler_created: true
  no_cron_created: true
  no_agent_runtime_created: true
  no_calendar_write_created: true
  no_project_kb_write_created: true
  no_status_overwrite_created: true
  no_external_api_integration_created: true
```

## Finalization Dependency

```yaml
finalization_dependency:
  remaining_file:
    path: .claude/skills/status-merge/SKILL.md
    requirement: >
      Create the skill entrypoint with only allowed frontmatter fields `name`
      and `description`, with description beginning exactly with
      `Use this skill when`, a 5-8 step procedure, compact failure modes, and a
      boolean completion gate.
```
