# FILE: .claude/skills/ai-routing-and-usage-tracking/references/usage-delta-contract.md

# Usage Delta Contract

## Contract

```yaml
usage_delta_contract:
  artifact_name: usage_delta
  file_role: ai_routing_usage_reference_contract
  purpose: >
    Define the minimum valid structure for capturing actual AI usage after a
    prompt, flow, sprint, or execution block has been run. This file owns
    actual-versus-planned usage delta, deviation classification, quality and
    usefulness feedback, routing-learning signals, and next-planning influence.
    It does not define planned usage budget schema, monthly quota schema,
    routing-decision schema, AI surface inventory schema, prompt_packet schema,
    workflow taxonomy, or process taxonomy.

  ownership:
    owns:
      - usage_delta
      - usage_delta_item
      - actual_usage_capture
      - planned_vs_actual_comparison
      - deviation_classification
      - quality_feedback_fields
      - usefulness_feedback_fields
      - routing_learning_signal
      - quota_effect_observation
      - next_planning_influence
      - usage_delta_validation
    must_not_own:
      - planned_usage_budget_schema
      - monthly_quota_map_schema
      - routing_decision_schema
      - AI_surface_inventory_schema
      - prompt_packet_schema
      - prompt_quality_schema
      - workflow_stage_taxonomy
      - process_stage_taxonomy
      - exact_current_pricing
      - exact_current_model_rankings
      - exact_product_limits

  dependency_references:
    planned_budget_reference: references/planned-usage-budget-contract.md
    quota_map_reference: references/monthly-quota-map-contract.md
    routing_decision_reference: references/routing-decision-contract.md
    surface_inventory_reference: references/AI-surface-inventory-contract.md
    scarcity_rules_reference: references/cost-class-and-scarcity-rules.md

  volatility_policy:
    stable_claims_allowed:
      - planned_vs_actual_usage_structure
      - qualitative_cost_class
      - qualitative_scarcity_effect
      - routing_learning_signal
      - operator_feedback_fields
      - capture_source_classes
    volatile_claims_forbidden_without_current_verification:
      - exact_token_cost
      - exact_credit_cost
      - exact_remaining_quota
      - exact_rate_limit
      - exact_provider_limit
      - exact_current_model_availability
```

## Schema: usage_delta

```yaml
usage_delta:
  type: object
  required:
    - usage_delta_id
    - capture_scope
    - capture_source
    - captured_at
    - related_usage_context
    - delta_items
    - aggregate_delta_summary
    - routing_learning_summary
    - validation_status

  fields:
    usage_delta_id:
      type: string
      format: "usage_delta_<short_slug>"
      required: true

    capture_scope:
      type: string
      allowed:
        - single_prompt
        - sprint
        - flow
        - day
        - manual_operator_note
        - automated_log_batch_later
      required: true

    capture_source:
      type: string
      allowed:
        - FlowRecap
        - operator_manual_capture
        - prompt_result_feedback
        - automated_API_log_later
        - imported_usage_summary
        - provider_dashboard_manual_readout
      required: true

    captured_at:
      type: string
      format: "YYYY-MM-DD or YYYY-MM-DDTHH:MM"
      required: true

    related_usage_context:
      type: object_ref
      ref: related_usage_context
      required: true

    delta_items:
      type: list
      item_ref: usage_delta_item
      min_items: 1
      max_items: 20
      required: true

    aggregate_delta_summary:
      type: object_ref
      ref: aggregate_delta_summary
      required: true

    routing_learning_summary:
      type: object_ref
      ref: routing_learning_summary
      required: true

    next_planning_influence:
      type: object_ref
      ref: next_planning_influence
      required: false

    operator_review_flags:
      type: list
      item_type: string
      max_items: 12
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

## Schema: related_usage_context

```yaml
related_usage_context:
  type: object
  required:
    - context_kind
    - related_ids

  fields:
    context_kind:
      type: string
      allowed:
        - prompt_packet
        - prompt_sequence
        - flow_prompt_pack
        - flow_packet
        - next_day_plan
        - routing_decision
        - planned_usage_budget
        - operator_manual_context
      required: true

    related_ids:
      type: object
      required: false
      fields:
        prompt_packet_id:
          type: string
          required: false
        prompt_sequence_id:
          type: string
          required: false
        flow_id:
          type: string
          required: false
        sprint_id:
          type: string
          required: false
        routing_decision_id:
          type: string
          required: false
        planned_usage_budget_id:
          type: string
          required: false
        next_day_plan_id:
          type: string
          required: false

    project_context:
      type: string
      required: false

    expected_output_type:
      type: string
      required: false

    prompt_task_type:
      type: string
      required: false
```

## Schema: usage_delta_item

```yaml
usage_delta_item:
  type: object
  required:
    - item_id
    - planned_reference
    - actual_usage
    - planned_vs_actual
    - outcome_feedback
    - deviation_classification
    - validation_status

  fields:
    item_id:
      type: string
      format: "usage_delta_item_<short_slug>"
      required: true

    planned_reference:
      type: object
      required: true
      fields:
        routing_decision_id:
          type: string
          required: false
        planned_usage_budget_id:
          type: string
          required: false
        planned_surface_class:
          type: string
          required: false
        planned_provider_target:
          type: string
          required: false
        planned_cost_class:
          type: string
          required: false
        planned_scarcity_class:
          type: string
          required: false
        planned_usage_intent:
          type: string
          required: false

    actual_usage:
      type: object_ref
      ref: actual_usage
      required: true

    planned_vs_actual:
      type: object_ref
      ref: planned_vs_actual
      required: true

    outcome_feedback:
      type: object_ref
      ref: outcome_feedback
      required: true

    deviation_classification:
      type: object_ref
      ref: deviation_classification
      required: true

    routing_learning_signal:
      type: object_ref
      ref: routing_learning_signal
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

## Schema: actual_usage

```yaml
actual_usage:
  type: object
  required:
    - actual_surface_class
    - actual_provider_target
    - usage_capture_confidence

  fields:
    actual_surface_class:
      type: string
      allowed:
        - frontier_chat
        - deep_research
        - agent_run
        - coding_agent
        - long_context_surface
        - multimodal_surface
        - supplemental_API
        - local_or_nonfrontier_tool
        - unknown_surface
      required: true

    actual_provider_target:
      type: string
      allowed:
        - ChatGPT
        - Claude
        - Gemini
        - OpenRouter_later
        - provider_unspecified
        - unknown_provider
      required: true

    actual_mode:
      type: string
      allowed:
        - standard_chat
        - high_reasoning
        - deep_research
        - agent_run
        - code_generation
        - long_context_digest
        - multimodal_briefing
        - API_batch
        - manual_unknown
      required: false

    model_or_surface_label:
      type: string
      required: false
      note: "Use only when currently verified or directly observed by operator."

    usage_quantity:
      type: object
      required: false
      fields:
        unit_type:
          type: string
          allowed:
            - message_count
            - run_count
            - prompt_count
            - document_count
            - token_estimate
            - credit_estimate
            - unknown_unit
          required: false
        planned_units:
          type: number
          min: 0
          required: false
        actual_units:
          type: number
          min: 0
          required: false
        measurement_confidence:
          type: string
          allowed:
            - exact_from_provider_log
            - operator_estimate
            - approximate_from_context
            - unknown
          required: false

    actual_cost_class:
      type: string
      allowed:
        - free_or_included
        - low
        - medium
        - high
        - scarce_subscription
        - paid_API_unknown_amount
        - unknown
      required: false

    actual_scarcity_class:
      type: string
      allowed:
        - abundant
        - normal
        - limited
        - scarce
        - critical
        - unknown
      required: false

    usage_capture_confidence:
      type: string
      allowed:
        - high
        - medium
        - low
        - unknown
      required: true
```

## Schema: planned_vs_actual

```yaml
planned_vs_actual:
  type: object
  required:
    - alignment_status
    - variance_type
    - variance_reason

  fields:
    alignment_status:
      type: string
      allowed:
        - matched_plan
        - minor_variance
        - major_variance
        - unplanned_usage
        - planned_but_not_used
        - blocked_before_usage
        - unknown
      required: true

    variance_type:
      type: string
      allowed:
        - none
        - provider_changed
        - surface_class_changed
        - mode_changed
        - cost_class_higher_than_planned
        - cost_class_lower_than_planned
        - scarcity_higher_than_planned
        - scarcity_lower_than_planned
        - quantity_higher_than_planned
        - quantity_lower_than_planned
        - output_required_retry
        - task_not_executed
        - unknown
      required: true

    variance_reason:
      type: string
      allowed:
        - operator_choice
        - better_fit_found
        - planned_surface_unavailable
        - prompt_failed
        - output_quality_insufficient
        - quota_preservation
        - quota_spend_opportunity
        - time_constraint
        - tool_or_access_limitation
        - task_scope_changed
        - accidental_or_untracked_use
        - unknown
      required: true

    variance_note:
      type: string
      max_words: 80
      required: false

    operator_review_needed:
      type: boolean
      required: false
```

## Schema: outcome_feedback

```yaml
outcome_feedback:
  type: object
  required:
    - output_status
    - quality_score
    - usefulness_score
    - follow_up_needed

  fields:
    output_status:
      type: string
      allowed:
        - successful
        - successful_with_minor_edits
        - partially_successful
        - failed_output
        - blocked
        - not_evaluated
      required: true

    quality_score:
      type: integer
      min: 1
      max: 100
      required: true

    usefulness_score:
      type: integer
      min: 1
      max: 100
      required: true

    follow_up_needed:
      type: boolean
      required: true

    follow_up_type:
      type: string
      allowed:
        - none
        - prompt_revision
        - provider_change
        - stronger_model_or_mode
        - cheaper_surface_next_time
        - workflow_clarification
        - operator_review
        - retry_later
        - unknown
      required: false

    operator_feedback_note:
      type: string
      max_words: 120
      required: false

    failure_or_friction_tags:
      type: list
      item_type: string
      max_items: 10
      required: false
```

## Schema: deviation_classification

```yaml
deviation_classification:
  type: object
  required:
    - deviation_severity
    - correction_needed

  fields:
    deviation_severity:
      type: string
      allowed:
        - none
        - low
        - medium
        - high
        - critical
      required: true

    correction_needed:
      type: boolean
      required: true

    correction_target:
      type: string
      allowed:
        - no_correction
        - routing_decision
        - planned_usage_budget
        - monthly_quota_map
        - AI_surface_inventory
        - prompt_engineering
        - workflow_process_design
        - operator_preference
        - unknown
      required: false

    correction_note:
      type: string
      max_words: 100
      required: false
```

## Schema: routing_learning_signal

```yaml
routing_learning_signal:
  type: object
  required:
    - signal_type
    - signal_strength
    - recommended_learning_action

  fields:
    signal_type:
      type: string
      allowed:
        - route_worked_as_expected
        - route_underpowered
        - route_overpowered
        - route_too_expensive_or_scarce
        - route_too_slow
        - route_quality_surprisingly_high
        - route_quality_surprisingly_low
        - quota_spend_was_worth_it
        - quota_spend_was_not_worth_it
        - supplemental_API_candidate
        - frontier_surface_needed_next_time
        - insufficient_data
      required: true

    signal_strength:
      type: string
      allowed:
        - weak
        - medium
        - strong
        - unknown
      required: true

    recommended_learning_action:
      type: string
      allowed:
        - keep_route_rule
        - adjust_route_rule
        - increase_model_or_mode_for_similar_task
        - decrease_model_or_mode_for_similar_task
        - mark_surface_as_candidate_for_task_class
        - mark_surface_as_avoid_for_task_class
        - update_quota_strategy
        - request_operator_decision
        - collect_more_data
      required: true

    learning_note:
      type: string
      max_words: 100
      required: false
```

## Schema: aggregate_delta_summary

```yaml
aggregate_delta_summary:
  type: object
  required:
    - total_items_captured
    - usage_alignment_overall
    - scarcity_effect_overall
    - quality_outcome_overall

  fields:
    total_items_captured:
      type: integer
      min: 1
      max: 200
      required: true

    usage_alignment_overall:
      type: string
      allowed:
        - mostly_matched_plan
        - mixed_variance
        - mostly_unplanned
        - mostly_not_executed
        - unknown
      required: true

    scarcity_effect_overall:
      type: string
      allowed:
        - no_meaningful_scarcity_effect
        - scarcity_spent_deliberately
        - scarcity_spent_accidentally
        - scarcity_preserved
        - scarcity_pressure_increased
        - unknown
      required: true

    quality_outcome_overall:
      type: string
      allowed:
        - high_value_success
        - acceptable_success
        - mixed
        - low_value_or_failed
        - not_evaluated
      required: true

    budget_update_recommended:
      type: boolean
      required: false

    quota_map_review_recommended:
      type: boolean
      required: false
```

## Schema: routing_learning_summary

```yaml
routing_learning_summary:
  type: object
  required:
    - primary_learning
    - routing_rule_change_recommended
    - operator_decision_needed

  fields:
    primary_learning:
      type: string
      max_words: 120
      required: true

    routing_rule_change_recommended:
      type: boolean
      required: true

    operator_decision_needed:
      type: boolean
      required: true

    affected_task_classes:
      type: list
      item_type: string
      max_items: 12
      required: false

    affected_surface_classes:
      type: list
      item_type: string
      max_items: 12
      required: false

    recommended_next_file_to_update:
      type: string
      allowed:
        - none
        - routing-decision-contract.md
        - planned-usage-budget-contract.md
        - monthly-quota-map-contract.md
        - AI-surface-inventory-contract.md
        - cost-class-and-scarcity-rules.md
        - prompt_quality_feedback_file
        - operator_preference_note
      required: false
```

## Schema: next_planning_influence

```yaml
next_planning_influence:
  type: object
  required:
    - influence_next_day_planning
    - influence_type

  fields:
    influence_next_day_planning:
      type: boolean
      required: true

    influence_type:
      type: string
      allowed:
        - none
        - preserve_quota
        - spend_more_scarce_quota_on_high_value_work
        - route_similar_work_to_cheaper_surface
        - route_similar_work_to_stronger_surface
        - schedule_deep_research
        - schedule_agent_run
        - improve_prompt_before_next_use
        - clarify_workflow_before_next_use
        - operator_tradeoff_decision_needed
      required: true

    suggested_planning_note:
      type: string
      max_words: 120
      required: false
```

## Capture Rules

```yaml
usage_delta_capture_rules:
  minimum_capture_required_after:
    - high_end_reasoning_usage
    - deep_research_usage
    - agent_run_usage
    - scarce_subscription_usage
    - supplemental_API_batch_usage
    - major_prompt_failure
    - provider_or_surface_changed_from_plan

  light_capture_allowed_for:
    - ordinary_chat_usage
    - low_risk_prompt_iteration
    - exploratory_prompting
    - operator_unsure_but_low_impact_use

  exact_numbers_policy:
    exact_numbers_allowed_when:
      - provider_log_is_available
      - operator_reports_exact_dashboard_value
      - automated_API_log_later_provides_verified_value
    exact_numbers_not_required_when:
      - only qualitative_usage_is_available
      - subscription_quota_remaining_is_unknown
      - prompt_was_run_in_manual_chat
      - operator_does_not_want_tracking_overhead

  default_when_uncertain:
    actual_cost_class: unknown
    actual_scarcity_class: unknown
    usage_capture_confidence: low
    validation_status: operator_review_recommended
```

## Failure Modes

```yaml
usage_delta_failure_modes:
  planned_budget_duplication:
    trigger: "The file redefines planned_usage_budget fields or allocation rules."
    correction: "Remove the duplicated budget schema and reference planned-usage-budget-contract.md."

  quota_map_duplication:
    trigger: "The file redefines monthly quota inventory, limits, or scarcity classes as source-of-truth."
    correction: "Move quota definitions to monthly-quota-map-contract.md and keep only observed effects here."

  exact_pricing_claim:
    trigger: "The file claims exact current pricing, credit use, or remaining quota without verified current data."
    correction: "Replace exact claims with qualitative classes or mark exact value as requiring verification."

  route_decision_rewrite:
    trigger: "Usage feedback is used to silently overwrite the original routing decision."
    correction: "Record a routing_learning_signal and mark routing_rule_change_recommended instead."

  feedback_overhead_too_high:
    trigger: "The delta capture requires more detail than the value of the prompt justifies."
    correction: "Use light capture with qualitative fields and mark low capture confidence."

  missing_outcome_feedback:
    trigger: "Actual usage is captured without quality or usefulness outcome."
    correction: "Set output_status to not_evaluated or ask operator for a compact quality/usefulness rating."

  provider_label_unverified:
    trigger: "A model or surface label is recorded from memory rather than direct observation."
    correction: "Move it to model_or_surface_label only when observed; otherwise use unknown_provider or provider_unspecified."

  ambiguous_deviation:
    trigger: "Actual usage differs from plan but the cause is unclear."
    correction: "Set variance_reason to unknown and add operator_review_needed."
```

## Minimal Examples

### FlowRecap usage delta

```yaml
usage_delta:
  usage_delta_id: usage_delta_f3_prompt_pack_review
  capture_scope: flow
  capture_source: FlowRecap
  captured_at: "YYYY-MM-DD"
  related_usage_context:
    context_kind: flow_prompt_pack
    related_ids:
      flow_id: F3
      planned_usage_budget_id: planned_usage_budget_f3
  delta_items:
    - item_id: usage_delta_item_f3_research_prompt
      planned_reference:
        routing_decision_id: routing_decision_f3_research_prompt
        planned_surface_class: deep_research
        planned_provider_target: ChatGPT
        planned_cost_class: scarce_subscription
        planned_scarcity_class: scarce
      actual_usage:
        actual_surface_class: deep_research
        actual_provider_target: ChatGPT
        actual_mode: deep_research
        actual_cost_class: scarce_subscription
        actual_scarcity_class: scarce
        usage_capture_confidence: medium
      planned_vs_actual:
        alignment_status: matched_plan
        variance_type: none
        variance_reason: better_fit_found
      outcome_feedback:
        output_status: successful_with_minor_edits
        quality_score: 88
        usefulness_score: 92
        follow_up_needed: false
      deviation_classification:
        deviation_severity: none
        correction_needed: false
      routing_learning_signal:
        signal_type: quota_spend_was_worth_it
        signal_strength: strong
        recommended_learning_action: keep_route_rule
      validation_status: valid
  aggregate_delta_summary:
    total_items_captured: 1
    usage_alignment_overall: mostly_matched_plan
    scarcity_effect_overall: scarcity_spent_deliberately
    quality_outcome_overall: high_value_success
  routing_learning_summary:
    primary_learning: "Deep research was worth the scarce quota for this high-value synthesis task."
    routing_rule_change_recommended: false
    operator_decision_needed: false
  next_planning_influence:
    influence_next_day_planning: true
    influence_type: spend_more_scarce_quota_on_high_value_work
    suggested_planning_note: "Use scarce research mode again for similar high-impact synthesis tasks."
  validation_status: valid
```

### Unplanned usage delta

```yaml
usage_delta:
  usage_delta_id: usage_delta_unplanned_prompt_iteration
  capture_scope: single_prompt
  capture_source: operator_manual_capture
  captured_at: "YYYY-MM-DD"
  related_usage_context:
    context_kind: prompt_packet
    related_ids:
      prompt_packet_id: prompt_packet_draft_cleanup
  delta_items:
    - item_id: usage_delta_item_unplanned_cleanup
      planned_reference:
        planned_surface_class: null
        planned_provider_target: null
      actual_usage:
        actual_surface_class: frontier_chat
        actual_provider_target: provider_unspecified
        actual_mode: standard_chat
        actual_cost_class: free_or_included
        actual_scarcity_class: normal
        usage_capture_confidence: low
      planned_vs_actual:
        alignment_status: unplanned_usage
        variance_type: unknown
        variance_reason: operator_choice
        variance_note: "Operator used a normal chat surface for a quick cleanup."
      outcome_feedback:
        output_status: successful
        quality_score: 75
        usefulness_score: 80
        follow_up_needed: false
      deviation_classification:
        deviation_severity: low
        correction_needed: false
      validation_status: valid_with_warnings
  aggregate_delta_summary:
    total_items_captured: 1
    usage_alignment_overall: mostly_unplanned
    scarcity_effect_overall: no_meaningful_scarcity_effect
    quality_outcome_overall: acceptable_success
  routing_learning_summary:
    primary_learning: "Low-risk cleanup worked without a formal route."
    routing_rule_change_recommended: false
    operator_decision_needed: false
  validation_status: valid_with_warnings
```

---

# VALIDATION — FILE-SPECIFIC CHECKS

- [ ] The file defines `usage_delta` schema.
- [ ] The file defines `usage_delta_item` schema.
- [ ] The file defines actual usage capture fields.
- [ ] The file defines planned-versus-actual comparison fields.
- [ ] The file defines deviation classification.
- [ ] The file defines quality and usefulness feedback fields.
- [ ] The file defines routing-learning signal fields.
- [ ] The file defines next-planning influence fields.
- [ ] The file defines capture rules for FlowRecap, manual capture, and automated logs later.
- [ ] The file does not duplicate planned usage budget schema.
- [ ] The file does not duplicate monthly quota map schema.
- [ ] The file does not duplicate routing-decision schema.
- [ ] The file does not duplicate AI surface inventory schema.
- [ ] The file does not claim exact current pricing, exact quota limits, exact model rankings, or exact product limits.

---

# NEXT PROMPT

Paste this next:
> Prompt AR7:
> Create exactly one file.
>
> # FILE: .claude/skills/ai-routing-and-usage-tracking/references/routing-recommendation-packet-contract.md
>
> File type: routing_recommendation_packet_contract.
> Schema ownership: owns final routing recommendation packet assembled from surface inventory, quota map, routing decision, planned budget, and usage feedback.
> Context carry-forward: load AR1-AR6 outputs before writing.
>
> This file must define:
> - routing recommendation packet schema
> - recommendation summary fields
> - provider/surface recommendation fields
> - quota/scarcity recommendation fields
> - prompt and workflow context references
> - operator tradeoff card fields
> - fallback recommendation fields
> - validation statuses
> - failure modes
> - minimal examples
>
> Rules:
> - Do not duplicate AI_surface_inventory schema.
> - Do not duplicate monthly_quota_map schema.
> - Do not duplicate routing_decision schema.
> - Do not duplicate planned_usage_budget schema.
> - Do not duplicate usage_delta schema.
> - Do not define prompt_packet schema.
> - Do not define workflow/process taxonomies.
> - Do not claim current pricing, exact model rankings, exact product limits, or exact availability.
>
> Next prompt target: Prompt AR8.
