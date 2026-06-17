# FILE: .claude/skills/ai-routing-and-usage-tracking/references/monthly-quota-map-contract.md

# Monthly Quota Map Contract

## Contract

```yaml
monthly_quota_map_contract:
  artifact_name: monthly_quota_map
  file_role: ai_routing_usage_reference_contract
  purpose: >
    Define the minimum valid structure for monthly quota maps, quota windows,
    surface quota entries, scarcity classes, quota update rules, and validation
    requirements. This file supports planned AI usage decisions without owning
    routing decisions, planned usage budgets, usage deltas, current prices,
    exact product limits, or volatile provider claims.

  ownership:
    owns:
      - monthly_quota_map
      - quota_window
      - surface_quota_entry
      - quota_unit_type
      - quota_reset_policy
      - scarcity_class
      - quota_update_rules
      - quota_validation_rules
      - quota_review_flags
    must_not_own:
      - AI_surface_inventory_schema
      - routing_decision_schema
      - planned_usage_budget_schema
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
    exact_limits_must_be_operator_supplied_or_currently_verified: true
    pricing_must_not_be_encoded_here: true
    provider_rankings_must_not_be_encoded_here: true
    stale_quota_values_must_be_marked_for_review: true
```

## Schema: monthly_quota_map

```yaml
monthly_quota_map:
  type: object
  required:
    - map_id
    - created_or_updated_at
    - quota_period
    - quota_entries
    - scarcity_policy
    - validation_status

  fields:
    map_id:
      type: string
      format: "monthly_quota_map_<YYYY_MM>"
      required: true

    created_or_updated_at:
      type: string
      format: "YYYY-MM-DD"
      required: true

    quota_period:
      type: object_ref
      ref: quota_window
      required: true

    source_basis:
      type: string
      allowed:
        - operator_supplied
        - current_verified
        - estimated_from_prior_usage
        - unknown
      required: false

    quota_entries:
      type: list
      item_ref: surface_quota_entry
      min_items: 1
      required: true

    scarcity_policy:
      type: object_ref
      ref: scarcity_policy
      required: true

    quota_update_rules:
      type: object_ref
      ref: quota_update_rules
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

## Schema: quota_window

```yaml
quota_window:
  type: object
  required:
    - period_type
    - period_start
    - period_end
    - reset_policy

  fields:
    period_type:
      type: string
      allowed:
        - calendar_month
        - rolling_window
        - subscription_cycle
        - operator_defined
      required: true

    period_start:
      type: string
      format: "YYYY-MM-DD"
      required: true

    period_end:
      type: string
      format: "YYYY-MM-DD"
      required: true

    reset_policy:
      type: object_ref
      ref: quota_reset_policy
      required: true

    timezone:
      type: string
      required: false

    notes:
      type: string
      required: false
```

## Schema: quota_reset_policy

```yaml
quota_reset_policy:
  type: object
  required:
    - reset_type
    - reset_confidence

  fields:
    reset_type:
      type: string
      allowed:
        - fixed_calendar_date
        - rolling_reset
        - subscription_anniversary
        - manual_reset
        - unknown
      required: true

    reset_day:
      type: integer
      min: 1
      max: 31
      required: false

    reset_confidence:
      type: string
      allowed:
        - confirmed
        - likely
        - estimated
        - unknown
      required: true

    operator_review_required:
      type: boolean
      required: true
```

## Schema: surface_quota_entry

```yaml
surface_quota_entry:
  type: object
  required:
    - surface_id
    - provider_family
    - surface_class
    - quota_unit
    - quota_limit_status
    - scarcity_class
    - intended_use_policy
    - validation_status

  fields:
    surface_id:
      type: string
      required: true

    provider_family:
      type: string
      allowed:
        - ChatGPT
        - Claude
        - Gemini
        - OpenRouter_later
        - local_or_custom
        - provider_unspecified
      required: true

    surface_class:
      type: string
      allowed:
        - chat_surface
        - high_reasoning_surface
        - deep_research_surface
        - agent_run_surface
        - coding_surface
        - long_context_surface
        - visual_or_image_surface
        - API_surface
        - local_surface
        - unknown_surface
      required: true

    quota_unit:
      type: object_ref
      ref: quota_unit_type
      required: true

    quota_limit_status:
      type: string
      allowed:
        - known_current
        - operator_supplied
        - estimated
        - unlimited_for_planning
        - unknown
      required: true

    quota_limit_value:
      type: number
      min: 0
      required: false

    quota_used_value:
      type: number
      min: 0
      required: false

    quota_remaining_value:
      type: number
      min: 0
      required: false

    usage_estimation_confidence:
      type: string
      allowed:
        - confirmed
        - likely
        - estimated
        - unknown
      required: false

    scarcity_class:
      type: object_ref
      ref: scarcity_class
      required: true

    intended_use_policy:
      type: object_ref
      ref: intended_use_policy
      required: true

    review_cadence:
      type: string
      allowed:
        - daily_when_active
        - weekly
        - monthly
        - before_high_impact_use
        - operator_defined
      required: false

    stale_after_days:
      type: integer
      min: 1
      max: 90
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

## Schema: quota_unit_type

```yaml
quota_unit_type:
  type: object
  required:
    - unit_name
    - unit_grain

  fields:
    unit_name:
      type: string
      allowed:
        - messages
        - prompts
        - agent_runs
        - deep_research_runs
        - compute_minutes
        - tokens
        - credits
        - currency_budget
        - manual_counter
        - unknown
      required: true

    unit_grain:
      type: string
      allowed:
        - count
        - approximate_count
        - duration
        - token_volume
        - cost_budget
        - qualitative
        - unknown
      required: true

    measurement_note:
      type: string
      required: false
```

## Schema: scarcity_class

```yaml
scarcity_class:
  type: object
  required:
    - class_name
    - planning_meaning
    - default_use_rule

  fields:
    class_name:
      type: string
      allowed:
        - abundant
        - moderate
        - scarce
        - critical
        - unknown
      required: true

    planning_meaning:
      type: string
      required: true

    default_use_rule:
      type: string
      allowed:
        - use_freely_for_matching_tasks
        - use_normally_but_track
        - reserve_for_high_value_tasks
        - require_operator_review_before_use
        - do_not_use_until_verified
      required: true

    minimum_high_end_reasoning_score:
      type: integer
      min: 1
      max: 400
      required: false

    operator_override_allowed:
      type: boolean
      required: true
```

## Schema: scarcity_policy

```yaml
scarcity_policy:
  type: object
  required:
    - default_policy
    - class_rules
    - operator_override_policy

  fields:
    default_policy:
      type: string
      allowed:
        - deliberate_quota_utilization
        - conservative_quota_preservation
        - balanced_usage
        - operator_defined
      required: true

    class_rules:
      type: list
      item_ref: scarcity_class
      min_items: 4
      required: true

    operator_override_policy:
      type: string
      allowed:
        - operator_can_override_any_recommendation
        - operator_review_required_for_scarce_or_critical
        - operator_review_required_for_unknown
      required: true

    high_end_reasoning_score_reference:
      type: string
      allowed:
        - impact_risk_evidence_need_ambiguity
      required: false

    conflict_resolution_note:
      type: string
      allowed:
        - operator_decision_workflow_fit_prompt_quality_routing_cost
      required: true
```

## Schema: intended_use_policy

```yaml
intended_use_policy:
  type: object
  required:
    - allowed_use_classes
    - discouraged_use_classes
    - default_planning_role

  fields:
    allowed_use_classes:
      type: list
      item_type: string
      min_items: 1
      required: true

    discouraged_use_classes:
      type: list
      item_type: string
      required: false

    default_planning_role:
      type: string
      allowed:
        - primary_daily_flow_engine
        - high_impact_reasoning_reserve
        - deep_research_reserve
        - agent_run_reserve
        - supplemental_batch_engine
        - low_reasoning_cost_sensitive_support
        - fallback_only
        - unknown
      required: true

    notes:
      type: string
      required: false
```

## Quota Update Rules

```yaml
quota_update_rules:
  update_sources:
    allowed:
      - operator_manual_update
      - FlowRecap_usage_delta
      - automated_API_log_later
      - provider_dashboard_check
      - monthly_reset
      - estimate_correction

  update_policy:
    manual_operator_update_beats_estimate: true
    verified_provider_dashboard_beats_manual_memory: true
    FlowRecap_usage_delta_updates_planned_vs_actual_tracking: true
    automated_API_logs_later_may_update_API_surface_usage: true
    unknown_quota_must_not_be_treated_as_abundant: true
    stale_values_must_trigger_operator_review: true

  reset_policy:
    reset_only_when_period_boundary_or_operator_confirms: true
    do_not_silently_reset_unknown_cycles: true
    preserve_prior_period_summary_when_available: true

  correction_policy:
    if_usage_exceeds_limit:
      validation_status: operator_review_recommended
      action: "Mark quota entry inconsistent and request operator correction."
    if_limit_unknown:
      validation_status: low_confidence_auto_generated
      action: "Use conservative scarcity class until verified."
    if_reset_date_unknown:
      validation_status: operator_review_recommended
      action: "Flag reset_policy for operator review."
```

## Scarcity Classification Rules

```yaml
scarcity_classification_rules:
  default_classes:
    abundant:
      planning_meaning: "Enough remaining capacity for normal use without careful rationing."
      default_use_rule: use_freely_for_matching_tasks
      operator_override_allowed: true

    moderate:
      planning_meaning: "Useful capacity remains, but repeated high-cost use should be tracked."
      default_use_rule: use_normally_but_track
      operator_override_allowed: true

    scarce:
      planning_meaning: "Remaining capacity should be reserved for high-value tasks."
      default_use_rule: reserve_for_high_value_tasks
      minimum_high_end_reasoning_score: 240
      operator_override_allowed: true

    critical:
      planning_meaning: "Remaining capacity is low or strategically important."
      default_use_rule: require_operator_review_before_use
      minimum_high_end_reasoning_score: 300
      operator_override_allowed: true

    unknown:
      planning_meaning: "Quota state is not reliable enough for automatic routing assumptions."
      default_use_rule: do_not_use_until_verified
      operator_override_allowed: true

  classification_inputs:
    - quota_remaining_value
    - quota_limit_value
    - usage_estimation_confidence
    - reset_policy
    - operator_supplied_priority
    - surface_planning_role

  important_rules:
    - "Known high remaining capacity may be abundant or moderate."
    - "Unknown capacity is never abundant by default."
    - "Scarce high-end surfaces should be proposed for high-impact work, not hoarded indefinitely."
    - "Cost and scarcity do not override operator decision, workflow fit, or prompt quality."
```

## Cross-Package Interface Notes

```yaml
cross_package_interface_notes:
  consumed_by:
    - routing_decision_contract
    - planned_usage_budget_contract
    - routing_recommendation_packet_contract
    - PreCapNextDay_usage_tracking_plan

  expects_from_AI_surface_inventory:
    - surface_id
    - provider_family
    - surface_class
    - access_mode
    - capability_tags

  may_receive_from_usage_delta:
    - actual_surface_used
    - actual_unit_count
    - usage_confidence
    - usage_notes

  provides_to_routing_decision:
    - scarcity_class
    - quota_remaining_value
    - quota_limit_status
    - intended_use_policy
    - review_flags

  does_not_decide:
    - final_provider_choice
    - final_model_choice
    - prompt_quality
    - workflow_stage_fit
```

## Validation Rules

```yaml
quota_validation_rules:
  required_checks:
    monthly_quota_map_has_period: true
    every_quota_entry_has_surface_id: true
    every_quota_entry_has_surface_class: true
    every_quota_entry_has_quota_unit: true
    every_quota_entry_has_scarcity_class: true
    unknown_limits_are_flagged: true
    stale_values_are_flagged: true
    volatile_limits_are_not_hardcoded_as_doctrine: true
    pricing_is_not_encoded: true
    routing_decision_schema_is_not_redefined: true

  validation_status_rules:
    valid:
      use_when: "All required fields are present, current enough, and internally consistent."
    valid_with_warnings:
      use_when: "Minor uncertainty exists but planning use remains safe."
    operator_review_recommended:
      use_when: "Quota limit, reset window, or scarcity class may materially affect routing."
    low_confidence_auto_generated:
      use_when: "Quota values are estimated or mostly unknown."
    blocked_by_missing_operator_decision:
      use_when: "A required operator quota policy decision is missing."
```

## Failure Modes

```yaml
quota_failure_modes:
  - trigger: "A quota entry has no surface_id."
    correction: "Mark validation_status as blocked_by_missing_operator_decision and request or infer only a placeholder surface reference."

  - trigger: "A quota limit is unknown but the surface is marked abundant."
    correction: "Change scarcity_class to unknown and add operator_review_flags."

  - trigger: "Quota values encode exact provider limits without verification basis."
    correction: "Mark quota_limit_status as estimated or unknown and require current verification before high-impact routing use."

  - trigger: "Pricing or exact cost tables appear in the quota map."
    correction: "Remove pricing data and defer cost class handling to cost-class and scarcity rules."

  - trigger: "The map attempts to choose the final provider or model."
    correction: "Move that decision to routing_decision and keep only quota constraints here."

  - trigger: "Usage has been updated from memory but not tied to a source."
    correction: "Set source_basis to estimated_from_prior_usage and mark validation_status as valid_with_warnings or low_confidence_auto_generated."

  - trigger: "The reset date or period boundary is ambiguous."
    correction: "Set reset_confidence to unknown and flag reset_policy for operator review."

  - trigger: "A scarce surface is never recommended even for high-impact tasks."
    correction: "Apply deliberate_quota_utilization policy and allow recommendation when score and operator intent justify it."
```

## Minimal Example

```yaml
monthly_quota_map_example:
  map_id: monthly_quota_map_2026_06
  created_or_updated_at: "2026-06-16"
  quota_period:
    period_type: calendar_month
    period_start: "2026-06-01"
    period_end: "2026-06-30"
    reset_policy:
      reset_type: unknown
      reset_confidence: unknown
      operator_review_required: true
    timezone: Europe/Berlin
  source_basis: operator_supplied
  quota_entries:
    - surface_id: high_reasoning_subscription_surface
      provider_family: provider_unspecified
      surface_class: high_reasoning_surface
      quota_unit:
        unit_name: messages
        unit_grain: approximate_count
        measurement_note: "Operator-maintained planning estimate only."
      quota_limit_status: unknown
      usage_estimation_confidence: estimated
      scarcity_class:
        class_name: unknown
        planning_meaning: "Capacity is not reliable enough for automatic assumptions."
        default_use_rule: do_not_use_until_verified
        operator_override_allowed: true
      intended_use_policy:
        allowed_use_classes:
          - high_impact_reasoning
          - architecture_decision
          - prompt_system_validation
        discouraged_use_classes:
          - low_value_batch_generation
          - rote_formatting
        default_planning_role: high_impact_reasoning_reserve
      review_cadence: before_high_impact_use
      stale_after_days: 14
      validation_status: low_confidence_auto_generated
      operator_review_flags:
        - quota_limit_unknown
        - reset_policy_unknown
  scarcity_policy:
    default_policy: deliberate_quota_utilization
    class_rules:
      - class_name: abundant
        planning_meaning: "Normal use is acceptable."
        default_use_rule: use_freely_for_matching_tasks
        operator_override_allowed: true
      - class_name: moderate
        planning_meaning: "Use normally but track repeated use."
        default_use_rule: use_normally_but_track
        operator_override_allowed: true
      - class_name: scarce
        planning_meaning: "Reserve for high-value tasks."
        default_use_rule: reserve_for_high_value_tasks
        minimum_high_end_reasoning_score: 240
        operator_override_allowed: true
      - class_name: critical
        planning_meaning: "Use only with operator review."
        default_use_rule: require_operator_review_before_use
        minimum_high_end_reasoning_score: 300
        operator_override_allowed: true
      - class_name: unknown
        planning_meaning: "Verify before relying on this surface."
        default_use_rule: do_not_use_until_verified
        operator_override_allowed: true
    operator_override_policy: operator_review_required_for_scarce_or_critical
    high_end_reasoning_score_reference: impact_risk_evidence_need_ambiguity
    conflict_resolution_note: operator_decision_workflow_fit_prompt_quality_routing_cost
  validation_status: low_confidence_auto_generated
  operator_review_flags:
    - current_limits_need_verification
```

---

# VALIDATION - FILE-SPECIFIC CHECKS

- [ ] File defines the `monthly_quota_map` contract.
- [ ] File defines `quota_window`, `quota_reset_policy`, and `surface_quota_entry`.
- [ ] File defines quota units without hardcoding current product limits.
- [ ] File defines scarcity classes and deliberate quota utilization policy.
- [ ] File defines update rules for operator updates, FlowRecap usage deltas, future API logs, and reset handling.
- [ ] File includes validation rules and failure modes.
- [ ] File includes a minimal example.
- [ ] File does not define routing-decision schema.
- [ ] File does not define planned-usage-budget schema.
- [ ] File does not define usage-delta schema.
- [ ] File does not encode current pricing, exact product limits, exact model rankings, or final OpenRouter mapping.

---

# NEXT PROMPT

Paste this next:
> Prompt AR4:
> Create exactly one file.
>
> # FILE: .claude/skills/ai-routing-and-usage-tracking/references/routing-decision-contract.md
>
> File type: contract.
> Schema ownership: owns routing_decision schema and routing rationale fields.
> Context carry-forward: load AR1, AR2, and AR3 outputs before writing.
>
> This file must define:
> - routing_decision schema
> - route surface classes
> - model or surface target fields
> - provider rationale fields
> - quota rationale fields
> - fallback rule fields
> - operator override fields
> - validation statuses
> - failure modes
> - minimal example
>
> Rules:
> - Use stable surface classes, not volatile model claims.
> - Do not claim current pricing, exact model rankings, or exact product limits.
> - Do not duplicate AI_surface_inventory schema.
> - Do not duplicate monthly_quota_map schema.
> - Do not define planned_usage_budget schema.
> - Keep OpenRouter model mapping as later/TODO only.
>
> Next prompt target: Prompt AR5.
