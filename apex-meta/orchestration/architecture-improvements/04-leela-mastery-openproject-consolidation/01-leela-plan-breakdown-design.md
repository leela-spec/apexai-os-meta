---
type: Design / Import Plan
title: Leela plan → OpenProject breakdown design (read-only, pre-creation)
description: The complete epic→task→subtask→dependency mapping for transforming all open Leela orchestration plans (apex-meta epics + Leela-Cloud-2026 SSOT packets) into the private OpenProject instance. Design only — nothing created in OpenProject until the operator approves this structure.
tags: [openproject, leela, import-plan, dependencies, design, read-only]
status: draft
generated: { by: "claude/opus-4.8", at: "2026-09-26" }
stale_after: "2026-10-31"
authority: non-authoritative-design-proposal
implementation_authority: none
---

# Leela plan → OpenProject breakdown design

**Read this first:** This is a *design proposal*, not an executed import. Per the initiative handover's
safety boundary, the structural bulk-create is gated on explicit operator approval of this whole plan
seen as one picture — not discovered one confirm-prompt at a time. Nothing in this document has been
written to OpenProject.

## Operator decisions this design is built on (2026-09-26)

1. **OpenProject becomes the authoritative operational PM owner.** The Leela-Cloud-2026 repo SSOT PM
   layer (`STATUS.md` + packets) is to be narrowed/retired **later, in a separately-approved migration
   wave** — not as part of this import. Until then, the coexistence rule from all four prior research
   docs holds: *do not author the same operational PM fact in both OpenProject and a repo file* — during
   transition, OpenProject is the plan of record and the repo packets are treated as the migration
   source, not a parallel live truth.
2. **Scope = full Leela, both corpora:** (A) the 3 apex-meta Leela epics; (B) all 30 Leela-Cloud-2026
   orchestration packets.
3. **This pass is read-only design.** Create nothing until the structure below is approved.

## Live target confirmed (this session)

`leela-op178-openproject` = OpenProject **17.8.0**, authenticated as admin (token in
`C:\GitDev\leela-op178\op.env`). Currently only demo/scrum seed data + 1 real closed Leela WP (#38) —
effectively a clean slate. Types and statuses available are the standard set (below). Two operational
caveats that gate *creation* (not this design): the instance is only reachable from inside the WSL2 VM
(not the Windows host) and it idle-sleeps (~80s cold boot). See
`[[leela-openproject-instance-access]]`.

---

# Part A — Target OpenProject model

## A1. Project hierarchy

```
Leela & Mastery              (root project — the operator's single cockpit)
└── Leela                    (product sub-project; reuse existing project id 3 "Leela Cloud 2026", re-parented)
    ├── [Epic WPs …]         (work-package hierarchy lives INSIDE this one project — see A2)
    └── (Mastery sub-projects added in a later round — taxonomy session deferred per handover)
```

**Design choice — one project, work-package hierarchy for the rest (not a project-per-wave).**
Rationale: OpenProject enforces dependency relations and renders a single Gantt/board most cleanly
*within* one project; splitting waves into sub-projects fragments the dependency graph and, in
Community edition, cross-project aggregate views are limited. So waves and epics are modeled as
**work packages**, not projects. (Portfolio/program *project* hierarchy beyond simple parent/child is
partly Enterprise; simple parent/child projects — root → Leela — is Community-safe.)

**Open sub-choice for operator:** reuse existing project id 3 as the "Leela" sub-project (keeps its
one real WP #38) vs. create a fresh "Leela" project and leave id 3 as-is. *Recommendation: reuse id 3,
rename to "Leela", re-parent under the new root.*

## A2. Work-package type mapping

| Source concept | OpenProject type | Notes |
|---|---|---|
| apex-meta epic (`epic.md`) | **Epic** | one per epic bundle |
| apex-meta story (`00N.md`) | **User story** | child of its Epic |
| Leela wave (e.g. `wave-stats`, `wave-c`) | **Epic** | a wave = program slice ≈ epic |
| Leela packet (e.g. `wave-stats-fixture-spine`) | **Feature** | child of its wave-Epic |
| packet task / exit-criterion / deliverable | **Task** | child of its Feature |
| decomposed sub-step of a task | **Task** (nested) | child Task = "subtask" |
| wave exit / decision gate / release point | **Milestone** | zero-duration marker |
| defect noted in a plan | **Bug** | child of the relevant Feature |

Available types confirmed live: `Task, Milestone, Summary task, Feature, Epic, User story, Bug`.

## A3. Status mapping

| Source status | OpenProject status | id |
|---|---|---|
| complete / done | **Closed** | 12 |
| active / in-progress | **In progress** | 7 |
| blocked | **On hold** | 13 (+ a "blocked by" relation carrying the real edge) |
| open / not started | **New** | 1 |
| rejected / dropped / superseded | **Rejected** | 14 |
| specified-but-not-started (if a plan says so) | **Specified** | 3 |

Full workflow available: New(1) · In specification(2) · Specified(3) · Confirmed(4) · To be
scheduled(5) · Scheduled(6) · In progress(7) · Developed(8) · In testing(9) · Tested(10) · Test
failed(11) · Closed(12) · On hold(13) · Rejected(14).

## A4. Dependency / relation mapping

| Source edge | OpenProject relation | Direction |
|---|---|---|
| "blocked by X" / "depends on X" | **blocked** (blocked by) | this WP ← X |
| "blocks X" | **blocks** | this WP → X |
| temporal "after / precedes / follows" | **precedes / follows** | ordered |
| wave→packet, epic→story, task→subtask | **parent/child hierarchy** | not a relation |
| "relates to / see also" | **relates** | undirected |

Hierarchy (parent link) is used for containment; explicit relations are used only for cross-branch
dependencies (the graph edges). Every dependency claim in Part B is grounded in the originating plan
file with `path:line`.

## A5. Naming, evidence, and traceability conventions

- **WP subject** = the plan's own title, prefixed with a stable source id, e.g.
  `[wave-stats-fixture-spine] Stats fixture spine`. Keeps a hard trace back to the repo source.
- **Description** = short objective (quoted from source) + a **repository link** to the originating
  file (path), **not** a copy of the full plan prose (avoids the duplicate-truth trap; the repo file
  remains the semantic source until the retirement wave).
- **Custom field / tag** (if enabled) `source_id` = the packet manifest `id` or epic/story path — the
  join key for the eventual repo→OpenProject reconciliation.
- Completed packets are imported as **Closed** WPs so the dependency graph and history are complete,
  not just the open frontier.

---

# Part B — Plan-by-plan breakdown (newest first)

> Assembled from direct, cited reads of every source plan. Each item lists: source path, status
> (grounded), proposed OpenProject type, parent, and dependency edges. Ordering is newest-first by the
> date evidence found in each source.

## B0. Ordering basis (finding: dates are nearly absent)

- **Corpus A:** all 3 epics + 23 stories are dated `created/updated 2026-08-16` — a single day. "Newest-first" does not differentiate them; they are ordered by **dependency readiness** instead.
- **Corpus B:** only the active packet's subordinate handover and a few in-body correction notes carry dates (mostly 2026-08-15/08-18, and 2026-08-21 for the active packet); the packet manifests carry only commit SHAs, not dates. Ordering is therefore by **wave + dependency chain**, not calendar. If OpenProject start/due dates are wanted, they must be operator-supplied.

## B1. Corpus A — apex-meta Leela epics (3 Epics / 23 User stories, all `open`, all 2026-08-16)

Source: `C:\GitDev\apexai-os-meta\apex-meta\epics\`. → OpenProject: each `epic.md` = **Epic**; each `00N.md` = **User story** child; each story's implied steps = optional **Task** children (see A2). Status: all **New**, except the 7 operator-gated stories → **On hold** (blocked-on-operator).

### Epic 1 — `leela-core-interaction-development` (high) — "Home→Skill Tree→frozen resolution-context vertical slice"
Stories (id · title · status · deps → OpenProject):
- 1 Verify Home runtime vs Home screen contract — open — deps none
- 2 Verify bounded spatial Skill Tree runtime — open — deps none
- 3 Promote bounded cluster to primary Skill Tree nav — open — `depends_on [1,2]`
- 4 Make canonical ScopeSelection handoff origin-aware — open — `depends_on [3]`
- 5 Quarantine fake/legacy scope-resolution state — open — `depends_on [4]`
- 6 Reconcile ResolutionRequest/Context with Home+SkillTree contracts — open — `depends_on [4]`
- 7 Build Home request adapter into frozen resolution context — open — `depends_on [5,6]`
- 8 Validate the full vertical slice — open — `depends_on [3,4,5,6,7]`
- Each story carries explicit acceptance criteria + DoD (see source files `001.md`..`008.md`) and 5–8 implied tasks.

### Epic 2 — `leela-product-decisions` (high) — "Close Leela decisions and questions"
- 1 Reconcile stale decision-ledger vs SSOT-D records — open — deps none (**root**; 6,7,8,9 depend on it)
- 2 Prepare/close QA-02 & QA-11 resolution-profile — open — **blocked_by operator_answer_required**
- 3 Prepare/close QA-100 Home override persistence — open — **blocked_by operator_answer_required** (keep distinct from QA-131)
- 4 Close QA-138 spatial a11y fallback policy — open (med) — **blocked_by operator_answer (global policy)**; sequenced after core-interaction story 2
- 5 Close QA-73 Harmonization ownership/namespace — open (med) — **blocked_by operator_answer_required**
- 6 Evidence-sweep Sequencing/Builder cluster (QA-07,10,13,16,17,20a,21a,76) — open — `depends_on [1]`
- 7 Evidence-sweep Path/Stats cluster (QA-08,14,42,101,102,132,143) — open (med) — `depends_on [1]`
- 8 Reconcile source-integrity/stale-plan debt (QA-30,40,85,86,141,142,151,160) — open (med) — `depends_on [1]`
- 9 Create operator-facing decision batches + cadence — open (med) — `depends_on [1]`

### Epic 3 — `leela-project-management-cleanup` (med) — "Reduce PM ambiguity, move state into Apex backbone"
- 1 Inventory & classify Leela project-control artifacts — open (high) — deps none (**root**)
- 2 Publish one current authority map — open (high) — `depends_on [1]`
- 3 Retire/annotate stale Spatial-Opus/Nowa instructions — open (high) — `depends_on [1,2]`
- 4 Consolidate active Leela projects into central Apex records — open (high) — `depends_on [2]` + **blocked_by operator_approval_of_project_packets** (this OpenProject migration realizes this story)
- 5 Reconcile runtime Micro packets with Apex task identity — open (med) — `depends_on [2,4]`
- 6 Verify decluttered restart path — open (med) — `depends_on [2,3,4,5]`

## B2. Corpus B — Leela-Cloud-2026 orchestration packets (30 packets → 8 wave-Epics / 30 Features)

Source: `C:\GitDev\Leela-Cloud-2026\docs\orchestration\`. → OpenProject: each **wave** = **Epic**; each **packet** = **Feature** child; the active packet additionally gets **15 Task** children (its `PMH-*` work-units). **Modeling nuance:** most `blocked` = "authored, never activated" (single-active-packet rule retired by SSOT-D-033) → **activation-gated (On hold, needs operator go)**, distinct from **dependency-gated** (needs a prior packet's output). Tag each accordingly.

### B2a. ACTIVE (1) → In progress
- `wave-orchestration-project-management-consolidation` — "Reduce execution routing to one derived status view…and retire the duplicates." 4 stages → 15 work-units `PMH-000, 101,102,199, 201,202,203,299, 301,302,399, 401,402,403` with a full prerequisite DAG + stage gates (subordinate `HANDOVER.md:618-1151`). Acceptance: PM-ACTIVE-PACKET-001, PM-STATUS-VIEW-001, PM-RETIREMENT-001, PM-QUESTION-CLOSURE-001. Owes 3 external successors (QA-170 idea-mining, a C2 feasibility packet, design A2/A4 materialization binding). **Richest source — the flagship dependency-structure demo.**

### B2b. BLOCKED (12) → On hold
Wave C (owner Sequencing/algorithm; each additionally needs a separate activation decision):
- `C3-scientific-projection` — validation memo + policy-versioned projected XP/TP/BP. **superseded as active control by `ssot-materialization-rhythm-pilot`**; hands off to → C4.
- `C4-ranking-resolver` — ResolutionCandidate wire + ST-022 comparator. Activation is a separate reviewed decision (SSOT-D-031 landed prereqs); one sub-item **blocked_by QA-30** (filling `ScoringPolicyParameter.value`).
- `C5-fixtures-parity-exit` — freeze Wave C APIs into deterministic fixtures. **blocked_by C2,C3,C4** (prereq commits "to be recorded"); precedes external Wave D.
- `ssot-materialization-forward-opportunity-resolution` — documentation-only contract for remaining-opportunity signal + pre-rank exclusion. **Blocked on an architecture-ownership question** ("Who owns the emphasis-to-candidate match?" — RH-B02 contract widening vs. a 2nd consumer on Rhythm draft), plus a missing runtime seam. Acceptance: FWD-OPP-SIGNAL-001, FWD-OPP-EXCLUSION-001, FWD-OPP-REASONS-001.

Wave Stats (owner stats-realization; clean dependency tree, all activation-gated):
- `01 fixture-spine` (root, no in-wave dep) → `02 domain-repository` (dep 01) · `03 stat-chip` (dep 01) → `04 today-and-week` (dep 02,03) → `05 drilldown-and-flow` (dep 04; ext QA-132) · `06 evidence-quality` (dep 04; ext F-03) · `07 embedded-surfaces` (dep 03,04) · `08 drift-retirement` (dep 04). Acceptance IDs STATS-R-0xx per packet.

### B2c. COMPLETE (17) → Closed (imported for graph + history completeness)
Wave C: `C1-contract-freeze` → `C2-feasibility-timeline` (→ C3 ext). Skill-Tree: `ST-program-design` (standalone). Integration: `wave-integration-three-branch-stabilization`, `integration-merge-differential-audit-15` (both → activate `…second-iteration-home`). PATH-finalization: `path-run-2-application-ownership` → `path-run-3-snapshot-handoff` → `path-run-4-weekly-convergence`. ssot-materialization: `rhythm-pilot(01)` → `algorithm-truth-convergence(02)` → `algorithm-source-convergence(05)`; `feature-discovery-control-plane(03)` → `rhythm-alignment-run(04)` → `05`; `…second-iteration-home(06)` → `…second-iteration-rhythm(07)` → `…week-decision-gate(08)` → `…current-master-contract-recovery(09)`. **Data caveat:** packet 09's manifest `wave` is `C1-recovery` though it is filed under `ssot-materialization/` — flag on import. Three packets never pushed to origin (path-run-2, path-run-3, packet 09) — matters only if linking remote commits.

---

# Part C — Global dependency graph

**Relations to create (~50 edges), all after all WPs exist.** Format: `A --relation--> B`.

Corpus A (intra-epic `precedes/follows` from `depends_on`):
- Epic1: (1,2)→3→4→(5,6)→7; 8←(3,4,5,6,7)
- Epic2: 1→(6,7,8,9); stories 2,3,4,5 = On-hold(operator), no story edge
- Epic3: 1→2→3; 4←2; 5←(2,4); 6←(2,3,4,5)

Corpus B (packet `precedes/blocks` reconstructed from `handoff`/`prerequisiteCommits`/`remainingWork`):
- Wave C: C1→C2→C3→C4→C5 ; C3 `relates`(superseded-by) rhythm-pilot(01)
- ssot-materialization: 01→02→05 ; 03→04→05 ; three-branch-stabilization→06 ; audit-15→06 ; 06→07→08→09
- Wave Stats: 01→02 ; 01→03 ; 02→04 ; 03→04 ; 04→05 ; 04→06 ; 04→07 ; 03→07 ; 04→08

**External cross-references (notes/relations to non-WP items, NOT invented as work packages):** QA-30, QA-132, QA-170, feedback F-03, the external C2 feasibility packet, Wave D. Captured as description links to the repo, honoring "link, don't duplicate."

## C1. Proposed totals (what you would see)

| Element | Lean import (recommended) | Full import |
|---|---|---|
| Projects | 2 (root + Leela) | 2 |
| Epics | 11 (3 apex-meta + 8 waves) | 11 |
| Features | 30 (packets) | 30 |
| User stories | 23 (apex-meta) | 23 |
| Tasks | 15 (active packet work-units only) | ~146 (+ ~131 apex-meta story steps) |
| Milestones | 0–8 (optional wave-exit/decision gates) | 8 |
| Relations | ~50 dependency edges | ~50 |

Status coloring: **17 Closed** (complete packets) · **1 In progress** (active packet) · **12 On hold** (blocked packets) · **23 New/On-hold** (apex-meta stories: 16 New + 7 operator-gated On hold). Whole waves Skill-Tree, Integration, PATH-finalization are fully Closed.

**Recommendation:** import the **Lean** shape first (Epics + Features + Stories + the 15 active-packet Tasks + all ~50 relations). Explode stories/packets into finer Tasks only where you want live execution tracking — otherwise the ~146-task version is mostly noise for work that is Closed or not-yet-activated.

---

# Part D — Creation plan (gated — awaiting single operator GO)

## D0. Locked operator choices (2026-09-26)
1. **Granularity: Lean** — 11 Epics + 30 Features + 23 User stories + 15 active-packet Tasks + ~50 relations. Per-item acceptance detail goes in WP descriptions, not as separate task WPs.
2. **Project: reuse & re-parent id 3** — rename "Leela Cloud 2026" → **Leela**, move under new root **Leela & Mastery**. Keeps WP #38.
3. **Milestones yes, dates no** — ~8 milestones (wave completions + key decision gates); no start/due dates.
4. **Execution from inside WSL2** with a boot-wait wrapper; every write via skill preview → `--confirmed` → reread.

## D1. Exact ordered creation sequence (one batch, ~87 objects)
1. Create root project **Leela & Mastery**; rename+re-parent id 3 → **Leela** under it. *(2 project ops)*
2. Create **11 Epics**: 3 apex-meta (`core-interaction-development`, `product-decisions`, `project-management-cleanup`) + 8 waves (`orchestration`, `wave-c`, `skill-tree`, `integration`, `path-finalization`, `ssot-materialization`, `wave-stats`, `c1-recovery`).
3. Create **30 Features** (packets) as children of their wave-Epic, subject-prefixed with source id, description = objective quote + repo link.
4. Create **23 User stories** as children of their apex-meta Epic.
5. Create **15 Tasks** (`PMH-*`) under the active PM-consolidation Feature.
6. Create **~8 Milestones** (Wave-C exit, Wave-Stats exit, ssot-materialization convergence, integration→master, PATH complete, active-packet stage gates).
7. Set **statuses**: 17 Closed · 1 In progress · 12 On hold · apex-meta stories 16 New + 7 On-hold(operator). Tag On-hold items `activation-gated` vs `dependency-gated`.
8. Create **~50 relations** LAST (both endpoints must exist): precedes/follows for chains, blocks/blocked for hard deps, relates for supersede + external cross-ref notes.
9. **Reread** every created object; compare intended-vs-observed; any partial/unexpected = stop.

## D2. Safety
- Runs from inside the WSL2 VM (only reachable there); boot-wait wrapper for idle-sleep.
- Each mutation: preview → operator-authorized `--confirmed` → reread (skill write-policy).
- No repo files edited; no Leela SSOT/governance touched; external blockers linked, never duplicated.
- This whole batch is the structural decision the handover says the operator must approve as one plan
  before any create runs — that GO is the only remaining gate.
