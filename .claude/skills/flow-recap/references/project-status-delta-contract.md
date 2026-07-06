# Project Status Delta Contract

## Contract Role

```yaml
project_status_delta_contract:
  artifact_name: candidate_project_status_delta
  file_role: flow_recap_reference_contract
  package: flow-recap
  purpose: >
    Define the minimal candidate-only project status delta created by FlowRecap
    from one flow recap packet. This contract allows FlowRecap to propose
    project-state changes without accepting, merging, writing, or overwriting
    durable project state.

  ownership:
    owns:
      - candidate_project_status_delta
      - candidate_delta_confidence
      - candidate_delta_evidence_refs
      - candidate_delta_operator_validation_gate
    must_not_own:
      - accepted_project_status_update
      - current_project_status_overview
      - project_kb_durable_schema
      - apex_orchestration_state_packet
      - status_merge_packet_schema
      - updated_all_project_status_packet
      - next_PreCapNextDay_input_context
      - model_usage_delta_schema
      - runtime_execution

  upstream_inputs:
    required:
      - flow_recap_packet_ref
      - evidence_refs
    optional:
      - source_flow_packet_ref
      - normalized_raw_flow_dump_ref
      - apex_orchestration_state_packet_ref
      - current_project_status_overview_ref

  downstream_consumers:
    primary:
      - operator_review
      - status-merge
    secondary:
      - project-kb-manager
      - ProjectStatus
      - PreCapNextDay

  global_rules:
    candidate_only_until_status_merge_or_project_kb_acceptance: true
    evidence_refs_required_for_non_no_state_change_delta: true
    operator_validation_required_by_default: true
    no_project_kb_write: true
    no_current_project_status_overview_update: true
    no_status_merge_execution: true
    no_next_day_plan_creation: true
    no_runtime_execution: true
```

## Boundary Summary

FlowRecap may infer that one flow probably changed project state, but it must keep that inference as a candidate until a later operator-gated status merge or project KB acceptance step validates it.

```yaml
boundary_summary:
  candidate_delta_is_allowed: true
  accepted_delta_is_forbidden: true
  durable_state_mutation_is_forbidden: true
  merge_execution_is_forbidden: true
  validation_owner:
    - operator_review
    - status-merge
    - project-kb-manager_when_explicitly_accepting_update
```

## Schema: candidate_project_status_delta

```yaml
candidate_project_status_delta:
  type: object
  role: candidate_only_until_status_merge_or_project_kb_acceptance
  required:
    - delta_id
    - target_project
    - delta_type
    - proposed_change_summary
    - evidence_refs
    - confidence
    - requires_operator_validation

  fields:
    delta_id:
      type: string
      format: candidate_project_status_delta_<YYYY_MM_DD>_<flow_id>_<short_slug>
      required: true

    target_project:
      type: string
      required: true
      note: Use the source flow or state packet project label when supplied. Use unknown only when evidence is ambiguous.

    target_scope:
      type: string
      required: false
      note: Optional workstream, task, artifact, blocker, or decision scope within the target project.

    delta_type:
      type: string
      allowed:
        - task_progress
        - new_task_candidate
        - blocker_added
        - blocker_removed
        - decision_added
        - artifact_created
        - artifact_updated
        - priority_signal_changed
        - no_state_change
      required: true

    proposed_change_summary:
      type: string
      required: true
      note: One compact sentence describing what should change if later accepted.

    evidence_refs:
      type: list
      item_ref: evidence_ref
      min_items: 1
      required: true
      note: Required for every delta_type except no_state_change. For no_state_change, include the evidence that supports no durable update.

    confidence:
      type: string
      allowed:
        - high
        - medium
        - low
        - unknown
      required: true

    requires_operator_validation:
      type: boolean
      required: true
      default: true

    validation_reason:
      type: string
      required: false
      note: Explain why operator validation is required or why confidence is low.

    suggested_acceptance_route:
      type: string
      required: false
      allowed:
        - status_merge
        - project_kb_manager_update_mode
        - ProjectStatus_review
        - no_action
        - operator_decision_needed
        - unknown

    affected_artifacts:
      type: list
      item_ref: artifact_ref
      required: false

    related_blockers_or_questions:
      type: list
      item_ref: blocker_or_question_ref
      required: false
```

## Delta Type Selection Rules

```yaml
delta_type_selection_rules:
  task_progress:
    use_when:
      - evidence_shows_existing_task_advanced
      - output_or_decision_reduces_remaining_work
    must_include:
      - progress_summary
      - evidence_refs

  new_task_candidate:
    use_when:
      - evidence_reveals_new_followup_work
      - followup_is_not_yet_confirmed_as_existing_task
    must_include:
      - proposed_change_summary
      - requires_operator_validation

  blocker_added:
    use_when:
      - evidence_shows_new_issue_prevents_or_risks_progress
    must_include:
      - blocker_summary
      - evidence_refs

  blocker_removed:
    use_when:
      - evidence_shows_previous_blocker_is_resolved_or_no_longer_relevant
    must_include:
      - removed_blocker_summary
      - evidence_refs

  decision_added:
    use_when:
      - evidence_contains_a_new_decision_or_operator_choice
    must_include:
      - decision_summary
      - evidence_refs

  artifact_created:
    use_when:
      - evidence_shows_a_new_file_document_template_contract_or_output_exists
    must_include:
      - artifact_ref_or_label
      - evidence_refs

  artifact_updated:
    use_when:
      - evidence_shows_existing_artifact_was_changed_or_refined
    must_include:
      - artifact_ref_or_label
      - evidence_refs

  priority_signal_changed:
    use_when:
      - evidence_changes_likely_next_focus_or_urgency
      - change_is_not_already_an_accepted_project_status_update
    must_include:
      - old_signal_if_known
      - new_candidate_signal
      - evidence_refs

  no_state_change:
    use_when:
      - flow_was_skipped_without_project_state_effect
      - evidence_is_insufficient_for_a_candidate_change
      - work_was_exploratory_and_no_durable_update_is_supported
    must_include:
      - proposed_change_summary
      - evidence_refs_or_gap_reason
```

## Evidence Reference Sketch

```yaml
evidence_ref:
  type: object
  required:
    - ref_type
    - ref_label
    - evidence_role
  fields:
    ref_type:
      type: string
      allowed:
        - normalized_raw_flow_dump
        - flow_packet
        - flow_prompt_pack
        - artifact_path
        - chat_excerpt
        - operator_note
        - skipped_flow_marker
        - unknown
    ref_label:
      type: string
      required: true
    evidence_role:
      type: string
      allowed:
        - supports_delta
        - supports_no_state_change
        - supports_low_confidence
        - identifies_gap
        - conflicts_with_delta
    confidence_note:
      type: string
      required: false
```

## Validation Rules

```yaml
candidate_project_status_delta_validation_rules:
  required_identity:
    delta_id_present: true
    target_project_present_or_unknown_with_review_flag: true
    delta_type_allowed_value: true

  evidence_requirements:
    evidence_refs_required: true
    unsupported_delta_must_be_low_confidence_or_no_state_change: true
    conflicting_evidence_requires_operator_validation: true

  candidate_boundary:
    must_remain_candidate_only: true
    must_not_claim_project_status_updated: true
    must_not_write_project_kb_record: true
    must_not_create_updated_all_project_status_packet: true
    must_not_create_next_PreCapNextDay_input_context: true

  operator_validation:
    requires_operator_validation_defaults_true: true
    high_impact_changes_require_validation: true
    low_confidence_changes_require_validation: true

  valid_no_state_change:
    allowed: true
    requires_summary: true
    should_not_emit_fake_progress: true
```

## Minimal Examples

```yaml
minimal_examples:
  task_progress:
    delta_id: candidate_project_status_delta_2026_07_06_F3_contract
    target_project: APEX
    delta_type: task_progress
    proposed_change_summary: FlowRecap packet contract was drafted and is ready for operator review.
    evidence_refs:
      - ref_type: artifact_path
        ref_label: .claude/skills/flow-recap/references/flow-recap-packet-contract.md
        evidence_role: supports_delta
    confidence: high
    requires_operator_validation: true

  no_state_change:
    delta_id: candidate_project_status_delta_2026_07_06_F4_none
    target_project: APEX
    delta_type: no_state_change
    proposed_change_summary: No durable project status change is supported by the supplied evidence.
    evidence_refs:
      - ref_type: normalized_raw_flow_dump
        ref_label: raw_flow_dump_2026_07_06_F4_placeholder
        evidence_role: supports_no_state_change
    confidence: medium
    requires_operator_validation: true
```
