# Plan Cluster Contract

```yaml
plan_cluster_contract:
  file_role: apex_plan_scope_and_mapping_contract
  package_name: apex-plan
  package_path: ".claude/skills/apex-plan/"
  purpose: >
    Define the canonical no-script planning boundary for Apex Plan. Apex Plan
    captures project intent, drafts epic and task records, proposes dependencies,
    explains priority and urgency policy, and emits operator-gated handoff
    requests without computing deterministic rankings or mutating durable state.

  durable_paths:
    base: "apex-meta/"
    harmonization: "apex-meta/harmonization/"
    epics: "apex-meta/epics/"
    registry: "apex-meta/registry/index.md"
    handoff: "apex-meta/handoff/"

  status_enum:
    type: string
    allowed:
      - open
      - in-progress
      - blocked
      - done
      - deferred

  script_policy:
    scripts_allowed: false
    bash_allowed: false
    python_allowed: false
```

## 1. Preserved Mapping

```yaml
mapping_to_preserve:
  natural_clusters:
    intake_and_task_contract:
      primary_home: apex-plan
      package_role: project_capture_and_task_record_contracts

    decomposition_and_dependency_engine:
      primary_home: apex-plan
      secondary_home: apex-sync
      package_role: decomposition_and_dependency_proposal_only

    product_scoring_and_recommendation:
      primary_home: apex-plan
      secondary_home: apex-sync
      package_role: qualitative_rationale_and_policy_only

    governance_and_validation:
      primary_home: apex-session
      package_role_in_apex_plan: review_flags_and_handoff_requests
```

## 2. Process Scope

```yaml
package_process_scope:
  owns:
    PM1_capture_project:
      role: "Capture project goal, scope, constraints, source, and review flags."
      output: project_capture_record

    PM2_decompose_project:
      role: "Break a project or epic into proposed task records."
      output: proposed_task_records

    PM3_assign_dependency_proposals:
      role: "Propose depends_on relationships and dependency review flags."
      output: dependency_plan

    PD1_priority_policy:
      role: "Assign high, medium, or low priority with rationale."
      output: priority_rationale

    PD2_urgency_policy:
      role: "Record due_date and explain urgency qualitatively."
      output: urgency_rationale

    PD4_focus_recommendation_rationale:
      role: "Draft provisional focus rationale without exact sorting."
      output: provisional_focus_recommendation

  must_handoff_to_apex_sync:
    - exact_next_task_computation
    - dependency_graph_traversal
    - blocker_scan
    - registry_rebuild
    - drift_detection
    - exact_priority_urgency_unlock_sorting

  must_handoff_to_apex_session:
    - status_mutation
    - entity_update
    - session_progress_log
    - next_session_context
    - operator_confirmed_write
```

## 3. Record Purposes

```yaml
record_purposes:
  project_capture_record:
    purpose: "Capture project goal, scope, constraints, source, and review flags."
    required_when:
      - new_project_or_goal_is_introduced
      - existing_project_scope_is_reframed
      - operator_supplies_unstructured_project_notes

  epic_record:
    purpose: "Define a project-level work container under apex-meta/epics/<slug>/."
    required_when:
      - new_epic_container_is_needed
      - task_records_need_a_durable_parent
      - operator_requests_new_epic_planning
```

## 4. Handoff Request Contract

```yaml
handoff_requests:
  to_apex_sync:
    validate_dependencies:
      use_when: "depends_on proposals need graph validation or circular dependency checks beyond obvious direct risk."
    compute_next_action:
      use_when: "the operator asks what exact task should be actioned next."
    scan_blockers:
      use_when: "the operator asks for current blockers across task records."
    rebuild_registry:
      use_when: "registry/index.md needs deterministic refresh."
    compute_focus_candidates:
      use_when: "the operator asks for ranked focus candidates or exact sorting."

  to_apex_session:
    request_status_mutation:
      use_when: "the operator asks to change status on durable task records."
    request_operator_confirmed_write:
      use_when: "the operator approves proposed epic or task content for durable write."
    request_session_handoff_update:
      use_when: "planning output must become next-session context or progress log material."
```

## 5. Non-Goals

```yaml
non_goals:
  - "Do not compute deterministic next-task ranking."
  - "Do not traverse the full dependency graph."
  - "Do not scan blockers across the registry."
  - "Do not rebuild apex-meta/registry/index.md."
  - "Do not detect drift or stale state."
  - "Do not mutate task status or session state."
  - "Do not write durable files from apex-plan."
  - "Do not generate or call scripts."
```