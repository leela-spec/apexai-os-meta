# Bootstrap Ritual

## Goal

Start work from verified environment facts without drifting into unsupported assumptions.

## When to Run

- first run in a new workspace
- after long inactivity
- when migration or governance state changed

## Steps

1. verify repo branch and working tree state
2. verify GitHub fetch capability and non-destructive push capability when relevant
3. verify Python by command name first
4. if command-name resolution fails, verify by absolute path
5. record the verified interpreter path when absolute-path fallback is required
6. read `managed/rules/AGENTS.base.md`, `managed/rules/OPERATING_SPINE_CANON.md`, `managed/rules/ESCALATION_EXCEPTION_BLOCK.md`, and `managed/rules/AGENT_SWARM_INTERACTION_CANON.md`
7. check whether the validation gate blocks the requested orchestration pattern
8. create or update run artifacts when work changes canon or migration state
9. if the task touches named-agent routing or multi-agent orchestration, read:
   - `managed/agents/AGENT_INDEX.md`
   - `managed/processes/HOLDING_ORCHESTRATION_FLOW.md`
   - `managed/processes/AGENT_HANDOFF_CONTRACTS.md`
10. if the task touches KB placement, learning, or promotion-bound candidates, read:
   - `managed/knowledge/AGENT_KB_LANES.md`
   - `managed/knowledge/KB_STARTING_SOURCE_MAP.md`
   - `managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md`

## Human-facing Bootstrap (only when bootstrapping a new session)

Read, in order:
- `managed/rules/AGENTS.base.md`
- `managed/rules/OPERATING_SPINE_CANON.md`
- `managed/rules/ESCALATION_EXCEPTION_BLOCK.md`
- `managed/rules/AGENT_SWARM_INTERACTION_CANON.md`
- `managed/agents/AGENT_INDEX.md` when the session may involve routing or specialist activation
- `managed/processes/HOLDING_ORCHESTRATION_FLOW.md` when the session may involve cross-agent orchestration
- `managed/knowledge/AGENT_KB_LANES.md` when the session may create or route durable learning
- `managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md` when the session may produce promotion-bound candidates
- `user/identity/SOUL.md`
- `user/identity/IDENTITY.md`
- `user/identity/USER.md`
- `managed/rituals/HEARTBEAT.md`
- `user/memory/MEMORY.md` (main session only)
- recent daily logs: `user/memory/memory-daily/YYYY-MM-DD.md` (today + yesterday)
