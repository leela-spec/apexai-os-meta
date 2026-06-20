# Session Cluster Contract

~~~yaml
session_cluster_contract:
  file_role: canonical_session_package_boundary
  package_name: apex-session
  package_path: ".claude/skills/apex-session/"

  package_boundary:
    durable_paths:
      base: "apex-meta/"
      epics: "apex-meta/epics/"
      registry: "apex-meta/registry/index.md"
      handoff: "apex-meta/handoff/"
      entities: "apex-meta/entities/"
      raw: "apex-meta/raw/"

    mutation_targets:
      - "apex-meta/epics/<slug>/<NNN>.md"
      - "apex-meta/entities/*.md"
      - "apex-meta/handoff/task_plan.md"
      - "apex-meta/handoff/findings.md"
      - "apex-meta/handoff/progress.md"
      - "apex-meta/handoff/next-session.md"

    output_policy:
      chat_output_only: true
      generated_files_are_file_blocks_not_repo_writes: true

  process_scope:
    owns:
      - PM6_update_status
      - KB1_write_session_progress
      - KB2_extract_state_deltas
      - KB3_maintain_entity_files
      - KB6_produce_next_session_context
      - PD5_validate_with_operator
      - PD6_feed_planning_layer

    coordinates_with_apex_sync:
      - PM7_stall_flags
      - KB4_index_rebuild
      - KB5_drift_flags
      - PD3_unlock_depth

    coordinates_with_apex_plan:
      - PM1_project_capture
      - PM2_decomposition
      - PM3_dependency_proposals
      - PD4_focus_rationale

  apex_plan_boundary:
    primary_home: apex-plan
    package_role:
      - project_capture
      - task_decomposition
      - dependency_proposals
      - focus_rationale
    apex_session_role:
      - operator_confirmed_status_update
      - state_delta_capture

  apex_sync_boundary:
    primary_home: apex-sync
    package_role:
      - deterministic_next_action_detection
      - blocker_scan
      - registry_rebuild
      - drift_detection
      - priority_urgency_unlock_focus_scores
    apex_session_role:
      - handoff_requests
      - sync_required_before_final_context_review_flag

  session_artifact_inventory:
    required_outputs:
      - status_mutation_proposal
      - before_after_mutation_preview
      - session_progress_log
      - state_delta_summary
      - entity_update_proposal
      - next_session_context
      - planning_layer_feed
      - operator_validation_result

    handoff_files:
      task_plan:
        path: "apex-meta/handoff/task_plan.md"
        role: current_session_plan_and_phase_tracking
      findings:
        path: "apex-meta/handoff/findings.md"
        role: durable_discoveries_and_decisions
      progress:
        path: "apex-meta/handoff/progress.md"
        role: append_only_session_activity_log
      next_session:
        path: "apex-meta/handoff/next-session.md"
        role: context_bootstrap_for_next_session
~~~

## 1. Natural Cluster Mapping

~~~yaml
natural_clusters:
  session_memory_and_handoff:
    primary_home: apex-session
    secondary_home: apex-sync
    package_role:
      - task_plan
      - findings
      - progress
      - next_session_context
      - session_recovery_surface

  knowledge_entity_maintenance:
    primary_home: apex-session
    secondary_home: apex-sync
    package_role:
      - raw_source_preservation
      - entity_file_update_proposal
      - concept_or_project_record_update
      - index_rebuild_request

  governance_and_validation:
    primary_home: apex-session
    package_role:
      - explicit_operator_gate
      - before_after_mutation_preview
      - review_flags
      - mutation_audit_note

  intake_and_task_contract:
    primary_home: apex-plan
    secondary_home: apex-session
    package_role:
      - operator_confirmed_status_update
      - state_delta_capture
~~~

## 2. Task Field Compatibility

~~~yaml
task_field_compatibility:
  status:
    type: string
    allowed:
      - open
      - in-progress
      - blocked
      - done
      - deferred

  depends_on:
    type: integer_array
    rule: "All depended task IDs must have status done before the task is actionable."

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
~~~

## 3. Non-Goals

~~~yaml
non_goals:
  - "Do not compute deterministic next-task ranking."
  - "Do not traverse dependency graphs."
  - "Do not scan blockers."
  - "Do not rebuild registry or index files."
  - "Do not detect drift by exact comparison."
  - "Do not compute priority, urgency, unlock, or focus scores."
  - "Do not decompose new work by planning rationale."
  - "Do not write without explicit operator confirmation."
~~~