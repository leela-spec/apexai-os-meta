---
okf_version: "0.2"
type: operator-decision-delta
durable_id: M01-OPERATOR-DECISIONS-20261106-2
title: "Module 01 operator answers — sequences, sprint ownership, weekend, recap authority, presentation"
date: 2026-11-06
status: operator_confirmed_with_open_design_items
branch: main
baseline_before_record: 7cf9d923d1e0b887d58fd1ea7e2f058efb81c865
scope: [matrix_1, matrix_2, precap_next_day, flow_recap, status_merge, skill_backlog]
supersedes_questions_in:
  - ORCHESTRATOR-MODULE-01-QA-BOARD-20261106.okf.md
applies_to_handover_drafts:
  - ORCHESTRATOR-MATRIX-1-DESIGN-HANDOVER-20261106.okf.md
  - ORCHESTRATOR-MATRIX-2-DESIGN-HANDOVER-20261106.okf.md
production_contract_mutation: none
---

# Operator decision delta — interpret this before the earlier proposal board

## Interpretation and authority

This record captures the operator's explicit answers given after the Q01-Q14 proposal board. **Explicit corrections override the earlier recommended defaults**; unchanged recommendations are operator-verified as described below. Design handovers and the old Q&A board are preserved as historical proposals, not silently altered. These decisions do not by themselves grant access or permission to mutate OpenProject, calendar or production skill files. Existing production contracts still require narrow patch-only reconciliation.

### Decision ledger

| Q | Operator outcome | Status and exact interpretation |
|---|---|---|
| Q01 | B — state authority by fact type | ACCEPTED: OP for enrolled PM commitments/status; Git/accepted decisions/tests for implementation and proof |
| Q02 | B — unresolved identity, degrade planning | ACCEPTED: fail-closed on numeric WP IDs, retain honest fallback provenance |
| Q03 | B — dynamic project coverage | ACCEPTED: no fixed project roster gate; verify Priority Website identity |
| Q04 | A — selective Matrix 1 depth | ACCEPTED: project/epic/tasks/dependencies; expand subtasks when valuable |
| Q05 | A — evidence-backed critical path | ACCEPTED: distinguish dependency and shortlist status from numeric ranking |
| Q06 | **Old recommendation A rejected as semantically wrong** | CORRECTED: **sequence = execution time block/container**, NOT a project. It may change time and composition across days; multiple projects may share one sequence. A sprint may also contain work from several projects, but exact mixing policy remains OPEN. No per-project fixed sequence allocation |
| Q07 | A — time-based capacity computation | ACCEPTED: count actual feasible intervals; distinguish planned/available |
| Q08 | A, clarified | ACCEPTED: PrecapWeek gives weekly directional allocation, **PrecapNextDay** owns precise sprint and microtask planning (including cross-project details as chosen) |
| Q09 | **B, corrected scope** | ACCEPTED: Saturday is a **normal workday**, equal in principle to Monday–Friday; Sunday is **OFF by default**, unless operator explicitly elects a special Sunday activity. The Sunday weekly precap timing is not to be assumed automatic from stale contracts |
| Q10 | A — calendar proposal / gated daily write | ACCEPTED: preserve external meeting safety and explicit write approvals |
| Q11 | A — one Brief + compact YAML | ACCEPTED: no duplicated machine handoff; the embedded presentation_handoff remains |
| Q12 | A only with corrected ownership/routing | ACCEPTED INTENT, NEEDS ROUTE RECONCILIATION: existing FlowRecap/day recap -> StatusMerge -> actual PM update -> current next-day feed must be reused. OpenProject replaces old internal project management for migrated/enrolled work. **Do not bypass or recreate the recap machinery**; repair legacy Apex Session write path only after confirming the actual owning WP and write policy |
| Q13 | **No option approved** | OPEN: first produce and compare several concrete presentation/design variations, then choose exactly one canonical solution. Do not prematurely promote Markdown-first, HTML-first or dual-format proposal |
| Q14 | A — real-week/next-day evaluation | ACCEPTED: independently verify operator usefulness, source truth, calendar feasibility and approved writes |

Other options in the previous proposal board remain rejected *only for questions marked ACCEPTED*. L0-L3 / I-E-R here are evaluation aids for high-impact design questions; they must **not** become mandatory 1–100 task score gates.

## Q06 — accepted definition versus remaining assumptions

### ACCEPTED by operator

1. A **sequence is a block**: a bounded execution/planning container within a day, not a project identity, task hierarchy or permanent project lane.
2. Its position and duration in a calendar may vary across days.
3. Its project allocation may vary across days.
4. **One sequence may combine tasks from several projects**; no single-project restriction.
5. **Even one sprint may involve multiple projects**. This is a capability to support/evaluate, not a mandate to always mix.
6. Matrix 1 remains non-temporal; Matrix 2 lays selected work into sequences/sprints and calendar capacity.
7. The four named projects (MoA, Investment, Apex OS, Leela) are example/current priority streams and cannot define the identity of Seq 1-4.

### Working vocabulary (proposed design definition; review in sequencing-skill task)

- **Project**: source/ownership and objective domain (e.g., Master of Arts); project identity persists across days.
- **Epic/task/work package**: unit of non-temporal project work; OP ID only when verified.
- **Sequence**: one schedulable **block** or container within a day, with a local stable ID, available window, capacity, and a collection of planned sprint(s)/work items. May be single-project or multi-project.
- **Sprint**: a smaller execution segment inside a sequence, with an outcome and one or more work items. Default "30 minutes" appears in v4.1 fixtures; actual duration policy is an OPEN design choice.
- **Work item**: reference to a Matrix 1 task/outcome, with source identity and prerequisite readiness. Several items may share a sequence/sprint.
- **Flow**: the existing PrecapNextDay/Flow Execution Card/FlowRecap unit. Relationship of a flow to a sequence (1:1? 1:many? naming?) is **UNRESOLVED**. Do not rename old flow contracts by assumption.
- **Calendar block / slot**: actual or proposed time interval occupied by a sequence; project and time-slot IDs are separate.
- **Mixed-project allocation**: one sequence or sprint carries work from more than one project; preserve each project's true WP/source refs, independently auditable evidence and recap status.
- **Operator decision**: actual choice of weekly focus, scope and exceptions; not inferred from the sample draft's fixed names.

### OPEN assumptions requiring sequencing-skill design/verification

A. How many sequences per day? v4.1 shows four common blocks, not necessarily a fixed minimum.
B. What are default/allowed sequence durations (2h is a sample, and W45's midday example is 1h)?
C. Sprint duration: fixed 30m, variable, or outcome-bounded?
D. Mixing within a sprint: freely allowed vs exceptional vs guarded based on context-switch overhead and dependencies.
E. Maximum simultaneous/consecutive project switches and what grouping algorithm should minimize overhead.
F. Sequence-to-flow/FlowCard mapping: is an execution flow one sequence, several sequences, or a distinct output structure?
G. Across mixed projects, how does FlowRecap attribute evidence and candidate PM deltas to *each* originating WP?
H. When do planning constraints trigger a split/defer/shortening of a sequence?
I. Does the existing Workflow&Processes skill already cover planning/review logic sufficiently, or is a thin new sequencing skill actually necessary?
J. Which default structure is operator-friendly on desktop and mobile, given multi-project cells?
K. How do Sunday-off and Saturday-normal rules propagate to weekly and daily validation?
L. Which typed inputs/outputs are minimal for direct fork dispatch without creating redundant wrappers or state stores?

### Worked non-authoritative fixture for definition

Monday (EXAMPLE, no real calendar proof):
- Sequence S-20261109-A: 09:00–11:00. First sprint: Master of Arts invoice schema. Second sprint: Investment ingestion blocker. Third sprint: shared review of evidence for both; fourth segment reserved for buffer. This is **allowed by accepted definition**, but whether 30-minute segments and mixed sprints are optimal remains unapproved.
- Tuesday: sequence "A" need not occupy 09:00–11:00 or contain the same projects. Its **occurrence ID** must distinguish days; "Sequence 1" is not a globally reserved project lane.
- Matrix 1 source WPs remain unchanged. Matrix 2 changes only allocation. PrecapNextDay refines sprint details after a fresh read.

## Q08 — clarified PrecapWeek / PrecapNextDay boundary

- **PrecapWeek**: identify desired outcomes, selected tasks, approximate day/sequence allocations, feasible capacity and dependencies; can show light sprint topics where useful, not obligatory detailed three-item microchecklists for all week cells.
- **PrecapNextDay**: revalidate live day constraints/PM evidence; choose and refine the day's sequence and sprint composition; create Flow Execution Cards, prompts and exact execution-order detail. Must support multi-project sequence/sprint without losing task source IDs.
- **FlowRecap**: result/evidence and candidate deltas only; does not mutate task authority.

## Q09 — updated weekly calendar scope

- **Monday–Saturday**: six normal potential workdays, with individual real constraints and capacity; a day need not be filled merely because it is eligible.
- **Sunday**: default OFF, no automatic regular project execution or calendar blocks. An operator can explicitly authorize a special Sunday exception; distinguish a weekly planning session from standard project work.
- The live PrecapWeek contract, blueprint and validation checklist still say Monday–Friday/Saturday excluded. **Known production contradiction; patch later**, never misstate it as resolved.
- Date-specific weekly schedule must use actual calendar evidence; Saturday normal does not imply obligatory full 8h.

## Q12 — preserve actual recap chain; transition owning PM system

### VERIFIED CURRENT REPOSITORY IMPLEMENTATION

\`weekly-orchestrator/SKILL.md\`: PrecapNextDay G2 -> execution G3 -> normalized evidence -> \`flow-recap\` G4 -> \`status-merge\` G5 -> **apex-session** mutation -> later PrecapNextDay.

\`flow-recap/SKILL.md\`: one recap per flow, evidence-based candidate_project_status_delta and next_step_proposal, explicitly **no writes**.

\`status-merge/SKILL.md\`: reconciles candidates, emits proposed_apex_session_mutation + next_PreCapNextDay_input_context, explicitly no direct mutation.

\`07-status-merge/README.md\`: Module 07 expects a reliable status-change decision path, with lower-friction routine changes *to be designed*, not an already accepted blanket autonomy rule.

**What is NOT verified:** a separate first-class "day recap" skill/stage under .claude/skills; a live completed OpenProject writeback path in the weekly loop; universal migration of every project. The operator recalls day recap/flow recap; do not invent another stage. Inspect the relevant existing domain files when implementing.

### TARGET OWNERSHIP (operator direction, implementation not yet aligned)

- Keep FlowRecap, consolidated day-level StatusMerge, gate decisions and compact next-day handoff as **the pipeline**.
- Route a confirmed mutation to **OpenProject for the WP actually enrolled and owned there**, via canonical Node client, per-action operator confirmation/preview, current lockVersion and post-write reread; do not mirror the task into the old Apex PM graph.
- Preserve Apex Session only for truly Apex-native control-plane objects and cross-project decisions, not as default PM state for migrated work.
- After confirmed updates (or explicit no-change/degraded state), PrecapNextDay must read that fresh result/evidence plus the Weekly Brief, not stale alternate task state.
- Investigate whether "day recap" describes a daily aggregation stage, end-of-day routine or an independent skill; prefer reuse without speculative parallel implementation.

### PATCH TARGETS / TO-DO, not performed

1. Inspect .claude/skills/weekly-orchestrator/SKILL.md stage_routing, G5 mutation path and all Session/Sync project-state assumptions.
2. Inspect .claude/skills/status-merge/SKILL.md and references; update proposed mutation *target routing by owner* after explicit approval.
3. Inspect .claude/skills/flow-recap/SKILL.md, its candidate delta contract, and support for multiple project refs in one mixed sequence.
4. Inspect .claude/skills/PrecapNextDay/SKILL.md and \`templates/flow-execution-card-template.md\` currently singular **Project** field; adapt as needed for mixed-project flows/sprints with per-WP evidence.
5. Inspect .claude/skills/PrecapWeek/SKILL.md, Session/Sync references and ProjectStatus default intake; distinguish Apex-native control plane from OpenProject PM and remove stale PM priority claims *only after project ownership audit*.
6. Verify OP project enrollment/current WP data and the authorized write policy in a local runtime before changing write routing.
7. Define and test post-mutation reread -> next_PreCapNextDay_input_context for both successful and unreachable OP cases.
8. Do not change old unrelated repo contracts by whole-file overwrite; use exact-context patch files and diff review.

## Q13 — presentation design explicitly OPEN

- Operator will **first compare several concrete design variations** and then choose one canonical rendering/model.
- Candidates to prototype, not recommendations: (1) readable Markdown-first + derived HTML calendar, (2) HTML-first interactive single source plus durable Markdown/YAML export, (3) structured neutral data model producing synchronized Markdown/HTML views. Include one distinct responsive calendar/sequence variant with mixed-project sprints.
- Evaluate on the same fixture: four sequence blocks with varied daily timing, multiple projects inside one sequence and potentially inside one sprint, partial-day calendar constraints, Saturday normal, Sunday off, and canonical OP source refs.
- Compare: comprehension, legibility, editing ergonomics, provenance links, persistence/diff/patch safety, render parity, offline/static fallback, NextDay handoff, and actual working interactions. Do not claim that styled HTML scrolling equals functioning interactivity.
- Choose exactly one source-of-truth architecture **only after operator review**. No default Q13 A accepted; existing live template remains as current implementation until changed through patches.

## New to-do — sequencing skill (operator requested)

**SEQ-SKILL-01: Design and create a lightweight sequencing skill/capability** able to transform Matrix 1 selected work + day/calendar capacity + operator constraints into flexible sequences and sprints, including optional multi-project composition, and produce references consumable by PrecapNextDay/FlowRecap.

- Status: **BACKLOG / DESIGN FIRST — NOT IMPLEMENTED**.
- Priority: **High**, critical prerequisite to final Matrix 2 behavior and Q13 prototypes; **not** automatically a new runtime agent/wrapper.
- Location: \`SEQUENCING-SKILL-CAPABILITY-BACKLOG-20261106.okf.md\` in this directory.
- First step: audit existing \`.claude/skills/Workflow&Processes/SKILL.md\`, \`PrecapNextDay\`, \`weekly-blueprint-standard.md\`, \`FlowRecap\` for reusable behavior; avoid building a redundant skill.
- Skills design requires explicit acceptance of inputs, outputs and connector use before creation, then a minimal \`SKILL.md\` and only necessary references/scripts.
- Must preserve D012 direct forked skill topology and no new persisted PM state.

## Outstanding operator questions (focused, not reinterpretations of accepted Qs)

- SEQ-A: In a sprint containing multiple projects, should the default be one shared outcome or multiple separately tracked mini-outcomes? (See sequencing skill backlog.)
- SEQ-B: Should four daily sequence blocks remain a standard **capacity starting point** but not a mandatory count?
- REC-A: Is "recap day" an existing consolidated end-of-day activity (using StatusMerge), or is there an additional source file to follow?
- VIS-A: Which of the three Q13 prototypes works best when the same sprint has tasks from two projects? Decision deferred pending actual visual prototypes.

## Verification boundary

Source evidence checked from GitHub \`main\` at 7cf9d923: active skill contracts, W45 drafts, dual-view specs and November 6 OpenProject decision candidate. No local Windows pull, live private OP API call, live calendar read, new sequencing skill creation, production patch, WP mutation or calendar write occurred in this decision capture.
