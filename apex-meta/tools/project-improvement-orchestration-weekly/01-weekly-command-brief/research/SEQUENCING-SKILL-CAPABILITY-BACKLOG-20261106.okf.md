---
okf_version: "0.2"
type: capability-design-backlog
durable_id: SEQ-SKILL-01
title: "Sequencing Capability: variable time blocks, optional multi-project sprints"
description: "Operator-requested sequencing skill TODO: definitions, reuse audit, I/O contracts, acceptance tests and design questions."
created: 2026-11-06
status: TODO_NOT_IMPLEMENTED
priority: high
depends_on: ["OPERATOR-DECISION-DELTA-Q06-Q08-Q09-Q12-Q13-20261106.okf.md"]
not_authorized_to_modify_production: true
---

# SEQ-SKILL-01 — Sequencing skill/capability: design backlog

## Mandate

The operator explicitly requested: **record creation of a sequencing skill as a to-do**. Do not mistake that for authorization to implement or dispatch it now. Skill design begins from the existing D012 direct forked-skill architecture, never legacy wrapper agents.

**Job:** Given selected work from Matrix 1, available time and constraints for the day/week, produce **flexible sequences (execution blocks)** containing sprints and project work, potentially **multiple projects in a single sequence or even single sprint**, without changing actual project/WP state. It should be reusable by PrecapWeek (directional) and PrecapNextDay (detailed), or a thin shared dependency if reuse of existing Workflow&Processes suffices.

## Operator-confirmed definitions

- **Sequence** = one time/capacity block/container; not a project, project identity, permanent order or fixed morning slot.
- Sequence timing, duration and project membership may vary by day.
- Sequence can contain tasks from several projects.
- Sprint is a smaller segment inside a sequence and **may** contain multiple projects; exact mixing strategy is **open**.
- Project/task identity comes from Matrix 1, not the sequence label.
- PrecapWeek gives directional weekly allocation; PrecapNextDay produces actual sprint details, flow cards and prompt files.
- Saturday is a normal planning/workday; Sunday is off by default, except explicit operator decisions.
- This task does not create a new state authority, PM database, agent-wrapper or automatic calendar writer.

## Candidate vocabulary and minimal typed fields (not approved schema)

| Concept | Minimum identity/reference | Ownership and content |
|---|---|---|
| Project | project_source_ref / repo or verified OP project ID | Real work domain; identity persists across days |
| Matrix 1 work item | source_kind + source_work_ref + readiness + dependency | Selected target/acceptance evidence; NOT invented OP ID |
| Sequence occurrence | day + sequence_id + optional calendar interval | Schedulable time block; may cover many projects |
| Sprint occurrence | sequence_id + ordinal + duration + goal | A smaller outcome slice; may cite multiple work_refs |
| Work allocation | work_ref + sprint_ref + intended_result | Relation linking one real task to one or more time segments |
| Flow | existing PrecapNextDay/FlowRecap execution artifact ID | Relation to sequence remains to be determined |
| Review outcome | per-work-ref evidence refs and candidate changes | Routed through existing FlowRecap/StatusMerge, not rewritten directly |

Sequence IDs must be stable enough to trace a plan occurrence but not masquerade as canonical OpenProject IDs. Avoid making "Seq 1" globally refer to a project. Capacity is computed from actual intervals; 2 hours/30 minutes are sample defaults until decided.

## Concrete user stories

1. **Single-project block:** On Monday a 90-minute free period is used for Master of Arts invoicing. The skill proposes one sequence, 2–3 sprints, and no unnecessary cross-project switching.
2. **Mixed sequence:** On Tuesday a two-hour block contains Investment ingestion checks and a short Apex OS unblocker. Both tasks retain independent WP/source refs and can produce separate recap evidence.
3. **Mixed sprint (open decision):** A 30-minute administrative sprint covers one quick invoice confirmation and one Leela skill-tree status update. The operator sees the cost of context switching and can group/reject the mix.
4. **Meeting cancellation:** A Wednesday 11:30 meeting disappears; sequence start/end shift with unchanged Matrix 1 task identity. PrecapNextDay recomputes exact sprints and asks before any calendar write.
5. **Dependency:** Apex OS UI cannot be claimed ready before its prerequisite driver event hook. Unready work is marked blocked/deferred instead of being assigned as executable.
6. **Saturday normal, Sunday off:** Saturday permits ordinary sequences if actual capacity permits; Sunday remains unscheduled unless operator explicitly chooses an exception.
7. **FlowRecap / status writeback:** After a mixed sequence, each project's evidence maps back to the right OP WP or Apex-native record; the existing FlowRecap and StatusMerge stages are reused, no multi-project PM updates by inference.

## Existing capabilities to inspect before building

| Source | Reusable parts | Critical gap |
|---|---|---|
| .claude/skills/Workflow&Processes/SKILL.md | Validates workflow/sprint/iteration/process fit, produces sprint_structure_review | Does not own final daily planning or week calendar allocation; one declared sprint-structure-rules reference is known missing |
| .claude/skills/PrecapNextDay/SKILL.md | Daily flow selection, sprint detail, cards/prompts, calendar-write requests | Existing FlowCard and brief templates use singular Project and fixed flows, not a proven multi-project sprint model |
| .claude/skills/PrecapNextDay/templates/flow-execution-card-template.md | Flow-sprint workspace and evidence handoff | Project field singular; multi-project outcomes/evidence require design |
| .claude/skills/PrecapWeek/weekly-blueprint-standard.md | Time anchors, compressed/omitted flows and scheduling grammar | Mon-Fri and default project ordering are stale vs operator decisions |
| .claude/skills/PrecapWeek/weekly-command-brief-template.md | Four project-name rows, durable handoff | Treats Seq N as project rather than a time-block occurrence |
| .claude/skills/flow-recap/SKILL.md | Per-flow evidence and candidate status deltas | Need verify candidate deltas can represent several projects/WPs within one execution container |
| .claude/skills/status-merge/SKILL.md | Consolidated evidence and next-planning seed | Current approved-mutation target is Apex Session; OpenProject routing needs reconciliation |
| .claude/skills/weekly-orchestrator/SKILL.md | Direct forked skill dispatch, stages, G1-G5 | Sequence capability should be an on-demand helper, not an extra top-level wrapper |
| apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/SPEC-DUAL-VIEW-WEEKLY-PRECAP.md | Proposed 2h/30m geometry and styled calendar | "Sequence 1 = MoA" and fixed 3-item sprint constraints contradict new operator-approved semantics |
| apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/WEEKLY_PRECAP_DRAFT_W45.html | Prototype for timed daily blocks | Draft labels sequence blocks by changing project; its sample hour total is inconsistent |

## Candidate ownership designs (to compare; not yet selected)

**A. Extend PrecapNextDay + reuse Workflow&Processes validator.** No new independent Skill; keep sequence composition as small reusable reference/algorithm. Fewer owners but operator explicitly requested a dedicated sequencing capability — compare before choosing.

**B. Dedicated thin sequencing Skill (preferred test candidate, not accepted).** One stateless Skill reads Matrix 1 refs plus calendar constraints, emits validated sequence allocations and dependency-aware proposed sprint groupings. It is invoked by PrecapWeek for week-level direction and by PrecapNextDay for daily detail with mode-specific depth. It never owns durable status, creates time events or substitutes for flow recap. Direct fork context must be demonstrated rather than assumed.

**C. Deterministic slot planner script plus existing skills.** Read-only scheduling calculator handles intervals/conflicts; PrecapNextDay and Workflow&Processes provide semantic grouping. Effective if calendar arithmetic dominates and a new AI skill would add little unique reasoning.

The reuse-first audit must compare A/B/C on actual complexity and capability before a new skill is created.

## Decisions to resolve before skill implementation

- **SEQ-Q1 (L3):** Relationship between sequence and flow: 1:1, many-to-one, or orthogonal? Requires existing FlowCard and Recap compatibility audit.
- **SEQ-Q2 (L3):** Mixed sprint default: freely mix projects, exception with cost/benefit, or split by default? User explicitly left this open.
- **SEQ-Q3 (L2):** Standard count: four daily blocks as heuristic, or computed flexibly from capacity?
- **SEQ-Q4 (L2):** Duration: 2h sequence and 30m sprint as soft defaults, variable by source window and cognitive task.
- **SEQ-Q5 (L3):** How to preserve per-WP evidence and status updates when a single flow touches multiple projects?
- **SEQ-Q6 (L3):** Can a weekly view show block/sprint composition without taking over NextDay detail? Test with one Sunday weekly handoff and one changing day.
- **SEQ-Q7 (L2):** Skill vs existing skill extension vs deterministic script, with compare on actual user stories, simplicity, maintenance and correctness.
- **SEQ-Q8 (L2):** Conflict/replanning rule: meetings, unexpected task completion, variable energy/capacity and urgent operator overrides.
- **SEQ-Q9 (L2):** Visible representation of multiple projects within one sprint for Q13 prototype comparison.

## Proposed inputs, outputs, connectors (clarify for build)

**Inputs:** selected Matrix 1 work refs/outcomes and dependencies; available interval windows with source/freshness; operator priority/energy/time constraints; existing day plans/recap carry-forward. Source IDs never fabricated.

**Outputs:** a proposed per-day sequence/block ledger with IDs/time/capacity, sprint outlines, project membership, work refs, dependency/readiness flags and reasons for mixing/deferral; diagnostic flags; a *reference* payload for NextDay. Weekly mode emits high-level direction; daily mode may emit deeper plans only by explicit downstream responsibility. No new durable PM schema.

**Connectors:** canonical OpenProject read-only client for selected identities when verified and accessible; an actually connected calendar read interface or user-provided constraints. **No connection assumed**; writes remain separately gated.

## Acceptance tests

1. Single-project and mixed-project sequence renders with unchanged source work IDs.
2. Optional multi-project sprint maps each item and result to its originating project and actual WP; no lost evidence.
3. Time interval arithmetic has no overlap and does not assume false four-by-2h capacity.
4. Schedules six normal days Mon-Sat if capacity and intent warrant it; Sunday is default-off.
5. A surprise meeting or WP status change can replan without rewriting Matrix 1 project truth.
6. PrecapNextDay produces detailed sprints/cards/prompts without duplicating the weekly brief; FlowRecap creates separate candidate deltas as needed; StatusMerge routes by owning PM.
7. Prove no wrapper agents, no synthetic numeric priorities/IDs, no automatic writes, no persistent redundant state store.
8. Validate with a real-week / next-day test and independent source+usability review before promoting.

## Next action

Conduct an operator-facing concrete walkthrough of two mixed-project cases, resolve SEQ-Q1 and SEQ-Q2 first, inspect existing templates and contracts, then decide whether to build the dedicated skill or satisfy the capability by reusing current components. No Skill files or scripts have been created by this backlog record.
