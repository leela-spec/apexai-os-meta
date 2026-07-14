---
name: apex-plan
description: >
  Use this skill when the operator asks to capture a project, create a new epic/task plan, decompose work, propose dependencies, assign priority/due-date rationale, or draft a provisional focus recommendation. Accepts operator notes, project goals, prior planning context, and existing task records. Produces operator-gated planning packets and handoff requests. Does not run scripts, compute exact next tasks, traverse dependency graphs, rebuild registries, scan blockers, or mutate state.
---

# Apex Plan

## APEX OS Backbone Role

`apex-plan` is the proposal and decomposition capability in the shared Plan-Sync-Session Backbone. Multi-Agent Orchestration may invoke it through the Meta Ops integration contract. Weekly Orchestrator does not treat it as an implicit weekly stage. Invoking this skill does not activate either orchestration system.

## Skill Contract

```yaml
skill_contract:
  primary_output: apex_plan_packet
  output_role: no_script_operator_gated_project_planning
  package_path: ".claude/skills/apex-plan/"

  durable_paths:
    base: "apex-meta/"
    harmonization: "apex-meta/harmonization/"
    epics: "apex-meta/epics/"
    registry: "apex-meta/registry/index.md"
    handoff: "apex-meta/handoff/"

  process_scope:
    owns:
      - PM1_capture_project
      - PM2_decompose_project
      - PM3_assign_dependency_proposals
      - PD1_priority_policy
      - PD2_urgency_policy
      - PD4_focus_recommendation_rationale
    hands_off_to_apex_sync:
      - exact_next_task_computation
      - dependency_graph_traversal
      - blocker_scan
      - registry_rebuild
      - drift_detection
      - exact_priority_urgency_unlock_sorting
    hands_off_to_apex_session:
      - status_mutation
      - entity_update
      - session_progress_log
      - next_session_context
      - operator_confirmed_write

  status_enum:
    type: string
    allowed:
      - open
      - in-progress
      - blocked
      - done
      - deferred

  dependency_field:
    name: depends_on
    type: integer_array
    rule: "All task IDs listed in depends_on must have status done before the task is actionable."

  priority_policy:
    values:
      high: 3
      medium: 2
      low: 1
    apex_plan_role: "Assign a qualitative priority value and rationale."
    apex_sync_role: "Use policy weights only when computing exact ranking."

  urgency_policy:
    field: due_date
    apex_plan_role: "Record due_date and explain urgency qualitatively."
    apex_sync_role: "Compute exact urgency score from due_date."

  script_policy:
    scripts_allowed: false
    bash_allowed: false
    python_allowed: false

  boundaries:
    must_not_create:
      - exact_next_task_computation
      - dependency_graph_traversal
      - blocker_scan
      - registry_rebuild
      - drift_detection
      - exact_priority_urgency_unlock_sorting
      - status_mutation
      - entity_update
      - session_progress_log
      - next_session_context
      - operator_confirmed_write
```

## Supporting Files

```yaml
supporting_files:
  - path: references/plan-cluster-contract.md
    read_when:
      - validating_package_scope
      - clarifying_apex_plan_boundaries
      - preparing_handoff_requests

  - path: references/task-record-contract.md
    read_when:
      - creating_task_records
      - validating_task_fields
      - checking_status_priority_dependency_values

  - path: references/decomposition-and-dependency-rules.md
    read_when:
      - decomposing_work
      - proposing_depends_on
      - flagging_circular_dependency_risk

  - path: references/priority-urgency-focus-policy.md
    read_when:
      - assigning_priority_policy
      - explaining_due_date_urgency
      - drafting_provisional_focus_rationale

  - path: templates/epic-template.md
    read_when:
      - operator_requests_epic_template
      - drafting_new_epic_record
      - preparing_epic_handoff_request

  - path: templates/task-template.md
    read_when:
      - operator_requests_task_template
      - drafting_task_records
      - preparing_task_handoff_request

  - path: package-manifest.md
    read_when:
      - operator_inspects_package_structure
      - validating_file_inventory
```

## Procedure

1. **Load planning context.** Read the operator request, supplied notes, project goal, prior planning context, and any existing task records; if no usable project context exists, apply the `no_project_context` failure mode.

2. **Capture the project.** Convert source material into a project capture record with goal, scope, constraints, source, and review flags, without creating or mutating durable files.

3. **Define the epic container.** Draft an epic record for `apex-meta/epics/<slug>/` when the request introduces a new project-level work container, and mark unresolved scope decisions for operator review.

4. **Decompose work.** Produce proposed task records using the canonical task fields from `references/task-record-contract.md`, preserving the status enum, priority policy, due_date field, depends_on field, blocked_by field, acceptance criteria, definition of done, notes, and source.

5. **Propose dependencies.** Assign only dependency proposals in `depends_on`, flag obvious circular dependency risk, and mark uncertain or incomplete dependency evidence for apex-sync validation.

6. **Explain priority, urgency, and focus.** Assign high, medium, or low priority with rationale, record due_date when known, explain urgency qualitatively, and draft only a provisional focus recommendation.

7. **Gate and hand off.** Present the planning packet, review flags, and handoff requests to the operator; do not mutate state, and route exact ranking or validation to apex-sync and any confirmed write or status mutation to apex-session.

## Failure Modes

```yaml
failure_modes:
  no_project_context:
    trigger: "The operator request lacks a project goal, project notes, or prior planning context."
    correction: "Ask for source context or return only a blank epic and task template proposal."

  missing_task_id:
    trigger: "A dependency proposal refers to a task that has no integer id."
    correction: "Keep the dependency out of depends_on and add a dependency_uncertainty review flag."

  invalid_status_value:
    trigger: "A proposed task status is not open, in-progress, blocked, done, or deferred."
    correction: "Replace the status with open and add an invalid_status review flag."

  invalid_priority_value:
    trigger: "A proposed priority is not high, medium, or low."
    correction: "Set priority to medium and add an invalid_priority review flag."

  uncertain_dependency:
    trigger: "The source context suggests a dependency but does not prove the prerequisite task relationship."
    correction: "Record the uncertainty in review_flags and request apex-sync dependency validation."

  circular_dependency_risk:
    trigger: "Two or more proposed tasks appear to depend on each other directly."
    correction: "Keep the proposed tasks but flag circular_dependency_risk and request apex-sync validation."

  deterministic_ranking_requested:
    trigger: "The operator asks for exact next-task computation, dependency graph traversal, or exact priority-urgency sorting."
    correction: "Provide qualitative rationale only and hand off exact computation to apex-sync."

  state_mutation_requested:
    trigger: "The operator asks apex-plan to update task status, write files, rebuild the registry, or mutate session state."
    correction: "Return a handoff request to apex-session and do not perform the mutation."
```

## Output Requirements

```yaml
output_requirements:
  primary_output: apex_plan_packet
  output_mode: operator_review_packet_only

  required_sections:
    - plan_packet_metadata
    - project_capture_record
    - epic_record
    - proposed_task_records
    - dependency_plan
    - priority_urgency_focus_rationale
    - review_flags
    - handoff_requests
    - operator_gate

  plan_packet_metadata:
    include_package_name: true
    include_source_summary: true
    include_planning_status: true

  proposed_task_records:
    canonical_source: "references/task-record-contract.md"
    include_only_proposed_records: true
    do_not_claim_files_written: true

  dependency_plan:
    canonical_source: "references/decomposition-and-dependency-rules.md"
    include_depends_on_proposals: true
    include_uncertainty_flags: true
    do_not_compute_graph_traversal: true

  priority_urgency_focus_rationale:
    canonical_source: "references/priority-urgency-focus-policy.md"
    qualitative_only: true
    do_not_compute_exact_ranking: true

  handoff_requests:
    to_apex_sync:
      - validate_dependencies
      - compute_next_action
      - scan_blockers
      - rebuild_registry
      - compute_focus_candidates
    to_apex_session:
      - request_status_mutation
      - request_operator_confirmed_write
      - request_session_handoff_update

  operator_gate:
    required_before_mutation_handoff: true
    accepted_states:
      - operator_review_needed
      - approved_for_handoff
      - needs_revision
```

## Completion Gate

```yaml
completion_gate:
  source_context_accounted_for: true
  task_records_follow_contract: true
  status_enum_preserved: true
  depends_on_integer_array_preserved: true
  priority_due_date_policy_preserved: true
  dependency_uncertainty_flagged: true
  deterministic_ranking_not_computed: true
  apex_sync_handoff_present_when_needed: true
  apex_session_handoff_present_when_needed: true
  operator_gate_present: true
```