# Flow Packet — {{flow_id}} {{project}} — {{execution_day}}

```yaml
flow_packet:
  packet_id: flow_packet_{{execution_day}}_{{flow_id}}
  artifact_name: flow_packet
  created_or_updated_at: {{created_or_updated_at}}
  execution_day: {{execution_day}}
  generation_mode: {{generation_mode}}
  review_status: {{review_status}}

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
    flow_id: {{F1|F2|F3|F4}}
    flow_slot: {{F1|F2|F3|F4}}
    project: {{Leela|MasterOfArts|Apex|Residual|Investment|Others|operator_defined}}
    flow_role: {{flow_role}}
    flow_status: {{planned|compressed|omitted|skipped|blocked|placeholder}}
    default_flow: {{true|false}}
    override_reason: "{{optional}}"
    omission_reason: "{{optional}}"
    compression_reason: "{{optional}}"
    blocker_summary: "{{optional}}"

  flow_context_summary:
    operator_intent_summary: "{{operator intent for this flow}}"
    project_state_summary: "{{known state or missing-context statement}}"
    recap_carry_forward: []
    weekly_plan_alignment: {{aligned|partially_aligned|not_available|conflict_detected|operator_override}}
    calendar_constraints_summary: "{{optional}}"
    source_context_refs:
      - {{source_ref}}
    constraints: []
    assumptions: []
    unresolved_inputs: []
    confidence_notes: []

  workflow_process_labels:
    workflow_stage: {{workflow_stage_or_unknown}}
    process_stage: {{process_stage_or_unknown}}
    expected_output_type: {{expected_output_type_or_unknown}}
    validation_source: {{workflow-process-design|inferred_from_context|operator_supplied|not_available}}
    fit_status: {{valid|valid_with_warnings|operator_review_recommended|low_confidence_auto_generated|blocked_by_missing_operator_decision}}
    mismatch_flags: []
    operator_review_note: "{{optional}}"

  flow_sprint_plan:
    sprint_policy: {{default_three_sprints|compressed_single_sprint|compressed_two_sprints|omitted|skipped|operator_defined}}
    sprint_count: {{0-3}}
    recap_digest_required: {{true|false}}
    sprint_sequence_notes: []
    compression_handling:
      compression_status: {{not_compressed|compressed_single_sprint|compressed_two_sprints|omitted|skipped}}
      reason: "{{reason}}"
      preserved_sprint_roles: []
      dropped_or_merged_elements: []
      operator_review_needed: {{true|false}}
    sprints:
      - sprint_id: S1
        sprint_role: first_work_sprint
        sprint_goal: "{{sprint_goal}}"
        expected_output_type: "{{expected_output_type}}"
        success_criteria: []
        prompt_sequence_ref: "../prompts/{{flow_id}}-flow-prompt-pack.md#S1"
        capture_focus:
          - artifact_created
          - decision_made
          - unresolved_question
        completion_marker: not_started
        validation_status: {{validation_status}}
        operator_review_flags: []

      - sprint_id: S2
        sprint_role: second_work_or_deepening_sprint
        sprint_goal: "{{sprint_goal}}"
        expected_output_type: "{{expected_output_type}}"
        success_criteria: []
        prompt_sequence_ref: "../prompts/{{flow_id}}-flow-prompt-pack.md#S2"
        capture_focus:
          - artifact_created
          - blocker_found
          - next_step_guess
        completion_marker: not_started
        validation_status: {{validation_status}}
        operator_review_flags: []

      - sprint_id: S3
        sprint_role: recap_digest_preparation_sprint
        sprint_goal: "Prepare capture context for later FlowRecap without running FlowRecap."
        expected_output_type: recap_handoff_notes
        success_criteria: []
        prompt_sequence_ref: "../prompts/{{flow_id}}-flow-prompt-pack.md#S3"
        capture_focus:
          - source_context_used
          - prompt_result
          - next_step_guess
        completion_marker: not_started
        validation_status: {{validation_status}}
        operator_review_flags: []

  prompt_pack_ref:
    flow_prompt_pack_path: "../prompts/{{flow_id}}-flow-prompt-pack.md"
    prompt_pack_status: {{required|generated|generic_degraded_mode|unavailable|not_needed_for_skipped_flow}}
    prompt_pack_authority: references/flow-prompt-pack-contract.md
    prompt_engineering_dependency_status: {{available|missing_use_degraded_generic_prompt_mode|operator_supplied_prompt|not_needed_for_skipped_flow}}
    note: "{{optional}}"

  usage_tracking_refs:
    planned_usage_budget_ref: "../usage/usage-tracking-summary.md"
    routing_recommendation_ref: "{{optional}}"
    usage_tracking_status: {{planned|degraded_missing_usage_context|not_needed_for_skipped_flow|operator_review_recommended}}
    expected_usage_capture_fields:
      - provider_used
      - surface_class_used
      - prompt_count
      - result_quality_signal
    note: "{{optional}}"

  workflow_block_ref:
    workflow_block_status: {{workflow_block_requested|workflow_block_not_requested|calendar_unavailable|operator_acceptance_required}}
    calendar_event_write_request_ref: "../calendar/calendar-event-write-request.md"
    note: "{{optional}}"

  flow_execution_capture_preparation:
    raw_flow_dump_template:
      template_id: raw_flow_dump_template_{{execution_day}}_{{flow_id}}
      flow_id: {{flow_id}}
      execution_day: {{execution_day}}
      completion_marker: not_started
      operator_raw_notes: ""
      prompt_results: []
      artifacts_created: []
      decisions_made: []
      blockers: []
      model_usage_notes: []
      next_step_guess: ""
      recap_request: operator_review_first
    skipped_flow_marker_template:
      marker_id: skipped_flow_marker_{{execution_day}}_{{flow_id}}
      flow_id: {{flow_id}}
      execution_day: {{execution_day}}
      skip_status: planned_skip
      skip_reason: ""
      carry_forward_policy: operator_decides_later
      next_review_point: next_PreCapNextDay
      operator_note: ""
    capture_instructions:
      - "Fill raw_flow_dump_template only after operator execution."
      - "Do not run FlowRecap inside PreCapNextDay."
    capture_status: prepared

  FlowRecap_handoff_block:
    handoff_id: FlowRecap_handoff_{{execution_day}}_{{flow_id}}
    flow_packet_ref: "./{{flow_id}}-flow-packet.md"
    raw_flow_dump_expected: true
    skipped_flow_marker_allowed: true
    context_to_pass:
      - flow_identity
      - flow_sprint_plan
      - prompt_pack_ref
      - usage_tracking_refs
      - operator_review_flags
    required_operator_completion_marker: {{done|partial|skipped|blocked|not_started}}
    FlowRecap_ready_status: operator_review_first
    boundary_note: "PreCapNextDay prepares handoff only; FlowRecap is not run here."

  operator_review_flags: []
  validation_status: {{validation_status}}
```
