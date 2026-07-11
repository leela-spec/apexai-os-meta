```yaml
round5_review:
  J9:
    first_screen_card:
      title: Status Merge Decision
      shows:
        - candidate_change
        - current_accepted_state
        - proposed_difference
        - evidence_strength
        - conflicts_or_review_warning
        - current_decision_state
        - exact_next_action
      state_language:
        - candidate
        - approved_for_merge
        - rejected
        - deferred
        - unresolved
        - merged
      critical_rule: approved_for_merge_is_not_merged

    essential_sections:
      - current_accepted_state_summary
      - proposed_change_summary
      - evidence_and_conflicts
      - confidence_or_review_warning
      - durable_effect_if_approved
      - compact_machine_handoff:
          - candidate_project_status_delta_ref
          - previous_state_ref
          - review_decision
          - conflict_resolution
          - merge_proposal_ref
          - evidence_refs
          - confidence
          - operator_review_flags

    operator_actions:
      - approve_for_merge
      - edit_change
      - reject_change
      - defer_change
      - request_more_evidence
      - leave_unresolved

    boundary:
      may:
        - review_candidate_change
        - resolve_or_expose_conflicts
        - classify_review_decision
        - create_merge_proposal
      must_not:
        - silently_mutate_state
        - claim_merge_before_execution
        - update_project_KB_directly
        - reproduce_full_FlowRecap

    degraded_behavior:
      missing_previous_state:
        result: unresolved
        action: request_or_reference_current_accepted_state
      weak_evidence:
        result: candidate_with_review_warning
        action: lower_confidence_and_block_approval_when_material
      conflicting_evidence:
        result: unresolved
        action: preserve_conflict_and_require_operator_resolution
      safe_review_but_write_owner_missing:
        result: approved_for_merge
        action: retain_proposal_without_claiming_merge
      merge_execution_unconfirmed:
        result: approved_for_merge
        action: do_not_display_merged

    acceptance_checks:
      - first_screen_answers_change_evidence_and_decision
      - current_and_candidate_state_are_separate
      - conflicts_appear_before_approval
      - approved_for_merge_is_not_merged
      - merge_proposal_is_not_durable_state
      - project_KB_write_owner_is_preserved
      - evidence_and_confidence_are_visible_when_material
      - machine_handoff_contains_only_merge_minimum

  J10:
    first_screen_card:
      title: Project KB Update
      shows:
        - accepted_input
        - knowledge_change
        - target_location
        - change_type
        - replaced_or_preserved_knowledge
        - provenance
        - execution_decision
        - exact_next_action

    essential_sections:
      - accepted_input_reference
      - knowledge_change_summary
      - target_KB_location
      - change_type:
          allowed:
            - add
            - correct
            - supersede
            - consolidate
            - no_update
            - operator_review_needed
      - existing_knowledge_effect:
          - replace
          - preserve
          - consolidate
          - none
      - provenance
      - durable_effect_if_executed
      - compact_machine_handoff:
          - accepted_change_ref
          - target_project_ref
          - target_KB_location
          - knowledge_change_type
          - provenance_refs
          - superseded_knowledge_refs
          - update_execution_decision
          - operator_review_flags

    operator_actions:
      - execute_update
      - edit_update
      - choose_target
      - preserve_existing
      - mark_no_update
      - request_review
      - defer_update

    boundary:
      may:
        - prepare_accepted_KB_update
        - identify_target_and_provenance
        - expose_superseded_or_conflicting_knowledge
        - request_operator_confirmation_before_write
      must_not:
        - accept_candidate_project_state
        - become_project_status_dashboard
        - store_unverified_inference_as_fact
        - duplicate_full_source_artifact

    degraded_behavior:
      input_not_accepted:
        change_type: operator_review_needed
        action: route_back_to_J9
      target_location_unclear:
        change_type: operator_review_needed
        action: present_candidate_targets_without_writing
      conflicting_existing_knowledge:
        change_type: operator_review_needed
        action: preserve_both_refs_and_request_resolution
      provenance_missing:
        change_type: no_update
        action: do_not_store_as_fact
      no_durable_knowledge:
        change_type: no_update
        action: close_without_KB_mutation

    acceptance_checks:
      - accepted_input_is_explicit
      - target_location_is_visible
      - exactly_one_change_type_is_selected
      - replaced_and_preserved_knowledge_are_distinguished
      - provenance_supports_the_update
      - unverified_inference_is_not_stored_as_fact
      - execution_decision_is_separate_from_preparation
      - machine_handoff_contains_only_update_minimum

  J11:
    first_screen_card:
      title: Project Status Overview
      shows:
        - active_project_count
        - blocked_or_at_risk_count
        - review_needed_count
        - stale_or_missing_count
        - highest_priority_next_action
      primary_layout: compact_project_cards_or_short_rows
      avoid: wide_default_table

    essential_sections:
      - active_projects_or_workstreams:
          per_item:
            - project_name
            - accepted_status
            - blocker_or_risk
            - next_action
            - review_needed
            - freshness_or_staleness
            - drilldown_ref
      - cross_project_attention_summary
      - stale_missing_or_conflicting_status
      - compact_machine_handoff:
          - overview_ref
          - active_project_refs
          - accepted_status_refs
          - blocker_refs
          - next_action_refs
          - review_needed_refs
          - freshness_status
          - relevant_constraints

    operator_actions:
      - open_project
      - review_blocker
      - review_stale_status
      - use_as_context
      - request_refresh
      - no_action

    boundary:
      may:
        - aggregate_accepted_project_status
        - flag_stale_missing_or_conflicting_status
        - provide_cross_project_navigation
      must_not:
        - accept_candidate_updates
        - perform_status_merge
        - become_full_project_database_dump
        - invent_status_for_missing_projects

    degraded_behavior:
      missing_project_status:
        display: status_missing
        action: provide_refresh_or_source_reference
      stale_status:
        display: stale_with_last_known_date
        action: lower_context_confidence
      conflicting_accepted_sources:
        display: conflict_requires_review
        action: show_refs_without_selecting_truth
      no_active_projects:
        display: no_active_status_available
        action: do_not_invent_work
      partial_overview:
        display: partial_coverage
        action: identify_omitted_or_unknown_projects

    acceptance_checks:
      - overview_is_scannable_without_wide_table
      - only_accepted_status_is_presented_as_current_truth
      - blockers_next_actions_and_review_needs_are_visible
      - freshness_is_visible_per_project_when_material
      - missing_status_is_not_invented
      - candidate_updates_are_not_accepted
      - drilldown_references_replace_database_duplication
      - machine_handoff_contains_only_cross_project_context_minimum

  J12:
    first_screen_card:
      title: AI Routing
      shows:
        - task_context
        - recommended_route
        - short_rationale
        - important_constraints
        - confidence_or_warning
        - material_alternatives
        - operator_approval_needed
        - exact_next_action

    essential_sections:
      - task_context
      - recommended_route:
          includes:
            - selected_surface_or_model_class
            - fallback_route_when_material
      - short_rationale
      - important_constraints
      - alternatives_when_material:
          per_alternative:
            - route
            - main_tradeoff
      - evidence_and_confidence
      - operator_override_note
      - compact_machine_handoff:
          - routing_recommendation_ref
          - task_context_ref
          - recommended_route
          - selected_surface_or_model
          - fallback_route
          - constraints
          - evidence_refs
          - confidence
          - operator_decision
          - operator_review_flags

    operator_actions:
      - approve_route
      - choose_alternative
      - override_route
      - request_clarification
      - defer
      - no_route_needed

    boundary:
      may:
        - recommend_surface_model_or_execution_route
        - use_J8_learning_as_advisory_evidence
        - use_J11_project_context
        - expose_tradeoffs_and_constraints
      must_not:
        - execute_route
        - create_flow_plan
        - generate_prompt_pack
        - overwrite_routing_rules_automatically
        - invent_current_cost_quota_or_product_limits

    degraded_behavior:
      insufficient_task_context:
        result: clarification_needed
        action: state_one_missing_routing_input
      missing_surface_inventory:
        result: low_confidence_abstract_route
        action: use_stable_surface_class_only
      missing_quota_or_cost_evidence:
        result: route_without_current_resource_claim
        action: mark_resource_constraint_unknown
      conflicting_advisory_learning:
        result: operator_review_needed
        action: show_conflict_without_automatic_override
      no_special_route_required:
        result: no_route_needed
        action: avoid_creating_unnecessary_routing_work

    acceptance_checks:
      - first_screen_answers_route_reason_alternatives_and_approval
      - recommendation_is_advisory_until_operator_decision
      - J8_learning_does_not_override_routing
      - J11_context_does_not_become_route_decision
      - alternatives_appear_only_when_material
      - current_cost_quota_and_product_claims_require_evidence
      - route_is_not_executed
      - plan_and_prompt_owners_are_preserved
      - machine_handoff_contains_only_execution_route_minimum

  relationships:
    J7_to_J9:
      provides:
        - candidate_project_status_delta_ref
        - evidence_refs
        - confidence
        - conflicts
        - operator_review_flags
      J9_adds:
        - review_decision
        - conflict_resolution
        - merge_proposal
      ownership_rule: J7_interprets_execution_J9_reviews_candidate_state

    J9_to_J10:
      condition: accepted_change_contains_durable_project_knowledge
      provides:
        - accepted_change_ref
        - provenance
        - KB_update_candidate
      J10_adds:
        - target_KB_location
        - knowledge_change_type
        - update_execution_decision
      ownership_rule: J9_accepts_for_merge_J10_prepares_or_executes_KB_write

    J9_to_J11:
      condition: state_change_has_been_durably_merged
      provides:
        - accepted_status_ref
        - effective_change
      rule: approved_for_merge_is_not_yet_overview_truth

    J8_to_J12:
      provides:
        - advisory_route_signal
        - task_context
        - outcome_quality
        - confidence
        - evidence_ref
      rule: usage_learning_never_overrides_routing_automatically

    J11_to_J12:
      provides:
        - active_project_context
        - current_priority_or_blocker
        - relevant_constraints
      rule: overview_context_is_not_a_route_decision

    J12_to_J4_and_J5:
      condition: route_is_operator_approved
      provides:
        - approved_route_ref
        - selected_surface_or_model
        - constraints
      rule: J12_does_not_create_execution_cards_or_prompts

  decisions_requested:
    - keep
    - change
    - reject
```