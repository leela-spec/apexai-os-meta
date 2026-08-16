---
okf: open-knowledge-format
okf_version: 1
title: "Apex Plan Packet — Leela Project Management Cleanup"
document_role: apex_plan_operator_review_packet
created: 2026-08-16
status: operator_review_needed
planning_status: evidence_checked_candidate
package: apex-plan
project: Leela
candidate_epic_slug: leela-project-management-cleanup
target_week: 2026-W34
canonical_mutation_performed: false
source_checkpoints:
  - apex-meta/handoff/plan-packets/leela-project-management-cleanup-checkpoint-01-authority-drift-20260816.md
---

# Apex Plan Packet — Leela Project Management Cleanup

## project_capture_record

```yaml
project_capture_record:
  goal: >
    Declutter Leela project management by separating current authority from
    historical control artifacts, consolidating active cross-project work into
    the Apex Plan/Session/Sync backbone, and ensuring future agents can restart
    from one correct pointer per truth layer instead of conflicting old handovers.

  success_state:
    - current product semantic authority points unambiguously to Leela SSOT
    - current runtime execution authority points to Macro/Meso/one active Micro packet
    - cross-project project/task state lives in Apex canonical project records after Session approval
    - historical Spatial Opus control/handover files are explicitly historical/superseded where appropriate
    - stale constraints cannot be mistaken for current execution instructions
    - useful history remains preserved and searchable
    - restart instructions tell agents which repository/file to read for each type of work

  scope:
    in_scope:
      - inventory project-control artifacts across Leela repos
      - classify active/current/historical/superseded/duplicate control documents
      - reconcile old Leela-specific Apex handovers with current authority
      - create/update explicit authority pointers and restart instructions
      - migrate active project-management state into central Apex epics/tasks after approval
      - retire stale executable guidance without deleting historical evidence
      - verify no duplicate project-control layer silently re-owns product truth
    out_of_scope:
      - deleting research/product source merely for age
      - semantic SSOT redesign
      - rewriting current runtime Macro/Meso/Micro protocol
      - mass file cleanup without source-by-source classification
      - merging historical branches

  source:
    - operator request: declutter project management
    - Leela_APEX_Orchestration_Control.okf.md
    - SpatialOpus_NextChat_Handover.okf.md
    - current Leela-Cloud-2026 AGENTS.md
    - current weekly-cycle Apex project-management handover
    - authority-drift checkpoint
```

## epic_record

```yaml
epic_record:
  slug: leela-project-management-cleanup
  title: Leela Project Management Cleanup
  status: open
  priority: medium
  due_date: null
  goal: >
    Reduce project-control ambiguity while preserving history and moving active
    cross-portfolio state into the current Apex backbone.
```

## proposed_task_records

### Task 1 — Inventory and classify Leela project-control artifacts

```yaml
id: 1
title: Inventory and classify Leela project-control artifacts
status: open
priority: high
due_date: null
depends_on: []
blocked_by: []
acceptance_criteria:
  - project-control artifacts are inventoried across leela-spec/leela and Leela-Cloud-2026
  - each artifact is classified active current historical superseded duplicate or source-evidence-only
  - classification records exact authority relation and superseding pointer where known
  - no product/research artifact is marked deletable merely because it is old
  - known stale constraints in SpatialOpus handovers are captured
definition_of_done:
  - one machine-readable project-control inventory exists
  - every active-looking control artifact has explicit currentness status
source:
  - apex-meta/handoff/ in leela control repo
  - docs/orchestration/ and AGENTS.md in application repo
```

### Task 2 — Define and publish one current Leela authority map

```yaml
id: 2
title: Define and publish one current Leela project-control authority map
status: open
priority: high
due_date: null
depends_on: [1]
blocked_by: []
acceptance_criteria:
  - product semantics map to docs/ssot
  - runtime increment execution maps to Macro/Meso/active Micro protocol
  - cross-project project management maps to apexai-os-meta canonical epics/tasks
  - pre-canonical planning packets map to Apex handoff/plan-packets
  - historical control artifacts are explicitly non-authoritative by default
  - restart instructions state the minimal files to read for each work type
definition_of_done:
  - a future agent can determine correct authority without reading old handovers first
```

### Task 3 — Retire or annotate stale Spatial Opus control instructions

```yaml
id: 3
title: Retire or annotate stale Spatial Opus control instructions
status: open
priority: high
due_date: null
depends_on: [1, 2]
blocked_by: []
acceptance_criteria:
  - stale Nowa constraints are not presented as current rules
  - stale OD-1 through OD-6 status is not presented as current decision truth
  - old files either carry clear superseded/historical metadata or move to an explicit archive location
  - historical rationale remains preserved
  - any still-valid workflow rule points to its current authority instead of restating it
definition_of_done:
  - old Spatial Opus handovers cannot be mistaken for current restart authority
notes:
  - no deletion is required if clear archival status achieves the goal
```

### Task 4 — Consolidate active Leela projects into central Apex project records

```yaml
id: 4
title: Consolidate active Leela projects into central Apex project records
status: open
priority: high
due_date: null
depends_on: [2]
blocked_by:
  - operator_approval_of_project_packets
acceptance_criteria:
  - approved Leela epics are written under apex-meta/epics in apexai-os-meta through Apex Session
  - canonical task records contain source pointers to the relevant Leela repositories
  - Leela repo handovers do not become a second task database
  - future weekly ProjectStatus can read confirmed Leela state from the central Apex backbone
definition_of_done:
  - Leela has one confirmed cross-project task/state representation feeding the weekly cycle
source:
  - current Leela Apex Plan packets
```

### Task 5 — Reconcile runtime orchestration with cross-project project management

```yaml
id: 5
title: Reconcile runtime Micro packets with Apex project task identity
status: open
priority: medium
due_date: null
depends_on: [2, 4]
blocked_by: []
acceptance_criteria:
  - Apex task represents project outcome/state
  - application Micro packet represents one runtime executable increment
  - mapping between an active Micro packet and its parent Apex task is explicit when applicable
  - neither layer duplicates semantic product truth
  - Micro completion can feed confirmed Session progress without turning STATE.md into a second project registry
definition_of_done:
  - project management and runtime execution routing have a documented one-way relationship
```

### Task 6 — Verify decluttered restart path

```yaml
id: 6
title: Verify decluttered Leela restart path
status: open
priority: medium
due_date: null
depends_on: [2, 3, 4, 5]
blocked_by: []
acceptance_criteria:
  - a fresh agent starting from current authority pointers does not need chat memory
  - it does not load superseded Spatial Opus instructions as current
  - it can locate current product truth current project state and current execution packet separately
  - no unresolved duplicate active-control pointer remains
  - historical artifacts remain discoverable
  - relevant repository validation gates pass after documentation changes
definition_of_done:
  - restart walkthrough succeeds using repository state only
```

## dependency_plan

```yaml
dependency_plan:
  - task_id: 2
    depends_on: [1]
    rationale: authority map requires complete control-artifact inventory
  - task_id: 3
    depends_on: [1, 2]
    rationale: stale handovers must be retired against a known replacement authority
  - task_id: 4
    depends_on: [2]
    rationale: centralization should occur only after authority boundaries are explicit
  - task_id: 5
    depends_on: [2, 4]
    rationale: runtime-to-project mapping requires canonical project records
  - task_id: 6
    depends_on: [2, 3, 4, 5]
    rationale: restart verification is end-to-end validation
  apex_sync_handoff_requests:
    - validate_dependencies
    - compute_next_action
    - compute_focus_candidates
```

## priority_urgency_focus_rationale

```yaml
priority_urgency_focus_rationale:
  epic_priority: medium
  due_date: null
  provisional_focus_recommendation:
    first: Inventory and classify Leela project-control artifacts
    rationale: >
      Cleanup without inventory risks deleting valuable history or preserving
      stale control as active. The repository already shows concrete authority drift.
```

## review_flags

```yaml
review_flags:
  - operator_review_needed
  - cleanup_must_preserve_history
  - current_cross_project_authority_is_apexai_os_meta
  - application_runtime_protocol_remains_separate
```

## handoff_requests

```yaml
handoff_requests:
  to_apex_session_after_operator_approval:
    - create canonical epic/task records
  later_repo_execution:
    - classify/annotate/archive stale Leela control files
    - run relevant orchestration/documentation checks
```

## operator_gate

```yaml
operator_gate:
  status: operator_review_needed
  recommended_decision: approved_for_handoff
  mutation_allowed_by_this_packet: false
```
