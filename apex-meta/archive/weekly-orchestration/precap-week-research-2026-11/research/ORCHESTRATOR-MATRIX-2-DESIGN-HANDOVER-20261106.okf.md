---
okf_version: "0.2"
type: design-and-capability-handover
durable_id: M01-MATRIX2-ORCH-20261106
title: "Module 01 Matrix 2 — Responsive Weekly Calendar & Sequence Allocation"
description: "Source-grounded temporal handover; proposed decisions and acceptance tests, not a live calendar schedule."
status: DRAFT_PENDING_OPERATOR_DECISIONS
baseline_repo: leela-spec/apexai-os-meta
baseline_main_sha: 7e4ed05cb51532fa058d76bc26560a5a6e496b4f
created: 2026-11-06
runtime_authority: ".claude/skills/PrecapWeek/SKILL.md"
related_matrix: "ORCHESTRATOR-MATRIX-1-DESIGN-HANDOVER-20261106.okf.md"
decision_board: "ORCHESTRATOR-MODULE-01-QA-BOARD-20261106.okf.md"
production_contract_mutation: false
live_calendar_verified_in_this_session: false
live_openproject_verified_in_this_session: false
---

# Matrix 2: weekly calendar and sequence-allocation handover

## 0. Purpose and responsibility

**Operator question:** "Given the project development map and actual available time, which outcomes should advance on which days, what is blocked or deferred, and what should tomorrow's planning worker take forward?"

Matrix 2 is the **temporal allocation view of the same selected work** as Matrix 1. It does not own project status or invent work packages. Weekly Orchestrator holds governance; PrecapWeek (directly dispatched with context: fork, D012/D013) owns weekly direction; PrecapNextDay owns detailed daily flow cards, prompts, sprint preparation, exact intra-day order and gated calendar writes.

This document is a draft capability/decision handover. It is *not* a replacement for the live PrecapWeek skill, the approved v4.1 specification or a binding Google Calendar permission.

## 1. Source manifest and ownership

| Source / exact path | Role / read_when | Authority boundary |
|---|---|---|
| apex-meta/handoff/weekly-precap-evolution-and-version-audit-handover-20261105.okf.md | Verify v4 baseline and November 2026 v4.1 design | Historical lineage does not create new calendar write rights |
| apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/SPEC-DUAL-VIEW-WEEKLY-PRECAP.md | Current approved dual-view layout, named Seq 1-4 and responsive HTML pattern | Conflicts with older Mon-Fri scope and operator daily ownership; reconcile |
| apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-02-TIMELINE-CALENDAR-SEQUENCE-SPRINT-VIEW.md | Proposed 2h sequence, 30m sprint and three-item cell geometry | Includes unrealistic 2h claim for a 1h sequence; process examples not verified calendar |
| apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/DESIGN-DECISIONS.md | Earlier validated week/day ownership and single approval | Sprint/detail rules conflict with later visualization paragraphs |
| apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-MODULE-01-GUIDED-REAL-WORKFLOW-WALKTHROUGH.md | Explains weekly-vs-daily conflict with examples | Reconcile, do not resurrect a duplicated Daily Seed Map |
| apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/research/ORCHESTRATOR-MATRIX-1-DESIGN-HANDOVER-20261106.okf.md | Non-temporal project selected-work ledger | No calendar details are authored in Matrix 1 |
| .claude/skills/PrecapWeek/SKILL.md | Active weekly worker contract | Calendar read allowed; event creation excluded; operator validation required |
| .claude/skills/PrecapWeek/weekly-command-brief-template.md | Live 4-sequence table and embedded YAML handoff | Its rows encode per-project sequences, not 4 clock windows |
| .claude/skills/PrecapWeek/weekly-blueprint-standard.md | Default anchors/capacity and constrained-week patterns | Historical default project ordering should not override live priorities |
| .claude/skills/PrecapWeek/weekly-blueprint-meeting-example.md | How meetings compress/omit planned blocks | Example, not a user's real current calendar |
| .claude/skills/PrecapWeek/calendar-planning-guidance.md | Fixed constraints, source status, optional proposed blocks | Declares no creation/edit/deletion of calendar events in PrecapWeek |
| .claude/skills/PrecapWeek/references/validation-checklist.md | Scope, safety and completeness checks | Says Saturday excluded; conflicts with v4.1 Monday-Saturday column |
| .claude/skills/PrecapNextDay/SKILL.md | Downstream daily operationalization | Flow Execution Cards and real prompts, approved calendar-write requests only |
| .claude/skills/weekly-orchestrator/SKILL.md | Main-session orchestration and G1-G5 runtime gates | PrecapWeek remains direct forked Skill; not a separate agent or planner |
| apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/WEEKLY_PRECAP_DRAFT_W45.md | Real committed **design fixture** | Not a live approved schedule, actual meeting read, or verified task status |
| apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/WEEKLY_PRECAP_DRAFT_W45.html | Standalone static HTML draft | Scrollable styled HTML; no JavaScript controls or live connector |
| apex-meta/handoff/weekly-orchestration-openproject-transition-2026-11-06/01-DECISION-OPENPROJECT-WEEKLY-ORCHESTRATION.okf.md | Candidate authority/freshness split | Live OP WPs unverified; no automatic writes |
| Actual calendar read, operator-supplied constraints, and freshness metadata | Fixed meetings, unavailable windows, buffers, capacity | Not connected/queried in this session; W45 meeting labels are draft examples |

## 2. State and mismatch register at the audited baseline

1. **Correct named-sequence mapping in spec/template:** Seq 1 = Master of Arts (priority website and invoices); Seq 2 = Investment (pipeline, ingestion, dashboard); Seq 3 = Apex OS (OpenMouse); Seq 4 = Leela (skill tree).
2. **W45 HTML and Markdown draft repurpose "Seq 1-4" as time windows.** E.g. the 09:00-11:00 Seq 1 cell works on Apex OS Monday; 11:30-12:30 Seq 2 works on Leela Monday. This changes the meaning of sequence labels and defeats 1:1 mapping. It is an observed contract conflict, not an accepted priority change.
3. **Capacity arithmetic is not reconciled.** The W45 draft labels 38 net Mon-Fri focus hours but visible windows are 09:00-11:00 (2h) + 11:30-12:30 (1h) + 13:30-15:30 (2h) + 15:45-17:45 (2h) = 7h/day, or 35h across five unconstrained days. The Tuesday 11:00-11:30 meeting shown in the fixture occupies the preceding transition window; it cannot justify a 38h number. Calendar source and additional meetings remain unverified.
4. **Fixed duration claim is inconsistent.** One published example says four daily 2-hour sequences, while its second window is only 1 hour. A requested schedule cannot be declared feasible without actual time geometry.
5. **Sprint-depth leakage.** W45 full-week draft contains 30-minute sprint microtasks with three checklist items per sprint; existing Module 01 ownership states PrecapNextDay writes executable sprint and Flow Card detail.
6. **Saturday scope conflict.** v4 PrecapWeek contract and validation file exclude Saturday normal planning; v4.1 spec and W45 drafts show a Saturday review/buffer column. Whether that is a non-execution review annotation or a new planning day is not yet operator-reconciled.
7. **HTML "interactive" claim is overstated.** The W45 .html is a styled standalone table with CSS overflow; no client-side interactive controls or calendar integration were observed.
8. **Downstream handoff depth conflicts.** The live template has a compact presentation_handoff. W45 draft embeds a full monday_hourly_schedule within the same YAML; historical operator decision prefers reference + minimal next-day orientation.
9. **Status and freshness unknown.** OpenProject 127.0.0.1:8083 and the operator's real calendar were not queried in this chat. W45 [OP-OFFLINE] markers and the Tuesday "Stakeholder Sync" are examples from the committed draft, not new probe results.
10. **Current week example:** ISO 2026-W45 is Nov 2-8, 2026. Treat W45 as an existing design fixture for the audit, not a new upcoming week's real schedule.

## 3. Proposed capability and transformation pipeline

### Inputs (never duplicate ownership)

- Matrix 1: identity-stable selected work references with readiness, dependency/critical-path and expected completion evidence.
- Calendar: read-only actual availability and existing meetings; source, time zone, retrieval time and gaps clearly labeled.
- Operator: weekly intent, protected blocks, order preferences, non-movable commitments, approximate capacity.
- Blueprint: rhythm and recovery/anchor grammar. A historical project ordering is not priority authority.
- Last cycle: reconciled carry-forward and urgent change signals, selectively retrieved.
- OpenProject: actual WPs only when live and verified; otherwise unresolved references and explicit degraded state.

### Proposed algorithm, pending decisions

1. Freeze exact week_id, timezone and calendar source status. Read projects/selected items from Matrix 1 by reference; do not recreate the shortlist.
2. Reserve real fixed meetings, approved protected routine anchors, transitions, travel, recovery and necessary buffers.
3. Compute **available** minutes from free intervals. Distinguish capacity assumption, measured free time, and allocated deep-work time. Do not label estimates as observed.
4. Resolve whether Seq 1-4 are **project identities** or time windows. Proposed default: Seq labels remain the four named project streams; daily clock positions are separate "blocks" with their own time IDs. A day may contain no block for a particular project.
5. Place dependency-ready outcomes into feasible days/blocks honoring fixed deadlines, operator constraints and direction. Mark missing evidence, blocked and deferred items honestly.
6. For the weekly view, produce planned day-level movement and capacity class (STANDARD/REDUCED/CRITICAL). Propose optional time windows; never imply Google Calendar events were written.
7. Use 30-minute sprint units as a **daily execution capability**, not a requirement to fabricate 3-item lists in every weekly cell. The exact depth is an operator decision Q08.
8. Render responsive HTML as a readable view with fallback usable Markdown; preserve all source refs and the same work IDs in both without forking planning truth.
9. Produce one embedded presentation_handoff YAML containing a reference to the Weekly Brief/Matrix 1+2, review status, next target day, intended outcomes, fixed constraints, carry-forward dependencies and next_consumer. PrecapNextDay revalidates daily state and expands sprint cards/prompts.
10. Present the complete Weekly Command Brief for one portfolio-level operator decision, then record gate status; no silent calendar or OP mutations.

### Traceability example — W45 fixture, never promoted as live truth

Matrix 1 proposed work: Master of Arts invoice schema -> PDF template -> export gate, with a provisional source key [OP-OFFLINE: WP-MA-03] in W45 draft. If verified, Matrix 2 would show "Seq 1 / Wed: invoice schema gate" with the same resolved WP ref and a capacity source. If OP is not verified, it must show "source: W45 draft; OP-UNRESOLVED" and require review. PrecapNextDay would decide the exact 30-minute checks and prompt files on Wednesday after rechecking the calendar.

## 4. Proposed display contract (not implementation)

- Matrix 2 is full-width responsive, horizontally scrollable on narrow screens, with readable weekday labels and project sequence legends. Horizontal scrolling is presentation only and not evidence of live interaction.
- Project stream identity (Seq 1-4), time block ID, day, duration, selected task ref, intended outcome, prerequisites, capacity class, source and provisional state are distinct fields.
- Mark meeting load, source freshness, buffer/review/deferral and over-commitments explicitly.
- A schedule must survive a meeting cancellation or OP status change by replanning without mutating the non-temporal Matrix 1 graph.
- Standard week: Monday-Friday work direction; Saturday handling is provisional pending Q09.
- Prompts, Flow Execution Cards and exact intra-day sprint sequences are downstream.
- Keep per-fact source tags for consequential calendar and task claims; uncertainty is an operator review flag, not a made-up time or ID.
- No all-four-sequences-every-day obligation if the operator/capacity/dependencies do not support it.

## 5. Calendar and OpenProject safety boundary

**Read-only OP preflight (authorized local runner):** root, whoami, project.list, doctor, paginated wp.list, selected wp.get/relations. Never present guessed numeric IDs. An OP connection failure is distinct from zero work packages, and a stale snapshot is not current state.

**Calendar:** PrecapWeek may read real meetings if integration is available; may make proposals; cannot create/edit/delete actual meetings or claim it did. PrecapNextDay may prepare gated write requests only. Never modify external meetings. If calendar is unavailable, display UNSOURCED CAPACITY assumption and avoid false free-hour precision.

**Operator authority:** One final week review gate for the proposed plan. Separate confirmation for every consequential OP write, using current lockVersion and post-write reread; no status mirroring into Apex task files. This OpenProject write routing is still an unpromoted transition candidate pending operator approval/live trial.

## 6. Open decisions

- Q03: full portfolio project/sequence coverage and Priority Website mapping.
- Q06: Seq 1-4 as named projects versus time-window labels.
- Q07: calendar evidence, time geometry, calculation and meeting collision.
- Q08: weekly vs daily granularity; exact 30m sprints and 3-item lists.
- Q09: Saturday review/buffer vs actual execution planning.
- Q10: weekly vs daily calendar-write boundary.
- Q11: one embedded YAML handoff and minimum fields.
- Q13: Markdown/HTML rendering authority and actual interactivity.
- Q14: verified end-to-end tests and acceptance.

## 7. Acceptance tests and independent review

1. Compare W45 .md and .html against production template: Seq mapping must match operator choice; no missed active projects or hidden deferred items.
2. Recompute every visible day's minutes from intervals. Detect 2h/1h window mismatch and any 38h-vs-35h discrepancy. Do not accept an arithmetic assertion without interval evidence.
3. Test one meeting-heavy day, one unexpectedly cancelled meeting, one unmet dependency and one unavailable-calendar case. Show revised allocations and audit sources.
4. All work-cell refs resolve to Matrix 1 or carry an explicit OP-UNRESOLVED source marker. No fake numeric IDs, speculative deadlines or forged live calendar items.
5. Prove PrecapNextDay can consume the embedded handoff and produce one day’s Flow Cards/prompts without a duplicated seed packet.
6. Validate HTML closures, responsive overflow, plain Markdown readability and accessibility before asserting display PASS. Keep MD and HTML as projections of the same source, not two divergent schedules.
7. Two independent reviews: source/authority/freshness correctness; operator-user-story usability and calendar constraint feasibility. No self-awarded pass for file creation alone.
8. Make one actual future-week and next-day dry run with sourced OP/calendar data before promotion. Only then apply exact-context patches to production contracts under the existing patch-only policy.

## 8. Current next step

Collect operator decisions through the Q&A board; reconcile contradictions with the existing Matrix 1 handover and live template; retrieve actual OP/calendar evidence in a compatible local runtime. No production mutation and no actual calendar write are authorized by this design artifact.
