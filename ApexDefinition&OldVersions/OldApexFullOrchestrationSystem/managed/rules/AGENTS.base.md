# AGENTS.base.md

This file defines the managed base governance for the runtime shell.

## Base Rules

- Work sequentially by default.
- Verify environment facts before acting on assumptions.
- Keep changes reviewable and validation-gated.
- Stop and report when a requested action exceeds declared scope.
- Treat `user/AGENTS.md` as the user-owned override layer.

## Runtime Posture

- Use managed rituals for startup and maintenance.
- Keep runtime changes minimal and deliberate.
- Do not broaden concurrency without validation evidence.

## Authority Order

- `managed/rules/OPERATING_SPINE_CANON.md` defines the top-level operating law.
- `managed/rules/ESCALATION_EXCEPTION_BLOCK.md` defines stop, hold, exception, and escalation handling.
- `managed/rules/AGENT_SWARM_INTERACTION_CANON.md` defines delegation, state, routing, and handoff rules.
- `user/AGENTS.md` remains the user-owned local override layer.

## Canonical Read Order

- Read this file first as the compact base-governance anchor.
- Then read the operating spine, escalation block, and swarm canon before applying local overrides or ritual detail.
- When work touches named-agent routing, managed orchestration, or agent overlap, also read:
  - `managed/agents/AGENT_INDEX.md`
  - `managed/processes/HOLDING_ORCHESTRATION_FLOW.md`
  - `managed/processes/AGENT_HANDOFF_CONTRACTS.md`
- When work touches KB placement, candidate promotion, or cross-reference integrity, also read:
  - `managed/knowledge/AGENT_KB_LANES.md`
  - `managed/knowledge/KB_STARTING_SOURCE_MAP.md`
  - `managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md`
  - `managed/knowledge/OVERLAP_VALIDATION_MATRIX.md`

## Delegation and Override Limits

- Delegation and handoff must follow `managed/rules/AGENT_SWARM_INTERACTION_CANON.md`.
- `user/AGENTS.md` may add local rules or tighten behavior, but it must not weaken managed governance, bypass escalation, or override the canonical authority order.
