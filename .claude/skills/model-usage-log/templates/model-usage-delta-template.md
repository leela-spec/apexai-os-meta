# Model Usage Delta Template

Use this template to create one compact advisory `model_usage_delta` after an APEX flow has usage evidence or an explicit note that evidence is missing.

This artifact is advisory only. It must not stop FlowRecap, StatusMerge, PreCapNextDay, or operator execution.

---

## 1. Delta Status

```yaml
model_usage_delta_header:
  usage_delta_id: "model_usage_delta_<YYYY-MM-DD>_<flow_id_or_short_slug>"
  artifact_name: model_usage_delta
  execution_day: "<YYYY-MM-DD>"
  flow_id: "<F1|F2|F3|F4|operator_defined|unknown>"
  advisory_only: true
  validation_status: "<valid|valid_with_warnings|operator_review_recommended|low_confidence_auto_generated|blocked_by_missing_operator_decision>"
```

## 2. Planned Usage

Reference the planned usage source. Do not redefine routing, prompt, quota, or budget schemas here.

```yaml
planned_usage:
  planned_usage_refs:
    - ref_id: "<planned_usage_budget_or_prompt_pack_ref>"
      ref_type: "<routing_recommendation_packet|planned_usage_budget|flow_prompt_pack|next_day_plan|operator_note|unknown>"
      note: "<short note>"
  planned_route_ref: "<ref_or_unknown>"
  planned_surface_or_route_label: "<stable_surface_class_or_operator_label_or_unknown>"
  planned_usage_intent: "<what the plan expected this model_or_surface to do>"
  planned_scarcity_or_cost_note: "<operator_supplied_note_or_unknown>"
  quota_or_pricing_claim_status: "<not_claimed|operator_supplied|verified_from_explicit_source|unknown>"
```

## 3. Actual Usage Evidence

Do not claim exact model names, pricing, quota, or remaining limits unless explicitly supplied or verified.

```yaml
actual_usage:
  source_flow_recap_refs:
    - ref_id: "<flow_recap_packet_or_raw_flow_dump_ref>"
      ref_type: "<flow_recap_packet|raw_flow_dump|operator_note|artifact_ref|unknown>"
      note: "<short note>"
  actual_usage_evidence:
    evidence_status: "<explicit_operator_supplied|inferred_from_transcript|inferred_from_artifact_metadata|partial|missing|unknown>"
    evidence_refs: []
    evidence_notes: "<short evidence summary>"
    missing_evidence_reason: "<reason_or_null>"
  model_or_surface_used:
    provider_or_surface_label: "<operator_supplied_label_or_null>"
    stable_surface_class: "<stable_surface_class|provider_unspecified|unknown>"
    exact_model_name: "<exact_name_or_null>"
    exact_model_name_source: "<operator_note|artifact_metadata|verified_source|null>"
    verification_status: "<verified_by_operator|verified_by_artifact|inferred|not_supplied|unknown>"
  usage_purpose: "<prompt_generation|code_agent_run|deep_research|review_or_audit|recap_or_summary|planning|unknown>"
```

## 4. Planned vs Actual Summary

```yaml
planned_vs_actual_summary:
  comparison: "<matched_plan|cheaper_or_lighter_than_planned|heavier_or_scarcer_than_planned|different_route_used|planned_but_not_executed|executed_without_plan|insufficient_data>"
  actual_usage_observed: "<short plain-language observation>"
  operator_learning_note: "<what future planning should remember>"
```

## 5. Route Reuse / Avoid Signal

```yaml
route_reuse_or_avoid_signal:
  signal: "<reuse_route|avoid_route|use_only_for_high_value_tasks|insufficient_data|operator_review_needed>"
  rationale: "<why this signal is justified from evidence>"
  next_PreCapNextDay_hint: "<short advisory hint for future planning>"
```

## 6. Confidence

```yaml
confidence:
  level: "<high|medium|low|unknown>"
  confidence_flags:
    - "<actual_usage_evidence_missing|planned_usage_ref_missing|exact_model_unknown|inferred_from_context_only|operator_supplied_but_unverified|source_refs_incomplete|quota_or_pricing_not_verified>"
  review_note: "<what the operator should verify>"
```

## 7. Degraded Behavior When Actual Usage Evidence Is Missing

```yaml
degraded_behavior:
  used: "<true|false>"
  reason: "<actual_usage_evidence_missing|planned_usage_refs_missing|exact_model_or_surface_unknown|other>"
  required_behavior:
    produce_delta_anyway: true
    mark_advisory_only: true
    do_not_stop_FlowRecap: true
    do_not_stop_StatusMerge: true
    do_not_claim_quota_or_pricing_truth: true
    suggested_signal: "<insufficient_data|operator_review_needed>"
```

---

# Copy-Paste Skeleton

```yaml
model_usage_delta:
  usage_delta_id: "model_usage_delta_<YYYY-MM-DD>_<flow_id_or_short_slug>"
  artifact_name: model_usage_delta
  execution_day: "<YYYY-MM-DD>"
  source_flow_recap_refs:
    - ref_id: "<ref_or_unknown>"
      ref_type: "<flow_recap_packet|raw_flow_dump|operator_note|artifact_ref|unknown>"
      note: "<short note>"
  planned_usage_refs:
    - ref_id: "<ref_or_unknown>"
      ref_type: "<routing_recommendation_packet|planned_usage_budget|flow_prompt_pack|next_day_plan|operator_note|unknown>"
      note: "<short note>"
  actual_usage_evidence:
    evidence_status: "<explicit_operator_supplied|inferred_from_transcript|inferred_from_artifact_metadata|partial|missing|unknown>"
    evidence_refs: []
    evidence_notes: "<short evidence summary>"
    missing_evidence_reason: "<reason_or_null>"
  model_or_surface_used:
    provider_or_surface_label: "<operator_supplied_label_or_null>"
    stable_surface_class: "<stable_surface_class|provider_unspecified|unknown>"
    exact_model_name: "<exact_name_or_null>"
    exact_model_name_source: "<operator_note|artifact_metadata|verified_source|null>"
    verification_status: "<verified_by_operator|verified_by_artifact|inferred|not_supplied|unknown>"
  usage_purpose: "<prompt_generation|code_agent_run|deep_research|review_or_audit|recap_or_summary|planning|unknown>"
  planned_vs_actual_summary:
    planned_route_ref: "<ref_or_unknown>"
    planned_usage_intent: "<what was planned>"
    actual_usage_observed: "<what happened or unknown>"
    comparison: "<matched_plan|cheaper_or_lighter_than_planned|heavier_or_scarcer_than_planned|different_route_used|planned_but_not_executed|executed_without_plan|insufficient_data>"
    operator_learning_note: "<future planning note>"
  route_reuse_or_avoid_signal: "<reuse_route|avoid_route|use_only_for_high_value_tasks|insufficient_data|operator_review_needed>"
  route_signal_rationale: "<rationale without provider truth claims>"
  confidence:
    level: "<high|medium|low|unknown>"
    confidence_flags:
      - "<flag_or_empty>"
    review_note: "<operator review note>"
  validation_status: "<valid|valid_with_warnings|operator_review_recommended|low_confidence_auto_generated|blocked_by_missing_operator_decision>"
```
