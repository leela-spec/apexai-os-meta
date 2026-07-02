# AGENTS.md - Custom Override Rules (User)

This file is user-owned and should stay small and stable.
Base governance lives in `managed/rules/AGENTS.base.md`.

## Session Startup Read Order

1. `managed/rules/AGENTS.base.md` - global operating rules (sequential, validation-gated)
2. `managed/rules/OPERATING_SPINE_CANON.md` - top-level operating law
3. `managed/rules/ESCALATION_EXCEPTION_BLOCK.md` - stop, hold, exception, and escalation handling
4. `managed/rules/AGENT_SWARM_INTERACTION_CANON.md` - delegation, state, routing, and handoff rules
5. `managed/agents/AGENT_INDEX.md` - only when the session touches named agents, routing, or specialist activation
6. `managed/processes/HOLDING_ORCHESTRATION_FLOW.md` - only when the session needs multi-agent orchestration clarity
7. `user/identity/SOUL.md` - mission and boundaries
8. `user/identity/IDENTITY.md` - identity scaffold
9. `user/identity/USER.md` - who the human is and how they prefer to work
10. `user/memory/memory-daily/YYYY-MM-DD.md` (today + yesterday) - recent context
11. MAIN SESSION ONLY: `user/memory/MEMORY.md` (do not load in group chats)

## Custom Rules
<!-- Add rules specific to this runtime base / project fork. -->
- Local rules in this file may tighten or localize behavior, but they must not weaken managed governance, bypass escalation or promotion, or outrank the managed authority order.

## External Actions Require Permission
- email, messages, public posts, purchases, destructive commands

## Drift Prevention Conventions
- Prefer sequential work: one foreground flow at a time.
- Use BOOTSTRAP/CHECKLISTS when starting new work.
- If uncertain: STOP, REPORT, WAIT.
