---
name: flow-recap
description: Use this skill when converting one completed, partial, skipped, or blocked flow plus its normalized raw flow dump into a compact operator-reviewable FlowRecap packet with candidate-only project status and model usage deltas.
---

# FlowRecap

## Skill Contract

```yaml
skill_contract:
  package: flow-recap
  primary_artifact: flow_recap_packet
  input_contract:
    required:
      - source_flow_packet_ref
      - normalized_raw_flow_dump_ref
    optional:
      - flow_prompt_pack_ref
      - evidence_artifact_refs
      - model_usage_notes
      - skipped_flow_marker_ref
      - apex_orchestration_state_packet_ref
  output_contract:
    required:
      - flow_recap_packet
      - candidate_project_status_delta
      - model_usage_delta_candidate
      - next_step_proposal
      - operator_review_flags
  boundaries:
    owns:
      - recap_summary
      - evidence_ref_summary
      - candidate_project_status_delta
      - model_usage_delta_candidate
      - next_step_proposal
      - unresolved_questions
      - operator_validation_gate_for_recap
    must_not_own:
      - normalized_raw_flow_dump_schema
      - flow_packet_schema
      - flow_prompt_pack_schema
      - prompt_packet_schema
      - accepted_project_status_update
      - project_kb_durable_schema
      - model_usage_delta_final_schema
      - usage_summary_schema
      - status_merge_packet_schema
      - updated_all_project_status_packet
      - next_PreCapNextDay_input_context
      - runtime_execution
  global_rules:
    one_flow_recap_packet_per_flow: true
    candidate_deltas_not_accepted_state: true
    model_usage_candidate_not_final_usage_log: true
    no_project_kb_write: true
    no_status_merge_execution: true
    no_project_work_execution: true
    no_runtime_or_scheduler: true
    no_calendar_event_write: true
```

Use this skill only after a flow packet and normalized raw flow dump exist or are supplied by the operator. If evidence is incomplete, produce a low-confidence or blocked recap rather than inventing missing execution evidence.

## Supporting Files

```yaml
supporting_files:
  - path: .claude/skills/flow-recap/package-manifest.md
    read_when:
      - validating_package_structure
      - checking_file_roles
      - auditing_boundaries

  - path: .claude/skills/flow-recap/references/flow-recap-packet-contract.md
    read_when:
      - creating_flow_recap_packet
      - validating_required_fields
      - checking_candidate_delta_or_usage_boundary

  - path: .claude/skills/flow-recap/references/project-status-delta-contract.md
    read_when:
      - creating_candidate_project_status_delta
      - validating_delta_type
      - checking_status_merge_or_project_kb_boundary

  - path: .claude/skills/flow-recap/templates/flow-recap-packet-template.md
    read_when:
      - drafting_operator_facing_output
      - avoiding_schema_heavy_presentation
      - preparing_reviewable_packet

  - path: .claude/skills/flow-recap/examples/apex-minimal-flow-recap-example.md
    read_when:
      - examples_needed
      - manual_validation
      - checking_negative_outputs
```

## Procedure

```yaml
procedure:
  - step: 1
    name: validate_minimum_inputs
    actions:
      - confirm_source_flow_packet_ref_is_present
      - confirm_normalized_raw_flow_dump_ref_is_present
      - identify_completion_state_if_available
    fallback: mark_recap_status_blocked_by_missing_evidence_if_minimum_inputs_are_absent

  - step: 2
    name: load_contracts_as_needed
    actions:
      - read_flow_recap_packet_contract_when_schema_validation_is_needed
      - read_project_status_delta_contract_when_candidate_delta_is_needed
      - read_template_when_operator_facing_output_is_requested
    fallback: keep_output_minimal_and_mark_validation_status_operator_review_recommended

  - step: 3
    name: summarize_evidence
    actions:
      - extract_only_evidence_supported_facts
      - separate_completed_work_from_unfinished_or_out_of_scope_work
      - record_evidence_gaps_conflicts_or_missing_sources
    fallback: lower_confidence_and_add_operator_review_flag

  - step: 4
    name: create_flow_recap_packet
    actions:
      - populate_required_flow_recap_packet_fields
      - summarize_outputs_created_or_changed
      - summarize_decisions_blockers_failures_and_open_questions
      - assign_recap_status_and_validation_status
    fallback: use_low_confidence_or_blocked_status_instead_of_inventing_content

  - step: 5
    name: create_candidate_project_status_delta
    actions:
      - choose_delta_type_from_allowed_values
      - bind_delta_to_evidence_refs
      - keep_delta_candidate_only
      - require_operator_validation_by_default
    fallback: emit_no_state_change_or_low_confidence_delta_when_state_change_is_not_supported

  - step: 6
    name: create_model_usage_delta_candidate
    actions:
      - capture_model_usage_notes_only_when_evidenced
      - mark_finalization_owner_as_model_usage_log
      - keep_usage_delta_candidate_not_final
    fallback: mark_usage_confidence_low_and_list_unknown_usage_details

  - step: 7
    name: add_next_step_and_review_flags
    actions:
      - propose_one_next_step_without_creating_next_day_plan
      - add_operator_review_flags_for_candidate_state_usage_and_evidence_issues
      - verify_negative_output_check
    fallback: require_operator_validation_before_downstream_use
```

## Failure Modes

```yaml
failure_modes:
  - trigger: missing_source_flow_packet_ref
    correction: stop_or_emit_blocked_recap_with_missing_input_flag

  - trigger: missing_normalized_raw_flow_dump_ref
    correction: stop_or_emit_blocked_recap_with_missing_input_flag

  - trigger: evidence_is_partial_or_conflicting
    correction: lower_confidence_and_add_operator_review_flag

  - trigger: candidate_delta_would_be_treated_as_accepted_state
    correction: rewrite_as_candidate_only_and_route_to_status_merge_or_project_kb_acceptance

  - trigger: output_attempts_project_kb_write_or_status_merge
    correction: remove_mutation_claim_and_emit_candidate_handoff_only

  - trigger: output_attempts_final_model_usage_log
    correction: convert_to_model_usage_delta_candidate_with_model_usage_log_as_finalization_owner

  - trigger: next_step_becomes_next_day_plan_or_calendar_block
    correction: reduce_to_non_scheduled_next_step_proposal

  - trigger: runtime_scheduler_or_agent_behavior_is_requested
    correction: refuse_runtime_construction_and keep_interface_output_only
```

## Output Requirements

```yaml
output_requirements:
  required_sections:
    - recap_header
    - what_happened
    - evidence_summary
    - outputs_created_or_changed
    - decisions_made
    - blockers_failures_and_open_questions
    - candidate_project_status_delta
    - model_usage_delta_candidate
    - next_step_proposal
    - operator_review_flags
    - completion_gate
  required_markers:
    candidate_project_status_delta_marked_candidate_only: true
    model_usage_delta_candidate_marked_not_final: true
    next_step_proposal_marked_not_next_day_plan: true
  forbidden_outputs:
    accepted_project_status_update: false
    updated_all_project_status_packet: false
    project_kb_write: false
    final_model_usage_log: false
    next_PreCapNextDay_input_context: false
    calendar_event: false
    runtime_or_scheduler: false
```

## Completion Gate

```yaml
completion_gate:
  source_flow_packet_ref_present: true
  normalized_raw_flow_dump_ref_present: true
  evidence_summary_present: true
  work_completed_summary_present: true
  outputs_created_or_changed_listed: true
  candidate_project_status_delta_present_or_no_state_change: true
  candidate_project_status_delta_marked_candidate_only: true
  model_usage_delta_candidate_present: true
  model_usage_delta_candidate_marked_not_final: true
  next_step_proposal_present: true
  next_step_proposal_is_not_next_day_plan: true
  operator_review_flags_present: true
  no_project_kb_write_or_status_merge_claimed: true
  no_updated_all_project_status_packet_created: true
  no_runtime_scheduler_or_calendar_write_created: true
```
