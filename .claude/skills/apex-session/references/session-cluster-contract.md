# Session Cluster Contract

## package_role

~~~yaml
package_role:
  package_name: apex-session
  package_path: ".claude/skills/apex-session/"
  cluster: C_SESSION
  role: >
    Produce final Apex session artifacts, gated mutation records, state deltas,
    entity update records, and planning-layer handoff context from current
    task/session evidence.

  primary_outputs:
    - task_plan.md
    - findings.md
    - progress.md
    - next-session.md
    - status_mutation_record
    - before_after_preview
    - operator_validation_record
    - state_delta_summary
    - entity_update_record
    - planning_feed

  storage_roots:
    state_root: apex-meta/
    harmonization_root: apex-meta/harmonization/
    epics_root: apex-meta/epics/
    handoff_root: apex-meta/handoff/
    registry_root: apex-meta/registry/
    scripts_root: scripts/
    skills_root: .claude/skills/
~~~

`apex-session` is the C_SESSION package. It converts active session evidence into final handoff material and validated mutation records. It does not create new project plans, compute exact next actions, rebuild registries, or execute scripts.

## C_SESSION_process_scope

~~~yaml
C_SESSION_process_scope:
  cluster_name: C_SESSION
  owns:
    - PM6_update_status
    - KB1_write_session_progress
    - KB2_extract_state_deltas
    - KB3_maintain_entity_files
    - KB6_produce_next_session_context
    - PD5_operator_validation_for_mutation
    - PD6_feed_planning_layer

  boundary_note:
    - PD3_unlock_depth_context_can_be_recorded_but_not_computed

  status_enum_H1:
    - open
    - in-progress
    - blocked
    - done
    - deferred

  handoff_format_H6:
    files:
      - task_plan.md
      - findings.md
      - progress.md
      - next-session.md
    next_session_sections:
      - Current Step
      - Open Items
      - Risks
      - Decisions Made
      - Next Actions
~~~

## owned_processes

~~~yaml
owned_processes:
  PM6_update_status:
    responsibility: >
      Validate and record requested status changes using H1 status values,
      before_after_preview, and operator_validation_record.
    required_outputs:
      - status_mutation_record
      - before_after_preview
      - operator_validation_record

  KB1_write_session_progress:
    responsibility: >
      Produce or update progress-oriented session artifacts that log actions
      taken, status mutations, state deltas, errors, and review flags.
    required_outputs:
      - progress.md

  KB2_extract_state_deltas:
    responsibility: >
      Extract durable changes from session evidence, preserve raw source basis,
      and flag unresolved context or source conflicts.
    required_outputs:
      - state_delta_summary

  KB3_maintain_entity_files:
    responsibility: >
      Create entity update records for durable changes to tasks, projects,
      artifacts, concepts, people, tools, or sources.
    required_outputs:
      - entity_update_record

  KB6_produce_next_session_context:
    responsibility: >
      Produce next-session context that preserves Current Step, Open Items,
      Risks, Decisions Made, and Next Actions.
    required_outputs:
      - next-session.md
      - next_session_context

  PD5_operator_validation_for_mutation:
    responsibility: >
      Require operator validation for consequential status or entity changes
      before treating mutation records as confirmed.
    required_outputs:
      - operator_validation_record

  PD6_feed_planning_layer:
    responsibility: >
      Prepare clean planning_feed material for apex-plan without computing
      ranking, blocker state, registry state, scores, or new decomposition.
    required_outputs:
      - planning_feed
~~~

## excluded_processes

~~~yaml
excluded_processes:
  new_project_capture:
    route_to: apex-plan
  new_project_decomposition:
    route_to: apex-plan
  dependency_graph_scoring:
    route_to: apex-sync
  exact_next_task_ranking:
    route_to: apex-sync
  blocker_scan:
    route_to: apex-sync
  stale_detection:
    route_to: apex-sync
  registry_rebuild:
    route_to: apex-sync
  drift_detection:
    route_to: apex-sync
  priority_score_computation:
    route_to: apex-sync
  urgency_score_computation:
    route_to: apex-sync
  unlock_depth_computation:
    route_to: apex-sync_or_later_custom_helper
  script_execution:
    route_to: apex-sync_or_external_application_flow
  calendar_operations:
    route_to: out_of_scope
  public_web_research:
    route_to: out_of_scope
~~~

## cross_package_routing

~~~yaml
cross_package_routing:
  apex-plan:
    owns:
      - project_task_capture
      - project_decomposition
      - dependency_proposals
      - planning_packet_creation
    apex-session_may_send:
      - planning_feed
      - next_session_context
      - durable_findings
      - review_flags
      - unresolved_context

  apex-sync:
    owns:
      - next_action_computation
      - blocker_detection
      - registry_rebuild
      - drift_detection
      - scoring
      - exact_focus_candidate_reports
      - deterministic_Python_reports
    apex-session_may_send:
      - status_mutation_record
      - state_delta_summary
      - depends_on_context
      - raw_source_ref
      - raw_source_path
      - review_flags

  apex-session:
    owns:
      - session_artifact_creation
      - gated_status_mutation
      - before_after_preview
      - handoff_and_next_session_context
      - state_deltas
      - operator_validation
~~~

## PD3_unlock_depth_boundary

~~~yaml
PD3_unlock_depth_boundary:
  H5_owner: C_SESSION
  package_rule: >
    apex-session may record dependency context and unresolved dependency review
    flags, but it must not compute reverse unlock depth, dependency graph
    scores, final next-task ranking, or exact focus candidate reports.

  allowed:
    - preserve_depends_on_values
    - record_unresolved_dependency
    - record_dependency_context_from_operator
    - include_dependency_context_in_planning_feed

  forbidden:
    - compute_unlock_depth
    - rank_tasks_by_unlock_depth
    - scan_entire_dependency_graph
    - compute_final_focus_score
    - claim_apex_sync_outputs
~~~

## script_and_write_exclusions

~~~yaml
script_and_write_exclusions:
  no_scripts_in_this_package: true
  no_script_execution: true
  no_public_web_research: true
  no_calendar_operations: true
  no_silent_repo_writes: true

  mutation_policy: >
    The package creates final mutation records and handoff artifacts. It does
    not silently mutate repo files. Actual repo writes, if any, belong to a
    later explicit file-application flow.

  allowed_this_package:
    - produce_copy_paste_ready_file_contents
    - produce_status_mutation_record
    - produce_before_after_preview
    - produce_operator_validation_record
    - produce_state_delta_summary
    - produce_entity_update_record
    - produce_H6_handoff_artifacts

  forbidden_this_package:
    - create_scripts
    - run_scripts
    - update_repo_files_without_explicit_application_flow
    - create_branch
    - create_pull_request
    - mutate_registry
~~~

## final_acceptance_invariants

~~~yaml
final_acceptance_invariants:
  package_is_C_SESSION_only: true
  H1_status_enum_preserved:
    - open
    - in-progress
    - blocked
    - done
    - deferred
  H6_handoff_file_set_preserved:
    - task_plan.md
    - findings.md
    - progress.md
    - next-session.md
  next_session_sections_exact:
    - Current Step
    - Open Items
    - Risks
    - Decisions Made
    - Next Actions
  source_references_preserved: true
  unresolved_context_preserved: true
  operator_validation_required_for_consequential_mutation: true
  apex_plan_scope_absent: true
  apex_sync_scope_absent: true
  scripts_absent: true
  malformed_frontmatter_absent: true
~~~