# FILE: .claude/skills/precap-next-day/references/usage-tracking-dependency-contract.md

# Usage Tracking Dependency Contract

```yaml
usage_tracking_dependency_contract:
  artifact_name: usage_tracking_dependency_contract
  file_role: precap_next_day_dependency_contract
  purpose: >
    Define how PreCapNextDay consumes the ai-routing-and-usage-tracking skill
    package to plan daily AI usage, apply quota/scarcity awareness, generate
    usage tracking tags, and hand off planned usage context to FlowRecap without
    owning routing, quota, budget, or usage-delta schemas.

  ownership:
    owns:
      - PreCapNextDay_usage_tracking_dependency_interface
      - usage_context_intake_rules
      - planned_daily_usage_hook
      - flow_prompt_pack_usage_requirements
      - FlowRecap_usage_handoff_requirements
      - degraded_usage_tracking_behavior
      - dependency_validation_checks
      - minimal_examples
    must_not_own:
      - AI_surface_inventory_schema
      - monthly_quota_map_schema
      - routing_decision_schema
      - planned_usage_budget_schema
      - usage_delta_schema
      - routing_recommendation_packet_schema
      - cost_class_taxonomy
      - prompt_packet_schema
      - workflow_stage_taxonomy
      - process_stage_taxonomy
      - calendar_event_schema
      - FlowRecap_output_schema

  upstream_authorities:
    ai_routing_and_usage_tracking:
      package_path: ".claude/skills/ai-routing-and-usage-tracking/"
      owns:
        - AI_surface_inventory
        - monthly_quota_map
        - routing_decision
        - planned_usage_budget
        - usage_delta
        - routing_recommendation_packet
        - cost_class_and_scarcity_rules
    prompt_engineering:
      package_path: ".claude/skills/prompt-engineering/"
      owns:
        - prompt_packet
        - prompt_sequence
        - final_copy_paste_prompt
        - provider_style_contracts
    workflow_process_design:
      package_path: ".claude/skills/workflow-process-design/"
      owns:
        - workflow_stage
        - process_stage
        - expected_output_type
        - workflow_process_alignment_validation

  downstream_consumers:
    PreCapNextDay_outputs:
      - next_day_plan
      - flow_packet
      - flow_prompt_pack
      - usage_tracking_plan
      - FlowRecap_handoff_block
    later_consumers:
      - FlowRecap
      - usage_delta_capture
      - next_PreCapNextDay_input_context
```

## Dependency Role

```yaml
usage_tracking_dependency_role:
  role_summary: >
    PreCapNextDay does not choose models, define quotas, or log actual usage by
    itself. It requests routing and usage guidance, embeds the returned plan in
    daily outputs, and prepares enough capture structure for FlowRecap to record
    actual usage after operator execution.

  PreCapNextDay_may_do:
    - read_available_AI_surface_inventory_summary
    - read_available_monthly_quota_map_summary
    - request_or_embed_routing_recommendation_packet
    - request_or_embed_planned_usage_budget
    - attach_usage_tracking_tags_to_flow_prompt_packs
    - flag_high_value_prompts_for_scarce_monthly_modes
    - include_usage_capture_fields_in_FlowRecap_handoff_block
    - mark_usage_tracking_as_low_confidence_when_dependency_context_is_missing

  PreCapNextDay_must_not_do:
    - define_exact_provider_pricing
    - claim_current_product_limits_without_verification
    - claim_remaining_quota_without_operator_supplied_or_verified_source
    - finalize_OpenRouter_model_mapping
    - use_API_frontier_models_as_default_daily_flow_engines
    - override_operator_provider_choice
    - treat_cost_minimization_as_the_only_routing_goal
    - create_actual_usage_delta_before_execution
    - mutate_monthly_quota_map_after_planning
```

## Input Interface from AI Routing and Usage Tracking

```yaml
usage_tracking_dependency_inputs:
  type: object
  required:
    - dependency_status
    - validation_status

  fields:
    dependency_status:
      type: string
      allowed:
        - available
        - partially_available
        - missing
        - stale
        - operator_review_needed
      required: true

    AI_surface_inventory_ref:
      type: object_ref
      ref: AI_surface_inventory
      required: false
      note: "Reference only; schema is owned by ai-routing-and-usage-tracking."

    monthly_quota_map_ref:
      type: object_ref
      ref: monthly_quota_map
      required: false
      note: "Reference only; schema is owned by ai-routing-and-usage-tracking."

    model_usage_summary:
      type: object
      required: false
      fields:
        summary_status:
          type: string
          allowed:
            - current
            - stale
            - partial
            - missing
            - unknown
        known_scarce_modes:
          type: list
          item_type: string
          required: false
        known_abundant_modes:
          type: list
          item_type: string
          required: false
        operator_notes:
          type: string
          required: false
      note: >
        Compact summary may be supplied directly to PreCapNextDay. Detailed
        quota state remains in monthly_quota_map.

    routing_recommendation_packet_ref:
      type: object_ref
      ref: routing_recommendation_packet
      required: false
      note: "Use when routing recommendation was already generated upstream."

    planned_usage_budget_ref:
      type: object_ref
      ref: planned_usage_budget
      required: false
      note: "Use when planned usage budget was already generated upstream."

    operator_usage_preferences:
      type: object
      required: false
      fields:
        prefer_quality_over_cost_for_today:
          type: boolean
          required: false
        preserve_scarce_modes_today:
          type: boolean
          required: false
        deliberately_spend_scarce_modes_today:
          type: boolean
          required: false
        avoid_agent_runs_today:
          type: boolean
          required: false
        avoid_deep_research_today:
          type: boolean
          required: false
        provider_preferences:
          type: list
          item_type: string
          required: false
        provider_avoid_list:
          type: list
          item_type: string
          required: false
        notes:
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

## Planned Daily Usage Hook

```yaml
planned_daily_usage_hook:
  purpose: >
    Ensure every next_day_plan contains enough usage intent to make daily AI
    consumption deliberate, trackable, and later reviewable.

  required_in_next_day_plan:
    - usage_tracking_plan
    - usage_summary_for_operator
    - high_value_scarce_mode_candidates
    - low_cost_or_supplemental_candidates
    - usage_risks_and_review_flags

  usage_tracking_plan:
    type: object
    required:
      - plan_status
      - planning_basis
      - daily_usage_intent
      - flow_usage_overview
      - validation_status

    fields:
      plan_status:
        type: string
        allowed:
          - generated_from_dependency
          - generated_from_partial_context
          - generic_defaults_used
          - operator_review_needed
          - blocked_by_missing_operator_decision
        required: true

      planning_basis:
        type: object
        required: true
        fields:
          AI_surface_inventory_used:
            type: boolean
          monthly_quota_map_used:
            type: boolean
          model_usage_summary_used:
            type: boolean
          routing_recommendation_packet_used:
            type: boolean
          planned_usage_budget_used:
            type: boolean
          operator_usage_preferences_used:
            type: boolean
          volatile_claims_avoided:
            type: boolean

      daily_usage_intent:
        type: object
        required: true
        fields:
          daily_strategy:
            type: string
            allowed:
              - quality_first_for_planned_flows
              - conserve_scarce_modes
              - deliberately_spend_scarce_modes
              - balanced_usage
              - low_confidence_generic
          rationale:
            type: string
          scarce_mode_spend_policy:
            type: string
            allowed:
              - spend_when_high_impact
              - preserve_unless_operator_overrides
              - actively_schedule_one_high_value_use
              - unknown
          supplemental_API_policy:
            type: string
            allowed:
              - low_reasoning_cost_sensitive_only
              - avoid_today
              - allow_for_batch_or_transform_only
              - unknown

      flow_usage_overview:
        type: list
        item_ref: flow_usage_plan_summary
        min_items: 0
        max_items: 4
        required: true

      usage_risks_and_review_flags:
        type: list
        item_type: string
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

## Flow Usage Plan Summary

```yaml
flow_usage_plan_summary:
  type: object
  required:
    - flow_id
    - usage_intent
    - recommended_surface_class
    - scarcity_class
    - usage_tracking_tags_required
    - validation_status

  fields:
    flow_id:
      type: string
      allowed:
        - F1
        - F2
        - F3
        - F4
      required: true

    project_or_flow_name:
      type: string
      required: false

    usage_intent:
      type: string
      allowed:
        - high_reasoning_work
        - deep_research_work
        - agent_run_candidate
        - code_agent_candidate
        - long_context_digest
        - lightweight_batch_or_transform
        - no_AI_use_planned
        - unknown
      required: true

    recommended_surface_class:
      type: string
      allowed:
        - subscription_frontier_chat
        - subscription_frontier_reasoning
        - deep_research_surface
        - agent_run_surface
        - code_agent_surface
        - long_context_surface
        - supplemental_api_low_cost
        - provider_unspecified
      required: true

    scarcity_class:
      type: string
      allowed:
        - abundant
        - moderate
        - scarce
        - unknown
      required: true

    planned_usage_budget_ref:
      type: object_ref
      ref: planned_usage_budget
      required: false

    routing_decision_ref:
      type: object_ref
      ref: routing_decision
      required: false

    reason_for_surface:
      type: string
      required: false

    fallback_surface_class:
      type: string
      allowed:
        - subscription_frontier_chat
        - subscription_frontier_reasoning
        - deep_research_surface
        - agent_run_surface
        - code_agent_surface
        - long_context_surface
        - supplemental_api_low_cost
        - provider_unspecified
      required: false

    usage_tracking_tags_required:
      type: boolean
      required: true

    operator_review_flags:
      type: list
      item_type: string
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

## Flow Prompt Pack Usage Requirements

```yaml
flow_prompt_pack_usage_requirements:
  purpose: >
    Define the usage-related fields PreCapNextDay must include or request when
    assembling each flow_prompt_pack.

  required_per_flow_prompt_pack:
    - usage_tracking_tags
    - routing_summary
    - quota_or_scarcity_note
    - fallback_surface_note
    - usage_capture_hint_for_FlowRecap

  usage_tracking_tags:
    type: object
    required:
      - planned_surface_class
      - planned_cost_class
      - scarce_mode_planned
      - capture_actual_usage_after_execution

    fields:
      planned_surface_class:
        type: string
        allowed:
          - subscription_frontier_chat
          - subscription_frontier_reasoning
          - deep_research_surface
          - agent_run_surface
          - code_agent_surface
          - long_context_surface
          - supplemental_api_low_cost
          - provider_unspecified
        required: true

      planned_cost_class:
        type: string
        allowed:
          - subscription_frontier
          - quota_limited_frontier
          - scarce_monthly_mode
          - supplemental_API_low_reasoning
          - later_OpenRouter
          - unknown
        required: true

      scarce_mode_planned:
        type: boolean
        required: true

      scarce_mode_reason:
        type: string
        required: false

      route_requires_operator_review:
        type: boolean
        required: false

      capture_actual_usage_after_execution:
        type: boolean
        required: true

      actual_usage_delta_target:
        type: string
        allowed:
          - FlowRecap_usage_delta_section
          - manual_operator_note
          - automated_API_logs_later
          - not_applicable
        required: false

  routing_summary:
    type: object
    required:
      - selected_surface_class
      - selection_rationale
      - fallback_surface_class

    fields:
      selected_surface_class:
        type: string
        allowed:
          - subscription_frontier_chat
          - subscription_frontier_reasoning
          - deep_research_surface
          - agent_run_surface
          - code_agent_surface
          - long_context_surface
          - supplemental_api_low_cost
          - provider_unspecified
        required: true
      selection_rationale:
        type: string
        required: true
      fallback_surface_class:
        type: string
        allowed:
          - subscription_frontier_chat
          - subscription_frontier_reasoning
          - deep_research_surface
          - agent_run_surface
          - code_agent_surface
          - long_context_surface
          - supplemental_api_low_cost
          - provider_unspecified
        required: true
      routing_decision_ref:
        type: object_ref
        ref: routing_decision
        required: false

  quota_or_scarcity_note:
    type: object
    required:
      - scarcity_class
      - quota_claim_status
      - operator_note

    fields:
      scarcity_class:
        type: string
        allowed:
          - abundant
          - moderate
          - scarce
          - unknown
        required: true
      quota_claim_status:
        type: string
        allowed:
          - no_exact_quota_claim
          - operator_supplied_quota_claim
          - current_verified_quota_claim
          - unknown
        required: true
      operator_note:
        type: string
        required: true
```

## FlowRecap Usage Handoff Requirements

```yaml
FlowRecap_usage_handoff_requirements:
  purpose: >
    Ensure FlowRecap can capture actual model/surface usage after the operator
    executes the planned flow.

  required_in_FlowRecap_handoff_block:
    - planned_surface_class
    - planned_cost_class
    - planned_usage_reason
    - scarce_mode_planned
    - usage_capture_questions
    - expected_usage_delta_target

  usage_capture_questions:
    required_questions:
      - "Which AI provider or surface did you actually use?"
      - "Was the planned surface used, changed, skipped, or unavailable?"
      - "Was any scarce monthly mode used?"
      - "Was any supplemental API or OpenRouter-like route used?"
      - "Did the route feel underpowered, overpowered, or appropriate?"
      - "Should tomorrow preserve, spend, or rebalance scarce usage?"

  expected_usage_delta_target:
    type: object_ref
    ref: usage_delta
    note: >
      FlowRecap or the usage-tracking skill owns the actual usage_delta schema.
      PreCapNextDay only prepares capture prompts and references the target.
```

## Degraded Usage Tracking Behavior

```yaml
degraded_usage_tracking_behavior:
  when_dependency_missing:
    plan_status: generic_defaults_used
    default_surface_class: provider_unspecified
    default_cost_class: unknown
    required_flag: usage_tracking_dependency_missing
    correction: >
      Generate the daily plan anyway, but mark usage tracking as
      low_confidence_auto_generated and ask the operator to supply AI surface or
      quota context before high-value routing decisions are treated as final.

  when_quota_map_missing:
    plan_status: generated_from_partial_context
    default_scarcity_class: unknown
    required_flag: monthly_quota_map_missing
    correction: >
      Avoid exact quota claims. Use stable surface classes and mark scarce-mode
      decisions for operator review.

  when_inventory_stale:
    plan_status: generated_from_partial_context
    required_flag: AI_surface_inventory_stale
    correction: >
      Do not claim exact model availability. Use stable surface classes and
      request current verification before product-specific routing.

  when_operator_prefers_specific_provider:
    rule: >
      Preserve the operator preference unless it violates a known process gate
      or the requested provider is unavailable or unknown.
    required_flag_when_conflict: operator_provider_preference_conflict

  when_cost_and_quality_conflict:
    rule: >
      For planned daily flow work, quality and impact outrank cost. Present the
      tradeoff if cost or scarcity risk is nontrivial.
    conflict_resolution_order:
      - operator_tradeoff_decision
      - workflow_process_fit
      - prompt_quality
      - routing_cost_or_efficiency
```

## PreCapNextDay Procedure Insert

```yaml
PreCapNextDay_usage_tracking_procedure_insert:
  recommended_position: after_prompt_pack_generation_before_final_operator_review

  steps:
    1_load_usage_context: >
      Read any supplied AI_surface_inventory, monthly_quota_map,
      model_usage_summary, routing_recommendation_packet, planned_usage_budget,
      or operator usage preferences.

    2_request_or_infer_usage_plan: >
      If routing guidance exists, reference it. If absent, create only a generic
      usage_tracking_plan with stable surface classes and low-confidence flags.

    3_attach_usage_tags: >
      Add usage_tracking_tags, routing_summary, quota_or_scarcity_note, and
      fallback_surface_note to each flow_prompt_pack.

    4_prepare_FlowRecap_capture: >
      Add usage capture questions and usage_delta target references to each
      FlowRecap_handoff_block.

    5_validate_usage_boundaries: >
      Confirm no exact pricing, exact remaining quota, final OpenRouter model
      mapping, or actual usage_delta has been created by PreCapNextDay.
```

## Minimal Examples

```yaml
example_high_reasoning_flow_usage:
  usage_tracking_plan:
    plan_status: generated_from_dependency
    planning_basis:
      AI_surface_inventory_used: true
      monthly_quota_map_used: true
      model_usage_summary_used: true
      routing_recommendation_packet_used: true
      planned_usage_budget_used: true
      operator_usage_preferences_used: false
      volatile_claims_avoided: true
    daily_usage_intent:
      daily_strategy: quality_first_for_planned_flows
      rationale: "F3 is high-impact orchestration design work with ambiguity and risk."
      scarce_mode_spend_policy: spend_when_high_impact
      supplemental_API_policy: low_reasoning_cost_sensitive_only
    flow_usage_overview:
      - flow_id: F3
        project_or_flow_name: Apex
        usage_intent: high_reasoning_work
        recommended_surface_class: subscription_frontier_reasoning
        scarcity_class: moderate
        reason_for_surface: "High ambiguity and architecture risk justify stronger reasoning."
        fallback_surface_class: subscription_frontier_chat
        usage_tracking_tags_required: true
        validation_status: valid
    usage_risks_and_review_flags: []
    validation_status: valid

example_missing_usage_dependency:
  usage_tracking_plan:
    plan_status: generic_defaults_used
    planning_basis:
      AI_surface_inventory_used: false
      monthly_quota_map_used: false
      model_usage_summary_used: false
      routing_recommendation_packet_used: false
      planned_usage_budget_used: false
      operator_usage_preferences_used: false
      volatile_claims_avoided: true
    daily_usage_intent:
      daily_strategy: low_confidence_generic
      rationale: "No usable routing or quota context was supplied."
      scarce_mode_spend_policy: unknown
      supplemental_API_policy: unknown
    flow_usage_overview:
      - flow_id: F1
        usage_intent: unknown
        recommended_surface_class: provider_unspecified
        scarcity_class: unknown
        fallback_surface_class: provider_unspecified
        usage_tracking_tags_required: true
        operator_review_flags:
          - usage_tracking_dependency_missing
        validation_status: low_confidence_auto_generated
    usage_risks_and_review_flags:
      - usage_tracking_dependency_missing
      - monthly_quota_map_missing
      - AI_surface_inventory_missing
    validation_status: low_confidence_auto_generated
```

## Validation Checks

```yaml
usage_tracking_dependency_validation_checks:
  schema_ownership_preserved:
    AI_surface_inventory_schema_not_redefined: true
    monthly_quota_map_schema_not_redefined: true
    routing_decision_schema_not_redefined: true
    planned_usage_budget_schema_not_redefined: true
    usage_delta_schema_not_redefined: true
    routing_recommendation_packet_schema_not_redefined: true

  PreCapNextDay_requirements:
    usage_tracking_plan_present: true
    each_flow_prompt_pack_has_usage_tracking_tags: true
    each_flow_prompt_pack_has_routing_summary: true
    each_flow_prompt_pack_has_quota_or_scarcity_note: true
    each_FlowRecap_handoff_has_usage_capture_questions: true
    degraded_mode_available_when_dependency_missing: true

  volatility_and_boundary_checks:
    no_exact_pricing_claim_without_verification: true
    no_exact_remaining_quota_claim_without_verification: true
    no_final_OpenRouter_model_mapping: true
    no_actual_usage_delta_created_before_execution: true
    operator_choice_not_overridden: true
```

---

# VALIDATION — FILE-SPECIFIC CHECKS

- [ ] Exactly one file was produced.
- [ ] Target path is `.claude/skills/precap-next-day/references/usage-tracking-dependency-contract.md`.
- [ ] File owns only the PreCapNextDay dependency interface to usage tracking.
- [ ] File does not redefine `AI_surface_inventory`, `monthly_quota_map`, `routing_decision`, `planned_usage_budget`, `usage_delta`, or `routing_recommendation_packet` schemas.
- [ ] File includes degraded behavior for missing usage context.
- [ ] File includes `usage_tracking_plan`, flow-level usage summary, prompt-pack usage tags, and FlowRecap usage handoff requirements.
- [ ] File avoids exact pricing, exact quota, exact current availability, and final OpenRouter model mapping claims.
- [ ] YAML uses 2-space indentation.

---

# NEXT PROMPT

Paste this next:
> Prompt PND8:
> Create exactly one file.
>
> # FILE: .claude/skills/precap-next-day/references/calendar-event-write-contract.md
>
> File type: reference_contract.
> Schema ownership: owns PreCapNextDay calendar workflow-block write request interface.
> Context carry-forward:
> - .claude/skills/precap-next-day/SKILL.md
> - .claude/skills/precap-next-day/references/daily-plan-output-contract.md
> - .claude/skills/precap-next-day/references/flow-packet-contract.md
> - .claude/skills/precap-next-day/references/usage-tracking-dependency-contract.md
>
> This file must define:
> - calendar_event_write_request schema for workflow blocks only
> - operator approval requirements
> - create vs update decision rules
> - manual calendar constraint fallback
> - non-workflow block boundary
> - degraded behavior when calendar access is unavailable
> - examples
>
> Rules:
> - Do not create actual calendar events inside this file.
> - Do not define general calendar integration or connector implementation.
> - Do not create non-workflow personal blocks.
> - Do not require calendar access for PreCapNextDay to run.
> - Use YAML with 2-space indentation.
>
> Next prompt target: Prompt PND9.
