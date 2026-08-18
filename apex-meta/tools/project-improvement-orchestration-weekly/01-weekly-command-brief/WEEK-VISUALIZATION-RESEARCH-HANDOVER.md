# Module 01 — Weekly Visualization Research Handover

## Mission

Find and recommend the best human-facing visualization for the Weekly Command Brief's Monday-Friday architecture.

The target is a **simple, minimalist, information-dense week matrix that feels close to a calendar** and can be produced reliably in Markdown/chat while remaining usable by the operator at a glance.

This is a presentation-design research task. Do not redesign PrecapWeek architecture, project-state ownership, gating, or PrecapNextDay responsibilities.

## Operator requirement

The current prose-first week visualization is not understandable enough.

The operator wants:

- a table/matrix/calendar-like weekly view;
- Monday-Friday visible together;
- minimal visual noise;
- high information density;
- obvious sequencing, deadlines, meetings/capacity effects, and deliberate deferrals;
- tasks/outcomes shown compactly;
- inline metrics only in the form `Task (I94/R25/E9)`;
- no separate verbose metric columns unless a tested design proves they materially improve readability;
- enough human context to understand the week without reading machine schemas.

## Already validated semantics — do not reopen

Read `DESIGN-DECISIONS.md` first.

Key locked decisions:

- PrecapWeek owns the Monday-Friday week architecture.
- PrecapNextDay operationalizes the next day and may adapt the weekly architecture when reality changes.
- Every active project remains visible; deferred projects need only a compact reason.
- Project detail is weekly target + success evidence + actionable work, not sprint/prompt depth.
- Work-item metrics are inline `I/R/E` on the same line as the item.
- Rationale is consequence/exception based, not generic blueprint exposition.
- The Weekly Command Brief remains the single human source; its embedded handoff references it rather than duplicating it.

## Repository baseline and prior hints to inspect

Use live repository evidence first. At minimum inspect:

1. `.claude/skills/PrecapWeek/weekly-command-brief-template.md`
2. `.claude/skills/PrecapWeek/SKILL.md`
3. `.claude/skills/PrecapWeek/weekly-blueprint-standard.md`
4. `.claude/skills/PrecapWeek/weekly-blueprint-meeting-example.md`
5. `apex-meta/operator-output-design/step3-output-design-system/01-operator-output-design-principles.okf.yaml`
6. `apex-meta/operator-output-design/step3-output-design-system/02-shared-card-and-brief-anatomy.okf.yaml`
7. `apex-meta/operator-output-design/step3-output-design-system/03-planning-artifact-designs.okf.yaml`
8. `apex-meta/operator-output-design/step4-operator-template-system/01_RESEARCH_FINDINGS.md`
9. `artifacts/weekly-plans/weekly_plan_packet-20260816-2026-W34.md`
10. `artifacts/weekly-plans/weekly_plan_packet-20260712-2026-W29.md`
11. `apex-meta/kb/Weekly-Orchestrator/OperatorResearch/PersonalOrchestrationProcessFlow.md`
12. archived `weekly-plan-output-contract.md` only as historical evidence; it is not live authority.

Important prior findings:

- Step 3 locked human-first, first-10-seconds comprehension, progressive disclosure, and minimum machine payload.
- The old doctrine says wide Markdown tables should not be the primary surface. Treat this as evidence, not an immutable rule for this task, because the operator has now explicitly requested a calendar-like matrix for the week.
- The old weekly contract already had `weekday_plan_direction` for Monday-Friday with day role, capacity shape, priority projects, direction, calendar notes, and deferrals.
- W29 and W34 show real week structures that can be used as test fixtures.
- Previous output-template research identified table-first/schema-heavy outputs as a failure mode. The new design must avoid reproducing that failure while still satisfying the explicit calendar-matrix requirement.

## Research requirement

Perform fresh online research before recommending a design.

Research current best practices and existing implementations for compact weekly planning interfaces, specifically combinations of:

- weekly calendar views;
- project-by-day matrices;
- time-blocking / weekly planner layouts;
- executive portfolio planning dashboards;
- swimlane planning boards;
- Markdown-compatible calendar/table patterns;
- information-dense scheduling UI;
- progressive disclosure in planning interfaces;
- visual encoding of capacity, deadlines, dependencies, risk, and deferral.

Prefer primary or authoritative sources when available: design-system documentation, product documentation, academic/HCI sources, or maintained open-source implementations.

Also inspect existing code/components/libraries that could be imported or adapted if the production surface later moves beyond pure Markdown. Do not assume custom implementation is necessary.

## Design candidates to compare

Do not settle on the first table idea. Produce at least four materially different candidates, for example:

1. **Days as columns / projects as rows**
2. **Days as columns / priority blocks as rows**
3. **Vertical day cards in a compact 5-day matrix**
4. **Hybrid calendar strip + per-project compact list**
5. Any demonstrably better design found in research

Each candidate must be rendered using the same real W34-derived data so the comparison is meaningful.

## Stress-test data

Use at least these three scenarios:

### Scenario A — normal W34-style week

- Leela, MasterOfArts, Apex, Investment all primary.
- MasterOfArts website is an explicit weekly focus.
- Normal capacity.
- Multiple actionable work items across projects.

### Scenario B — meeting-heavy week

- at least one standard day;
- one compressed day;
- one minimal/overloaded day;
- deliberate deferrals;
- fixed meetings/deadlines visible.

### Scenario C — sequencing/dependency week

- one work item must happen before another;
- one deadline creates a specific weekday placement;
- at least one high-impact task is intentionally deferred because another task has stronger timing/dependency logic.

Use inline metric notation exactly like:

`Verify Home runtime (I90/R20/E95)`

Do not create separate I/R/E explanatory columns in the default candidate unless the research demonstrates a clearly superior compact pattern.

## Evaluation criteria

Score each candidate against:

- first-10-seconds comprehension;
- week-at-a-glance quality;
- Monday-Friday temporal clarity;
- ability to see project balance;
- ability to see dependencies and sequence;
- ability to see meetings/deadlines/capacity changes;
- information density;
- visual simplicity;
- Markdown/chat rendering resilience;
- mobile/narrow-screen degradation;
- ease for AI generation;
- ease for PrecapNextDay consumption/reference;
- avoidance of schema/table overload;
- compatibility with the validated Weekly Command Brief anatomy.

## Required output

Return a decision-ready research report, not implementation.

Required sections:

1. **Repository evidence** — prior decisions/hints and what remains applicable.
2. **External evidence** — concise findings with current sources.
3. **Candidate designs** — at least four rendered with the same sample data.
4. **Comparison matrix** — strengths, weaknesses, failure modes, device/Markdown behavior.
5. **Recommendation** — one primary design and optionally one fallback for narrow/mobile rendering.
6. **Exact proposed Weekly Command Brief visualization spec** — minimal grammar, not a full rewritten template.
7. **Import/reuse options** — existing code, format, library, or design pattern worth adopting instead of building from scratch.
8. **Open questions** — only genuinely unresolved operator decisions.

## Non-goals

Do not:

- implement production changes;
- edit the live Weekly Command Brief template;
- redesign the PrecapWeek/PrecapNextDay ownership boundary;
- introduce a second weekly artifact;
- turn the visualization into a machine schema dump;
- restore the old fixed five-project roster or old priority/urgency/date rating system;
- replace inline `I/R/E` with a synthetic total score;
- infer that the old `wide tables not primary` rule automatically wins over the current explicit operator requirement.

## Success condition

The operator should be able to compare concrete week views and say, with minimal explanation, "this is the format I want to use every Sunday."
