# FILE: .claude/skills/precap-next-day/references/flow-packet-contract.md

# Flow Packet Contract

```yaml
flow_packet_contract:
  artifact_name: flow_packet
  file_role: precap_next_day_reference_contract
  purpose: >
    Define the minimum valid structure for one PreCapNextDay per-flow packet.
    A flow_packet turns one day-level flow slot into an operator-executable
    work container with sprint intent, workflow/process labels, prompt-pack
    reference, usage-planning reference, raw execution capture preparation,
    skipped-flow handling, and FlowRecap handoff context. This file is a
    reference contract, not a prompt-pack schema, not a daily-plan schema, and
    not a FlowRecap output schema.

  ownership:
    owns:
      - flow_packet
      - flow_packet_metadata
      - flow_identity
      - flow_context_summary
      - flow_sprint_plan
      - flow_sprint_block
      - flow_execution_capture_preparation
      - raw_flow_dump_template
      - skipped_flow_marker_template
      - FlowRecap_handoff_block
      - flow_packet_validation_rules
      - flow_packet_examples
    must_not_own:
      - next_day_plan
      - daily_plan_metadata
      - flow_prompt_pack
      - prompt_packet
      - final_copy_paste_prompt
      - routing_decision
      - planned_usage_budget
      - usage_delta
      - workflow_stage_taxonomy
      - process_stage_taxonomy
      - expected_output_type_schema
      - calendar_event_write_request
      - FlowRecap_output
      - project_status_merge
      - project_execution

  dependency_contracts:
    daily_plan_output_contract: references/daily-plan-output-contract.md
    flow_prompt_pack_contract: references/flow-prompt-pack-contract.md
    prompt_engineering_dependency_contract: references/prompt-engineering-dependency-contract.md
    usage_tracking_dependency_contract: references/usage-tracking-dependency-contract.md
    workflow_process_validation_contract: references/workflow-process-validation-contract.md
    calendar_event_write_contract: references/calendar-event-write-contract.md

  global_rules:
    one_flow_packet_per_active_or_skipped_flow: true
    default_daily_flow_slots_are_F1_to_F4: true
    flow_packets_may_be_full_compressed_omitted_or_skipped: true
    omitted_flow_requires_reason_in_daily_plan: true
    skipped_flow_requires_skipped_flow_marker_template_or_marker: true
    compressed_flow_requires_compression_reason: true
    prompt_pack_is_referenced_not_embedded_as_schema: true
    FlowRecap_handoff_prepared_but_FlowRecap_not_run: true
    raw_flow_dump_template_prepared_but_not_filled_by_PreCapNextDay: true
    project_work_not_executed: true
    calendar_write_not_executed_here: true
```

## Schema: flow_packet

```yaml
flow_packet:
  type: object
  required:
    - packet_id
    - artifact_name
    - created_or_updated_at
    - execution_day
    - generation_mode
    - review_status
    - flow_packet_metadata
    - flow_identity
    - flow_context_summary
    - workflow_process_labels
    - flow_sprint_plan
    - prompt_pack_ref
    - usage_tracking_refs
    - flow_execution_capture_preparation
    - FlowRecap_handoff_block
    - operator_review_flags
    - validation_status

  fields:
    packet_id:
      type: string
      format: "flow_packet_<execution_day_id>_<flow_id>"
      required: true

    artifact_name:
      type: string
      allowed:
        - flow_packet
      required: true

    created_or_updated_at:
      type: string
      format: "YYYY-MM-DD"
      required: true

    execution_day:
      type: string
      format: "YYYY-MM-DD"
      required: true

    generation_mode:
      type: string
      allowed:
        - full_context_mode
        - standard_mode
        - recap_recovery_mode
        - bootstrap_mode
        - calendar_constrained_mode
        - prompt_heavy_mode
        - low_confidence_degraded_mode
      required: true

    review_status:
      type: string
      allowed:
        - operator_approved
        - operator_review_recommended
        - auto_generated
        - low_confidence_auto_generated
        - blocked_by_external_tool_unavailable
      required: true

    flow_packet_metadata:
      type: object_ref
      ref: flow_packet_metadata
      required: true

    flow_identity:
      type: object_ref
      ref: flow_identity
      required: true

    flow_context_summary:
      type: object_ref
      ref: flow_context_summary
      required: true

    workflow_process_labels:
      type: object_ref
      ref: workflow_process_labels_ref
      required: true

    flow_sprint_plan:
      type: object_ref
      ref: flow_sprint_plan
      required: true

    prompt_pack_ref:
      type: object_ref
      ref: prompt_pack_ref
      required: true

    usage_tracking_refs:
      type: object_ref
      ref: usage_tracking_refs
      required: true

    workflow_block_ref:
      type: object_ref
      ref: workflow_block_ref
      required: false

    flow_execution_capture_preparation:
      type: object_ref
      ref: flow_execution_capture_preparation
      required: true

    FlowRecap_handoff_block:
      type: object_ref
      ref: FlowRecap_handoff_block
      required: true

    operator_review_flags:
      type: list
      item_type: string
      min_items: 0
      max_items: 16
      required: true

    validation_status:
      type: string
      allowed:
        - valid
        - valid_with_warnings
        - operator_review_recommended
        - low_confidence_auto_generated
        - blocked_by_missing_operator_decision
      required: true
```

## Schema: flow_packet_metadata

```yaml
flow_packet_metadata:
  type: object
  required:
    - package
    - source_skill
    - contract_version
    - produced_during
    - primary_consumer
    - downstream_consumers

  fields:
    package:
      type: string
      allowed:
        - precap-next-day
      required: true

    source_skill:
      type: string
      allowed:
        - precap-next-day
      required: true

    contract_version:
      type: string
      format: "0.x"
      required: true

    produced_during:
      type: string
      allowed:
        - PreCapNextDay
      required: true

    primary_consumer:
      type: string
      allowed:
        - operator
      required: true

    downstream_consumers:
      type: list
      item_type: string
      allowed:
        - FlowRecap
        - prompt-engineering
        - ai-routing-and-usage-tracking
        - workflow-process-design
        - calendar_event_write_contract
        - status-merge_later
      required: true

    source_refs:
      type: list
      item_type: string
      required: false

    notes:
      type: string
      required: false
```

## Schema: flow_identity

```yaml
flow_identity:
  type: object
  required:
    - flow_id
    - flow_slot
    - project
    - flow_role
    - flow_status
    - default_flow

  fields:
    flow_id:
      type: string
      allowed:
        - F1
        - F2
        - F3
        - F4
        - operator_defined
      required: true

    flow_slot:
      type: string
      format: "F<number>"
      required: true

    project:
      type: string
      allowed:
        - Leela
        - MasterOfArts
        - Apex
        - Residual
        - Investment
        - Others
        - operator_defined
      required: true

    flow_role:
      type: string
      allowed:
        - app_product_or_system_work
        - coaching_business_website_offer_content_work
        - orchestration_system_buildout
        - overflow_recovery_lagging_threads_cross_project_cleanup
        - investment_review_or_reactivation
        - operator_defined
      required: true

    flow_status:
      type: string
      allowed:
        - planned
        - compressed
        - omitted
        - skipped
        - blocked
        - placeholder
      required: true

    default_flow:
      type: boolean
      required: true

    override_reason:
      type: string
      required: false

    omission_reason:
      type: string
      required: false

    compression_reason:
      type: string
      required: false

    blocker_summary:
      type: string
      required: false
```

## Fixed Flow Defaults

```yaml
fixed_flow_defaults:
  F1:
    project: Leela
    flow_role: app_product_or_system_work
    default_use: product_feature_system_definition_or_app_build_work
    default_sprints:
      S1: first_work_sprint
      S2: second_work_or_deepening_sprint
      S3: recap_digest_preparation_sprint

  F2:
    project: MasterOfArts
    flow_role: coaching_business_website_offer_content_work
    default_use: coaching_business_website_offer_content_or_facilitation_design_work
    default_sprints:
      S1: first_work_sprint
      S2: second_work_or_deepening_sprint
      S3: recap_digest_preparation_sprint

  F3:
    project: Apex
    flow_role: orchestration_system_buildout
    default_use: orchestration_process_skill_package_or_artifact_contract_work
    default_sprints:
      S1: first_work_sprint
      S2: second_work_or_deepening_sprint
      S3: recap_digest_preparation_sprint

  F4:
    project: Residual
    flow_role: overflow_recovery_lagging_threads_cross_project_cleanup
    default_use: recovery_overflow_lagging_thread_cross_project_or_low_energy_work
    default_sprints:
      S1: first_work_sprint
      S2: second_work_or_deepening_sprint
      S3: recap_digest_preparation_sprint

  investment_policy:
    fixed_daily_flow: false
    allowed_entry:
      - Residual
      - operator_override
      - explicitly_planned_in_next_day_plan
```

## Schema: flow_context_summary

```yaml
flow_context_summary:
  type: object
  required:
    - operator_intent_summary
    - project_state_summary
    - source_context_refs
    - constraints
    - assumptions
    - unresolved_inputs

  fields:
    operator_intent_summary:
      type: string
      required: true

    project_state_summary:
      type: string
      required: true

    recap_carry_forward:
      type: list
      item_type: string
      required: false

    weekly_plan_alignment:
      type: string
      allowed:
        - aligned
        - partially_aligned
        - not_available
        - conflict_detected
        - operator_override
      required: false

    calendar_constraints_summary:
      type: string
      required: false

    source_context_refs:
      type: list
      item_type: string
      min_items: 0
      required: true

    constraints:
      type: list
      item_type: string
      min_items: 0
      required: true

    assumptions:
      type: list
      item_type: string
      min_items: 0
      required: true

    unresolved_inputs:
      type: list
      item_type: string
      min_items: 0
      required: true

    confidence_notes:
      type: list
      item_type: string
      required: false
```

## Schema: workflow_process_labels_ref

```yaml
workflow_process_labels_ref:
  type: object
  required:
    - workflow_stage
    - process_stage
    - expected_output_type
    - validation_source
    - fit_status

  fields:
    workflow_stage:
      type: string
      required: true
      source_authority: workflow-process-design/references/workflow-stage-taxonomy.md

    process_stage:
      type: string
      required: true
      source_authority: workflow-process-design/references/process-stage-taxonomy.md

    expected_output_type:
      type: string
      required: true
      source_authority: workflow-process-design/references/expected-output-type-contract.md

    validation_source:
      type: string
      allowed:
        - workflow-process-design
        - inferred_from_context
        - operator_supplied
        - not_available
      required: true

    fit_status:
      type: string
      allowed:
        - valid
        - valid_with_warnings
        - operator_review_recommended
        - low_confidence_auto_generated
        - blocked_by_missing_operator_decision
      required: true

    mismatch_flags:
      type: list
      item_type: string
      required: false

    operator_review_note:
      type: string
      required: false
```

## Schema: flow_sprint_plan

```yaml
flow_sprint_plan:
  type: object
  required:
    - sprint_policy
    - sprint_count
    - sprints
    - recap_digest_required

  fields:
    sprint_policy:
      type: string
      allowed:
        - default_three_sprints
        - compressed_single_sprint
        - compressed_two_sprints
        - omitted
        - skipped
        - operator_defined
      required: true

    sprint_count:
      type: integer
      min: 0
      max: 3
      required: true

    sprints:
      type: list
      item_ref: flow_sprint_block
      min_items: 0
      max_items: 3
      required: true

    recap_digest_required:
      type: boolean
      required: true

    sprint_sequence_notes:
      type: list
      item_type: string
      required: false

    compression_handling:
      type: object_ref
      ref: compression_handling
      required: false
```

## Schema: flow_sprint_block

```yaml
flow_sprint_block:
  type: object
  required:
    - sprint_id
    - sprint_role
    - sprint_goal
    - expected_output_type
    - prompt_sequence_ref
    - capture_focus
    - completion_marker
    - validation_status

  fields:
    sprint_id:
      type: string
      allowed:
        - S1
        - S2
        - S3
        - SX
      required: true

    sprint_role:
      type: string
      allowed:
        - first_work_sprint
        - second_work_or_deepening_sprint
        - recap_digest_preparation_sprint
        - compressed_work_sprint
        - operator_defined
      required: true

    sprint_goal:
      type: string
      required: true

    expected_output_type:
      type: string
      required: true
      source_authority: workflow-process-design/references/expected-output-type-contract.md

    success_criteria:
      type: list
      item_type: string
      min_items: 1
      max_items: 8
      required: false

    prompt_sequence_ref:
      type: string
      format: "relative_or_logical_ref_to_flow_prompt_pack_sprint_sequence"
      required: true

    capture_focus:
      type: list
      item_type: string
      allowed:
        - artifact_created
        - decision_made
        - blocker_found
        - source_context_used
        - prompt_result
        - model_usage
        - next_step_guess
        - operator_energy_signal
        - unresolved_question
        - no_capture_needed
      required: true

    completion_marker:
      type: string
      allowed:
        - done
        - partial
        - skipped
        - blocked
        - not_started
        - operator_defined
      required: true

    validation_status:
      type: string
      allowed:
        - valid
        - valid_with_warnings
        - operator_review_recommended
        - low_confidence_auto_generated
        - blocked_by_missing_operator_decision
      required: true

    operator_review_flags:
      type: list
      item_type: string
      required: false
```

## Schema: compression_handling

```yaml
compression_handling:
  type: object
  required:
    - compression_status
    - reason
    - preserved_sprint_roles
    - dropped_or_merged_elements
    - operator_review_needed

  fields:
    compression_status:
      type: string
      allowed:
        - not_compressed
        - compressed_single_sprint
        - compressed_two_sprints
        - omitted
        - skipped
      required: true

    reason:
      type: string
      required: true

    preserved_sprint_roles:
      type: list
      item_type: string
      allowed:
        - first_work_sprint
        - second_work_or_deepening_sprint
        - recap_digest_preparation_sprint
      required: true

    dropped_or_merged_elements:
      type: list
      item_type: string
      required: true

    operator_review_needed:
      type: boolean
      required: true
```

## Schema: prompt_pack_ref

```yaml
prompt_pack_ref:
  type: object
  required:
    - flow_prompt_pack_path
    - prompt_pack_status
    - prompt_pack_authority

  fields:
    flow_prompt_pack_path:
      type: string
      format: "relative_or_logical_path_to_flow_prompt_pack"
      required: true

    prompt_pack_status:
      type: string
      allowed:
        - required
        - generated
        - generic_degraded_mode
        - unavailable
        - not_needed_for_skipped_flow
      required: true

    prompt_pack_authority:
      type: string
      allowed:
        - references/flow-prompt-pack-contract.md
      required: true

    prompt_engineering_dependency_status:
      type: string
      allowed:
        - available
        - missing_use_degraded_generic_prompt_mode
        - operator_supplied_prompt
        - not_needed_for_skipped_flow
      required: false

    note:
      type: string
      required: false
```

## Schema: usage_tracking_refs

```yaml
usage_tracking_refs:
  type: object
  required:
    - planned_usage_budget_ref
    - routing_recommendation_ref
    - usage_tracking_status
    - expected_usage_capture_fields

  fields:
    planned_usage_budget_ref:
      type: string
      format: "relative_or_logical_ref_to_planned_usage_budget"
      required: true

    routing_recommendation_ref:
      type: string
      format: "relative_or_logical_ref_to_routing_recommendation_packet"
      required: false

    usage_tracking_status:
      type: string
      allowed:
        - planned
        - degraded_missing_usage_context
        - not_needed_for_skipped_flow
        - operator_review_recommended
      required: true

    expected_usage_capture_fields:
      type: list
      item_type: string
      allowed:
        - provider_used
        - surface_class_used
        - model_or_mode_if_operator_records_it
        - prompt_count
        - deep_research_used
        - agent_run_used
        - high_reasoning_used
        - API_usage_if_known
        - subscription_quota_signal_if_known
        - cost_or_credit_signal_if_known
        - result_quality_signal
      required: true

    note:
      type: string
      required: false
```

## Schema: workflow_block_ref

```yaml
workflow_block_ref:
  type: object
  required:
    - workflow_block_status
    - calendar_event_write_request_ref

  fields:
    workflow_block_status:
      type: string
      allowed:
        - workflow_block_requested
        - workflow_block_not_requested
        - calendar_unavailable
        - operator_acceptance_required
      required: true

    calendar_event_write_request_ref:
      type: string
      format: "relative_or_logical_ref_to_calendar_event_write_request"
      required: true

    note:
      type: string
      required: false
```

## Schema: flow_execution_capture_preparation

```yaml
flow_execution_capture_preparation:
  type: object
  required:
    - raw_flow_dump_template
    - skipped_flow_marker_template
    - capture_instructions
    - capture_status

  fields:
    raw_flow_dump_template:
      type: object_ref
      ref: raw_flow_dump_template
      required: true

    skipped_flow_marker_template:
      type: object_ref
      ref: skipped_flow_marker_template
      required: true

    capture_instructions:
      type: list
      item_type: string
      min_items: 1
      max_items: 10
      required: true

    capture_status:
      type: string
      allowed:
        - prepared
        - not_needed_for_omitted_flow
        - not_needed_for_skipped_flow
        - operator_review_recommended
      required: true
```

## Schema: raw_flow_dump_template

```yaml
raw_flow_dump_template:
  type: object
  required:
    - template_id
    - flow_id
    - execution_day
    - completion_marker
    - operator_raw_notes
    - prompt_results
    - artifacts_created
    - decisions_made
    - blockers
    - model_usage_notes
    - next_step_guess
    - recap_request

  fields:
    template_id:
      type: string
      format: "raw_flow_dump_template_<execution_day_id>_<flow_id>"
      required: true

    flow_id:
      type: string
      allowed:
        - F1
        - F2
        - F3
        - F4
        - operator_defined
      required: true

    execution_day:
      type: string
      format: "YYYY-MM-DD"
      required: true

    completion_marker:
      type: string
      allowed:
        - done
        - partial
        - skipped
        - blocked
        - not_started
      required: true

    operator_raw_notes:
      type: string
      required: true
      fill_policy: operator_fills_after_work

    prompt_results:
      type: list
      item_type: string
      required: true
      fill_policy: operator_or_FlowRecap_fills_after_prompt_execution

    artifacts_created:
      type: list
      item_type: string
      required: true
      fill_policy: operator_fills_after_work

    decisions_made:
      type: list
      item_type: string
      required: true
      fill_policy: operator_fills_after_work

    blockers:
      type: list
      item_type: string
      required: true
      fill_policy: operator_fills_after_work

    model_usage_notes:
      type: list
      item_type: string
      required: true
      fill_policy: operator_fills_when_known

    next_step_guess:
      type: string
      required: true
      fill_policy: operator_or_FlowRecap_fills_after_work

    recap_request:
      type: string
      allowed:
        - run_FlowRecap
        - skip_FlowRecap
        - operator_review_first
      required: true
```

## Schema: skipped_flow_marker_template

```yaml
skipped_flow_marker_template:
  type: object
  required:
    - marker_id
    - flow_id
    - execution_day
    - skip_status
    - skip_reason
    - carry_forward_policy
    - next_review_point

  fields:
    marker_id:
      type: string
      format: "skipped_flow_marker_<execution_day_id>_<flow_id>"
      required: true

    flow_id:
      type: string
      allowed:
        - F1
        - F2
        - F3
        - F4
        - operator_defined
      required: true

    execution_day:
      type: string
      format: "YYYY-MM-DD"
      required: true

    skip_status:
      type: string
      allowed:
        - planned_skip
        - same_day_skip
        - blocked_skip
        - energy_or_time_skip
        - operator_override_skip
      required: true

    skip_reason:
      type: string
      required: true

    carry_forward_policy:
      type: string
      allowed:
        - carry_forward_to_next_PreCapNextDay
        - drop_with_reason
        - merge_into_Residual
        - operator_decides_later
      required: true

    next_review_point:
      type: string
      allowed:
        - next_PreCapNextDay
        - FlowRecap_if_partial_work_exists
        - weekly_review
        - operator_defined
      required: true

    operator_note:
      type: string
      required: false
```

## Schema: FlowRecap_handoff_block

```yaml
FlowRecap_handoff_block:
  type: object
  required:
    - handoff_id
    - flow_packet_ref
    - raw_flow_dump_expected
    - skipped_flow_marker_allowed
    - context_to_pass
    - required_operator_completion_marker
    - FlowRecap_ready_status
    - boundary_note

  fields:
    handoff_id:
      type: string
      format: "FlowRecap_handoff_<execution_day_id>_<flow_id>"
      required: true

    flow_packet_ref:
      type: string
      format: "relative_or_logical_ref_to_this_flow_packet"
      required: true

    raw_flow_dump_expected:
      type: boolean
      required: true

    skipped_flow_marker_allowed:
      type: boolean
      required: true

    context_to_pass:
      type: list
      item_type: string
      allowed:
        - flow_identity
        - flow_context_summary
        - workflow_process_labels
        - flow_sprint_plan
        - prompt_pack_ref
        - usage_tracking_refs
        - raw_flow_dump_template
        - skipped_flow_marker_template
        - operator_review_flags
      required: true

    required_operator_completion_marker:
      type: string
      allowed:
        - done
        - partial
        - skipped
        - blocked
        - not_started
      required: true

    FlowRecap_ready_status:
      type: string
      allowed:
        - ready_after_operator_execution
        - ready_after_operator_supplies_raw_dump
        - skipped_marker_only
        - blocked_missing_flow_packet
        - operator_review_recommended
      required: true

    boundary_note:
      type: string
      required: true
      rule: "PreCapNextDay prepares this handoff but does not run FlowRecap or create FlowRecap output."
```

## Flow Packet Validation Rules

```yaml
flow_packet_validation_rules:
  required_structure:
    one_packet_per_non_omitted_flow: true
    flow_identity_present: true
    sprint_plan_present_even_if_compressed_or_skipped: true
    prompt_pack_ref_present_unless_skipped_or_omitted: true
    raw_flow_dump_template_present_for_planned_partial_or_blocked_flows: true
    skipped_flow_marker_template_present_for_skipped_flows: true
    FlowRecap_handoff_block_present: true

  boundary_checks:
    does_not_embed_prompt_packet_schema: true
    does_not_embed_flow_prompt_pack_schema: true
    does_not_define_routing_decision: true
    does_not_define_planned_usage_budget: true
    does_not_define_usage_delta: true
    does_not_define_workflow_stage_taxonomy: true
    does_not_define_process_stage_taxonomy: true
    does_not_create_FlowRecap_output: true
    does_not_merge_project_status: true
    does_not_execute_project_work: true

  operator_review_triggers:
    - missing_project_state_summary
    - inferred_workflow_or_process_label
    - prompt_engineering_dependency_missing
    - routing_or_usage_context_missing_for_high_value_flow
    - compressed_flow_with_dropped_sprint_role
    - omitted_flow_without_reason
    - skipped_flow_without_carry_forward_policy
    - calendar_constraint_conflict
    - workflow_process_fit_warning
```

## Examples

```yaml
examples:
  standard_Apex_flow_packet:
    packet_id: flow_packet_2026-06-16_F3
    artifact_name: flow_packet
    created_or_updated_at: "2026-06-16"
    execution_day: "2026-06-17"
    generation_mode: standard_mode
    review_status: operator_review_recommended
    flow_identity:
      flow_id: F3
      flow_slot: F3
      project: Apex
      flow_role: orchestration_system_buildout
      flow_status: planned
      default_flow: true
    workflow_process_labels:
      workflow_stage: skill_package_file_generation
      process_stage: contract_definition
      expected_output_type: reference_contract
      validation_source: workflow-process-design
      fit_status: valid_with_warnings
    flow_sprint_plan:
      sprint_policy: default_three_sprints
      sprint_count: 3
      sprints:
        - sprint_id: S1
          sprint_role: first_work_sprint
          sprint_goal: Create the first complete version of the target reference contract.
          expected_output_type: reference_contract
          prompt_sequence_ref: flow_prompt_pack_2026-06-17_F3.S1
          capture_focus:
            - artifact_created
            - prompt_result
            - model_usage
          completion_marker: not_started
          validation_status: valid
        - sprint_id: S2
          sprint_role: second_work_or_deepening_sprint
          sprint_goal: Validate the contract against package boundaries and adjacent schemas.
          expected_output_type: validation_notes
          prompt_sequence_ref: flow_prompt_pack_2026-06-17_F3.S2
          capture_focus:
            - blocker_found
            - unresolved_question
            - decision_made
          completion_marker: not_started
          validation_status: valid
        - sprint_id: S3
          sprint_role: recap_digest_preparation_sprint
          sprint_goal: Prepare raw execution notes for FlowRecap.
          expected_output_type: recap_digest_notes
          prompt_sequence_ref: flow_prompt_pack_2026-06-17_F3.S3
          capture_focus:
            - next_step_guess
            - model_usage
            - artifact_created
          completion_marker: not_started
          validation_status: valid
      recap_digest_required: true
    prompt_pack_ref:
      flow_prompt_pack_path: artifacts/flows/prompt_packs/2026-06-17/F3-prompt-pack.md
      prompt_pack_status: generated
      prompt_pack_authority: references/flow-prompt-pack-contract.md
    usage_tracking_refs:
      planned_usage_budget_ref: usage/planned/2026-06-17-F3.yaml
      routing_recommendation_ref: usage/routing/2026-06-17-F3.yaml
      usage_tracking_status: planned
      expected_usage_capture_fields:
        - provider_used
        - surface_class_used
        - prompt_count
        - result_quality_signal
    flow_execution_capture_preparation:
      capture_status: prepared
      capture_instructions:
        - Record what was created.
        - Record the provider or surface used when known.
        - Record blockers and next-step guesses.
    FlowRecap_handoff_block:
      handoff_id: FlowRecap_handoff_2026-06-17_F3
      flow_packet_ref: artifacts/flows/packets/2026-06-17/F3.md
      raw_flow_dump_expected: true
      skipped_flow_marker_allowed: true
      context_to_pass:
        - flow_identity
        - flow_context_summary
        - workflow_process_labels
        - flow_sprint_plan
        - prompt_pack_ref
        - usage_tracking_refs
        - raw_flow_dump_template
        - operator_review_flags
      required_operator_completion_marker: done
      FlowRecap_ready_status: ready_after_operator_execution
      boundary_note: PreCapNextDay prepares this handoff but does not run FlowRecap.
    operator_review_flags:
      - workflow_labels_should_be_confirmed
    validation_status: valid_with_warnings

  compressed_Residual_flow_packet:
    packet_id: flow_packet_2026-06-16_F4
    artifact_name: flow_packet
    execution_day: "2026-06-17"
    generation_mode: calendar_constrained_mode
    review_status: operator_review_recommended
    flow_identity:
      flow_id: F4
      flow_slot: F4
      project: Residual
      flow_role: overflow_recovery_lagging_threads_cross_project_cleanup
      flow_status: compressed
      default_flow: true
      compression_reason: Limited day capacity; only recovery and carry-forward capture preserved.
    flow_sprint_plan:
      sprint_policy: compressed_single_sprint
      sprint_count: 1
      recap_digest_required: true
      compression_handling:
        compression_status: compressed_single_sprint
        reason: Calendar-constrained day.
        preserved_sprint_roles:
          - recap_digest_preparation_sprint
        dropped_or_merged_elements:
          - first_work_sprint
          - second_work_or_deepening_sprint
        operator_review_needed: true
    validation_status: operator_review_recommended

  skipped_MasterOfArts_flow_packet:
    packet_id: flow_packet_2026-06-16_F2
    artifact_name: flow_packet
    execution_day: "2026-06-17"
    generation_mode: standard_mode
    review_status: operator_review_recommended
    flow_identity:
      flow_id: F2
      flow_slot: F2
      project: MasterOfArts
      flow_role: coaching_business_website_offer_content_work
      flow_status: skipped
      default_flow: true
      override_reason: Operator deferred website work for the day.
    flow_sprint_plan:
      sprint_policy: skipped
      sprint_count: 0
      sprints: []
      recap_digest_required: false
    flow_execution_capture_preparation:
      capture_status: not_needed_for_skipped_flow
    validation_status: operator_review_recommended
```

---

# VALIDATION - FILE-SPECIFIC CHECKS

- [ ] Exactly one file was produced.
- [ ] File path is `.claude/skills/precap-next-day/references/flow-packet-contract.md`.
- [ ] File owns `flow_packet`, `flow_sprint_plan`, raw dump preparation, skipped-flow marker template, and `FlowRecap_handoff_block`.
- [ ] File does not redefine `next_day_plan`, `flow_prompt_pack`, `prompt_packet`, `routing_decision`, `planned_usage_budget`, `usage_delta`, workflow taxonomies, process taxonomies, or expected-output schema.
- [ ] YAML blocks use 2-space indentation.
- [ ] Numeric constraints use typed `type`/`min`/`max` objects.
- [ ] Compression, omission, skipped-flow, and FlowRecap handoff cases are represented.
- [ ] File prepares raw execution capture but does not run FlowRecap.
- [ ] File does not execute project work, merge project status, create calendar events, or finalize OpenRouter model mapping.

---

# NEXT PROMPT

Paste this next:
> Prompt PND5:
> Create exactly one file.
>
> # FILE: .claude/skills/precap-next-day/references/flow-prompt-pack-contract.md
>
> File type: reference_contract.
> Schema ownership: owns flow_prompt_pack as the per-flow operational prompt container produced by PreCapNextDay.
> Context carry-forward:
> - .claude/skills/precap-next-day/SKILL.md
> - .claude/skills/precap-next-day/references/input-intake-and-resilience-contract.md
> - .claude/skills/precap-next-day/references/daily-plan-output-contract.md
> - .claude/skills/precap-next-day/references/flow-packet-contract.md
> - .claude/skills/prompt-engineering/references/prompt-packet-contract.md
> - .claude/skills/ai-routing-and-usage-tracking/references/routing-recommendation-packet-contract.md
> - .claude/skills/workflow-process-design/references/prompt-process-alignment-validation.md
>
> This file must define:
> - flow_prompt_pack schema
> - one-prompt-pack-per-flow policy
> - sprint prompt sequence grouping
> - prompt_packet references without duplicating prompt_packet schema
> - routing and usage references without duplicating routing schemas
> - provider and prompt-design rationale references
> - start prompt and follow-up prompt placement rules
> - light capture hints and FlowRecap preparation notes
> - minimal examples
>
> Rules:
> - Do not duplicate prompt_packet schema owned by prompt-engineering.
> - Do not define routing_decision, planned_usage_budget, or usage_delta schemas.
> - Do not create multiple alternative prompt systems by default.
> - Do not require a machine-readable capture block inside every prompt.
> - Use YAML with 2-space indentation.
>
> Next prompt target: Prompt PND6.
