# status-merge Package Manifest

```yaml
package_manifest:
  package_name: status-merge
  package_path: .claude/skills/status-merge/
  package_role: minimal_interface_package
  lifecycle_status: interface_package_present
  created_for: APEX orchestration loop
  artifact_family:
    - status_merge_packet
    - merge_proposal
    - accepted_delta_register_view
    - conflict_notes
    - consumed_recap_candidate_list
    - next_PreCapNextDay_input_context
    - operator_conflict_review_gate

  intent: >
    Provide the minimal interface package for reviewing validated recap-derived
    candidate deltas, surfacing conflicts, proposing owner-safe project status
    updates, and preparing compact context for a later PreCapNextDay run.

  non_intent: >
    This package does not implement runtime automation, scheduler behavior,
    autonomous state overwrite, direct project KB mutation, or replacement of
    project-kb-manager, ProjectStatus, FlowRecap, PreCapNextDay, PreCapWeek,
    model-usage-log, apex-plan, apex-sync, apex-session, or apex-kb.
```

## File Inventory

```yaml
files:
  - path: .claude/skills/status-merge/references/status-merge-packet-contract.md
    role: primary_packet_contract
    status: created
    commit: 9dc21016090e46b3f797a617956c8caf7825a3c7
    loaded_by_default: false
    read_when:
      - defining_status_merge_packet_schema
      - validating_status_merge_packet_fields
      - checking_merge_scope_or_validation_status_values
      - auditing_project_kb_manager_boundary

  - path: .claude/skills/status-merge/references/next-precaphandoff-context-contract.md
    role: downstream_context_contract
    status: created
    commit: 772d4d56243ebc95c2f10aba3e722c6e19b0e0e3
    loaded_by_default: false
    read_when:
      - defining_next_PreCapNextDay_input_context
      - validating_daily_planning_seed_boundaries
      - separating_context_seed_from_next_day_plan
      - checking_usage_summary_reference_handling

  - path: .claude/skills/status-merge/templates/status-merge-packet-template.md
    role: operator_facing_template
    status: created
    commit: bb795f81bb30049668104839144fb550ee5cbcc0
    loaded_by_default: false
    read_when:
      - producing_operator_review_packet
      - drafting_merge_proposal_cards
      - surfacing_conflict_notes
      - preparing_next_PreCapNextDay_input_context_section

  - path: .claude/skills/status-merge/examples/apex-minimal-status-merge-example.md
    role: minimal_apex_example
    status: created
    commit: 90f3b1f8c056f4b1af248c46d210443d0e8470e3
    loaded_by_default: false
    read_when:
      - checking_minimal_valid_example
      - demonstrating_one_accepted_delta_and_one_conflict
      - confirming_no_actual_project_kb_mutation
      - showing_next_PreCapNextDay_input_context_seed

  - path: .claude/skills/status-merge/package-manifest.md
    role: package_inventory_and_boundary_manifest
    status: created_in_current_step
    commit: pending_current_commit
    loaded_by_default: false
    read_when:
      - auditing_package_contents
      - checking_source_gaps
      - validating_file_roles
      - confirming_non_runtime_scope

  - path: .claude/skills/status-merge/SKILL.md
    role: skill_entrypoint
    status: created
    commit: live_main_entrypoint_present
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
        - owns_durable_project_record_schema
        - owns_project_registry_and_consumed_recap_record_shapes
        - forbids_schema_drift_outside_project_schema

    - path: .claude/skills/project-kb-manager/references/apex-orchestration-state-packet-contract.md
      status: inspected
      relevance:
        - defines_compact_state_handoff_to_PreCapWeek_and_PreCapNextDay
        - preserves_upstream_owner_boundaries
        - prevents_redefinition_of_upstream_schemas

    - path: .claude/skills/project-kb-manager/templates/apex-orchestration-state-packet-template.md
      status: inspected
      relevance:
        - models_operator_review_first_state_handoff_style
        - uses_refs_short_digests_confidence_notes_and_review_flags
        - avoids_full_database_exposure

    - path: .claude/skills/ProjectStatus/project-status-overview_SKILL_v3.md
      status: inspected
      relevance:
        - owns_current_project_status_overview
        - explicitly_does_not_create_status_merges
        - separates_status_overview_from_daily_weekly_planning

    - path: .claude/skills/flow-recap/references/flow-recap-packet-contract.md
      status: inspected
      relevance:
        - defines_flow_recap_packet_as_candidate_delta_source
        - states_project_status_and_usage_deltas_are_candidate_only
        - routes_status_merge_as_downstream_consumer

    - path: apex-meta/kb/claude-code-orchestration-design/wiki/concepts/status-merge-packet.md
      status: inspected
      relevance:
        - describes_status_merge_as_validated_recap_delta_reconciliation
        - requires_conflicts_to_be_exposed_before_acceptance
        - defines_next_context_seed_without_runtime_implementation

    - path: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-skill-design/sources/operator-supplied/notes/Claude_Skill_Package_BestPractice_Handover.md
      status: inspected
      relevance:
        - defines_skill_package_anatomy
        - forbids_runtime_scheduler_task_board_and_calendar_integration_files
        - constrains_SKILL_md_frontmatter_and_section_order

    - path: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-skill-design/sources/operator-supplied/notes/Claude_Skill_PromptFlow_Design_Guidance_v1.md
      status: inspected
      relevance:
        - requires_description_to_start_with_use_this_skill_when
        - recommends_5_to_8_procedure_steps
        - requires_supporting_files_yaml_and_boolean_completion_gate
```

## Source Gap Register

```yaml
source_gap_register:
  - path: .claude/skills/flow-recap/references/project-status-delta-contract.md
    status: present
    impact: medium
    handling: >
      StatusMerge uses candidate_project_status_delta references from
      flow_recap_packet only. It does not define a separate durable project status
      delta schema.

  - path: .claude/skills/model-usage-log/references/usage-summary-contract.md
    status: present
    impact: medium
    handling: >
      StatusMerge keeps usage summaries as opaque source_usage_summary_refs and
      usage_summary_ref fields. It does not define or validate usage_summary
      internals.
```

## Boundary Register

```yaml
boundary_register:
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

  enforced_rules:
    interface_only: true
    no_runtime: true
    no_scheduler: true
    no_agent: true
    no_calendar_write: true
    no_direct_project_kb_mutation: true
    no_automatic_status_overwrite: true
    durable_writes_operator_gated: true
    durable_writes_project_kb_manager_bound: true
    conflicts_surface_before_acceptance: true
    state_changes_proposal_only_until_confirmed: true
```

## Artifact Coverage

```yaml
artifact_coverage:
  status_merge_packet:
    contract: .claude/skills/status-merge/references/status-merge-packet-contract.md
    template: .claude/skills/status-merge/templates/status-merge-packet-template.md
    example: .claude/skills/status-merge/examples/apex-minimal-status-merge-example.md
    status: covered

  next_PreCapNextDay_input_context:
    contract: .claude/skills/status-merge/references/next-precaphandoff-context-contract.md
    template_section: .claude/skills/status-merge/templates/status-merge-packet-template.md#11-next-precapnextday-input-context
    example_section: .claude/skills/status-merge/examples/apex-minimal-status-merge-example.md#9-next-precapnextday-input-context
    status: covered

  operator_conflict_review_gate:
    contract_section: .claude/skills/status-merge/references/status-merge-packet-contract.md#boundary-validation
    template_sections:
      - .claude/skills/status-merge/templates/status-merge-packet-template.md#2-operator-review-first
      - .claude/skills/status-merge/templates/status-merge-packet-template.md#3-prominent-conflict-notes
    example_section: .claude/skills/status-merge/examples/apex-minimal-status-merge-example.md#4-prominent-conflict--deferred-note
    status: covered

  project_kb_manager_write_boundary:
    contract: .claude/skills/status-merge/references/status-merge-packet-contract.md
    template: .claude/skills/status-merge/templates/status-merge-packet-template.md
    example: .claude/skills/status-merge/examples/apex-minimal-status-merge-example.md
    status: covered
```

## Completion Gate Snapshot

```yaml
completion_gate_snapshot:
  source_files_inspected_or_gaps_recorded: true
  package_path_created: true
  status_merge_packet_contract_created: true
  next_precap_context_contract_created: true
  template_created: true
  apex_minimal_example_created: true
  manifest_created: true
  SKILL_md_created_with_valid_frontmatter: true
  project_kb_manager_boundary_preserved: true
  conflicts_are_surfaced_before_acceptance: true
  no_automatic_status_overwrite_created: true
  next_PreCapNextDay_input_context_is_clear: true
```

## Promoted Operator Templates

```yaml
operator_templates:
  - artifact_id: J9
    path: .claude/skills/status-merge/templates/status-merge-decision-card-template.md
    purpose: Operator-facing presentation template
    read_when: operator_requests_template
```
