# 07 Final OpenClaw System

This folder is the active target input set for building the final OpenClaw system.

Treat the files in this folder as the current authoritative system-input baseline for the next build phase.

`BaselinePatches/VALIDATION_REPORT.md` records the validated overlap between this target set and the comparison material derived from `04_final-system-setup`.

## Final-system boundary

Only the following surfaces are treated as final-system runtime or durable companion surfaces:

- `managed/`
- `user/`
- `docs/`
- this `README-OpenClaw.md`

The following directories remain source, research, or staging inputs only and must not be treated as runtime authority:

- `NewFinals/`
- `BaselinePatches/`
- `AdvancedUpdateProcess/`

## First-iteration holding-orchestration surfaces

The first coherent holding-company / subsidiary-style architecture is expressed through:

- `managed/agents/` for named seed agents and overlap boundaries
- `managed/knowledge/` for KB lane ownership, source mapping, promotion logging, and cross references
- `managed/processes/` for orchestration flow, handoff contracts, and research-to-patchspec workflow

These surfaces operationalize the managed canons. They do not replace `managed/rules/` as runtime law.
