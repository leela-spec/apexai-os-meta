# Module 01 — Validated Design Decisions

Status: operator-validated design authority for Module 01, except the weekly visualization format, which remains intentionally unresolved pending focused research.

## Purpose

This file freezes the operator decisions already made for the Weekly Command Brief so later design/research/implementation does not re-litigate them or rely on chat memory.

## Locked runtime boundary

- Owner: `PrecapWeek`.
- Primary operator artifact: `Weekly_Command_Brief`.
- Downstream consumer: `PrecapNextDay`.
- The Brief contains the downstream handoff; do not create a duplicate machine-seed artifact.
- PrecapWeek designs the Monday-Friday week architecture; PrecapNextDay operationalizes the next day from that architecture and current conditions.
- PrecapWeek does not create sprint prompt packets, execute project work, merge project status, or claim calendar writes.

## Operator interaction

### Planning conversation

Use an adaptive hybrid:

- resolve what confirmed evidence supports automatically;
- ask only high-impact choices that cannot safely be inferred;
- then produce a complete proposed Weekly Command Brief.

### Approval

Use one final portfolio-level operator gate: approve, edit, reduce scope, resolve a consequential constraint, or reject/reframe. Do not create repeated per-project approval gates for already-decided semantics.

## Human-facing information architecture

### Layering

Use a compact control/result layer first, followed by sufficient project and week detail. The Brief must be quickly scannable without deleting meaningful planning depth.

### Project coverage

Every active project remains visible:

- projects receiving meaningful work get normal detail;
- intentionally inactive/deferred projects get a compact reason rather than disappearing.

### Project work granularity

For each active project show:

- weekly target;
- why this week when material;
- success evidence;
- actionable work items;
- dependencies/blockers/decisions when material;
- expected outputs.

Do not expand into sprint/prompt execution depth; that belongs downstream.

## Inline decision metrics

Every scored work item/task uses only this compact inline notation, on the same line as the task:

`Task or outcome (I94/R25/E9)`

Semantics:

- `I` = impact, 1-100;
- `R` = risk, 1-100;
- `E` = evidence strength, 1-100.

Rules:

- keep the three metrics inline with the work item;
- do not create separate metric columns or verbose labels beside each task;
- do not replace them with a synthetic single priority score;
- do not zero-pad values;
- the metrics support judgment but do not replace dependencies, deadlines, capacity, operator intent, or sequencing logic.

## Week/day ownership

### PrecapWeek owns the week architecture

The Weekly Command Brief must make the intended Monday-Friday structure visible. This is a core output, not an optional hint.

PrecapWeek determines at week level:

- which outcomes/work are intended on which weekdays;
- cross-day sequencing and dependencies;
- deadline-aware placement;
- meeting/calendar/capacity-aware placement;
- deliberate review, buffer, continuation, or recovery roles;
- project/flow allocation by day;
- full/compressed/minimal/omitted direction where capacity is foreseeable;
- deliberate deferrals and their reason;
- rationale for non-obvious placement.

### PrecapNextDay owns operationalization

PrecapNextDay:

- revalidates the actual next-day calendar/capacity and new evidence;
- adapts the weekly architecture when reality changed;
- selects the executable flows for that day;
- defines sprint-level execution structure;
- creates Flow Execution Cards and prompts;
- determines the exact intra-day execution sequence;
- handles relevant calendar-write requests under its own boundary.

The weekly plan is therefore authoritative direction but not a frozen executable daily schedule.

## Blueprint visibility

Use consequence-and-exception visibility:

- always show the resulting week/day architecture;
- show rationale when deadlines, meetings, dependencies, capacity, I/R/E evidence, or operator intent materially change allocation;
- do not print generic internal blueprint mechanics when they add no decision value;
- do not expose default project-order rules merely because they were consulted internally.

## Decisions, rationale, and provenance

- Surface consequential uncertainties/decisions, not every minor unknown.
- Use targeted rationale: explain non-obvious priority, sequence, deferral, deadline, capacity, or dependency choices.
- Keep provenance compact: decisive state sources, material freshness issues, consequential assumptions, and low-confidence areas only.

## Downstream handoff

Keep one embedded compact structured handoff in the Weekly Command Brief.

Because the week architecture is a core PrecapWeek output, the handoff must explicitly preserve access to it without duplicating the Brief. Minimum intent:

- week and weekly intent;
- result/review state;
- reference to the Brief's week-architecture section;
- next target day;
- that day's intended role/outcomes;
- capacity assumption and known fixed constraints;
- carry-forward dependencies/review items;
- next consumer: `PrecapNextDay`.

Prefer references plus a small next-day seed over copying the full weekly matrix into YAML.

## Repository repairs accepted for Module 01

1. Keep the existing J2 simulation fixture as legacy evidence and correct claims that it already has the target Brief shape.
2. Repair the malformed `active_files` path whose string currently contains explanatory prose.
3. Remove the stale template `source_gap` referring to the archived/superseded weekly-plan output contract; do not resurrect that old contract.

## Unresolved design question — weekly visualization

The human-facing visualization of the Monday-Friday architecture is not yet decided.

Operator requirement:

> The week must be visible in a simple, minimalist, information-dense table/matrix that feels close to a calendar and makes the weekly structure immediately understandable.

The visualization must be researched before production integration. See `WEEK-VISUALIZATION-RESEARCH-HANDOVER.md`.

Do not finalize or rewrite the production Weekly Command Brief template around a guessed visualization before that research is accepted.
