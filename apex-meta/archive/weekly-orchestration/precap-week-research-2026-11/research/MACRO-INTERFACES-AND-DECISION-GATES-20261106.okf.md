---
okf_version: "0.2"
type: orchestrator-macro-interface-design
durable_id: WEEKLY-MACRO-INTERFACES-20261106
title: "Weekly orchestration macro interfaces, reuse audit, and unresolved decision gates"
description: "Repository-verified design packet for source ownership, sequence-to-flow mapping, evidence attribution, PM write routing, and bounded next decisions."
status: DESIGN_PROPOSAL_NOT_PRODUCTION_AUTHORITY
created: 2026-11-06
repository: leela-spec/apexai-os-meta
verified_main_head: 5f87d2cadb5852b2118aa8be960e8fc6ff74fc1c
source_handover: apex-meta/tools/project-improvement-orchestration-weekly/MASTER-INFORMATION-FLOW-AND-DESIGN-CRITICAL-PATH-20261106.okf.md
production_contract_mutation: false
openproject_live_verified: false
calendar_live_verified: false
operator_acceptance_of_new_design: pending
---

# Weekly Orchestration — verified macro interfaces and decision gates


## Operator acceptance delta — later on 2026-11-06 (OVERRIDES earlier recommendations below)

- **OpenProject-first:** inspect the real live WP/dependency graph before constructing any current critical-path claim or Matrix 1/2 plan. This is now the first execution gate, with a bounded read-only handover at `../../00-openproject-dependency-intake/HANDOVER-20261106.okf.md` (path relative to this file's module research directory must be resolved against improvement project root; canonical repo-relative path is `apex-meta/tools/project-improvement-orchestration-weekly/00-openproject-dependency-intake/HANDOVER-20261106.okf.md`).
- **M02=B ACCEPTED** owner-aware OP vs Apex-native status update routing; target accepted, not production implemented.
- **M05=B ACCEPTED** dedicated stateless sequencing Skill for later design; the recommendation in section 6 to start with only existing skills is superseded. Reuse-first remains a constraint on its internals.
- **M06=A ACCEPTED** Saturday Precap, normal Mon–Sat working eligibility, Sunday OFF by default; runtime patch pending.
- **M04 OPEN:** sequence is broader than flow; operator explicitly deferred exact relationship. Section 4's option B remains a discarded early recommendation, NOT an accepted mapping.
- Full accepted decisions are recorded as D014–D017 in the improvement project's `DECISIONS.md`; current next action is updated in `CURRENT-STATE.md`.


## 0. Scope and precedence

This is an implementation-independent design packet for the temporary Master improvement role, NOT a new runtime orchestrator, PM backend, Skill, approved schema, or blanket authorization for changes. Read it after D012/D013 and the explicit operator decision delta Q06/Q08/Q09/Q12/Q13 (2026-11-06). Do not reinterpret accepted Q01-Q14. Current Skill files remain runtime authority until selectively patched, reviewed, and fresh-tested. Historical wrapper architecture and W34/W45 examples are provenance/fixtures, not today's project state.

Basis: GitHub main at commit 5f87d2c; inspected live GitHub file contents of weekly-orchestrator, PrecapWeek, PrecapNextDay, its flow/card/workflow contracts, Workflow&Processes, flow-recap, candidate delta, status-merge, and leela-spec/agent-skills master OpenProject Skill and write policy. No local CLI, private OP API, or calendar access. Therefore all OP enrollment and actual WP values remain unverified.

## 1. Operator-facing operating loop (no new stage)

1. **Read current truth** — enrolled OpenProject WPs for PM commitments/status/relations; Git/repo for implementation evidence; accepted Apex decisions/Session for Apex-native control objects; actual calendar or explicit operator capacity; recent evidence/receipts. Report unavailable/freshness explicitly.
2. **PrecapWeek / G1** — Matrix 1 answers WHAT and WHY, without dates; Matrix 2 proposes WHEN and approximate allocation using real capacity, flexible sequence blocks, Monday–Saturday; Sunday OFF unless the operator explicitly chooses an exception. One approved Weekly Command Brief with embedded compact handoff.
3. **PrecapNextDay / G2** — revalidate source facts and capacity; refine selected sequence occurrences, bounded flows, sprints, prompt files and evidence instructions. A planned task is not proof of completion.
4. **Operator/external execution / G3** — do work, or mark a skipped block; capture evidence keyed to originating work reference, not merely a project label.
5. **FlowRecap / G4** — assess actual evidence per execution flow; propose zero or more candidate deltas per independently identifiable work reference; no PM write and no accepted-state claim.
6. **StatusMerge / G5** — reconcile all relevant flow candidates once per batch/day: accepted, deferred, rejected, conflicted. Group intended mutations by canonical owning system/object. Do not create a mandatory separate RecapDay stage without a proven missing consumer.
7. **Authorized mutation / readback** — route approved OP-owned WP changes through canonical OpenProject client with per-action preview, operator confirmation, current lockVersion, and post-write reread. Route only Apex-native control objects through Apex Session. Missing identity/owner, stale read, denied write, failed reread -> NO CONFIRMED mutation.
8. **Next planning refresh** — merge confirmed receipts with independent evidence and carry-forward; PrecapNextDay rereads the authoritative owner rather than treating stale candidate summaries as PM state.

The production route is currently different at steps 1, 2, 3, 5, 6 and 7; this list is the desired interface, not a claim of implementation.

## 2. Source-of-truth and provenance ownership (M01; partly operator accepted, live verification still required)

| Fact | Canonical owner when applicable | Other evidence / not the owner | If inaccessible |
|---|---|---|---|
| Enrolled project/WP ID, subject, status, priority, relations, lockVersion | verified private OpenProject instance + exact WP | Git commits, Session feed, draft plan do not overwrite it | mark OP-UNRESOLVED, never invent numeric WP ID or status |
| Source implementation, tests, produced artifact | originating Git repo at verifiable commit/path | OP completion claim does not prove code worked | mark unverified or missing evidence |
| Apex-native durable decisions/control-plane state | accepted Apex decisions/Session where confirmed | OP may have an Apex container but migration scope is not proven | preserve source-specific uncertainty |
| Operator intent, approval, override | explicit operator gate decision with artifact reference | proposal/recommendation is not acceptance | pending, no write |
| Fixed meetings and available intervals | actually connected calendar or operator-supplied schedule with timestamp | examples and blueprints are not actual meetings | calendar-unverified fallback, no fictional events |
| Executed results and obstacles | raw evidence plus normalized trace and verification | flow plan is only intent | candidate/no-state-change, low confidence |

Known project coverage from OP transition record: Leela PM declared OP-owned (actual WP read still needed); MoA hybrid/ambiguous; Investment OP accessibility not proof of migration; Apex partial/unverified; ACIM enrollment unverified. Avoid global OP claims.

## 3. Producer -> consumer minimal handoff map (P2, proposed only)

| Interface | Producer -> consumer | Minimum durable/ref data | Status boundary and named consumer |
|---|---|---|---|
| H1 Current frontier | OP/repo/Apex/calendar/operator -> PrecapWeek | owner kind, source ref, retrieved_at, status, priorities, dependencies, constraints, gaps | current fact vs unverified; planning |
| H2 Weekly command | PrecapWeek -> operator G1 -> PrecapNextDay | Matrix 1 selected work refs/outcomes and dependencies; Matrix 2 day+sequence occurrences, window/budget, known constraints; approval+handoff | proposal until G1; next-day compiler |
| H3 Daily execution | PrecapNextDay -> operator/Prompts | flow occurrence ref, sequence occurrence ref(s), sprint refs, allocated work refs and expected outputs, source/evidence directions | intent until execution; operator and recap |
| H4 Actual outcome | operator/external surface -> normalize/FlowRecap | per-work-ref result, evidence refs, skipped/partial/blocked flags, source flow/sprint | evidence vs untrusted report; recap |
| H5 Candidates | FlowRecap -> StatusMerge | 0..N candidate deltas each bound to exact work_ref, change, evidence, confidence; explicit no-change if applicable | CANDIDATE not confirmed; merge |
| H6 Reconciliation | StatusMerge -> G5 -> owner-specific writer | accepted/deferred/rejected/conflicted decisions, owner destination, expected precondition, evidence basis | proposed until approval; OpenProject or Apex Session |
| H7 Receipt | OP skill/Apex Session -> next-day read | target ref, attempted action, approval ref, pre/post version or read marker, observed result, failure reason | CONFIRMED only after reread; PrecapNextDay |

Do not persist an extra shadow PM snapshot merely to satisfy this contract. A packet should reference upstream artifacts, not duplicate entire bodies.

## 4. M04 sequence vs flow: verified incompatibility and candidate mapping

**Accepted operator semantics:** A sequence is a day-scoped time/capacity block, NOT a project lane. It may move, vary in length, include multiple projects, and contain a mixed-project sprint. Sprint mixing is permitted as a capability, not mandatory. PrecapWeek only allocates direction; PrecapNextDay owns detailed sprints.

**Active-contract conflict:**
- PrecapNextDay's flow-packet-contract defines flow_identity.project as one string, default fixed F1–F4 with project-specific lanes, flow_sprint_plan max 3.
- PrecapNextDay's operator brief and Flow Execution Card templates display one Project/project_ref per flow and fixed S1/S2/S3 headings.
- FlowRecap currently emits one candidate_project_status_delta bound to target_project (no required WP ID); status-merge is hardwired to Apex Session.
- Therefore a mixed-project sequence/sprint cannot yet pass an end-to-end, WP-attributed confirmation test. Do not claim it can.

**Provisional recommended mapping (M04-B, pending operator decision):**
- A sequence_occurrence is one schedulable time block (date + local occurrence ID + actual/proposed interval); it has zero or more sprint occurrences.
- A flow_occurrence is an independently executable/reviewable/evidence-capturable work packet with its own local ID. A sequence may contain one or several flows. For the initial compatible design, each flow occurrence belongs to one sequence occurrence; work resumed in a later block gets a new occurrence referencing the same canonical work_ref.
- A flow may involve one or more projects; **do not equate a flow to project identity**. A sprint may contain multiple work_refs, including cross-project work. Each work_ref retains its own source owner, identity, outcome and evidence.
- FlowRecap may produce zero or more per-work-ref candidates from one flow; StatusMerge aggregates by source owner and work_ref, not by flow label.
- The sequence is time allocation, the flow is execution/evidence container, and the work_ref is PM identity. No new PM state object.

**Decision M04 (L3, proposed scoring: Impact I, Effort E, Reversibility R all 1–100):**
| Option | Design | I | E | R | Assessment |
|---|---|---:|---:|---:|---|
| A | Strict 1 sequence : 1 flow | 75 | 35 | 85 | Simpler but may force unrelated work into a giant recap |
| **B** | **One sequence : 1..N flows; flow occurrence belongs to one block; multi-work-ref support** | **96** | **63** | **83** | **Recommended test candidate; preserves operator flexibility with bounded traceability** |
| C | Unrestricted many-to-many flow/sequence network | 87 | 88 | 42 | More complex cross-block continuation/recap; unnecessary until consumer proven |

Scores are design judgment, not measured implementation or operator acceptance.

## 5. M02 owner-aware recap and mutation route

**Repository fact:** weekly-orchestrator and status-merge route G5 changes ONLY through Apex Session; FlowRecap is candidate-only. The canonical OpenProject skill lives in leela-spec/agent-skills master and requires private-instance identity verification, per-action write preview, explicit --confirmed, fresh lockVersion for wp.update, and post-write reread. Current policy still treats all real-instance mutations as explicit approval. No direct API read was possible in this GitHub-only review.

**Proposed owner-aware algorithm (M02-B; NOT production behavior):**
1. StatusMerge collects candidate deltas from every relevant flow and groups by (owner_system, canonical_work_ref), never by display project label alone.
2. Invalid/missing source identity, ambiguous enrollment, or conflicting evidence -> deferred/blocked. No guessed OP WP IDs.
3. For a verified OP-owned WP: read current WP and relations; compare candidate to observed status/version; prepare exact action preview; operator explicitly confirms that specific action; execute with current lockVersion; reread; record observed receipt; partial/failed write -> stop and preserve uncertainty.
4. For Apex-native control facts only: use existing Apex Session mutation/receipt route under its gate. For repo build facts: cite the commit/test, not a PM write by implication.
5. If no mutation is supported: record no-change/deferral with evidence, not artificial progress.
6. PrecapNextDay reads fresh OP/Session owner refs and the receipts as evidence; it must not turn a draft next-planning seed into confirmed status.

**Decision M02 (L3):**
| Option | Design | I | E | R | Assessment |
|---|---|---:|---:|---:|---|
| A | Apex Session for every task, OP only as read overlay | 40 | 28 | 35 | Conflicts with enrolled OP ownership, duplicate PM risk |
| **B** | **Owner-aware OP WP or Apex-native write with receipts/reread** | **99** | **68** | **90** | **Recommended; matches Q01/Q12 intent and existing OP safety policy** |
| C | Mirror every write into both PM systems | 25 | 80 | 18 | Reject: divergent double authority |

No extra "RecapDay" is justified now: the active weekly-orchestrator stage inventory has FlowRecap + StatusMerge; GitHub code search did not find an active RecapDay source. Search non-results alone do not prove absence from all history.

## 6. M05 reuse-first sequencing capability assessment

**Actual reusable components:** Workflow&Processes classifies workflow/process stage, validates sprint structure/iteration and prompt fit, and returns operator_review_flags. PrecapNextDay composes detailed daily flows/cards/prompts. PrecapWeek already owns weekly allocation/calendar proposals. A small deterministic interval calculation can handle feasible windows and overlap. Workflow&Processes currently declares a nonexistent sprint-structure-rules.md; O002 (on-demand registry) is unresolved. Neither should be silently fixed as part of this design pass.

| Option | I | E | R | Judgment |
|---|---:|---:|---:|---|
| **A: Compose existing PrecapWeek + PrecapNextDay + Workflow&Processes and a narrow deterministic interval helper if needed** | **92** | **35** | **92** | **Recommended first**; no new runtime node |
| B: Add one stateless, on-demand sequencing Skill after a demonstrated unowned consumer | 82 | 65 | 78 | Conditional; keep backlog, do not create now |
| C: Replace orchestration spine / new stateful scheduler | 34 | 95 | 22 | Reject |

Named-consumer gate before adding a skill: show two failing mixed-project fixtures that existing owners plus a typed reference cannot solve; specify ownership, exact consumer, no duplicate stage dispatch, and a fresh-context pass.

## 7. Other cross-module decisions not yet settled

- **M06 Sunday weekly planning (L2):** Saturday close-of-week planning is a sensible proposed default (I78/E20/R95); Sunday only by explicit operator exception (I72/E15/R99); Monday-morning planning is a fallback (I65/E30/R90). Operator choice OPEN. Saturday remains normal eligible workday; Sunday OFF by default regardless.
- **M07 Q13 canonical data/render architecture (L3):** OPEN. Do not select Markdown-, HTML-, or structured-data-first source before comparing functioning variants on one accepted fixture; the already-proposed HTML examples are not production authority.
- **M08 M1 vs M2 granularity:** Q04/Q05/Q07/Q08 already accepted. M1 non-temporal selected project/epic/work/dependency and confidence; M2 actual feasible capacity/day/variable sequences with outcomes; exact sprints and prompts NextDay. No operator re-approval needed.
- **M09 acceptance:** require real read-only OP enrollment/frontier, real calendar provenance or explicit unverified fallback, multi-project fixture, flow candidate per work_ref, G5 operator approval, authorized post-write reread in a separately approved test, and a fresh-context run before production promotion.

## 8. Minimal mixed-project fixture (SYNTHETIC, not actual OP tasks)

- Week example: Monday–Saturday eligible, Sunday OFF. One Tuesday capacity window: 09:30–11:00 (90 minutes), explicitly simulated rather than claimed calendar truth.
- Sequence occurrence: 2026-11-10/SEQ-A. Sprint A work references: DEMO-MOA/INVOICE-CHECK and DEMO-INV/IMPORT-CHECK. Both source IDs are demonstration labels, NOT OpenProject WP IDs. A second segment contains review of both results.
- Desired trace: Weekly Matrix 1 selects two work_refs -> Matrix 2 proposes one mixed sequence -> NextDay creates 1..N flow occurrence(s) with per-work_ref outcome and evidence instructions -> operator returns two distinct evidence results -> FlowRecap emits separate candidate status deltas or no-change -> StatusMerge groups by each true owner -> no OP write is allowed until real enrollment/ID/approval/lockVersion/reread.
- Negative tests: source ID unresolved; stale OP version; one project skipped while other completed; conflict between repo evidence and OP status; meeting removes 30 minutes; second block resumes a partial task; Saturday available; Sunday OFF; calendar unavailable. Each must preserve task ID, never invent completion, and never create a duplicate PM store.

## 9. Critical path, decisions, and bounded handovers

| Gate | Action | Deliverable | Exit evidence |
|---|---|---|---|
| P0 | Verify current contracts, topology, source hierarchy, known contradictions | this verified audit + upstream macro handover | DONE for static repository, not live systems |
| P1 | OP ownership/freshness and per-fact owner map; read-only runtime audit | OP enrollment ledger with real refs/coverage and failure behavior | OPEN: cannot claim live verification |
| P2 | Confirm M04 recommended mapping, M02 owner-aware routing, M05 reuse, M06 weekly timing | accepted cross-stage mini-contract and mixed-project test | PROPOSED, no operator acceptance presumed |
| P3 | Bounded Matrix 1 handover | project/epic/task/dependency fixture; no clock fields | waits P1+P2 |
| P4 | Bounded Matrix 2 handover | Monday–Saturday capacity/sequence allocation with source refs | waits P1+P2 |
| P5 | Bounded downstream handovers | NextDay/FlowCard, evidence/FlowRecap, StatusMerge/OP, next-day refresh | design in parallel; implementation gated |
| P6 | Q13 comparison | same-fixture functional UX alternatives, one source model selected | only after P2 and a stable fixture |
| P7 | Exact-context patch + independent verification + authorized fresh test | staged diffs, test outcomes, operator acceptance | not started |

Suggested implementation handover order after macro approval:
- H-01: Source owner/read frontier (PrecapWeek and OP boundary).
- H-02: WorkRef + Sequence/Flow/Sprint mapping and Workflow&Processes reuse (PrecapNextDay consumer).
- H-03: Per-work-item evidence and candidate delta (FlowRecap).
- H-04: Owner-aware StatusMerge/G5/write receipts and next-day refresh (weekly router/OP/Apex Session).
- H-05: Matrix 1 and Matrix 2 output refinement, then Q13 UX selection, then fresh integrated test.

**NEXT:** Obtain operator decision on M04 sequence-to-flow mapping and M06 weekly Precap timing; do not ask to re-approve Q01-Q14. Resolve source-owner facts with read-only private OP preflight from a runtime where canonical opCall.js can reach the instance; otherwise mark it explicitly unverified. After approved macro map, issue first bounded handover. No production file, OpenProject, or calendar mutation is authorized by this document.
