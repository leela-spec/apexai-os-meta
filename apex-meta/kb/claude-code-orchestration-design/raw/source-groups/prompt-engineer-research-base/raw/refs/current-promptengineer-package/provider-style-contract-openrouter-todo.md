# FILE: .claude/skills/prompt-engineering/references/provider-style-contract-openrouter-todo.md

```markdown
# Provider Style Contract — OpenRouter TODO

```yaml
provider_style_contract_openrouter_todo:
  artifact_name: provider_style_contract_openrouter_todo
  file_role: provider_boundary_placeholder
  purpose: >
    Define the OpenRouter placeholder boundary for prompt-engineering. This
    file records that OpenRouter mapping is TODO later, treats OpenRouter as an
    API routing layer rather than a single provider style, and keeps API use
    supplemental, low-reasoning, and cost-sensitive by default. It does not
    finalize specific models, pricing, availability, rankings, or routing
    decisions.

  ownership:
    owns:
      - OpenRouter_later_boundary
      - API_low_reasoning_placeholder
      - future_fields_to_define
      - OpenRouter_safety_boundaries
      - placeholder_routing_note_examples
    must_not_own:
      - finalized_OpenRouter_model_map
      - exact_model_rankings
      - exact_pricing
      - current_availability
      - benchmark_claims
      - routing_decision_schema
      - monthly_quota_schema
      - prompt_packet_schema
      - provider_specific_model_style
      - workflow_stage_taxonomy
      - process_stage_taxonomy

  boundary_status:
    OpenRouter_mapping_status: TODO_later
    provider_style_status: placeholder_only
    treated_as: API_routing_layer
    treated_as_single_provider_style: false
    API_calls_default_role: supplemental_low_reasoning_cost_sensitive
    specific_models_finalized: false
```

## Boundary Rules

```yaml
OpenRouter_boundary_rules:
  core_statements:
    - "OpenRouter mapping is TODO later."
    - "OpenRouter is treated as an API routing layer, not a single provider style."
    - "API calls are supplemental, low-reasoning, and cost-sensitive by default."
    - "Specific OpenRouter models must not be finalized in this package stage."

  allowed_now:
    - record_placeholder_routing_notes
    - mark_OpenRouter_as_later_surface
    - describe_API_cost_sensitivity
    - define_future_fields_to_collect
    - warn_against_unverified_model_claims
    - reference_ai_routing_and_usage_tracking_for_final_routing

  forbidden_now:
    - choose_specific_OpenRouter_model
    - claim_current_pricing
    - claim_current_availability
    - rank_OpenRouter_models
    - use_benchmark_claims_without_current_verification
    - treat_OpenRouter_as_default_daily_flow_engine
    - override_operator_provider_choice
    - duplicate_routing_decision_schema
```

## API Use Defaults

```yaml
API_use_defaults:
  default_class: supplemental_API_low_reasoning

  default_policy:
    reasoning_level: low_by_default
    cost_sensitivity: high
    used_for_frontier_daily_flow_core: false
    operator_review_recommended: true
    current_verification_required_before_final_use: true

  use_when_placeholder:
    - low_value_batch_transformation
    - mechanical_format_conversion
    - lightweight_classification
    - simple_extraction
    - noncritical_draft_expansion
    - supplemental_comparison_after_primary_frontier_work

  avoid_when_placeholder:
    - high_impact_architecture_decision
    - high_risk_strategy_or_project_direction
    - source_grounded_research_with_current_information_need
    - complex_prompt_pack_finalization
    - operator_relationship_or_business_critical_copy
    - tasks_requiring_reliable_long_context_reasoning
    - tasks_with_unclear_safety_or_permission_boundary

  escalation_rule: >
    If impact, risk, evidence_need, or ambiguity is high, do not route to the
    OpenRouter placeholder by default. Request ai-routing-and-usage-tracking
    guidance and current verification before recommending any API route.
```

## Future Fields to Define

```yaml
future_fields_to_define:
  model_inventory:
    status: TODO_later
    future_fields:
      - model_identifier
      - model_provider
      - model_capability_class
      - context_class
      - reasoning_class
      - tool_use_support
      - structured_output_fit
      - reliability_notes
      - current_availability_verified_at

  pricing_and_budget:
    status: TODO_later
    future_fields:
      - pricing_source
      - input_cost_class
      - output_cost_class
      - budget_limit
      - estimated_cost_per_prompt_class
      - budget_alert_threshold
      - verified_at

  routing_fit:
    status: TODO_later
    future_fields:
      - recommended_task_types
      - avoid_task_types
      - fallback_surface
      - confidence
      - stop_conditions
      - operator_review_flags

  quality_feedback:
    status: TODO_later
    future_fields:
      - prompt_packet_id
      - actual_model_used
      - result_quality
      - hallucination_or_drift_note
      - formatting_reliability
      - latency_or_friction_note
      - should_repeat_route
      - should_avoid_route

  integration_requirements:
    status: TODO_later
    future_fields:
      - API_access_method
      - logging_method
      - usage_capture_source
      - security_boundary
      - failure_recovery_note
```

## Safety Boundaries

```yaml
safety_boundaries:
  no_unverified_model_claims:
    trigger: "A prompt or routing note names exact OpenRouter models, rankings, pricing, or availability without current verification."
    correction: "Replace exact claims with placeholder fields and require current verification."

  no_default_frontier_replacement:
    trigger: "OpenRouter placeholder is used as the default engine for high-impact daily flow prompts."
    correction: "Use subscription frontier or operator-selected route for high-impact work unless ai-routing-and-usage-tracking validates otherwise."

  no_provider_style_overreach:
    trigger: "This file starts defining detailed prompt style for a specific model behind OpenRouter."
    correction: "Remove model-specific style and keep only API-layer placeholder boundaries."

  no_cost_only_optimization:
    trigger: "The route is selected only because it is cheaper."
    correction: "Require sufficient model fit, task value, risk, and output quality criteria before cost is considered."

  no_schema_duplication:
    trigger: "The file redefines routing_decision, planned_usage_budget, or prompt_packet schema."
    correction: "Remove duplicated schema and reference the owning package or contract."

  no_sensitive_or_state_changing_default:
    trigger: "API placeholder route is used for sensitive, permissioned, or state-changing work without operator approval."
    correction: "Mark blocked_by_missing_operator_decision and require explicit operator approval."
```

## Placeholder Routing Notes

```yaml
placeholder_routing_notes:
  valid_note_pattern:
    provider_target: OpenRouter_later
    status: placeholder_only
    model_selection: TODO_later
    use_case_class: supplemental_API_low_reasoning
    cost_policy: cost_sensitive
    current_verification_required: true
    final_routing_owner: ai-routing-and-usage-tracking

  note_templates:
    lightweight_extraction:
      note: >
        OpenRouter_later may be considered for low-risk extraction or formatting
        once model inventory and current pricing are verified. Do not finalize a
        model here.

    batch_transformation:
      note: >
        OpenRouter_later may be considered for supplemental batch transformation
        if output quality requirements are low-to-medium and current cost fit is
        verified by ai-routing-and-usage-tracking.

    fallback_surface:
      note: >
        OpenRouter_later may serve as a fallback surface after the primary
        route fails or is unavailable, but model choice remains TODO until the
        routing package validates current options.
```

## Failure Modes

```yaml
OpenRouter_failure_modes:
  finalized_model_drift:
    trigger: "The output names a specific OpenRouter model as the chosen route."
    correction: "Replace with OpenRouter_later and mark model_selection as TODO_later."

  volatile_claim_drift:
    trigger: "The output states current pricing, availability, benchmarks, or limits."
    correction: "Remove the claim or mark it as requiring current verification outside this file."

  provider_style_confusion:
    trigger: "OpenRouter is described as if it has one stable prompt style."
    correction: "Describe it as an API routing layer and keep style adaptation model-dependent and future-defined."

  API_overuse:
    trigger: "API route is recommended for high-impact reasoning because it is available or cheaper."
    correction: "Escalate to ai-routing-and-usage-tracking and apply impact, risk, evidence_need, and ambiguity checks."

  routing_schema_duplication:
    trigger: "The file defines routing decision fields as canonical schema."
    correction: "Move routing schema responsibility to ai-routing-and-usage-tracking."

  prompt_packet_duplication:
    trigger: "The file redefines prompt_packet or final_copy_paste_prompt schema."
    correction: "Reference prompt-packet-contract instead of redefining it."
```

## Minimal Examples

### Valid placeholder note for simple extraction

```yaml
example_simple_extraction_placeholder:
  provider_target: OpenRouter_later
  status: placeholder_only
  use_case_class: supplemental_API_low_reasoning
  candidate_task: "Extract labels from a small batch of short notes."
  model_selection: TODO_later
  reason: "Task appears low-risk, mechanical, and cost-sensitive."
  current_verification_required: true
  final_routing_owner: ai-routing-and-usage-tracking
  validation_status: operator_review_recommended
```

### Valid placeholder note for fallback

```yaml
example_fallback_placeholder:
  provider_target: OpenRouter_later
  status: placeholder_only
  use_case_class: fallback_surface
  candidate_task: "Retry a noncritical formatting task if the primary route is unavailable."
  model_selection: TODO_later
  fallback_reason: "Could be useful for supplemental work after current model inventory exists."
  current_verification_required: true
  validation_status: operator_review_recommended
```

### Invalid finalized model pattern

```yaml
invalid_finalized_model_pattern:
  invalid:
    provider_target: OpenRouter_later
    model_selection: "specific_model_name"
    claim: "This is the best cheap model for the task."
  correction:
    provider_target: OpenRouter_later
    model_selection: TODO_later
    claim: "Model choice requires current verification and belongs to ai-routing-and-usage-tracking."
```

### Invalid high-impact default

```yaml
invalid_high_impact_default:
  invalid:
    task_value_class: strategic_bottleneck
    provider_target: OpenRouter_later
    reason: "Cheaper API route."
  correction:
    task_value_class: strategic_bottleneck
    provider_target: provider_unspecified
    operator_review_flag: high_impact_route_requires_ai_routing_review
    reason: "Cost alone cannot route strategic bottleneck work."
```
```

---

# VALIDATION — FILE-SPECIFIC CHECKS

- [ ] OpenRouter mapping is marked TODO later.
- [ ] OpenRouter is treated as an API routing layer, not a single provider style.
- [ ] API calls are marked supplemental, low-reasoning, and cost-sensitive by default.
- [ ] No specific OpenRouter model is finalized.
- [ ] Future fields are placeholders only.
- [ ] Safety boundaries are included.
- [ ] Placeholder routing-note examples are included.
- [ ] The file does not define routing-decision schema owned by `ai-routing-and-usage-tracking`.
- [ ] The file does not duplicate `prompt_packet` schema.

---

# NEXT PROMPT

Paste this next:
> Prompt PE9:
> Create exactly one file.
>
> # FILE: .claude/skills/prompt-engineering/references/prompt-quality-validation.md
>
> File type: reference_rules.
> Schema ownership: owns prompt_quality_validation.
> Context carry-forward: load all previously generated prompt-engineering files before writing.
>
> This file must define:
> - prompt quality validation checks
> - clear_role
> - clear_task
> - relevant_context
> - explicit_output_contract
> - expected_output_type
> - validation_criteria
> - iteration_logic
> - stop_condition_or_red_flags
> - short_provider_rationale
> - short_design_rationale
> - prompt_failure_hints
> - workflow_stage_alignment
> - process_stage_alignment
> - validation_status assignment
> - operator_review_flags
> - valid, warning, and failed examples
>
> Rules:
> - Do not duplicate prompt_packet schema from PE2.
> - Reference workflow-process-design when workflow/process alignment is required.
> - Reference ai-routing-and-usage-tracking when provider or route fit is required.
> - Failed examples must produce learning signals.
>
> Next prompt target: Prompt PE10.
