# FILE: .claude/skills/workflow-process-design/references/prompt-process-alignment-validation.md

# Prompt Process Alignment Validation

```yaml
prompt_process_alignment_validation_file:
  artifact_name: prompt_process_alignment_validation
  file_role: workflow_process_reference_rules
  purpose: >
    Define how to validate whether a prompt or prompt packet matches the
    intended workflow stage, process stage, expected output type, sprint goal,
    success criteria, stop conditions, red flags, and operator review needs.
    This file owns alignment validation rules only. It references prompt
    engineering for prompt quality and does not redefine prompt schemas.

  ownership:
    owns:
      - prompt_process_alignment_validation
      - alignment_check_set
      - alignment_result_rules
      - mismatch_severity_rules
      - failed_prompt_output_learning_signal_rules
      - valid_warning_failed_examples
    must_not_own:
      - prompt_packet
      - prompt_sequence
      - final_copy_paste_prompt
      - prompt_quality_validation
      - provider_style_contract
      - routing_decision
      - planned_usage_budget
      - AI_surface_inventory
      - workflow_stage_taxonomy
      - process_stage_taxonomy
      - expected_output_type_contract
      - workflow_record
      - daily_plan
      - flow_packet
      - project_execution

  reference_authorities:
    prompt_schema: ".claude/skills/prompt-engineering/references/prompt-packet-contract.md"
    prompt_quality: ".claude/skills/prompt-engineering/references/prompt-quality-validation.md"
    prompt_learning_feedback: ".claude/skills/prompt-engineering/references/prompt-learning-feedback-contract.md"
    workflow_stage: ".claude/skills/workflow-process-design/references/workflow-stage-taxonomy.md"
    process_stage: ".claude/skills/workflow-process-design/references/process-stage-taxonomy.md"
    expected_output_type: ".claude/skills/workflow-process-design/references/expected-output-type-contract.md"
    workflow_record: ".claude/skills/workflow-process-design/references/workflow-record-contract.md"

  validation_status_allowed:
    - valid
    - valid_with_warnings
    - operator_review_recommended
    - low_confidence_auto_generated
    - blocked_by_missing_operator_decision
```

## Schema: prompt_process_alignment_validation

```yaml
prompt_process_alignment_validation:
  type: object
  required:
    - validation_id
    - source_prompt_ref
    - workflow_context
    - alignment_checks
    - alignment_result
    - validation_status
  fields:
    validation_id:
      type: string
      format: "prompt_process_alignment_<short_slug>"
      required: true

    source_prompt_ref:
      type: object
      required: true
      fields:
        packet_id:
          type: string
          required: false
        prompt_sequence_id:
          type: string
          required: false
        prompt_role:
          type: string
          allowed:
            - start_prompt
            - follow_up_prompt
            - standalone_prompt_packet
            - prompt_sequence_container
            - unknown
          required: true
        prompt_body_ref:
          type: string
          required: false
          note: "Reference only; do not copy the full prompt body unless needed for validation."

    workflow_context:
      type: object
      required: true
      fields:
        workflow_stage:
          type: string
          required: true
          source_authority: workflow_stage_taxonomy
        process_stage:
          type: string
          required: true
          source_authority: process_stage_taxonomy
        expected_output_type:
          type: string
          required: true
          source_authority: expected_output_type_contract
        sprint_goal:
          type: string
          required: true
        success_criteria:
          type: list
          item_type: string
          min_items: 1
          max_items: 8
          required: true
        stop_conditions_or_red_flags:
          type: list
          item_type: string
          min_items: 0
          max_items: 8
          required: false
        operator_review_point:
          type: string
          required: false

    alignment_checks:
      type: object_ref
      ref: alignment_check_set
      required: true

    alignment_result:
      type: object_ref
      ref: alignment_result
      required: true

    failed_prompt_output_learning_signal:
      type: object_ref
      ref: failed_prompt_output_learning_signal
      required: false

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

## Alignment Check Set

```yaml
alignment_check_set:
  type: object
  required:
    - workflow_stage_match
    - process_stage_match
    - expected_output_type_match
    - success_criteria_coverage
    - sprint_goal_fit
    - alignment_summary
  fields:
    workflow_stage_match:
      type: object_ref
      ref: alignment_check
      required: true
      checks:
        - prompt_action_matches_workflow_stage
        - prompt_does_not_skip_required_stage
        - prompt_does_not_create_artifact_from_wrong_stage

    process_stage_match:
      type: object_ref
      ref: alignment_check
      required: true
      checks:
        - prompt_action_matches_process_stage
        - prompt_iteration_logic_matches_process_stage
        - prompt_does_not_execute_when_process_stage_is_planning_or_validation

    expected_output_type_match:
      type: object_ref
      ref: alignment_check
      required: true
      checks:
        - requested_output_shape_matches_expected_output_type
        - output_contract_is_explicit_enough
        - prompt_does_not_request_extra_unowned_artifacts

    success_criteria_coverage:
      type: object_ref
      ref: alignment_check
      required: true
      checks:
        - each_required_success_criterion_is_addressed
        - acceptance_conditions_are_visible
        - validation_or_self_check_is_present_when_needed

    stop_condition_or_red_flag_coverage:
      type: object_ref
      ref: alignment_check
      required: false
      checks:
        - relevant_stop_conditions_are_present
        - red_flags_are_named_for_high_risk_tasks
        - escalation_to_operator_is_present_when_required

    sprint_goal_fit:
      type: object_ref
      ref: alignment_check
      required: true
      checks:
        - prompt_scope_fits_sprint_goal
        - prompt_does_not_expand_into_full_day_plan
        - prompt_outputs_are_usable_for_the_current_sprint

    source_context_fit:
      type: object_ref
      ref: alignment_check
      required: false
      checks:
        - prompt_uses_available_context_without_inventing_missing_state
        - prompt_marks_missing_context_when_needed
        - prompt_does_not_require_absent_files_unless_supplied

    operator_gate_fit:
      type: object_ref
      ref: alignment_check
      required: false
      checks:
        - operator_gate_is_preserved_when_stage_requires_review
        - prompt_does_not_override_operator_choice
        - prompt_surfaces_tradeoffs_when_conflict_exists

    alignment_summary:
      type: string
      required: true
```

## Schema: alignment_check

```yaml
alignment_check:
  type: object
  required:
    - status
    - severity
    - finding
    - correction_required
    - owner_package
  fields:
    status:
      type: string
      allowed:
        - aligned
        - warning
        - failed
        - not_applicable
      required: true

    severity:
      type: string
      allowed:
        - blocking
        - high
        - medium
        - low
        - none
      required: true

    finding:
      type: string
      required: true

    correction_required:
      type: string
      required: true

    owner_package:
      type: string
      allowed:
        - workflow-process-design
        - prompt-engineering
        - ai-routing-and-usage-tracking
        - precap-next-day
        - operator
        - none
      required: true
```

## Alignment Result Rules

```yaml
alignment_result:
  type: object
  required:
    - overall_status
    - blocking_mismatches
    - warnings
    - recommended_corrections
    - downstream_use
  fields:
    overall_status:
      type: string
      allowed:
        - aligned
        - aligned_with_warnings
        - misaligned_operator_review_needed
        - blocked_by_missing_operator_decision
        - low_confidence_due_to_missing_context
      required: true

    blocking_mismatches:
      type: list
      item_type: string
      required: true

    warnings:
      type: list
      item_type: string
      required: true

    recommended_corrections:
      type: list
      item_type: string
      min_items: 0
      max_items: 8
      required: true

    downstream_use:
      type: string
      allowed:
        - safe_to_use
        - safe_to_use_with_warnings
        - revise_prompt_before_use
        - operator_decision_required
        - blocked
      required: true
```

```yaml
status_derivation_rules:
  valid:
    use_when:
      - all_required_alignment_checks_are_aligned
      - no_blocking_mismatches_exist
      - prompt_quality_is_not_being_revalidated_here
    downstream_use: safe_to_use

  valid_with_warnings:
    use_when:
      - no_blocking_mismatches_exist
      - one_or_more_nonblocking_warnings_exist
      - corrections_are_minor_or_optional
    downstream_use: safe_to_use_with_warnings

  operator_review_recommended:
    use_when:
      - high_severity_mismatch_exists
      - workflow_or_process_fit_is_unclear
      - prompt_expands_scope_beyond_sprint_goal
      - expected_output_type_is_probable_but_not_certain
    downstream_use: revise_prompt_before_use

  low_confidence_auto_generated:
    use_when:
      - workflow_context_is_thin
      - expected_output_type_is_missing_or_inferred
      - sprint_goal_is_underspecified
    downstream_use: operator_decision_required

  blocked_by_missing_operator_decision:
    use_when:
      - conflict_requires_operator_tradeoff
      - prompt_requests_action_outside_authorized_workflow_stage
      - operator_gate_would_be_bypassed
      - two_or_more_valid_stage_interpretations_change_the_prompt_materially
    downstream_use: blocked
```

## Mismatch Severity Rules

```yaml
mismatch_severity_rules:
  blocking:
    conditions:
      - prompt_requests_project_execution_when_stage_is_planning
      - prompt_requests_status_merge_when_stage_is_recap_or_prompt_generation
      - prompt_output_type_conflicts_with_expected_output_type
      - prompt_bypasses_required_operator_gate
      - prompt_requires_provider_or_route_not_authorized_by_routing_decision
      - operator_tradeoff_decision_is_missing
    correction: "Stop and require prompt revision or operator decision before use."

  high:
    conditions:
      - workflow_stage_is_probable_but_not_explicit
      - process_stage_does_not_match_iteration_logic
      - key_success_criteria_are_missing
      - sprint_goal_is_partially_covered_only
      - prompt_expands_into_multiple_sprints_without_permission
    correction: "Revise before high-impact use; operator review recommended."

  medium:
    conditions:
      - stop_conditions_are_weak
      - red_flags_are_missing_for_moderate_risk_task
      - output_contract_is_usable_but_underconstrained
      - source_context_handling_is_underspecified
    correction: "Use with warnings or revise when time allows."

  low:
    conditions:
      - labels_are_present_but_could_be_more_precise
      - success_criteria_are_present_but not exhaustive
      - minor wording mismatch_without_material_output_risk
    correction: "Record warning; use if no higher-severity issue exists."
```

## Failed Prompt Output Learning Signals

```yaml
failed_prompt_output_learning_signal:
  type: object
  required:
    - learning_signal_id
    - source_prompt_ref
    - observed_failure
    - failure_category
    - suggested_learning_destination
    - update_policy
  fields:
    learning_signal_id:
      type: string
      format: "workflow_prompt_learning_<short_slug>"
      required: true

    source_prompt_ref:
      type: object
      required: true
      fields:
        packet_id:
          type: string
          required: false
        prompt_sequence_id:
          type: string
          required: false
        workflow_stage:
          type: string
          required: false
        process_stage:
          type: string
          required: false
        expected_output_type:
          type: string
          required: false

    observed_failure:
      type: string
      required: true

    failure_category:
      type: string
      allowed:
        - workflow_stage_mismatch
        - process_stage_mismatch
        - expected_output_type_mismatch
        - sprint_goal_mismatch
        - missing_success_criteria
        - missing_stop_condition_or_red_flag
        - operator_gate_bypass
        - prompt_quality_issue_owned_elsewhere
        - routing_or_surface_issue_owned_elsewhere
        - insufficient_source_context
      required: true

    suggested_learning_destination:
      type: string
      allowed:
        - prompt_engineering_feedback
        - workflow_record_revision
        - expected_output_contract_revision_candidate
        - workflow_stage_taxonomy_review
        - process_stage_taxonomy_review
        - operator_review_note
        - routing_review_note
      required: true

    update_policy:
      type: string
      allowed:
        - suggest_only
        - append_to_review_flags
        - create_revision_candidate
        - block_until_operator_decision
      required: true
```

```yaml
learning_signal_policy:
  prompt_quality_failures:
    owner: prompt-engineering
    rule: "Do not fix prompt quality doctrine here; emit a learning signal for prompt-engineering."

  workflow_fit_failures:
    owner: workflow-process-design
    rule: "Record the mismatch and propose stage, process, expected-output, or sprint-goal correction."

  routing_failures:
    owner: ai-routing-and-usage-tracking
    rule: "Record routing or surface mismatch only as a review note; routing schema remains external."

  operator_conflicts:
    owner: operator
    rule: "When tradeoff order or stage choice changes the prompt materially, block until operator decision."
```

## Validation Procedure

```yaml
prompt_process_alignment_validation_procedure:
  steps:
    1_load_prompt_reference:
      action: "Load prompt packet, prompt sequence, or prompt body reference."
      outcome: "source_prompt_ref is populated."

    2_load_workflow_context:
      action: "Load workflow_stage, process_stage, expected_output_type, sprint_goal, success criteria, and stop conditions if available."
      outcome: "workflow_context is populated or marked low confidence."

    3_run_required_checks:
      action: "Check workflow stage, process stage, expected output type, success criteria, and sprint goal."
      outcome: "required alignment checks are marked aligned, warning, failed, or not_applicable."

    4_run_optional_checks:
      action: "Check stop conditions, source context, and operator gate fit when relevant."
      outcome: "optional checks are added without blocking unrelated prompts."

    5_classify_result:
      action: "Apply mismatch severity and status derivation rules."
      outcome: "alignment_result and validation_status are assigned."

    6_emit_learning_signal:
      action: "If prompt output or prompt design failed because of process mismatch, create failed_prompt_output_learning_signal."
      outcome: "Learning signal is routed to the correct package or operator review lane."
```

## Examples

```yaml
valid_example:
  validation_id: prompt_process_alignment_apex_contract_generation
  source_prompt_ref:
    packet_id: prompt_packet_apex_contract
    prompt_role: start_prompt
  workflow_context:
    workflow_stage: artifact_creation
    process_stage: file_generation
    expected_output_type: reference_contract
    sprint_goal: "Create one workflow-process reference contract."
    success_criteria:
      - "One complete file is produced."
      - "The file owns only its declared schema."
      - "Validation checklist is present."
    stop_conditions_or_red_flags:
      - "Do not create multiple files."
      - "Do not duplicate upstream schemas."
  alignment_checks:
    workflow_stage_match:
      status: aligned
      severity: none
      finding: "Prompt asks for one reference contract, matching artifact creation."
      correction_required: "None."
      owner_package: none
    process_stage_match:
      status: aligned
      severity: none
      finding: "Prompt action is file generation, matching process stage."
      correction_required: "None."
      owner_package: none
    expected_output_type_match:
      status: aligned
      severity: none
      finding: "Output type is explicit and matches reference_contract."
      correction_required: "None."
      owner_package: none
    success_criteria_coverage:
      status: aligned
      severity: none
      finding: "Success criteria are directly represented in the prompt."
      correction_required: "None."
      owner_package: none
    sprint_goal_fit:
      status: aligned
      severity: none
      finding: "Prompt scope fits one sprint and one file."
      correction_required: "None."
      owner_package: none
    alignment_summary: "Prompt is aligned with workflow, process, expected output, and sprint goal."
  alignment_result:
    overall_status: aligned
    blocking_mismatches: []
    warnings: []
    recommended_corrections: []
    downstream_use: safe_to_use
  validation_status: valid
```

```yaml
warning_example:
  validation_id: prompt_process_alignment_moa_website_outline
  source_prompt_ref:
    packet_id: prompt_packet_moa_outline
    prompt_role: start_prompt
  workflow_context:
    workflow_stage: design_exploration
    process_stage: outline_expand_compress
    expected_output_type: structured_outline
    sprint_goal: "Draft a first website structure for MasterOfArts."
    success_criteria:
      - "Major pages are listed."
      - "Offer structure is visible."
    stop_conditions_or_red_flags: []
  alignment_checks:
    workflow_stage_match:
      status: aligned
      severity: none
      finding: "Prompt asks for design exploration, not final implementation."
      correction_required: "None."
      owner_package: none
    process_stage_match:
      status: warning
      severity: medium
      finding: "Prompt requests an outline but does not name compression or review criteria."
      correction_required: "Add a short compression or review step."
      owner_package: prompt-engineering
    expected_output_type_match:
      status: aligned
      severity: none
      finding: "Structured outline is explicit."
      correction_required: "None."
      owner_package: none
    success_criteria_coverage:
      status: warning
      severity: medium
      finding: "Offer structure is named, but page-level acceptance criteria are thin."
      correction_required: "Add page inclusion criteria or mark operator review."
      owner_package: workflow-process-design
    sprint_goal_fit:
      status: aligned
      severity: none
      finding: "Scope fits a single exploration sprint."
      correction_required: "None."
      owner_package: none
    alignment_summary: "Prompt is usable with warnings; criteria should be tightened."
  alignment_result:
    overall_status: aligned_with_warnings
    blocking_mismatches: []
    warnings:
      - "Process stage criteria are under-specified."
      - "Success criteria are thin."
    recommended_corrections:
      - "Add outline review criteria."
      - "Add operator-review flag for final page hierarchy."
    downstream_use: safe_to_use_with_warnings
  validation_status: valid_with_warnings
```

```yaml
failed_example:
  validation_id: prompt_process_alignment_wrong_stage_execution
  source_prompt_ref:
    packet_id: prompt_packet_leela_execute_feature
    prompt_role: start_prompt
  workflow_context:
    workflow_stage: planning
    process_stage: research_synthesize_decide
    expected_output_type: decision_matrix
    sprint_goal: "Decide implementation direction for a Leela feature."
    success_criteria:
      - "Options are compared."
      - "Risks and dependencies are visible."
    stop_conditions_or_red_flags:
      - "Do not implement code in this sprint."
  alignment_checks:
    workflow_stage_match:
      status: failed
      severity: blocking
      finding: "Prompt asks the model to implement code, but workflow stage is planning."
      correction_required: "Rewrite prompt as decision support, not execution."
      owner_package: prompt-engineering
    process_stage_match:
      status: failed
      severity: high
      finding: "Prompt does not research, synthesize, or decide; it executes."
      correction_required: "Use research_synthesize_decide structure."
      owner_package: prompt-engineering
    expected_output_type_match:
      status: failed
      severity: blocking
      finding: "Prompt requests code output instead of decision_matrix."
      correction_required: "Change output contract to decision_matrix."
      owner_package: prompt-engineering
    success_criteria_coverage:
      status: failed
      severity: high
      finding: "Comparison and risk criteria are absent."
      correction_required: "Add option comparison, risk, dependency, and recommendation fields."
      owner_package: workflow-process-design
    sprint_goal_fit:
      status: failed
      severity: blocking
      finding: "Prompt exceeds sprint goal by moving from decision to implementation."
      correction_required: "Block use until prompt is rewritten."
      owner_package: operator
    alignment_summary: "Prompt is misaligned and must not be used as written."
  alignment_result:
    overall_status: misaligned_operator_review_needed
    blocking_mismatches:
      - "Execution requested during planning stage."
      - "Wrong expected output type."
      - "Sprint goal exceeded."
    warnings: []
    recommended_corrections:
      - "Rewrite as a decision_matrix prompt."
      - "Add risks, dependencies, and option comparison."
      - "Preserve no-code stop condition."
    downstream_use: revise_prompt_before_use
  failed_prompt_output_learning_signal:
    learning_signal_id: workflow_prompt_learning_leela_wrong_stage
    source_prompt_ref:
      packet_id: prompt_packet_leela_execute_feature
      workflow_stage: planning
      process_stage: research_synthesize_decide
      expected_output_type: decision_matrix
    observed_failure: "Prompt tried to implement code instead of producing a decision matrix."
    failure_category: workflow_stage_mismatch
    suggested_learning_destination: prompt_engineering_feedback
    update_policy: append_to_review_flags
  validation_status: operator_review_recommended
```

---

# VALIDATION - FILE-SPECIFIC CHECKS

- [ ] Exactly one file was produced.
- [ ] The file path is `.claude/skills/workflow-process-design/references/prompt-process-alignment-validation.md`.
- [ ] The file owns `prompt_process_alignment_validation` only.
- [ ] Alignment checks cover `workflow_stage`, `process_stage`, and `expected_output_type`.
- [ ] Success criteria, stop conditions or red flags, and sprint goal fit are included.
- [ ] Prompt quality ownership is referenced but not duplicated.
- [ ] Failed prompt outputs become learning signals.
- [ ] Routing, quota, prompt-packet, workflow-stage, process-stage, and expected-output schemas are not duplicated.
- [ ] YAML blocks use 2-space indentation.

---

# NEXT PROMPT

Paste this next:
> Prompt WP9:
> Create exactly one file.
>
> # FILE: .claude/skills/workflow-process-design/references/operator-validation-and-conflict-resolution.md
>
> File type: reference_rules.
> Schema ownership: owns operator_validation_and_conflict_resolution.
> Context carry-forward:
> - all previously generated workflow-process-design files
>
> Structure constraints:
> - YAML-first rule file.
> - Include operator tradeoff cards and conflict handling.
> - Do not duplicate prompt_process_alignment_validation from WP8.
>
> Content constraints:
> - Define how to present conflicts between workflow fit, prompt quality, routing/cost, and operator intent.
> - Preserve conflict authority order: operator decision, workflow/process fit, prompt quality, routing/cost.
> - Define blocked, warning, and operator-review-needed states.
> - Define how options should be listed when skill databases disagree.
>
> File-specific checks:
> - [ ] Conflict authority order is preserved.
> - [ ] Operator choice is not overridden.
> - [ ] Prompt/process alignment rules are referenced, not duplicated.
>
> Next prompt target: Prompt WP10.
