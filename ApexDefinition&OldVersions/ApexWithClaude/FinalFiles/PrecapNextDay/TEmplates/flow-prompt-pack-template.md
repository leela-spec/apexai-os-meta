# Flow Prompt Pack — {{flow_id}} {{project}} — {{execution_day}}

```yaml
flow_prompt_pack:
  pack_id: flow_prompt_pack_{{execution_day}}_{{flow_id}}
  artifact_name: flow_prompt_pack
  created_or_updated_at: {{created_or_updated_at}}
  execution_day: {{execution_day}}
  flow_id: {{flow_id}}
  project: {{project}}
  generation_mode: {{full_context_mode|standard_mode|recap_recovery_mode|bootstrap_mode|calendar_constrained_mode|prompt_heavy_mode|degraded_generic_prompt_mode}}
  pack_status: {{ready_for_operator_review|operator_approved|operator_review_recommended|auto_generated|low_confidence_auto_generated|blocked_by_missing_operator_decision}}

  prompt_pack_policy:
    storage_policy:
      one_file_per_flow_prompt_pack: true
      embedded_in_daily_plan: false
      referenced_from_flow_packet: true
    prompt_system_policy:
      one_primary_prompt_system_only: true
      alternatives_allowed_by_default: false
      follow_up_prompts_allowed: true
      max_follow_up_prompts_per_sprint: {{0-6}}
    prompt_capture_policy:
      light_capture_hints_allowed: true
      mandatory_machine_readable_capture_block_inside_every_prompt: false
      canonical_capture_home: raw_flow_dump
    provider_rationale_policy:
      provider_rationale_required: true
      prompt_design_rationale_required: true
      rationale_source: {{prompt_packet_reference|routing_recommendation_reference|degraded_generic_prompt_mode_note}}
    fallback_policy:
      fallback_notes_allowed: true
      fallback_prompt_system_allowed_by_default: false
      fallback_requires_operator_review: true

  source_flow_packet_ref:
    flow_packet_id: flow_packet_{{execution_day}}_{{flow_id}}
    flow_packet_path_or_slot: "../flows/{{flow_id}}-flow-packet.md"
    flow_id: {{flow_id}}
    project: {{project}}

  daily_plan_ref:
    next_day_plan_id: {{plan_id}}
    next_day_plan_path_or_slot: "../next-day-plan.md"

  sprint_prompt_sequences:
    - sprint_id: S1
      sprint_role: first_work_sprint
      sprint_status: {{active|compressed|skipped|blocked|operator_review_needed}}
      expected_output_type_ref:
        expected_output_type: {{expected_output_type}}
        expected_output_contract_ref: workflow-process-design/references/expected-output-type-contract.md
      workflow_stage_ref:
        workflow_stage: {{workflow_stage_or_unknown}}
        taxonomy_ref: workflow-process-design/references/workflow-stage-taxonomy.md
      process_stage_ref:
        process_stage: {{process_stage_or_unknown}}
        taxonomy_ref: workflow-process-design/references/process-stage-taxonomy.md
      start_prompt_ref:
        prompt_packet_id: {{prompt_packet_id_or_placeholder}}
        packet_role: start_prompt
        prompt_task_type: {{planning|synthesis|validation|workflow_extraction|workflow_normalization|operator_defined}}
        provider_target: {{ChatGPT|Claude|Gemini|OpenRouter_later|provider_unspecified}}
        prompt_packet_path_or_slot: {{prompt_packet_ref_or_inline_slot}}
      follow_up_prompt_refs: []
      prompt_packet_refs:
        - prompt_packet_id: {{prompt_packet_id_or_placeholder}}
          packet_role: start_prompt
          prompt_task_type: {{prompt_task_type}}
          provider_target: {{provider_target}}
          prompt_packet_path_or_slot: {{prompt_packet_ref_or_inline_slot}}
      placement_rules_applied:
        - one_start_prompt_per_active_sprint
        - start_prompt_first
        - group_by_sprint
        - preserve_sprint_role
      operator_review_flags: []
      validation_status: {{validation_status}}

  routing_usage_summary:
    routing_source_status: {{routing_recommendation_available|routing_recommendation_partial|routing_recommendation_missing|operator_override}}
    route_mode: {{planned_flow_session|supplemental_or_batch_execution|degraded_provider_unspecified|operator_override}}
    primary_surface_class: {{subscription_frontier_chat|subscription_frontier_reasoning|deep_research_surface|agent_run_surface|code_agent_surface|long_context_surface|supplemental_api_low_cost|provider_unspecified}}
    routing_recommendation_packet_ref: "{{optional}}"
    planned_usage_budget_ref: "../usage/usage-tracking-summary.md"
    usage_tracking_tags_ref: "../usage/usage-tracking-summary.md#usage-tags"
    quota_or_scarcity_note: "{{abstract scarcity note only unless verified}}"
    operator_review_needed: {{true|false}}

  workflow_alignment_summary:
    alignment_source_status: {{validated|valid_with_warnings|partially_validated|missing_validation|operator_review_recommended}}
    prompt_process_alignment_status: {{aligned|aligned_with_warnings|mismatched|incomplete|unknown}}
    workflow_stage_coverage: []
    process_stage_coverage: []
    expected_output_coverage: []
    alignment_validation_ref: "{{optional}}"
    red_flags: []

  light_capture_hints:
    capture_policy: defer_to_raw_flow_dump
    suggested_operator_notes:
      - "Save the prompt result link or short result summary."
      - "Record whether the output changed the next action."
    forbidden_capture_requirements:
      - mandatory_machine_readable_capture_block_inside_every_prompt
      - prompt_embedded_full_recap_schema
      - prompt_embedded_status_merge_schema

  FlowRecap_preparation:
    FlowRecap_handoff_role: prepare_prompt_execution_context_only
    expected_usage_capture: true
    expected_prompt_result_feedback: true
    raw_flow_dump_connection: use_flow_packet_raw_flow_dump_template
    suggested_recap_fields:
      - prompt_results
      - model_usage_notes
      - result_quality_signal

  dependency_status:
    prompt_engineering_status: {{available|partially_available|missing_use_degraded_generic_prompt_mode|unknown}}
    ai_routing_status: {{available|partially_available|missing_use_provider_unspecified|unknown}}
    workflow_process_status: {{available|partially_available|missing_use_operator_review_recommended|unknown}}
    missing_dependency_notes: []

  operator_review_flags: []
  validation_status: {{validation_status}}
```

## Copy-paste prompt slots

> Keep final prompts here only when the prompt-engineering dependency has produced or approved them. Otherwise reference prompt packets instead of inventing prompt doctrine.

### S1 start prompt

```text
{{copy_paste_prompt_or_prompt_packet_reference}}
```

### S2 start prompt

```text
{{copy_paste_prompt_or_prompt_packet_reference}}
```

### S3 recap-prep prompt

```text
{{copy_paste_prompt_or_prompt_packet_reference}}
```
