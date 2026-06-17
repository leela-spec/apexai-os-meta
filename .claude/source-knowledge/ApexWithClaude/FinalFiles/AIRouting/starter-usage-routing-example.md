# FILE: .claude/skills/ai-routing-and-usage-tracking/examples/starter-usage-routing-example.md

# Starter Usage Routing Example

## Example Metadata

```yaml
example_metadata:
  artifact_name: starter_usage_routing_example
  file_role: ai_routing_usage_example
  schema_ownership: none
  purpose: >
    Show one compact, realistic example of how AI surface inventory, monthly
    quota posture, routing decisions, planned usage budget, usage delta, and
    routing recommendations can work together during one PreCapNextDay flow.
    This file illustrates existing contracts only and does not define schemas.
  package_context: ai-routing-and-usage-tracking
  example_scope: single_flow_prompt_pack
  related_flow: F3
  related_project: Apex
  example_status: illustrative_only

boundaries:
  does_not_define:
    - routing_decision_schema
    - planned_usage_budget_schema
    - usage_delta_schema
    - routing_recommendation_packet_schema
    - AI_surface_inventory_schema
    - monthly_quota_map_schema
    - prompt_packet_schema
  volatile_claims_excluded:
    - exact_current_pricing
    - exact_current_quota_limits
    - exact_model_rankings
    - live_provider_availability
    - final_OpenRouter_model_mapping
```

## Scenario

```yaml
scenario:
  day_plan_context: PreCapNextDay_flow_prompt_pack
  date_placeholder: YYYY-MM-DD
  flow_id: F3
  flow_label: Apex_orchestration_buildout
  flow_goal: >
    Finalize one reference contract and one example file for the
    ai-routing-and-usage-tracking package, then capture whether the selected
    route was worth repeating.
  sprint_plan:
    S1:
      sprint_goal: Create routing-decision contract draft.
      expected_output_type: reference_contract
      prompt_task_type: file_generation
    S2:
      sprint_goal: Validate quota and scarcity boundaries against the contract.
      expected_output_type: validation_notes
      prompt_task_type: validation
    S3:
      sprint_goal: Capture usage delta and next-day routing learning.
      expected_output_type: usage_delta_summary
      prompt_task_type: prompt_result_feedback
```

## Input Excerpts

These excerpts show the kind of source context the routing package consumes. They are examples, not new schemas.

```yaml
AI_surface_inventory_excerpt:
  inventory_id: AI_surface_inventory_example
  surface_posture: operator_supplied_or_recently_verified
  available_surface_classes:
    - surface_class: subscription_frontier
      label: regular_frontier_chat
      availability_status: available
      best_fit:
        - structured_reasoning
        - prompt_pack_generation
        - architecture_tradeoffs
    - surface_class: quota_limited_frontier
      label: deep_research_surface
      availability_status: available_if_currently_verified
      best_fit:
        - source_grounded_research
        - claim_verification
        - broad_comparison
    - surface_class: supplemental_API_low_reasoning
      label: mechanical_batch_route
      availability_status: not_needed_for_this_flow
      best_fit:
        - low_risk_format_conversion
        - deterministic_extraction
    - surface_class: later_OpenRouter
      label: OpenRouter_later
      availability_status: todo_later
      best_fit:
        - future_low_risk_supplemental_batch
```

```yaml
monthly_quota_map_excerpt:
  quota_map_id: monthly_quota_map_example
  quota_posture: operator_supplied_or_recently_verified
  quota_items:
    - quota_name: deep_research_surface
      scarcity_class: managed
      posture: underused_but_not_free
      reset_pressure: medium
      planning_note: Spend only when evidence need justifies it.
    - quota_name: agent_run_surface
      scarcity_class: scarce
      posture: preserve_for_bounded_tool_like_execution
      reset_pressure: low
      planning_note: Save for file navigation or bounded multi-step execution.
```

## Planned Usage Budget Example

```yaml
planned_usage_budget_example:
  budget_id: planned_usage_budget_F3_example
  created_or_updated_at: YYYY-MM-DD
  budget_horizon:
    horizon_type: single_flow
    starts_at: YYYY-MM-DD
    ends_at: YYYY-MM-DD
    flow_id: F3
    sprint_id: NA
  planning_context:
    context_type: PreCapNextDay_flow_prompt_pack
    budget_goal: leverage_weighted_quality
    planning_assumption_status: valid_with_warnings
    source_artifact_refs:
      - flow_prompt_pack_F3_example
      - AI_surface_inventory_example
      - monthly_quota_map_example
  planned_usage_entries:
    - entry_id: planned_usage_entry_F3_S1_contract_generation
      related_prompt_or_sprint: F3_S1
      planned_surface_class: subscription_frontier
      cost_class: subscription_frontier
      scarcity_class: abundant
      planned_use_reason: >
        Contract generation needs strong structure and boundary control, but
        does not require fresh source-grounded research.
      expected_value: high
      fallback_if_unavailable: use_operator_directed_frontier_surface
    - entry_id: planned_usage_entry_F3_S2_validation
      related_prompt_or_sprint: F3_S2
      planned_surface_class: subscription_frontier
      cost_class: subscription_frontier
      scarcity_class: managed
      planned_use_reason: >
        Validation needs reasoning and consistency checking, not a scarce
        external research mode.
      expected_value: medium
      fallback_if_unavailable: defer_or_reduce_scope
    - entry_id: planned_usage_entry_F3_S3_capture
      related_prompt_or_sprint: F3_S3
      planned_surface_class: subscription_frontier
      cost_class: subscription_frontier
      scarcity_class: abundant
      planned_use_reason: >
        Usage learning capture is lightweight and should not spend scarce modes.
      expected_value: medium
      fallback_if_unavailable: manual_operator_capture
  scarce_mode_reservations:
    - reservation_label: preserve_deep_research_surface
      reserved_for:
        - source_grounded_verification
        - provider_claim_check
      spend_now: false
      reason: Current sprint uses supplied project context and does not require live research.
  planned_usage_totals:
    planned_subscription_frontier_prompts: 3
    planned_quota_limited_frontier_uses: 0
    planned_supplemental_API_uses: 0
    planned_OpenRouter_later_uses: 0
  validation_status: valid_with_warnings
  operator_review_flags:
    - quota_posture_should_be_verified_if_spending_scarce_modes
```

## Routing Decisions Example

```yaml
routing_decisions_example:
  decisions:
    - decision_id: routing_decision_F3_S1_contract_generation
      created_or_updated_at: YYYY-MM-DD
      source_packet_id: prompt_packet_F3_S1_contract_generation
      routing_mode: planned_flow_session
      routing_intent: maximize_quality
      task_summary: Generate one routing contract file with strict schema ownership.
      task_risk_profile:
        impact: 82
        risk: 64
        evidence_need: 42
        ambiguity: 58
        high_end_reasoning_score_total: 246
        route_sensitivity: high
      primary_route:
        route_surface_class: subscription_frontier
        model_or_surface_target: regular_frontier_chat
        provider_target: provider_unspecified
        cost_class: subscription_frontier
        scarcity_class: abundant
      alternate_route:
        route_surface_class: quota_limited_frontier
        model_or_surface_target: deep_research_surface
        provider_target: provider_unspecified
        cost_class: quota_limited_frontier
        scarcity_class: managed
      provider_rationale:
        summary: >
          Use a strong general frontier route because structure, boundary
          control, and validation matter more than cost minimization.
        confidence: medium
      quota_rationale:
        summary: >
          Do not spend scarce research capacity because the task uses supplied
          project context rather than fresh external evidence.
        scarcity_tradeoff: save_scarce_mode
      fallback_rule:
        fallback_when:
          - primary_surface_unavailable
          - output_quality_fails_contract
        fallback_action: retry_with_operator_selected_frontier_surface_or_reduce_scope
      expected_usage_capture:
        capture_in_usage_delta: true
        capture_fields:
          - actual_surface_class
          - planned_vs_actual_use
          - quality_signal
          - correction_overhead
      validation_status: valid_with_warnings
      operator_review_flags: []

    - decision_id: routing_decision_F3_S2_validation
      created_or_updated_at: YYYY-MM-DD
      source_packet_id: prompt_packet_F3_S2_validation
      routing_mode: validation_only_route
      routing_intent: balance_quality_and_cost
      task_summary: Validate routing contract boundaries and surface schema leakage.
      task_risk_profile:
        impact: 76
        risk: 71
        evidence_need: 35
        ambiguity: 46
        high_end_reasoning_score_total: 228
        route_sensitivity: moderate
      primary_route:
        route_surface_class: subscription_frontier
        model_or_surface_target: regular_frontier_chat
        provider_target: provider_unspecified
        cost_class: subscription_frontier
        scarcity_class: abundant
      alternate_route: null
      provider_rationale:
        summary: General reasoning is sufficient for contract validation against known package rules.
        confidence: medium
      quota_rationale:
        summary: Save quota-limited and scarce modes for evidence-heavy or tool-like work.
        scarcity_tradeoff: preserve_quota
      fallback_rule:
        fallback_when:
          - validation_confidence_low
        fallback_action: mark_operator_review_recommended
      expected_usage_capture:
        capture_in_usage_delta: true
        capture_fields:
          - defects_found
          - correction_overhead
          - operator_review_needed
      validation_status: valid
      operator_review_flags: []

    - decision_id: routing_decision_F3_S3_usage_capture
      created_or_updated_at: YYYY-MM-DD
      source_packet_id: prompt_packet_F3_S3_usage_capture
      routing_mode: supplemental_or_batch_execution
      routing_intent: minimize_cost_when_quality_sufficient
      task_summary: Capture actual usage and next-day route learning.
      task_risk_profile:
        impact: 48
        risk: 32
        evidence_need: 20
        ambiguity: 25
        high_end_reasoning_score_total: 125
        route_sensitivity: low
      primary_route:
        route_surface_class: subscription_frontier
        model_or_surface_target: regular_frontier_chat
        provider_target: provider_unspecified
        cost_class: subscription_frontier
        scarcity_class: abundant
      alternate_route:
        route_surface_class: supplemental_API_low_reasoning
        model_or_surface_target: mechanical_batch_route
        provider_target: OpenRouter_later
        cost_class: later_OpenRouter
        scarcity_class: unknown
      provider_rationale:
        summary: Lightweight capture can use a lower-cost route later, but OpenRouter mapping remains TODO.
        confidence: low
      quota_rationale:
        summary: No scarce quota should be spent on routine capture.
        scarcity_tradeoff: do_not_spend_scarce_mode
      fallback_rule:
        fallback_when:
          - OpenRouter_mapping_not_ready
          - capture_quality_uncertain
        fallback_action: use_manual_operator_capture_or_regular_frontier_surface
      expected_usage_capture:
        capture_in_usage_delta: true
        capture_fields:
          - actual_route_used
          - low_reasoning_route_sufficient
          - next_day_influence
      validation_status: operator_review_recommended
      operator_review_flags:
        - OpenRouter_mapping_todo_later
```

## Usage Delta Example

```yaml
usage_delta_example:
  usage_delta_id: usage_delta_F3_example
  capture_scope: flow
  capture_source: FlowRecap
  captured_at: YYYY-MM-DD
  related_usage_context:
    context_kind: flow_prompt_pack
    related_ids:
      flow_id: F3
      planned_usage_budget_id: planned_usage_budget_F3_example
      next_day_plan_id: next_day_plan_example
    project_context: Apex
    expected_output_type: reference_contract_and_usage_learning
    prompt_task_type: file_generation
  delta_items:
    - delta_item_id: usage_delta_item_F3_S1
      planned_route_ref: routing_decision_F3_S1_contract_generation
      actual_surface_class: subscription_frontier
      actual_cost_class: subscription_frontier
      planned_vs_actual: matched_plan
      observed_quality: strong
      correction_overhead: low
      usefulness: high
      learning_signal: Keep strong frontier route for contract generation.
    - delta_item_id: usage_delta_item_F3_S2
      planned_route_ref: routing_decision_F3_S2_validation
      actual_surface_class: subscription_frontier
      actual_cost_class: subscription_frontier
      planned_vs_actual: matched_plan
      observed_quality: acceptable
      correction_overhead: medium
      usefulness: medium
      learning_signal: Add stricter schema-leak checks before finalizing reference contracts.
    - delta_item_id: usage_delta_item_F3_S3
      planned_route_ref: routing_decision_F3_S3_usage_capture
      actual_surface_class: operator_manual_capture
      actual_cost_class: no_model_use
      planned_vs_actual: cheaper_than_planned
      observed_quality: sufficient
      correction_overhead: low
      usefulness: medium
      learning_signal: Routine usage capture can often be manual or low-reasoning later.
  aggregate_delta_summary:
    planned_routes_mostly_worked: true
    scarce_quota_spent: false
    subscription_frontier_overused: false
    supplemental_API_needed: false
    operator_review_needed: false
  routing_learning_summary:
    routes_to_reuse:
      - subscription_frontier_for_contract_generation
      - subscription_frontier_for_validation_when_schema_leak_risk_exists
    routes_to_deprioritize:
      - scarce_monthly_mode_for_supplied_context_contract_generation
    candidate_future_tests:
      - low_reasoning_capture_route_after_OpenRouter_mapping_exists
  next_planning_influence:
    influence_level: moderate
    recommendation: prefer_subscription_frontier_for_F3_contract_generation
    rationale: Strong output quality and low correction overhead justify repeating the route.
  validation_status: valid_with_warnings
  operator_review_flags:
    - OpenRouter_mapping_todo_later
```

## Routing Recommendation Packet Example

```yaml
routing_recommendation_packet_example:
  packet_id: routing_recommendation_F3_example
  generated_from_window:
    start_date: YYYY-MM-DD
    end_date: YYYY-MM-DD
    source_scope: same_day
  routes_to_prefer:
    - route_label: subscription_frontier_for_contract_generation
      provider_or_surface_class: subscription_frontier
      prefer_when:
        - task_is_reference_contract_generation
        - boundary_control_matters
        - source_context_is_supplied
      evidence_signal: high_value_output
      confidence: medium
  routes_to_avoid:
    - route_label: scarce_monthly_mode_for_supplied_context_generation
      avoid_when:
        - fresh_external_research_not_needed
        - task_can_be_completed_from_project_context
      reason: cost_not_justified
      recovery_route_hint: use_subscription_frontier_or_operator_review
  underused_quota_to_spend: []
  scarce_modes_to_save:
    - quota_name: deep_research_surface
      save_for:
        - source_grounded_research_needed
        - current_provider_or_standard_verification
      avoid_spending_on:
        - supplied_context_contract_generation
        - routine_usage_capture
      scarcity_reason: Scarce mode has better leverage on evidence-heavy tasks.
  models_or_modes_to_test:
    - candidate_label: low_reasoning_capture_route_later
      test_context: usage_delta_summary_after_OpenRouter_mapping_exists
      success_signal: correct compact usage summary with low correction overhead
      current_verification_needed: true
  prompt_patterns_that_worked:
    - pattern_label: explicit_contract_ownership_boundary
      worked_for:
        - routing_decision_contract
        - planned_usage_budget_contract
      reuse_hint: State owns and must_not_own before schema examples.
      feed_to_prompt_engineering: true
  next_day_influence:
    influence_level: moderate
    recommended_preCapNextDay_action: prefer_listed_routes
    suggested_flow_or_sprint_targets:
      - F3_S1
      - F3_S2
    rationale: Repeat subscription-frontier routing for Apex contract work unless next task requires live evidence.
  operator_review_flags:
    - OpenRouter_mapping_todo_later
```

## Failure Example

```yaml
failure_example:
  bad_pattern: cheapest_route_for_high_impact_contract_generation
  observed_problem: >
    The route selected a low-reasoning supplemental API path for a high-impact,
    ambiguous reference contract because cost was prioritized over quality.
  why_invalid:
    - impact_and_boundary_risk_were_material
    - prompt_quality_should_override_cost_efficiency
    - OpenRouter_mapping_was_not_final
    - workflow_fit_and_operator_decision_were_not_checked
  correction:
    - use_subscription_frontier_or_operator_selected_frontier_route
    - mark_OpenRouter_mapping_todo_later
    - capture_usage_delta_after_execution
    - update_routing_recommendation_packet_only_as_advisory_signal
```

## Operator Reading Notes

```yaml
operator_reading_notes:
  what_this_example_demonstrates:
    - route_planning_happens_before_execution
    - actual_usage_capture_happens_after_execution
    - recommendations_influence_next_day_planning_but_do_not_override_operator_choice
    - scarce_modes_are_saved_unless evidence_or_risk_justifies_spend
    - OpenRouter_remains_later_placeholder_until_mapping_is_verified
  what_to_copy_for_manual_tests:
    - scenario
    - planned_usage_budget_example
    - routing_decisions_example
    - usage_delta_example
    - routing_recommendation_packet_example
  what_not_to_copy_as_schema:
    - example_field_order
    - example_route_labels
    - example_quota_names
    - example_surface_labels
```
