---
type: specification-audit
id: M01-PRECAP-RESET-SOURCES-20261107
title: Weekly Precap source map and drift findings
description: Evidence-backed locations of the weekly planning specifications and gaps between intended layering, current runtime and conversation prototypes.
status: audit_complete_for_handover
date: 2026-11-07
scope: [source_authority, layered_overview, drift_assessment]
---

# Weekly Precap source map and drift findings

## Invariants

- [P0 | I99] The operator's current intent is a layered project → epic/workstream → task → next-work overview and guided planning of the coming week.
- [P0 | I98] A live task inventory is not an individually validated project plan; a rendered graph or timeline is not evidence of resource feasibility.
- [P0 | I97] Keep current runtime behavior, accepted operator corrections and design proposals distinguishable.

## Where the specifications are

All repository paths below are under `C:/GitDev/apexai-os-meta/`.

| Source | Role | Exact evidence |
|---|---|---|
| [Module README](../../README.md) | Purpose and user experience | Lines 9–21: iterative operator/AI conversation using confirmed reality, intent and capacity; not a status dump. |
| [PrecapWeek runtime skill](../../../../../../.claude/skills/PrecapWeek/SKILL.md) | Current production owner and procedure | Lines 11–25: weekly planning owner, input contracts and PrecapNextDay handoff. Lines 104–110: actual current procedure. |
| [Active output template](../../../../../../.claude/skills/PrecapWeek/weekly-command-brief-template.md) | Current production rendering contract | Lines 31–53: Matrix 1 project baseline, process, shortlist and longlist. Lines 55–62: separate temporal Matrix 2. |
| [Validated design decisions](../../DESIGN-DECISIONS.md) | Recorded operator decisions, subject to later corrections | Lines 20–30: adaptive conversation and one final portfolio gate. Lines 34–56: compact first layer, all active projects and actionable work at sufficient depth. |
| [Dual-view specification](../../SPEC-DUAL-VIEW-WEEKLY-PRECAP.md) | Matrix 1/2 architectural specification with unresolved inconsistencies | Lines 48–75: non-temporal per-project development, current baseline, next work, shortlist and longlist. Do not blindly adopt its fixed sequence/project/calendar examples. |
| [Project/epic hierarchy handover](../../HANDOVER-01-PROJECT-MATRIX-EPICS-CRITICAL-PATH.md) | Explicit original layered hierarchy | Lines 19–35: source hierarchy; Project → Epic → Task → selective detail. Its fixed roster, mandatory sprint decomposition and score requirements conflict with newer corrections. |
| [Assumption-first Matrix 1 design](../../HANDOVER-MATRIX-1-DESIGN-ASSUMPTION-FIRST-20261106.okf.md) | Most directly applicable project-view design process | Lines 121–128: precedence and known source discrepancies. Lines 134–152: project baseline, epic/workstream, task, typed dependencies, proposed shortlist and handoff to Matrix 2. |
| [Operator correction ledger](../OPERATOR-DECISION-DELTA-Q06-Q08-Q09-Q12-Q13-20261106.okf.md) | Later accepted semantic corrections | Lines 29–42: fact-specific authority, dynamic projects, selective hierarchy, time-block sequences, actual capacity, weekly/daily split, Saturday normal and Sunday off by default. |
| [Guided real-workflow walkthrough](../../HANDOVER-MODULE-01-GUIDED-REAL-WORKFLOW-WALKTHROUGH.md) | Existing guided review route to reuse | Lines 5–21: experience the real workflow rather than abstract architecture questions; do not start by editing production files. Its older calendar wording requires the newer corrections above. |
| [Calendar planning guidance](../../../../../../.claude/skills/PrecapWeek/calendar-planning-guidance.md) | Existing capacity/calendar integration boundary | Lines 5–30: fixed constraints, overloaded-day analysis and proposals; no calendar mutations or detailed next-day scheduling. |
| [PrecapNextDay runtime](../../../../../../.claude/skills/PrecapNextDay/SKILL.md) | Daily consumer boundary | Lines 14–30: next-day brief and execution-card outputs; no project execution or unapproved calendar writes. |
| [Original Northstar review guide](../prototypes/Matrix1-Review-Guide.md) | Presentation research, not production authority | Lines 51–69: compact project blockers, expanded epic detail and scoped graphs on demand. |
| [Conversation decisions](../NORTHSTAR-DECISIONS-AND-2DO-20261106.md) | Operator's specific display choices in this thread | Lines 25–29: Northstar direction; item name as outcome; visible state indicator; labelled mock supplements; dependency presentation still open. |

## Findings: intended layering versus delivered prototypes

| Requirement | Evidence | Assessment |
|---|---|---|
| Guided weekly planning, not a project-status dump | Module README lines 9–21; design decisions lines 20–30 | The latest artifacts present inventories, charts and proposed choices but do not conduct a grounded operator planning session. |
| Project → epic/workstream → task → useful next action | Matrix 1 handover lines 23–35; assumption-first design lines 134–152 | The latest visual overview leads with state counts and graphs; its source panel lists each project's items flat. Existing epic parents are labelled but not used as the primary drilldown. |
| Select next work from verified project reality | Assumption-first design lines 135–151 | OpenProject source facts were read, but current implementation/acceptance evidence, project targets and estimates were not validated individually. |
| Matrix 1 before temporal allocation | Dual-view spec lines 48–80; operator correction ledger lines 34–36 and 55 | The four-week illustrative Gantt and one-focus-per-day scenario are secondary experiments. They cannot replace the project/epic/task selection layer. |
| Feasible resource planning | Runtime accepted inputs lines 21–25; correction ledger line 35 | Source feed has no actual capacity/calendar intake or verified task effort. There is no resource-feasible weekly commitment. |
| Current runtime coherent with operator decisions | Runtime lines 34–44 and 105–109 versus correction ledger lines 31–37 | Baseline inconsistencies remain: Monday–Friday/Saturday exclusion; fixed project-sequence vocabulary; four-sequence examples; weekly-versus-daily depth. |

The latest source renderer is directly inspectable at [render-pages.cjs](C:/Users/gehma/Documents/Codex/2026-11-06/recently-in-the-apex-ai-os/visual-render-work/render-pages.cjs), line 10: `sourceProject` renders `ws.map(...)` at one level. The earlier [stress-test prototype](../northstar-mock/northstar-stress-test.html) does have recursive parent/child drilldown; it remains a stress fixture rather than an accepted weekly planning implementation. Preserve reusable layering there without adopting its mock planning content as fact.

## Data and implementation boundary

The [dated source snapshot](../northstar-exports-week-20261109/live-snapshot.json) records retrieval at 2026-11-07T09:14:26.576Z. The [non-sample feed](../northstar-exports-week-20261109/northstar-weekly-feed.json) retains the native projects, work packages and relations, plus separately marked proposals. The [visual plan](../northstar-exports-week-20261109/portfolio-visual-plan.json) explicitly calls its date positions illustrative assumptions.

Concrete native hierarchy already exists: Skill Tree project 10 → Epic #159, Canonical Chunk identity and Epic placement → Tasks #187 and #188. All three native states in the dated feed are New. Sequencing project 11 → Epic #215 → Tasks #216–#220 is another real example. Neither hierarchy proves which task is currently executable or what can fit next week.

No production PrecapWeek skill or template changes from this conversation were observed by `git -C C:/GitDev/apexai-os-meta diff --name-only -- .claude/skills/PrecapWeek/SKILL.md .claude/skills/PrecapWeek/weekly-command-brief-template.md`, which returned no paths. This is a working-tree observation, not a historical authorship proof. The conversation's showroom modification and research artifacts are catalogued in [INDEX.md](INDEX.md).

## Verification method

Searches used `qmd search 'PrecapWeek' -n 7`, `qmd search 'project epic task Matrix' -c apex-weekly-orchestration -n 5`, bounded `qmd get` windows, and direct line-numbered reads of the named originating files. Direct reads resolve discrepancies between indexed text and current source. Artifact existence and complete index coverage are verified separately in the handover folder.

## Failure guards

- [P0 | I99] Do not promote a runtime clause that conflicts with a later explicit operator correction.
- [P0 | I98] Do not promote a mock date, priority, relation or acceptance claim into project truth.
- [P0 | I97] Do not use a visually complete page as evidence that the weekly planning requirements are satisfied.
