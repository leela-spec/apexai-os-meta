Below is the consolidated **one-big-output** version at **macro/meso detail**. It is **machine-readable first, human-readable second**, and applies your correction: **prompt packets should have their own file system, preferably one prompt-pack file per flow containing all prompts for that flow**.

Grounding: the accepted loop is **PreCapWeek → PreCapNextDay → OperatorExecutesPlannedFlow → FlowRecap → AllProjectStatusPacketUpdate/status-merge → next PreCapNextDay**, with DayExecution, FlowExecution, and required RecapDay removed from the core. The accepted architecture also requires real file/file-like artifacts, normalized raw flow dumps, whole-day plans plus per-flow extractable packets, and status-merge producing next PreCapNextDay context. For the Claude-only version, historical Hermes/OpenCLAW/Apex concepts must be translated into Claude-ready files and not drift back into runtime implementation language.

---

# MACHINE-READABLE SPEC

```yaml
document:
  id: apex_alfred_output_artifact_system_v0_2_macro_meso
  title: Apex Alfred Output Artifact System v0.2
  status: validated_decision_synthesis
  detail_level: macro_meso
  target_language: Claude_native
  human_readable_section: second
  created_for: operator
  purpose: >
    Define the core output/delivery artifacts produced by the Apex Alfred
    planning-execution-recap-status loop, including file-system logic,
    producer/consumer contracts, validation gates, and content options for each
    artifact.
  correction_applied:
    corrected_question: Q7_prompt_packet_storage
    previous_default: embedded_inside_flow_packet
    new_decision: per_flow_prompt_pack_file
    meaning: >
      Prompt packets should have a separate file system. The preferred v0.2
      structure is one prompt-pack file per flow containing all prompts for that
      flow. Individual per-prompt files remain an optional later expansion if
      prompt volume or copy-paste handling becomes too heavy.
  explicit_non_goals:
    - no_final_runtime_implementation
    - no_Hermes_runtime_files
    - no_OpenCLAW_runtime_files
    - no_cron_or_task_board_implementation
    - no_micro_level_prompt_text
    - no_exact_absolute_paths_yet
    - no_extra_permanent_agents
```

---

## 0. System boundary

```yaml
system_boundary:
  system_name: Apex Alfred
  target_environment: Claude_Code_authoring_environment
  current_phase: output_artifact_contract_definition
  artifact_style: markdown_files_with_structured_yaml_blocks

  allowed_concepts:
    - Claude_ready_roles
    - Claude_skills
    - Claude_workflow_specs
    - operator_artifacts
    - planning_artifacts
    - flow_artifacts
    - recap_artifacts
    - status_artifacts
    - prompt_pack_artifacts

  forbidden_concepts_in_final_artifacts:
    - Hermes_runtime_profile_mechanics
    - Hermes_Kanban_runtime_mechanics
    - Hermes_cron_runtime_mechanics
    - OpenCLAW_runtime_assumptions
    - generic_agent_swarm_sprawl
    - DayExecution_as_standalone_process
    - FlowExecution_as_standalone_process
    - required_RecapDay_core_layer

  permanent_control_plane_roles:
    alfred:
      role_type: operator_interface
      owns:
        - intake
        - routing
        - handoff_packet_creation
      does_not_own:
        - deep_execution
        - final_validation

    meta_strategist:
      role_type: strategy_head
      owns:
        - goal_interpretation
        - priority_ranking
        - dependency_mapping
        - sequencing

    meta_operations:
      role_type: operations_and_artifact_packaging_head
      owns:
        - workflow_packaging
        - artifact_contracts
        - file_creation_sequence
        - operational_output_structure

    meta_detective_controller:
      role_type: validation_and_drift_control_head
      owns:
        - contradiction_detection
        - role_boundary_validation
        - source_drift_detection
        - completion_criteria_verification
```

---

## 1. Canonical loop

```yaml
canonical_loop:
  name: weekly_daily_flow_recap_status_loop
  status: locked_v0_2

  sequence:
    S1_PreCapWeek:
      function: weekly_strategy_and_constraints
      primary_output:
        - weekly_plan_packet

    S2_PreCapNextDay:
      function: executable_next_day_planning
      primary_outputs:
        - next_day_plan
        - per_flow_packets
        - per_flow_prompt_packs

    S3_OperatorExecutesPlannedFlow:
      function: human_executes_selected_flow
      primary_outputs:
        - raw_flow_dump
        - skipped_flow_marker_if_needed

    S4_FlowRecap:
      function: digest_one_flow_into_structured_memory
      primary_outputs:
        - flow_recap_packet
        - project_status_delta
        - model_usage_delta
        - artifact_index
        - operator_validated_next_step

    S5_StatusMerge:
      function: merge_recaps_into_project_state
      primary_outputs:
        - updated_all_project_status_packet
        - next_PreCapNextDay_input_context
        - consumed_flow_recap_registry
        - updated_usage_summary_optional

    S6_NextCycle:
      function: next_PreCapNextDay_uses_updated_context
      primary_input:
        - next_PreCapNextDay_input_context

  optional_parallel_layer:
    RecapDay:
      status: deferred
      role: personal_evening_reflection_or_Alfred_layer
      not_required_for_project_state_loop: true
```

---

## 2. Fixed daily grammar

```yaml
daily_execution_grammar:
  applies_to: every_execution_day
  source_routine: PreCapNextDay
  execution_layer: operator_executes_flow_directly
  recap_layer: FlowRecap
  merge_layer: StatusMerge

  fixed_flow_order:
    F1:
      project: Leela
      flow_class: product_feature_or_system_definition
      default_goal: fully_define_spatial_system_for_existing_app
      expected_artifact_family:
        - product_system_notes
        - architecture_questions
        - implementation_boundary_candidates

    F2:
      project: MasterOfArts
      flow_class: website_structure_content_design
      default_goal: prepare_MasterOfArts_website
      expected_artifact_family:
        - website_map
        - offer_structure
        - page_copy_blocks
        - design_handoff_notes

    F3:
      project: Apex_Alfred_orchestration
      flow_class: orchestration_process_specification
      default_goal: finalize_process_descriptions_and_artifact_contracts
      expected_artifact_family:
        - process_specs
        - workflow_specs
        - artifact_contracts
        - Claude_ready_file_prompts

    F4:
      project: Residual
      flow_class: priority_recovery_or_deepening
      default_goal: recover_lagging_or_high_value_threads
      composition_options:
        option_A_split_by_project:
          S1: Leela_residual
          S2: MasterOfArts_residual
          S3: Apex_Alfred_residual_plus_day_digest
        option_B_single_lagging_project:
          rule: all_three_sprints_go_to_highest_priority_lagging_project
        option_C_operator_selected:
          rule: operator_selects_residual_focus_during_PreCapNextDay_review
      recommendation: option_A_split_by_project_until_loop_is_proven

  universal_flow_anatomy:
    S1:
      role: work_sprint_1
      purpose: create_first_concrete_output_chunk
      output_options:
        - first_draft
        - research_summary
        - decision_matrix
        - structure_map
        - implementation_candidate

    S2:
      role: work_sprint_2
      purpose: deepen_iterate_translate_or_validate_first_output
      output_options:
        - revised_draft
        - validation_notes
        - second_artifact_chunk
        - implementation_boundary
        - contradiction_report

    S3:
      role: recap_planning_digest_sprint
      purpose: prepare_material_for_FlowRecap
      output_options:
        - raw_dump_material
        - prompt_result_summary
        - model_usage_notes
        - decisions
        - blockers
        - unresolved_questions
        - next_step_guess
```

---

## 3. File-system strategy

```yaml
file_system_strategy:
  status: logical_paths_only_v0_2
  absolute_paths: unresolved_until_Claude_Code_or_operator_confirms_repo_root
  root_placeholder: APEX_ALFRED_ROOT

  primary_principles:
    - artifacts_are_real_markdown_or_yaml_files
    - each_major_process_has_clear_input_and_output_artifacts
    - every_artifact_has_one_primary_producer
    - every_artifact_has_at_least_one_consumer
    - prompt_packets_get_separate_flow_prompt_pack_files
    - flow_packets_are_both_embedded_in_day_plan_and_extractable_per_flow
    - raw_flow_dumps_normalize_messy_input_into_one_file_per_flow
    - status_merge_does_not_silently_trigger_next_day_planning_in_v0_2

  proposed_tree:
    APEX_ALFRED_ROOT:
      docs:
        purpose: system_definition_and_operator_guidance
        possible_files:
          - 00_SYSTEM_INTENT.md
          - 01_DECISION_REGISTER.md
          - 02_ARTIFACT_CONTRACT_REGISTRY.md
          - 03_FILE_TREE_PROPOSAL.md

      artifacts:
        plans:
          weekly:
            purpose: weekly_plan_packets
            pattern: "{week_id}.md"
          daily:
            purpose: next_day_plans
            pattern: "{execution_day_id}.md"

        flows:
          packets:
            purpose: extractable_per_flow_packets
            pattern: "{execution_day_id}/{flow_id}.md"
          prompt_packs:
            purpose: one_prompt_pack_file_per_flow
            pattern: "{execution_day_id}/{flow_id}-prompt-pack.md"
          raw:
            purpose: raw_flow_dumps
            pattern: "{execution_day_id}/{flow_id}-raw-dump.md"
          skipped:
            purpose: skipped_flow_markers
            pattern: "{execution_day_id}/{flow_id}-skipped.md"

        recaps:
          flows:
            purpose: flow_recap_packets
            pattern: "{execution_day_id}/{flow_id}-recap.md"

        status:
          current:
            purpose: current_all_project_status_packet
            pattern: "all-project-status-current.md"
          archive:
            purpose: historical_status_snapshots
            pattern: "{execution_day_id}-all-project-status.md"

        context:
          purpose: next_cycle_planning_context
          possible_files:
            - next-precapnextday-input-context.md

        registry:
          purpose: deduplication_and_traceability
          possible_files:
            - consumed-flow-recaps-registry.md
            - artifact-index-current.md

        usage:
          purpose: model_and_AI_surface_usage_memory
          possible_files:
            - model-usage-summary-current.md
            - model-usage-archive.md

        config:
          purpose: operator_maintained_routing_config
          possible_files:
            - ai-surface-inventory.md
            - project-inventory.md

  prompt_pack_storage_decision:
    chosen: one_file_per_flow_prompt_pack
    rejected_options:
      embedded_only:
        reason: too_hard_to_extract_and_reuse_prompts_during_execution
      one_file_per_prompt_initially:
        reason: likely_too_many_files_for_v0_2
      one_big_day_prompt_file:
        reason: loses_flow_boundary_and_makes_recap_mapping_weaker
    later_options:
      per_prompt_files:
        use_if:
          - prompt_volume_is_high
          - copy_paste_friction_is_high
          - prompt_evaluation_needs_prompt_level_history
      database_or_table:
        use_if:
          - usage_tracking_becomes_quantitative
          - prompt_library_becomes_large
```

---

## 4. Artifact registry

```yaml
artifact_registry:
  A1_weekly_plan_packet:
    artifact_name: weekly_plan_packet
    primary_producer: PreCapWeek
    primary_consumers:
      - PreCapNextDay
      - operator
    logical_location: artifacts/plans/weekly/{week_id}.md
    format: markdown_with_yaml_blocks
    validation_gate: G1_weekly_plan_validation
    required: true_after_weekly_planning

  A2_next_day_plan:
    artifact_name: next_day_plan
    primary_producer: PreCapNextDay
    primary_consumers:
      - operator
      - FlowRecap
      - StatusMerge_indirect
    logical_location: artifacts/plans/daily/{execution_day_id}.md
    format: markdown_with_yaml_blocks
    validation_gate: G2_next_day_plan_validation
    required: true_before_flow_execution

  A3_flow_packet:
    artifact_name: flow_packet
    primary_producer: PreCapNextDay
    primary_consumers:
      - operator
      - FlowRecap
    logical_location: artifacts/flows/packets/{execution_day_id}/{flow_id}.md
    format: markdown_with_yaml_blocks
    validation_gate: inherits_G2
    required: true_per_flow

  A4_flow_prompt_pack:
    artifact_name: flow_prompt_pack
    primary_producer: PreCapNextDay
    primary_consumers:
      - operator
      - FlowRecap
      - model_usage_log
    logical_location: artifacts/flows/prompt_packs/{execution_day_id}/{flow_id}-prompt-pack.md
    format: markdown_with_yaml_blocks_and_prompt_templates
    validation_gate: inherits_G2
    required: true_per_flow_if_AI_prompts_are_used
    correction_note: >
      This supersedes embedded-only prompt packets. Prompt packets may still be
      summarized in the flow packet, but the operational prompt material lives
      in a separate per-flow prompt-pack file.

  A5_raw_flow_dump:
    artifact_name: raw_flow_dump
    primary_producer: operator
    primary_consumers:
      - FlowRecap
    logical_location: artifacts/flows/raw/{execution_day_id}/{flow_id}-raw-dump.md
    format: messy_or_structured_markdown_with_minimum_metadata
    validation_gate: G3_flow_done_or_skipped_gate
    required: true_for_completed_or_partially_completed_flow

  A6_skipped_flow_marker:
    artifact_name: skipped_flow_marker
    primary_producer:
      - operator
      - FlowRecap
      - StatusMerge
    primary_consumers:
      - StatusMerge
      - PreCapNextDay
    logical_location: artifacts/flows/skipped/{execution_day_id}/{flow_id}-skipped.md
    format: markdown_or_yaml
    validation_gate: G3_flow_done_or_skipped_gate
    required: true_for_skipped_or_blocked_flow_without_raw_dump

  A7_flow_recap_packet:
    artifact_name: flow_recap_packet
    primary_producer: FlowRecap
    primary_consumers:
      - StatusMerge
      - PreCapNextDay_indirect
      - model_usage_log
    logical_location: artifacts/recaps/flows/{execution_day_id}/{flow_id}-recap.md
    format: markdown_with_structured_yaml_blocks
    validation_gate: G4_flow_recap_next_step_validation
    required: true_before_status_merge_for_completed_flow

  A8_project_status_delta:
    artifact_name: project_status_delta
    primary_producer: FlowRecap
    primary_consumers:
      - StatusMerge
    logical_location: section_inside_flow_recap_packet
    format: yaml_block
    validation_gate: G4_status_delta_validation
    required: true_inside_flow_recap

  A9_model_usage_delta:
    artifact_name: model_usage_delta
    primary_producer: FlowRecap
    primary_consumers:
      - model_usage_log
      - StatusMerge_optional
      - PreCapNextDay_indirect
    logical_location: section_inside_flow_recap_packet
    format: yaml_block
    validation_gate: G4_or_low_friction_capture
    required: recommended

  A10_updated_all_project_status_packet:
    artifact_name: updated_all_project_status_packet
    primary_producer: StatusMerge
    primary_consumers:
      - PreCapNextDay
      - PreCapWeek
      - operator
    logical_location: artifacts/status/current/all-project-status-current.md
    archive_location: artifacts/status/archive/{execution_day_id}-all-project-status.md
    format: markdown_with_yaml_blocks
    validation_gate: G5_selective_status_merge_validation
    required: true_after_status_merge

  A11_next_PreCapNextDay_input_context:
    artifact_name: next_PreCapNextDay_input_context
    primary_producer: StatusMerge
    primary_consumers:
      - PreCapNextDay
      - operator
    logical_location: artifacts/context/next-precapnextday-input-context.md
    format: markdown_with_yaml_blocks
    validation_gate: G5_if_conflict_or_high_impact
    required: recommended_after_each_status_merge

  A12_consumed_flow_recap_registry:
    artifact_name: consumed_flow_recap_registry
    primary_producer: StatusMerge
    primary_consumers:
      - StatusMerge_next_run
    logical_location: artifacts/registry/consumed-flow-recaps-registry.md
    format: yaml_or_markdown_table
    validation_gate: internal_consistency_check
    required: true_after_first_status_merge

  A13_usage_summary:
    artifact_name: usage_summary
    primary_producer:
      - model_usage_log
      - StatusMerge_optional
    primary_consumers:
      - PreCapNextDay
      - operator
    logical_location: artifacts/usage/model-usage-summary-current.md
    format: markdown_or_yaml
    validation_gate: low_friction_operator_review_optional
    required: optional_v0_2_recommended

  A14_AI_surface_inventory:
    artifact_name: AI_surface_inventory
    primary_producer: operator
    primary_consumers:
      - PreCapNextDay
      - flow_prompt_pack_generation
      - usage_summary
    logical_location: artifacts/config/ai-surface-inventory.md
    format: markdown_or_yaml
    validation_gate: operator_maintained
    required: recommended_for_routing_quality

  A15_artifact_index:
    artifact_name: artifact_index
    primary_producer:
      - FlowRecap
      - StatusMerge
    primary_consumers:
      - operator
      - PreCapNextDay
      - future_search_or_review
    logical_location: artifacts/registry/artifact-index-current.md
    format: markdown_table_or_yaml
    validation_gate: optional
    required: optional_v0_2_recommended
```

---

## 5. Artifact content contracts

### 5.1 Weekly plan packet

```yaml
weekly_plan_packet:
  artifact_id: A1
  macro_purpose: >
    Define the weekly strategic container and constraints that daily planning
    must obey.

  required_sections:
    document_metadata:
      options:
        - week_id
        - producer
        - source_status_packet_ref
        - operator_validation_status
        - created_at

    weekly_intent:
      options:
        - one_sentence_week_goal
        - main_week_theme
        - not_this_week_list
        - weekly_success_condition
        - weekly_failure_condition

    project_priorities:
      options:
        - Leela_priority
        - MasterOfArts_priority
        - Apex_Alfred_priority
        - Residual_priority_logic
        - urgency_notes
        - leverage_notes
        - dependencies

    weekly_constraints:
      options:
        - calendar_constraints
        - energy_constraints
        - model_subscription_constraints
        - external_commitments
        - project_blockers
        - unavailable_days

    day_by_day_direction:
      options:
        - execution_day_candidates
        - expected_day_focus
        - maximum_flow_load
        - recovery_days
        - flexible_slots

    first_PreCapNextDay_seed:
      options:
        - target_execution_day
        - first_day_goals
        - required_inputs
        - warnings
        - special_operator_notes

    operator_validation:
      options:
        - approved
        - approved_with_edits
        - rejected
        - blocked
        - corrections
        - timestamp

  missing_input_behavior:
    missing_project_status: ask_operator_for_brief_project_state_or_mark_first_cycle
    missing_calendar: create_calendar_unverified_week_plan
    missing_operator_intent: infer_from_status_packet_but_mark_low_confidence

  validation_rule: operator_must_approve_before_PreCapNextDay_uses_it
```

### 5.2 Next day plan

```yaml
next_day_plan:
  artifact_id: A2
  macro_purpose: >
    Convert the weekly plan and current project state into one executable day
    with four flows and clear handoff material.

  required_sections:
    document_metadata:
      options:
        - execution_day_id
        - target_calendar_date
        - source_weekly_plan_ref
        - source_status_packet_ref
        - source_next_day_context_ref
        - validation_status

    day_intent:
      options:
        - one_sentence_day_goal
        - expected_day_outputs
        - risk_notes
        - energy_notes
        - calendar_notes

    input_basis:
      options:
        - weekly_plan_used
        - project_status_used
        - flow_recaps_used
        - skipped_markers_used
        - usage_summary_used
        - AI_surface_inventory_used

    flow_overview:
      options:
        - F1_summary
        - F2_summary
        - F3_summary
        - F4_summary
        - flow_feasibility
        - priority_order
        - optional_flow_reduction_if_day_is_short

    file_links:
      options:
        - per_flow_packet_refs
        - per_flow_prompt_pack_refs
        - raw_dump_target_slots
        - recap_target_slots

    operator_execution_instructions:
      options:
        - execute_flows_in_order
        - may_override_order_with_reason
        - after_each_flow_create_raw_dump
        - if_skipped_create_skipped_marker
        - run_FlowRecap_after_each_completed_or_partial_flow

    operator_validation:
      options:
        - approved
        - approved_with_edits
        - rejected
        - blocked
        - corrections

  validation_rule: operator_must_approve_before_execution
```

### 5.3 Flow packet

```yaml
flow_packet:
  artifact_id: A3
  macro_purpose: >
    Give the operator one clean executable packet for one flow.

  required_sections:
    document_metadata:
      options:
        - execution_day_id
        - flow_id
        - project_id
        - fixed_flow_position
        - linked_next_day_plan
        - linked_prompt_pack

    flow_intent:
      options:
        - flow_goal
        - why_this_flow_now
        - expected_output_family
        - definition_of_done
        - project_status_target

    context_instructions:
      options:
        - required_files
        - useful_previous_artifacts
        - project_context_notes
        - do_not_use_sources
        - missing_context_warnings

    sprint_plan:
      S1_options:
        - goal
        - operator_actions
        - expected_outputs
        - prompt_ids_from_prompt_pack
        - completion_signal
      S2_options:
        - goal
        - operator_actions
        - expected_outputs
        - prompt_ids_from_prompt_pack
        - completion_signal
      S3_options:
        - recap_preparation_goal
        - raw_dump_items_to_collect
        - decisions_to_record
        - blockers_to_record
        - next_step_guess_instruction
        - model_usage_capture_instruction

    linked_artifacts:
      options:
        - prompt_pack_ref
        - raw_dump_slot
        - flow_recap_slot
        - skipped_marker_slot

    FlowRecap_handoff:
      options:
        - when_to_run
        - required_inputs
        - validation_question
        - expected_recap_outputs

  validation_rule: inherited_from_next_day_plan_operator_approval
```

### 5.4 Flow prompt pack

```yaml
flow_prompt_pack:
  artifact_id: A4
  macro_purpose: >
    Store all prompt packets for one flow in a separate operational file so the
    operator can execute prompts cleanly and FlowRecap can evaluate them later.

  file_granularity:
    chosen: one_file_per_flow
    contains: all_prompts_for_S1_S2_S3_of_that_flow
    optional_future_expansion: one_file_per_prompt_if_prompt_volume_requires_it

  required_sections:
    document_metadata:
      options:
        - execution_day_id
        - flow_id
        - project_id
        - linked_flow_packet
        - linked_next_day_plan
        - producer
        - status

    routing_assumptions:
      options:
        - available_AI_surfaces
        - preferred_surface
        - fallback_surface
        - scarce_mode_policy
        - budget_or_quota_notes
        - operator_override_allowed

    prompt_index:
      options:
        - prompt_id
        - sprint_id
        - purpose
        - suggested_surface
        - expected_output
        - priority
        - cost_class
        - copy_paste_ready_status

    prompt_packets:
      per_prompt_options:
        - prompt_id
        - sprint_id
        - task_goal
        - context_to_paste_or_attach
        - exact_or_rough_prompt_text
        - output_format_request
        - expected_output
        - fallback_prompt
        - capture_instruction
        - model_usage_capture_fields

    synthesis_instructions:
      options:
        - how_to_combine_prompt_outputs
        - what_to_keep
        - what_to_discard
        - what_to_move_to_raw_dump
        - what_to_include_in_FlowRecap

    usage_capture_template:
      options:
        - planned_surface
        - actual_surface
        - model_or_mode
        - result_quality
        - repeat_route
        - failure_mode
        - quota_notes

  content_options_by_prompt_type:
    research_prompt:
      include:
        - source_requirements
        - citation_requirements
        - recency_requirements
        - synthesis_format
    design_prompt:
      include:
        - constraints
        - options
        - tradeoffs
        - recommendation
    validation_prompt:
      include:
        - acceptance_criteria
        - contradiction_checks
        - source_alignment_checks
        - correction_output_format
    drafting_prompt:
      include:
        - tone_constraints
        - structure_constraints
        - preserve_vs_change_rules
        - output_format
    implementation_prompt:
      include:
        - target_file
        - input_context
        - boundary_conditions
        - verification_steps

  missing_input_behavior:
    no_AI_surface_inventory: use_generic_surface_labels_and_mark_low_confidence
    prompt_unclear: operator_or_meta_operations_refines_before_execution
    high_cost_mode_unavailable: use_fallback_route_and_record_quality_delta

  validation_rule: reviewed_as_part_of_next_day_plan_gate
```

### 5.5 Raw flow dump

```yaml
raw_flow_dump:
  artifact_id: A5
  macro_purpose: >
    Normalize messy execution evidence into one file per flow so FlowRecap has a
    stable input.

  accepted_input_forms:
    - pasted_chat_history
    - uploaded_markdown
    - linked_AI_chats
    - copied_prompt_outputs
    - file_paths
    - artifact_references
    - screenshots_described_by_operator
    - voice_notes_transcribed
    - operator_notes
    - decisions
    - blockers
    - unfinished_items
    - next_step_guess

  required_minimum_fields:
    - execution_day_id
    - flow_id
    - project_id
    - completion_state
    - what_was_done
    - outputs_created_or_missing
    - blockers_or_unresolved_items
    - prompt_outputs_or_note_that_no_prompts_were_used
    - model_usage_if_known
    - operator_next_step_guess_if_known

  optional_sections:
    - raw_chat_logs
    - prompt_output_fragments
    - artifact_list
    - decisions
    - rejected_ideas
    - emotional_or_energy_notes
    - quality_self_assessment
    - questions_for_FlowRecap

  missing_input_behavior:
    missing_flow_id: infer_only_if_obvious_else_ask_operator
    too_sparse: create_minimal_recap_with_validation_needed
    no_work_done: create_skipped_flow_marker_instead
    no_model_usage: mark_unknown_not_blocking
```

### 5.6 Skipped flow marker

```yaml
skipped_flow_marker:
  artifact_id: A6
  macro_purpose: >
    Make skipped, blocked, or moved work visible to StatusMerge and next
    PreCapNextDay.

  required_sections:
    document_metadata:
      options:
        - execution_day_id
        - flow_id
        - project_id
        - producer
        - created_at

    skip_state:
      options:
        - skipped
        - blocked
        - moved_to_next_day
        - moved_to_residual
        - intentionally_cancelled

    reason:
      options:
        - time_constraint
        - energy_constraint
        - missing_input
        - higher_priority_override
        - blocked_by_external_dependency
        - operator_choice
        - scope_too_large

    recovery_logic:
      options:
        - recover_next_execution_day
        - move_to_F4_residual
        - drop_until_weekly_review
        - needs_operator_decision
        - convert_to_smaller_flow

    status_impact:
      options:
        - no_progress
        - blocker_created
        - priority_increased
        - priority_decreased
        - dependency_changed
        - no_status_change

  validation_rule: operator_confirms_skip_or_block_state
```

### 5.7 Flow recap packet

```yaml
flow_recap_packet:
  artifact_id: A7
  macro_purpose: >
    Convert one flow’s plan and raw dump into structured memory, status delta,
    artifact index, prompt/model learning, and next-step proposal.

  required_sections:
    document_metadata:
      options:
        - flow_recap_id
        - execution_day_id
        - flow_id
        - project_id
        - producer
        - validation_status

    source_references:
      options:
        - next_day_plan_ref
        - flow_packet_ref
        - flow_prompt_pack_ref
        - raw_flow_dump_ref
        - previous_status_packet_ref
        - previous_flow_recap_refs

    completion_state:
      options:
        - completed
        - partially_completed
        - skipped
        - blocked
        - aborted
        - moved_to_next_day

    planned_vs_actual:
      options:
        - planned_goal
        - actual_result
        - expected_outputs_completed
        - expected_outputs_missing
        - scope_changes
        - deviations

    sprint_level_summary:
      options:
        - S1_summary
        - S2_summary
        - S3_summary
        - sprint_quality_notes
        - sprint_outputs

    artifact_index:
      options:
        - created
        - edited
        - reused
        - discarded
        - missing
        - should_promote_to_project_context

    prompt_result_summary:
      options:
        - prompt_id
        - planned_route
        - actual_route
        - result_quality
        - reusable_fragments
        - failure_modes
        - should_repeat_route

    project_status_delta:
      options:
        - progress_delta
        - blocker_delta
        - decision_delta
        - artifact_delta
        - priority_delta
        - next_executable_chunk
        - confidence

    model_usage_delta:
      options:
        - surface_used
        - model_or_mode_used
        - scarce_mode_used
        - quality
        - route_learning
        - quota_notes

    reusable_learning:
      options:
        - what_worked
        - what_failed
        - prompt_lessons
        - planning_lessons
        - context_missing_next_time

    next_step_proposal:
      options:
        - recommended_next_step
        - alternative_next_steps
        - dependencies
        - urgency
        - suggested_flow_slot

    operator_validation:
      options:
        - accepted
        - edited
        - rejected
        - uncertain
        - needs_more_review

  special_rules:
    ordinary_flows:
      applies_to:
        - F1
        - F2
        - F3
      status_delta: one_primary_project_delta

    residual_flow:
      applies_to:
        - F4
      status_delta_options:
        split_by_sprint_project:
          S1: Leela_delta
          S2: MasterOfArts_delta
          S3: Apex_Alfred_delta
        single_focus:
          rule: if_residual_was_one_project_only_then_one_delta
      validation: operator_confirms_delta_mapping

  validation_rule: no_flow_recap_complete_until_operator_validates_next_step_and_status_delta
```

### 5.8 Updated all-project status packet

```yaml
updated_all_project_status_packet:
  artifact_id: A10
  macro_purpose: >
    Maintain canonical cross-project state for planning.

  required_sections:
    document_metadata:
      options:
        - status_packet_id
        - created_at
        - producer
        - source_recap_refs
        - source_skipped_marker_refs
        - previous_status_packet_ref

    consumed_inputs:
      options:
        - consumed_flow_recaps
        - skipped_markers
        - model_usage_summary
        - operator_merge_notes
        - conflicts_detected

    project_status_entries:
      Leela_options:
        - current_state
        - next_executable_chunks
        - blockers
        - artifacts
        - decisions
        - priority
        - confidence
      MasterOfArts_options:
        - current_state
        - next_executable_chunks
        - blockers
        - artifacts
        - decisions
        - priority
        - confidence
      Apex_Alfred_options:
        - current_state
        - next_executable_chunks
        - blockers
        - artifacts
        - decisions
        - priority
        - confidence
      Residual_options:
        - unresolved_residue
        - recovery_candidates
        - next_residual_focus_options

    priority_or_urgency_changes:
      options:
        - project
        - previous_priority
        - new_priority
        - reason
        - confidence
        - needs_operator_review

    unresolved_conflicts:
      options:
        - conflicting_recaps
        - conflicting_next_steps
        - uncertain_status_delta
        - missing_artifact_reference
        - operator_decision_required

    next_PreCapNextDay_context_pointer:
      options:
        - generated_context_file_ref
        - included_inline_context
        - missing_inputs_for_next_plan

  validation_gate:
    default: selective
    operator_review_required_if:
      - conflict_detected
      - skipped_flow_ambiguity
      - high_impact_priority_change
      - uncertain_status_delta
      - missing_required_status_input
```

### 5.9 Next PreCapNextDay input context

```yaml
next_PreCapNextDay_input_context:
  artifact_id: A11
  macro_purpose: >
    Give the next daily planning cycle a compact, high-signal planning seed.

  required_sections:
    document_metadata:
      options:
        - target_execution_day_candidate
        - source_status_packet_ref
        - source_usage_summary_ref
        - created_at

    planning_seed:
      options:
        - preserved_weekly_goal
        - latest_project_state_summary
        - skipped_flows_to_recover
        - blockers_to_respect
        - priority_shifts
        - residual_flow_recommendation

    next_executable_chunks:
      options:
        - Leela_next_chunk
        - MasterOfArts_next_chunk
        - Apex_Alfred_next_chunk
        - Residual_candidates

    routing_recommendations:
      options:
        - high_reasoning_needed_for
        - standard_model_ok_for
        - avoid_deep_research_for
        - prompt_routes_to_repeat
        - prompt_routes_to_avoid

    missing_inputs:
      options:
        - missing_project_context
        - missing_calendar_constraints
        - missing_AI_surface_inventory
        - missing_raw_dump_or_recap

    operator_review_flags:
      options:
        - decisions_needed_before_planning
        - project_conflicts
        - blocked_flows
        - high_impact_uncertainties

  validation_rule: reviewed_during_next_PreCapNextDay_if_flags_exist
```

### 5.10 Usage summary

```yaml
usage_summary:
  artifact_id: A13
  macro_purpose: >
    Track planned vs actual AI surface/model usage so PreCapNextDay can route
    future prompts better.

  required_sections:
    document_metadata:
      options:
        - summary_id
        - date_range
        - source_flow_recaps
        - producer

    usage_table:
      options:
        - prompt_id
        - flow_id
        - sprint_id
        - planned_surface
        - actual_surface
        - model_or_mode
        - cost_class
        - result_quality
        - repeat_route
        - failure_mode

    scarce_mode_log:
      options:
        - high_reasoning_uses
        - deep_research_uses
        - expensive_context_uses
        - questionable_uses
        - justified_uses

    route_learning:
      options:
        - route_successes
        - route_weaknesses
        - project_specific_routing_lessons
        - prompt_type_lessons

    recommendations:
      options:
        - use_high_reasoning_for
        - use_standard_model_for
        - avoid_external_research_for
        - save_deep_research_for
        - update_AI_surface_inventory

  validation_rule: low_friction_optional_operator_review
```

### 5.11 AI surface inventory

```yaml
AI_surface_inventory:
  artifact_id: A14
  macro_purpose: >
    Maintain the operator’s available AI tools, surfaces, modes, and routing
    constraints.

  required_sections:
    document_metadata:
      options:
        - inventory_id
        - last_reviewed
        - producer
        - status

    available_surfaces:
      per_surface_options:
        - surface_id
        - surface_name
        - best_use_cases
        - weak_use_cases
        - constraints
        - scarcity
        - cost_or_subscription_notes
        - access_notes

    routing_defaults:
      options:
        - architecture_reasoning_default
        - writing_default
        - validation_default
        - external_research_default
        - code_or_repo_default
        - low_cost_default

    scarcity_policy:
      options:
        - reserve_high_reasoning_for
        - reserve_deep_research_for
        - avoid_high_cost_for
        - operator_override_rule

    known_route_lessons:
      options:
        - task_type
        - recommended_surface
        - avoid_surface
        - evidence_from_usage_summary

  validation_rule: operator_maintained_update_when_tools_or_subscription_context_changes
```

### 5.12 Consumed flow recap registry

```yaml
consumed_flow_recap_registry:
  artifact_id: A12
  macro_purpose: >
    Prevent status merge from consuming the same flow recap multiple times.

  required_sections:
    document_metadata:
      options:
        - registry_id
        - last_updated
        - producer

    consumed_recaps:
      per_entry_options:
        - flow_recap_id
        - execution_day_id
        - flow_id
        - project_id
        - consumed_into_status_packet
        - consumed_at
        - status

    pending_recaps:
      options:
        - detected_but_not_consumed
        - blocked
        - missing_validation
        - skipped

    duplicate_detection:
      options:
        - duplicate_recap_id
        - duplicate_artifact_path
        - conflicting_versions
        - resolution

  validation_rule: internal_consistency_check_during_StatusMerge
```

---

## 6. Process-stage contracts

```yaml
process_stage_contracts:
  PreCapWeek:
    produces:
      - A1_weekly_plan_packet
    consumes_options:
      - previous_A10_updated_all_project_status_packet
      - previous_week_summary
      - operator_weekly_intent
      - calendar_constraints
      - A14_AI_surface_inventory
    validation:
      gate: G1
      strictness: always_required
    failure_modes:
      missing_status_packet: first_cycle_fallback
      unclear_weekly_intent: ask_operator
      calendar_missing: mark_calendar_unverified

  PreCapNextDay:
    produces:
      - A2_next_day_plan
      - A3_flow_packet_per_flow
      - A4_flow_prompt_pack_per_flow
    consumes_options:
      - A1_weekly_plan_packet
      - A10_updated_all_project_status_packet
      - A11_next_PreCapNextDay_input_context
      - A6_skipped_flow_markers
      - A13_usage_summary
      - A14_AI_surface_inventory
      - calendar_constraints
    validation:
      gate: G2
      strictness: always_required
    failure_modes:
      missing_AI_surface_inventory: use_generic_routes_and_mark_low_confidence
      missing_status_packet: first_cycle_fallback
      too_many_flow_items: reduce_scope_or_use_F4_residual

  OperatorExecutesPlannedFlow:
    produces:
      - A5_raw_flow_dump
      - A6_skipped_flow_marker_if_needed
    consumes:
      - A2_next_day_plan
      - A3_selected_flow_packet
      - A4_selected_flow_prompt_pack
    validation:
      gate: G3
      strictness: always_required
    failure_modes:
      flow_skipped: create_skipped_flow_marker
      flow_partial: create_raw_dump_and_mark_partial
      no_prompt_used: raw_dump_notes_manual_work

  FlowRecap:
    produces:
      - A7_flow_recap_packet
      - A8_project_status_delta_inside_recap
      - A9_model_usage_delta_inside_recap
      - A15_artifact_index_optional
    consumes:
      - A3_flow_packet
      - A4_flow_prompt_pack
      - A5_raw_flow_dump
      - A10_status_packet_optional
    validation:
      gate: G4
      strictness: next_step_and_status_delta_required
    failure_modes:
      raw_dump_missing: request_dump_or_create_skipped_marker
      status_delta_unclear: mark_validation_needed
      residual_delta_ambiguous: ask_operator_to_map_sprints_to_projects

  StatusMerge:
    produces:
      - A10_updated_all_project_status_packet
      - A11_next_PreCapNextDay_input_context
      - A12_consumed_flow_recap_registry
      - A13_usage_summary_optional
    consumes:
      - A7_flow_recap_packets_since_last_merge
      - A6_skipped_flow_markers
      - previous_A10_status_packet
      - A12_consumed_registry
      - A13_usage_summary_optional
    validation:
      gate: G5
      strictness: selective
    failure_modes:
      conflicting_recaps: require_operator_review
      duplicate_recaps: use_registry_and_report
      missing_previous_status: first_cycle_fallback
      high_impact_priority_change: require_operator_review
```

---

## 7. Validation gates

```yaml
validation_gates:
  G1_weekly_plan_validation:
    applies_to:
      - weekly_plan_packet
    operator_required: true
    pass_states:
      - approved
      - approved_with_edits
    fail_states:
      - rejected
      - blocked
    checks:
      - weekly_goals_correct
      - project_priorities_correct
      - constraints_respected
      - first_daily_seed_usable

  G2_next_day_plan_validation:
    applies_to:
      - next_day_plan
      - flow_packets
      - flow_prompt_packs
    operator_required: true
    pass_states:
      - approved
      - approved_with_edits
    checks:
      - execution_day_correct
      - four_flows_feasible
      - prompt_packs_useful
      - AI_routes_acceptable
      - raw_dump_instructions_clear
      - F4_residual_logic_correct

  G3_flow_done_or_skipped_gate:
    applies_to:
      - raw_flow_dump
      - skipped_flow_marker
    operator_required: true
    checks:
      - flow_state_explicit
      - raw_dump_exists_if_work_done
      - skipped_marker_exists_if_skipped
      - blockers_recorded_if_blocked

  G4_flow_recap_validation:
    applies_to:
      - flow_recap_packet
      - project_status_delta
      - next_step_proposal
    operator_required: true
    pass_states:
      - next_step_accepted
      - next_step_edited
      - next_step_marked_uncertain
    checks:
      - planned_vs_actual_correct
      - artifact_index_complete_enough
      - project_status_delta_correct
      - next_step_not_invented
      - residual_sprint_delta_mapping_correct_if_F4

  G5_status_merge_validation:
    applies_to:
      - updated_all_project_status_packet
      - next_PreCapNextDay_input_context
    operator_required: selective
    required_if:
      - conflict_detected
      - high_impact_priority_change
      - skipped_flow_ambiguity
      - status_delta_low_confidence
      - missing_required_input
    checks:
      - no_duplicate_recap_consumption
      - project_states_updated_correctly
      - next_day_context_is_usable
      - unresolved_conflicts_explicit
```

---

## 8. Options library for artifact contents

```yaml
artifact_content_options_library:
  priority_fields:
    options:
      - impact
      - urgency
      - dependency
      - effort
      - strategic_value
      - emotional_energy_required
      - risk_if_delayed
      - compounding_value

  context_fields:
    options:
      - project_id
      - repo_or_workspace
      - source_files
      - previous_artifacts
      - external_links
      - operator_notes
      - constraints
      - known_failure_modes
      - examples_to_follow
      - examples_to_avoid

  prompt_pack_fields:
    options:
      - prompt_id
      - prompt_goal
      - prompt_type
      - sprint_id
      - expected_output
      - suggested_AI_surface
      - suggested_model_or_mode
      - reasoning_depth
      - context_to_include
      - context_to_exclude
      - exact_prompt_text
      - rough_prompt_template
      - fallback_prompt
      - output_capture_instruction
      - quality_check
      - usage_capture

  raw_dump_fields:
    options:
      - what_happened
      - what_was_created
      - what_was_changed
      - what_was_rejected
      - prompt_outputs
      - model_usage
      - blockers
      - unresolved_questions
      - decisions
      - next_step_guess
      - emotional_or_energy_notes
      - links_or_paths
      - screenshots_or_visual_notes

  recap_fields:
    options:
      - source_references
      - planned_vs_actual
      - sprint_summaries
      - artifact_index
      - prompt_quality_summary
      - model_usage_delta
      - project_status_delta
      - blockers
      - unresolved_questions
      - reusable_learning
      - next_step_proposal
      - operator_validation

  status_fields:
    options:
      - current_state
      - latest_progress
      - next_executable_chunks
      - active_blockers
      - unresolved_questions
      - decisions_made
      - artifacts_created
      - priority
      - urgency
      - confidence
      - stale_context_warning
      - next_PreCapNextDay_seed

  validation_fields:
    options:
      - validation_required
      - validation_owner
      - pass_condition
      - fail_condition
      - open_questions
      - confidence
      - source_conflict
      - correction_needed
      - operator_decision
```

---

## 9. Recommended build order

```yaml
recommended_build_order:
  phase_0_contracts:
    purpose: define artifact system_before_runtime_or_skill_implementation
    outputs:
      - this_artifact_system_spec
      - artifact_contract_registry
      - file_tree_proposal

  phase_1_minimal_artifact_templates:
    purpose: create macro_meso_templates_for_core_outputs
    outputs:
      - weekly_plan_packet_template
      - next_day_plan_template
      - flow_packet_template
      - flow_prompt_pack_template
      - raw_flow_dump_template
      - flow_recap_packet_template
      - status_packet_template
      - next_PreCapNextDay_context_template

  phase_2_core_Claude_skills:
    purpose: define reusable procedures that produce or process artifacts
    outputs:
      - precap-week_skill
      - precap-next-day_skill
      - flow-recap_skill
      - status-merge_skill
      - prompt-pack-writer_skill

  phase_3_workflow_specs:
    purpose: define how skills and roles interact
    outputs:
      - weekly_to_daily_planning_workflow
      - flow_execution_to_recap_workflow
      - recap_to_status_merge_workflow
      - status_to_next_day_context_workflow

  phase_4_example_run:
    purpose: test artifact chain on one example execution day
    outputs:
      - example_weekly_plan_packet
      - example_next_day_plan
      - four_example_flow_packets
      - four_example_flow_prompt_packs
      - one_example_raw_flow_dump
      - one_example_flow_recap
      - one_example_status_packet

  phase_5_revision:
    purpose: patch contracts based_on_example_failure_modes
    outputs:
      - updated_artifact_registry
      - updated_templates
      - updated_skills
```

---

# HUMAN-READABLE SUMMARY

## Core decision

The system should be built around **durable artifact files**, not vague memory or hidden chat state. The main artifact chain is:

```text
weekly plan
→ next day plan
→ per-flow packet
→ per-flow prompt pack
→ raw flow dump
→ flow recap
→ all-project status packet
→ next PreCapNextDay input context
```

The most important correction is that **prompt packets should get their own artifact layer**. The best v0.2 structure is:

```text
one prompt-pack file per flow
```

Not embedded-only, and not one separate file per individual prompt yet.

---

## Recommended prompt file strategy

|Option|Assessment|
|---|---|
|**Embedded only in flow packet**|Too cramped. Hard to execute and hard to evaluate later.|
|**One file per prompt**|Precise but likely creates too many files too early.|
|**One file with all prompts for one flow**|Best current option. Keeps flow boundary clean and execution manageable.|
|**One big prompt file for the whole day**|Too broad; makes FlowRecap mapping weaker.|

**Recommended:** `artifacts/flows/prompt_packs/{execution_day_id}/{flow_id}-prompt-pack.md`

Each prompt pack can contain:

- prompt index
    
- prompt IDs
    
- sprint mapping
    
- suggested AI surface/model
    
- exact or rough prompt text
    
- expected output
    
- fallback prompt
    
- capture instructions
    
- usage tracking fields
    

---

## Practical artifact interpretation

**PreCapWeek** creates the weekly strategic frame.

**PreCapNextDay** converts that frame into the next executable day. It produces:

- one daily plan
    
- four flow packets
    
- four prompt-pack files
    

**OperatorExecutesPlannedFlow** is not an autonomous process. It is you doing the work, then dumping the evidence into one raw markdown file.

**FlowRecap** converts that raw dump into durable structured memory.

**StatusMerge** updates the project state and writes the next planning context.

---

## Highest-value next file to create

The next best actual file is:

```text
03_ARTIFACT_CONTRACT_REGISTRY.md
```

It should contain the artifact registry above in a more formal file-ready version. That file becomes the source of truth for all future Claude skills and workflow specs.