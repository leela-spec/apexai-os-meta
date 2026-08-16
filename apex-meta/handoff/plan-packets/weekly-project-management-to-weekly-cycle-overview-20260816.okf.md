```okf
okf:
  id: "weekly-project-management-to-weekly-cycle-overview-20260816"
  version: 1.0
  status: operator_review
  purpose: >
    Provide one end-to-end view of the intended Apex project-management and
    weekly-planning pipeline so the operator can verify direction before
    canonical project/task creation begins.

target:
  run_date: 2026-08-16
  target_week: 2026-W34
  weekdays:
    - 2026-08-17
    - 2026-08-18
    - 2026-08-19
    - 2026-08-20
    - 2026-08-21

weekly_categories:
  - Leela
  - MasterOfArts
  - Apex
  - Investment
  - Residual

core_principle:
  statement: >
    Build reliable project truth first, validate it, compress it into a
    cross-project status layer, and only then let the Weekly Orchestrator
    derive the week.
  authority_chain:
    - operator_source_truth
    - Apex_Plan_proposals
    - operator_approval
    - Apex_Session_confirmed_canonical_state
    - Apex_Sync_deterministic_validation
    - ProjectStatus_cross_project_summary
    - PreCap_Week_weekly_direction
    - later_daily_and_execution_stages

pipeline:

  - step: 0
    name: establish_pipeline_authority_and_working_memory
    purpose: >
      Ensure every AI window operates from current repository truth rather
      than reconstructing the workflow from chat memory.
    substeps:
      - id: 0.1
        action: read_current_Apex_skill_and_weekly_contracts
        inputs:
          - apex-plan contract
          - apex-session contract
          - apex-sync contract
          - weekly-orchestrator contract
          - PreCap Week contract
        output:
          - current_authority_model
      - id: 0.2
        action: read_current_portfolio_cursor_and_plan_packet_index
        output:
          - exact_resume_point
          - current_gate
      - id: 0.3
        action: save_intermediate_reasoning_checkpoints_to_GitHub
        rule: >
          Every significant investigation or bounded planning flow gets a
          durable checkpoint before moving to the next flow.
        output:
          - durable_AI_working_memory
    completion_condition:
      - future AI can resume from repository files without chat reconstruction

  - step: 1
    name: portfolio_inventory
    purpose: identify the real projects that can feed the weekly cycle
    current_state: substantially_complete_as_proposal
    substeps:
      - id: 1.1
        action: collect_operator_meta_level_project_inventory
        operator_input:
          - project_or_workstream_name
          - rough_goal_or_current_intent
        output:
          - raw_portfolio_inventory
      - id: 1.2
        action: map_items_to_fixed_weekly_categories
        output:
          - category_to_project_map
      - id: 1.3
        action: distinguish_real_projects_from_tasks_and_capacity_inputs
        examples:
          project:
            - Leela Core Interaction Development
            - ApexKB Evolution
          task_cluster:
            - Outstanding Business Invoices
          capacity_input_not_project:
            - Dating
        output:
          - normalized_project_inventory
      - id: 1.4
        action: identify_existing_initiatives_to_avoid_duplicate_epics
        examples:
          - First Real Weekly Flow -> existing FEE2 weekly pilot
          - First Apex Plan/Sync/Session setup -> current PM-backbone initiative
        output:
          - existing_initiative_mapping
    output:
      primary: portfolio_project_capture_index
      status: proposal_only

  - step: 2
    name: evidence_ground_each_project
    purpose: >
      Understand what already exists before decomposing work, so tasks describe
      real gaps rather than imagined greenfield work.
    repeat_for_each_project: true
    substeps:
      - id: 2.1
        action: locate_relevant_repository_and_authoritative_sources
        output:
          - source_map
      - id: 2.2
        action: read_current_code_specs_decisions_handoffs_or_process_SSOT
        output:
          - evidence_checkpoint
      - id: 2.3
        action: classify_existing_state
        classes:
          - already_implemented
          - partially_implemented
          - explicit_drift
          - genuinely_missing
          - unresolved_operator_decision
          - stale_management_artifact
          - unknown_insufficient_evidence
        output:
          - current_state_model
      - id: 2.4
        action: save_checkpoint_to_Apex_Git
        output:
          - reusable_project_evidence_packet
    output:
      examples_already_created:
        - Leela Home/Skill Tree/current resolution-context evidence
        - Leela decision-ledger triage
        - ApexKB lifecycle/value evidence
        - Investment OpenClaw Cron capability evidence

  - step: 3
    name: Apex_Plan_project_capture
    purpose: convert grounded project context into operator-reviewable project structures
    authority: Apex_Plan
    status: proposal_only
    repeat_for_each_new_project: true
    substeps:
      - id: 3.1
        action: define_project_goal
        rule: >
          Derived only from operator intent and evidence; no invented desired
          outcome.
        output:
          - project_capture_record
      - id: 3.2
        action: define_epic_boundary
        checks:
          - one coherent outcome
          - not merely a task
          - not duplicate of existing initiative
          - no artificial sub-epic hierarchy
        output:
          - proposed_epic_record
      - id: 3.3
        action: decompose_into_reviewable_tasks
        task_fields:
          - id
          - title
          - status
          - priority
          - due_date
          - depends_on
          - blocked_by
          - acceptance_criteria
          - definition_of_done
          - notes
          - source
        output:
          - proposed_task_records
      - id: 3.4
        action: propose_real_dependencies_only
        rule: >
          depends_on only when one task genuinely cannot be executed before
          another completes.
        output:
          - dependency_plan
      - id: 3.5
        action: add_priority_and_urgency_rationale
        rule:
          priority: qualitative_high_medium_low_only
          due_date: only_when_operator_or_source_supports_it
          exact_ranking: forbidden_here
        output:
          - qualitative_focus_rationale
      - id: 3.6
        action: surface_uncertainty_and_operator_decisions
        output:
          - review_flags
          - decision_packets
      - id: 3.7
        action: persist_plan_packet
        output:
          - "apex-meta/handoff/plan-packets/apex_plan_packet-<date>-<slug>.md"
    final_output:
      - complete_Apex_Plan_proposal_set

  - step: 4
    name: decision_closure_where_required
    purpose: >
      Resolve only decisions that materially change the project/task design or
      first execution slices.
    applies_when:
      - unresolved_operator_choice_changes_task_contract
      - conflicting_authoritative_sources
      - implementation_would_require_silent_product_choice
    substeps:
      - id: 4.1
        action: reconcile_stale_or_already_answered_questions_first
        output:
          - no_unnecessary_operator_questions
      - id: 4.2
        action: evidence_narrow_genuine_choices
        output:
          - bounded_options
          - consequences
          - recommendation_when_supported
      - id: 4.3
        action: obtain_operator_decision
        output:
          - confirmed_decision
      - id: 4.4
        action: integrate_decision_into_project_plan
        output:
          - revised_plan_packet
    current_Leela_examples:
      - QA-02_and_QA-11_resolution_profiles
      - QA-100_Home_override_lifetime
      - QA-138_narrowed_to_nonblocking_accessibility_policy
      - QA-73_narrowed_to_harmonization_migration_shell_status

  - step: 5
    name: operator_gate_on_project_inventory_and_capture
    purpose: >
      Prevent proposal-stage interpretation from becoming canonical project
      truth without operator validation.
    current_gate: THIS_IS_THE_NEXT_REAL_GATE
    review_scope:
      - project_inventory
      - project_boundaries
      - titles_and_slugs
      - proposed_task_decomposition
      - explicit_dependencies
      - priority_classification
      - unresolved_flags
    operator_outcomes:
      - approved_for_handoff
      - needs_revision
    output:
      approved_set:
        - operator_confirmed_project_capture_set
    important_boundary:
      - Apex_Plan_stops_here
      - no_canonical_epic_or_task_files_exist_yet

  - step: 6
    name: canonicalize_confirmed_projects
    purpose: write durable confirmed project/task truth
    authority: Apex_Session
    prerequisite:
      - step_5_approved
    repeat_for_each_approved_epic: true
    substeps:
      - id: 6.1
        action: prepare_before_after_mutation_preview
        output:
          - Session_mutation_preview
      - id: 6.2
        action: create_epic_container
        target:
          - "apex-meta/epics/<slug>/epic.md"
        output:
          - canonical_epic_record
      - id: 6.3
        action: create_canonical_task_records
        target:
          - "apex-meta/epics/<slug>/<id>.md"
        output:
          - canonical_task_records
      - id: 6.4
        action: record_source_and_operator_confirmation
        output:
          - traceable_confirmation_evidence
      - id: 6.5
        action: refresh_Session_handoff_and_planning_feed
        output:
          - task_plan.md
          - findings.md
          - progress.md
          - next-session.md
          - confirmed_planning_feed
    final_output:
      - canonical_cross_project_PM_database

  - step: 7
    name: deterministic_project_validation
    purpose: >
      Validate the confirmed graph mechanically instead of asking an LLM to
      estimate blockers, next tasks, or exact rankings.
    authority: Apex_Sync
    prerequisite:
      - canonical_task_records_exist
    substeps:
      - id: 7.1
        action: validate_task_shapes_and_dependencies
        output:
          - dependency_validation_report
      - id: 7.2
        action: compute_next_actions
        output:
          - deterministic_next_action_report
      - id: 7.3
        action: scan_explicit_blockers_and_stale_tasks
        output:
          - blocker_and_staleness_report
      - id: 7.4
        action: compute_priority_urgency_unlock_depth_focus_candidates
        output:
          - deterministic_focus_candidate_report
      - id: 7.5
        action: rebuild_or_preview_registry
        default: dry_run_first
        output:
          - registry_validation
    final_output:
      - validated_project_graph
      - deterministic_read_side_reports

  - step: 8
    name: project_status_overview
    purpose: >
      Compress project-level confirmed truth into the smallest useful
      cross-project input for weekly planning.
    inputs:
      - canonical_epics_and_tasks
      - Session_confirmed_planning_feed
      - Sync_reports
    substeps:
      - id: 8.1
        action: summarize_each_active_project
        include:
          - current_goal
          - confirmed_current_state
          - meaningful_next_actions
          - blockers
          - relevant_due_dates
          - current_decisions_or_uncertainty
        output:
          - per_project_status
      - id: 8.2
        action: map_projects_to_weekly_categories
        rule: >
          Category is a weekly planning lens, not necessarily the same thing as
          one epic.
        output:
          - category_status_view
      - id: 8.3
        action: save_cross_project_overview
        target:
          - "artifacts/weekly-plans/project-status-overview-20260816.md"
    final_output:
      - confirmed_cross_project_status_input

  - step: 9
    name: collect_week_specific_inputs
    purpose: >
      Add only information that is specific to this week and therefore should
      not live permanently inside project records.
    inputs_may_include:
      - operator_week_intent
      - exceptional_deadlines
      - appointments_or_calendar_constraints
      - desired_capacity_distribution
      - personal_capacity
      - temporary_context
    examples:
      - Dating_time_allocation
      - unusual_week_capacity
      - one_off_business_commitments
    output:
      - weekly_context_inputs
    rule:
      - do_not_turn_temporary_week_context_into_fake_project_tasks

  - step: 10
    name: PreCap_Week_G1
    purpose: >
      Convert confirmed project truth plus current-week context into weekly
      direction.
    authority: PreCap_Week_via_Weekly_Orchestrator
    prerequisites:
      - validated_project_graph
      - project_status_overview
      - weekly_context_inputs
    substeps:
      - id: 10.1
        action: load_fixed_roster
        categories:
          - Leela
          - MasterOfArts
          - Apex
          - Investment
          - Residual
      - id: 10.2
        action: load_confirmed_project_context
        preferred_sources:
          - Session_planning_feed
          - next-session.md
          - Sync_next_action_report
          - Sync_blocker_report
          - ProjectStatus_overview
      - id: 10.3
        action: synthesize_weekly_direction
        includes:
          - what_each_category_should_advance
          - qualitative_or_contractual_priority_and_urgency_representation
          - important_constraints
          - cross_project_tradeoffs
        forbidden:
          - creating_new_project_database_records
          - detailed_daily_scheduling
          - prompt_pack_generation
          - execution
          - calendar_mutation
      - id: 10.4
        action: write_G1_packet
        target:
          - "artifacts/weekly-plans/weekly_plan_packet-20260816-2026-W34.md"
      - id: 10.5
        action: stop_at_G1_operator_gate
        output:
          - weekly_direction_for_operator_review
    final_output:
      - G1_weekly_plan_packet

  - step: 11
    name: operator_weekly_direction_gate
    purpose: >
      Confirm the strategic weekly direction before the system translates it
      into individual days and execution packets.
    operator_reviews:
      - category_focus
      - relative_weekly_emphasis
      - major_tradeoffs
      - missing_context
      - explicit_exclusions
    output:
      - approved_G1_weekly_direction

  - step: 12
    name: daily_planning
    purpose: translate approved weekly direction into an executable day
    authority: later_Weekly_Orchestrator_stage
    repeat_each_day: true
    substeps:
      - select_relevant_confirmed_project_actions
      - combine_with_daily_constraints
      - form_bounded_flow_candidates
      - define_daily_scope
      - prepare_exact_execution_inputs
    outputs:
      - next_day_plan
      - flow_packet
      - prompt_pack
    gate:
      - operator_approval_before_external_or_consequential_execution

  - step: 13
    name: execution
    purpose: execute already-designed bounded work
    actors_may_include:
      - operator
      - Claude_Code
      - OpenClaw
      - subscription_AI
      - deterministic_scripts
    rule:
      - execution_actor_does_not_redesign_the_plan
    outputs:
      - execution_result
      - raw_evidence
      - receipts
      - failure_evidence

  - step: 14
    name: normalize_and_recap_execution
    purpose: convert raw execution evidence into candidate project-state changes
    substeps:
      - normalize_evidence
      - compare_expected_vs_actual
      - determine_candidate_task_progress
      - identify_new_findings_blockers_or_decisions
    outputs:
      - normalized_evidence_packet
      - flow_recap_packet
      - candidate_state_delta

  - step: 15
    name: confirmed_state_merge
    purpose: >
      Feed only operator-confirmed execution results back into project truth.
    authority: Apex_Session
    substeps:
      - present_candidate_state_delta
      - operator_confirms_consequential_changes
      - mutate_task_status_or_project_state
      - refresh_H6_and_planning_feed
    outputs:
      - updated_canonical_project_state
      - updated_Session_handoff

  - step: 16
    name: post_execution_sync
    purpose: >
      Recompute what the confirmed change means for remaining work.
    authority: Apex_Sync
    outputs:
      - new_next_actions
      - updated_blockers
      - updated_focus_candidates
      - drift_or_staleness_findings

  - step: 17
    name: close_feedback_loop
    purpose: >
      Ensure the next daily or weekly planning cycle uses the newly confirmed
      project state rather than stale plans.
    outputs:
      - refreshed_ProjectStatus
      - refreshed_daily_input
      - next_week_confirmed_input
    success_condition:
      - execution_result_is_visible_in_the_next_planning_cycle

artifact_flow:

  operator_meta_input:
    feeds:
      - Apex_Plan

  Apex_Plan:
    outputs:
      - project_capture_records
      - epic_proposals
      - task_proposals
      - dependency_proposals
      - decision_packets
    does_not_output:
      - canonical_project_state

  Apex_Session:
    inputs:
      - operator_approved_Plan_proposals
    outputs:
      - canonical_epics
      - canonical_tasks
      - confirmed_status_mutations
      - H6_handoff
      - planning_feed

  Apex_Sync:
    inputs:
      - canonical_epics_and_tasks
    outputs:
      - next_actions
      - blockers
      - stale_items
      - deterministic_scores
      - focus_candidates
      - registry_validation

  ProjectStatus:
    inputs:
      - Session
      - Sync
    output:
      - compact_cross_project_status

  PreCap_Week:
    inputs:
      - ProjectStatus
      - Session_context
      - Sync_reports
      - week_specific_inputs
    output:
      - weekly_direction_packet

  daily_orchestration:
    input:
      - approved_weekly_direction
    outputs:
      - daily_plan
      - flow_packet
      - prompt_pack

  execution:
    input:
      - frozen_execution_packet
    output:
      - evidence

  recap_and_session:
    input:
      - execution_evidence
    output:
      - confirmed_project_state_delta

current_position:

  completed_or_substantially_complete:
    - step_0_authority_and_durable_working_memory
    - step_1_portfolio_inventory_proposal
    - step_2_evidence_grounding_for_major_projects
    - step_3_Apex_Plan_project_capture_proposals
    - substantial_step_4_decision_triage_for_Leela

  current_gate:
    step: 5
    name: operator_gate_on_project_inventory_and_capture

  not_started_as_canonical_work:
    - step_6_Apex_Session_project_creation
    - step_7_Apex_Sync_validation
    - step_8_ProjectStatus
    - step_9_week_specific_input_capture
    - step_10_PreCap_Week_G1

direction_check:

  intended_result_before_weekly_planning:
    - every_real_active_project_has_a_canonical_epic_or_known_existing_mapping
    - useful_work_is_decomposed_into_canonical_tasks
    - dependencies_are_explicit
    - unsupported_deadlines_are_absent
    - unresolved_decisions_are_visible
    - Sync_can_compute_real_next_actions
    - Weekly_planner_receives_compact_confirmed_cross_project_truth

  intended_result_after_G1:
    - one_clear_weekly_direction_across_all_five_categories
    - no_project_truth_invented_by_the_weekly_planner
    - no_daily_overplanning_yet
    - operator_can_adjust_weekly_tradeoffs_before_execution_planning

  anti_patterns_this_pipeline_is_designed_to_prevent:
    - planning_the_week_directly_from_chat_memory
    - inventing_tasks_inside_PreCap_Week
    - treating_weekly_categories_as_project_database_structure
    - creating_duplicate_epics_for_existing_initiatives
    - letting_execution_results_change_state_without_confirmation
    - asking_an_LLM_to_fake_deterministic_Sync_results
    - carrying_stale_project_plans_forward
    - turning_personal_capacity_inputs_into_artificial_projects
    - making_OpenClaw_or_an_execution_AI_the_planner

operator_verification_focus:
  - >
    Is the sequence Project Truth -> Validation -> ProjectStatus -> Weekly
    Direction -> Daily Planning -> Execution -> Confirmed Feedback the right
    macro architecture?
  - >
    Do you want ProjectStatus as the explicit compression layer between project
    management and PreCap Week?
  - >
    Is the current rule correct that weekly categories are planning lenses,
    while several independent epics can sit underneath one category?
  - >
    Is the Session gate correctly placed after all Plan packets are reviewed,
    rather than writing each project piecemeal while still discovering the
    portfolio?
  - >
    Is G1 intentionally strategic/minimal enough, with detailed daily planning
    deferred until after weekly-direction approval?
```
