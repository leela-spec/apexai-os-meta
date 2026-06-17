# FILE: .claude/skills/precap-next-day/references/daily-plan-output-contract.md

# Daily Plan Output Contract

```yaml
daily_plan_output_contract:
  artifact_name: next_day_plan
  file_role: precap_next_day_reference_contract
  purpose: >
    Define the minimum valid structure for the PreCapNextDay output artifact:
    a resilient next_day_plan that compiles day intent, fixed flow structure,
    flow packet references, prompt pack references, usage planning, workflow
    block requests, raw execution capture preparation, and operator review
    flags. This contract is a reference file, not a template and not a project
    execution plan.

  ownership:
    owns:
      - next_day_plan
      - daily_plan_metadata
      - daily_plan_context_summary
      - daily_flow_overview
      - generated_file_index
      - day_level_operator_review_flags
      - day_level_completion_gate
      - day_level_validation_rules
    must_not_own:
      - input_intake_schema
      - flow_packet_schema
      - flow_prompt_pack_schema
      - prompt_packet_schema
      - routing_decision_schema
      - planned_usage_budget_schema
      - usage_delta_schema
      - workflow_stage_taxonomy
      - process_stage_taxonomy
      - calendar_event_write_schema
      - FlowRecap_output
      - project_status_merge
      - project_execution

  dependency_contracts:
    input_resilience_contract: references/input-intake-and-resilience-contract.md
    flow_packet_contract: references/flow-packet-contract.md
    flow_prompt_pack_contract: references/flow-prompt-pack-contract.md
    prompt_engineering_dependency_contract: references/prompt-engineering-dependency-contract.md
    usage_tracking_dependency_contract: references/usage-tracking-dependency-contract.md
    calendar_event_write_contract: references/calendar-event-write-contract.md
    workflow_process_validation_contract: references/workflow-process-validation-contract.md

  global_rules:
    one_next_day_plan_per_execution_day: true
    fixed_daily_flows_are_default: true
    compressed_or_omitted_flows_allowed: true
    omitted_flow_requires_reason: true
    bootstrap_mode_allowed: true
    calendar_write_requires_operator_acceptance: true
    prompt_execution_not_performed: true
    project_work_not_executed: true
    FlowRecap_not_run: true
    status_merge_not_run: true
    no_final_OpenRouter_model_map: true
```

## Schema: next_day_plan

```yaml
next_day_plan:
  type: object
  required:
    - plan_id
    - artifact_name
    - created_or_updated_at
    - execution_day
    - generation_mode
    - review_status
    - daily_plan_metadata
    - daily_plan_context_summary
    - daily_flow_overview
    - generated_file_index
    - day_level_operator_review_flags
    - day_level_completion_gate
    - validation_status
  fields:
    plan_id:
      type: string
      format: "next_day_plan_<YYYY_MM_DD>_<short_slug>"
      required: true

    artifact_name:
      type: string
      allowed:
        - next_day_plan
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

    daily_plan_metadata:
      type: object_ref
      ref: daily_plan_metadata
      required: true

    daily_plan_context_summary:
      type: object_ref
      ref: daily_plan_context_summary
      required: true

    daily_flow_overview:
      type: object_ref
      ref: daily_flow_overview
      required: true

    generated_file_index:
      type: object_ref
      ref: generated_file_index
      required: true

    usage_tracking_summary:
      type: object_ref
      ref: day_usage_tracking_summary
      required: false

    workflow_block_summary:
      type: object_ref
      ref: workflow_block_summary
      required: false

    FlowRecap_preparation_summary:
      type: object_ref
      ref: FlowRecap_preparation_summary
      required: true

    day_level_operator_review_flags:
      type: object_ref
      ref: day_level_operator_review_flags
      required: true

    day_level_completion_gate:
      type: object_ref
      ref: day_level_completion_gate
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

## Schema: daily_plan_metadata

```yaml
daily_plan_metadata:
  type: object
  required:
    - plan_title
    - plan_role
    - operator_intent_status
    - source_context_status
    - input_resilience_mode
    - fixed_flow_policy
    - sprint_policy
  fields:
    plan_title:
      type: string
      required: true
      example: "PreCap Next Day Plan — 2026-06-17"

    plan_role:
      type: string
      allowed:
        - resilient_daily_orchestration_plan
      required: true

    operator_intent_status:
      type: string
      allowed:
        - supplied
        - inferred_from_context
        - missing
        - unclear
      required: true

    source_context_status:
      type: string
      allowed:
        - complete_enough
        - partial
        - minimal
        - missing
        - contradictory
      required: true

    input_resilience_mode:
      type: string
      allowed:
        - full_context_mode
        - degraded_context_mode
        - bootstrap_mode
        - recovery_mode
      required: true

    fixed_flow_policy:
      type: object
      required: true
      fields:
        default_flows_required:
          type: boolean
        compression_allowed:
          type: boolean
        omission_allowed:
          type: boolean
        omission_requires_reason:
          type: boolean

    sprint_policy:
      type: object
      required: true
      fields:
        default_sprints_per_flow:
          type: integer
          min: 1
          max: 3
        compressed_sprints_allowed:
          type: boolean
        recap_digest_sprint_expected:
          type: boolean
```

## Schema: daily_plan_context_summary

```yaml
daily_plan_context_summary:
  type: object
  required:
    - used_inputs
    - missing_inputs
    - assumptions
    - degraded_mode_reasons
    - day_constraints
    - planning_conflicts
  fields:
    used_inputs:
      type: list
      item_type: string
      required: true
      allowed_items:
        - operator_day_intent
        - current_project_status_overview
        - flow_recap_packets
        - skipped_flow_markers
        - recap_day_notes
        - precap_week_output
        - weekly_plan_packet
        - fixed_calendar_constraints
        - calendar_events
        - AI_surface_inventory
        - model_usage_summary
        - detailed_project_state_files
        - prior_next_day_plan
        - manual_operator_notes

    missing_inputs:
      type: list
      item_type: string
      required: true

    assumptions:
      type: list
      item_type: string
      min_items: 0
      max_items: 12
      required: true

    degraded_mode_reasons:
      type: list
      item_type: string
      min_items: 0
      max_items: 8
      required: true

    day_constraints:
      type: list
      item_type: string
      min_items: 0
      max_items: 12
      required: true

    planning_conflicts:
      type: list
      item_type: string
      min_items: 0
      max_items: 12
      required: true
```

## Schema: daily_flow_overview

```yaml
daily_flow_overview:
  type: object
  required:
    - flows
    - flow_count
    - omitted_flows
    - compressed_flows
    - residual_policy
  fields:
    flows:
      type: list
      item_ref: daily_flow_summary
      min_items: 1
      max_items: 4
      required: true

    flow_count:
      type: integer
      min: 1
      max: 4
      required: true

    omitted_flows:
      type: list
      item_ref: omitted_flow_summary
      min_items: 0
      max_items: 4
      required: true

    compressed_flows:
      type: list
      item_type: string
      min_items: 0
      max_items: 4
      required: true

    residual_policy:
      type: string
      allowed:
        - split_by_project
        - single_lagging_project
        - operator_selected
        - omitted_with_reason
        - bootstrap_placeholder
      required: true
```

## Schema: daily_flow_summary

```yaml
daily_flow_summary:
  type: object
  required:
    - flow_id
    - project
    - flow_role
    - flow_status
    - sprint_count
    - primary_goal
    - expected_outputs
    - workflow_process_labels
    - file_refs
    - review_flags
  fields:
    flow_id:
      type: string
      allowed:
        - F1
        - F2
        - F3
        - F4
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
      required: true
      examples:
        - app_product_or_system_work
        - coaching_business_website_offer_content_work
        - orchestration_system_buildout
        - overflow_recovery_lagging_threads_cross_project_cleanup

    flow_status:
      type: string
      allowed:
        - planned
        - compressed
        - optional
        - omitted
        - blocked
        - low_confidence_auto_generated
      required: true

    sprint_count:
      type: integer
      min: 0
      max: 3
      required: true

    primary_goal:
      type: string
      required: true

    expected_outputs:
      type: list
      item_type: string
      min_items: 0
      max_items: 8
      required: true

    workflow_process_labels:
      type: object
      required: true
      fields:
        workflow_stage:
          type: string
          required: false
        process_stage:
          type: string
          required: false
        expected_output_type:
          type: string
          required: false
        validation_status:
          type: string
          allowed:
            - valid
            - valid_with_warnings
            - operator_review_recommended
            - low_confidence_auto_generated
            - blocked_by_missing_operator_decision

    file_refs:
      type: object_ref
      ref: daily_flow_file_refs
      required: true

    review_flags:
      type: list
      item_type: string
      min_items: 0
      max_items: 8
      required: true
```

## Schema: daily_flow_file_refs

```yaml
daily_flow_file_refs:
  type: object
  required:
    - flow_packet_ref
    - flow_prompt_pack_ref
    - raw_flow_dump_template_ref
    - skipped_flow_marker_template_ref
    - FlowRecap_handoff_block_ref
  fields:
    flow_packet_ref:
      type: string
      format: "relative_or_logical_path_to_flow_packet"
      required: true

    flow_prompt_pack_ref:
      type: string
      format: "relative_or_logical_path_to_flow_prompt_pack"
      required: true

    raw_flow_dump_template_ref:
      type: string
      format: "relative_or_logical_path_to_raw_flow_dump_template_or_section"
      required: true

    skipped_flow_marker_template_ref:
      type: string
      format: "relative_or_logical_path_to_skipped_flow_marker_template_or_section"
      required: true

    FlowRecap_handoff_block_ref:
      type: string
      format: "relative_or_logical_path_to_FlowRecap_handoff_block_or_section"
      required: true

    calendar_event_write_request_ref:
      type: string
      required: false

    planned_usage_budget_ref:
      type: string
      required: false

    workflow_process_validation_ref:
      type: string
      required: false
```

## Schema: omitted_flow_summary

```yaml
omitted_flow_summary:
  type: object
  required:
    - flow_id
    - project
    - omission_reason
    - operator_review_required
  fields:
    flow_id:
      type: string
      allowed:
        - F1
        - F2
        - F3
        - F4
      required: true

    project:
      type: string
      required: true

    omission_reason:
      type: string
      required: true
      examples:
        - blocked_by_missing_context
        - intentionally_skipped_for_recovery
        - replaced_by_higher_priority_residual_work
        - day_capacity_too_limited
        - operator_override

    operator_review_required:
      type: boolean
      required: true
```

## Schema: generated_file_index

```yaml
generated_file_index:
  type: object
  required:
    - day_plan_ref
    - generated_or_defined_files
    - generated_file_count
    - files_requiring_operator_action
  fields:
    day_plan_ref:
      type: string
      required: true

    generated_or_defined_files:
      type: list
      item_ref: generated_file_ref
      min_items: 1
      max_items: 40
      required: true

    generated_file_count:
      type: integer
      min: 1
      max: 40
      required: true

    files_requiring_operator_action:
      type: list
      item_ref: operator_action_file_ref
      min_items: 0
      max_items: 20
      required: true
```

## Schema: generated_file_ref

```yaml
generated_file_ref:
  type: object
  required:
    - artifact_name
    - artifact_role
    - logical_path
    - production_status
  fields:
    artifact_name:
      type: string
      required: true
      examples:
        - next_day_plan
        - flow_packet
        - flow_prompt_pack
        - raw_flow_dump_template
        - skipped_flow_marker_template
        - calendar_event_write_request
        - planned_usage_budget

    artifact_role:
      type: string
      required: true

    logical_path:
      type: string
      required: true

    production_status:
      type: string
      allowed:
        - created
        - defined_inline
        - referenced_existing
        - pending_operator_approval
        - blocked
      required: true

    validation_status:
      type: string
      allowed:
        - valid
        - valid_with_warnings
        - operator_review_recommended
        - low_confidence_auto_generated
        - blocked_by_missing_operator_decision
      required: false
```

## Schema: operator_action_file_ref

```yaml
operator_action_file_ref:
  type: object
  required:
    - artifact_name
    - action_needed
    - reason
  fields:
    artifact_name:
      type: string
      required: true

    action_needed:
      type: string
      allowed:
        - approve
        - edit
        - supply_missing_input
        - create_calendar_event
        - accept_calendar_write_request
        - execute_flow
        - run_FlowRecap_after_execution
        - skip_flow_with_marker
      required: true

    reason:
      type: string
      required: true
```

## Schema: day_usage_tracking_summary

```yaml
day_usage_tracking_summary:
  type: object
  required:
    - usage_plan_status
    - routing_recommendation_status
    - scarce_surface_use_policy
    - usage_tracking_tags_present
  fields:
    usage_plan_status:
      type: string
      allowed:
        - present
        - partial
        - missing_dependency
        - low_confidence_auto_generated
      required: true

    routing_recommendation_status:
      type: string
      allowed:
        - present
        - partial
        - not_needed
        - missing_dependency
        - operator_review_recommended
      required: true

    scarce_surface_use_policy:
      type: string
      allowed:
        - deliberate_monthly_quota_use
        - conserve_due_to_low_value_task
        - unknown_quota_operator_review
        - no_scarce_surface_planned
      required: true

    usage_tracking_tags_present:
      type: boolean
      required: true
```

## Schema: workflow_block_summary

```yaml
workflow_block_summary:
  type: object
  required:
    - calendar_mode
    - workflow_blocks_defined
    - write_requests_present
    - operator_acceptance_required
  fields:
    calendar_mode:
      type: string
      allowed:
        - calendar_read_available
        - manual_constraints_only
        - calendar_unavailable
        - calendar_not_requested
      required: true

    workflow_blocks_defined:
      type: boolean
      required: true

    write_requests_present:
      type: boolean
      required: true

    operator_acceptance_required:
      type: boolean
      required: true

    write_policy_note:
      type: string
      required: false
      rule: "Calendar write requests may define workflow blocks only and require operator acceptance before write execution."
```

## Schema: FlowRecap_preparation_summary

```yaml
FlowRecap_preparation_summary:
  type: object
  required:
    - raw_flow_dump_templates_present
    - skipped_flow_marker_templates_present
    - FlowRecap_handoff_blocks_present
    - recap_capture_scope
  fields:
    raw_flow_dump_templates_present:
      type: boolean
      required: true

    skipped_flow_marker_templates_present:
      type: boolean
      required: true

    FlowRecap_handoff_blocks_present:
      type: boolean
      required: true

    recap_capture_scope:
      type: list
      item_type: string
      required: true
      allowed_items:
        - what_was_done
        - outputs_created
        - decisions_made
        - blockers
        - skipped_or_partial_work
        - prompt_results
        - usage_delta
        - next_step_guess
        - operator_validation_notes
```

## Schema: day_level_operator_review_flags

```yaml
day_level_operator_review_flags:
  type: object
  required:
    - flags
    - review_required
    - review_reason
  fields:
    flags:
      type: list
      item_type: string
      min_items: 0
      max_items: 20
      required: true
      allowed_items:
        - missing_operator_day_intent
        - missing_project_status_context
        - missing_weekly_plan
        - missing_calendar_context
        - missing_AI_surface_inventory
        - missing_model_usage_summary
        - conflicting_priorities
        - flow_goal_unclear
        - omitted_flow_requires_approval
        - compressed_flow_requires_approval
        - prompt_pack_low_confidence
        - workflow_process_alignment_warning
        - calendar_write_requires_acceptance
        - scarce_quota_use_requires_review
        - bootstrap_mode_used

    review_required:
      type: boolean
      required: true

    review_reason:
      type: string
      required: true
```

## Schema: day_level_completion_gate

```yaml
day_level_completion_gate:
  type: object
  required:
    - next_day_plan_present
    - each_active_flow_has_flow_packet_ref
    - each_active_flow_has_prompt_pack_ref
    - raw_flow_dump_capture_prepared
    - skipped_flow_marker_capture_prepared
    - FlowRecap_handoff_prepared
    - operator_review_flags_present
    - no_project_work_executed
    - no_FlowRecap_run
    - no_status_merge_run
  fields:
    next_day_plan_present:
      type: boolean
      required: true
    each_active_flow_has_flow_packet_ref:
      type: boolean
      required: true
    each_active_flow_has_prompt_pack_ref:
      type: boolean
      required: true
    raw_flow_dump_capture_prepared:
      type: boolean
      required: true
    skipped_flow_marker_capture_prepared:
      type: boolean
      required: true
    FlowRecap_handoff_prepared:
      type: boolean
      required: true
    operator_review_flags_present:
      type: boolean
      required: true
    no_project_work_executed:
      type: boolean
      required: true
    no_FlowRecap_run:
      type: boolean
      required: true
    no_status_merge_run:
      type: boolean
      required: true
```

## Validation Rules

```yaml
next_day_plan_validation_rules:
  required_structure:
    next_day_plan_has_metadata: true
    context_summary_present: true
    active_flows_have_file_refs: true
    generated_file_index_present: true
    operator_review_flags_present: true
    completion_gate_present: true

  flow_rules:
    fixed_flow_ids_are_used_when_possible: true
    omitted_flow_has_reason: true
    compressed_flow_has_status: true
    sprint_count_is_between_0_and_3: true
    residual_flow_policy_is_explicit: true

  dependency_rules:
    flow_packet_schema_not_redefined: true
    prompt_pack_schema_not_redefined: true
    routing_schema_not_redefined: true
    usage_budget_schema_not_redefined: true
    calendar_write_schema_not_redefined: true
    workflow_taxonomies_not_redefined: true

  boundary_rules:
    no_project_work_execution: true
    no_prompt_execution: true
    no_FlowRecap_output: true
    no_project_status_merge: true
    no_calendar_write_without_operator_acceptance: true
    no_final_OpenRouter_model_map: true
```

## Minimal Examples

### Example 1 — Standard four-flow day

```yaml
next_day_plan_example_standard:
  plan_id: next_day_plan_2026_06_17_standard
  artifact_name: next_day_plan
  created_or_updated_at: "2026-06-16"
  execution_day: "2026-06-17"
  generation_mode: standard_mode
  review_status: operator_review_recommended
  daily_plan_metadata:
    plan_title: "PreCap Next Day Plan — 2026-06-17"
    plan_role: resilient_daily_orchestration_plan
    operator_intent_status: supplied
    source_context_status: partial
    input_resilience_mode: degraded_context_mode
    fixed_flow_policy:
      default_flows_required: true
      compression_allowed: true
      omission_allowed: true
      omission_requires_reason: true
    sprint_policy:
      default_sprints_per_flow: 3
      compressed_sprints_allowed: true
      recap_digest_sprint_expected: true
  daily_plan_context_summary:
    used_inputs:
      - operator_day_intent
      - current_project_status_overview
      - AI_surface_inventory
      - model_usage_summary
    missing_inputs:
      - calendar_events
      - weekly_plan_packet
    assumptions:
      - "Use fixed F1-F4 flow grammar because no contrary operator override was supplied."
    degraded_mode_reasons:
      - "Calendar events were not available."
    day_constraints: []
    planning_conflicts: []
  daily_flow_overview:
    flow_count: 4
    residual_policy: split_by_project
    omitted_flows: []
    compressed_flows: []
    flows:
      - flow_id: F1
        project: Leela
        flow_role: app_product_or_system_work
        flow_status: planned
        sprint_count: 3
        primary_goal: "Define next concrete Leela product/system chunk."
        expected_outputs:
          - product_system_notes
          - implementation_boundary_candidates
        workflow_process_labels:
          workflow_stage: system_design
          process_stage: first_definition_pass
          expected_output_type: structured_design_notes
          validation_status: valid_with_warnings
        file_refs:
          flow_packet_ref: "flows/2026-06-17/F1.md"
          flow_prompt_pack_ref: "flows/2026-06-17/F1-prompt-pack.md"
          raw_flow_dump_template_ref: "flows/2026-06-17/F1-raw-dump.md"
          skipped_flow_marker_template_ref: "flows/2026-06-17/F1-skipped.md"
          FlowRecap_handoff_block_ref: "flows/2026-06-17/F1.md#flowrecap-handoff"
        review_flags: []
  generated_file_index:
    day_plan_ref: "plans/daily/2026-06-17.md"
    generated_file_count: 5
    generated_or_defined_files:
      - artifact_name: next_day_plan
        artifact_role: day_level_plan
        logical_path: "plans/daily/2026-06-17.md"
        production_status: created
        validation_status: valid_with_warnings
    files_requiring_operator_action:
      - artifact_name: next_day_plan
        action_needed: approve
        reason: "Calendar context is missing, so day timing requires operator review."
  FlowRecap_preparation_summary:
    raw_flow_dump_templates_present: true
    skipped_flow_marker_templates_present: true
    FlowRecap_handoff_blocks_present: true
    recap_capture_scope:
      - what_was_done
      - outputs_created
      - decisions_made
      - blockers
      - prompt_results
      - usage_delta
      - next_step_guess
  day_level_operator_review_flags:
    flags:
      - missing_calendar_context
    review_required: true
    review_reason: "Calendar context was unavailable."
  day_level_completion_gate:
    next_day_plan_present: true
    each_active_flow_has_flow_packet_ref: true
    each_active_flow_has_prompt_pack_ref: true
    raw_flow_dump_capture_prepared: true
    skipped_flow_marker_capture_prepared: true
    FlowRecap_handoff_prepared: true
    operator_review_flags_present: true
    no_project_work_executed: true
    no_FlowRecap_run: true
    no_status_merge_run: true
  validation_status: valid_with_warnings
```

### Example 2 — Bootstrap mode with compressed flows

```yaml
next_day_plan_example_bootstrap:
  plan_id: next_day_plan_2026_06_17_bootstrap
  artifact_name: next_day_plan
  created_or_updated_at: "2026-06-16"
  execution_day: "2026-06-17"
  generation_mode: bootstrap_mode
  review_status: low_confidence_auto_generated
  daily_plan_metadata:
    plan_title: "PreCap Next Day Plan — Bootstrap"
    plan_role: resilient_daily_orchestration_plan
    operator_intent_status: missing
    source_context_status: missing
    input_resilience_mode: bootstrap_mode
    fixed_flow_policy:
      default_flows_required: true
      compression_allowed: true
      omission_allowed: true
      omission_requires_reason: true
    sprint_policy:
      default_sprints_per_flow: 1
      compressed_sprints_allowed: true
      recap_digest_sprint_expected: true
  daily_plan_context_summary:
    used_inputs:
      - manual_operator_notes
    missing_inputs:
      - operator_day_intent
      - current_project_status_overview
      - weekly_plan_packet
      - calendar_events
      - AI_surface_inventory
      - model_usage_summary
    assumptions:
      - "Create a low-confidence skeleton day plan using fixed project slots."
    degraded_mode_reasons:
      - "No reliable planning context was supplied."
    day_constraints: []
    planning_conflicts: []
  daily_flow_overview:
    flow_count: 4
    residual_policy: bootstrap_placeholder
    omitted_flows: []
    compressed_flows:
      - F1
      - F2
      - F3
      - F4
    flows:
      - flow_id: F1
        project: Leela
        flow_role: app_product_or_system_work
        flow_status: low_confidence_auto_generated
        sprint_count: 1
        primary_goal: "Clarify the next Leela work target."
        expected_outputs:
          - clarification_notes
        workflow_process_labels:
          workflow_stage: intake
          process_stage: context_reconstruction
          expected_output_type: clarification_notes
          validation_status: low_confidence_auto_generated
        file_refs:
          flow_packet_ref: "flows/bootstrap/F1.md"
          flow_prompt_pack_ref: "flows/bootstrap/F1-prompt-pack.md"
          raw_flow_dump_template_ref: "flows/bootstrap/F1-raw-dump.md"
          skipped_flow_marker_template_ref: "flows/bootstrap/F1-skipped.md"
          FlowRecap_handoff_block_ref: "flows/bootstrap/F1.md#flowrecap-handoff"
        review_flags:
          - bootstrap_mode_used
          - flow_goal_unclear
  generated_file_index:
    day_plan_ref: "plans/daily/bootstrap.md"
    generated_file_count: 1
    generated_or_defined_files:
      - artifact_name: next_day_plan
        artifact_role: bootstrap_day_plan
        logical_path: "plans/daily/bootstrap.md"
        production_status: created
        validation_status: low_confidence_auto_generated
    files_requiring_operator_action:
      - artifact_name: next_day_plan
        action_needed: supply_missing_input
        reason: "Bootstrap plan needs operator intent before execution."
  FlowRecap_preparation_summary:
    raw_flow_dump_templates_present: true
    skipped_flow_marker_templates_present: true
    FlowRecap_handoff_blocks_present: true
    recap_capture_scope:
      - what_was_done
      - skipped_or_partial_work
      - next_step_guess
      - operator_validation_notes
  day_level_operator_review_flags:
    flags:
      - missing_operator_day_intent
      - missing_project_status_context
      - bootstrap_mode_used
    review_required: true
    review_reason: "Plan was created without reliable source context."
  day_level_completion_gate:
    next_day_plan_present: true
    each_active_flow_has_flow_packet_ref: true
    each_active_flow_has_prompt_pack_ref: true
    raw_flow_dump_capture_prepared: true
    skipped_flow_marker_capture_prepared: true
    FlowRecap_handoff_prepared: true
    operator_review_flags_present: true
    no_project_work_executed: true
    no_FlowRecap_run: true
    no_status_merge_run: true
  validation_status: low_confidence_auto_generated
```

---

# VALIDATION — FILE-SPECIFIC CHECKS

- [ ] Exactly one file was produced.
- [ ] The file path is `.claude/skills/precap-next-day/references/daily-plan-output-contract.md`.
- [ ] The file owns `next_day_plan` and day-level plan structure only.
- [ ] The file does not redefine `input_intake`, `flow_packet`, `flow_prompt_pack`, `prompt_packet`, `routing_decision`, `planned_usage_budget`, `usage_delta`, workflow taxonomies, or calendar write schemas.
- [ ] YAML blocks use 2-space indentation.
- [ ] Numeric constraints use typed objects with `type`, `min`, and `max` where relevant.
- [ ] Validation statuses use the canonical allowed values.
- [ ] The contract supports full, degraded, recovery, calendar-constrained, prompt-heavy, and bootstrap modes.
- [ ] The contract prepares raw-flow-dump and skipped-flow-marker capture without running FlowRecap.
- [ ] The contract forbids project execution, prompt execution, FlowRecap output, project status merge, calendar writes without acceptance, and final OpenRouter model mapping.

---

# NEXT PROMPT

Paste this next:
> Prompt PND4:
> Create exactly one file.
>
> # FILE: .claude/skills/precap-next-day/references/flow-packet-contract.md
>
> File type: reference_contract.
> Schema ownership: owns flow_packet, sprint block structure, raw_flow_dump_template, skipped_flow_marker_template, and FlowRecap_handoff_block.
> Context carry-forward:
> - .claude/skills/precap-next-day/SKILL.md
> - .claude/skills/precap-next-day/references/input-intake-and-resilience-contract.md
> - .claude/skills/precap-next-day/references/daily-plan-output-contract.md
>
> This file must define:
> - flow_packet schema
> - sprint block schema
> - flow goal and expected output fields
> - raw_flow_dump_template
> - skipped_flow_marker_template
> - FlowRecap_handoff_block
> - flow compression and omission rules
> - minimal examples
>
> Rules:
> - Do not define next_day_plan schema owned by PND3.
> - Do not define flow_prompt_pack schema owned by PND5.
> - Do not define prompt_packet schema owned by prompt-engineering.
> - Do not execute project work.
> - Use YAML with 2-space indentation.
>
> Next prompt target: Prompt PND5.
