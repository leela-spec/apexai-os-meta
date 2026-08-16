# Apex Weekly-Cycle Project Management Infrastructure Handover

```okf
handover:
  date: 2026-08-16
  repository: leela-spec/apexai-os-meta
  branch: main
  purpose: >
    Prepare the project-management infrastructure required to feed the first real
    full-portfolio Weekly Orchestrator / PreCap Week run with confirmed project
    truth instead of ad-hoc chat context.
  operator_goal: >
    Create a real working weekly plan across the complete portfolio for the first
    time, using repository-native Apex project, task, Session, Sync, ProjectStatus,
    and Weekly Orchestrator contracts so the resulting artifacts become testable
    examples for the orchestration infrastructure.
  orchestration_owner: subscription_ai_main_chat
  implementation_owner_next: separate_ai_chat_for_project_management_setup
  current_stage: before_project_capture_and_before_G1
  g1_allowed_now: false
```

## 1. Bigger Goal

```okf
bigger_goal:
  desired_end_state:
    - all real portfolio work needed for the target week is represented by repository-backed project/task truth
    - operator intent is converted into current project records without inventing state
    - confirmed project/task records are written only through the Apex Plan-Sync-Session backbone
    - deterministic Sync reports establish actionability, blockers, and current project signals
    - ProjectStatus produces a compact confirmed cross-project overview
    - PreCap Week consumes confirmed project references plus operator weekly intent and calendar constraints
    - G1 produces the first real weekly-plan packet for operator approval
    - later stages can use this real packet to test PreCap Next Day, execution, recap, merge, Session mutation, and loop closure
  target_week:
    run_date: 20260816
    week_id: 2026-W34
    weekday_scope: 2026-08-17_to_2026-08-21
  required_weekly_portfolio_categories:
    - Leela
    - MasterOfArts
    - Apex
    - Investment
    - Residual
```

## 2. Why Project Management Must Come First

```okf
problem:
  current_repository_state:
    epics_root: apex-meta/epics/
    confirmed_epics_detected:
      - narm-support-knowledgebase
    registry_current_scope: narm_support_tasks_only
    cross_project_status_truth: incomplete_for_full_portfolio_week
  consequence: >
    Running PreCap Week now would either rely on incomplete project truth or force
    the planning AI to reconstruct state from operator conversation, which defeats
    the purpose of testing the actual Apex project-management and weekly-flow
    infrastructure.
  rule: >
    Weekly planning is not the authority for creating project/task state. Missing
    projects and tasks must first be captured through Apex Plan, confirmed/written
    through Apex Session, validated/read through Apex Sync, and exposed to the
    weekly layer by reference.
```

## 3. Canonical Backbone and Authority Boundaries

```okf
backbone:
  apex_plan:
    role: propose_project_capture_epic_tasks_dependencies_priority_and_due_date_rationale
    authority: proposal_only
    may_not:
      - write durable task state
      - compute exact next-task ranking
      - mutate status
  apex_session:
    role: operator_gated_confirmed_write_and_mutation_authority
    authority: confirmed_state_writer
    produces:
      - mutation_records
      - planning_feed
      - task_plan.md
      - findings.md
      - progress.md
      - next-session.md
  apex_sync:
    role: deterministic_read_side_validation_and_computation
    authority: computed_reports_only
    reads: apex-meta/epics/*/[0-9][0-9][0-9].md
    produces:
      - next_action_report
      - blocker_report
      - dependency_validation_report
      - score_or_focus_reports_when_requested
      - registry_preview_or_explicit_registry_write
  project_status:
    role: compact_cross_project_confirmed_overview_for_weekly_planning
    input_rule: confirmed_session_and_sync_truth_only
  weekly_orchestrator:
    role: route_weekly_stages_and_hold_G1_G5
    state_authority: files_not_agent_memory
  precap_week:
    role: convert_confirmed_project_context_plus_operator_weekly_inputs_into_weekly_direction
    must_not_create:
      - project_database
      - task_records
      - prompt_packets
      - detailed_daily_plan
      - project_execution
      - calendar_events
```

## 4. Canonical Sources the Next AI Must Read Before Acting

```okf
required_reads:
  project_engine:
    - .claude/skills/apex-plan/SKILL.md
    - .claude/skills/apex-plan/references/task-record-contract.md
    - .claude/skills/apex-plan/references/decomposition-and-dependency-rules.md
    - .claude/skills/apex-plan/references/priority-urgency-focus-policy.md
    - .claude/skills/apex-plan/templates/epic-template.md
    - .claude/skills/apex-plan/templates/task-template.md
    - .claude/skills/apex-session/SKILL.md
    - .claude/skills/apex-session/references/handoff-and-next-session-contract.md
    - .claude/skills/apex-sync/SKILL.md
    - apex-meta/registry/index.md
    - apex-meta/epics/
  weekly_interface:
    - .claude/skills/weekly-orchestrator/SKILL.md
    - .claude/skills/weekly-orchestrator/references/handoff-schema.md
    - .claude/skills/PrecapWeek/SKILL.md
    - .claude/skills/PrecapWeek/weekly-plan-output-contract.md
    - .claude/skills/PrecapWeek/references/validation-checklist.md
  pilot_context:
    - FEE2/00-WEEKLY-ORCHESTRATION-PILOT.okf.md
    - FEE2/02-OPENCLAW-TRIGGER-EVALUATION-MATRIX.md
    - apex-meta/orchestration/README.md
```

## 5. Project-Management Infrastructure to Create

```okf
required_infrastructure:
  per_real_project:
    project_capture:
      durable_target: apex-meta/epics/<slug>/epic.md
      required_meaning:
        - project_goal
        - scope
        - constraints
        - source_basis
        - planning_context
    task_records:
      durable_target: apex-meta/epics/<slug>/<id>.md
      canonical_required_fields:
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
  portfolio_mapping:
    requirement: >
      Map real work into the fixed weekly categories Leela, MasterOfArts, Apex,
      Investment, and Residual without pretending that each category is necessarily
      one epic. Preserve real project boundaries; the weekly category is a planning
      layer classification, not a replacement for project structure.
  confirmed_state:
    requirement:
      - operator approves proposed project/task records
      - Apex Session performs confirmed durable writes
      - Session refreshes planning_feed and next-session context
  deterministic_validation:
    requirement:
      - run Apex Sync against confirmed task files
      - validate dependencies and malformed records
      - generate next-action and blocker reports needed by weekly planning
      - rebuild apex-meta/registry/index.md only through the explicit Sync registry path when required
  weekly_input_view:
    requirement:
      - generate a current ProjectStatus overview from confirmed Session/Sync context
      - store it under artifacts/weekly-plans/project-status-overview-<YYYYMMDD>.md
      - use references, not copied project bodies, in later weekly packets
```

## 6. Operator Interaction Model

```okf
operator_interaction:
  principle: operator_supplies_meta_truth_ai_proposes_structured_detail
  operator_should_supply_per_project:
    - project_name_or_workstream_name
    - plain_language_goal
    - current_state_in_rough_terms
    - what_should_move_next
    - known_deadlines_or_fixed_dates
    - known_blockers_or_dependencies
    - material_sources_or_repository_paths
    - explicit_exclusions_or_sensitive_context
  ai_should_derive_and_propose:
    - project_slug
    - epic_structure
    - task_decomposition
    - acceptance_criteria
    - definition_of_done
    - qualitative_priority
    - dependency_proposals
    - due_date_only_when_operator_evidence_supports_it
    - review_flags
  forbidden_inference:
    - invented_current_state
    - invented_deadlines
    - invented_dependencies
    - invented_operator_priority
    - invented_completion_status
```

## 7. Delegation Strategy

```okf
delegation:
  reason: >
    Keep the main subscription-AI conversation focused on orchestration, source
    authority, gates, validation, and cross-project coherence. Use separate AI
    chats for bounded project capture/decomposition so detailed project context
    does not overload or drift the orchestration thread.
  recommended_pattern:
    - one bounded AI chat may prepare one project or tightly related project cluster
    - each worker receives repository paths plus operator-provided meta details
    - each worker must produce an Apex Plan-compatible proposal only
    - no worker may silently write canonical state unless explicitly acting under the Session handoff
    - the orchestration chat reviews proposal completeness and cross-project consistency
    - confirmed writes are routed through Apex Session
  worker_return_contract:
    - sources_read
    - project_capture_record
    - proposed_epic_record
    - proposed_task_records
    - dependency_plan
    - priority_and_due_date_rationale
    - review_flags
    - unresolved_operator_questions
    - requested_session_write_handoff
```

## 8. Recommended Execution Sequence

```okf
execution_sequence:
  1:
    action: inventory_real_portfolio_projects
    output: operator_confirmed_project_list_mapped_to_weekly_categories
  2:
    action: collect_minimal_meta_input_for_each_project
    output: bounded_operator_source_packet_per_project
  3:
    action: delegate_project_capture_and_decomposition_to_separate_ai_chats
    output: Apex_Plan_compatible_proposals
  4:
    action: orchestration_review
    checks:
      - no_duplicate_epics
      - project_boundaries_make_sense
      - sources_are_preserved
      - task_records_match_current_contract
      - dependencies_are_proposals_not_fabricated_truth
      - no weekly planning has leaked into canonical project state
  5:
    action: operator_approval_of_project_and_task_proposals
    output: approved_for_session_handoff
  6:
    action: route_confirmed_records_to_apex_session
    output:
      - durable_epic_and_task_records
      - refreshed_planning_feed
      - refreshed_H6_handoff_context
  7:
    action: run_apex_sync_validation
    output:
      - dependency_validation
      - next_action_report
      - blocker_report
      - registry_current_or_explicitly_rebuilt
  8:
    action: generate_project_status_overview
    output: artifacts/weekly-plans/project-status-overview-20260816.md
  9:
    action: collect_week_specific_operator_inputs
    inputs:
      - weekly_intent
      - minimum_successful_weekly_outcome
      - per_category_priority_urgency_date_ratings
      - active_maintenance_deferred_roles
      - calendar_capacity_constraints
      - fixed_decision_dates
  10:
    action: run_PreCap_Week_G1
    output: artifacts/weekly-plans/weekly_plan_packet-20260816-2026-W34.md
    stop_condition: present_exact_G1_approval_question_and_do_not_run_G2
```

## 9. Current Known Repository Conditions

```okf
current_conditions:
  confirmed:
    - only narm-support-knowledgebase is currently present under apex-meta/epics/
    - apex-meta/registry/index.md currently reflects the NARM task set rather than the full portfolio
    - the current weekly project roster is fixed to Leela, MasterOfArts, Apex, Investment, Residual
    - the current PreCap Week contract can consume detailed project-state files and a compact ProjectStatus overview
    - Weekly Orchestrator must read confirmed Session planning context rather than reconstruct accepted truth from candidate artifacts
  caution:
    - older June task examples do not fully match the newest task-record contract
    - follow the current task-record contract for newly created records
    - historical handoff/session material from unrelated projects must not be reused as current project truth
```

## 10. Stop Conditions for the Next AI

```okf
stop_conditions:
  stop_and_ask_operator_when:
    - project_identity_or_scope_is_ambiguous
    - a claimed deadline_is_not_operator_or_source_supported
    - two_sources_conflict_on_current_state
    - a proposed_dependency_is_material_but_unproven
    - sensitive_material_would_need_to_be_exposed
  never_do_without_explicit_stage_authority:
    - run_PreCap_Week_G1
    - create_weekly_plan_packet
    - invoke_OpenClaw
    - execute_project_work
    - fabricate_status
    - mutate_confirmed_task_status
```

## 11. Immediate Next Action for the Receiving AI Chat

```okf
next_action:
  instruction: >
    Read the required project-engine and weekly-interface contracts from main.
    Then inventory what real projects/workstreams need representation for the
    upcoming full-portfolio week. Present the operator with the smallest possible
    project-intake questionnaire, one project at a time or in a compact portfolio
    table. Convert only operator-confirmed meta details into Apex Plan-compatible
    project/task proposals. Do not run G1 and do not create weekly-plan artifacts.
  first_operator_gate: approve_project_inventory_and_project_capture_order
```
