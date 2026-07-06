# APEX Minimal Model Usage Example

This is a synthetic APEX-only example for `model-usage-log`.

It shows one low-confidence usage candidate from a FlowRecap-like source, one `model_usage_delta`, and one mini `usage_summary`.

Rules shown by this example:

- Advisory only.
- No AIRouting package update.
- No quota-map mutation.
- No provider pricing claim.
- No current product-limit claim.
- Missing usage evidence degrades confidence but does not block FlowRecap, StatusMerge, or PreCapNextDay.

---

## 1. Synthetic Source Context

```yaml
synthetic_source_context:
  project: Apex
  execution_day: "2026-07-06"
  flow_id: F3
  flow_label: apex_skill_database_contract_work
  source_type: synthetic_flow_recap_usage_candidate
  advisory_only: true

  planned_usage_candidate:
    planned_usage_ref: "flow_prompt_pack_2026-07-06_F3.routing_usage_summary"
    planned_surface_or_route_label: subscription_frontier_reasoning
    planned_usage_intent: >
      Use a high-quality reasoning surface for creating a compact interface
      package contract and checking schema-boundary risks.
    scarcity_or_cost_note: "No verified quota or pricing data supplied."

  actual_usage_candidate:
    evidence_status: partial
    evidence_note: >
      Operator transcript indicates a reasoning model was used to create a
      package file, but exact provider, exact model, token count, and quota
      impact were not supplied.
    exact_model_supplied: false
    verified_quota_data_supplied: false
```

---

## 2. model_usage_delta

```yaml
model_usage_delta:
  usage_delta_id: model_usage_delta_2026-07-06_F3
  artifact_name: model_usage_delta
  execution_day: "2026-07-06"

  source_flow_recap_refs:
    - ref_id: synthetic_flow_recap_usage_candidate_2026-07-06_F3
      ref_type: operator_note
      note: "Synthetic low-confidence usage candidate for APEX interface work."

  planned_usage_refs:
    - ref_id: flow_prompt_pack_2026-07-06_F3.routing_usage_summary
      ref_type: flow_prompt_pack
      note: "Planned high-quality reasoning use for APEX contract work."

  actual_usage_evidence:
    evidence_status: partial
    evidence_refs:
      - synthetic_flow_recap_usage_candidate_2026-07-06_F3
    evidence_notes: >
      Usage was partially evidenced by the flow record, but exact provider,
      model name, token count, cost, and quota impact were not supplied.
    missing_evidence_reason: "Exact usage telemetry was not captured."

  model_or_surface_used:
    provider_or_surface_label: null
    stable_surface_class: provider_unspecified
    exact_model_name: null
    exact_model_name_source: null
    verification_status: unknown

  usage_purpose: review_or_audit

  planned_vs_actual_summary:
    planned_route_ref: flow_prompt_pack_2026-07-06_F3.routing_usage_summary
    planned_usage_intent: >
      High-quality reasoning surface for creating and boundary-checking a
      minimal APEX skill interface package.
    actual_usage_observed: >
      Reasoning work appears to have happened, but the concrete model or
      surface is not verified.
    comparison: insufficient_data
    operator_learning_note: >
      Future APEX flow prompts should ask the operator to capture the surface
      or model label manually when exact telemetry is unavailable.

  route_reuse_or_avoid_signal: insufficient_data
  route_signal_rationale: >
    The task appears suitable for a high-quality reasoning route, but the actual
    route evidence is too weak to produce a reuse recommendation.

  confidence:
    level: low
    confidence_flags:
      - exact_model_unknown
      - inferred_from_context_only
      - source_refs_incomplete
      - quota_or_pricing_not_verified
    review_note: >
      Advisory only. Do not use this as quota, pricing, provider, or exact-model
      truth.

  validation_status: low_confidence_auto_generated
```

---

## 3. Mini usage_summary

```yaml
usage_summary:
  summary_id: usage_summary_2026-07-06_apex_minimal
  artifact_name: usage_summary
  created_or_updated_at: "2026-07-06"

  covered_period:
    period_start: "2026-07-06"
    period_end: "2026-07-06"
    period_label: execution_day
    coverage_status: sparse

  usage_deltas_included:
    - ref_id: model_usage_delta_2026-07-06_F3
      ref_type: model_usage_delta
      note: "Low-confidence APEX skill-interface package usage delta."

  useful_routes: []

  routes_to_avoid: []

  scarcity_or_quota_notes:
    status: missing
    notes:
      - "No verified quota map was supplied."
      - "No pricing or remaining-limit claim is made."
    source_refs: []
    forbidden_inferences_observed: []

  next_PreCapNextDay_usage_context:
    context_status: sparse
    suggested_context_block: >
      APEX contract/package work may justify a high-quality reasoning surface,
      but recent actual usage evidence is incomplete. For the next PreCapNextDay,
      keep usage guidance advisory and ask the operator to capture the chosen
      model or surface label after execution.
    candidate_reuse_signals: []
    candidate_avoid_signals: []
    review_flags:
      - exact_model_unknown
      - quota_or_pricing_not_verified
      - insufficient_actual_usage_evidence
    missing_context_notes:
      - "No exact model label supplied."
      - "No verified quota or pricing data supplied."

  confidence:
    level: low
    confidence_flags:
      - some_actual_usage_evidence_missing
      - exact_models_unknown
      - quota_or_pricing_not_verified
      - source_refs_incomplete
    review_note: >
      Use as a planning hint only. Do not treat as AIRouting truth or quota-map
      truth.

  validation_status: low_confidence_auto_generated
```

---

## 4. Boundary Confirmation

```yaml
boundary_confirmation:
  output_is_advisory: true
  AIRouting_package_updated: false
  monthly_quota_map_mutated: false
  routing_recommendation_packet_redefined: false
  provider_pricing_claim_made: false
  current_product_limit_claim_made: false
  FlowRecap_blocked: false
  StatusMerge_blocked: false
  PreCapNextDay_blocked: false
```
