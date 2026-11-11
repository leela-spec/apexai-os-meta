---
okf_version: "0.2"
type: module-design-handover
durable_id: M01-MATRIX1-DESIGN-ASSUMPTION-FIRST-20261106
title: "Matrix 1 Design — Project Architecture, Epics, Critical Path, Decision Support"
description: "Standalone, bounded design handover that assumes upstream phases rather than blocking on their completion."
status: READY_FOR_OPERATOR_DESIGN_QA
date: 2026-11-06
repository: leela-spec/apexai-os-meta
baseline_main_at_intake: 46cbc4fb45b80e70b38fd9c532516032e89057d8
module: 01-weekly-command-brief
scope: Matrix_1_only
upstream_phases: ASSUMED_NOT_BLOCKING
current_runtime_owner: .claude/skills/PrecapWeek/SKILL.md
downstream_consumer: Matrix_2_then_PreCapNextDay
decision_source: research/OPERATOR-DECISION-DELTA-Q06-Q08-Q09-Q12-Q13-20261106.okf.md
production_mutation_authorized: false
openproject_live_verified: false
---

# Matrix 1 — Standalone design handover (assumption-first)

## 0. Read this first — mission and next action

**Operator direction (2026-11-06):** "It's the handover to design matrix one. Let's work with assumptions regarding the phases before that."

Do **not** rerun a broad macro architecture project or demand completion of preceding phases. This handover is a self-contained starting brief for a focused **Matrix 1 design** conversation.

**Design question:** "For each relevant project, what is the actual/assumed starting position, what development architecture connects it to meaningful outcomes, which prerequisites are blocking, which work should be pursued next, and what evidence would show success?"

Build the **information and decision design for Matrix 1**, not a standalone PM system, not a calendar, not a new sequencing Skill, and not a production patch yet. The first design exercise should show one concrete project workstream and compare genuinely useful visualization/information-depth choices; then run targeted high-impact operator Q&A to refine the model.

### Outputs expected from this design work

1. One explicit, accepted Matrix 1 **user-job and capability contract** (what an operator must understand and decide).
2. A small, testable **source-to-display information map** with authority/freshness/uncertainty semantics and zero invented numeric OpenProject IDs.
3. An agreed **project/epic/task/dependency/iteration model** for both serial and parallel work, with correctly defined evidence-backed critical path.
4. A **shortlist/longlist and weekly outcome selection** model without forcing calendar sequencing or micro-sprint detail.
5. **2–3 concrete Matrix 1 presentation alternatives** using the same sourced/labelled fixture, followed by one operator choice of preferred direction for Matrix 1. Do not prematurely decide the global Q13 canonical rendering/serialization architecture.
6. A tested minimal **Matrix 1 -> Matrix 2 export/selection interface** (identity-stable refs, not a duplicated PM database).
7. An **operator decision ledger** and bounded exact-context **patch-only implementation handover** for after the design is accepted. Do not directly change current live skill/template in this design phase.

**Success criterion:** A person unfamiliar with the internal architecture can look at Matrix 1 and say: "This project is here; these are its next meaningful steps; this is the blocking prerequisite; this is the output; these are the items we are choosing now and deferring; this is why."

## 1. Non-negotiable accepted decisions (do not re-open by accident)

| Ref | Accepted requirement | Matrix 1 consequence |
|---|---|---|
| D012/D013 | Main-thread weekly-orchestrator dispatches directly forked stage Skills; no legacy wrapper agents | Matrix 1 is the PrecapWeek output component, never a new orchestrator |
| DESIGN-DECISIONS.md + operator Q01 | One Weekly Command Brief, human-first, one final portfolio gate | Matrix 1 is a section, with integrated operator choices, not a competing artifact |
| Q01 (accepted B) | OpenProject owns PM status/commitments **for enrolled work**; Git/accepted decisions/tests own implementation evidence | Show different fact types and provenance, not one universal truth claim |
| Q02 (accepted B) | Continue in honest degraded mode if OP identity unavailable | Preserve local source ref, explicitly say OP-UNRESOLVED; never fabricate WP#IDs |
| Q03 (accepted B) | Dynamic project coverage; no mandatory four/five-project roster | Include active and intentionally deferred projects; Priority Website identity is unresolved |
| Q04 (accepted A) | Project -> Epic -> Task, selective subtask expansion | Depth is decided by usefulness, not required 30-minute sprint decomposition |
| Q05 (accepted A) | Critical path is grounded in real prerequisites; shortlist reflects readiness/leverage/constraints | No score-based faux critical paths |
| Q06 correction | **Sequence means variable time/capacity block**; may span projects, a sprint can mix project work | Matrix 1 must NOT identify projects as Seq 1-4; export task refs that can coexist in any sequence |
| Q08 correction | Detailed sprint planning, cards/prompts and exact intra-day order belong to PrecapNextDay | Matrix 1 shows evolution, prerequisites and selected outcomes, not microtasks |
| Q09 correction | Saturday normal workday; Sunday off by default with explicit operator exceptions | Not a Matrix 1 schedule field, but never assume a Friday-only milestone just because legacy sample does |
| Q11 | Compact embedded presentation_handoff in the combined Weekly Brief | Matrix 1 produces stable refs/sections to point to, no second machine seed |
| Q12 correction | Existing FlowRecap -> StatusMerge -> PM update -> NextDay must be reused | Matrix 1 does not own completion writes or replace recap stages |
| Q13 correction | Final presentation and source format choice explicitly OPEN | Compare Matrix 1 layouts without unilaterally selecting MD/HTML/structured source |
| Q14 | Real workflow and independent verification determine readiness | No PASS just for Markdown headings or a pretty graph |

Ratings I/E/R may support **decision Q&A** as estimates, but there is no mandatory synthetic single work score or priority gate. Here E = evidence, never effort.

## 2. Upstream phases — temporarily ASSUMED, not blocking

Use the assumptions below to proceed. Each can be replaced by future verified evidence without redefining Matrix 1 itself.

| ID | Working assumption for design | Confidence/status | Change trigger | Matrix 1 behavior |
|---|---|---|---|---|
| A01 | PrecapWeek is the weekly output owner under D012 | VERIFIED_REPO | Accepted runtime revision | Design one section in Weekly Brief |
| A02 | For enrolled projects, live OP WPs describe current PM commitments; enrollment varies by project | OP POLICY_ACCEPTED; LIVE_ENROLLMENT_UNVERIFIED | Live root/whoami/project.list/wp.list | Show provenance and unresolved identity |
| A03 | Git, repo AGENTS/accepted decisions and tests describe code/design existence and completion proof | ACCEPTED_POLICY | Source conflict or accepted exception | Present PM status separately from build evidence |
| A04 | A concise intake can reference the relevant current WP frontier instead of pasting every task | WORKING_ASSUMPTION | Consumer audit shows missing information | Expand only evidence needed for relevant epics |
| A05 | Legacy Apex Session/Sync have genuinely Apex-native control-plane roles; migrating PM work should not mirror into their task graph | OPERATOR_DIRECTION; ROUTING_UNPATCHED | Owner-aware mutation design accepted | Treat as provenance/fallback, never double-write |
| A06 | Matrix 2 will allocate Matrix 1 selected work into variable time blocks, possibly mixed-project | OPERATOR_CONFIRMED | Further sequencing-detail decision | Export multiple refs; no M1 sequence lane |
| A07 | PrecapNextDay/FlowRecap/StatusMerge already provide daily execution/recap spine | VERIFIED_REPO | Mixed-flow compatibility review | Matrix 1 stops before these responsibilities |
| A08 | Specific sequence-to-flow mapping and sprint-mixing heuristics are undecided | OPEN_BELOW_THIS_MODULE | Sequence capability design | Export task references independent of flow schema |
| A09 | Life/personal routines and energy/focus constraints belong in holistic sequencing/calendar design, not technical project process DAG | SOURCE_BACKLOG_UPDATED; SCOPE_ASSUMPTION | Operator asks for non-project objective coverage in M1 | Keep M1 focused; expose capacity needs only as handoff hints |
| A10 | Calendar availability, weekday positions and sprint durations are external temporal concerns | ASSUMED_BOUNDARY | Matrix 2 design accepted | No clock-times, day allocations or 30m units in M1 |
| A11 | W45 draft is a committed **design fixture**, not proof of current OP status, hardware readiness, real milestone or calendar | VERIFIED_REPO_AS_DRAFT | Real OP and repo reads | Label every illustration DRAFT/ASSUMPTION |
| A12 | Priority Website might be MoA workstream or separate project; cannot decide from W45 name alone | OPEN_IDENTITY | Per-project source read/operator identity statement | Display a provisional classification review flag, never silently merge or invent a fifth project |
| A13 | The old 2026-08-18 "every task has 30m sprint units, 5 projects, synthetic composite score" requirement is superseded by operator Q03/Q04/Q05/Q08 corrections | CONFIRMED_CONFLICT_RESOLUTION | Explicit new operator decision | Preserve useful epic/dependency insight; discard forced microdepth/composites |
| A14 | Sunday timing of weekly Precap and OpenProject write privileges are not settled | OUT_OF_SCOPE_FOR_MATRIX1 | Later macro/module reconciliation | No dependency on them for present non-temporal model |

**Do not stop design** due to A02/A05/A08/A12/A14. Use clearly labelled fixtures and record which later integration step will validate the assumption. If a source claim materially changes a critical path or external state mutation, retain a review flag and avoid presenting it as confirmed.

## 3. Source map — fetch in this order (reference paths, not copies)

### Tier 0: operator intent and runtime contracts (mandatory)

1. \`apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/research/OPERATOR-DECISION-DELTA-Q06-Q08-Q09-Q12-Q13-20261106.okf.md\` — operator answers **override** previous proposal choices where they conflict.
2. \`apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/DESIGN-DECISIONS.md\` — validated human output, project coverage, week/day ownership; interpret through later operator corrections.
3. \`apex-meta/tools/project-improvement-orchestration-weekly/DECISIONS.md\` — D012/D013 direct fork topology; O002 existing workflow-process dependency.
4. \`.claude/skills/weekly-orchestrator/SKILL.md\` — current central routing/gates.
5. \`.claude/skills/PrecapWeek/SKILL.md\` — active weekly worker, known scope and OP overbroad claim.
6. \`.claude/skills/PrecapWeek/weekly-command-brief-template.md\` — active human-facing output shape; Matrix 1 location and embedded YAML handoff.
7. \`apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/README.md\` and \`HANDOVER.md\` — bounded Module 01 mission.

### Tier 1: Matrix 1 design authorities and operator examples

8. \`apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-01-PROJECT-MATRIX-EPICS-CRITICAL-PATH.md\` — existing detailed hierarchy/DAG intent. **Exception:** forced five projects, mandatory numerical composite scores and 30m micro-sprint units are not accepted under latest operator answers.
9. \`apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/SPEC-DUAL-VIEW-WEEKLY-PRECAP.md\` — dual-view separation and example Matrix 1 hierarchy, but inconsistent Seq=project naming in Matrix 2 and effort/evidence metric labels.
10. \`apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/research/ORCHESTRATOR-MATRIX-1-DESIGN-HANDOVER-20261106.okf.md\` — initial proposed source/provenance/shortlist contract, to refine in this handover.
11. \`apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/research/ORCHESTRATOR-MODULE-01-QA-BOARD-20261106.okf.md\` — earlier 14 Q&As; Q01–Q05 accepted, Q06/Q09/Q12/Q13 corrected later. **Do not restart those decisions.**
12. \`apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/WEEKLY_PRECAP_DRAFT_W45.md\` — fixture/example of process graph and project sections; **not live project truth**.
13. \`apex-meta/operator-output-design/step3-output-design-system/03-planning-artifact-designs.okf.yaml\` — recovered J2 operator purpose and outcome model; rationale, not higher precedence than live skill/confirmed operator decisions.

### Tier 2: conditional source ownership and downstream interface (load when needed)

14. \`apex-meta/handoff/weekly-orchestration-openproject-transition-2026-11-06/01-DECISION-OPENPROJECT-WEEKLY-ORCHESTRATION.okf.md\` and \`02-CONFLICT-AND-DECISION-LOG.okf.md\` — enrolled-project PM authority and conflicts.
15. \`leela-spec/agent-skills\` (\`master\`) \`skills/openproject/SKILL.md\` and \`references/write-policy.md\`; local CLI \`node C:\GitDev\agent-skills\skills\openproject\client\opCall.js\` — canonical OP API. Read-only verification must include root/whoami, project.list, doctor for selected project and **paginated** wp.list. Never invent numeric IDs; no token leakage.
16. Project-specific \`AGENTS.md\`, accepted decisions, README/current-state, implementation ledgers, tests/commits from repos \`leela-spec/MasterOfArts\`, \`leela-spec/Investment\`, \`leela-spec/Leela-Cloud-2026\`, \`leela-spec/apexai-os-meta\`; other projects only if operator/current context establishes relevance.
17. \`apex-meta/tools/project-improvement-orchestration-weekly/MASTER-INFORMATION-FLOW-AND-DESIGN-CRITICAL-PATH-20261106.okf.md\` — earlier macro information map and initial conflict ledger; upstream detail assumed for this design.
18. \`apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/research/SEQUENCING-SKILL-CAPABILITY-BACKLOG-20261106.okf.md\` — current semantics, including life/work context and Flow Card enrichment; **do not create/implement skill here**.
19. \`.claude/skills/PrecapNextDay/SKILL.md\`, \`templates/precap-next-day-brief-template.md\`, \`templates/flow-execution-card-template.md\` — consumer/provenance only.
20. \`.claude/skills/flow-recap/SKILL.md\`, \`.claude/skills/status-merge/SKILL.md\` — completion/candidate-to-confirmed distinction; not part of Matrix 1 authoring.
21. Historical W34 planning/next-day fixtures under \`artifacts/weekly-plans/\` and \`artifacts/next-day-plans/\`, when comparing before/after. Old models are not production templates.

**Precedence rule:** user's newest explicit decisions > earlier design proposals on the same issue; runtime skill describes what code *currently* does, not necessarily what operator has newly authorized; source-type-specific authorities own facts; old illustrative IDs never turn into real identifiers.

## 4. Current state and discrepancy list

- **Implemented today:** a live PrecapWeek Skill with Weekly Command Brief output, a Matrix 1 placeholder in template, two-matrix concept, D012 direct fork; project-epic-DAG concepts exist in handovers and W45 draft.
- **Not yet verified today:** OP private live project/WP frontier; actual latest project dependencies and completion state; whether sample files/paths in W45 exist; whether the Priority Website is a separate enrolled project.
- **Known contradictions in live/current docs:** (i) v4.1 Matrix 2 falsely equates Seq N with projects despite latest Q06, (ii) forced 30-minute Matrix 1 tasks despite Q08, (iii) fixed five-project DoD despite Q03, (iv) numeric composite priority despite Q05/no synthetic score, (v) universal OP authority vs enrolled-project-only, (vi) live Mon–Fri excludes operator-approved Saturday, (vii) stale template source_gap.
- **Matrix 1 action:** design robust source-aware information model and operator display; **do not repair these unrelated production files during design**. Put precise patch targets in the eventual implementation handover.

## 5. The intended Matrix 1 process (macro -> meso)

### Phase A: build the project landscape (non-temporal)

1. Resolve actual project identities and per-project source owner. Display all relevant projects, including purposefully inactive/deferred, and classify uncertain identities explicitly.
2. For each project, identify current **baseline**, desired **destination**, the nearest worthwhile **outcome** and the evidence that would count as success.
3. Group actual/sourced candidate work by **epic or meaningful workstream**. Do not force an OP hierarchy where repo facts differ; record which labels are interpreted vs native OP WPs.
4. Distinguish status facts: OP status (if verified); repo implementation evidence; operator target; uncertainty. Label observed_at/source_ref where material.

### Phase B: construct the work architecture

5. Model project -> epic/workstream -> task/WP -> selective subtasks and **development order**.
6. Classify edges as prerequisite, "unblocks", parallel opportunity, feedback/iteration, or loose association; only genuine prerequisites form a gating DAG.
7. Detect blockers, conflicts and critical path. An item is on a **critical dependency chain** if it blocks a consequential deliverable. A mathematically longest *schedule-critical* path requires duration/deadline evidence, which Matrix 1 need not invent.
8. Record important review/test/decision gates and outputs. Iteration means a potential return to earlier state: show as review/rework loop outside the prerequisite DAG, not as a cyclic dependency in a topological graph.
9. Identify useful parallel work if other prerequisites are blocked or waiting.

### Phase C: select weekly commitments, not time slots

10. Produce a **shortlist** of a small number of high-leverage, dependency-ready, operator-aligned outcomes with expected deliverable and evidence. Status **PROPOSED** until approved; never imply OP task assignment/write.
11. Retain a **longlist** for follow-up/later work with reason and revisit trigger (blocked, capacity-limited, waiting on proof, low leverage, pending decision).
12. Show consequences: "If [schema gate] completes, [PDF generation] becomes ready; if not, [dashboard review] remains feasible in parallel."
13. Export stable selected-work references + outcome/evidence/dependency/readiness flags to Matrix 2, where weekday/time/sequence planning is performed.

**Never:** reserve calendar slots; identify Seq 1 as a project; invent an exact hour count; create Flow Cards/prompt assets; accept a proposed WP update; duplicate every OP work package into a second persistent database; manufacture priority scores.

## 6. Proposed information contract (for human design, not a new PM schema)

| Unit | Essential fields | Visible only when material |
|---|---|---|
| Project header | project display name, real project key/source, current strategic goal, observed baseline and uncertainty | operator owner, enrolled OP project ID |
| Workstream/Epic | name, outcome, why it matters, review/done evidence | cross-project leverage, parallel path |
| Work item | **stable work_ref + ref_kind**, concise action, current observed/assumed state, expected output | native WP ID/status/updated_at, implementation evidence and accepted design |
| Relationship | depends_on, unblocks, parallel_with, iteration/review edge | reasons, cross-project interface and source reliability |
| Readiness | ready, blocked, waiting_on_decision, needs_source_verification, already_completed_evidence_not_reconciled | blocker owner and resume trigger |
| Selection | shortlist (candidate/accepted) or longlist (staged/deferred) | I/E/R inline estimates ONLY if useful; no composite rank |
| Result/evidence | artifact type/ref, acceptance condition, verification owner | build/test receipt, critical milestone proof |
| Provenance | source kind/ref/observed_at, evidence vs proposal | contradiction and freshness flag |
| Matrix 2 handoff | selected work refs, expected outcome, dependencies, readiness, scope hints | rough work size or priority constraint **as hint**, not scheduled times |

**Cardinality:** one project -> many epics; one epic -> many work items; one task may support several outcomes; work items may have multiple prerequisites; an item's selection may be used in several different later sequences. Never make the calendar the identity key.

## 7. Concrete design fixture (source-grounded as a DRAFT, not verified live state)

Use **Master of Arts invoice development** from the committed W45 example. It contains a provisional development chain:

\`\`\`text
Project: Master of Arts  [repo/current OP status: UNVERIFIED]
Workstream: Invoicing

[W45-LOCAL-MA-03] Invoice data schema
           |
           | prerequisite (draft claim)
           v
[W45-LOCAL-MA-04] PDF template engine
           |
           | prerequisite (draft claim)
           v
[W45-LOCAL-MA-05] Accounting export gate

Parallel: Website navigation and copy/asset sync
\`\`\`

None of those \`W45-LOCAL-*\` labels is a verified OpenProject ID. The actual W45 artifact uses provisional \`[WP-MA-03]\` and \`[OP-OFFLINE: WP-MA-03]\` markers; these have been explicitly converted to **demo-local references** to avoid suggesting current API fact. Do not claim an invoice engine exists or works without current source/test evidence.

Suggested operator-facing miniature:

> **Master of Arts — invoice workflow** (source: W45 design fixture; live status unknown)
>
> **Where:** invoice pipeline exists as a *proposed process*; actual implementation must be read.
>
> **Desired outcome:** reviewable invoice output and export evidence.
>
> **Path:** Schema validation -> PDF generation -> accounting export check.
>
> **Blocking question:** Is schema/financial formula already verified? If not, PDF/export readiness is conditional.
>
> **Proposed shortlist:** verify schema gate and produce acceptance evidence; PDF/export follows when ready.
>
> **Longlist:** styling and extra automation if they do not unblock the current gate.
>
> **Matrix 2 handoff:** source ref for schema gate, output requirement, readiness + blocker. **No specific day, time or sprint count.**

Use at least a **second fixture** with parallel branches from Apex OS or Leela (also labelled illustrative), so the design can show joins, iteration loops and cross-epic prerequisite links.

## 8. Presentation-design variations — compare on one identical fixture

Do not decide the global Q13 storage/rendering architecture yet. Evaluate **Matrix 1 view design** independently.

| Candidate | Operator experience | Good for | Potential weakness |
|---|---|---|---|
| V1 — Project Strategy Ledger | Each project has goal/baseline/shortlist/longlist and concise blocker rows; expand epic details on demand | Fast portfolio overview, evidence/review | DAG relationships less visible |
| V2 — Epic Dependency Map + Side Ledger | Per-project graph (real prerequisite arrows/parallel branches/iteration markers), linked to shortlists and evidence | Understanding how work unlocks other work | Graph congestion, uncertain edge provenance |
| V3 — Progressive "Project -> Epic -> Work" drilldown | High-level outcomes at first glance, one expanded project with full dependency/decision/evidence detail | Both overview and substantial depth | Needs careful static/interactive fallback and navigation |

**Design test:** With the **same** W45 invoice fixture plus one parallel workstream, can a novice answer in 20–30 seconds (not a performance claim, just a user test) where work stands, what's next, why it is blocked, what happens when completed, and what is deferred? Show comparable low-width and wide-screen information density. Do not say HTML scrolling alone is genuine interactivity.

## 9. High-impact Matrix 1 decisions to resolve (after concrete examples)

The older Q01–Q05 have already been operator-confirmed as principles. The following are **new implementation/design choices within those boundaries**, not attempts to reapprove the same fundamentals.

| ID | Level (estimated I/E/R) | Exact unresolved Matrix 1 choice | Default hypothesis |
|---|---|---|---|
| M1-D01 | L3 (I94/E69/R58) | What is the smallest project/epic/task view that still explains the whole development path? | Progressive overview + expandable evidence, not raw OP backlog dump |
| M1-D02 | L3 (I93/E58/R67) | How are native OP epics/WPs reconciled with repo workstreams and operator language when their boundaries differ? | Show actual owner plus optional display grouping; do not mutate hierarchy |
| M1-D03 | L3 (I95/E65/R70) | How are prerequisite edges, parallel branches, review/rework loops and *true* critical chain distinguished visually? | Directed prerequisites + separate annotated feedback loops; never infer duration-criticality |
| M1-D04 | L3 (I92/E60/R65) | How should cross-project dependencies and shared deliverables appear without creating a fictitious umbrella WP? | Linked work refs with owner on each side, named integration gate |
| M1-D05 | L2 (I88/E77/R40) | How many weekly outcomes or shortlisting layers are readable per project before the display becomes backlog spam? | 1 strategic target and 2–4 meaningful subtargets, expansion optional |
| M1-D06 | L3 (I94/E55/R69) | How to show OP "closed/open" vs passing Git tests or unresolved implementation evidence? | Separate status and implementation/evidence fields; explicit conflict note |
| M1-D07 | L2 (I86/E76/R32) | How to mark evidence, assumptions, provisional IDs and freshness in a readable view? | Compact in-line source marker plus material uncertainties, detail on demand |
| M1-D08 | L3 (I90/E57/R62) | What precisely makes a work item shortlist-ready if its predecessor is partially verified or blocked? | Distinguish executable, preparation-only, blocked and review-dependent candidates |
| M1-D09 | L2 (I83/E72/R35) | How should "Why this week" and strategic leverage be shown without calendar times or composite numeric priority? | One consequential reason, explicit dependency/deliverable and constraint |
| M1-D10 | L3 (I91/E45/R60) | How is "Priority Website" classified—separate project, Master of Arts epic, or source-unresolved? | Unknown until actual owner/source review; no forced fifth project |
| M1-D11 | L2 (I85/E68/R42) | What is the best Matrix 1 -> Matrix 2 selection payload when one later sequence may mix projects? | Stable work refs and readiness/evidence; no copied task graph or sequence ID |
| M1-D12 | L3 (I91/E54/R70) | Which user-facing layout (V1/V2/V3 or hybrid) works for many projects, branching graphs and longlists on desktop/mobile? | Compare real identical fixtures before choosing |
| M1-D13 | L2 (I82/E76/R35) | Do explicit iterative/review gates need a separate progress status, or can existing WP status + evidence represent them? | Use lightweight edge/gate annotations; no parallel lifecycle state machine |
| M1-D14 | L3 (I92/E66/R61) | How does the design handle "no live OP", empty project coverage and conflicts without inventing work? | Honest degraded view with named missing facts and operator actions |
| M1-D15 | L2 (I84/E70/R42) | How much accepted/deferred project detail should be visible when no weekly work is assigned? | Compact name + reason + trigger + source |

**Decision procedure:** Use the operator's required Q&A format:
- *Question:* one exact decision, title with \`Lx (I#/E#/R#)\`.
- *Options:* letters A/B/C, each mechanism in 2–4 lines, grounded user stories/everyday examples and separate \`(I#/E#/R#)\` estimates per option.
- *Recommendation:* one letter.
- *Reasoning:* grounded, dense tradeoff analysis.
- *Notes:* one rejection reason per non-selected letter.
- At L2 add a worked realistic example **per option**, source-type evidence, reversal cost and conditions that would change the recommendation.
- At L3 **first run a comprehension check**, add 2+ user stories/personas and a labelled fixture simulation **per option**, plus independent verification and a reply sheet with recommended defaults. Silence may accept drafting defaults for discussion only, **never** real OP/calendar mutations.
- Split questions into focused rounds: **R1 user jobs/decomposition (D01-D05)**; **R2 evidence/readiness/selection (D06-D11,D13-D15)**; **R3 view design (D12)**. Do not ask a flat set of 15 jargon-only questions; show the fixture and current source snapshots first. The user can override \`L3\` to \`L2\` explicitly.
- Only ask about unresolved consequence-bearing choices; automatically apply already accepted operator decisions.

## 10. Interfaces and exact module boundaries

\`\`\`text
Current project truth (OP for enrolled commitments; Git/tests for implementation)
       + operator intent and relevant recent evidence
                         |
                         v
     PrecapWeek / Matrix 1: PROJECT DEVELOPMENT
       projects / epic workstreams / work refs
       baseline -> goal -> dependencies / gates
       selection / evidence / blockers / deferments
                         |
               selection refs only
                         v
     Matrix 2: WEEKLY TEMPORAL ALLOCATION
       variable sequences/blocks, time windows, possibly mixed projects
                         |
               one embedded handoff
                         v
     PrecapNextDay: detailed flows, sprints, Flow Cards, prompts
                         |
                execution / FlowRecap / StatusMerge
                         |
                 authorized PM write + refreshed state
\`\`\`

For **Matrix 1 -> Matrix 2**, the minimum meaningful fields to exchange by reference are:
\`\`\`yaml
selected_work_reference:
  project_ref: "<resolved project or explicit unknown>"
  work_ref: "<canonical OP WP only when verified; else explicit local source ref>"
  ref_kind: "openproject_verified | repo_native | demo_local_unresolved"
  outcome: "<intended useful result>"
  expected_evidence: "<observable completion condition>"
  prerequisite_refs: []
  readiness: "ready | blocked | review_needed | unverified"
  criticality_basis: "<actual gating evidence or unknown>"
  operator_scope_state: "proposed | accepted | deferred"
  source_ref: "<actual reference>"
\`\`\`
**This is an illustrative interface, not authorization to introduce a new persisted YAML packet or schema authority.** Matrix 2 may reference entries in the Weekly Brief directly or consume a small derived selection view. Source IDs and done evidence must be traceable across several sequences/sprints without ambiguity.

## 11. Validation and definition of done

### Design quality acceptance

1. Operator can identify baseline, nearest useful outcome, next step, gating prerequisite, deliverable and deferred alternatives without reading schema terms.
2. Matrix 1 shows all relevant projects, including compact entries for those deliberately deferred; a fifth project isn't created by title coincidence.
3. All dependency arrows have explicit meanings and, where critical, grounded evidence. Feedback loops are not presented as invalid prerequisite DAG cycles.
4. An OP WP's PM state is never used as proof of tested code. Unverified references cannot be mistaken for real OP numbers.
5. Shortlist is differentiated from longlist by concrete selection/deferral reasons; no forced 30-minute unit breakdown and no mandatory I/E/R score.
6. Matrix 1 has no calendar time or "Seq 1 = Project A" assumption.
7. One project/work item can move into different later sequences without acquiring a new task identity.
8. A mixed-project sequence consumes multiple Matrix 1 refs and can ultimately produce per-project evidence; no recap implementation required in this design module.
9. Three comparable variants use exactly the same fixture; operator chooses a **Matrix 1 information-view direction**, without preempting global Q13 rendering authority.
10. The output includes a durable decision ledger, source matrix, a minimal producer/consumer contract and candidate **patch-only** instructions; design approval occurs before production patching.

### Later integration verification (not design prerequisite)

- Real read-only OP coverage/project identities and paginated WP relations in authorized local runtime or explicit unverified boundary.
- Verify project-specific AGENTS/accepted decisions and source code evidence for selected work packages.
- Cross-check live PrecapWeek template/skill and following Matrix 2/NextDay consumer after narrow patches are proposed.
- Use existing W34 and W45 fixtures for regression **without** mislabeling them as live.
- Two independent reviews: ownership/provenance and operator comprehension/usefulness.
- Actual production changes only by exact-context diff patches to current \`.claude/skills/\` files, after the operator approves the design.

## 12. How to start the next Matrix 1 design conversation

1. Read this handover and Tier 0/Tier 1 sources in order.
2. State the **accepted boundaries** and the assumptions you will use. Do not ask to finish OpenProject integration or sequencing-skill creation first.
3. Show the W45-derived Master of Arts invoicing development map and a Leela/Apex parallel-path example, both clearly marked **illustrative/unverified**.
4. Show V1 (strategy ledger), V2 (dependency map + ledger) and V3 (progressive drilldown) as *information architectures* with identical work items.
5. Run the first comprehension check and the first bounded Q&A round D01-D05 in the exact I/E/R L0–L3 format, with meaningful simulations and real-world interpretation.
6. Capture operator decisions, iterate the design in place (as proposals) and then advance to evidence/selection and display rounds.
7. Produce a final accepted Matrix 1 model plus narrow implementation patch handover, which the temporary Master can verify against the whole Weekly loop.

**Immediate next action:** Begin **Matrix 1 design R1**. Do not require another macro-architecture handover, live OP runtime, calendar connection, or fresh skill scaffolding to start.

## 13. Explicit out of scope

- Rebuilding Weekly Orchestrator, D012 fork topology or legacy wrapper agents.
- Creating or installing the Sequencing Skill during Matrix 1 design.
- Repairing the existing status-merge/OpenProject write path, calendars, Google Calendar connectors or Sunday scheduling.
- Final Matrix 2 visual/calendar design, exact sprint timelines, Flow Card generation or prompt generation.
- Broad PM migration, new task database, changing WP status, inventing OpenProject numeric IDs.
- Whole-file rewrite of existing runtime files, silent contradictory authority promotion, or claiming design/prototype file creation equals production readiness.
