# Usage Summary Contract

```yaml
usage_summary_contract:
  artifact_name: usage_summary_contract
  file_role: model_usage_log_reference_contract
  package_path: ".claude/skills/model-usage-log/"
  purpose: >
    Define the minimal advisory usage_summary artifact that aggregates
    model_usage_delta records into compact future-planning context for
    PreCapNextDay, FlowRecap review, and operator usage reflection. This file
    does not define provider quotas, pricing truth, routing schemas, or runtime
    usage metering.

  ownership:
    owns:
      - usage_summary
      - usage_deltas_included
      - useful_routes
      - routes_to_avoid
      - scarcity_or_quota_notes
      - next_PreCapNextDay_usage_context
      - usage_confidence_flags
      - missing_usage_data_degraded_behavior
    must_not_own:
      - routing_recommendation_packet_schema
      - AI_surface_inventory_schema
      - monthly_quota_map_schema
      - provider_pricing_truth
      - current_product_limit_truth_without_verification
      - prompt_packet_schema
      - flow_recap_packet_schema
      - project_status_delta_schema
      - status_merge_packet_schema
      - project_kb_schema
      - runtime_usage_metering
      - automated_quota_tracking

  global_rules:
    advisory_only: true
    non_blocking_for_PreCapNextDay: true
    non_blocking_for_FlowRecap: true
    non_blocking_for_StatusMerge: true
    usable_with_zero_deltas: true
    missing_usage_evidence_degrades_confidence: true
    quota_or_pricing_claims_require_explicit_source: true
    route_schema_referenced_not_redefined: true
    no_runtime_metering_or_automation: true
```

## Schema: usage_summary

```yaml
usage_summary:
  type: object
  role: non_blocking_advisory_context_for_future_planning
  required:
    - summary_id
    - created_or_updated_at
    - covered_period
    - usage_deltas_included
    - useful_routes
    - routes_to_avoid
    - scarcity_or_quota_notes
    - next_PreCapNextDay_usage_context
    - confidence
    - validation_status

  fields:
    summary_id:
      type: string
      format: "usage_summary_<YYYY-MM-DD_or_period_slug>"
      required: true

    artifact_name:
      type: string
      const: usage_summary
      required: false

    created_or_updated_at:
      type: string
      format: "YYYY-MM-DD"
      required: true

    covered_period:
      type: object
      required: true
      fields:
        period_start:
          type: string
          format: "YYYY-MM-DD"
          required: false
        period_end:
          type: string
          format: "YYYY-MM-DD"
          required: false
        period_label:
          type: string
          required: true
          examples:
            - execution_day
            - planning_day
            - week_to_date
            - operator_defined
        coverage_status:
          type: string
          allowed:
            - complete_for_known_deltas
            - partial
            - sparse
            - empty
            - unknown
          required: true

    usage_deltas_included:
      type: list
      item_type: object_ref
      required: true
      min_items: 0
      note: >
        References to model_usage_delta records. A summary may be valid with an
        empty list when usage evidence is missing, but confidence must degrade.

    useful_routes:
      type: list
      item_type: object
      required: true
      min_items: 0
      fields:
        route_label:
          type: string
          required: true
        supporting_delta_refs:
          type: list
          item_type: object_ref
          required: false
        reason:
          type: string
          required: true
        reuse_guidance:
          type: string
          allowed:
            - reuse_route
            - use_for_similar_tasks
            - use_only_for_high_value_tasks
            - needs_more_evidence
          required: true
      note: >
        Route labels may use stable surface classes or operator-supplied names.
        Do not define routing_decision schema here.

    routes_to_avoid:
      type: list
      item_type: object
      required: true
      min_items: 0
      fields:
        route_label:
          type: string
          required: true
        supporting_delta_refs:
          type: list
          item_type: object_ref
          required: false
        reason:
          type: string
          required: true
        avoid_guidance:
          type: string
          allowed:
            - avoid_route
            - avoid_for_low_value_tasks
            - avoid_until_operator_review
            - insufficient_data_do_not_generalize
          required: true

    scarcity_or_quota_notes:
      type: object
      required: true
      fields:
        status:
          type: string
          allowed:
            - operator_supplied_current
            - verified_from_explicit_source
            - stale
            - partial
            - missing
            - unknown
          required: true
        notes:
          type: list
          item_type: string
          required: true
        source_refs:
          type: list
          item_type: object_ref
          required: false
        forbidden_inferences_observed:
          type: list
          item_type: string
          required: false
      rule: >
        Do not claim remaining quotas, exact provider pricing, product limits, or
        billing facts unless they are operator-supplied or explicitly verified.

    next_PreCapNextDay_usage_context:
      type: object
      required: true
      fields:
        context_status:
          type: string
          allowed:
            - ready
            - ready_with_warnings
            - sparse
            - missing
            - operator_review_needed
          required: true
        suggested_context_block:
          type: string
          required: true
          note: >
            Compact human-readable advisory block that PreCapNextDay may embed
            or reference without treating it as route authority.
        candidate_reuse_signals:
          type: list
          item_type: string
          required: false
        candidate_avoid_signals:
          type: list
          item_type: string
          required: false
        review_flags:
          type: list
          item_type: string
          required: false
        missing_context_notes:
          type: list
          item_type: string
          required: false
      rule: >
        This context informs future planning but must not block next_day_plan,
        FlowRecap, or StatusMerge when incomplete.

    confidence:
      type: object
      required: true
      fields:
        level:
          type: string
          allowed:
            - high
            - medium
            - low
            - unknown
          required: true
        confidence_flags:
          type: list
          item_type: string
          allowed:
            - no_model_usage_deltas
            - some_actual_usage_evidence_missing
            - planned_usage_refs_missing
            - exact_models_unknown
            - quota_or_pricing_not_verified
            - derived_from_operator_notes_only
            - source_refs_incomplete
            - stale_summary
          required: false
        review_note:
          type: string
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

## Aggregation Rules

```yaml
usage_summary_aggregation_rules:
  input_policy:
    preferred_inputs:
      - model_usage_delta
      - operator_usage_notes
      - planned_usage_refs
      - flow_recap_refs
    all_inputs_optional: true
    missing_inputs_do_not_block_summary: true

  route_signal_rollup:
    reuse_route:
      use_when:
        - one_or_more_deltas_support_successful_or_suitable_route
        - actual_usage_evidence_is_at_least_partial
      summary_destination: useful_routes
    avoid_route:
      use_when:
        - one_or_more_deltas_support_failed_or_wrong_route
        - operator_or_evidence_indicates_route_mismatch
      summary_destination: routes_to_avoid
    use_only_for_high_value_tasks:
      use_when:
        - route_helped_but_appears_scarce_expensive_or_attention_heavy
        - evidence_does_not_justify_default_use
      summary_destination: useful_routes
    insufficient_data:
      use_when:
        - actual_usage_evidence_missing_or_too_sparse
      summary_destination: next_PreCapNextDay_usage_context.review_flags
    operator_review_needed:
      use_when:
        - signal_conflict_or_high_impact_uncertainty_exists
      summary_destination: next_PreCapNextDay_usage_context.review_flags

  conflict_handling:
    same_route_has_reuse_and_avoid_signals:
      behavior: >
        Preserve both signals, explain the conflict, and set validation_status
        to operator_review_recommended.
    quota_notes_are_unverified:
      behavior: >
        Keep notes as operator context only, set confidence flag
        quota_or_pricing_not_verified, and do not infer remaining limits.
    no_deltas_available:
      behavior: >
        Produce an empty low-confidence summary with next_PreCapNextDay context
        stating that usage learning is unavailable.
```

## Degraded Behavior

```yaml
usage_summary_degraded_behavior:
  no_usage_deltas_available:
    output_required: true
    usage_deltas_included: []
    useful_routes: []
    routes_to_avoid: []
    confidence_level: low
    validation_status: low_confidence_auto_generated
    required_review_flag: no_model_usage_deltas
    next_PreCapNextDay_context_status: sparse

  partial_or_missing_actual_usage_evidence:
    output_required: true
    confidence_level: low
    validation_status: valid_with_warnings
    required_review_flag: some_actual_usage_evidence_missing

  stale_or_unverified_quota_notes:
    output_required: true
    confidence_level: low
    validation_status: operator_review_recommended
    forbidden_claims:
      - exact_provider_pricing
      - current_product_limit_truth
      - remaining_quota
      - billing_fact_without_source

  conflicting_route_signals:
    output_required: true
    confidence_level: medium
    validation_status: operator_review_recommended
    required_review_flag: route_signal_conflict_requires_operator_review
```

## Minimal Valid Object Skeleton

```yaml
usage_summary_minimal_skeleton:
  summary_id: "usage_summary_<YYYY-MM-DD_or_period_slug>"
  artifact_name: usage_summary
  created_or_updated_at: "YYYY-MM-DD"
  covered_period:
    period_label: operator_defined
    coverage_status: empty
  usage_deltas_included: []
  useful_routes: []
  routes_to_avoid: []
  scarcity_or_quota_notes:
    status: missing
    notes:
      - "No verified quota, pricing, or scarcity notes supplied."
  next_PreCapNextDay_usage_context:
    context_status: sparse
    suggested_context_block: >
      No reliable model-usage learning is available for the next PreCapNextDay.
      Treat future routing and scarcity decisions as advisory and request
      operator review for high-value or scarce-mode tasks.
    candidate_reuse_signals: []
    candidate_avoid_signals: []
    review_flags:
      - no_model_usage_deltas
  confidence:
    level: low
    confidence_flags:
      - no_model_usage_deltas
      - quota_or_pricing_not_verified
    review_note: "Advisory only; do not use as quota truth."
  validation_status: low_confidence_auto_generated
```

## Boundary Checks

```yaml
usage_summary_boundary_checks:
  does_not_block_future_planning: true
  does_not_define_routing_schema: true
  does_not_mutate_monthly_quota_map: true
  does_not_claim_unverified_pricing_or_limits: true
  does_not_execute_usage_tracking: true
  does_not_create_runtime_metering: true
  does_not_replace_AIRouting: true
  does_not_replace_FlowRecap_or_StatusMerge: true
```
