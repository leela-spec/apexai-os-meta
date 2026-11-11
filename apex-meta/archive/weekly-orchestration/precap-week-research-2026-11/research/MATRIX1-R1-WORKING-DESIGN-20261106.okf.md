---
okf_version: "0.2"
type: module-design-working-proposal
durable_id: M01-MATRIX1-R1-DESIGN-WORKING-20261106
title: "Matrix 1 — R1 project architecture, hierarchy, dependencies, and scope choices"
description: "Unapproved operator-review proposal with identical labelled fixtures, three view alternatives, and decisions M1-D01 through M1-D05."
status: DRAFT_FOR_OPERATOR_REVIEW
date: 2026-11-06
repository: leela-spec/apexai-os-meta
source_baseline_main: 5a316e6bb14118a32ca174826b5635ed87360c59
source_handover: apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-MATRIX-1-DESIGN-ASSUMPTION-FIRST-20261106.okf.md
source_fixture: apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/WEEKLY_PRECAP_DRAFT_W45.md
scope: Matrix_1_design_only
operator_approval: NOT_REQUESTED
production_mutation_authorized: false
openproject_live_verified: false
---

# Matrix 1 — R1 working design

## Purpose and boundaries

This is a **design proposal**, not a confirmed week plan, OpenProject read, verified project baseline, or production patch. Operator decisions Q01-Q05 and corrected Q06/Q08/Q09/Q12/Q13 plus accepted D014-D017 remain authoritative. This round only explores information architecture: M1-D01...D05. Previous upstream phases are assumed, not required for design. Matrix 1 is one non-temporal section of the Weekly Command Brief, owned by PrecapWeek.

### Source inspection receipts (GitHub, 2026-11-06)

- Current source baseline: main 5a316e6bb14118a32ca174826b5635ed87360c59, whose commit handovers Matrix 1 design using assumed upstream phases.
- PrecapWeek live SKILL and active weekly-command-brief-template exist, but include legacy fixed Seq=project and synthetic OpenProject placeholder patterns. Current template is not an accepted production description of the new model.
- Durable DECISIONS.md records D014 OpenProject dependency intake priority, D015 owner-aware later PM writeback, D016 deferred stateless sequencing skill and D017 Saturday Precap/Sunday-off timing.
- Source authority by fact type: OP for *verified enrolled-project PM commitments/status*, Git/accepted decisions/tests for implementation proof, operator for priorities. The connected GitHub client cannot establish live private OpenProject work-package status.
- W45 draft is a design fixture. Its [WP-MA-*] and [WP-APEX-*] are not verified OpenProject IDs. No empirical schedule-critical path may be asserted from it.

## Operator job/capability hypothesis (M1-D01, not yet accepted)

Operator user story: "When I prepare a week, I need to understand where each relevant project actually stands, its nearest consequential deliverable, the steps and gates to reach it, and useful parallel alternatives. I want to choose outcomes without sorting through every work package, guessing a critical path or planning the day's sprints."

Reviewer user story: "When I inspect a claimed blocker/ready state, I can trace the work reference, source, evidence and prerequisite; I can distinguish unverified source claims from PM status and working code."

Non-temporal pipeline:
1. Identify dynamic relevant projects; compactly retain deferred items.
2. Separate project goal, baseline, epic/workstream, task/WP, selective subtask.
3. Associate native source refs, provenance, uncertainty and evidence.
4. Build *typed* dependency edges; keep feedback/rework separate from prerequisite DAG.
5. Identify actual blocking prerequisites and consequential deliverables; mark critical-chain evidence vs unknown duration-criticality.
6. Propose a small weekly shortlist with outputs/evidence and keep explicit longlist reasons/triggers.
7. Export stable work refs with readiness; do not allocate blocks, sequences, sprints, calendar time or write PM state.

## Same labelled fixture for all three views

**EVERY ITEM BELOW IS W45 DRAFT-ILLUSTRATIVE; current implementation, OP identity, status and relations are UNVERIFIED.**

Source file: WEEKLY_PRECAP_DRAFT_W45.md, Matrix 1 project graph and MoA detail, 2026-W45 example.

- Master of Arts / Invoicing: W45-LOCAL-MA-03 invoice data schema -> W45-LOCAL-MA-04 PDF template engine -> W45-LOCAL-MA-05 accounting export gate. DRAFT dependency claim.
- Master of Arts / Website (parallel): W45-LOCAL-MA-01 responsive navigation -> W45-LOCAL-MA-02 copy/asset sync.
- Apex OS / OpenMouse (parallel join): W45-LOCAL-APEX-01 USB HID polling -> W45-LOCAL-APEX-02 click/hold intercept; intercept -> W45-LOCAL-APEX-03 latency benchmarking AND W45-LOCAL-APEX-04 HUD overlay integration; both feed W45-LOCAL-APEX-05 driver packaging.
- Proposed outcomes: MoA reviewable invoice export evidence; Apex OS packaging gate only after both branches have verifiable evidence. Not claims of existing finished software.
- Proposed weekly focus for illustration: verify invoicing schema/precondition; verify Apex intercept's actual prerequisite and collect evidence. Website work is parallel candidate, not selected by default.
- Longlist illustration: styling extensions, extra website polish, release packaging pending both gates.
- Identity: each W45-LOCAL-* reference is demo-local only, ref_kind=demo_local_unresolved. None is OP-WP#number. Critical path not proven.

## Comparable view alternatives — identical data

### V1: Project strategy ledger

| Project/epic | Observed baseline | Target / next useful output | Gate / what blocks | Shortlist proposed | Deferred |
|---|---|---|---|---|---|
| MoA — Invoicing | Live state unknown; W45 draft chain | Evidence-backed invoice export | Schema -> PDF -> export (draft only) | Check schema and tax evidence | PDF/export until confirmed |
| MoA — Website | Live state unknown | Navigation/copy work | Nav -> assets (draft) | None by default | Available parallel candidate |
| Apex OS — OpenMouse | Live state unknown | Verified packaging candidate | HID -> intercept; latency AND HUD -> packaging (draft) | Validate interceptor readiness | Packaging until join proven |

Best for portfolio scanning; weak at communicating branching joins.

### V2: Epic dependency map + source/decision ledger

~~~mermaid
flowchart LR
  M1["MoA | invoice schema"] --> M2["PDF template"]
  M2 --> M3["Accounting export"]
  N1["MoA | responsive navigation"] --> N2["Copy/asset sync"]
  A1["Apex | HID polling"] --> A2["Click/hold intercept"]
  A2 --> A3["Latency verification"]
  A2 --> A4["HUD integration"]
  A3 --> A5["Packaging gate"]
  A4 --> A5
~~~

**Legend:** arrows represent W45 DRAFT prerequisite claims, not verified current OP relations or duration-criticality. Each graph node links by stable *demo-local* ref to the ledger above with source/uncertainty, expected evidence, proposed scope and explanation. Real review/rework would be a separate annotated gate/loop, never a cycle in the prerequisite DAG.

Best for seeing branching/joins; can become unreadable when dozens of WPs appear.

### V3: Progressive project -> epic -> work inspection

Portfolio summary (collapsed):
- MoA: target invoice export; baseline unknown; principal gate schema evidence; shortlist schema verification; website available in parallel.
- Apex OS: target packaging evidence; baseline unknown; principal join latency + HUD; shortlist validate intercept baseline.

Expanding MoA -> Invoicing:
- Goal: reviewable invoice export, evidence yet to establish.
- Work sequence: [W45-LOCAL-MA-03] schema -> [W45-LOCAL-MA-04] PDF -> [W45-LOCAL-MA-05] accounting export. All DRAFT only.
- Proposed current investigation: determine whether schema and financial calculation proof exist; if missing, mark PDF/export as blocked/review-needed rather than ready.
- Source: W45 artifact. Project enrollment/PM state: OP_UNRESOLVED; repo implementation proof: NOT_YET_READ.
- Longlist: nice-to-have PDF styling (example), follow-up trigger: schema/PDF verification.

Expanding Apex OS -> OpenMouse:
- Work sequence: HID -> intercept -> two parallel checks (latency; HUD) -> packaging join.
- Proposed next step: verify whether HID and intercept are real/ready in Git; map corresponding enrolled OP refs if accessible; no guessed WP IDs.
- Longlist: packaging after both branches have success evidence.

Best for combining portfolio overview and depth; static fallback must preserve visible summary, current blockers and one-click/single-document accessibility.

### Comprehension test for all three views

A reader unfamiliar with the internal skills should answer:
1. What is each project's next worthwhile deliverable?
2. Which work has real versus merely illustrated prerequisite edges?
3. If invoicing is blocked, what MoA work could progress in parallel?
4. Why is Apex packaging behind a join of two prerequisites?
5. What is proposed this week, and what is deferred?
6. How can an unverified ref be passed to Matrix 2 without becoming an invented OP ID?

If a view fails these tests, adapt it. Readability at low width and many projects must be assessed before choosing one presentation direction (M1-D12 is R3, not R1).

## R1 operator decisions — proposed defaults only

Metrics I=impact, E=evidence confidence, R=reversal/risk exposure (1–100), estimated for design debate. They are **not work-item priority scores**. L3 means high-consequence design choice, not production approval.

### M1-D01 [L3 | I94/E69/R58] Smallest useful project-depth design?

A. Flat portfolio/project strategy ledger. (I75/E80/R35)
- Operator story: can scan projects quickly; cannot easily see nested blockers.
- Reviewer story: can check one-line sources; may need extra navigation to inspect a multi-gate epic.
- Fixture: invoice chain compressed to one row, Apex join hidden.
B. **Progressive project -> epic -> task depth, with selective subtask/evidence expansion. RECOMMEND.** (I95/E72/R43)
- Operator: sees all projects and nearest results first, drills into only the blocked epic.
- Reviewer: expands proof and source refs without a duplicated PM backlog.
- Fixture: MoA overview and invoice detail, Apex join expanded only if consequential.
C. All projects/epics/tasks/subtasks always fully expanded. (I81/E60/R68)
- Operator: has all details but high scanning cost.
- Reviewer: sees every source but can't prioritize consequential evidence easily.
- Fixture: W45 30-minute micro-units clutter Matrix 1.
Reversal: B can become a static layered document without changing source semantics. Change to A only if the user wants pure dashboard scan and separate detailed report; choose C only if proven high-density display remains readable.

### M1-D02 [L3 | I93/E58/R67] OP work hierarchy vs actual repo/operator workstreams?

A. Source-native hierarchy only, with exceptions as footnotes. (I80/E80/R50)
- Operator: faithful OP grouping but may find business outcomes split awkwardly.
- Reviewer: simple trace; cross-repo workstreams hard to follow.
- Fixture: invoice and website appear wherever upstream WP parents happen to place them.
B. **Preserve native ownership/IDs AND add display-only epic/workstream groupings. RECOMMEND.** (I96/E70/R43)
- Operator: sees meaningful invoicing/website workstreams without requiring OP restructuring.
- Reviewer: can trace each displayed task to its real owner and original hierarchy.
- Fixture: MoA invoice chain and parallel website grouped for presentation, source anchors unchanged.
C. Normalize every source into one new canonical hierarchy. (I70/E45/R85)
- Operator: clean display initially but risks losing accepted project reality.
- Reviewer: must reconcile two PM truths.
- Fixture: W45 demo labels could be incorrectly promoted as new canonical WPs.
Reversal: B display grouping can be renamed without mutating native sources. Switch to A if groupings add little value; C requires exceptional explicit data-migration approval and is not appropriate for this design.

### M1-D03 [L3 | I95/E65/R70] What constitutes a critical dependency chain?

A. Simple arrows and a single "critical" highlight. (I59/E45/R79)
- Operator: visually simple but may mistake parallel or feedback relations for blockers.
- Reviewer: lacks edge type/proof; can't audit a critical-path claim.
- Fixture: Apex latency and HUD paths both marked "critical" without explained joining evidence.
B. **Typed prerequisite DAG, separate parallel/review/feedback semantics; critical-chain labels only when backed by evidence. RECOMMEND.** (I96/E70/R39)
- Operator: understands what unlocks packaging and what can progress independently.
- Reviewer: audits prerequisite evidence and never mistakes an iteration loop for DAG cycle.
- Fixture: intercept branches to latency/HUD, both join at packaging; optional review loop annotated outside DAG.
C. Mathematical longest-duration path from estimates. (I73/E20/R87)
- Operator: falsely precise sequencing.
- Reviewer: cannot substantiate uncertain durations/deadlines.
- Fixture: W45 dependency graph has no trustworthy durations for calculation.
Reversal: B easily supports later real duration evidence. C becomes appropriate only after validated effort/time, resource and deadline inputs.

### M1-D04 [L3 | I92/E60/R65] Cross-project dependencies/shared deliverables?

A. **Link owning work refs on each side, annotate the shared integration gate. RECOMMEND.** (I95/E68/R45)
- Operator: sees who is waiting for whom across two projects.
- Reviewer: follows each source without a fake parent task.
- Fixture extension: if Apex UI requires Leela capability, link both verified refs, marking example as unverified until source confirmed.
B. Create an umbrella cross-project epic. (I76/E45/R72)
- Operator: convenient grouping but may suggest a new PM owner.
- Reviewer: has to track what the umbrella means versus original project records.
- Fixture: fake "Apex + Leela combined epic" risks becoming a duplicate WP.
C. Keep projects isolated, explain in prose only. (I63/E72/R66)
- Operator: can miss shared gates.
- Reviewer: cross-project edge less auditable.
- Fixture: Apex packaging appears unblocked even if a real Leela dependency exists.
Reversal: A is low-cost to remove/relink. B only if a real source owns an integration umbrella; C only for immaterial associations.

### M1-D05 [L2 | I88/E77/R40] How much weekly shortlisting per project?

A. **One meaningful strategic target plus approximately 2–4 useful subtargets for active projects; show more only when needed. RECOMMEND.** (I92/E74/R39)
- Operator: identifies practical weekly decisions without micro-sprint detail.
- Reviewer: can validate a shortlist entry's output and prerequisite.
- Fixture: MoA verify schema gate + optional parallel website readiness; Apex validate interceptor; packaging deferred.
B. Show full WP backlog/frontier in Matrix 1. (I75/E83/R69)
- Operator: may mistake full backlog for weekly commitment.
- Reviewer: completeness improves but relevance decreases; current live WP data still missing.
- Fixture: all W45 draft tasks appear as actionable.
C. Only one high-level goal for each project. (I73/E81/R55)
- Operator: minimal scan, but no concrete selection refs to Matrix 2.
- Reviewer: cannot test task readiness.
- Fixture: "deliver invoicing" with no schema/PDF/export breakdown.
Reversal: A is a display default, not hard limit. Expand when a project has many consequential gates; compress when project is deferred.

## Proposed R1 reply sheet (NO approvals inferred)

- M1-D01: B recommended; operator answer pending.
- M1-D02: B recommended; operator answer pending.
- M1-D03: B recommended; operator answer pending.
- M1-D04: A recommended; operator answer pending.
- M1-D05: A recommended; operator answer pending.
- View preference V1/V2/V3 intentionally non-binding until R3 (M1-D12).
- Comprehension check not yet answered by operator.

## R2 and R3 boundaries

R2: M1-D06...D11 and D13...D15: source evidence vs OP status, uncertainty/freshness, readiness, shortlist/longlist, Matrix 2 minimal work-ref handoff, empty/degraded state. R3: M1-D12 three alternatives, low-width / many-project check, one preferred Matrix 1 information view; global Q13 source/rendering architecture remains separately OPEN.

## Validation / no-write declaration

- GitHub source inspection happened; no live OP API call occurred in this chat.
- Every fixture is historical draft-only; no project completion, PM enrollment or critical path asserted as current.
- No production SKILL/template, OP task, calendar, recap path or sequencing Skill was altered.
- No operator decisions have yet been approved by silence. Later acceptance should create a durable R1 decision ledger and bounded patch-only implementation handover after the design rounds.

## Operator feedback delta — 2026-11-06 (later than R1 defaults)

**Latest explicit preferences override conflicting earlier R1 recommendations.** Unanswered design choices stay open.

- **V3 preferred:** Progressive project drilldown is the selected direction for further Matrix 1 exploration. Sophisticated dependency graphs are useful selectively, rather than as a permanent portfolio-wide task maze. Global Q13 source/rendering architecture remains OPEN.
- **Shortlist plus longlist required:** Shortlist is comparatively highest-priority weekly work; longlist holds nice-to-haves, later opportunities and work staged behind prerequisites. Keep hierarchical priority and reasons for selection/deferral.
- **M1-D05 count revised:** Do NOT impose a 1-target/2–4-subtarget hard rule. Per-project shortlist size varies by goal intensity, project and capacity. The operator sets the scope during weekly briefing. No numeric composite task priority score.
- **M1-D02 still OPEN:** The operator did not understand native OP hierarchy vs repo/operator grouping, and requests concrete examples. Do not treat recommendation B as accepted.
- **M1-D03 still OPEN:** The operator wants several different ways to present serial dependencies, branches/joins, evidence gates, cross-project links and feedback. No W45 draft arrow is current verified fact.
- **M1-D04 still OPEN:** No explicit cross-project representation choice this turn.
- **M1-D12 direction:** V3 is preferred as the high-level experience; a final hybrid and its rendering/serialization choice are not approved.
- **No production authorization:** Do not patch runtime Skills, OpenProject, calendar or recap stages during this design iteration.

### Companion exploratory artifacts (chat-delivered, not yet tracked in repo)

- matrix1-design-showroom.html — twelve genuinely different interactive layout prototypes with the same illustrative W45-derived four-project fixture; all employ progressive project/epic expansion where it serves the design.
- Q2 hierarchy lab: three explicit hypothetical mappings (MoA invoice, Investment pipeline, Leela/Apex integration) distinguishing original OP owner, repository organization and display-only workstream.
- Q3 dependency lab: five visual grammars (ribbon, fork/join, gate checklist, cross-project swimlane, feedback annotation).
- Local-only shortlist/longlist priority toggles and JSON export, explicitly unapproved and without PM mutation.
- matrix1-twelve-designs-overview.png — visual contact sheet. QA: twelve layouts rendered, hierarchy and dependency labs rendered, local priority interaction tested, mobile overflow corrected.

### Post-feedback decision state

| Choice | State |
|---|---|
| V3 progressive drilldown | OPERATOR_PREFERRED; further design selection pending |
| M1-D01 | Largely aligned with V3; fine detail still open |
| M1-D02 | OPEN; concrete examples requested |
| M1-D03 | OPEN; diverse visual implementations requested |
| M1-D04 | OPEN |
| M1-D05 | FLEXIBLE_OPERATOR_SET_SCOPE_CONFIRMED; reject fixed shortlist count |
| M1-D12 | V3 preferred, final hybrid and cross-device QA pending |
