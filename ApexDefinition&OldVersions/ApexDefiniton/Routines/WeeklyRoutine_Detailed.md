# Information-Process Architecture — Next Work Plan v0.1

```yaml
document:
  id: info-process-architecture-next-work-v0-1
  status: working_definition
  phase: design_architecture_before_runtime_translation
  implementation_scope:
    included:
      - task definitions
      - information flow
      - input/output contracts
      - schema requirements
      - validation logic
      - example-driven test path
    excluded:
      - real filesystem paths
      - final Hermes runtime files
      - final SKILL.md files
      - cron implementation
      - Kanban runtime implementation
      - profile/toolset implementation
```

# 1. Current understanding

```yaml
canonical_model:
  current_goal: >
    Convert the existing PreCapNextDay / FlowRecap / AllProjectStatusPacketUpdate
    design package into a precise information-process architecture before
    runtime translation.

  core_loop:
    - PreCapWeek
    - PreCapNextDay
    - OperatorExecutesPlannedFlow
    - FlowRecapSkill
    - AllProjectStatusPacketUpdate
    - PreCapNextDay_next_cycle

  removed_from_core:
    - DayExecution_as_standalone_process
    - FlowExecution_as_standalone_process
    - DayExecutionController_as_standalone_process
    - RecapDay_as_required_core_layer

  optional_later:
    RecapDay:
      role: Alfred_or_personal_daily_review_layer
      status: on_hold

  locked_daily_flow_order:
    F1:
      project: Leela
      purpose: product_feature_specification
    F2:
      project: MasterOfArts
      purpose: website_structure_content_design_handoff
    F3:
      project: ApexAI_or_Hermes_orchestration
      purpose: orchestration_process_specification
    F4:
      project: Residual
      purpose: recovery_or_deepening
      sprint_mapping:
        S1: Leela_residual
        S2: MasterOfArts_residual
        S3: ApexAI_or_Hermes_residual

  universal_flow_anatomy:
    S1: first_work_sprint
    S2: second_work_sprint
    S3: recap_planning_digest_sprint
```

# 2. Macro process — what to do next

```yaml
macro_process:
  M0_preserve_scope:
    goal: prevent premature implementation
    rule: >
      Do not create runtime files until information contracts are complete.
    output:
      - scope_lock_statement

  M1_lock_artifact_taxonomy:
    goal: define all artifact types that move through the system
    input:
      - handover
      - example_PreCapNextDay_flow_package
      - FlowRecapSkill_spec
      - PromptAndAIRoutingPlanning_spec
      - PreCapNextDay_v0_2_spec
      - APSU_spec
      - ModelSubscriptionUsageTracking_spec
      - review_notes
    output:
      - artifact_taxonomy_v0_1

  M2_define_contract_template:
    goal: create one universal format for every input/output
    output:
      - universal_io_contract_template

  M3_patch_core_artifact_contracts:
    goal: define every handoff between processes
    output:
      - PreCapWeek_to_PreCapNextDay_contract
      - PreCapNextDay_to_Operator_contract
      - PreCapNextDay_to_FlowRecapSkill_contract
      - Operator_to_FlowRecapSkill_contract
      - FlowRecapSkill_to_APSU_contract
      - FlowRecapSkill_to_ModelUsageTracking_contract
      - APSU_to_PreCapNextDay_contract
      - ModelUsageTracking_to_PreCapNextDay_contract

  M4_test_against_example_package:
    goal: verify contracts against concrete flows before abstracting further
    required_examples:
      - F1_Leela_spatial_system
      - F2_MasterOfArts_website
      - F3_Apex_Hermes_orchestration
      - F4_Residual_multi_project_flow
    output:
      - contract_fit_report
      - missing_field_register
      - ambiguity_register

  M5_patch_specs_minimally:
    goal: update existing specs only where contracts fail
    rule: >
      Patch schema blocks and handoff contracts. Do not rewrite whole specs
      unless the current structure is wrong.
    output:
      - patch_plan_v0_1

  M6_run_minimal_end_to_end_simulation:
    goal: simulate one full execution day
    output:
      - one_PreCapNextDay_plan
      - four_flow_packets
      - four_raw_flow_dumps_or_skipped_markers
      - four_FlowRecap_outputs
      - one_APSU_output
      - one_next_PreCapNextDay_input_context

  M7_prepare_runtime_translation_package:
    prerequisite:
      - no_blocking_io_gaps
      - no_schema_enum_conflicts
      - all_artifacts_have_logical_locations
      - all_consumers_have readable inputs
      - all_missing_input behaviors defined
    output:
      - final_design_spec_sequence
      - future_runtime_translation_sequence
```

# 3. Meso architecture — process responsibilities and handoffs

## 3.1 PreCapWeek

```yaml
process:
  id: PreCapWeek
  role: weekly_planning_source
  responsibility: >
    Provides weekly priorities, day-by-day direction, and first execution-day
    planning context.

  outputs:
    weekly_plan_packet:
      consumer: PreCapNextDay
      required_fields:
        - week_id
        - weekly_priorities
        - project_allocations
        - day_by_day_direction
        - fixed_calendar_constraints
        - first_PreCapNextDay_trigger_context
      validation_rule: >
        Must contain at least one planned execution day and project allocation
        for Leela, MasterOfArts, ApexAI_or_Hermes_orchestration, or explicit
        reason for omission.
```

## 3.2 PreCapNextDay

```yaml
process:
  id: PreCapNextDay
  role: daily_flow_planner
  responsibility: >
    Converts weekly priorities, status state, previous FlowRecaps, skipped
    markers, calendar constraints, and routing guidance into one executable
    next-day plan.

  required_inputs:
    weekly_plan_packet:
      source: PreCapWeek
    all_project_status_packet:
      source: AllProjectStatusPacketUpdate
    latest_FlowRecaps:
      source: FlowRecapSkill
      required: optional_for_first_day_required_after_first_cycle
    skipped_flow_markers:
      source: FlowRecapSkill_or_APSU
      required: optional
    calendar_constraints:
      source: operator_or_calendar_context
      required: recommended
    model_usage_summary:
      source: ModelSubscriptionUsageTracking
      required: recommended
    AI_surface_inventory:
      source: operator_defined_registry
      required: recommended_before_prompt_routing

  required_outputs:
    next_day_plan:
      format: markdown_with_yaml_blocks
      contains:
        - execution_day_id
        - day_intent
        - calendar_feasibility_notes
        - fixed_flow_sequence
        - model_usage_constraints
        - operator_review_status

    flow_packets:
      count: 4
      item_contract:
        - flow_id
        - project_id
        - fixed_position
        - flow_goal
        - why_this_flow_now
        - expected_outputs
        - three_sprints
        - prompt_packets
        - embedded_context_instructions
        - output_capture_instruction
        - FlowRecapSkill_instruction
        - usage_tracking_expectation

    prompt_packets:
      format: embedded_yaml_blocks_inside_flow_packets
      item_contract:
        - prompt_packet_id
        - project_id
        - flow_id
        - sprint_id
        - prompt_goal
        - suggested_AI_surface
        - suggested_model_or_mode
        - reasoning_depth
        - context_to_include
        - files_to_upload_or_reference
        - expected_prompt_output
        - fallback_route
        - usage_tracking_required
        - cost_class
        - monthly_cap_relevant
        - output_capture_instruction

    FlowRecapSkill_instruction_blocks:
      count: one_per_flow
      required_fields:
        - original_flow_packet_reference
        - required_raw_dump_items
        - required_operator_validation_question
        - completion_state_options
```

## 3.3 OperatorExecutesPlannedFlow

```yaml
process:
  id: OperatorExecutesPlannedFlow
  type: human_action_not_Hermes_process
  responsibility: >
    Operator performs the planned flow using the provided prompt packets,
    context instructions, AI routes, and expected outputs.

  inputs:
    - selected_flow_packet
    - prompt_packets
    - context_instructions
    - expected_outputs
    - output_capture_instruction

  outputs:
    raw_flow_dump:
      consumer: FlowRecapSkill
      format: messy_or_structured_operator_material
      accepted_forms:
        - pasted_chat_history
        - uploaded_markdown
        - links_to_AI_chats
        - artifact_references
        - created_or_edited_files
        - prompt_outputs
        - model_usage_notes
        - operator_notes
        - decisions
        - blockers
        - unfinished_items
        - suspected_next_step
      minimal_required_fields:
        - flow_id_or_original_flow_packet
        - what_was_done
        - outputs_created_or_missing
        - unresolved_items
        - model_or_AI_surface_usage_if_known
        - operator_guess_for_next_step_if_known
```

## 3.4 FlowRecapSkill

```yaml
process:
  id: FlowRecapSkill
  future_runtime_target: Hermes_skill
  role: atomic_execution_memory_unit
  responsibility: >
    Converts one planned flow plus raw dump into validated structured memory,
    status delta, model usage delta, artifact index, and future planning context.

  inputs:
    original_planned_flow_packet:
      source: PreCapNextDay
      required: true
    raw_flow_dump:
      source: OperatorExecutesPlannedFlow
      required: true
    prompt_execution_log:
      source: Operator_or_raw_dump
      required: recommended
    artifact_references:
      source: Operator_or_raw_dump
      required: recommended
    existing_project_status_packet:
      source: APSU
      required: optional
    previous_flow_recap_for_same_project:
      source: FlowRecapSkill
      required: optional
    usage_tracking_file:
      source: ModelSubscriptionUsageTracking
      required: optional

  outputs:
    flow_recap_packet:
      format: markdown_with_structured_yaml_blocks
      required_sections:
        - document_metadata
        - source_flow_packet_reference
        - raw_dump_sources
        - completion_state
        - planned_vs_actual
        - sprint_level_summary
        - completed_outputs
        - artifact_index
        - prompt_result_summary
        - model_usage_delta
        - project_status_delta
        - blockers
        - unresolved_questions
        - reusable_learning
        - next_step_proposal
        - operator_validated_next_step
        - context_for_future_PreCapNextDay
        - validation_needed

  special_rules:
    ordinary_flows:
      applies_to:
        - F1_Leela
        - F2_MasterOfArts
        - F3_ApexHermes
      status_delta_rule: one_primary_project_status_delta

    residual_flow:
      applies_to:
        - F4_Residual
      status_delta_rule: split_project_status_delta_by_sprint_project
      required_project_deltas:
        - Leela_from_F4_S1
        - MasterOfArts_from_F4_S2
        - ApexAI_or_Hermes_from_F4_S3

  validation_rule: >
    No FlowRecap is complete until the next_step_proposal has been accepted,
    modified, rejected, or marked uncertain by the operator.
```

## 3.5 AllProjectStatusPacketUpdate

```yaml
process:
  id: AllProjectStatusPacketUpdate
  role: daily_or_manual_cross_project_state_merge
  responsibility: >
    Consumes FlowRecaps and skipped markers since the last update, merges
    project-level status deltas, resolves or flags conflicts, and publishes the
    status state consumed by the next PreCapNextDay.

  cadence:
    normal: once_daily
    manual: allowed
    explicitly_not_after_every_flow: true

  inputs:
    FlowRecaps_since_last_update:
      source: FlowRecapSkill
      required: true
    previous_all_project_status_packet:
      source: prior_APSU_output
      required: true_after_first_run
    skipped_flow_markers:
      source: FlowRecapSkill_or_operator
      required: optional
    model_usage_summary:
      source: ModelSubscriptionUsageTracking
      required: recommended
    operator_merge_notes:
      source: operator
      required: optional
    consumed_flow_recap_registry:
      source: APSU
      required: required_after_first_run

  outputs:
    updated_all_project_status_packet:
      format: markdown_with_yaml_blocks
      required_sections:
        - document_metadata
        - source_inputs
        - consumed_flow_recap_registry
        - skipped_flow_marker_registry
        - project_status_entries
        - next_executable_chunks
        - blockers
        - priority_or_urgency_changes
        - unresolved_conflicts
        - model_usage_summary_pointer
        - next_PreCapNextDay_context

    next_PreCapNextDay_input_context:
      format: yaml_block_or_markdown_section
      required_fields:
        - execution_day_target
        - project_next_chunks
        - project_blockers
        - skipped_flow_markers_to_consider
        - prompt_routes_to_reuse_or_avoid
        - high_impact_changes_requiring_operator_review
```

## 3.6 ModelSubscriptionUsageTracking

```yaml
process:
  id: ModelSubscriptionUsageTracking
  role: model_and_subscription_usage_state
  responsibility: >
    Tracks planned versus actual use of AI surfaces, modes, scarce capabilities,
    route quality, route failures, and recommendations for future prompt routing.

  inputs:
    planned_prompt_packet:
      source: PreCapNextDay_or_PromptAndAIRoutingPlanning
      required: true
    actual_usage_delta:
      source: FlowRecapSkill
      required: true
    available_AI_surface_inventory:
      source: operator_defined_registry
      required: practically_required_for_first_test
    previous_usage_summary:
      source: prior_ModelSubscriptionUsageTracking_output
      required: recommended

  outputs:
    usage_entries:
      consumer:
        - APSU
        - PreCapNextDay
    daily_usage_summary:
      consumer:
        - PreCapNextDay
        - APSU
    routing_recommendation_packet:
      consumer:
        - PromptAndAIRoutingPlanning
        - PreCapNextDay

  immediate_schema_patches_required:
    - replace_or_define_confidence_medium_high
    - rewrite_reserve_for_as_object_schema
    - define_source_update_id
    - choose_owner_of_daily_summary_file
    - define_planned_prompt_packet_contract
    - define_actual_usage_delta_contract
    - define_available_AI_surface_inventory_contract
```

# 4. Universal input/output contract template

```yaml
universal_io_contract:
  artifact_id: string
  artifact_name: string
  artifact_role: input | output | intermediate | registry | summary
  producer: process_id_or_operator
  consumer:
    - process_id
  lifecycle:
    created_when: string
    consumed_when: string
    updated_by: string | null
    archived_or_marked_consumed_when: string | null

  location:
    logical_location: string
    real_path_status: unresolved_until_runtime_phase
    location_slot: REQUIRED
    note: >
      Use logical location slots now. Do not invent actual paths yet.

  format:
    container: markdown_with_yaml_blocks | yaml_block | json | freeform_text | mixed_raw_dump
    schema_ref: string
    required_sections:
      - string

  source:
    upstream_process: string
    source_artifact_id: string | null
    source_event_id: string | null

  validation_rule:
    required_fields_present: true
    enum_values_valid: true
    consumer_can_parse: true
    missing_input_behavior: block_or_request_or_mark_validation_needed
    no_silent_fabrication: true

  minimal_example:
    required: true
    example_scope: smallest_valid_instance_not_full_document
```

# 5. Core artifact taxonomy

```yaml
artifact_taxonomy:
  A1_weekly_plan_packet:
    producer: PreCapWeek
    consumer: PreCapNextDay

  A2_next_day_plan:
    producer: PreCapNextDay
    consumer:
      - Operator
      - FlowRecapSkill
      - APSU_indirectly

  A3_flow_packet:
    producer: PreCapNextDay
    consumer:
      - Operator
      - FlowRecapSkill

  A4_prompt_packet:
    producer:
      - PromptAndAIRoutingPlanning
      - PreCapNextDay
    consumer:
      - Operator
      - FlowRecapSkill
      - ModelSubscriptionUsageTracking

  A5_context_instruction_packet:
    producer: PreCapNextDay
    consumer: Operator
    note: embedded_inside_flow_packet_for_now

  A6_raw_flow_dump:
    producer: Operator
    consumer: FlowRecapSkill

  A7_flow_recap_packet:
    producer: FlowRecapSkill
    consumer:
      - APSU
      - PreCapNextDay
      - ModelSubscriptionUsageTracking

  A8_project_status_delta:
    producer: FlowRecapSkill
    consumer: APSU

  A9_model_usage_delta:
    producer: FlowRecapSkill
    consumer: ModelSubscriptionUsageTracking

  A10_all_project_status_packet:
    producer: APSU
    consumer:
      - PreCapNextDay
      - PreCapWeek

  A11_next_PreCapNextDay_input_context:
    producer: APSU
    consumer: PreCapNextDay

  A12_skipped_flow_marker:
    producer:
      - FlowRecapSkill
      - Operator
    consumer:
      - APSU
      - PreCapNextDay

  A13_usage_summary:
    producer: ModelSubscriptionUsageTracking
    consumer:
      - PreCapNextDay
      - APSU
```

# 6. Micro-level next actions

```yaml
micro_next_actions:
  step_1_create_artifact_contract_registry:
    objective: >
      Create one canonical list of all artifacts and assign each one a producer,
      consumer, schema, lifecycle, and logical location slot.
    output:
      - artifact-contract-registry-v0-1
    acceptance_check:
      - every artifact has exactly one primary producer
      - every artifact has at least one consumer
      - no artifact is only described as "section" without a contract

  step_2_define_logical_location_slots:
    objective: >
      Define logical storage slots without choosing actual paths.
    output:
      - logical-location-slots-v0-1
    slots:
      - WEEKLY_PLAN_SLOT
      - NEXT_DAY_PLAN_SLOT
      - FLOW_PACKET_SLOT
      - FLOW_RECAP_SLOT
      - STATUS_PACKET_SLOT
      - SKIPPED_MARKER_SLOT
      - MODEL_USAGE_SLOT
      - REGISTRY_SLOT
    acceptance_check:
      - no real paths invented
      - each slot has producer and consumer

  step_3_normalize_ids:
    objective: >
      Define stable identifiers that tie artifacts together.
    output:
      - id-schema-v0-1
    required_ids:
      - week_id
      - execution_day_id
      - flow_id
      - sprint_id
      - prompt_packet_id
      - flow_recap_id
      - project_status_delta_id
      - usage_entry_id
      - APSU_update_id
      - source_event_id
    acceptance_check:
      - every downstream input can reference upstream output by ID

  step_4_patch_prompt_packet_schema:
    objective: >
      Make prompt packets traceable across PreCapNextDay, FlowRecapSkill, and
      ModelSubscriptionUsageTracking.
    output:
      - prompt-packet-contract-v0-1
    acceptance_check:
      - every prompt_packet_id includes project, flow, sprint, and sequence
      - every prompt packet has expected_output and output_capture_instruction
      - every prompt packet has usage_tracking_required

  step_5_patch_FlowRecapSkill_contract:
    objective: >
      Ensure FlowRecapSkill outputs every field needed by APSU and
      ModelSubscriptionUsageTracking.
    output:
      - FlowRecapSkill_contract_patch_v0_2
    acceptance_check:
      - model_usage_delta exists
      - project_status_delta exists
      - operator_validated_next_step exists
      - context_for_future_PreCapNextDay exists
      - residual flow split rule exists

  step_6_patch_APSU_contract:
    objective: >
      Ensure APSU can consume multiple FlowRecaps and produce the next planning
      state.
    output:
      - APSU_contract_patch_v0_2
    acceptance_check:
      - consumed_flow_recap_registry defined
      - skipped_flow_marker_registry defined
      - previous_all_project_status_packet defined
      - next_PreCapNextDay_input_context defined
      - high_impact_change_threshold defined

  step_7_patch_ModelSubscriptionUsageTracking_contract:
    objective: >
      Fix schema contradictions and define model usage inputs/outputs.
    output:
      - ModelSubscriptionUsageTracking_contract_patch_v0_2
    acceptance_check:
      - confidence enum valid
      - reserve_for schema valid
      - source_update_id defined
      - daily_summary owner chosen
      - planned_prompt_packet and actual_usage_delta have examples

  step_8_run_example_package_against_contracts:
    objective: >
      Validate F1/F2/F3/F4 examples against the new contracts.
    output:
      - example-fit-report-v0-1
    tests:
      - Can PreCapNextDay generate all four flow packets?
      - Can each flow packet generate a valid raw dump requirement?
      - Can FlowRecapSkill digest each flow?
      - Can residual F4 split status deltas by project?
      - Can APSU merge all recaps without guessing?
      - Can next PreCapNextDay read the result?

  step_9_create_minimal_end_to_end_simulation:
    objective: >
      Produce one fake but structurally valid day to prove information flow.
    output:
      - minimal-simulation-day-v0-1
    required_artifacts:
      - one_next_day_plan
      - four_flow_packets
      - three_normal_flow_recaps
      - one_residual_flow_recap_or_marker
      - one_model_usage_summary
      - one_updated_all_project_status_packet
      - one_next_PreCapNextDay_input_context

  step_10_only_then_prepare_final_file_sequence:
    objective: >
      After contracts pass simulation, decide final design files and runtime
      translation files.
    output:
      - final-file-creation-sequence-v0-1
```

# 7. Minimal end-to-end information flow

```yaml
minimal_information_flow:
  1_PreCapWeek_to_PreCapNextDay:
    input_to_PreCapNextDay:
      - weekly_priorities
      - project_allocations
      - first_execution_day_context

  2_PreCapNextDay_to_Operator:
    output_to_operator:
      - next_day_plan
      - F1_flow_packet
      - F2_flow_packet
      - F3_flow_packet
      - F4_flow_packet
      - prompt_packets
      - context_instructions
      - output_capture_instructions

  3_Operator_to_FlowRecapSkill:
    output_from_operator:
      - raw_flow_dump_per_flow
      - prompt_outputs
      - artifacts
      - decisions
      - blockers
      - model_usage_notes

  4_FlowRecapSkill_to_APSU:
    output_to_APSU:
      - flow_recap_packet
      - project_status_delta
      - artifact_index
      - blocker_list
      - operator_validated_next_step
      - skipped_flow_marker_if_applicable

  5_FlowRecapSkill_to_ModelUsageTracking:
    output_to_model_usage:
      - prompt_result_summary
      - model_usage_delta
      - route_reuse_or_avoid_signal

  6_ModelUsageTracking_to_PreCapNextDay:
    output_to_next_planning:
      - daily_usage_summary
      - routing_recommendation_packet
      - scarce_mode_warning

  7_APSU_to_PreCapNextDay:
    output_to_next_cycle:
      - updated_all_project_status_packet
      - next_executable_chunks
      - unresolved_conflicts
      - skipped_flow_markers
      - next_PreCapNextDay_input_context
```

# 8. Required minimal examples per artifact

```yaml
minimal_examples_required:
  flow_packet_example:
    use: F1_LEELA_SPATIAL_SYSTEM
    must_show:
      - one flow_goal
      - three sprints
      - one prompt_packet
      - one FlowRecapSkill_instruction

  raw_flow_dump_example:
    use: messy_operator_dump
    must_show:
      - copied AI output summary
      - artifact reference
      - decision
      - blocker
      - model usage note
      - suspected next step

  FlowRecap_example:
    use: F1_LEELA_SPATIAL_SYSTEM
    must_show:
      - planned_vs_actual
      - artifact_index
      - prompt_result_summary
      - project_status_delta
      - model_usage_delta
      - operator_validated_next_step

  residual_FlowRecap_example:
    use: F4_RESIDUAL_PRIORITY_CONTINUATION
    must_show:
      - split_project_status_delta_for_Leela
      - split_project_status_delta_for_MasterOfArts
      - split_project_status_delta_for_ApexHermes
      - skipped_marker_if_any_sprint_missing

  APSU_example:
    use: one_day_merge
    must_show:
      - consumed_flow_recap_registry
      - skipped_flow_marker_registry
      - updated_project_status_entries
      - next_executable_chunks
      - unresolved_conflicts
      - next_PreCapNextDay_input_context

  model_usage_example:
    use: one_prompt_packet
    must_show:
      - planned_route
      - actual_route
      - output_quality
      - should_repeat_route
      - recommendation_for_next_PreCapNextDay
```

# 9. Blocking variables to resolve before runtime translation

```yaml
blocking_variables:
  storage:
    - logical_location_slots_now
    - real_absolute_paths_later

  artifact_contracts:
    - every_input_output_has_location_source_format_validation_example
    - no_consumer_depends_on_vague_prose_section

  IDs:
    - execution_day_id
    - flow_id
    - sprint_id
    - prompt_packet_id
    - flow_recap_id
    - APSU_update_id
    - usage_entry_id

  triggers:
    - primary_PreCapNextDay_trigger
    - APSU_to_PreCapNextDay_trigger
    - manual_trigger_method
    - scheduled_fallback_method

  operator_gates:
    - PreCapNextDay_review_scope
    - FlowRecap_next_step_validation
    - APSU_high_impact_change_threshold

  schemas:
    - prompt_packet_schema
    - raw_flow_dump_schema
    - FlowRecap_output_schema
    - project_status_delta_schema
    - model_usage_delta_schema
    - APSU_output_schema
    - next_PreCapNextDay_input_context_schema

  model_usage:
    - AI_surface_inventory_source
    - planned_prompt_packet_contract
    - actual_usage_delta_contract
    - daily_summary_owner
    - confidence_enum
    - reserve_for_schema
    - source_update_id
```

# 10. Recommended work order from here

```yaml
recommended_work_order:
  W1:
    name: artifact_taxonomy_and_contract_registry
    reason: >
      This is the missing basis. Without it, all later specs remain ambiguous.

  W2:
    name: id_schema_and_logical_location_slots
    reason: >
      Downstream artifacts need stable references before storage or runtime
      implementation is discussed.

  W3:
    name: example_package_contract_test
    reason: >
      The Example PreCapNextDay flow package is the stress test for all schemas.

  W4:
    name: patch_FlowRecapSkill
    reason: >
      It is the atomic execution-memory unit and produces the key downstream
      deltas.

  W5:
    name: patch_PromptAndAIRoutingPlanning
    reason: >
      Prompt packet fields must be normalized before PreCapNextDay is patched.

  W6:
    name: patch_PreCapNextDay
    reason: >
      PreCapNextDay must output complete executable flow packets with routing,
      context, recap, and usage instructions.

  W7:
    name: patch_APSU
    reason: >
      APSU must merge FlowRecaps without guessing and produce next-cycle
      planning context.

  W8:
    name: patch_ModelSubscriptionUsageTracking
    reason: >
      It must consume planned/actual prompt usage and feed routing logic back
      into PreCapNextDay.

  W9:
    name: minimal_day_simulation
    reason: >
      Proves the architecture before final Hermes translation.

  W10:
    name: runtime_translation_preparation
    reason: >
      Only after the information architecture is closed should Hermes skills,
      profiles, cron jobs, and Kanban graphs be defined.
```