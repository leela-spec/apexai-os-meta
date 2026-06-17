# FILE: .claude/skills/ai-routing-and-usage-tracking/references/planned-usage-budget-contract.md

# Planned Usage Budget Contract

## Contract

```yaml
planned_usage_budget_contract:
  artifact_name: planned_usage_budget
  file_role: ai_routing_usage_reference_contract
  purpose: >
    Define the minimum valid structure for planned AI usage budgets, budget
    horizons, per-task planned usage entries, scarce-mode reservations,
    fallback budget rules, review flags, and validation requirements. This file
    owns planned allocation before execution and references monthly_quota_map,
    routing_decision, and usage_delta instead of duplicating their schemas.

  ownership:
    owns:
      - planned_usage_budget
      - budget_horizon
      - planned_usage_entry
      - scarce_mode_reservation
      - planned_usage_totals
      - budget_fallback_rule
      - planned_usage_validation_rules
      - planned_usage_failure_modes
      - planned_usage_minimal_example
    must_not_own:
      - AI_surface_inventory_schema
      - monthly_quota_map_schema
      - routing_decision_schema
      - usage_delta_schema
      - routing_recommendation_packet_schema
      - prompt_packet_schema
      - workflow_stage_taxonomy
      - process_stage_taxonomy
      - current_pricing
      - exact_product_limits
      - exact_model_rankings
      - final_OpenRouter_model_mapping

  volatility_policy:
    current_prices_forbidden: true
    exact_product_limits_forbidden: true
    exact_model_rankings_forbidden: true
    exact_quota_values_must_come_from_monthly_quota_map: true
    actual_usage_must_be_captured_by_usage_delta: true
```

## Schema: planned_usage_budget

```yaml
planned_usage_budget:
  type: object
  required:
    - budget_id
    - created_or_updated_at
    - budget_horizon
    - planning_context
    - planned_usage_entries
    - planned_usage_totals
    - validation_status

  fields:
    budget_id:
      type: string
      format: "planned_usage_budget_<short_slug>"
      required: true

    created_or_updated_at:
      type: string
      format: "YYYY-MM-DD"
      required: true

    budget_horizon:
      type: object_ref
      ref: budget_horizon
      required: true

    planning_context:
      type: object_ref
      ref: planning_context
      required: true

    monthly_quota_map_ref:
      type: string
      required: false
      nullable: true
      meaning: "Reference to the quota map used for this planned budget."

    AI_surface_inventory_ref:
      type: string
      required: false
      nullable: true
      meaning: "Reference to the surface inventory used to constrain available routes."

    planned_usage_entries:
      type: list
      item_ref: planned_usage_entry
      min_items: 1
      required: true

    scarce_mode_reservations:
      type: list
      item_ref: scarce_mode_reservation
      min_items: 0
      required: false

    planned_usage_totals:
      type: object_ref
      ref: planned_usage_totals
      required: true

    fallback_rules:
      type: list
      item_ref: budget_fallback_rule
      min_items: 0
      max_items: 8
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

## Schema: budget_horizon

```yaml
budget_horizon:
  type: object
  required:
    - horizon_type
    - starts_at
    - ends_at

  fields:
    horizon_type:
      type: string
      allowed:
        - single_prompt
        - single_flow
        - single_day
        - weekly_plan
        - monthly_plan
        - operator_defined
      required: true

    starts_at:
      type: string
      format: "YYYY-MM-DD"
      required: true

    ends_at:
      type: string
      format: "YYYY-MM-DD"
      required: true

    flow_id:
      type: string
      allowed:
        - F1
        - F2
        - F3
        - F4
        - NA
      required: false

    sprint_id:
      type: string
      allowed:
        - S1
        - S2
        - S3
        - NA
      required: false

    operator_defined_label:
      type: string
      required: false
      nullable: true
```

## Schema: planning_context

```yaml
planning_context:
  type: object
  required:
    - context_type
    - budget_goal
    - planning_assumption_status

  fields:
    context_type:
      type: string
      allowed:
        - PreCapNextDay_flow_prompt_pack
        - prompt_sequence
        - standalone_prompt_packet
        - deep_research_session
        - agent_run_session
        - supplemental_batch
        - operator_defined
      required: true

    source_artifact_refs:
      type: list
      item_type: string
      required: false

    budget_goal:
      type: string
      allowed:
        - use_monthly_quota_deliberately
        - reserve_scarce_modes_for_high_impact_work
        - balance_quality_and_cost
        - minimize_cost_when_quality_sufficient
        - follow_operator_override
        - bootstrap_unknown_usage
      required: true

    planning_assumption_status:
      type: string
      allowed:
        - quota_known
        - quota_partially_known
        - quota_unknown
        - operator_override_supplied
        - current_verification_needed
      required: true

    notes:
      type: string
      required: false
      max_words: 80
```

## Schema: planned_usage_entry

```yaml
planned_usage_entry:
  type: object
  required:
    - entry_id
    - planned_task_ref
    - planned_route_ref
    - planned_surface_class
    - planned_usage_class
    - scarcity_class
    - expected_value_class
    - planned_status

  fields:
    entry_id:
      type: string
      format: "planned_usage_entry_<short_slug>"
      required: true

    planned_task_ref:
      type: string
      required: true
      meaning: "Reference to prompt_packet, prompt_sequence, flow_packet, sprint, or operator_task."

    planned_route_ref:
      type: string
      required: false
      nullable: true
      meaning: "Reference to routing_decision if already created."

    planned_surface_class:
      type: string
      allowed:
        - frontier_chat_subscription
        - frontier_deep_research
        - frontier_agent_run
        - long_context_multimodal
        - supplemental_API_low_cost
        - local_or_free_tool
        - provider_unspecified
        - blocked_until_verified
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

    model_or_surface_target:
      type: string
      required: false
      nullable: true
      meaning: "Stable surface label or operator-supplied model label; exact volatile claims require current verification."

    planned_usage_class:
      type: string
      allowed:
        - low_reasoning_short_prompt
        - standard_reasoning_prompt
        - high_end_reasoning_prompt
        - deep_research_run
        - agent_run
        - long_context_digest
        - multimodal_analysis
        - batch_or_supplemental_API
        - validation_only
      required: true

    scarcity_class:
      type: string
      allowed:
        - abundant
        - limited
        - scarce
        - unknown
        - operator_reserved
      required: true

    expected_value_class:
      type: string
      allowed:
        - low
        - moderate
        - high
        - critical
      required: true

    high_end_reasoning_score:
      type: object_ref
      ref: high_end_reasoning_score
      required: false
      nullable: true

    planned_unit_estimate:
      type: object_ref
      ref: planned_unit_estimate
      required: false
      nullable: true

    reservation_id:
      type: string
      required: false
      nullable: true

    fallback_rule_ref:
      type: string
      required: false
      nullable: true

    planned_status:
      type: string
      allowed:
        - planned
        - planned_with_warning
        - operator_review_recommended
        - reserved
        - deferred
        - blocked_by_missing_quota_data
        - blocked_by_missing_operator_decision
      required: true

    operator_review_flags:
      type: list
      item_type: string
      required: false
```

## Schema: high_end_reasoning_score

```yaml
high_end_reasoning_score:
  type: object
  required:
    - impact
    - risk
    - evidence_need
    - ambiguity
    - total
    - high_end_reasoning_recommended

  fields:
    impact:
      type: integer
      min: 1
      max: 100
      required: true

    risk:
      type: integer
      min: 1
      max: 100
      required: true

    evidence_need:
      type: integer
      min: 1
      max: 100
      required: true

    ambiguity:
      type: integer
      min: 1
      max: 100
      required: true

    total:
      type: integer
      min: 4
      max: 400
      required: true
      meaning: "Sum of impact, risk, evidence_need, and ambiguity."

    high_end_reasoning_recommended:
      type: boolean
      required: true

    recommendation_basis:
      type: string
      allowed:
        - impact_threshold
        - risk_threshold
        - evidence_need_threshold
        - ambiguity_threshold
        - combined_score_threshold
        - operator_override
        - not_recommended
      required: false
```

## Schema: planned_unit_estimate

```yaml
planned_unit_estimate:
  type: object
  required:
    - estimate_type
    - estimate_confidence

  fields:
    estimate_type:
      type: string
      allowed:
        - prompt_count
        - run_count
        - session_count
        - token_or_credit_estimate
        - quota_unit_estimate
        - unknown
      required: true

    planned_units:
      type: number
      min: 0
      required: false
      nullable: true

    quota_unit_type:
      type: string
      allowed:
        - message
        - run
        - search
        - minute
        - token
        - credit
        - currency
        - operator_defined
        - unknown
      required: false

    estimate_confidence:
      type: string
      allowed:
        - high
        - moderate
        - low
        - unknown
      required: true

    estimate_note:
      type: string
      required: false
      max_words: 40
```

## Schema: scarce_mode_reservation

```yaml
scarce_mode_reservation:
  type: object
  required:
    - reservation_id
    - reserved_surface_class
    - reservation_purpose
    - reservation_status

  fields:
    reservation_id:
      type: string
      format: "scarce_mode_reservation_<short_slug>"
      required: true

    reserved_surface_class:
      type: string
      allowed:
        - frontier_deep_research
        - frontier_agent_run
        - high_end_reasoning_prompt
        - long_context_multimodal
        - operator_defined_scarce_mode
      required: true

    reservation_purpose:
      type: string
      allowed:
        - high_impact_flow
        - high_risk_decision
        - source_grounded_research
        - architecture_or_prompt_generation
        - validation_gate
        - operator_override
      required: true

    applies_to_refs:
      type: list
      item_type: string
      min_items: 1
      required: true

    reservation_limit:
      type: object_ref
      ref: planned_unit_estimate
      required: false
      nullable: true

    reservation_status:
      type: string
      allowed:
        - reserved
        - soft_reserved
        - suggested
        - released
        - blocked_by_unknown_quota
        - operator_review_recommended
      required: true

    release_rule:
      type: string
      required: false
      max_words: 60
```

## Schema: planned_usage_totals

```yaml
planned_usage_totals:
  type: object
  required:
    - total_entries
    - by_surface_class
    - by_usage_class
    - scarce_mode_summary

  fields:
    total_entries:
      type: integer
      min: 0
      required: true

    by_surface_class:
      type: list
      item_ref: planned_total_by_class
      required: true

    by_usage_class:
      type: list
      item_ref: planned_total_by_class
      required: true

    scarce_mode_summary:
      type: object_ref
      ref: scarce_mode_summary
      required: true

    quota_pressure_summary:
      type: string
      allowed:
        - no_pressure_detected
        - moderate_pressure
        - high_pressure
        - unknown_pressure
        - operator_review_recommended
      required: false
```

## Schema: planned_total_by_class

```yaml
planned_total_by_class:
  type: object
  required:
    - class_label
    - planned_entry_count

  fields:
    class_label:
      type: string
      required: true

    planned_entry_count:
      type: integer
      min: 0
      required: true

    planned_units:
      type: number
      min: 0
      required: false
      nullable: true

    scarcity_class:
      type: string
      allowed:
        - abundant
        - limited
        - scarce
        - unknown
        - mixed
      required: false
```

## Schema: scarce_mode_summary

```yaml
scarce_mode_summary:
  type: object
  required:
    - scarce_entries_count
    - reservations_count
    - operator_review_required

  fields:
    scarce_entries_count:
      type: integer
      min: 0
      required: true

    reservations_count:
      type: integer
      min: 0
      required: true

    operator_review_required:
      type: boolean
      required: true

    review_reason:
      type: string
      required: false
      max_words: 60
```

## Schema: budget_fallback_rule

```yaml
budget_fallback_rule:
  type: object
  required:
    - fallback_id
    - trigger
    - correction

  fields:
    fallback_id:
      type: string
      format: "budget_fallback_<short_slug>"
      required: true

    trigger:
      type: string
      required: true
      max_words: 40

    correction:
      type: string
      required: true
      max_words: 60

    fallback_surface_class:
      type: string
      allowed:
        - frontier_chat_subscription
        - supplemental_API_low_cost
        - local_or_free_tool
        - provider_unspecified
        - defer_to_operator
      required: false
```

## Planning Rules

```yaml
planned_usage_budget_rules:
  default_planning_order:
    1: read_or_create_monthly_quota_map_reference
    2: read_AI_surface_inventory_reference
    3: inspect_routing_decisions_if_available
    4: classify_each_planned_task_by_usage_class
    5: assign_scarcity_class_from_quota_map
    6: reserve_scarce_modes_for_high_impact_or_high_risk_tasks
    7: create_fallback_rules_for_unknown_or_scarce_quota
    8: mark_operator_review_flags_before_execution

  planned_flow_session_policy:
    quality_first_when:
      - expected_value_class_is_high_or_critical
      - impact_at_least_80
      - risk_at_least_70
      - evidence_need_at_least_70
      - ambiguity_at_least_70
    cost_is_secondary_when:
      - planned_work_is_core_daily_flow
      - output_feeds_PreCapNextDay_or_status_merge
      - error_cost_is_material

  supplemental_or_batch_policy:
    cost_efficiency_can_dominate_when:
      - task_is_low_risk
      - task_is_mechanical
      - quality_sufficient_threshold_is_clear
      - task_does_not_drive_operator_decision

  operator_override_policy:
    operator_can_force_route: true
    forced_route_must_be_recorded: true
    forced_route_must_not_silently_remove_review_flags: true
```

## Validation Rules

```yaml
planned_usage_budget_validation_rules:
  required_checks:
    budget_has_horizon: true
    budget_has_planning_context: true
    at_least_one_planned_usage_entry_exists: true
    every_entry_has_surface_class: true
    every_entry_has_usage_class: true
    every_entry_has_scarcity_class: true
    scarce_or_unknown_quota_entries_have_review_flags: true
    high_impact_tasks_have_high_end_reasoning_score_when_relevant: true
    fallback_rules_exist_for_blocked_or_unknown_quota: true
    planned_totals_are_present: true
    actual_usage_is_not_recorded_here: true
    current_prices_are_not_encoded: true
    exact_product_limits_are_not_encoded: true
    exact_model_rankings_are_not_encoded: true

  validation_status_rules:
    valid:
      rule: "All required fields are present, quota references are sufficient, and no blocking review flag remains."
    valid_with_warnings:
      rule: "The plan is usable but contains non-blocking unknowns or soft reservations."
    operator_review_recommended:
      rule: "Scarce, high-impact, high-risk, or ambiguous allocations need operator review before execution."
    low_confidence_auto_generated:
      rule: "The budget is inferred from partial or stale data and should not be treated as authoritative."
    blocked_by_missing_operator_decision:
      rule: "A route, quota, or scarce-mode choice cannot be resolved without operator input."
```

## Failure Modes

```yaml
planned_usage_budget_failure_modes:
  - trigger: "No quota map is available for the planned period."
    correction: "Create a budget with quota_unknown status, use conservative defaults, and mark operator_review_recommended."

  - trigger: "A planned task requests a scarce mode without impact or risk justification."
    correction: "Add a review flag and either request operator approval or route to a non-scarce fallback."

  - trigger: "The budget attempts to record actual usage after execution."
    correction: "Remove actual usage fields and direct actual consumption capture to usage_delta."

  - trigger: "The budget encodes current prices, exact limits, or model rankings."
    correction: "Remove volatile claims and reference operator-supplied or currently verified external quota data instead."

  - trigger: "A planned entry duplicates routing_decision schema fields in full."
    correction: "Replace duplicated route schema content with planned_route_ref and only keep budget-specific fields."

  - trigger: "All work is routed to the cheapest available surface despite high value or risk."
    correction: "Reclassify using planned_flow_session_policy and escalate high-impact work to operator review."

  - trigger: "The budget reserves scarce modes for too many tasks to be actionable."
    correction: "Rank reservations by expected value, release low-value reservations, and keep only the most leveraged scarce uses."

  - trigger: "The budget lacks fallback rules for unknown or blocked quota."
    correction: "Add explicit fallback rules before marking the budget valid."
```

## Minimal Example

```yaml
planned_usage_budget:
  budget_id: planned_usage_budget_apex_flow_f3
  created_or_updated_at: "YYYY-MM-DD"
  budget_horizon:
    horizon_type: single_flow
    starts_at: "YYYY-MM-DD"
    ends_at: "YYYY-MM-DD"
    flow_id: F3
    sprint_id: NA
  planning_context:
    context_type: PreCapNextDay_flow_prompt_pack
    source_artifact_refs:
      - flow_prompt_pack_F3
    budget_goal: use_monthly_quota_deliberately
    planning_assumption_status: quota_partially_known
  monthly_quota_map_ref: monthly_quota_map_current
  AI_surface_inventory_ref: AI_surface_inventory_current
  planned_usage_entries:
    - entry_id: planned_usage_entry_f3_prompt_generation
      planned_task_ref: prompt_sequence_f3_skill_generation
      planned_route_ref: routing_decision_f3_prompt_generation
      planned_surface_class: frontier_chat_subscription
      provider_target: Claude
      model_or_surface_target: Claude_Code_file_generation_surface
      planned_usage_class: high_end_reasoning_prompt
      scarcity_class: limited
      expected_value_class: high
      high_end_reasoning_score:
        impact: 85
        risk: 70
        evidence_need: 60
        ambiguity: 75
        total: 290
        high_end_reasoning_recommended: true
        recommendation_basis: combined_score_threshold
      planned_unit_estimate:
        estimate_type: prompt_count
        planned_units: 2
        quota_unit_type: message
        estimate_confidence: low
      planned_status: planned_with_warning
      operator_review_flags:
        - quota_estimate_low_confidence
  scarce_mode_reservations:
    - reservation_id: scarce_mode_reservation_f3_validation
      reserved_surface_class: high_end_reasoning_prompt
      reservation_purpose: architecture_or_prompt_generation
      applies_to_refs:
        - prompt_sequence_f3_skill_generation
      reservation_status: soft_reserved
  planned_usage_totals:
    total_entries: 1
    by_surface_class:
      - class_label: frontier_chat_subscription
        planned_entry_count: 1
        scarcity_class: limited
    by_usage_class:
      - class_label: high_end_reasoning_prompt
        planned_entry_count: 1
        scarcity_class: limited
    scarce_mode_summary:
      scarce_entries_count: 0
      reservations_count: 1
      operator_review_required: true
      review_reason: "Quota estimate is partial and reservation uses a high-value reasoning surface."
    quota_pressure_summary: unknown_pressure
  fallback_rules:
    - fallback_id: budget_fallback_quota_unknown
      trigger: "Quota data is too stale or incomplete to trust."
      correction: "Use provider_unspecified fallback or ask operator before consuming scarce mode."
      fallback_surface_class: defer_to_operator
  validation_status: operator_review_recommended
  operator_review_flags:
    - quota_estimate_low_confidence
    - scarce_mode_soft_reservation_needs_review
```

---

# VALIDATION - FILE-SPECIFIC CHECKS

- [ ] The file defines `planned_usage_budget` schema.
- [ ] The file defines budget horizon fields.
- [ ] The file defines planning context fields.
- [ ] The file defines per-task planned usage entries.
- [ ] The file defines scarce-mode reservations.
- [ ] The file defines planned usage totals.
- [ ] The file defines fallback budget rules.
- [ ] The file defines validation rules.
- [ ] The file defines failure modes.
- [ ] The file includes a minimal example.
- [ ] The file does not record actual usage; that belongs to `usage_delta`.
- [ ] The file does not duplicate `monthly_quota_map`, `AI_surface_inventory`, or `routing_decision` schema.
- [ ] The file does not claim current pricing, exact product limits, exact model rankings, or final OpenRouter model mapping.

---

# NEXT PROMPT

Paste this next:
> Prompt AR6: Create exactly one file. # FILE: .claude/skills/ai-routing-and-usage-tracking/references/usage-delta-contract.md File type: reference_contract. Schema ownership: owns usage_delta and actual usage capture after execution. Context carry-forward: load AR1, AR2, AR3, AR4, and AR5 outputs before writing. This file must define actual usage delta structure, planned-versus-actual comparison fields, FlowRecap capture interface, automated API log placeholder fields, validation statuses, failure modes, and minimal examples. Rules: Do not define planned usage budget schema. Do not define monthly quota map schema. Do not claim current pricing, exact product limits, exact model rankings, or final OpenRouter model mapping. Next prompt target: Prompt AR7.
