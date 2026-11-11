---
okf_version: "0.2"
type: design-and-capability-handover
durable_id: M01-MATRIX1-ORCH-20261106
title: "Module 01 Matrix 1 — Project Development & Critical Path"
description: "Source-grounded handover for the non-temporal project-development view, pending operator Q&A."
status: DRAFT_PENDING_OPERATOR_DECISIONS
baseline_repo: leela-spec/apexai-os-meta
baseline_main_sha: 7e4ed05cb51532fa058d76bc26560a5a6e496b4f
created: 2026-11-06
runtime_authority: ".claude/skills/PrecapWeek/SKILL.md"
related_matrix: "ORCHESTRATOR-MATRIX-2-DESIGN-HANDOVER-20261106.okf.md"
decision_board: "ORCHESTRATOR-MODULE-01-QA-BOARD-20261106.okf.md"
production_contract_mutation: false
live_openproject_verified_in_this_session: false
---

# Matrix 1: project development and critical-path handover

## 0. Purpose and authority

**Operator question:** "For each project, where are we; what development steps, dependencies, iterations and outputs get us to the next meaningful result; what should be shortlisted now?"

The Weekly Orchestrator coordinates the conversation, routing, provenance, decisions and final acceptance. PrecapWeek remains the existing directly forked worker (D012/D013). Matrix 1 is one **section** of the single human-first Weekly Command Brief, not a new agent, task database, secondary plan or status authority. Matrix 2 is the calendar-allocation view; PrecapNextDay elaborates daily execution.

**Do not promote this draft into a competing contract.** The 2026-11-06 specification is marked approved, but conflicts with historical Module 01 decisions and the OpenProject transition remains a candidate. The operator Q&A must reconcile those facts before targeted patch-only promotion.

## 1. Source-of-truth and input inventory

| Input / exact path or interface | Owner and type | Required use / read_when | Caveat |
|---|---|---|---|
| apex-meta/handoff/weekly-precap-evolution-and-version-audit-handover-20261105.okf.md | Version lineage | First-read navigation; v1-v4.1 | History is not authority to reactivate retired contracts |
| apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/SPEC-DUAL-VIEW-WEEKLY-PRECAP.md | v4.1 approved layout specification | Dual-view boundary and OP grounding | Scoring and calendar examples contain conflicts to reconcile |
| apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-01-PROJECT-MATRIX-EPICS-CRITICAL-PATH.md | Previous Matrix 1 handover | Epic/task/subtask and critical-path expectations | 30-minute sprint decomposition is not yet reconciled with daily ownership |
| apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/DESIGN-DECISIONS.md | Earlier operator-validated design | Project visibility, approval, provenance, flow ownership | Historical visualization/scoring paragraphs conflict internally and with v4.1 |
| apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-MODULE-01-GUIDED-REAL-WORKFLOW-WALKTHROUGH.md | Reconciliation and examples | Verify known contradictions before patch | Its walkthrough is orientation, not a newer production schema |
| .claude/skills/weekly-orchestrator/SKILL.md | Active control plane | Gate/routing and fork orchestration | Current status-merge path is Apex Session-centric; OP split still candidate |
| .claude/skills/PrecapWeek/SKILL.md | Active worker | Intake, weekly synthesis, approval, outputs | Current unconditional OP claim is broader than verified enrollment |
| .claude/skills/PrecapWeek/weekly-command-brief-template.md | Active output | How Matrix 1 appears in Weekly Brief | Stale template source_gap remains; different display depth than W45 draft |
| apex-meta/handoff/weekly-orchestration-openproject-transition-2026-11-06/01-DECISION-OPENPROJECT-WEEKLY-ORCHESTRATION.okf.md | Proposed ownership policy | Work commitment vs implementation evidence | candidate_for_operator_acceptance; NOT universal PM migration |
| apex-meta/handoff/weekly-orchestration-openproject-transition-2026-11-06/02-CONFLICT-AND-DECISION-LOG.okf.md | Conflict register | C01-C15 authority splits and open migration questions | Repo evidence only; no live OP API verified |
| leela-spec/agent-skills, branch master: skills/openproject/SKILL.md; client/opCall.js; references/operations.md; references/write-policy.md | Canonical private OP API skill | root, whoami, project.list, doctor, paginated wp.list; targeted wp.get/relations | Cannot query user-local 127.0.0.1:8083 through GitHub connector |
| Per-project GitHub AGENTS.md, accepted decisions, implementation/ledger files, tests and commit SHAs | Project-specific product/build authorities | Confirm baseline, architecture, outputs and acceptance evidence after candidate selection | OP task status does not prove code is built or tested |
| apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/WEEKLY_PRECAP_DRAFT_W45.md | Historical design fixture | Illustrate epics, tasks, diagrams and provisional OP markers | NOT a live WP read, tested project baseline, verified dependency graph or approved plan |
| .claude/skills/PrecapNextDay/SKILL.md | Downstream worker | Ensure only work references and direction transfer to daily planning | Exact sprint cards, prompt files, intra-day sequence belong downstream |

**Live OP access sequence, read-only, in an authorized local runtime:** root and whoami for identity; project.list for real project IDs; doctor --project for a selected project; wp.list --project <id> with pagination; selected wp.get and relation reads. Preserve source ID, project, type, parent, status, priority, dependency, updated timestamp and retrieval time when returned. Do not guess project IDs, numeric WP IDs, statuses, dependencies or completion.

**State precedence by question, not one universal rank:**
- Commitments, WP assignment and task status: current OpenProject for projects verified enrolled there; otherwise explicit repo/Apex-native control ownership.
- Code existence, design, product behavior and build status: accepted source-repository decisions, code/ledger, tests and commit evidence.
- Operator priorities and constraints: current explicit operator decisions.
- Scheduling constraints: calendar evidence (used by Matrix 2, not Matrix 1).
- Old Session/Sync, ProjectStatus and historical W45 plans: supporting/fallback context only; never automatically overwrite live OP for enrolled tasks.

## 2. Current state (verified at remote main 7e4ed05c)

- **Implemented:** D012 direct forked PrecapWeek; human-first Weekly Command Brief; dual-view Markdown/HTML template; W45 candidate project/epic decomposition.
- **Unverified:** live OP identity and pagination; enrolled project set beyond the repo evidence; W45 task status and hardware/software claims; the proposed five-project roster; real candidate critical path; estimated durations and acceptance evidence.
- **Known contradictions:** 2026 W45 draft claims five active projects but its Matrix 1 details describe Apex OS, Leela, Master of Arts and Investment; it separately calls out "Priority Website". Current spec has four named calendar sequences. Several draft numeric WP keys and process dependencies are *provisional illustrative labels*. Historical design has both inline I/R/E and a composite formula; the active skill says numeric rating is never a mandatory gate.
- **OP coverage from Nov 6 candidate:** Leela confirmed PM in repository contract; MasterOfArts hybrid/ambiguous; Investment access listed but PM migration unverified; ApexAI-OS container exists but task migration scope unverified; acim-secular repository-local until enrolled.

## 3. Proposed target capability (pending decisions)

### Inputs and workflow

1. Identify the operator's weekly intent and full active project set; distinguish active, deliberately deferred, and unverified project coverage.
2. Resolve the owner of *each* candidate task and its identity; never treat an offline placeholder as an actual OP ID.
3. Read a bounded OP frontier for enrolled projects; use selective repo evidence to establish implementation reality and accepted design constraints; avoid full-repo ingestion by default.
4. Normalize unique work references and source/freshness labels; build project -> epic/workstream -> task/WP -> subtask; expose dependencies, blockers and cycles.
5. Distinguish **baseline state**, **next target**, **expected artifact**, **proof of completion**, **critical prerequisite**, and **decision needed**.
6. Create a shortlist of proposed weekly commitments and a longlist of staged/deferred work with reason/trigger. Mark scope as PROPOSED until the operator accepts.
7. Render a non-temporal process view: Step 1 -> Step 2 <-> iteration/review -> Step 3 -> deliverable. Critical-path labels are conditional on evidenced dependency, not decorative.
8. Pass only selected, identity-stable, readiness-qualified work references to Matrix 2, never a copied secondary task graph.

### Illustrative mini-fixture (from W45 *draft*, not confirmed production state)

- Master of Arts: invoice data schema -> invoice/PDF generation -> accounting export gate.
- Labels such as WP-MA-03 or [OP-OFFLINE: WP-MA-03] are **draft-local provisional keys**, NOT genuine OpenProject work-package IDs.
- The operator sees: baseline unverified; desired deliverable invoice export evidence; predecessor chain proposed; source: W45 draft; status: needs OP/repo validation. If an actual dependency differs, the diagram must change before it is promoted to weekly critical path.
- The same selected work is represented by a stable reference in Matrix 2, possibly scheduled on Wednesday, without embedding a clock time in Matrix 1.

### Proposed compact data contract (semantic, not a new persisted authority)

| Field | Purpose |
|---|---|
| project_key and enrollment_state | Link the project to its actual owner/source |
| work_ref + ref_kind | Canonical OP-WP#ID when proven, else explicitly local/unresolved provisional ref |
| source_ref, source_kind, observed_at, freshness | Explain provenance; current vs historical |
| current_state and confidence | Separate verified progress from intentions/draft assumptions |
| target_outcome, expected_artifact, done_evidence | What successful progress means |
| parent/epic, dependencies, blocks, iteration | Real development process topology |
| shortlist_state, deferral_reason, operator_decision | Proposed commitment without auto-approving |
| readiness and allocation_hint | Lightweight feed into Matrix 2; no date/time ownership here |

Local provisional refs must not be styled as OP numeric IDs. If there is no live read, say OP-UNRESOLVED and preserve original local source references. A disconnected service is *not* assumed unless an actual connection check failed.

## 4. Handoff to Matrix 2 and daily execution

Matrix 1 provides a **selection reference ledger**: unique project/task refs, intended outcomes, prerequisites, relative sequence/readiness, completion evidence, missing inputs and operator intent. Matrix 2 reads that ledger to assign usable capacity. No task duplication or automatic status write is implied. The Weekly Brief remains one artifact and carries one embedded presentation_handoff for PrecapNextDay.

The expected Matrix 2 consumption rule is: an item requiring predecessor WP B cannot be allocated as executable work before B is accepted as ready; an unresolved task can be displayed for operator review but not silently upgraded to a confirmed OP commitment.

## 5. Decisions awaiting operator (link to QA board)

- Q01: source authority / cross-system conflict.
- Q02: live OP failure / identity fallback.
- Q03: project set, Priority Website vs Master of Arts.
- Q04: Matrix 1 decomposition depth and iteration semantics.
- Q05: critical-path proof and shortlist/longlist promotion.
- Q06: priority ranking without synthetic numerical gates.
- Q11: shared traceability and downstream seed.
- Q12: approvals and writeback ownership.
- Q14: output evaluation and freshness.

## 6. Definition of done and independent checks

1. Real OP read has verified identity, project enrollment and pagination **or** the artifact explicitly states the unverified/offline boundary.
2. Every displayed item has source/provenance and either a valid canonical work ID or a visibly unresolved local marker.
3. The process graph is non-temporal, DAG/iteration semantics are clear, and every CRITICAL PATH claim traces to observed prerequisites rather than draft fiction.
4. A shortlist and longlist can be distinguished by an operator without jargon; deferrals retain reasons and revisit triggers.
5. No fixed roster gate, synthetic master score, wrapper agent, duplicate OP task store or direct status mutation is created.
6. Two independent reviewers: (a) architecture/ownership and no-drift audit, (b) user-story simulation against real current WP and repo evidence. Their findings must be recorded, not self-scored.
7. Operator can choose approve/edit/reduce/reject at one portfolio-level gate. Only confirmed decisions become durable.
8. Promotion to existing source files is later, narrow, exact-context patch-only, after approved Q&A and real weekly/next-day fixture tests.

## 7. Boundaries and next actions

- No production file was changed by creating this draft.
- No write to OpenProject, Google Calendar, Hermes or project status is authorized.
- Do not reactivate v1 scoring/roster or archived v2 wrapper agents.
- Do not make Matrix 1 a calendar or prompt-execution planner.
- Next: resolve Q01-Q06, source actual OP WPs and per-project repo baselines, test against real data, then promote through patch-only implementation.
