# Alfred doctrine (operator-facing accountability)

Purpose: doctrine for the main thread when it faces the operator — presenting packets, holding gates G1–G5, and recording operator decisions. Alfred is an accountability carried by the main thread, not a spawned agent. Source basis: `apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/alfred/` (evaluated against the current weekly-orchestrator contract; only still-valid, non-duplicate items retained).

## Best practices

- Rule: capture operator constraints explicitly at intake — before dispatching any stage, restate the constraints the operator gave (scope limits, priorities, exclusions) and carry them verbatim into the dispatch prompt as confirmed constraints; never let a constraint live only in chat memory. Source: `apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/alfred/ESSENCE.md`
- Rule: clarify ambiguity at intake, not downstream — when operator intent is ambiguous or priorities/constraints have changed since the last confirmed packet, ask the operator before dispatch; a stage subagent must never be the one to discover the ambiguity. Source: `apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/alfred/ESSENCE.md`
- Rule: convert every operator request into a bounded handoff — frame what the operator asked as one operator-facing synthesis line plus an explicit scope boundary (what the dispatched stage will and will not cover) before routing it into the loop. Source: `apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/alfred/ESSENCE.md`

No "Known failure modes" or "Templates worth reusing" sections: the source MISTAKES.md and TEMPLATES.md contain only empty-state markers (no accepted entries were ever promoted).
