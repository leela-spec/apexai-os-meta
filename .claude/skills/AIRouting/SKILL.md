---
name: ai-routing-and-usage-tracking
description: >
  Use this skill when the operator asks to choose AI providers, model surfaces, usage classes, or quota plans for prompts or flow work. Accepts operator_task, prompt_packet, flow_packet, AI_surface_inventory, model_usage_summary, and usage_delta. Produces routing_decision, planned_usage_budget, usage_tracking_tags, and routing_recommendation_packet. Does not execute prompts, create project plans, create calendar events, or override operator choice.
---

# AI Routing and Usage Tracking

## Skill Contract

```yaml
skill_contract:
  primary_output: routing_recommendation_packet
  output_role: usage_aware_ai_routing_advisor

  accepted_inputs:
    - operator_task
    - prompt_packet
    - prompt_sequence
    - flow_packet
    - workflow_context
    - expected_output_type
    - AI_surface_inventory
    - monthly_quota_map
    - model_usage_summary
    - usage_delta
    - prompt_result_feedback

  primary_outputs:
    - routing_decision
    - planned_usage_budget
    - usage_tracking_tags
    - routing_recommendation_packet

  routing_modes:
    planned_flow_session:
      priority_order:
        - quality
        - impact
        - risk_control
        - weekly_plan_alignment
        - cost
      cost_policy: subscription_frontier_models_mean_cost_is_not_primary_constraint
    supplemental_or_batch_execution:
      priority_order:
        - leverage_weighted_quality
        - sufficient_surface_fit
        - cost_efficiency
        - speed
        - risk_control
      cost_policy: use_low_cost_surfaces_when_quality_is_sufficient

  surface_class_policy:
    stable_surface_classes_only: true
    final_model_mapping_status: todo_later
    volatile_claims_require_current_verification: true
    abstract_surface_classes:
      - subscription_frontier_chat
      - subscription_frontier_reasoning
      - deep_research_surface
      - agent_run_surface
      - code_agent_surface
      - long_context_surface
      - supplemental_api_low_cost
      - provider_unspecified

  high_end_reasoning_score:
    impact:
      type: integer
      min: 1
      max: 100
    risk:
      type: integer
      min: 1
      max: 100
    evidence_need:
      type: integer
      min: 1
      max: 100
    ambiguity:
      type: integer
      min: 1
      max: 100

  validation_status_allowed:
    - valid
    - valid_with_warnings
    - operator_review_recommended
    - low_confidence_auto_generated
    - blocked_by_missing_operator_decision

  boundaries:
    must_create_or_define:
      - routing_decision
      - planned_usage_budget
      - usage_tracking_tags
      - routing_recommendation_packet
      - fallback_surface
      - quota_rationale
      - operator_review_flags
    must_not_create:
      - prompt_execution
      - project_execution
      - daily_plan
      - flow_packet
      - final_copy_paste_prompt
      - workflow_stage_taxonomy
      - process_stage_taxonomy
      - calendar_event
      - final_OpenRouter_model_map
      - exact_current_pricing_claim
      - exact_product_limit_claim
```

## Supporting Files

```yaml
supporting_files:
  - path: old-apex-routing-doctrine.md
    read_when:
      - forming_routing_recommendation
      - checking_routing_failure_modes
      - operator_requests_routing_doctrine

  - path: references/AI-surface-inventory-contract.md
    read_when:
      - AI_surface_inventory_missing
      - validating_available_surfaces
      - selecting_surface_class
      - checking_surface_capability_tags

  - path: references/monthly-quota-map-contract.md
    read_when:
      - monthly_quota_map_available
      - scarce_mode_possible
      - quota_pressure_needs_review
      - planning_high_end_reasoning_use

  - path: references/routing-decision-contract.md
    read_when:
      - creating_routing_decision
      - validating_route_fields
      - resolving_provider_or_surface_conflict
      - assigning_fallback_surface

  - path: references/planned-usage-budget-contract.md
    read_when:
      - creating_planned_usage_budget
      - estimating_daily_or_flow_usage
      - comparing_planned_use_to_quota
      - preparing_next_day_usage_plan

  - path: references/usage-delta-contract.md
    read_when:
      - usage_delta_available
      - capturing_FlowRecap_usage_feedback
      - comparing_actual_use_to_planned_use
      - updating_usage_learning_signal

  - path: references/routing-recommendation-packet-contract.md
    read_when:
      - creating_routing_recommendation_packet
      - producing_operator_tradeoff_card
      - combining_routing_and_budget_outputs
      - validating_final_recommendation

  - path: references/cost-class-and-scarcity-rules.md
    read_when:
      - assigning_cost_class
      - deciding_scarce_mode_allowed
      - preventing_minimum_cost_overoptimization
      - applying_high_value_route_rules

  - path: examples/starter-usage-routing-example.md
    read_when:
      - operator_requests_example
      - testing_skill_for_first_time
      - calibrating_routing_decision_shape
      - validating_package_behavior

  - path: package-manifest.md
    read_when:
      - operator_inspects_package_structure
      - validating_package_files
```

## Procedure

1. **Load routing context.** Read the operator task, prompt packet, flow packet, expected output type, workflow context, AI surface inventory, quota map, model usage summary, and usage delta when available; mark missing inputs without blocking unless routing cannot be estimated.

2. **Classify task value.** Assign routing mode, cost class, risk level, evidence need, ambiguity, and high_end_reasoning_score using the task impact and downstream consequences.

3. **Select surface.** Choose the best stable surface class and fallback surface for the task, using quality and risk first for planned flow sessions and leverage-weighted cost efficiency for supplemental or batch work.

4. **Plan usage.** Create a planned usage budget that states expected scarcity pressure, whether scarce or high-end modes are justified, and what usage fields must be captured later.

5. **Create recommendation.** Produce a routing recommendation packet containing routing_decision, planned_usage_budget, usage_tracking_tags, quota_rationale, fallback_rule, and operator_review_flags.

6. **Resolve conflicts.** If operator preference, workflow fit, prompt quality, and cost disagree, apply the authority order operator decision, workflow fit, prompt quality, then routing cost; surface unresolved conflicts as an operator tradeoff card.

7. **Validate boundaries.** Confirm that the recommendation does not execute prompts, create project plans, create calendar events, define workflow/process taxonomies, or finalize volatile provider/model/pricing claims.

8. **Prepare feedback hook.** State how FlowRecap or later usage logs should report actual usage_delta so future routing recommendations can compare planned use with actual use.

## Failure Modes

```yaml
failure_modes:
  missing_AI_surface_inventory:
    trigger: "No AI_surface_inventory is supplied or the inventory lacks usable surface classes."
    correction: "Use provider_unspecified with stable abstract surface classes and mark validation_status as low_confidence_auto_generated."

  missing_quota_map:
    trigger: "No monthly_quota_map or model_usage_summary is supplied for a quota-sensitive decision."
    correction: "Create a conservative planned_usage_budget and add operator_review_flags for missing quota context."

  volatile_provider_claim_requested:
    trigger: "The task requires current pricing, exact model rankings, product limits, or availability."
    correction: "Do not claim the value; require current verification or mark the claim as unknown."

  cost_overrides_quality:
    trigger: "The route selects a cheaper surface even though impact, risk, evidence need, or ambiguity justify stronger reasoning."
    correction: "Re-rank the route using the planned_flow_session priority order and explain the tradeoff."

  prompt_execution_requested:
    trigger: "The operator asks this skill to run the prompt rather than route it."
    correction: "Return the routing recommendation only and state that prompt execution is out of scope."

  workflow_conflict_detected:
    trigger: "The selected route conflicts with workflow stage, process stage, or expected output type."
    correction: "Defer to workflow-process-design validation and mark operator_review_recommended."

  operator_choice_conflict:
    trigger: "The operator explicitly chooses a provider or surface that conflicts with routing recommendations."
    correction: "Preserve operator choice, show the risk/cost/quality tradeoff, and flag the conflict."

  final_model_map_drift:
    trigger: "The output tries to finalize OpenRouter or exact model mapping."
    correction: "Replace exact mapping with TODO placeholder classes and keep API use supplemental by default."
```

## Output Requirements

```yaml
output_requirements:
  routing_decision:
    required: true
    must_include:
      - selected_surface_class
      - fallback_surface
      - routing_mode
      - cost_class
      - scarce_mode_allowed
      - route_rationale
      - validation_status

  planned_usage_budget:
    required: true
    must_include:
      - planned_usage_unit
      - expected_usage_intensity
      - quota_pressure
      - high_end_reasoning_score
      - usage_capture_fields
      - validation_status

  usage_tracking_tags:
    required: true
    must_include:
      - planned_surface_class
      - planned_cost_class
      - planned_reasoning_level
      - flow_or_prompt_reference
      - capture_required

  routing_recommendation_packet:
    required: true
    must_include:
      - routing_decision
      - planned_usage_budget
      - usage_tracking_tags
      - quota_rationale
      - fallback_rule
      - operator_review_flags
      - validation_status

  output_format:
    preferred: compact_markdown_with_yaml_blocks
    machine_readable_first: true
    human_readable_second: true
```

## Completion Gate

```yaml
completion_gate:
  routing_decision_present: true
  planned_usage_budget_present: true
  usage_tracking_tags_present: true
  routing_recommendation_packet_present: true
  selected_surface_class_is_stable_not_exact_model_claim: true
  high_end_reasoning_score_uses_typed_1_to_100_axes: true
  fallback_surface_present: true
  quota_rationale_present: true
  operator_review_flags_present_when_needed: true
  prompt_execution_not_performed: true
  project_plan_not_created: true
  calendar_event_not_created: true
  final_OpenRouter_model_map_not_created: true
```

---

# VALIDATION — FILE-SPECIFIC CHECKS

- [ ] The file is `.claude/skills/ai-routing-and-usage-tracking/SKILL.md`.
- [ ] Frontmatter contains only `name` and `description`.
- [ ] Description begins exactly with `Use this skill when`.
- [ ] Section order follows the required SKILL.md sequence.
- [ ] Supporting files use YAML with `path` and snake_case `read_when` conditions.
- [ ] Procedure has 8 steps and no sub-bullets.
- [ ] Failure modes use YAML with only `trigger` and `correction` fields per mode.
- [ ] Output requirements are machine-readable YAML.
- [ ] Completion gate is a YAML boolean checklist.
- [ ] The file does not execute prompts, create project plans, create calendar events, or finalize OpenRouter model mapping.
- [ ] The file uses stable surface classes and avoids volatile provider/model/pricing claims.

---

# NEXT PROMPT

Paste this next:
> Prompt AR2:
> Create exactly one file.
>
> # FILE: .claude/skills/ai-routing-and-usage-tracking/references/AI-surface-inventory-contract.md
>
> File type: reference_contract.
> Schema ownership: owns AI_surface_inventory and stable AI surface class taxonomy.
> Context carry-forward: load AR1 and all prompt-engineering package outputs before writing.
>
> This file must define:
> - AI_surface_inventory schema
> - stable surface class taxonomy
> - capability tags
> - availability and uncertainty fields
> - provider/model volatility policy
> - surface-to-task fit hints
> - minimal examples
>
> Rules:
> - Use abstract surface classes, not exact model rankings.
> - Do not claim current pricing, exact availability, or product limits.
> - Do not define routing_decision schema owned by AR4.
> - Do not duplicate prompt_packet schema from prompt-engineering.
> - Use YAML with 2-space indentation.
>
> Next prompt target: Prompt AR3.
