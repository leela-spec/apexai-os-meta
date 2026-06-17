# PreCap Next Day — Contract-Only Example Output

```yaml
next_day_plan_example_contract_only:
  plan_id: next_day_plan_2026_06_18_bootstrap_contract_only
  artifact_name: next_day_plan
  created_or_updated_at: "2026-06-17"
  execution_day: "2026-06-18"
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
        primary_goal: "Clarify the next work target."
        expected_outputs: []
        workflow_process_labels:
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

      - flow_id: F2
        project: MasterOfArts
        flow_role: coaching_business_website_offer_content_work
        flow_status: low_confidence_auto_generated
        sprint_count: 1
        primary_goal: "Clarify the next work target."
        expected_outputs: []
        workflow_process_labels:
          validation_status: low_confidence_auto_generated
        file_refs:
          flow_packet_ref: "flows/bootstrap/F2.md"
          flow_prompt_pack_ref: "flows/bootstrap/F2-prompt-pack.md"
          raw_flow_dump_template_ref: "flows/bootstrap/F2-raw-dump.md"
          skipped_flow_marker_template_ref: "flows/bootstrap/F2-skipped.md"
          FlowRecap_handoff_block_ref: "flows/bootstrap/F2.md#flowrecap-handoff"
        review_flags:
          - bootstrap_mode_used
          - flow_goal_unclear

      - flow_id: F3
        project: Apex
        flow_role: orchestration_system_buildout
        flow_status: low_confidence_auto_generated
        sprint_count: 1
        primary_goal: "Clarify the next work target."
        expected_outputs: []
        workflow_process_labels:
          validation_status: low_confidence_auto_generated
        file_refs:
          flow_packet_ref: "flows/bootstrap/F3.md"
          flow_prompt_pack_ref: "flows/bootstrap/F3-prompt-pack.md"
          raw_flow_dump_template_ref: "flows/bootstrap/F3-raw-dump.md"
          skipped_flow_marker_template_ref: "flows/bootstrap/F3-skipped.md"
          FlowRecap_handoff_block_ref: "flows/bootstrap/F3.md#flowrecap-handoff"
        review_flags:
          - bootstrap_mode_used
          - flow_goal_unclear

      - flow_id: F4
        project: Residual
        flow_role: overflow_recovery_lagging_threads_cross_project_cleanup
        flow_status: low_confidence_auto_generated
        sprint_count: 1
        primary_goal: "Clarify the next work target."
        expected_outputs: []
        workflow_process_labels:
          validation_status: low_confidence_auto_generated
        file_refs:
          flow_packet_ref: "flows/bootstrap/F4.md"
          flow_prompt_pack_ref: "flows/bootstrap/F4-prompt-pack.md"
          raw_flow_dump_template_ref: "flows/bootstrap/F4-raw-dump.md"
          skipped_flow_marker_template_ref: "flows/bootstrap/F4-skipped.md"
          FlowRecap_handoff_block_ref: "flows/bootstrap/F4.md#flowrecap-handoff"
        review_flags:
          - bootstrap_mode_used
          - flow_goal_unclear

  generated_file_index:
    day_plan_ref: "plans/daily/bootstrap.md"
    generated_file_count: 13
    generated_or_defined_files:
      - artifact_name: next_day_plan
        artifact_role: bootstrap_day_plan
        logical_path: "plans/daily/bootstrap.md"
        production_status: defined_inline
        validation_status: low_confidence_auto_generated

      - artifact_name: flow_packet
        artifact_role: per_flow_execution_container
        logical_path: "flows/bootstrap/F1.md"
        production_status: defined_inline
        validation_status: low_confidence_auto_generated

      - artifact_name: flow_packet
        artifact_role: per_flow_execution_container
        logical_path: "flows/bootstrap/F2.md"
        production_status: defined_inline
        validation_status: low_confidence_auto_generated

      - artifact_name: flow_packet
        artifact_role: per_flow_execution_container
        logical_path: "flows/bootstrap/F3.md"
        production_status: defined_inline
        validation_status: low_confidence_auto_generated

      - artifact_name: flow_packet
        artifact_role: per_flow_execution_container
        logical_path: "flows/bootstrap/F4.md"
        production_status: defined_inline
        validation_status: low_confidence_auto_generated

      - artifact_name: flow_prompt_pack
        artifact_role: per_flow_prompt_container
        logical_path: "flows/bootstrap/F1-prompt-pack.md"
        production_status: defined_inline
        validation_status: low_confidence_auto_generated

      - artifact_name: flow_prompt_pack
        artifact_role: per_flow_prompt_container
        logical_path: "flows/bootstrap/F2-prompt-pack.md"
        production_status: defined_inline
        validation_status: low_confidence_auto_generated

      - artifact_name: flow_prompt_pack
        artifact_role: per_flow_prompt_container
        logical_path: "flows/bootstrap/F3-prompt-pack.md"
        production_status: defined_inline
        validation_status: low_confidence_auto_generated

      - artifact_name: flow_prompt_pack
        artifact_role: per_flow_prompt_container
        logical_path: "flows/bootstrap/F4-prompt-pack.md"
        production_status: defined_inline
        validation_status: low_confidence_auto_generated

      - artifact_name: raw_flow_dump_template
        artifact_role: execution_capture_shell
        logical_path: "flows/bootstrap/raw-flow-dump-templates.md"
        production_status: defined_inline
        validation_status: low_confidence_auto_generated

      - artifact_name: skipped_flow_marker_template
        artifact_role: skipped_flow_capture_shell
        logical_path: "flows/bootstrap/skipped-flow-marker-templates.md"
        production_status: defined_inline
        validation_status: low_confidence_auto_generated

      - artifact_name: calendar_event_write_request
        artifact_role: workflow_block_request
        logical_path: "calendar/bootstrap-calendar-write-request.md"
        production_status: pending_operator_approval
        validation_status: low_confidence_auto_generated

      - artifact_name: planned_usage_budget
        artifact_role: usage_planning_dependency_reference
        logical_path: "usage/bootstrap-usage-plan.md"
        production_status: blocked
        validation_status: low_confidence_auto_generated

    files_requiring_operator_action:
      - artifact_name: next_day_plan
        action_needed: supply_missing_input
        reason: "Bootstrap plan needs operator intent before execution."

      - artifact_name: calendar_event_write_request
        action_needed: accept_calendar_write_request
        reason: "Calendar writes require explicit operator acceptance before actual write."

      - artifact_name: flow_packet
        action_needed: execute_flow
        reason: "Flow packets are prepared but project work has not been executed."

      - artifact_name: flow_prompt_pack
        action_needed: approve
        reason: "Prompt packs are low-confidence because prompt-engineering and usage dependencies are missing."

  usage_tracking_summary:
    usage_plan_status: low_confidence_auto_generated
    routing_recommendation_status: missing_dependency
    scarce_surface_use_policy: unknown_quota_operator_review
    usage_tracking_tags_present: false

  workflow_block_summary:
    calendar_mode: calendar_unavailable
    workflow_blocks_defined: false
    write_requests_present: true
    operator_acceptance_required: true
    write_policy_note: "Calendar write requests may define workflow blocks only and require operator acceptance before write execution."

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
      - missing_weekly_plan
      - missing_calendar_context
      - missing_AI_surface_inventory
      - missing_model_usage_summary
      - bootstrap_mode_used
      - flow_goal_unclear
      - prompt_pack_low_confidence
      - calendar_write_requires_acceptance
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

## Defined Flow Packet Example Shape

```yaml
flow_packet_example_contract_only_F1:
  packet_id: flow_packet_2026_06_18_F1
  artifact_name: flow_packet
  created_or_updated_at: "2026-06-17"
  execution_day: "2026-06-18"
  generation_mode: bootstrap_mode
  review_status: low_confidence_auto_generated

  flow_packet_metadata:
    package: precap-next-day
    source_skill: precap-next-day
    contract_version: "0.x"
    produced_during: PreCapNextDay
    primary_consumer: operator
    downstream_consumers:
      - FlowRecap
      - prompt-engineering
      - ai-routing-and-usage-tracking
      - workflow-process-design
      - calendar_event_write_contract
      - status-merge_later

  flow_identity:
    flow_id: F1
    flow_slot: F1
    project: Leela
    flow_role: app_product_or_system_work
    flow_status: placeholder
    default_flow: true
    blocker_summary: "No operator day intent or project status context supplied."

  flow_context_summary:
    operator_intent_summary: ""
    project_state_summary: ""
    source_context_refs:
      - "manual_operator_notes"
    constraints: []
    assumptions:
      - "Bootstrap mode used because reliable planning context was not supplied."
    unresolved_inputs:
      - operator_day_intent
      - current_project_status_overview
      - weekly_plan_packet
      - calendar_events
      - AI_surface_inventory
      - model_usage_summary

  workflow_process_labels:
    workflow_stage_ref: ""
    process_stage_ref: ""
    expected_output_type_ref: ""
    validation_status: low_confidence_auto_generated

  flow_sprint_plan:
    sprint_policy: compressed_single_sprint
    sprint_count: 1
    recap_digest_required: true
    compression_handling:
      compression_status: compressed_single_sprint
      reason: "Bootstrap mode with missing planning context."
      preserved_sprint_roles:
        - recap_digest_preparation_sprint
      dropped_or_merged_elements:
        - first_work_sprint
        - second_work_or_deepening_sprint
      operator_review_needed: true
    sprints:
      - sprint_id: S3
        sprint_role: recap_digest_preparation_sprint
        sprint_goal: "Prepare capture context for later operator execution and FlowRecap handoff."
        expected_outputs: []
        expected_output_type_ref: ""
        prompt_ref: "flows/bootstrap/F1-prompt-pack.md"
        completion_marker: not_started
        validation_status: low_confidence_auto_generated
        operator_review_flags:
          - bootstrap_mode_used
          - flow_goal_unclear

  prompt_pack_ref:
    flow_prompt_pack_path: "flows/bootstrap/F1-prompt-pack.md"
    prompt_pack_status: generic_degraded_mode
    prompt_pack_authority: references/flow-prompt-pack-contract.md
    prompt_engineering_dependency_status: missing_use_degraded_generic_prompt_mode
    note: "Prompt pack requires operator review before execution."

  usage_tracking_refs:
    planned_usage_budget_ref: "usage/bootstrap-usage-plan.md"
    routing_recommendation_ref: ""
    usage_tracking_status: degraded_missing_usage_context
    expected_usage_capture_fields:
      - provider_used
      - surface_class_used
      - model_or_mode_if_operator_records_it
      - prompt_count
      - result_quality_signal

  workflow_block_ref:
    workflow_block_status: calendar_unavailable
    calendar_event_write_request_ref: "calendar/bootstrap-calendar-write-request.md"
    note: "No calendar write has been performed."

  flow_execution_capture_preparation:
    raw_flow_dump_template:
      raw_dump_id: raw_flow_dump_2026_06_18_F1
      flow_id: F1
      execution_day: "2026-06-18"
      capture_status: prepared_empty
      fields:
        what_was_done: ""
        outputs_created: ""
        decisions_made: ""
        blockers: ""
        skipped_or_partial_work: ""
        prompt_results: ""
        usage_delta: ""
        next_step_guess: ""
        operator_validation_notes: ""
    skipped_flow_marker_template:
      skipped_marker_id: skipped_flow_marker_2026_06_18_F1
      flow_id: F1
      project: Leela
      marker_status: prepared
      fields:
        skip_or_omission_reason: ""
        recovery_recommendation: ""
        whether_to_reschedule: ""
    capture_instructions:
      - "Capture only after operator execution."
      - "Do not run FlowRecap inside PreCapNextDay."
    capture_status: prepared

  FlowRecap_handoff_block:
    handoff_id: FlowRecap_handoff_2026_06_18_F1
    source_flow_packet_ref: flow_packet_2026_06_18_F1
    source_prompt_pack_ref: "flows/bootstrap/F1-prompt-pack.md"
    raw_flow_dump_template_ref: raw_flow_dump_2026_06_18_F1
    skipped_flow_marker_template_ref: skipped_flow_marker_2026_06_18_F1
    FlowRecap_not_run: true
    expected_capture_scope:
      - what_was_done
      - skipped_or_partial_work
      - next_step_guess
      - operator_validation_notes

  operator_review_flags:
    - missing_operator_day_intent
    - missing_project_status_context
    - bootstrap_mode_used
    - flow_goal_unclear
    - prompt_pack_low_confidence

  validation_status: low_confidence_auto_generated
```

---

## Defined Flow Prompt Pack Example Shape

```yaml
flow_prompt_pack_example_contract_only_F1:
  pack_id: flow_prompt_pack_2026_06_18_F1
  artifact_name: flow_prompt_pack
  created_or_updated_at: "2026-06-17"
  execution_day: "2026-06-18"
  flow_id: F1
  project: Leela
  generation_mode: degraded_generic_prompt_mode
  pack_status: low_confidence_auto_generated

  prompt_pack_policy:
    storage_policy:
      one_file_per_flow_prompt_pack: true
      embedded_in_daily_plan: false
      referenced_from_flow_packet: true
    prompt_system_policy:
      one_primary_prompt_system_only: true
      alternatives_allowed_by_default: false
      follow_up_prompts_allowed: true
      max_follow_up_prompts_per_sprint: 0
    prompt_capture_policy:
      light_capture_hints_allowed: true
      mandatory_machine_readable_capture_block_inside_every_prompt: false
      canonical_capture_home: raw_flow_dump
    provider_rationale_policy:
      provider_rationale_required: true
      prompt_design_rationale_required: true
      rationale_source: degraded_generic_prompt_mode_note
    fallback_policy:
      fallback_notes_allowed: true
      fallback_prompt_system_allowed_by_default: false
      fallback_requires_operator_review: true

  source_flow_packet_ref:
    flow_packet_id: flow_packet_2026_06_18_F1
    flow_packet_path_or_slot: "flows/bootstrap/F1.md"
    flow_id: F1
    project: Leela

  daily_plan_ref:
    next_day_plan_id: next_day_plan_2026_06_18_bootstrap_contract_only
    next_day_plan_path_or_slot: "plans/daily/bootstrap.md"

  sprint_prompt_sequences: []

  routing_usage_summary:
    routing_source_status: routing_recommendation_missing
    route_mode: degraded_provider_unspecified
    primary_surface_class: provider_unspecified
    planned_usage_budget_ref: unknown
    usage_tracking_tags_ref: unknown
    operator_review_needed: true

  workflow_alignment_summary:
    alignment_source_status: missing
    prompt_process_alignment_status: unknown
    workflow_stage_coverage: []
    process_stage_coverage: []
    expected_output_coverage: []
    red_flags:
      - Missing workflow-process validation context.
      - Missing prompt-engineering dependency.
      - Missing routing recommendation.

  light_capture_hints:
    capture_home: raw_flow_dump
    capture_required_after_execution: true
    capture_fields:
      - what_was_done
      - prompt_results
      - blockers
      - next_step_guess

  FlowRecap_preparation:
    FlowRecap_handoff_role: prepare_prompt_execution_context_only
    expected_usage_capture: true
    expected_prompt_result_feedback: true
    raw_flow_dump_connection: use_flow_packet_raw_flow_dump_template

  dependency_status:
    prompt_engineering_status: missing_use_degraded_generic_prompt_mode
    ai_routing_status: missing_use_provider_unspecified
    workflow_process_status: unknown
    missing_dependency_notes:
      - "Prompt-engineering package context unavailable."
      - "Routing recommendation unavailable."
      - "Workflow-process validation unavailable."

  operator_review_flags:
    - degraded_generic_prompt_mode
    - provider_unspecified
    - prompt_pack_requires_review_before_execution

  validation_status: low_confidence_auto_generated
```

---

## Calendar Write Request Summary

```yaml
calendar_event_write_request_summary_contract_only:
  request_status: review_ready
  write_mode: review_only
  request_scope: workflow_blocks_only
  calendar_context_status: unavailable
  approval_required_for_actual_write: true
  approval_status: pending_operator_approval
  workflow_blocks: []
  note: "No calendar write has been performed."
```

---

## Operator Review Flags

```yaml
operator_review_required_before_execution:
  review_required: true
  flags:
    - missing_operator_day_intent
    - missing_project_status_context
    - missing_weekly_plan
    - missing_calendar_context
    - missing_AI_surface_inventory
    - missing_model_usage_summary
    - bootstrap_mode_used
    - flow_goal_unclear
    - prompt_pack_low_confidence
    - calendar_write_requires_acceptance
  operator_actions:
    - supply_missing_input
    - approve
    - edit
    - accept_calendar_write_request
    - execute_flow
    - run_FlowRecap_after_execution
```