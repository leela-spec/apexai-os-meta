# FILE: .claude/skills/ai-routing-and-usage-tracking/references/cost-class-and-scarcity-rules.md

# Cost Class and Scarcity Rules

## Rules Contract

```yaml
cost_class_and_scarcity_rules:
  artifact_name: cost_class_and_scarcity_rules
  file_role: ai_routing_usage_reference_rules
  schema_owner: ai-routing-and-usage-tracking
  purpose: >
    Define stable cost_class values and scarcity rules used by routing_decision,
    planned_usage_budget, usage_delta, and routing_recommendation_packet files.
    This file uses abstract planning classes only. It does not define exact
    prices, exact current quotas, exact model rankings, live availability, or
    routing_decision schema.

  ownership:
    owns:
      - cost_class_values
      - scarcity_class_values
      - cost_class_selection_rules
      - scarcity_planning_rules
      - API_default_policy
      - budget_use_implications
      - cost_class_examples
    must_not_own:
      - routing_decision_schema
      - planned_usage_budget_schema
      - usage_delta_schema
      - routing_recommendation_packet_schema
      - monthly_quota_map_schema
      - AI_surface_inventory_schema
      - prompt_packet_schema
      - exact_current_pricing
      - exact_current_product_limits
      - exact_model_rankings
      - final_OpenRouter_model_mapping

  volatility_policy:
    exact_prices_forbidden: true
    exact_current_limits_forbidden: true
    exact_model_rankings_forbidden: true
    current_provider_availability_forbidden_without_verification: true
    quota_values_must_come_from_monthly_quota_map: true
    surface_availability_must_come_from_AI_surface_inventory: true
```

## Cost Class Values

```yaml
cost_class_values:
  subscription_frontier:
    definition: >
      A frontier subscription surface whose marginal cost is treated as already
      paid for planning purposes, subject to availability, usage limits, and
      operator preference.
    use_when:
      - planned_flow_session
      - prompt_quality_matters
      - impact_or_risk_is_material
      - operator_has_available_subscription_capacity
      - current_surface_inventory_confirms_available
    avoid_when:
      - task_is_low_value_mechanical_batch
      - subscription_capacity_is_under_pressure
      - operator_requests_cost_minimal_API_route
      - current_surface_inventory_is_missing_or_uncertain
    planning_implication: >
      Prefer for daily flow prompts when quality, reasoning, and operator
      leverage matter more than marginal cost efficiency.
    usage_capture_requirement:
      capture_in_planned_usage_budget: true
      capture_in_usage_delta: true
      capture_fields:
        - cost_class
        - surface_class
        - planned_vs_actual_use
        - operator_quality_signal
    examples:
      - "A high-impact PreCapNextDay prompt pack generation task."
      - "A strategic synthesis prompt for deciding tomorrow's flow focus."

  quota_limited_frontier:
    definition: >
      A frontier model, mode, or provider surface constrained by explicit
      usage allowance, quota, reset window, or scarce interactive capacity.
    use_when:
      - output_value_justifies_quota_spend
      - quality_or_evidence_need_is_high
      - monthly_quota_map_shows_sufficient_remaining_capacity
      - operator_or_budget_allows_spend
    avoid_when:
      - quota_remaining_is_low
      - task_has_low_impact
      - cheaper_or_subscription_route_is_sufficient
      - current_quota_state_is_unknown_and_task_is_not_urgent
    planning_implication: >
      Reserve for high-leverage prompts and make the quota rationale explicit
      in planned_usage_budget and routing_decision outputs.
    usage_capture_requirement:
      capture_in_planned_usage_budget: true
      capture_in_usage_delta: true
      capture_fields:
        - quota_name
        - planned_quota_spend
        - actual_quota_spend
        - reset_window_if_known
        - scarcity_flag
    examples:
      - "A limited high-reasoning mode used for architecture tradeoff analysis."
      - "A quota-limited research mode used for source-grounded verification."

  scarce_monthly_mode:
    definition: >
      A high-value mode with monthly scarcity, reset pressure, or deliberate
      spend strategy. The class is scarcity-aware, not price-specific.
    use_when:
      - task_is_high_impact
      - task_is_high_risk
      - evidence_need_is_high
      - ambiguity_is_high
      - underused_quota_should_be_spent_before_reset
      - operator_approves_or_budget_policy_allows_use
    avoid_when:
      - task_is_routine_formatting
      - task_is_low_risk_low_ambiguity
      - quota_should_be_saved_for_later_high_value_work
      - operator_has_not_approved_a_material_tradeoff
    planning_implication: >
      Create a visible scarce-mode reservation or explicit spend note. Use
      underused scarce capacity deliberately, but do not let scarcity logic
      override workflow fit, prompt quality, or operator decision.
    usage_capture_requirement:
      capture_in_planned_usage_budget: true
      capture_in_usage_delta: true
      capture_fields:
        - scarce_mode_name
        - reservation_reason
        - spend_or_save_decision
        - actual_use_status
        - next_day_influence
    examples:
      - "A deep research session planned because underused quota is near reset."
      - "A high-stakes prompt-quality audit before finalizing a reusable skill package."

  supplemental_API_low_reasoning:
    definition: >
      A supplemental API route for low-reasoning, mechanical, cost-sensitive,
      or batch-style work. This is not the default daily flow engine.
    use_when:
      - task_is_mechanical_transformation
      - task_is_low_risk
      - task_has_clear_input_output_contract
      - high_end_reasoning_is_not_needed
      - batch_cost_efficiency_matters
    avoid_when:
      - task_requires_frontier_reasoning
      - task_is_high_impact_or_high_risk
      - source_grounded_current_research_is_required
      - task_needs_complex_workflow_or_prompt_quality_judgment
      - safety_or_permission_boundary_is_unclear
    planning_implication: >
      Treat API calls as supplemental, low-reasoning, and cost-sensitive by
      default. Use them to offload simple work, not to replace frontier daily
      planning or high-value prompt generation.
    usage_capture_requirement:
      capture_in_planned_usage_budget: true
      capture_in_usage_delta: true
      capture_fields:
        - API_route_label
        - cost_sensitivity_reason
        - low_reasoning_fit_reason
        - batch_or_single_use
    examples:
      - "Normalize a list of labels into a fixed enum."
      - "Convert simple notes into a known Markdown table shape."

  later_OpenRouter:
    definition: >
      A placeholder class for future OpenRouter/API mapping. It may be used as
      an explicit TODO route class but must not name final models, rankings,
      exact prices, or current availability without later verification.
    use_when:
      - operator_explicitly_requests_OpenRouter_placeholder
      - future_API_route_should_be_marked_for_review
      - low_reasoning_supplemental_route_is_plausible_later
      - final_model_map_is_not_needed_now
    avoid_when:
      - task_requires_final_model_selection
      - exact_pricing_or_availability_is_needed_now
      - high_impact_daily_flow_prompt_needs_reliable_frontier_route
      - route_would_be_treated_as_final_mapping
    planning_implication: >
      Mark as TODO_later and route through operator review before use. Do not
      let placeholder API planning become a final model recommendation.
    usage_capture_requirement:
      capture_in_planned_usage_budget: true
      capture_in_usage_delta: false
      capture_fields:
        - placeholder_route_label
        - review_reason
        - current_verification_needed
    examples:
      - "Future low-cost classification route after OpenRouter mapping is built."
      - "Placeholder note for a later supplemental batch transformation model."
```

## Scarcity Class Values

```yaml
scarcity_class_values:
  abundant:
    definition: "Capacity is comfortably available for normal planning use."
    planning_rule: "Use when fit is strong and no higher-priority reservation is needed."

  managed:
    definition: "Capacity is available but should be tracked and allocated deliberately."
    planning_rule: "Use for normal high-value work while recording planned and actual use."

  scarce:
    definition: "Capacity is limited enough that use requires explicit rationale."
    planning_rule: "Reserve for high-impact, high-risk, high-evidence, or high-ambiguity tasks."

  critical:
    definition: "Capacity is nearly exhausted, blocked, or strategically reserved."
    planning_rule: "Avoid use unless operator approves a clear override."

  unknown:
    definition: "Capacity state is missing, stale, or not yet verified."
    planning_rule: "Use conservative fallback routes or mark operator_review_recommended."
```

## Cost and Scarcity Selection Rules

```yaml
cost_class_selection_rules:
  priority_order:
    1: operator_explicit_route_choice
    2: workflow_process_fit
    3: prompt_quality_need
    4: impact_risk_evidence_ambiguity_score
    5: quota_or_scarcity_state
    6: cost_efficiency

  planned_flow_session_policy:
    default_preference: subscription_frontier
    use_quota_limited_frontier_when:
      - subscription_frontier_is_insufficient
      - scarce_mode_has_clear_high_value_justification
      - deep_research_or_agent_run_is_appropriate
      - operator_or_budget_policy_allows_use
    avoid_cost_minimization_only: true

  supplemental_or_batch_policy:
    default_preference: supplemental_API_low_reasoning
    use_when:
      - task_is_low_risk
      - contract_is_clear
      - transformation_is_mechanical
      - frontier_reasoning_would_be_wasteful
    require_fallback_to_frontier_when:
      - output_quality_fails
      - ambiguity_increases
      - operator_marks_result_as_low_confidence

  OpenRouter_policy:
    current_status: later_placeholder
    final_model_mapping_allowed: false
    current_verification_required_before_use: true
    default_role: supplemental_API_low_reasoning
```

## Scarcity Planning Rules

```yaml
scarcity_planning_rules:
  reserve_scarce_capacity_for:
    - high_impact_planning
    - high_risk_decisions
    - source_grounded_research
    - complex_architecture_tradeoffs
    - prompt_pack_finalization
    - workflow_process_conflict_resolution

  spend_underused_scarce_capacity_when:
    - reset_window_is_near
    - monthly_quota_map_marks_underused
    - task_has_high_leverage
    - operator_has_not_reserved_capacity_for_later
    - workflow_and_prompt_quality_need_supports_spend

  save_scarce_capacity_when:
    - known_future_high_impact_task_exists
    - quota_remaining_is_low
    - current_task_is_low_value
    - cheaper_route_is_sufficient
    - route_confidence_is_low

  operator_review_required_when:
    - scarce_mode_use_conflicts_with_budget_policy
    - cost_efficiency_conflicts_with_prompt_quality
    - workflow_fit_conflicts_with_route_recommendation
    - quota_state_is_unknown_for_material_route
    - later_OpenRouter_would_be_used_for_nontrivial_work

  planned_usage_budget_integration:
    required_fields_to_inform:
      - cost_class
      - scarcity_class
      - scarce_mode_reservation
      - fallback_rule
      - operator_review_flags
    do_not_duplicate:
      - planned_usage_budget_schema
      - monthly_quota_map_schema
      - usage_delta_schema
```

## Examples

```yaml
cost_class_examples:
  high_value_daily_prompt:
    task_summary: "Generate a provider-aware prompt pack for one Apex planning flow."
    recommended_cost_class: subscription_frontier
    scarcity_class: managed
    planning_implication: "Use a frontier subscription route and capture quality feedback in usage_delta."
    operator_review_flags: []

  deep_research_quota_spend:
    task_summary: "Verify current external claims before a high-impact architecture decision."
    recommended_cost_class: scarce_monthly_mode
    scarcity_class: scarce
    planning_implication: "Reserve a scarce research mode if monthly quota and operator approval allow it."
    operator_review_flags:
      - scarce_mode_use_requires_rationale

  mechanical_batch_transform:
    task_summary: "Convert 40 stable labels into a fixed enum list."
    recommended_cost_class: supplemental_API_low_reasoning
    scarcity_class: abundant
    planning_implication: "Use supplemental API only if available; fallback to subscription frontier if output quality fails."
    operator_review_flags: []

  OpenRouter_placeholder:
    task_summary: "Mark a future low-cost route for simple extraction after OpenRouter mapping exists."
    recommended_cost_class: later_OpenRouter
    scarcity_class: unknown
    planning_implication: "Record as TODO_later and require current verification before use."
    operator_review_flags:
      - OpenRouter_mapping_todo_later
      - current_verification_needed
```

## Failure Modes

```yaml
cost_class_and_scarcity_failure_modes:
  routing_schema_duplication:
    trigger: The file defines routing_decision fields instead of cost and scarcity classes.
    correction: Remove routing_decision fields and reference routing-decision-contract.md.

  quota_schema_duplication:
    trigger: The file defines monthly quota fields or exact quota values.
    correction: Move quota structure to monthly-quota-map-contract.md and keep only scarcity rules here.

  exact_price_claim:
    trigger: The file states current prices, live limits, availability, or exact rankings.
    correction: Replace with abstract cost_class language and require current verification.

  API_default_drift:
    trigger: API calls are treated as default daily flow engines or high-reasoning routes.
    correction: Mark API calls as supplemental, low-reasoning, and cost-sensitive by default.

  scarcity_overrides_quality:
    trigger: Scarcity or cost savings overrides workflow fit, prompt quality, or operator choice.
    correction: Restore the priority order and add operator_review_flags for the tradeoff.

  OpenRouter_finalization_drift:
    trigger: later_OpenRouter is treated as a final model mapping.
    correction: Keep later_OpenRouter as TODO_later and require current verification before final use.
```

---

# VALIDATION - FILE-SPECIFIC CHECKS

- [ ] Cost classes are defined once.
- [ ] The file includes subscription_frontier.
- [ ] The file includes quota_limited_frontier.
- [ ] The file includes scarce_monthly_mode.
- [ ] The file includes supplemental_API_low_reasoning.
- [ ] The file includes later_OpenRouter.
- [ ] API calls are marked supplemental, low-reasoning, and cost-sensitive by default.
- [ ] Scarcity rules are usable by planned_usage_budget.
- [ ] routing_decision schema is not redefined.
- [ ] Exact prices, live limits, and model rankings are not included.

---

# NEXT PROMPT

Paste this next:
> Prompt AR9:
> Create exactly one file.
>
> # FILE: .claude/skills/ai-routing-and-usage-tracking/examples/starter-usage-routing-example.md
>
> File type: example.
> Schema ownership: owns no schema.
> Context carry-forward:
> - all previously generated ai-routing-and-usage-tracking files
>
> Structure constraints:
> - Example file only.
> - Use current decisions only.
> - Do not define new schemas.
>
> Content constraints:
> - Show one prompt-heavy daily flow, one Deep Research planned use, one Agent Run planned use, one regular frontier model prompt, one usage_delta from FlowRecap, and one underused quota influencing next-day recommendation.
> - Include operator_review_flags where route confidence is limited.
> - Keep examples compact.
>
> File-specific checks:
> - [ ] Example does not define a new schema.
> - [ ] Example shows underused quota influence.
> - [ ] Example includes usage_delta.
