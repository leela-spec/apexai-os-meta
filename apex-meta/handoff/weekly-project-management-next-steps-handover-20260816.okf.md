```okf
okf:
  id: "weekly-project-management-next-steps-handover-20260816"
  version: 1.0
  status: ready_for_receiving_ai
  document_role: next_ai_execution_handover
  created: 2026-08-16
  week: 2026-W34
  purpose: >
    Allow another AI chat/window to continue the first real portfolio-to-weekly
    Apex workflow from durable repository truth without reconstructing prior
    reasoning from chat memory.

receiving_ai_mission:
  primary_goal: >
    Continue from the completed Apex Plan proposal stage through the operator
    gate, Apex Session canonicalization, Apex Sync validation, ProjectStatus,
    week-specific input capture, and PreCap Week G1.
  execution_style:
    - read_repository_truth_before_each_stage
    - work_iteratively
    - persist_intermediate_checkpoints_to_GitHub
    - do_not_depend_on_chat_memory
    - do_not_silently_infer_operator_decisions
    - preserve_Apex_authority_boundaries

repository:
  full_name: leela-spec/apexai-os-meta
  branch: main

start_here_in_order:
  - path: apex-meta/handoff/weekly-project-management-next-steps-handover-20260816.okf.md
    role: this_handover
  - path: apex-meta/handoff/plan-packets/weekly-project-management-to-weekly-cycle-overview-20260816.okf.md
    role: end_to_end_stage_and_artifact_architecture
  - path: apex-meta/handoff/portfolio-project-capture-cursor-20260816.md
    role: exact_current_gate_and_resume_cursor
  - path: apex-meta/handoff/plan-packets/portfolio-project-capture-index-20260816-2026-W34.md
    role: index_of_all_project_packets_and_supporting_evidence

source_loading_rule:
  principle: >
    Load the smallest sufficient current context for the stage being executed.
    Do not preload every historical handover or reconstruct accepted work from
    prior conversation history.
  before_each_project_or_mutation:
    - read_the_current_plan_packet
    - read_the_relevant_current_source_repository_when_needed
    - read_the_current_skill_contract_for_the_authority_being_invoked
    - persist_any_material_new_evidence_before_advancing

current_state:
  pipeline_stage: 5
  stage_name: operator_gate_on_project_inventory_and_capture
  Apex_Plan_proposal_work: substantially_complete
  canonical_new_project_files_created: false
  new_project_Apex_Sync_run: false
  ProjectStatus_created: false
  PreCap_Week_G1_run: false

portfolio_proposal_scope:
  Leela:
    - leela-core-interaction-development
    - leela-product-decisions
    - leela-project-management-cleanup
  MasterOfArts:
    - masterofarts-website-definition
    - transendance-concept
    - business-invoicing
  Apex:
    new_epic:
      - apex-kb-evolution
    extend_existing_not_duplicate:
      - first-real-weekly-flow
      - first-apex-plan-sync-session-project-management
  Investment:
    - investment-intelligence-automation
  Residual:
    - apartment-improvements
  weekly_capacity_only:
    - dating

fixed_weekly_categories:
  - Leela
  - MasterOfArts
  - Apex
  - Investment
  - Residual

current_gate:
  from: Apex_Plan_proposal_state
  to: Apex_Session_confirmed_canonical_state
  operator_review_required: true
  accepted_operator_outcomes:
    - approved_for_handoff
    - needs_revision
  important_rule: >
    The existence of this handover, cursor, project packets, or prior assistant
    recommendation does not itself constitute operator approval for canonical
    mutation.

next_steps:

  - step: A
    name: operator_verification_of_pipeline_and_portfolio
    authority: operator
    inputs:
      - weekly-project-management-to-weekly-cycle-overview-20260816.okf.md
      - portfolio-project-capture-index-20260816-2026-W34.md
      - project_plan_packets_as_needed
    action: >
      Resolve any operator-requested corrections to the macro pipeline,
      project boundaries, task decomposition, dependencies, priorities, or
      unresolved decisions.
    outputs:
      approved:
        - operator_confirmed_project_capture_set
      revision:
        - revised_Apex_Plan_packets
    stop_condition:
      - do_not_enter_Apex_Session_without_operator_approval

  - step: B
    name: prepare_Apex_Session_mutation_preview
    authority: Apex_Session
    prerequisite:
      - operator_approved_project_capture_set
    required_skill_entrypoint:
      - skills://apex-session
    actions:
      - read_current_Apex_Session_contract_fully
      - derive_exact_canonical_files_to_create_from_approved_packets
      - produce_before_after_preview
      - preserve_sources_and_review_flags
      - distinguish_new_epics_from_existing_initiative_extensions
    outputs:
      - Session_mutation_preview
      - exact_file_write_manifest
    canonical_targets:
      - apex-meta/epics/<slug>/epic.md
      - apex-meta/epics/<slug>/<id>.md
      - required_Session_H6_or_planning_feed_artifacts
    forbidden:
      - silent_status_mutation
      - creating_duplicate_Apex_weekly_or_PM_epics
      - converting_dating_into_task_records

  - step: C
    name: apply_confirmed_canonical_project_state
    authority: Apex_Session
    prerequisite:
      - Session_gate_satisfied_under_current_contract
    actions:
      - create_approved_epic_records
      - create_approved_task_records
      - record_confirmation_and_sources
      - refresh_Session_handoff_and_planning_feed
    outputs:
      - canonical_cross_project_PM_database
      - refreshed_Session_context

  - step: D
    name: run_Apex_Sync_validation
    authority: Apex_Sync
    prerequisite:
      - canonical_project_task_files_exist
    required_skill_entrypoint:
      - skills://apex-sync
    execution_rule:
      - use_the_canonical_sync_script_not_LLM_estimation
      - dry_run_first
    actions:
      - validate_task_graph
      - validate_dependencies
      - compute_next_actions
      - scan_blockers
      - detect_staleness_or_drift
      - compute_priority_urgency_unlock_depth_focus_candidates
      - preview_or_rebuild_registry_only_per_contract
    outputs:
      - deterministic_dependency_report
      - deterministic_next_action_report
      - blocker_staleness_report
      - focus_candidate_report
      - registry_validation
    repair_rule: >
      Any structural correction must be routed back through the correct
      Plan/Session authority rather than directly patched by Sync narrative.

  - step: E
    name: generate_ProjectStatus
    purpose: >
      Compress confirmed project truth into a minimal cross-project status
      layer for weekly planning.
    inputs:
      - canonical_epics_and_tasks
      - Session_planning_feed
      - Sync_reports
    target:
      - artifacts/weekly-plans/project-status-overview-20260816.md
    required_content_per_project:
      - current_goal
      - confirmed_current_state
      - meaningful_next_actions
      - blockers
      - relevant_due_dates
      - relevant_decisions_or_uncertainty
    category_rule: >
      Weekly categories are planning lenses. Do not force a one-category-one-epic
      database structure.
    output:
      - confirmed_cross_project_status_input

  - step: F
    name: collect_week_specific_inputs
    purpose: >
      Capture W34-only constraints that should not be stored as permanent
      project truth.
    inputs_may_include:
      - operator_week_intent
      - calendar_constraints
      - exceptional_deadlines
      - temporary_capacity_constraints
      - desired_category_emphasis
      - dating_time_slot
    output:
      - weekly_context_inputs
    rule:
      - temporary_week_context_must_not_become_fake_project_tasks

  - step: G
    name: run_PreCap_Week_G1
    authority: Weekly_Orchestrator_and_PreCap_Week
    prerequisite:
      - canonical_state_exists
      - Sync_validation_complete
      - ProjectStatus_complete
      - weekly_context_inputs_available_or_missing_items_explicitly_named
    actions:
      - load_fixed_five_category_roster
      - load_latest_confirmed_Session_context
      - load_relevant_Sync_reports
      - load_ProjectStatus
      - synthesize_weekly_direction_only
    target:
      - artifacts/weekly-plans/weekly_plan_packet-20260816-2026-W34.md
    forbidden:
      - new_project_database_creation
      - detailed_daily_schedule
      - prompt_pack_generation
      - project_execution
      - calendar_mutation
    output:
      - G1_weekly_direction_packet
    final_gate:
      - stop_for_operator_G1_approval

post_G1_sequence_for_orientation_only:
  - approved_G1_weekly_direction
  - daily_or_next_day_planning
  - bounded_flow_packet_and_prompt_pack
  - operator_gate_before_external_or_consequential_execution
  - execution
  - evidence_normalization
  - FlowRecap_candidate_state_delta
  - Apex_Session_confirmed_state_merge
  - Apex_Sync_recomputation
  - refreshed_ProjectStatus_and_next_planning_input

artifact_ownership:
  Apex_Plan:
    owns:
      - capture_proposals
      - decomposition_proposals
      - dependency_proposals
      - qualitative_priority_and_focus_rationale
    must_not_own:
      - canonical_mutation
      - exact_ranking
  Apex_Session:
    owns:
      - confirmed_canonical_writes
      - confirmed_status_mutation
      - H6_and_next_session_context
      - planning_feed
  Apex_Sync:
    owns:
      - deterministic_read_side_computation
      - dependency_validation
      - next_actions
      - blockers
      - staleness_and_drift
      - exact_focus_computation
  ProjectStatus:
    owns:
      - compact_confirmed_cross_project_summary
  PreCap_Week:
    owns:
      - weekly_direction_only

critical_do_not_do:
  - do_not_rebuild_project_inventory_from_chat_memory
  - do_not_treat_old_NARM_Session_state_as_current_portfolio_truth
  - do_not_create_duplicate_epics_for_existing_Apex_initiatives
  - do_not_infer_priorities_or_due_dates_without_source_support
  - do_not_infer_completion_status
  - do_not_make_OpenClaw_a_planner
  - do_not_run_G1_before_project_truth_and_ProjectStatus_exist
  - do_not_fake_Apex_Sync_outputs
  - do_not_turn_dating_into_a_backlog
  - do_not_silently_resolve_Leela_product_choices

checkpoint_policy:
  rule: >
    After each material bounded workstep, write a concise durable checkpoint or
    update the relevant packet before moving on. The next AI must be able to
    restart from GitHub without needing the previous chat window.
  especially_checkpoint_after:
    - operator_pipeline_corrections
    - operator_project_capture_approval
    - Session_mutation_preview
    - canonical_write_completion
    - Sync_validation
    - ProjectStatus_generation
    - week_specific_input_capture
    - G1_generation_and_gate_result

success_definition_for_next_AI_session:
  minimum_success: >
    Reach the next legitimate authority gate with every intermediate artifact
    persisted and no reliance on conversational memory.
  preferred_success_if_operator_approval_is_available: >
    Complete Apex Session canonicalization, Apex Sync validation, ProjectStatus,
    week-specific input capture, generate the W34 G1 packet, and stop at the G1
    operator gate.

resume_instruction: >
  Read this handover, the pipeline overview, the portfolio cursor, and the
  portfolio index. Continue from the current operator gate. Do not redo prior
  evidence work unless a current packet explicitly identifies an unresolved
  evidence gap or the operator asks for re-verification.
```
