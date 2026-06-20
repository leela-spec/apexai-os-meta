
# FILE: .claude/skills/apex-sync/references/sync-cluster-contract.md

```markdown
# Sync Cluster Contract

```yaml
sync_cluster_contract:
  canonical_source: ".claude/skills/apex-sync/references/sync-cluster-contract.md"

  package_boundary:
    package_name: apex-sync
    package_path: ".claude/skills/apex-sync/"
    durable_paths:
      base: "apex-meta/"
      epics: "apex-meta/epics/"
      registry: "apex-meta/registry/index.md"
      handoff: "apex-meta/handoff/"
      scripts: "apex-meta/scripts/"
    role: deterministic_read_side_synchronization
    default_behavior: read_only
    exact_computation_owner: true

  process_scope:
    owns:
      - PM4_compute_next_action
      - PM5_detect_blockers
      - PM7_detect_stall
      - PM8_generate_work_registry
      - KB4_rebuild_index
      - KB5_detect_drift
      - PD1_compute_priority_score
      - PD2_compute_urgency_score
      - PD3_compute_unlock_depth
      - PD4_compute_focus_candidates

    must_not_own:
      - PM1_project_capture
      - PM2_human_decomposition
      - PM6_status_mutation
      - KB1_session_narrative
      - KB2_state_delta_interpretation
      - KB3_entity_synthesis
      - KB6_next_session_authoring
      - PD5_operator_validation
      - PD6_planning_feed_authoring

    required_outputs:
      - next_action_report
      - blocker_report
      - registry_report
      - stall_report
      - drift_report
      - score_report
      - focus_candidate_report
      - dependency_validation_report

  apex_plan_boundary:
    package_name: apex-plan
    owns:
      - project_capture
      - human_decomposition
      - dependency_proposal
      - priority_rationale
      - urgency_rationale
      - provisional_focus_recommendation
    hands_off_to_apex_sync:
      - exact_next_action_computation
      - exact_dependency_validation
      - exact_score_computation
      - exact_focus_candidate_ordering
    rule: >
      apex-plan may propose policy, rationale, and task records, but apex-sync
      owns deterministic read-side computation over accepted task files.

  apex_session_boundary:
    package_name: apex-session
    owns:
      - status_mutation
      - operator_confirmation_gate
      - session_progress_log
      - state_delta_interpretation
      - KB_entity_synthesis
      - next_session_context
      - planning_feed_authoring
    hands_off_to_apex_sync:
      - stale_state_detection
      - drift_detection
      - registry_rebuild
      - blocker_scan
    rule: >
      apex-session may write confirmed state changes after operator approval,
      but apex-sync must not mutate task files, handoff files, entity files, or
      skill files.

  non_goals:
    - "Do not capture projects."
    - "Do not decompose project work by reasoning."
    - "Do not mutate status."
    - "Do not author KB narrative."
    - "Do not synthesize entity pages."
    - "Do not create next-session context."
    - "Do not perform operator validation."
      
## Boundary Notes

`apex-sync` is the exact-computation layer. It is intentionally narrow: it reads task files, computes reports, and optionally writes only the generated registry when the registry command is explicitly non-dry-run.

The package may attach short machine-readable `reason` strings to report entries. It must not add narrative planning rationale, create new tasks, or decide whether a task status should change.