# FILE: .claude/skills/ai-routing-and-usage-tracking/references/routing-decision-contract.md

# Routing Decision Contract

## Contract

```yaml
routing_decision_contract:
  artifact_name: routing_decision
  file_role: ai_routing_reference_contract
  purpose: >
    Define the minimum valid structure for a routing_decision, including
    stable surface selection, model_or_surface_target fields, provider
    rationale, quota rationale, fallback rules, operator overrides,
    validation statuses, failure modes, and a minimal example. This file owns
    routing_decision schema only and references AI_surface_inventory and
    monthly_quota_map instead of duplicating them.

  ownership:
    owns:
      - routing_decision
      - route_surface_class_field
      - model_or_surface_target_field
      - provider_rationale
      - quota_rationale
      - fallback_rule
      - operator_override
      - routing_decision_validation_rules
      - routing_decision_failure_modes
      - routing_decision_minimal_example
    must_not_own:
      - AI_surface_inventory_schema
      - monthly_quota_map_schema
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
    stable_surface_classes_only: true
    exact_model_claims_require_current_verification: true
    current_pricing_forbidden: true
    exact_product_limits_forbidden: true
    OpenRouter_model_mapping_status: todo_later
```

## Schema: routing_decision

```yaml
routing_decision:
  type: object
  required:
    - decision_id
    - created_or_updated_at
    - routing_mode
    - task_risk_profile
    - primary_route
    - provider_rationale
    - quota_rationale
    - fallback_rule
    - validation_status

  fields:
    decision_id:
      type: string
      format: "routing_decision_<short_slug>"
      required: true

    created_or_updated_at:
      type: string
      format: "YYYY-MM-DD"
      required: true

    source_packet_id:
      type: string
      required: false
      nullable: true
      meaning: "Optional prompt_packet, prompt_sequence, flow_packet, or operator_task identifier used as routing input."

    routing_mode:
      type: string
      allowed:
        - planned_flow_session
        - supplemental_or_batch_execution
        - operator_directed_route
        - validation_only_route
        - blocked_route
      required: true

    routing_intent:
      type: string
      allowed:
        - maximize_quality
        - balance_quality_and_cost
        - minimize_cost_when_quality_sufficient
        - preserve_scarce_quota
        - use_operator_selected_surface
        - defer_until_verified
      required: false

    task_summary:
      type: string
      required: false
      max_words: 40

    task_risk_profile:
      type: object_ref
      ref: task_risk_profile
      required: true

    primary_route:
      type: object_ref
      ref: route_target
      required: true

    alternate_route:
      type: object_ref
      ref: route_target
      required: false
      nullable: true

    provider_rationale:
      type: object_ref
      ref: provider_rationale
      required: true

    quota_rationale:
      type: object_ref
      ref: quota_rationale
      required: true

    fallback_rule:
      type: object_ref
      ref: fallback_rule
      required: true

    operator_override:
      type: object_ref
      ref: operator_override
      required: false
      nullable: true

    expected_usage_capture:
      type: object_ref
      ref: expected_usage_capture
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

## Schema: task_risk_profile

```yaml
task_risk_profile:
  type: object
  required:
    - impact
    - risk
    - evidence_need
    - ambiguity
    - high_end_reasoning_score_total
    - route_sensitivity

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

    high_end_reasoning_score_total:
      type: integer
      min: 4
      max: 400
      required: true
      meaning: "Sum of impact, risk, evidence_need, and ambiguity."

    route_sensitivity:
      type: string
      allowed:
        - low
        - moderate
        - high
        - critical
      required: true

    risk_notes:
      type: list
      item_type: string
      max_items: 5
      required: false
```

## Schema: route_target

```yaml
route_target:
  type: object
  required:
    - route_role
    - route_surface_class
    - provider_family
    - model_or_surface_target
    - target_specificity
    - cost_class
    - scarcity_class
    - fit_confidence

  fields:
    route_role:
      type: string
      allowed:
        - primary
        - alternate
        - fallback
        - blocked
      required: true

    route_surface_class:
      type: string
      allowed_ref: "AI_surface_inventory.surface_class_taxonomy.allowed"
      allowed_stable_examples:
        - frontier_subscription_chat
        - frontier_subscription_agent
        - frontier_deep_research
        - frontier_code_agent
        - long_context_subscription_chat
        - supplemental_api
        - low_cost_batch_api
        - local_or_offline_tool
        - manual_operator_surface
        - operator_defined
      required: true

    provider_family:
      type: string
      allowed_ref: "AI_surface_inventory.provider_family_taxonomy.allowed"
      allowed_stable_examples:
        - ChatGPT
        - Claude
        - Gemini
        - OpenRouter_later
        - local_tool
        - manual_operator
        - provider_unspecified
        - operator_defined
      required: true

    model_or_surface_target:
      type: object_ref
      ref: model_or_surface_target
      required: true

    access_mode:
      type: string
      allowed_ref: "AI_surface_inventory.access_mode_taxonomy.allowed"
      required: false

    cost_class:
      type: string
      allowed:
        - no_incremental_cost_subscription
        - scarce_subscription_quota
        - API_metered_low
        - API_metered_medium
        - API_metered_high
        - local_no_provider_cost
        - manual_operator_time
        - unknown_requires_verification
      required: true

    scarcity_class:
      type: string
      allowed:
        - abundant
        - limited
        - scarce
        - critical
        - manual_only
        - unknown_requires_verification
      required: true

    fit_confidence:
      type: string
      allowed:
        - high
        - medium
        - low
        - unknown
      required: true

    route_constraints:
      type: list
      item_type: string
      max_items: 8
      required: false
```

## Schema: model_or_surface_target

```yaml
model_or_surface_target:
  type: object
  required:
    - target_kind
    - target_label
    - target_verification_status

  fields:
    target_kind:
      type: string
      allowed:
        - surface_class_only
        - provider_family
        - operator_named_surface
        - currently_verified_model
        - local_tool
        - manual_operator_action
        - unknown_requires_verification
      required: true

    target_label:
      type: string
      required: true
      meaning: "Human-readable target label. Use stable surface class or operator-supplied label when exact model details are not verified."

    target_id:
      type: string
      required: false
      nullable: true
      meaning: "Optional link to AI_surface_inventory.surface_id when available."

    target_specificity:
      type: string
      allowed:
        - surface_class
        - provider_family
        - named_surface
        - exact_model_verified_current
        - exact_model_unverified_operator_supplied
        - unknown
      required: true

    target_verification_status:
      type: string
      allowed:
        - verified_current
        - operator_supplied_unverified
        - stale_requires_review
        - not_verified
        - volatile_claim_removed
        - blocked_by_missing_operator_decision
      required: true

    volatile_claims_removed:
      type: boolean
      required: false

    notes:
      type: string
      required: false
```

## Schema: provider_rationale

```yaml
provider_rationale:
  type: object
  required:
    - selected_because
    - quality_reason
    - task_fit_reason
    - known_limitations

  fields:
    selected_because:
      type: string
      required: true
      max_words: 50

    quality_reason:
      type: string
      required: true
      max_words: 50

    task_fit_reason:
      type: string
      required: true
      max_words: 50

    workflow_fit_reason:
      type: string
      required: false
      max_words: 50

    prompt_fit_reason:
      type: string
      required: false
      max_words: 50

    known_limitations:
      type: list
      item_type: string
      max_items: 5
      required: true

    volatile_claims:
      type: string
      allowed:
        - none_used
        - removed
        - operator_supplied_unverified
        - requires_current_verification
      required: false
```

## Schema: quota_rationale

```yaml
quota_rationale:
  type: object
  required:
    - quota_context_status
    - scarcity_interpretation
    - use_policy
    - quota_tradeoff

  fields:
    quota_context_status:
      type: string
      allowed:
        - quota_map_available
        - quota_map_missing
        - quota_map_stale
        - quota_not_relevant
        - operator_review_required
      required: true

    scarcity_interpretation:
      type: string
      allowed:
        - abundant_or_subscription_normal_use
        - limited_track_usage
        - scarce_use_deliberately
        - critical_require_operator_review
        - unknown_verify_first
        - manual_operator_time_only
      required: true

    use_policy:
      type: string
      allowed:
        - use_freely_when_fit_is_good
        - use_normally_but_track
        - use_deliberately_for_high_value_work
        - reserve_for_high_impact_high_risk_work
        - require_operator_review_before_use
        - avoid_until_verified
        - operator_decision_required
      required: true

    scarce_mode_allowed:
      type: boolean
      required: true

    scarce_mode_reason:
      type: string
      required: false
      max_words: 50

    quota_tradeoff:
      type: string
      required: true
      max_words: 60

    quota_review_flags:
      type: list
      item_type: string
      max_items: 8
      required: false
```

## Schema: fallback_rule

```yaml
fallback_rule:
  type: object
  required:
    - fallback_required
    - fallback_condition
    - fallback_surface_class
    - fallback_behavior

  fields:
    fallback_required:
      type: boolean
      required: true

    fallback_condition:
      type: string
      allowed:
        - primary_surface_unavailable
        - quota_too_scarce
        - operator_declines_scarce_mode
        - current_verification_fails
        - output_quality_insufficient
        - task_risk_reclassified
        - no_fallback_needed
      required: true

    fallback_surface_class:
      type: string
      allowed_ref: "AI_surface_inventory.surface_class_taxonomy.allowed"
      required: true

    fallback_provider_family:
      type: string
      allowed_ref: "AI_surface_inventory.provider_family_taxonomy.allowed"
      required: false

    fallback_behavior:
      type: string
      allowed:
        - reroute_to_next_best_surface
        - use_lower_cost_surface_with_warning
        - ask_operator_for_surface_choice
        - block_until_current_verification
        - split_task_into_high_and_low_reasoning_parts
        - proceed_without_fallback
      required: true

    fallback_notes:
      type: list
      item_type: string
      max_items: 5
      required: false
```

## Schema: operator_override

```yaml
operator_override:
  type: object
  required:
    - override_present
    - override_type
    - override_effect

  fields:
    override_present:
      type: boolean
      required: true

    override_type:
      type: string
      allowed:
        - force_provider_family
        - force_surface_class
        - force_low_cost
        - force_high_quality
        - reserve_quota
        - allow_scarce_mode
        - block_route
        - none
      required: true

    override_reason:
      type: string
      required: false
      max_words: 60

    override_effect:
      type: string
      allowed:
        - replaces_auto_route
        - constrains_auto_route
        - confirms_auto_route
        - blocks_auto_route
        - no_effect
      required: true

    conflict_with_recommendation:
      type: boolean
      required: false

    conflict_note:
      type: string
      required: false
      max_words: 60
```

## Schema: expected_usage_capture

```yaml
expected_usage_capture:
  type: object
  required:
    - capture_required
    - capture_destination
    - capture_fields

  fields:
    capture_required:
      type: boolean
      required: true

    capture_destination:
      type: string
      allowed:
        - FlowRecap
        - usage_delta
        - automated_API_logs_later
        - operator_manual_note
        - none
      required: true

    capture_fields:
      type: list
      item_type: string
      allowed_items:
        - provider_family
        - route_surface_class
        - surface_id
        - model_or_surface_target
        - usage_unit
        - estimated_units
        - actual_units
        - result_quality
        - reroute_used
        - quota_pressure_after_use
      required: true

    learning_note:
      type: string
      required: false
      max_words: 60
```

## Route Selection Rules

```yaml
route_selection_rules:
  authority_order:
    1: operator_decision_from_tradeoff_card
    2: workflow_process_fit
    3: prompt_quality
    4: ai_routing_cost_or_efficiency

  planned_flow_session:
    priority_order:
      - quality
      - impact
      - risk_control
      - weekly_plan_alignment
      - cost
    route_rule: "Use stronger reasoning surfaces when impact, risk, evidence_need, or ambiguity are high."

  supplemental_or_batch_execution:
    priority_order:
      - leverage_weighted_quality
      - sufficient_surface_fit
      - cost_efficiency
      - speed
      - risk_control
    route_rule: "Use low-cost or batch surfaces when quality suffices and downside risk is low."

  high_end_reasoning_guidance:
    consider_high_end_when_any:
      - impact_gte_80
      - risk_gte_70
      - evidence_need_gte_70
      - ambiguity_gte_70
      - high_end_reasoning_score_total_gte_260
    require_operator_review_when:
      - scarcity_class_is_critical
      - quota_context_is_unknown_and_surface_is_scarce
      - operator_override_conflicts_with_high_risk_route

  OpenRouter_policy:
    status: todo_later
    allowed_use_now: supplemental_api_or_low_cost_batch_api_only_when_operator_supplied
    forbidden_now:
      - final_model_map
      - exact_provider_ranking
      - exact_pricing_claim
      - default_daily_frontier_engine
```

## Validation Rules

```yaml
routing_decision_validation_rules:
  required_checks:
    decision_id_present: true
    routing_mode_allowed: true
    task_risk_profile_complete: true
    primary_route_complete: true
    provider_rationale_present: true
    quota_rationale_present: true
    fallback_rule_present: true
    validation_status_allowed: true
    no_current_pricing_claims: true
    no_exact_product_limit_claims: true
    no_exact_model_rankings: true
    no_final_OpenRouter_model_mapping: true

  review_flag_conditions:
    - AI_surface_inventory_missing
    - monthly_quota_map_missing_or_stale
    - target_verification_status_not_verified
    - scarcity_class_unknown_or_critical
    - operator_override_conflicts_with_recommendation
    - fallback_rule_absent_or_unusable
    - volatile_claim_requires_current_verification
    - workflow_or_prompt_fit_conflict

  pass_conditions:
    valid: "All required checks pass and no unresolved review flags affect the route."
    valid_with_warnings: "Required fields pass but non-blocking review flags remain."
    operator_review_recommended: "A human choice materially affects route quality, cost, scarcity, or risk."
    low_confidence_auto_generated: "Inventory, quota, or target verification is missing but a safe abstract route can be suggested."
    blocked_by_missing_operator_decision: "The route requires an operator choice before proceeding."
```

## Failure Modes

```yaml
failure_modes:
  missing_inventory_match:
    trigger: "No AI_surface_inventory record matches the intended route."
    correction: "Use a stable abstract route_surface_class, set target_verification_status to not_verified, and mark validation_status as low_confidence_auto_generated."

  missing_or_stale_quota_context:
    trigger: "The route depends on scarce quota but monthly_quota_map is missing, stale, or unclear."
    correction: "Keep the route abstract, add quota review flags, and mark operator_review_recommended unless the task is low risk."

  volatile_model_claim_detected:
    trigger: "The routing decision includes current pricing, exact product limits, exact model rankings, or unverified availability."
    correction: "Remove the volatile claim and replace it with a verification requirement or stable surface class."

  cost_overrides_high_value_quality:
    trigger: "A low-cost route is selected for high impact, high risk, high evidence need, or high ambiguity work without rationale."
    correction: "Re-evaluate under planned_flow_session priority order and surface the tradeoff to the operator."

  fallback_rule_missing:
    trigger: "The primary route may fail or be unavailable but no fallback rule is defined."
    correction: "Add fallback_rule with a stable fallback_surface_class and a clear fallback_condition."

  operator_override_unexplained:
    trigger: "An operator override changes the route but has no override_reason or conflict note."
    correction: "Preserve the override, request or mark the missing reason, and flag any conflict with workflow fit, prompt quality, or cost."

  OpenRouter_mapping_finalized:
    trigger: "The routing decision attempts to encode a final OpenRouter model map or exact provider ranking."
    correction: "Replace with OpenRouter_later and restrict use to supplemental or low-cost batch API pending later verification."

  route_scope_creep:
    trigger: "The routing decision starts defining prompt bodies, planned usage budgets, usage deltas, workflow taxonomies, or project plans."
    correction: "Remove the non-owned content and reference the owning contract or skill package instead."
```

## Minimal Example

```yaml
routing_decision_example:
  decision_id: routing_decision_apex_skill_contract_review
  created_or_updated_at: "2026-06-16"
  source_packet_id: prompt_packet_apex_skill_contract_review
  routing_mode: planned_flow_session
  routing_intent: maximize_quality
  task_summary: "Review and improve a Claude skill package contract before operator use."
  task_risk_profile:
    impact: 85
    risk: 70
    evidence_need: 55
    ambiguity: 60
    high_end_reasoning_score_total: 270
    route_sensitivity: high
    risk_notes:
      - contract_drift_would_affect_downstream_skill_quality
      - source_fidelity_and_schema_ownership_matter
  primary_route:
    route_role: primary
    route_surface_class: frontier_subscription_chat
    provider_family: Claude
    model_or_surface_target:
      target_kind: surface_class_only
      target_label: "Claude subscription chat or extended reasoning surface"
      target_id: null
      target_specificity: surface_class
      target_verification_status: operator_supplied_unverified
      volatile_claims_removed: true
    access_mode: chat_ui
    cost_class: scarce_subscription_quota
    scarcity_class: limited
    fit_confidence: medium
    route_constraints:
      - preserve_schema_ownership
      - do_not_finalize_volatile_model_claims
  alternate_route:
    route_role: alternate
    route_surface_class: frontier_subscription_chat
    provider_family: ChatGPT
    model_or_surface_target:
      target_kind: surface_class_only
      target_label: "ChatGPT high-reasoning chat surface"
      target_id: null
      target_specificity: surface_class
      target_verification_status: operator_supplied_unverified
      volatile_claims_removed: true
    access_mode: chat_ui
    cost_class: scarce_subscription_quota
    scarcity_class: limited
    fit_confidence: medium
  provider_rationale:
    selected_because: "The task needs careful contract reasoning and semantic fidelity."
    quality_reason: "A frontier subscription chat surface is appropriate for high-impact schema work."
    task_fit_reason: "The task is structured review and artifact generation rather than bulk transformation."
    workflow_fit_reason: "The route supports workflow/process correctness before downstream planning."
    prompt_fit_reason: "The route can preserve strict output-contract constraints."
    known_limitations:
      - exact_current_model_rank_not_claimed
      - current_quota_remaining_unknown
    volatile_claims: removed
  quota_rationale:
    quota_context_status: quota_map_missing
    scarcity_interpretation: scarce_use_deliberately
    use_policy: use_deliberately_for_high_value_work
    scarce_mode_allowed: true
    scarce_mode_reason: "The artifact is high leverage for later skill-package generation."
    quota_tradeoff: "Use a stronger route now to reduce downstream repair cost."
    quota_review_flags:
      - current_remaining_quota_unknown
  fallback_rule:
    fallback_required: true
    fallback_condition: quota_too_scarce
    fallback_surface_class: supplemental_api
    fallback_provider_family: OpenRouter_later
    fallback_behavior: split_task_into_high_and_low_reasoning_parts
    fallback_notes:
      - keep_final_review_on_frontier_subscription_surface
      - use_supplemental_api_only_for_low_risk_subtasks
  operator_override:
    override_present: false
    override_type: none
    override_effect: no_effect
  expected_usage_capture:
    capture_required: true
    capture_destination: FlowRecap
    capture_fields:
      - provider_family
      - route_surface_class
      - model_or_surface_target
      - result_quality
      - reroute_used
      - quota_pressure_after_use
    learning_note: "Compare whether high-end routing reduced later correction work."
  validation_status: operator_review_recommended
  operator_review_flags:
    - monthly_quota_map_missing
    - target_verification_status_not_verified
```

---

# VALIDATION - FILE-SPECIFIC CHECKS

- [ ] File defines the `routing_decision` schema.
- [ ] File defines route surface class fields by reference to AI_surface_inventory instead of duplicating its schema.
- [ ] File defines model_or_surface_target fields without making volatile model claims.
- [ ] File defines provider_rationale fields.
- [ ] File defines quota_rationale fields without duplicating monthly_quota_map schema.
- [ ] File defines fallback_rule fields.
- [ ] File defines operator_override fields.
- [ ] File defines validation statuses and review flag conditions.
- [ ] File defines failure modes and corrections.
- [ ] File includes a minimal example.
- [ ] File does not define planned_usage_budget schema.
- [ ] File does not claim current pricing, exact model rankings, exact product limits, or final OpenRouter mapping.

---

# NEXT PROMPT

Paste this next:
> Prompt AR5:
> Create exactly one file.
>
> # FILE: .claude/skills/ai-routing-and-usage-tracking/references/planned-usage-budget-contract.md
>
> File type: contract.
> Schema ownership: owns planned_usage_budget schema and usage planning fields.
> Context carry-forward: load AR1, AR2, AR3, and AR4 outputs before writing.
>
> This file must define:
> - planned_usage_budget schema
> - daily and flow-level planned usage fields
> - expected quota pressure fields
> - scarce mode allocation fields
> - high_end_reasoning_score budget use
> - capture requirements for later usage_delta
> - operator review flags
> - validation statuses
> - failure modes
> - minimal example
>
> Rules:
> - Use stable surface classes, not volatile model claims.
> - Do not claim current pricing, exact model rankings, or exact product limits.
> - Do not duplicate AI_surface_inventory schema.
> - Do not duplicate monthly_quota_map schema.
> - Do not duplicate routing_decision schema.
> - Keep OpenRouter model mapping as later/TODO only.
>
> Next prompt target: Prompt AR6.
