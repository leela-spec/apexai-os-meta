# FILE: .claude/skills/workflow-process-design/references/workflow-record-contract.md

# Workflow Record Contract

```yaml
workflow_record_contract:
  artifact_name: workflow_record_contract
  file_role: workflow_process_design_reference_contract
  purpose: >
    Define the reusable workflow_record schema used by workflow-process-design
    to preserve normalized workflows, workflow/process labels, expected-output
    references, gates, transitions, review flags, and downstream handoff needs.
    This file records reusable workflow structure. It does not own workflow
    stage taxonomy, process stage taxonomy, expected output taxonomy, prompt
    packet schema, routing logic, usage tracking, daily plans, flow packets, or
    project status schemas.

  ownership:
    owns:
      - workflow_record_schema
      - workflow_identity_fields
      - workflow_scope_fields
      - workflow_input_fields
      - workflow_output_fields
      - workflow_gate_fields
      - workflow_transition_fields
      - workflow_process_label_references
      - expected_output_references
      - operator_review_and_conflict_fields
      - downstream_consumer_fields
      - reusable_workflow_normalization_fields
      - workflow_record_examples
    must_not_own:
      - workflow_stage_taxonomy
      - process_stage_taxonomy
      - expected_output_type_taxonomy
      - prompt_packet_schema
      - prompt_sequence_schema
      - provider_specific_prompt_rules
      - routing_decision_schema
      - planned_usage_budget_schema
      - monthly_quota_map_schema
      - usage_delta_schema
      - daily_plan_schema
      - flow_packet_schema
      - project_status_schema

  global_rules:
    workflow_record_is_reusable_process_memory: true
    labels_reference_taxonomies_without_redefining_them: true
    expected_outputs_reference_expected_output_contract_without_redefining_it: true
    preserve_operator_intent_and_scope: true
    normalize_messy_workflow_notes_without_silent_decision_changes: true
    operator_review_required_when_conflicts_affect_downstream_prompt_or_plan: true
    no_provider_specific_prompt_style_inside_workflow_record: true

  validation_status_allowed:
    - valid
    - valid_with_warnings
    - operator_review_recommended
    - low_confidence_auto_generated
    - blocked_by_missing_operator_decision
```

## Schema: workflow_record

```yaml
workflow_record:
  type: object
  required:
    - record_id
    - record_role
    - workflow_name
    - workflow_summary
    - workflow_scope
    - label_references
    - expected_output_references
    - workflow_inputs
    - workflow_outputs
    - gates
    - transitions
    - downstream_consumers
    - operator_review
    - validation_status

  fields:
    record_id:
      type: string
      format: "workflow_record_<short_slug>"
      required: true

    record_role:
      type: string
      allowed:
        - reusable_workflow_definition
        - one_off_workflow_capture
        - workflow_normalization_result
        - workflow_repair_record
        - prompt_alignment_source_record
      required: true

    workflow_name:
      type: string
      required: true
      rule: "Use a compact human-readable name, not an opaque ID."

    workflow_summary:
      type: string
      required: true
      rule: "Describe what the workflow enables in one or two sentences."

    workflow_scope:
      type: object_ref
      ref: workflow_scope
      required: true

    label_references:
      type: object_ref
      ref: workflow_label_references
      required: true

    expected_output_references:
      type: list
      item_ref: expected_output_reference
      min_items: 1
      required: true

    workflow_inputs:
      type: list
      item_ref: workflow_input
      min_items: 0
      required: true

    workflow_outputs:
      type: list
      item_ref: workflow_output
      min_items: 1
      required: true

    gates:
      type: list
      item_ref: workflow_gate
      min_items: 0
      required: true

    transitions:
      type: list
      item_ref: workflow_transition
      min_items: 0
      required: true

    iteration_logic:
      type: object_ref
      ref: iteration_logic
      required: false

    success_criteria:
      type: list
      item_type: string
      min_items: 1
      max_items: 10
      required: false

    risks_and_failure_modes:
      type: list
      item_ref: workflow_risk
      min_items: 0
      max_items: 8
      required: false

    conflict_fields:
      type: object_ref
      ref: workflow_conflict_fields
      required: false

    downstream_consumers:
      type: list
      item_ref: downstream_consumer
      min_items: 0
      required: true

    normalization_notes:
      type: object_ref
      ref: workflow_normalization_notes
      required: false

    operator_review:
      type: object_ref
      ref: operator_review
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

## Schema: Workflow Identity and Scope Fields

```yaml
workflow_scope:
  type: object
  required:
    - scope_id
    - scope_type
    - project_or_domain
    - reusable
    - boundary

  fields:
    scope_id:
      type: string
      format: "workflow_scope_<short_slug>"
      required: true

    scope_type:
      type: string
      allowed:
        - project_specific
        - cross_project
        - package_internal
        - operator_personal_process
        - temporary_one_off
        - unknown
      required: true

    project_or_domain:
      type: string
      required: true
      examples:
        - Leela
        - MasterOfArts
        - Apex
        - Residual
        - cross_project
        - unknown

    reusable:
      type: boolean
      required: true

    reuse_conditions:
      type: list
      item_type: string
      min_items: 0
      max_items: 8
      required: false

    boundary:
      type: object
      required:
        - includes
        - excludes
      fields:
        includes:
          type: list
          item_type: string
          min_items: 1
          required: true
        excludes:
          type: list
          item_type: string
          min_items: 0
          required: true

    source_state:
      type: string
      allowed:
        - operator_supplied
        - extracted_from_notes
        - normalized_from_existing_workflow
        - inferred_low_confidence
        - unknown
      required: false
```

## Schema: Workflow and Process Label References

```yaml
workflow_label_references:
  type: object
  required:
    - primary_workflow_stage_ref
    - primary_process_stage_ref
    - label_confidence
    - label_review_flags

  fields:
    primary_workflow_stage_ref:
      type: string
      ref: "references/workflow-stage-taxonomy.md#workflow_stage_values"
      required: true
      rule: "Reference the canonical workflow_stage value. Do not redefine the taxonomy here."

    secondary_workflow_stage_refs:
      type: list
      item_type: string
      ref: "references/workflow-stage-taxonomy.md#workflow_stage_values"
      min_items: 0
      max_items: 3
      required: false

    primary_process_stage_ref:
      type: string
      ref: "references/process-stage-taxonomy.md#process_stage_taxonomy"
      required: true
      rule: "Reference the canonical process_stage value. Do not redefine the taxonomy here."

    secondary_process_stage_refs:
      type: list
      item_type: string
      ref: "references/process-stage-taxonomy.md#process_stage_taxonomy"
      min_items: 0
      max_items: 2
      required: false

    label_confidence:
      type: integer
      min: 1
      max: 100
      required: true

    label_selection_basis:
      type: list
      item_type: string
      min_items: 1
      max_items: 8
      required: false

    label_review_flags:
      type: list
      item_type: string
      min_items: 0
      max_items: 8
      required: true
```

## Schema: Expected Output References

```yaml
expected_output_reference:
  type: object
  required:
    - expected_output_ref_id
    - expected_output_type_ref
    - role_in_workflow
    - output_required

  fields:
    expected_output_ref_id:
      type: string
      format: "expected_output_ref_<short_slug>"
      required: true

    expected_output_type_ref:
      type: string
      ref: "references/expected-output-type-contract.md#expected_output_type_taxonomy"
      required: true
      rule: "Reference the expected_output_type taxonomy. Do not duplicate its allowed values here."

    role_in_workflow:
      type: string
      allowed:
        - primary_deliverable
        - intermediate_artifact
        - validation_artifact
        - handoff_artifact
        - learning_artifact
        - operator_decision_artifact
      required: true

    output_required:
      type: boolean
      required: true

    minimum_completion_evidence:
      type: list
      item_type: string
      min_items: 0
      max_items: 10
      required: false

    fidelity_requirement:
      type: string
      allowed:
        - strict_source_fidelity
        - semantic_fidelity
        - flexible_synthesis
        - creative_generation_allowed
        - unknown
      required: false
```

## Schema: Inputs, Outputs, Gates, and Transitions

```yaml
workflow_input:
  type: object
  required:
    - input_id
    - input_name
    - input_role
    - required
    - source_status

  fields:
    input_id:
      type: string
      format: "workflow_input_<short_slug>"
      required: true
    input_name:
      type: string
      required: true
    input_role:
      type: string
      allowed:
        - operator_intent
        - source_context
        - project_context
        - workflow_context
        - flow_packet
        - sprint_goal
        - prompt_packet
        - prompt_result_feedback
        - expected_output_context
        - prior_workflow_record
        - other
      required: true
    required:
      type: boolean
      required: true
    source_status:
      type: string
      allowed:
        - supplied
        - missing
        - inferred
        - optional
        - blocked
      required: true
    missing_behavior:
      type: string
      allowed:
        - block
        - degrade_with_review_flag
        - infer_with_low_confidence
        - proceed_without_input
        - ask_operator
      required: false

workflow_output:
  type: object
  required:
    - output_id
    - output_name
    - expected_output_ref
    - consumer
    - completion_status

  fields:
    output_id:
      type: string
      format: "workflow_output_<short_slug>"
      required: true
    output_name:
      type: string
      required: true
    expected_output_ref:
      type: string
      ref: expected_output_reference
      required: true
    consumer:
      type: string
      allowed:
        - operator
        - prompt_engineering
        - ai_routing_and_usage_tracking
        - workflow_process_design
        - PreCapNextDay
        - FlowRecap
        - status_merge
        - future_skill
        - unknown
      required: true
    completion_status:
      type: string
      allowed:
        - complete
        - partial
        - draft
        - blocked
        - not_started
        - unknown
      required: true

workflow_gate:
  type: object
  required:
    - gate_id
    - gate_name
    - gate_type
    - required
    - pass_condition

  fields:
    gate_id:
      type: string
      format: "workflow_gate_<short_slug>"
      required: true
    gate_name:
      type: string
      required: true
    gate_type:
      type: string
      allowed:
        - operator_approval
        - validation_check
        - source_sufficiency_check
        - prompt_process_alignment_check
        - conflict_resolution
        - completion_check
      required: true
    required:
      type: boolean
      required: true
    pass_condition:
      type: string
      required: true
    fail_behavior:
      type: string
      allowed:
        - stop_and_request_operator_decision
        - return_for_revision
        - mark_operator_review_recommended
        - degrade_to_low_confidence
        - block_downstream_use
      required: false

workflow_transition:
  type: object
  required:
    - transition_id
    - from_step
    - to_step
    - condition

  fields:
    transition_id:
      type: string
      format: "workflow_transition_<short_slug>"
      required: true
    from_step:
      type: string
      required: true
    to_step:
      type: string
      required: true
    condition:
      type: string
      required: true
    blocked_when:
      type: list
      item_type: string
      min_items: 0
      max_items: 8
      required: false
```

## Schema: Iteration, Risk, Conflict, and Downstream Fields

```yaml
iteration_logic:
  type: object
  required:
    - iteration_required
    - iteration_pattern

  fields:
    iteration_required:
      type: boolean
      required: true
    iteration_pattern:
      type: string
      allowed:
        - none
        - draft_review_revise
        - extract_normalize_validate
        - generate_critique_revise
        - research_synthesize_decide
        - plan_execute_recap
        - operator_defined
        - unknown
      required: true
    max_iterations:
      type: integer
      min: 0
      max: 6
      required: false
    stop_conditions:
      type: list
      item_type: string
      min_items: 0
      max_items: 8
      required: false

workflow_risk:
  type: object
  required:
    - risk_id
    - risk_name
    - risk_level
    - mitigation

  fields:
    risk_id:
      type: string
      format: "workflow_risk_<short_slug>"
      required: true
    risk_name:
      type: string
      required: true
    risk_level:
      type: string
      allowed:
        - low
        - medium
        - high
        - blocking
        - unknown
      required: true
    mitigation:
      type: string
      required: true

workflow_conflict_fields:
  type: object
  required:
    - conflicts_present
    - conflict_items
    - resolution_authority_order

  fields:
    conflicts_present:
      type: boolean
      required: true
    conflict_items:
      type: list
      item_ref: workflow_conflict_item
      min_items: 0
      max_items: 8
      required: true
    resolution_authority_order:
      type: list
      item_type: string
      required: true
      fixed_value:
        - operator_decision_from_tradeoff_card
        - workflow_process_fit
        - prompt_quality
        - ai_routing_cost_or_efficiency

workflow_conflict_item:
  type: object
  required:
    - conflict_id
    - conflict_type
    - description
    - recommended_resolution_mode

  fields:
    conflict_id:
      type: string
      format: "workflow_conflict_<short_slug>"
      required: true
    conflict_type:
      type: string
      allowed:
        - workflow_stage_conflict
        - process_stage_conflict
        - expected_output_conflict
        - prompt_process_alignment_conflict
        - routing_workflow_fit_conflict
        - operator_intent_conflict
        - source_fidelity_conflict
        - unknown
      required: true
    description:
      type: string
      required: true
    recommended_resolution_mode:
      type: string
      allowed:
        - operator_tradeoff_card
        - revise_prompt
        - revise_workflow_record
        - change_expected_output_type
        - block_downstream_use
        - accept_with_warning
      required: true

downstream_consumer:
  type: object
  required:
    - consumer_name
    - consumer_role
    - handoff_fields

  fields:
    consumer_name:
      type: string
      allowed:
        - prompt_engineering
        - ai_routing_and_usage_tracking
        - PreCapNextDay
        - FlowRecap
        - status_merge
        - operator
        - future_skill
        - unknown
      required: true
    consumer_role:
      type: string
      required: true
    handoff_fields:
      type: list
      item_type: string
      min_items: 1
      max_items: 12
      required: true
    handoff_readiness:
      type: string
      allowed:
        - ready
        - ready_with_warnings
        - operator_review_needed
        - blocked
        - unknown
      required: false
```

## Schema: Normalization and Operator Review Fields

```yaml
workflow_normalization_notes:
  type: object
  required:
    - source_shape
    - normalization_actions
    - semantic_preservation_status

  fields:
    source_shape:
      type: string
      allowed:
        - raw_notes
        - existing_workflow
        - prompt_result_feedback
        - operator_description
        - mixed_sources
        - inferred
        - unknown
      required: true
    normalization_actions:
      type: list
      item_type: string
      min_items: 0
      max_items: 10
      required: true
    semantic_preservation_status:
      type: string
      allowed:
        - preserved
        - preserved_with_warnings
        - low_confidence
        - not_applicable
      required: true
    dropped_or_compressed_material:
      type: list
      item_type: string
      min_items: 0
      max_items: 10
      required: false
    unresolved_questions:
      type: list
      item_type: string
      min_items: 0
      max_items: 10
      required: false

operator_review:
  type: object
  required:
    - review_required
    - review_reason
    - review_flags

  fields:
    review_required:
      type: boolean
      required: true
    review_reason:
      type: string
      required: true
    review_flags:
      type: list
      item_type: string
      min_items: 0
      max_items: 12
      required: true
    safe_next_step:
      type: string
      required: false
```

## Minimal Examples

```yaml
examples:
  minimal_reusable_workflow_record:
    record_id: workflow_record_prompt_process_validation
    record_role: reusable_workflow_definition
    workflow_name: Prompt Process Validation
    workflow_summary: >
      Validate whether a prompt asks for the right workflow stage, process role,
      and expected output before it is sent to a provider-specific prompt layer.
    workflow_scope:
      scope_id: workflow_scope_prompt_validation
      scope_type: package_internal
      project_or_domain: Apex
      reusable: true
      reuse_conditions:
        - prompt_packet_exists
        - expected_output_context_exists
      boundary:
        includes:
          - workflow_stage_check
          - process_stage_check
          - expected_output_check
        excludes:
          - provider_specific_prompt_style
          - model_routing
          - final_prompt_rewrite
      source_state: normalized_from_existing_workflow
    label_references:
      primary_workflow_stage_ref: validation
      secondary_workflow_stage_refs:
        - operator_decision
      primary_process_stage_ref: validation
      secondary_process_stage_refs:
        - refinement
      label_confidence: 92
      label_selection_basis:
        - prompt_is_checked_against_output_contract
        - downstream_revision_may_be_required
      label_review_flags: []
    expected_output_references:
      - expected_output_ref_id: expected_output_ref_alignment_review
        expected_output_type_ref: critique_report
        role_in_workflow: validation_artifact
        output_required: true
        minimum_completion_evidence:
          - mismatch_checks_present
          - review_flags_present
        fidelity_requirement: semantic_fidelity
    workflow_inputs:
      - input_id: workflow_input_prompt_packet
        input_name: prompt_packet
        input_role: prompt_packet
        required: true
        source_status: supplied
        missing_behavior: block
    workflow_outputs:
      - output_id: workflow_output_alignment_review
        output_name: prompt_workflow_alignment_review
        expected_output_ref: expected_output_ref_alignment_review
        consumer: prompt_engineering
        completion_status: complete
    gates:
      - gate_id: workflow_gate_alignment_valid
        gate_name: Alignment Review Gate
        gate_type: prompt_process_alignment_check
        required: true
        pass_condition: prompt_matches_workflow_stage_process_stage_and_expected_output
        fail_behavior: return_for_revision
    transitions:
      - transition_id: workflow_transition_review_to_revision
        from_step: alignment_review
        to_step: prompt_engineering_revision
        condition: mismatch_detected
        blocked_when:
          - expected_output_missing
    iteration_logic:
      iteration_required: true
      iteration_pattern: generate_critique_revise
      max_iterations: 2
      stop_conditions:
        - validation_status_valid_or_valid_with_warnings
    success_criteria:
      - workflow_stage_is_referenced
      - process_stage_is_referenced
      - expected_output_reference_present
      - no_provider_specific_style_rewrite
    risks_and_failure_modes:
      - risk_id: workflow_risk_prompt_style_drift
        risk_name: Prompt Style Drift
        risk_level: medium
        mitigation: hand_off_to_prompt_engineering_without_rewriting_provider_style
    conflict_fields:
      conflicts_present: false
      conflict_items: []
      resolution_authority_order:
        - operator_decision_from_tradeoff_card
        - workflow_process_fit
        - prompt_quality
        - ai_routing_cost_or_efficiency
    downstream_consumers:
      - consumer_name: prompt_engineering
        consumer_role: revise_prompt_against_alignment_review
        handoff_fields:
          - workflow_stage_ref
          - process_stage_ref
          - expected_output_ref
          - review_flags
        handoff_readiness: ready
    normalization_notes:
      source_shape: operator_description
      normalization_actions:
        - separated_workflow_fit_from_prompt_style
        - added_explicit_validation_gate
      semantic_preservation_status: preserved
      dropped_or_compressed_material: []
      unresolved_questions: []
    operator_review:
      review_required: false
      review_reason: no_conflict_detected
      review_flags: []
      safe_next_step: send_alignment_review_to_prompt_engineering
    validation_status: valid

  low_confidence_workflow_capture:
    record_id: workflow_record_messy_notes_to_output_contract
    record_role: workflow_normalization_result
    workflow_name: Messy Notes To Output Contract
    workflow_summary: >
      Provisional workflow captured from incomplete notes. The workflow appears
      to convert messy operator material into an expected output contract, but
      scope and downstream consumer are still unclear.
    workflow_scope:
      scope_id: workflow_scope_unclear_notes
      scope_type: temporary_one_off
      project_or_domain: unknown
      reusable: false
      boundary:
        includes:
          - extract_possible_workflow_steps
          - flag_missing_scope
        excludes:
          - final_prompt_generation
          - downstream_planning
      source_state: inferred_low_confidence
    label_references:
      primary_workflow_stage_ref: extraction
      secondary_workflow_stage_refs:
        - normalization
      primary_process_stage_ref: extraction
      secondary_process_stage_refs:
        - normalization
      label_confidence: 58
      label_selection_basis:
        - raw_notes_indicate_extraction
        - missing_downstream_consumer
      label_review_flags:
        - unclear_scope
        - unclear_downstream_consumer
    expected_output_references:
      - expected_output_ref_id: expected_output_ref_contract_candidate
        expected_output_type_ref: structured_contract
        role_in_workflow: intermediate_artifact
        output_required: true
        minimum_completion_evidence:
          - candidate_fields_listed
          - missing_decisions_flagged
        fidelity_requirement: strict_source_fidelity
    workflow_inputs: []
    workflow_outputs:
      - output_id: workflow_output_contract_candidate
        output_name: candidate_expected_output_contract
        expected_output_ref: expected_output_ref_contract_candidate
        consumer: operator
        completion_status: partial
    gates:
      - gate_id: workflow_gate_operator_scope_review
        gate_name: Operator Scope Review
        gate_type: operator_approval
        required: true
        pass_condition: operator_confirms_scope_and_consumer
        fail_behavior: stop_and_request_operator_decision
    transitions: []
    downstream_consumers:
      - consumer_name: operator
        consumer_role: confirm_scope_before_reuse
        handoff_fields:
          - unclear_scope
          - candidate_output_contract
          - missing_consumer
        handoff_readiness: operator_review_needed
    operator_review:
      review_required: true
      review_reason: workflow_scope_and_downstream_consumer_are_unclear
      review_flags:
        - unclear_scope
        - unclear_consumer
      safe_next_step: ask_operator_to_confirm_reuse_scope
    validation_status: operator_review_recommended
```

---

# VALIDATION - FILE-SPECIFIC CHECKS

- [ ] Defines `workflow_record` schema exactly once.
- [ ] Includes workflow identity, scope, inputs, outputs, gates, transitions, label references, expected-output references, operator review, conflict fields, downstream consumers, and minimal examples.
- [ ] References but does not duplicate `workflow_stage_taxonomy`, `process_stage_taxonomy`, or `expected_output_type_taxonomy`.
- [ ] Does not define prompt packet, routing, usage, quota, daily-plan, flow-packet, or project-status schemas.
- [ ] Does not create provider-specific prompt rules.
- [ ] Uses YAML with 2-space indentation and typed numeric constraints.

---

# NEXT PROMPT

Paste this next:
> Prompt WPD6:
> Create exactly one file.
>
> # FILE: .claude/skills/workflow-process-design/references/prompt-workflow-alignment-validation.md
>
> File type: reference_rules.
> Schema ownership: owns prompt_workflow_alignment_review schema and prompt-to-workflow validation rules.
> Context carry-forward:
> - .claude/skills/workflow-process-design/SKILL.md
> - .claude/skills/workflow-process-design/references/workflow-stage-taxonomy.md
> - .claude/skills/workflow-process-design/references/process-stage-taxonomy.md
> - .claude/skills/workflow-process-design/references/expected-output-type-contract.md
> - .claude/skills/workflow-process-design/references/workflow-record-contract.md
>
> This file must define:
> - prompt_workflow_alignment_review schema
> - prompt-to-workflow validation dimensions
> - workflow/process/output mismatch rules
> - review flags and severity levels
> - repair recommendation fields
> - failed prompt output learning signals
> - minimal examples
>
> Rules:
> - Do not define prompt_packet schema; reference prompt-engineering when needed.
> - Do not generate provider-specific prompt rules or final prompt bodies.
> - Do not route models, quota, or usage.
> - Do not duplicate workflow_stage, process_stage, expected_output_type, or workflow_record schemas.
> - Use YAML with 2-space indentation.
>
> Next prompt target: Prompt WPD7.
