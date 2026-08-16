---
okf: open-knowledge-format
okf_version: 1
title: "Apex Plan Packet — Close Leela Decisions and Questions"
document_role: apex_plan_operator_review_packet
created: 2026-08-16
status: operator_review_needed
planning_status: evidence_checked_candidate
package: apex-plan
project: Leela
candidate_epic_slug: leela-product-decisions
target_week: 2026-W34
canonical_mutation_performed: false
source_checkpoints:
  - apex-meta/handoff/plan-packets/leela-product-decisions-checkpoint-01-ledger-triage-20260816.md
  - apex-meta/handoff/plan-packets/leela-product-decisions-checkpoint-02-resolution-profiles-20260816.md
  - apex-meta/handoff/plan-packets/leela-product-decisions-checkpoint-03-home-override-persistence-20260816.md
  - apex-meta/handoff/plan-packets/leela-product-decisions-checkpoint-04-spatial-accessibility-fallback-20260816.md
  - apex-meta/handoff/plan-packets/leela-product-decisions-checkpoint-05-harmonization-ownership-20260816.md
---

# Apex Plan Packet — Close Leela Decisions and Questions

## plan_packet_metadata

```yaml
plan_packet_metadata:
  package: apex-plan
  planning_status: evidence_checked_candidate
  project: Leela
  candidate_epic_slug: leela-product-decisions
  target_week: 2026-W34
  operator_goal: close decisions and questions broadly across the complete Leela app and project
  source_of_truth:
    - leela-spec/Leela-Cloud-2026/docs/ssot/decisions/OPEN_QUESTIONS.md
    - leela-spec/Leela-Cloud-2026/docs/ssot/decisions/registry.csv
    - leela-spec/Leela-Cloud-2026/docs/ssot/decisions/index.md
    - current feature specs/code/materialization per decision cluster
    - durable Apex checkpoints listed above
  canonical_mutation_performed: false
```

## project_capture_record

```yaml
project_capture_record:
  goal: >
    Reduce the unresolved Leela decision surface without asking the operator to
    re-answer questions that are already resolved, stale, obsolete, or answerable
    by repository evidence. Reconcile the decision ledger first, then present
    genuinely operator-owned choices in small evidence-backed batches ordered by
    current blocking impact.

  success_state:
    - stale open rows are separated from genuinely unresolved rows
    - already-answered rows point to their authoritative decision artifacts
    - immediate Core Interaction blocker questions are decision-ready
    - broader decision clusters are grouped by product domain and dependency
    - operator decision load is minimized through evidence/code sweeps before asking
    - every accepted answer lands in a decision record and ledger pointer
    - no QA row is silently resolved by AI inference

  constraints:
    - OPEN_QUESTIONS rule: agent cannot resolve an open QA row by inference
    - every closed QA must point to the artifact carrying the answer
    - current decision records/spec/code outrank stale question wording
    - do not merge distinct QA questions merely because they touch the same model
    - operator-facing decision language should avoid unnecessary framework jargon

  review_flags:
    - operator_review_needed
```

## epic_record

```yaml
epic_record:
  slug: leela-product-decisions
  title: Close Leela Decisions and Questions
  status: open
  priority: high
  due_date: null
  goal: >
    Reconcile and systematically close Leela's unresolved decision queue using
    current evidence and bounded operator decision batches.
  source:
    - operator portfolio intake 2026-08-16
    - current Leela decision ledger and registry
    - Apex decision-triage checkpoints
```

## proposed_task_records

### Task 1 — Reconcile stale decision-ledger state

```yaml
id: 1
title: Reconcile stale decision-ledger state against authoritative decision records
status: open
priority: high
due_date: null
depends_on: []
blocked_by: []
acceptance_criteria:
  - registry/open-question rows are compared against current SSOT-D decision records
  - rows already resolved by newer authoritative artifacts are identified
  - each stale row has the exact answer pointer recorded in the reconciliation output
  - no genuinely open row is closed by inference
  - QA-130 is included as the first confirmed stale-ledger example
definition_of_done:
  - one reconciliation report lists already_answered_ledger_stale versus truly open rows
  - proposed ledger repairs are explicit and source-backed
source:
  - docs/ssot/decisions/OPEN_QUESTIONS.md
  - docs/ssot/decisions/registry.csv
  - docs/ssot/decisions/index.md
```

### Task 2 — Close the Home/Resolution profile decision batch

```yaml
id: 2
title: Prepare and close QA-02 and QA-11 resolution-profile decisions
status: open
priority: high
due_date: null
depends_on: []
blocked_by:
  - operator_answer_required
acceptance_criteria:
  - QA-02 is presented as entry-flow mapping rather than a vague profile-design question
  - demand-sensitive, entry-source-fixed, and Path-required versions are shown with consequences
  - QA-11 ad-hoc factor options are shown without inventing a Path priority
  - repository-backed recommendation is clearly non-authoritative until operator answer
  - accepted answer is recorded in a Leela decision artifact and linked from both QA rows
definition_of_done:
  - QA-02 and QA-11 have authoritative answer pointers
  - Algorithm profile contract and materialization reflect the accepted choice
notes:
  - current recommended candidates are demand-sensitive profile selection and neutral ad-hoc factor 1.00
source:
  - leela-product-decisions-checkpoint-02-resolution-profiles-20260816.md
```

### Task 3 — Close Home override persistence decision

```yaml
id: 3
title: Prepare and close QA-100 Home override persistence
status: open
priority: high
due_date: null
depends_on: []
blocked_by:
  - operator_answer_required
acceptance_criteria:
  - operator sees request-only, current-Home-session, sticky-until-clear, and durable-default consequences
  - current app-global GS_Spark lifetime is not treated as product authority
  - QA-100 remains distinct from QA-131
  - accepted lifecycle is added to Home screen contract/tests and decision ledger
definition_of_done:
  - QA-100 has an authoritative decision pointer
  - Home scope/duration lifecycle is explicit
notes:
  - evidence-backed recommended candidate is current Home interaction session, not durable preference
source:
  - leela-product-decisions-checkpoint-03-home-override-persistence-20260816.md
```

### Task 4 — Narrow and close spatial accessibility fallback policy

```yaml
id: 4
title: Close QA-138 spatial accessibility fallback policy after bounded-cluster verification
status: open
priority: medium
due_date: null
depends_on: []
blocked_by:
  - operator_answer_required_for_global_policy
acceptance_criteria:
  - QA-138 is framed around spatial surfaces that cannot satisfy accessibility directly
  - bounded cluster accessibility is evaluated on its own deterministic focus/semantics behavior
  - legacy WGT_ST_TreeView implementation is not conflated with the abstract requirement for an accessible projection
  - accepted policy states when an alternate projection is mandatory
definition_of_done:
  - QA-138 has an authoritative decision pointer
  - legacy Skill Tree fallback disposition can be finalized without weakening accessibility
notes:
  - QA-138 does not block bounded-cluster primary routing
source:
  - leela-product-decisions-checkpoint-04-spatial-accessibility-fallback-20260816.md
```

### Task 5 — Ratify Harmonization as feature or migration shell

```yaml
id: 5
title: Close QA-73 Harmonization ownership and namespace disposition
status: open
priority: medium
due_date: null
depends_on: []
blocked_by:
  - operator_answer_required
acceptance_criteria:
  - current fixed 11-feature catalog is included in the evidence
  - current harmonization runtime dependencies are acknowledged rather than called dead
  - current migration map's owner-by-owner convergence is included
  - operator chooses between migration shell, new feature, or immediate archive with consequences
  - accepted answer defines whether new domain authority may ever be added under harmonization
  - migration/retirement policy is recorded
definition_of_done:
  - QA-73 has authoritative answer pointer
  - harmonization namespace has explicit architectural status
notes:
  - evidence strongly supports migration shell, not feature; this is still operator-owned
source:
  - leela-product-decisions-checkpoint-05-harmonization-ownership-20260816.md
```

### Task 6 — Process Sequencing and Builder decision cluster

```yaml
id: 6
title: Evidence-sweep and close Sequencing and Builder decision cluster
status: open
priority: high
due_date: null
depends_on: [1]
blocked_by: []
acceptance_criteria:
  - QA-07 QA-10 QA-13 QA-16 QA-17 QA-20a QA-21a QA-76 are re-read against current code/specs/decision sheets
  - already-implemented answers are distinguished from real operator choices
  - operator receives small coherent batches rather than raw ledger rows
  - accepted answers land in decision artifacts and downstream specs/materialization
definition_of_done:
  - each named QA is closed, narrowed with explicit blocker, or intentionally deferred with current source pointer
source:
  - current Sequencing SSOT
  - DECISION-SHEET-01 and related records
```

### Task 7 — Process Path, Stats, and policy decision cluster

```yaml
id: 7
title: Evidence-sweep and close Path Stats and policy decision cluster
status: open
priority: medium
due_date: null
depends_on: [1]
blocked_by: []
acceptance_criteria:
  - QA-08 QA-14 QA-42 QA-101 QA-102 QA-132 QA-143 are checked against current implementation and newer decisions
  - Packet-09 changes are included where they narrow QA-143
  - decision packets separate data-contract choices from presentation-only choices
  - no Path/Stats ownership is silently reassigned
  - accepted answers land in decision artifacts
source:
  - current Path/Stats/Algorithm/Sequencing specs and materialization
```

### Task 8 — Repair source-integrity and stale-plan decision debt

```yaml
id: 8
title: Reconcile source-integrity and stale-plan decision debt
status: open
priority: medium
due_date: null
depends_on: [1]
blocked_by: []
acceptance_criteria:
  - QA-30 QA-40 QA-85 QA-86 QA-141 QA-142 QA-151 QA-160 are treated as evidence/provenance work before operator choice
  - mandatory unread sources are identified
  - stale or impossible denominator/hash claims are separated from product decisions
  - executed-but-unretired plans are marked so future agents cannot execute stale instructions
  - only residual genuine operator choices are presented to operator
definition_of_done:
  - source-integrity debt no longer creates false open decisions or unsafe stale instructions
source:
  - decision ledger
  - source-ingestion worklists/audits
  - current master implementation
```

### Task 9 — Create operator-facing decision batches and closure cadence

```yaml
id: 9
title: Create operator-facing decision batches and closure cadence
status: open
priority: medium
due_date: null
depends_on: [1]
blocked_by: []
acceptance_criteria:
  - technical QA language is translated into user-facing product choices without changing semantics
  - each batch contains few coherent decisions
  - each decision has concrete versions, consequences, worked example when useful, and recommendation when evidence supports one
  - accepted answer is immediately routed to a decision record and ledger repair
  - unresolved decisions are never carried forward only in chat memory
definition_of_done:
  - a repeatable operator decision workflow exists and is used for the remaining queue
notes:
  - directly addresses QA-70's validation problem without itself resolving QA-70
```

## dependency_plan

```yaml
dependency_plan:
  - task_id: 6
    depends_on: [1]
    rationale: do not ask sequencing questions before stale-ledger reconciliation
  - task_id: 7
    depends_on: [1]
    rationale: same anti-duplication requirement
  - task_id: 8
    depends_on: [1]
    rationale: source integrity triage needs reconciled current queue
  - task_id: 9
    depends_on: [1]
    rationale: operator batches should be based on reconciled decision truth
  apex_sync_handoff_requests:
    - validate_dependencies
    - compute_next_action
    - compute_focus_candidates
```

## priority_urgency_focus_rationale

```yaml
priority_urgency_focus_rationale:
  epic_priority: high
  due_date: null
  provisional_focus_recommendation:
    first: Reconcile stale decision-ledger state against authoritative decision records
    parallel:
      - QA-02/QA-11 evidence packet already ready
      - QA-100 evidence packet already ready
    rationale: >
      Reconciliation prevents wasting operator attention and prevents stale ledger rows
      from blocking implementation that newer decisions already authorized.
```

## review_flags

```yaml
review_flags:
  - operator_review_needed
  - operator_answers_required_for_actual_QA_closure
  - QA-130_confirmed_ledger_drift_example
  - do_not_bulk_close_open_rows
  - do_not_merge_QA100_and_QA131
```

## handoff_requests

```yaml
handoff_requests:
  to_apex_session_after_operator_approval:
    - create canonical epic/task records for this project
  to_leela_decision_process_during_execution:
    - write accepted operator answers as SSOT decision records
    - update OPEN_QUESTIONS and registry pointers
    - verify downstream specs/materialization
```

## operator_gate

```yaml
operator_gate:
  status: operator_review_needed
  recommended_decision: approved_for_handoff
  mutation_allowed_by_this_packet: false
```
