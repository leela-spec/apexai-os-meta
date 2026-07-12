<file>/.claude/Claude.md</file>
<old>
Stage subagents under `.claude/agents/` run each loop stage in an isolated context with its owning skill preloaded (`skills:` frontmatter). The main thread (WeeklyOrchestrator skill) dispatches them, holds gates, and owns the single durable write path. Ownership matrix + rationale: `apex-meta/kb/Weekly-Orchestrator/architecture/01-macro-architecture-decision.md`. Packet envelope + gate primitive: `.claude/skills/weekly-orchestrator/references/handoff-schema.md`. Terms: `apex-meta/GLOSSARY.md`.
</old>
<new>
Stage subagents under `.claude/agents/` run each weekly-loop stage in an isolated context with its owning skill preloaded (`skills:` frontmatter). The main thread (WeeklyOrchestrator skill) dispatches weekly stages, holds gates, and owns the weekly durable write path. Ownership matrix + rationale: `apex-meta/kb/Weekly-Orchestrator/architecture/01-macro-architecture-decision.md`. Weekly packet envelope + gate primitive: `.claude/skills/weekly-orchestrator/references/handoff-schema.md`. Terms: `apex-meta/GLOSSARY.md`.
</new>
<file>/.claude/Claude.md</file>
<old>
| apex-plan-ops | project planning proposal | apex-plan | operator gate in packet |
| apex-sync-ops | deterministic sync reports (dry-run) | apex-sync | none |
</old>
<new>
</new>
<file>/.claude/Claude.md</file>
<old>
| apex-review-validity / apex-review-alignment | dual-blind review of consequential packets | — | review |

## artifact_paths
</old>
<new>
| apex-review-validity / apex-review-alignment | dual-blind review of consequential packets | — | review |

### Project-management engine

Plan and Sync are optional global capabilities invoked independently; they are not WeeklyOrchestrator stages. `apex-plan-ops` returns native planning proposals, `apex-sync-ops` returns native deterministic reports, and `apex-session` remains the operator-facing/main-thread authority for approved project, task, and session mutation. Confirmed Session outputs and Sync reports become weekly-planning inputs only through a separate bridge.

| capability | role | authority |
|---|---|---|
| apex-plan-ops | project planning proposal | apex-plan native contract |
| apex-sync-ops | deterministic sync reports (dry-run) | apex-sync native contract |
| apex-session | approved project/task/session mutation and regenerated planning context | operator-facing/main-thread mutation authority |

## artifact_paths
</new>