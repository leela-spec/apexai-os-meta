---
type: execution-handover
id: M01-PRECAP-RESET-HANDOVER-20261107
title: Weekly Precap — restore the layered planning workflow
description: Review packet for the next agent/session, including source authority, artifact access, drift findings and a bounded route into individual project planning and weekly resource planning.
status: ready_for_operator_walkthrough
date: 2026-11-07
scope: [spec_review, layered_overview, project_readiness, resource_planning_design]
---

# Weekly Precap — restore the layered planning workflow

## Invariants

- [P0 | I99] The primary experience is a guided project → epic/workstream → task → next-work overview for planning the coming week.
- [P0 | I98] Resource allocation follows validated project readiness and operator intent; a chart must not manufacture either.
- [P0 | I97] Preserve actual OpenProject identities, ownership, status and relation semantics; verify implementation truth in the originating project evidence.
- [P0 | I96] This packet authorizes review and design continuation, not production rewrites, project mutations, calendar writes or project execution.

## 1. Input and priority ledger

### Latest operator direction

The operator reports drift: the expected layered overview should show different projects, their epics, their tasks and what should be done next. The operator requested the specification locations, a handover, a README and an index linking all files created in this conversation. The operator also wants a future individual-project planning step that provides correct inputs to a resource-aware, guided weekly planning experience. The operator confirmed this handover scope with “go”.

Record the future project/resource planning idea as an intended direction with unresolved details, not an implemented feature or a fully approved design.

### Source priority and reading route

1. Read [SOURCE-FINDINGS.md](SOURCE-FINDINGS.md) for the precise source map and line references.
2. Read the [module purpose](../../README.md), [validated decisions](../../DESIGN-DECISIONS.md), and [later operator correction ledger](../OPERATOR-DECISION-DELTA-Q06-Q08-Q09-Q12-Q13-20261106.okf.md).
3. Read the [explicit Matrix 1 process](../../HANDOVER-MATRIX-1-DESIGN-ASSUMPTION-FIRST-20261106.okf.md), particularly lines 130–168.
4. Inspect the [current runtime](../../../../../../.claude/skills/PrecapWeek/SKILL.md) and [active template](../../../../../../.claude/skills/PrecapWeek/weekly-command-brief-template.md) to distinguish implemented behavior from the accepted target.
5. Reuse the [guided workflow walkthrough](../../HANDOVER-MODULE-01-GUIDED-REAL-WORKFLOW-WALKTHROUGH.md) as a facilitation route, applying the later calendar/sequence corrections rather than repeating stale examples.
6. Use the [artifact index](INDEX.md) only for the specific evidence or presentation example needed. Do not bulk-ingest every generated file.

Current explicit operator corrections outrank older examples on the same issue. OpenProject owns enrolled PM facts; accepted repository decisions, current code and test evidence own implementation proof. Mock additions own neither.

### Conversation decisions to preserve

- Northstar is the preferred visual direction; a calm progressive drilldown is reusable.
- The item name represents its outcome; do not require an extra duplicate Outcome heading.
- Current state should have a visible indicator with an accessible exact status label.
- Real data is preferred; any necessary mock supplement remains explicitly local and labelled.
- Layered dropdown/bullet dependency presentation versus the Northstar treatment remains a comparison to perform, not a settled choice.
- Graphs, timelines and Gantts were requested as examples, but they do not replace the newly reiterated layered weekly planning requirement.

These display decisions are recorded in [the Northstar decision note](../NORTHSTAR-DECISIONS-AND-2DO-20261106.md). Its information ranking is a proposal, not a frozen specification.

## 2. Observation, reasoning and conclusion

### Observations

The [module README](../../README.md), lines 9–21, calls weekly planning an iterative operator/AI conversation using project reality, intent and capacity. The [design decisions](../../DESIGN-DECISIONS.md), lines 34–56, require a compact first layer with meaningful project detail. The [Matrix 1 process](../../HANDOVER-MATRIX-1-DESIGN-ASSUMPTION-FIRST-20261106.okf.md), lines 134–152, explicitly builds project → epic/workstream → task, then selects proposed next work before allocating dates.

The latest [visual dashboard](../northstar-exports-week-20261109/northstar-portfolio-visual.html) leads with state counts, example date windows and a diagram atlas. Its final source panel lists work packages flat within each project. [The local renderer](C:/Users/gehma/Documents/Codex/2026-11-06/recently-in-the-apex-ai-os/visual-render-work/render-pages.cjs), line 10, uses `ws.map(...)` rather than recursive epic/task drilldown. The earlier [stress-test page](../northstar-mock/northstar-stress-test.html) does preserve recursive parent/child expansion, but it is still a mock/stress fixture rather than an accepted weekly run.

The [source snapshot](../northstar-exports-week-20261109/live-snapshot.json) is dated 2026-11-07T09:14:26.576Z. The [non-sample feed](../northstar-exports-week-20261109/northstar-weekly-feed.json) contains real PM fields plus separately labelled proposals. Current repository implementation, per-project accepted targets, effort, actual calendar capacity and owner availability were not validated by those export/visualization tasks. The [visual schedule](../northstar-exports-week-20261109/portfolio-visual-plan.json) labels its dates as assumptions.

### Reasoning chain

1. Weekly planning needs a source-grounded explanation of each project's next meaningful movement.
2. A task inventory provides identity and PM state, but does not establish project intent, acceptance, readiness, effort or resource feasibility.
3. Graph and date rendering improves visibility only after those meanings are understood.
4. The generated views do not establish a verified individual-project plan or the intended guided weekly conversation.
5. Therefore the next step is to recover the layered workflow and its per-project inputs, not to add another visualization layer or more hypothetical dates.

### Conclusion

The operator's drift concern is supported. Preserve useful visual and source work, but treat it as reference material. The central deliverable still needs to be a guided, layered Weekly Command Brief using validated project inputs and real weekly constraints.

### Caveats and baseline issues

The production runtime and template still contain clauses inconsistent with recorded corrections: Monday–Friday/Saturday exclusions, project/sequence conflation, fixed sequence examples, and overly deep weekly sprint detail. These are baseline specification issues, not proof that the conversation modified production. `git diff --name-only` against the runtime and active template returned no paths during this audit. No production fix was made here.

Prototype render helpers can lag later exact-match refinements in the output HTML/SVG/PDF. Treat helpers as diagnostic implementation references, not authoritative generators to rerun blindly. Machine/file existence and layout checks show artifacts render; they do not establish operator usefulness or requirement compliance.

## 3. Intended layered overview

Begin with a compact list of relevant projects. Expanding a project shows its goal/baseline and meaningful epics or workstreams. Expanding an epic shows task names, state indicators, readiness, prerequisites and the proposed next work. Expand subtasks, evidence or diagrams only when they help the next decision. Keep inactive/deferred projects visible with a reason.

An existing native example, not a new mock hierarchy:

```text
Project: Skill Tree — project 10
  Epic #159: Canonical Chunk identity and Epic placement — New
    Task #187: [materialization] STF-22 — materialize canonical Chunk Library identity — New
    Task #188: [materialization] STF-23 — define durable Epic placement identity — New
    Next-work decision: verify current evidence and the unresolved placement choices;
                        do not infer implementation order from ownership alone.
```

The source feed verifies the native Epic/Task types and parent links. It does not verify that either task is ready or determine which should be selected. If a project lacks a useful native epic, distinguish a proposed presentation grouping from a real work package; do not silently create or move records.

Matrix 1 owns this non-temporal project/selection view. Matrix 2 consumes selected references and reconciles them with the coming week's actual capacity. PrecapNextDay owns precise daily execution detail. Preserve one Weekly Command Brief and its compact downstream handoff, not a duplicated machine seed.

## 4. Next phase: individual project planning feeding weekly resource planning

### Intended flow

```text
Individual project review with the operator
  → confirmed goal, baseline and epic/task readiness
  → project-level next-work candidates and evidence gaps
  → weekly intent and cross-project choices
  → actual calendar/resource constraints and bounded estimates
  → proposed weekly allocation, deferrals and contingencies
  → one operator-reviewed Weekly Command Brief
  → compact reference-based handoff to PrecapNextDay
```

This is a proposed integration direction, not a new data schema or a new skill. First inspect the existing project-context producers referenced by PrecapWeek's accepted inputs, plus [calendar guidance](../../../../../../.claude/skills/PrecapWeek/calendar-planning-guidance.md). Reuse them if they can supply the required facts without a second PM store.

### What one project review must establish

| Planning input | Question to resolve |
|---|---|
| Current goal and nearest useful result | What should this project achieve next, in the operator's own priorities? |
| Epic/task identity and ownership | Which native records represent that result, and who owns them? |
| Verified baseline and acceptance | What exists now; what exact evidence establishes success? |
| Dependencies and readiness | What is genuinely required, already accepted, waiting or unknown? |
| Next candidate work and alternatives | What can move next if a prerequisite or decision remains blocked? |
| Bounded size and resources | What is the smallest useful slice; what effort range, people, tools or operator input does it need? |
| Evidence and freshness | Which source supports each statement, and what needs a fresh read? |

### What weekly resource planning must add

Resolve the target week and timezone, fixed commitments, usable work intervals, protected routines, buffers, owner availability, effort uncertainty and cross-project priorities. Compare proposed demand with actual capacity before allocating. Mark overcommitment, prerequisite waits and explicit deferrals. The accepted Saturday-normal/Sunday-off and mixed-project time-block semantics in the correction ledger apply; fixed project-per-day assumptions do not become defaults.

### Open decisions

- Does “resource planning” initially mean only operator time/attention, or also collaborators, AI capacity, costs and tool availability?
- What minimal per-project planning output should be reused or added to existing project-context intake?
- How are estimates obtained, updated and bounded when the source has none?
- Which projects need review first, and what makes a project input sufficiently reliable for weekly selection?
- Are missing epic structures handled as display groupings or proposed OpenProject structural edits?
- Which dependency representation supports the layered menu without overwhelming it?
- Which presentation becomes canonical after an actual guided run succeeds?

## 5. Next-session process and output

Start by showing the specification locations and confirming the operator's intended layers. Walk one real project through those layers using fresh source facts, current implementation evidence and one meaningful next-work decision. Ask only the consequential missing question at that point. Then show how that candidate competes for actual next-week resources with another project.

Do not begin with a large questionnaire, a production rewrite, a new planning skill, or another Gantt. Use graphs or timelines within the walkthrough only when they clarify a real prerequisite or capacity decision. Do not execute project work to make the example appear complete.

The expected next design output is an operator-reviewed walkthrough and an agreed minimal project-planning input plus weekly resource-allocation behavior. Only after that scope is accepted should a narrow patch proposal identify exact changes to existing runtime/template files. This handover does not grant that implementation authorization.

## 6. Definition of done for the recovery phase

- The operator can navigate project → epic/workstream → task → next useful work without first sorting a global task dump.
- Each candidate has true identity, source state, readiness caveats and expected success evidence.
- At least one real project and one cross-project resource trade-off have been walked through with the operator.
- Native status, implementation proof, proposal and mock information remain distinct.
- Weekly selection is reconciled with actual or explicitly unavailable capacity; speculative dates are not treated as confirmed.
- Matrix 1, Matrix 2 and PrecapNextDay responsibilities remain distinct.
- The operator accepts the experience, corrects it, reduces scope or rejects it at a meaningful portfolio-level gate.

A verification script or a passing screenshot check is evidence only. It cannot replace these operator-facing criteria.

## 7. Artifact access and reproduction

[INDEX.md](INDEX.md) links the entire scoped conversation artifact set, including QA/diagnostic files and source helpers; [ARTIFACT-MANIFEST.json](ARTIFACT-MANIFEST.json) provides paths and classifications. The original showroom is a pre-existing source modified for hash selection; the original design guide/images remain source references, not newly authored deliverables. User attachments and browser/cache profiles are excluded from the authored-artifact inventory.

Reproduce discovery with `qmd search 'PrecapWeek' -n 7` and `qmd search 'project epic task Matrix' -c apex-weekly-orchestration -n 5`, then inspect bounded windows and current originating files. Inventory task-owned folders with `rg --files --hidden --no-ignore`. Check working-tree runtime changes with `git -C C:/GitDev/apexai-os-meta diff --name-only -- .claude/skills/PrecapWeek/SKILL.md .claude/skills/PrecapWeek/weekly-command-brief-template.md`. Packet verification receipts are in [VERIFICATION.json](VERIFICATION.json).

## Failure guards

- [P0 | I99] Do not promote a chart, export or mock scenario into the weekly specification merely because it exists.
- [P0 | I98] Do not infer an executable project plan or available capacity from native task names alone.
- [P0 | I97] Do not silently alter hierarchy, priorities, source state, calendar events or production contracts during this review.
- [P0 | I96] Do not hand over a source lookup or artifact inventory that can be resolved now as an open task; those are completed in this packet.
