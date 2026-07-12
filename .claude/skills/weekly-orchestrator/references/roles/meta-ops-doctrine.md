# Meta Ops Doctrine (migrated from old-apex v1 role KB)

Purpose: distilled still-valid doctrine for the meta_ops accountability — the main-thread orchestrator (stage dispatch, gate holding, single write path) and the meta_ops stage subagents (apex-evidence-normalize, apex-flow-recap, apex-status-merge, apex-project-status, apex-precap-next-day, apex-plan-ops, apex-sync-ops).
Source basis: `apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/meta_ops/` (ESSENCE.md; BEST_PRACTICES.md, MISTAKES.md, TEMPLATES.md carry no accepted entries). Governing baseline: `.claude/skills/weekly-orchestrator/SKILL.md`, `references/handoff-schema.md`, `apex-meta/kb/Weekly-Orchestrator/architecture/01-macro-architecture-decision.md`.

## Best practices

- Rule: keep activation sets minimal — for any operator trigger, dispatch the smallest useful set of stage subagents the current loop position actually requires; never fan out stages speculatively or "while we're at it". Parallelism rules in SKILL.md say what MAY run concurrently; this rule says only dispatch what the trigger needs. (ESSENCE.md — agent boundary + core constraints)

## Known failure modes

- Avoid: self-validating high-impact output that meta_ops itself assembled. Review wiring covers stage packets; anything the main thread synthesizes itself (aggregations, integration summaries, conflict resolutions) that would justify a canon-changing write must also route through the dual-blind reviewer pair before its inputs count as verified — the orchestrator never acts as its own validator. (ESSENCE.md — core constraints: "do not self-validate high-impact output")
