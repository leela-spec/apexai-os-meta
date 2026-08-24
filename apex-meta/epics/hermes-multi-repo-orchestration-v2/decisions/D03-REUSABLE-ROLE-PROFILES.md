# D03 Appendix — Reusable Durable Role Profiles

**Decision status:** ACCEPTED WITH CONSTRAINTS  
**Decision ledger:** `../DECISIONS.md`  
**Primary subject file:** `../05-REUSABLE-PROFILES-LEARNING-AND-MEMORY.md`

## Decision

Hermes profiles represent durable roles/agents, not repositories. Reuse the same role profile sequentially across managed repos. Initial v2 forbids simultaneous independent workers writing to the same profile state.

Examples:

- `research-strategist`
- `independent-reviewer`
- `workshop-designer` where useful
- `marketing-executive` where useful
- `portfolio-orchestrator`

## Forces

- useful role-level procedural learning should compound across projects;
- repo-specific profile copies would fragment learning and multiply maintenance;
- project facts must remain project-local;
- Hermes profiles have independent memory/session/config/credential state;
- current upstream guidance warns against concurrent processes sharing one writable profile.

## Verified reasoning

A profile supplies stable role identity and local learning. The active repo/workspace supplies project context. QMD supplies scoped project evidence. Therefore the same role can work Investment today and ACIM tomorrow without requiring copied profiles.

## Normal process

```text
role profile
  + explicit repo/workspace
  + repo AGENTS/context
  + explicit QMD collection scope
  -> bounded project task
  -> role-local procedural learning if appropriate
```

## Risks

- role memory can accumulate project facts if learning is not disciplined;
- same-profile parallel workers can race on profile memory/state;
- fixed repo-specific `terminal.cwd` in the reusable profile can defeat task/workspace isolation;
- overly broad role profiles can accumulate irrelevant skills/context.

## Shortcomings

- sequential same-profile use limits parallelism initially;
- truly parallel identical specialists require separate worker profiles/identities;
- role-local raw learning does not automatically propagate to other roles.

## Rejected alternatives

1. **One profile per repo** — rejected: fragmented learning, duplicated config, role drift.
2. **One universal super-profile** — rejected: excessive skill/context surface and poor identity separation.
3. **Concurrent workers on the same writable profile** — rejected until Hermes provides/proves safe machine-wide coordination for that state.

## Implementation consequence

Keep profiles thin. Do not encode repo facts or fixed repo cwd in reusable role definitions. Route project variance through workspace/context/QMD. Add a second specialist profile only when genuine same-role concurrency is required.

## Watch / revisit conditions

Revisit concurrency when installed Hermes proves gateway-wide/same-profile worker coordination or upstream introduces explicit safe shared-profile concurrency semantics.

## Evidence links

- Hermes profiles: https://hermes-agent.nousresearch.com/docs/user-guide/profiles
- Hermes Kanban: https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban
- Cross-board concurrency issue #78122: https://github.com/NousResearch/hermes-agent/issues/78122
- Current analysis: `../05-REUSABLE-PROFILES-LEARNING-AND-MEMORY.md`
