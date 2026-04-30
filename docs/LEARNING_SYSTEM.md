# Learning System

This file is a companion explainer for how learning is written down and routed in the current OpenClaw shell.

Important boundary: learning does not automatically promote truth. Promotion authority lives in `managed/rules/PROMOTION_PROTOCOL.md`, not in this file.

- `user/memory/MEMORY.md` stores lightweight local indexed context.
- `user/memory/MISTAKES.md` records recurring mistake patterns and standing rules.
- Repeated successes, failures, or reflections may produce candidate improvements, but accepted truth changes remain review-gated and packetized.
- Important learnings should be written down in an appropriate durable local or governed surface instead of being left in transient chat context.

The goal is disciplined write-down behavior without creating an unreviewed automatic mutation loop.

## Production-first learning boundary

Artifact-producing runs create learning only after the requested artifact exists or after a concrete blocker prevents artifact creation.

This matters for file, patch, KB, prompt, and workflow runs:

- A missing or unvalidated artifact is not a learning success.
- A plan, source ledger, claim cache, scope contract, or broad audit is not a substitute for the requested artifact.
- The useful learning unit is the concrete production result: produced artifact, validation result, failed check, repair attempt, blocker, and operator decision.
- Repeated production failures may nominate candidate mistakes or best practices, but they still require the governed promotion path before becoming accepted truth.
- Prompt/workflow learnings should normally route to `managed/agent_kb/special_ops__prompts_workflows/` when they concern reusable prompt shape, continuation loops, artifact-first sequencing, or repair templates.
- Structural production failures should normally route to `managed/rules/QA_HYGIENE_PROTOCOL.md` as hygiene findings when they affect reliability, traceability, or closure conditions.

For the first holding-layer KB infrastructure, durable learning should route through:

- `managed/knowledge/AGENT_KB_LANES.md` for lane ownership
- `managed/knowledge/KB_STARTING_SOURCE_MAP.md` for source seeding
- `managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md` for candidate logging and promotion readiness
- `managed/knowledge/OVERLAP_VALIDATION_MATRIX.md` for required second-agent validation

Those files remain managed companions to `PROMOTION_PROTOCOL.md`; they do not replace the packetized promotion rule.

## Learning capture checklist

When a material run creates learning, record at minimum:

- the requested artifact or bounded target
- whether the artifact was produced, validated, repaired, applied, blocked, or skipped
- the exact file paths affected
- the evidence or command that proved validation state
- the owner lane and validator lane for any candidate promotion
- the reason a lesson is candidate-only rather than accepted truth

Learning is complete only when the captured lesson remains separable from source material, candidate material, accepted canon, and live operational state.
