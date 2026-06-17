# FILE: .claude/skills/prompt-engineering/references/prompt-learning-feedback-contract.md

```markdown id="p34l9x"
# Prompt Learning Feedback Contract

```yaml
prompt_learning_feedback_contract:
  artifact_name: prompt_learning_feedback
  file_role: prompt_engineering_reference_contract
  purpose: >
    Define lightweight structures for turning prompt outputs, failed outputs,
    operator feedback, model friction, and FlowRecap observations into reusable
    learning signals. This file owns prompt learning feedback contracts only.
    It does not require mandatory capture blocks inside every prompt body and
    does not define routing, usage, workflow, prompt_packet, or FlowRecap schema.

  ownership:
    owns:
      - prompt_learning_feedback
      - prompt_result_feedback
      - failed_prompt_output_learning
      - provider_fit_learning
      - prompt_pattern_update_candidate
      - what_to_feed_to_usage_tracking
      - what_to_feed_to_workflow_process_design
      - prompt_learning_signal_examples
    must_not_own:
      - prompt_packet_schema
      - prompt_quality_validation_schema
      - routing_decision_schema
      - planned_usage_budget_schema
      - usage_delta_schema
      - workflow_stage_taxonomy
      - process_stage_taxonomy
      - workflow_record_schema
      - FlowRecap_output_schema
      - daily_plan_schema

  learning_policy:
    lightweight_by_default: true
    feedback_capture_optional_per_prompt: true
    mandatory_capture_block_inside_every_prompt_body: false
    canonical_capture_sources:
      - prompt_result_feedback
      - operator_feedback
      - failed_prompt_output
      - provider_friction_note
      - FlowRecap_observation
    learning_must_be_reusable: true
    learning_must_not_store_private_reasoning: true
    learning_must_not_override_operator_decisions: true
```

## Schema: prompt_learning_feedback

```yaml id="n8r1fp"
prompt_learning_feedback:
  type: object
  required:
    - feedback_id
    - feedback_source
    - prompt_packet_id
    - learning_summary
    - learning_signals
    - validation_status

  fields:
    feedback_id:
      type: string
      format: "prompt_learning_feedback_<short_slug>"
      required: true

    feedback_source:
      type: string
      allowed:
        - prompt_result_feedback
        - failed_prompt_output
        - operator_feedback
        - provider_friction_note
        - FlowRecap_observation
        - prompt_quality_review
      required: true

    prompt_packet_id:
      type: string
      required: true

    provider_target:
      type: string
      allowed:
        - ChatGPT
        - Claude
        - Gemini
        - OpenRouter_later
        - provider_unspecified
      required: false

    prompt_task_type:
      type: string
      required: false

    expected_output_type:
      type: string
      required: false

    learning_summary:
      type: string
      max_words:
        type: integer
        min: 1
        max: 80
      required: true

    learning_signals:
      type: list
      item_type: string
      min_items: 1
      max_items: 8
      required: true

    recommended_action:
      type: string
      allowed:
        - keep_pattern
        - revise_prompt
        - revise_provider_choice
        - revise_output_contract
        - revise_workflow_alignment
        - add_failure_hint
        - add_example
        - operator_review_recommended
        - no_action
      required: true

    handoffs:
      type: object
      required: false
      fields:
        usage_tracking:
          type: object_ref
          ref: what_to_feed_to_usage_tracking
          required: false
        workflow_process_design:
          type: object_ref
          ref: what_to_feed_to_workflow_process_design
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
```

## Schema: prompt_result_feedback

```yaml id="m0f7ak"
prompt_result_feedback:
  type: object
  required:
    - result_id
    - prompt_packet_id
    - result_quality
    - operator_feedback_summary
    - reusable_learning

  fields:
    result_id:
      type: string
      format: "prompt_result_<short_slug>"
      required: true

    prompt_packet_id:
      type: string
      required: true

    provider_target:
      type: string
      allowed:
        - ChatGPT
        - Claude
        - Gemini
        - OpenRouter_later
        - provider_unspecified
      required: false

    result_quality:
      type: string
      allowed:
        - excellent
        - usable
        - usable_after_minor_edit
        - weak
        - failed
        - not_used
      required: true

    operator_feedback_summary:
      type: string
      max_words:
        type: integer
        min: 1
        max: 100
      required: true

    output_shape_fit:
      type: string
      allowed:
        - matched_expected_output
        - partially_matched_expected_output
        - wrong_shape
        - too_verbose
        - too_sparse
        - unclear
      required: false

    prompt_instruction_fit:
      type: string
      allowed:
        - followed_well
        - partially_followed
        - ignored_key_constraint
        - invented_context
        - overexpanded_scope
        - unclear
      required: false

    reusable_learning:
      type: list
      item_type: string
      min_items: 1
      max_items: 6
      required: true

    next_prompt_change:
      type: string
      allowed:
        - none
        - tighten_output_contract
        - add_context_boundary
        - add_validation_criteria
        - add_stop_condition
        - change_provider_style
        - change_iteration_loop
        - split_prompt
        - operator_review_needed
      required: false
```

## Schema: failed_prompt_output_learning

```yaml id="u4bi8s"
failed_prompt_output_learning:
  type: object
  required:
    - failure_id
    - prompt_packet_id
    - failure_class
    - failure_description
    - correction_hint

  fields:
    failure_id:
      type: string
      format: "failed_prompt_output_<short_slug>"
      required: true

    prompt_packet_id:
      type: string
      required: true

    failure_class:
      type: string
      allowed:
        - wrong_output_shape
        - missing_context_boundary
        - hallucinated_source_claim
        - weak_validation
        - weak_stop_condition
        - provider_mismatch
        - workflow_mismatch
        - process_stage_mismatch
        - excessive_alternatives
        - unbounded_agentic_scope
        - ignored_operator_boundary
        - too_abstract_to_use
      required: true

    failure_description:
      type: string
      max_words:
        type: integer
        min: 1
        max: 100
      required: true

    likely_prompt_cause:
      type: string
      allowed:
        - role_too_vague
        - task_too_broad
        - missing_output_contract
        - missing_constraints
        - missing_validation_criteria
        - provider_style_mismatch
        - workflow_labels_missing_or_wrong
        - source_context_unclear
        - task_too_large_for_one_prompt
        - unknown
      required: false

    correction_hint:
      type: string
      max_words:
        type: integer
        min: 1
        max: 80
      required: true

    should_create_pattern_update_candidate:
      type: boolean
      required: true
```

## Schema: provider_fit_learning

```yaml id="q3j8zz"
provider_fit_learning:
  type: object
  required:
    - provider_target
    - fit_result
    - provider_learning_summary

  fields:
    provider_target:
      type: string
      allowed:
        - ChatGPT
        - Claude
        - Gemini
        - OpenRouter_later
        - provider_unspecified
      required: true

    fit_result:
      type: string
      allowed:
        - strong_fit
        - acceptable_fit
        - weak_fit
        - wrong_fit
        - inconclusive
      required: true

    provider_learning_summary:
      type: string
      max_words:
        type: integer
        min: 1
        max: 80
      required: true

    model_or_surface_friction:
      type: list
      item_type: string
      allowed_items:
        - too_slow
        - quota_pressure
        - weak_instruction_following
        - weak_long_context_handling
        - weak_tool_or_file_handling
        - weak_source_grounding
        - over_verbose_output
        - underpowered_reasoning
        - no_friction_observed
        - unknown
      required: false

    route_adjustment_hint:
      type: string
      allowed:
        - prefer_same_provider_next_time
        - avoid_same_provider_for_this_task_type
        - use_higher_reasoning_surface
        - use_long_context_surface
        - use_research_surface
        - use_agent_run_surface
        - use_lower_cost_surface
        - ask_ai_routing_for_decision
        - no_change
      required: false
```

## Schema: prompt_pattern_update_candidate

```yaml id="a7x2dl"
prompt_pattern_update_candidate:
  type: object
  required:
    - candidate_id
    - source_feedback_ids
    - pattern_area
    - proposed_update
    - evidence_strength
    - operator_review_required

  fields:
    candidate_id:
      type: string
      format: "prompt_pattern_update_<short_slug>"
      required: true

    source_feedback_ids:
      type: list
      item_type: string
      min_items: 1
      max_items: 8
      required: true

    pattern_area:
      type: string
      allowed:
        - prompt_task_taxonomy
        - iteration_loop_patterns
        - provider_style_contract
        - prompt_quality_validation
        - prompt_packet_contract
        - starter_examples
        - failure_hints
        - learning_hints
      required: true

    proposed_update:
      type: string
      max_words:
        type: integer
        min: 1
        max: 120
      required: true

    evidence_strength:
      type: string
      allowed:
        - single_observation
        - repeated_observation
        - strong_operator_feedback
        - failed_regression_example
        - inconclusive
      required: true

    operator_review_required:
      type: boolean
      required: true

    acceptance_condition:
      type: string
      required: false
```

## Schema: what_to_feed_to_usage_tracking

```yaml id="inl9bx"
what_to_feed_to_usage_tracking:
  type: object
  required:
    - prompt_packet_id
    - provider_target
    - result_quality
    - provider_fit_result
    - usage_learning_signal

  fields:
    prompt_packet_id:
      type: string
      required: true

    provider_target:
      type: string
      allowed:
        - ChatGPT
        - Claude
        - Gemini
        - OpenRouter_later
        - provider_unspecified
      required: true

    result_quality:
      type: string
      allowed:
        - excellent
        - usable
        - usable_after_minor_edit
        - weak
        - failed
        - not_used
      required: true

    provider_fit_result:
      type: string
      allowed:
        - strong_fit
        - acceptable_fit
        - weak_fit
        - wrong_fit
        - inconclusive
      required: true

    usage_learning_signal:
      type: string
      allowed:
        - repeat_route
        - avoid_route
        - use_higher_reasoning_next_time
        - use_lower_cost_next_time
        - reserve_scarce_mode
        - spend_underused_quota
        - route_inconclusive
      required: true

    operator_friction_note:
      type: string
      required: false

    should_influence_next_day_planning:
      type: boolean
      required: true
```

## Schema: what_to_feed_to_workflow_process_design

```yaml id="o1g7rh"
what_to_feed_to_workflow_process_design:
  type: object
  required:
    - prompt_packet_id
    - workflow_alignment_signal
    - expected_output_type_signal
    - process_learning_signal

  fields:
    prompt_packet_id:
      type: string
      required: true

    workflow_stage:
      type: string
      required: false

    process_stage:
      type: string
      required: false

    expected_output_type:
      type: string
      required: false

    workflow_alignment_signal:
      type: string
      allowed:
        - aligned
        - partially_aligned
        - workflow_stage_unclear
        - process_stage_unclear
        - mismatched_to_flow_goal
        - mismatched_to_sprint_goal
        - inconclusive
      required: true

    expected_output_type_signal:
      type: string
      allowed:
        - output_type_worked
        - output_type_too_broad
        - output_type_too_narrow
        - output_type_wrong_for_task
        - output_contract_missing
        - inconclusive
      required: true

    process_learning_signal:
      type: string
      allowed:
        - keep_workflow_label
        - revise_workflow_label
        - revise_process_stage
        - revise_expected_output_type
        - add_validation_example
        - operator_review_recommended
        - no_change
      required: true

    validation_note:
      type: string
      required: false
```

## Learning Flow Rules

```yaml id="re91zv"
learning_flow_rules:
  create_prompt_learning_feedback_when:
    - operator_reports_prompt_result
    - prompt_output_failed_expected_shape
    - provider_or_surface_created_friction
    - FlowRecap_names_prompt_failure_or_success
    - prompt_quality_review_marks_failed_or_warning

  do_not_create_prompt_learning_feedback_when:
    - result_is_unknown_and_no_feedback_exists
    - operator_only_requests_final_prompt_without_learning
    - feedback_would_duplicate_existing_learning_without_change

  compactness_rules:
    max_learning_signals_per_feedback:
      type: integer
      min: 1
      max: 8
    max_words_learning_summary:
      type: integer
      min: 1
      max: 80
    max_pattern_candidates_from_one_feedback:
      type: integer
      min: 0
      max: 2

  handoff_rules:
    feed_usage_tracking_when:
      - provider_fit_result_is_weak_or_strong
      - route_should_be_repeated_or_avoided
      - scarce_or_high_value_mode_was_used
      - operator_friction_affects_future_route
    feed_workflow_process_design_when:
      - workflow_stage_or_process_stage_mismatch_exists
      - expected_output_type_failed
      - output_contract_was_wrong_for_task
      - flow_or_sprint_goal_mismatch_exists
    create_pattern_update_candidate_when:
      - repeated_observation_exists
      - strong_operator_feedback_exists
      - failed_regression_example_exists
      - single_observation_is_high_impact
```

## Minimal Example

```yaml id="m5v2ck"
minimal_prompt_learning_feedback:
  feedback_id: prompt_learning_feedback_clear_output_contract
  feedback_source: operator_feedback
  prompt_packet_id: prompt_packet_apex_contract_review
  provider_target: Claude
  prompt_task_type: validation
  expected_output_type: critique_report
  learning_summary: "The prompt worked because it constrained the review to exact contract defects and surgical fixes."
  learning_signals:
    - clear_defect_categories_helped
    - surgical_fix_constraint_reduced_rewrite_drift
  recommended_action: keep_pattern
  validation_status: valid
```

## Realistic Example

```yaml id="br5jhc"
realistic_prompt_result_feedback:
  prompt_result_feedback:
    result_id: prompt_result_precap_prompt_pack_review
    prompt_packet_id: prompt_packet_precap_prompt_pack_review
    provider_target: ChatGPT
    result_quality: usable_after_minor_edit
    operator_feedback_summary: "The answer found the main prompt-pack issues but added too much generic advice."
    output_shape_fit: partially_matched_expected_output
    prompt_instruction_fit: partially_followed
    reusable_learning:
      - "For prompt-pack validation, require defects to map to a named contract rule."
      - "Add a hard limit against generic improvement advice."
    next_prompt_change: add_validation_criteria

  prompt_learning_feedback:
    feedback_id: prompt_learning_feedback_prompt_pack_generic_advice
    feedback_source: prompt_result_feedback
    prompt_packet_id: prompt_packet_precap_prompt_pack_review
    provider_target: ChatGPT
    prompt_task_type: validation
    expected_output_type: critique_report
    learning_summary: "Validation prompts need explicit rule-to-defect mapping to prevent generic advice."
    learning_signals:
      - generic_advice_drift
      - missing_rule_to_defect_mapping
      - validation_contract_needs_tighter_output_shape
    recommended_action: revise_prompt
    handoffs:
      usage_tracking:
        prompt_packet_id: prompt_packet_precap_prompt_pack_review
        provider_target: ChatGPT
        result_quality: usable_after_minor_edit
        provider_fit_result: acceptable_fit
        usage_learning_signal: repeat_route
        operator_friction_note: "Minor edit required to remove generic advice."
        should_influence_next_day_planning: true
      workflow_process_design:
        prompt_packet_id: prompt_packet_precap_prompt_pack_review
        workflow_stage: validation
        process_stage: review
        expected_output_type: critique_report
        workflow_alignment_signal: aligned
        expected_output_type_signal: output_type_worked
        process_learning_signal: add_validation_example
        validation_note: "Add a validation example requiring named contract-rule mapping."
    validation_status: valid_with_warnings
```

## Failure Example

```yaml id="s6yyvq"
failure_prompt_learning_example:
  failed_prompt_output_learning:
    failure_id: failed_prompt_output_unbounded_agent_run
    prompt_packet_id: prompt_packet_agent_run_repo_cleanup
    failure_class: unbounded_agentic_scope
    failure_description: "The result proposed broad file creation and follow-on tasks beyond the requested bounded cleanup plan."
    likely_prompt_cause: missing_constraints
    correction_hint: "Add allowed actions, forbidden actions, explicit deliverable, and stop condition before use."
    should_create_pattern_update_candidate: true

  provider_fit_learning:
    provider_target: ChatGPT
    fit_result: weak_fit
    provider_learning_summary: "The task needed stricter agent-run boundaries and probably a narrower output contract."
    model_or_surface_friction:
      - over_verbose_output
      - weak_tool_or_file_handling
    route_adjustment_hint: ask_ai_routing_for_decision

  prompt_pattern_update_candidate:
    candidate_id: prompt_pattern_update_agent_run_boundaries
    source_feedback_ids:
      - failed_prompt_output_unbounded_agent_run
    pattern_area: provider_style_contract
    proposed_update: "Agent-run prompt examples should always include allowed actions, forbidden actions, exact deliverable, progress checks, and stop condition."
    evidence_strength: single_observation
    operator_review_required: true
    acceptance_condition: "Promote only after a second similar failure or direct operator approval."
```

## Non-Mandatory Capture Example

```yaml id="p7plkc"
non_mandatory_capture_example:
  rule: "Do not add a required machine-readable capture block inside every final prompt."
  allowed_light_hint_inside_prompt: >
    After using this prompt, note any major failure or operator edit as
    prompt_result_feedback if it would improve future prompts.
  canonical_capture_locations:
    - prompt_result_feedback
    - FlowRecap_observation
    - operator_feedback
  reason: "Learning capture is useful, but mandatory capture blocks make prompts heavier and reduce copy-paste usability."
```
```

---

# VALIDATION - FILE-SPECIFIC CHECKS

- [ ] The file defines `prompt_learning_feedback` structures exactly once.
- [ ] The file includes `prompt_result_feedback`, `failed_prompt_output_learning`, `provider_fit_learning`, and `prompt_pattern_update_candidate`.
- [ ] Usage-tracking handoff is explicit through `what_to_feed_to_usage_tracking`.
- [ ] Workflow-process handoff is explicit through `what_to_feed_to_workflow_process_design`.
- [ ] Learning feedback remains lightweight and compact.
- [ ] The file does not create a mandatory capture block for every prompt.
- [ ] The file does not duplicate `prompt_packet`, routing, workflow, or FlowRecap schemas.

---

# NEXT PROMPT

Paste this next:
> Prompt PE11:
> Create exactly one file.
>
> # FILE: .claude/skills/prompt-engineering/examples/starter-prompt-pack-example.md
>
> File type: example.
> Schema ownership: owns no schema.
> Context carry-forward:
> - all previously generated prompt-engineering files
>
> Structure constraints:
> - Example file only.
> - Use current decisions only.
> - Include one compact realistic prompt pack example.
> - Do not define new schemas.
>
> Content constraints:
> - Show one flow, two sprints, multiple prompts in one sprint, one ChatGPT prompt, one Claude prompt, short provider rationale, short design rationale, failure hints, learning hints, expected output type, and usage tags.
> - Use one primary prompt per prompt unit.
> - Include fallback notes only when useful.
>
> File-specific checks:
> - [ ] Example does not define a new schema.
> - [ ] Example includes provider and design rationale.
> - [ ] Example shows learning hints without mandatory capture blocks.
