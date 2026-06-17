# FILE: .claude/skills/ai-routing-and-usage-tracking/references/routing-recommendation-packet-contract.md

# Routing Recommendation Packet Contract

## Contract

```yaml
routing_recommendation_packet:
  artifact_name: routing_recommendation_packet
  file_role: ai_routing_usage_reference_contract
  schema_owner: ai-routing-and-usage-tracking
  purpose: >
    Define an advisory packet that turns routing decisions, planned usage
    budgets, usage deltas, quota posture, and operator feedback into next-day
    routing recommendations. This packet influences PreCapNextDay planning but
    never overrides operator choice, prompt quality, workflow fit, or explicit
    route decisions.

  ownership:
    owns:
      - routes_to_prefer
      - routes_to_avoid
      - underused_quota_to_spend
      - scarce_modes_to_save
      - models_or_modes_to_test
      - prompt_patterns_that_worked
      - next_day_influence
      - operator_review_flags
    must_not_own:
      - routing_decision_schema
      - planned_usage_budget_schema
      - usage_delta_schema
      - monthly_quota_map_schema
      - AI_surface_inventory_schema
      - prompt_packet_schema
      - prompt_quality_schema
      - workflow_stage_taxonomy
      - process_stage_taxonomy
      - daily_plan_schema

  advisory_policy:
    recommendations_are_binding: false
    operator_choice_overrides_packet: true
    workflow_process_fit_overrides_packet: true
    prompt_quality_overrides_cost_efficiency: true
    volatile_provider_claims_require_current_verification: true
    exact_prices_or_live_limits_forbidden: true

  input_dependencies:
    reads_from:
      - routing_decision
      - planned_usage_budget
      - usage_delta
      - monthly_quota_map
      - AI_surface_inventory
      - operator_feedback
    may_inform:
      - next_day_plan
      - flow_prompt_pack
      - planned_usage_budget
      - prompt_provider_rationale
      - usage_tracking_plan

  fields:
    packet_id:
      type: string
      required: true
      format: "routing_recommendation_<date_or_short_slug>"

    generated_from_window:
      type: object
      required: true
      fields:
        start_date:
          type: string
          required: false
          nullable: true
        end_date:
          type: string
          required: false
          nullable: true
        source_scope:
          type: string
          required: true
          allowed:
            - same_day
            - previous_day
            - rolling_week
            - manual_review_window
            - operator_defined

    routes_to_prefer:
      type: list
      required: true
      item_type: object
      item_fields:
        route_label:
          type: string
          required: true
        provider_or_surface_class:
          type: string
          required: true
        prefer_when:
          type: list
          item_type: string
          min_items: 1
          max_items: 6
          required: true
        evidence_signal:
          type: string
          required: true
          allowed:
            - repeated_good_result
            - high_value_output
            - low_friction_execution
            - underused_quota_available
            - strong_task_fit
            - operator_preference
            - low_confidence_signal
        confidence:
          type: string
          required: true
          allowed:
            - high
            - medium
            - low
            - unknown

    routes_to_avoid:
      type: list
      required: true
      item_type: object
      item_fields:
        route_label:
          type: string
          required: true
        avoid_when:
          type: list
          item_type: string
          min_items: 1
          max_items: 6
          required: true
        reason:
          type: string
          required: true
          allowed:
            - poor_result_quality
            - high_operator_friction
            - quota_pressure
            - weak_task_fit
            - unavailable_or_unverified
            - cost_not_justified
            - safety_or_permission_boundary
            - low_confidence_signal
        recovery_route_hint:
          type: string
          required: false
          nullable: true

    underused_quota_to_spend:
      type: list
      required: true
      item_type: object
      item_fields:
        quota_name:
          type: string
          required: true
        use_before_reset_priority:
          type: integer
          min: 1
          max: 100
          required: true
        spend_on:
          type: list
          item_type: string
          min_items: 1
          max_items: 6
          required: true
        planning_note:
          type: string
          required: true

    scarce_modes_to_save:
      type: list
      required: true
      item_type: object
      item_fields:
        quota_name:
          type: string
          required: true
        save_for:
          type: list
          item_type: string
          min_items: 1
          max_items: 6
          required: true
        avoid_spending_on:
          type: list
          item_type: string
          min_items: 0
          max_items: 6
          required: false
        scarcity_reason:
          type: string
          required: true

    models_or_modes_to_test:
      type: list
      required: true
      item_type: object
      item_fields:
        candidate_label:
          type: string
          required: true
        test_context:
          type: string
          required: true
        success_signal:
          type: string
          required: true
        current_verification_needed:
          type: boolean
          required: true

    prompt_patterns_that_worked:
      type: list
      required: true
      item_type: object
      item_fields:
        pattern_label:
          type: string
          required: true
        worked_for:
          type: list
          item_type: string
          min_items: 1
          max_items: 6
          required: true
        reuse_hint:
          type: string
          required: true
        feed_to_prompt_engineering:
          type: boolean
          required: true

    next_day_influence:
      type: object
      required: true
      fields:
        influence_level:
          type: string
          required: true
          allowed:
            - none
            - light
            - moderate
            - strong
            - operator_review_required
        recommended_preCapNextDay_action:
          type: string
          required: true
          allowed:
            - no_change
            - prefer_listed_routes
            - avoid_listed_routes
            - reserve_scarce_mode
            - spend_underused_quota
            - test_candidate_route
            - request_operator_route_decision
        suggested_flow_or_sprint_targets:
          type: list
          item_type: string
          min_items: 0
          max_items: 8
          required: false
        rationale:
          type: string
          required: true

    operator_review_flags:
      type: list
      item_type: string
      required: true
      allowed:
        - route_confidence_low
        - quota_state_unknown
        - provider_claim_requires_current_verification
        - scarce_mode_tradeoff_needed
        - underused_quota_spend_candidate
        - route_quality_conflict
        - workflow_fit_should_override_route
        - prompt_quality_should_override_cost
        - operator_preference_needed
        - OpenRouter_mapping_todo_later
```

## Recommendation Rules

```yaml
recommendation_rules:
  advisory_only:
    rule: >
      Treat every recommendation as planning advice. The packet may bias the
      next planned route, but it must not silently override the operator,
      workflow-process-design, prompt-engineering validation, or a concrete
      routing_decision.

  next_day_influence_required:
    rule: >
      Every packet must state whether and how the recommendation should affect
      the next PreCapNextDay planning pass.
    allowed_actions:
      - no_change
      - prefer_listed_routes
      - avoid_listed_routes
      - reserve_scarce_mode
      - spend_underused_quota
      - test_candidate_route
      - request_operator_route_decision

  use_usage_delta_without_duplication:
    rule: >
      Usage deltas provide learning signals only. Do not restate or redefine
      usage_delta fields inside this contract.

  underused_quota_policy:
    rule: >
      Recommend spending underused quota only when task value, impact, evidence
      need, or learning value justifies it.
    avoid_when:
      - task_is_low_value
      - workflow_stage_is_unclear
      - prompt_quality_is_low
      - quota_state_is_unknown_and_high_risk

  scarcity_policy:
    rule: >
      Recommend saving scarce modes for high-impact, high-risk, high-evidence,
      or high-ambiguity tasks. Cost minimization alone is not the optimization
      goal.

  current_verification_policy:
    rule: >
      If a recommendation depends on live model availability, price, quota, or
      ranking, set current_verification_needed to true or add the appropriate
      operator_review_flag.
```

## Minimal Examples

### Example: Strong Next-Day Influence

```yaml
example_strong_next_day_influence:
  packet_id: routing_recommendation_2026_06_16
  generated_from_window:
    start_date: "2026-06-15"
    end_date: "2026-06-16"
    source_scope: previous_day
  routes_to_prefer:
    - route_label: ChatGPT_deep_research_for_source_grounded_strategy
      provider_or_surface_class: scarce_monthly_mode
      prefer_when:
        - source_grounded_research_needed
        - evidence_need_is_high
        - decision_has_strategic_impact
      evidence_signal: underused_quota_available
      confidence: medium
  routes_to_avoid:
    - route_label: supplemental_API_for_high_ambiguity_architecture
      avoid_when:
        - architecture_tradeoffs_are_open
        - wrong_answer_cost_is_high
      reason: weak_task_fit
      recovery_route_hint: use_frontier_reasoning_or_operator_review
  underused_quota_to_spend:
    - quota_name: ChatGPT_Deep_Research
      use_before_reset_priority: 85
      spend_on:
        - high_evidence_product_decision
        - provider_or_standard_verification
      planning_note: Use deliberately when the next day includes research-heavy planning.
  scarce_modes_to_save:
    - quota_name: ChatGPT_Agent_Runs
      save_for:
        - bounded_multi_step_file_generation
        - repository_or_file_navigation_task
      avoid_spending_on:
        - simple_copy_editing
        - low_value_format_conversion
      scarcity_reason: Save agent runs for bounded tool-like execution.
  models_or_modes_to_test:
    - candidate_label: Claude_Code_for_structured_file_generation
      test_context: one bounded file-generation sprint
      success_signal: complete artifact with low correction overhead
      current_verification_needed: false
  prompt_patterns_that_worked:
    - pattern_label: explicit_role_task_context_output_validation
      worked_for:
        - routing_contract_generation
        - prompt_pack_generation
      reuse_hint: Keep role, task, context boundary, output contract, and validation gate explicit.
      feed_to_prompt_engineering: true
  next_day_influence:
    influence_level: strong
    recommended_preCapNextDay_action: spend_underused_quota
    suggested_flow_or_sprint_targets:
      - F3_S1
      - F3_S2
    rationale: Prior use indicates high leverage for source-grounded planning and underused research quota should be spent deliberately.
  operator_review_flags:
    - underused_quota_spend_candidate
    - provider_claim_requires_current_verification
```

### Example: Light Advisory Influence

```yaml
example_light_advisory_influence:
  packet_id: routing_recommendation_light_example
  generated_from_window:
    start_date: null
    end_date: null
    source_scope: manual_review_window
  routes_to_prefer:
    - route_label: regular_frontier_prompt_for_prompt_refinement
      provider_or_surface_class: subscription_frontier
      prefer_when:
        - task_is_prompt_refinement
        - output_contract_is_clear
      evidence_signal: repeated_good_result
      confidence: high
  routes_to_avoid: []
  underused_quota_to_spend: []
  scarce_modes_to_save:
    - quota_name: ChatGPT_Deep_Research
      save_for:
        - source_grounded_research_needed
      avoid_spending_on:
        - prompt_polishing
      scarcity_reason: No evidence-heavy task is present in the next plan.
  models_or_modes_to_test: []
  prompt_patterns_that_worked:
    - pattern_label: compact_failure_hints
      worked_for:
        - prompt_refinement
      reuse_hint: Include two or three concrete failure hints after the final prompt.
      feed_to_prompt_engineering: true
  next_day_influence:
    influence_level: light
    recommended_preCapNextDay_action: prefer_listed_routes
    suggested_flow_or_sprint_targets: []
    rationale: Prior result quality supports the same route for similar low-risk refinement tasks.
  operator_review_flags: []
```

### Example: Operator Review Required

```yaml
example_operator_review_required:
  packet_id: routing_recommendation_review_example
  generated_from_window:
    start_date: "2026-06-16"
    end_date: "2026-06-16"
    source_scope: same_day
  routes_to_prefer: []
  routes_to_avoid:
    - route_label: unknown_API_low_reasoning_route
      avoid_when:
        - route_quality_unproven
        - task_impact_is_high
      reason: low_confidence_signal
      recovery_route_hint: request_operator_route_decision
  underused_quota_to_spend: []
  scarce_modes_to_save: []
  models_or_modes_to_test:
    - candidate_label: OpenRouter_later_candidate
      test_context: low-risk mechanical extraction only
      success_signal: acceptable extraction quality at low friction
      current_verification_needed: true
  prompt_patterns_that_worked: []
  next_day_influence:
    influence_level: operator_review_required
    recommended_preCapNextDay_action: request_operator_route_decision
    suggested_flow_or_sprint_targets:
      - F4_S1
    rationale: Route confidence is too low and OpenRouter mapping is still TODO later.
  operator_review_flags:
    - route_confidence_low
    - provider_claim_requires_current_verification
    - OpenRouter_mapping_todo_later
```

## Failure Modes

```yaml
routing_recommendation_packet_failure_modes:
  duplicate_usage_delta_schema:
    trigger: The packet redefines usage_delta fields instead of consuming learning signals.
    correction: Remove duplicated fields and reference usage_delta as an input dependency only.

  recommendation_becomes_command:
    trigger: A recommendation silently overrides operator choice or workflow/prompt validation.
    correction: Mark the packet advisory and add operator_review_flags when tradeoffs require a decision.

  quota_claim_overprecision:
    trigger: The packet states exact current quotas, prices, model rankings, or availability without verification.
    correction: Replace with abstract quota posture or set current_verification_needed to true.

  cost_minimization_drift:
    trigger: The packet recommends the cheapest route despite high impact, high risk, or high evidence need.
    correction: Re-rank recommendations by leverage-weighted quality before cost.

  missing_next_day_influence:
    trigger: The packet lists observations but does not state how PreCapNextDay should use them.
    correction: Fill next_day_influence with an allowed action and rationale.

  vague_operator_flags:
    trigger: Operator review flags are generic or unactionable.
    correction: Use only specific allowed flags tied to route confidence, quota state, verification, or tradeoff decisions.
```

---

# VALIDATION - FILE-SPECIFIC CHECKS

- [ ] routing_recommendation_packet schema is defined once.
- [ ] The file includes routes_to_prefer.
- [ ] The file includes routes_to_avoid.
- [ ] The file includes underused_quota_to_spend.
- [ ] The file includes scarce_modes_to_save.
- [ ] The file includes models_or_modes_to_test.
- [ ] The file includes prompt_patterns_that_worked.
- [ ] The file includes next_day_influence.
- [ ] The file includes operator_review_flags.
- [ ] Recommendations are advisory and do not override operator choice.
- [ ] usage_delta is referenced but not duplicated.

---

# NEXT PROMPT

Paste this next:
> Prompt AR8:
> Create exactly one file.
>
> # FILE: .claude/skills/ai-routing-and-usage-tracking/references/cost-class-and-scarcity-rules.md
>
> File type: reference_rules.
> Schema ownership: owns cost_class and scarcity rules.
> Context carry-forward:
> - all previously generated ai-routing-and-usage-tracking files
>
> Structure constraints:
> - YAML-first rule file.
> - Define cost_class values and scarcity rules.
> - Include examples.
> - Do not define routing_decision again.
>
> Content constraints:
> - Include subscription_frontier, quota_limited_frontier, scarce_monthly_mode, supplemental_API_low_reasoning, and later_OpenRouter.
> - For each define use_when, avoid_when, planning_implication, usage_capture_requirement, and examples.
> - State API calls are supplemental, low-reasoning, and cost-sensitive by default.
>
> File-specific checks:
> - [ ] Cost classes are defined once.
> - [ ] API calls are marked supplemental.
> - [ ] Scarcity rules are usable by planned_usage_budget.
