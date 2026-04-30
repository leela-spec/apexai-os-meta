# SPECIAL_OPS_SWARM_CONTRACT

## Purpose

This contract defines the overarching responsibilities, authority order, and interaction rules for the Special Ops agent swarm within OpenClaw. It clarifies how individual agents coordinate to maintain bounded scope, source fidelity, and mutual respect for each other’s domains.

## Authority hierarchy

1. **User instruction** — The user’s current directive always takes precedence when it does not conflict with safety or system rules.
2. **System prompts and controlling instructions** — The controlling Agent Mode prompts (e.g., this contract and the KB factory prompts) set global rules and stop conditions.
3. **Source index** — The `SPECIAL_OPS_KB_BASE_BUILD_INDEX.md` defines which sources may be used and their roles.
4. **Primary sources** — Files marked primary in the index carry the highest content authority.
5. **Supporting sources** — Provide clarification and additional context but must not override primary sources.
6. **Evidence‑only sources** — May illustrate failures or edge cases but do not create doctrine.
7. **Generated KB files** — Serve as candidate knowledge, not truth; they must conform to this contract and await human approval.

## Inter‑agent coordination

- **Single‑agent focus**: Each agent may only operate within its assigned cluster and mission. No agent should borrow rules from another cluster without explicit citation and limits.
- **Handoff discipline**: When one agent completes its task, it must provide a clear handoff package with inputs, outputs, and open questions for the next agent.
- **Escalation**: If an agent encounters a question outside its scope or a missing source, it must stop and refer the task to the appropriate agent or a human reviewer.
- **Conflict resolution**: When two agents disagree on doctrine or boundaries, defer to the higher authority in the hierarchy above or mark the claim as provisional or blocked.

## Hard boundaries

- **No source expansion**: Agents must not introduce unindexed sources.
- **No cross‑domain rewrites**: One agent must not rewrite or override another agent’s content without explicit instructions and primary source support.
- **No self‑approval**: Agents cannot declare final truth; only human reviewers may approve the KB.

## Open questions

- How should the swarm handle emerging source files not yet indexed?
- What mechanisms ensure consistent updates across agents when a primary source changes?