# D02 Appendix — Separate Repo Boards + Asynchronous Apex Rollup

**Decision status:** ACCEPTED 2026-08-24  
**Decision ledger:** `../DECISIONS.md`  
**Primary subject file:** `../04-KANBAN-TOPOLOGY-AND-APEX-ROLLUP.md`

## Decision

Use one separate Hermes Kanban board per managed repository:

- `apex`
- `masterofarts`
- `acim`
- `investment`

Aggregate them asynchronously into a read-only Apex portfolio rollup. Do not use Hermes tenants as the repo-isolation boundary. Do not mirror every source task into Apex.

## Forces

- the operator wants each repo to retain its own project/Kanban boundary;
- Hermes boards are the stronger native isolation unit;
- tenants are soft namespaces rather than hard board boundaries;
- synchronization does not need to be simultaneous;
- Apex needs portfolio visibility without becoming a second task system;
- native Hermes cross-board task links are intentionally unsupported.

## Verified reasoning

- Hermes documents boards as independent queues with their own storage/workspace/log boundaries;
- Hermes supports explicitly selecting boards from CLI, enabling deterministic read-only collection;
- current upstream issue #85497 reports tenant memory isolation is not actually implemented as expected;
- an asynchronous rollup can be script-only and therefore requires no model calls or token spend.

## Chosen process

```text
source repo board
  -> explicit --board machine-readable read
  -> normalize selected status fields
  -> validate completeness/freshness
  -> write derived Apex portfolio snapshot
```

Apex source references always retain `source_board` and `source_task_id`.

## Risks

- no native cross-board dependency graph;
- rollup may be stale;
- partial board-query failure could publish a misleading aggregate unless validation fails closed;
- duplicating task bodies into the rollup would slowly recreate a second Kanban system;
- automatic write-back from Apex could create conflicts if introduced without policy.

## Shortcomings

- cross-project dependencies are references/escalations in Apex, not native Hermes dependency edges;
- portfolio views are eventually consistent rather than transactional;
- an additional deterministic rollup process is required.

## Rejected alternatives

1. **One global board + repo tenants** — rejected for initial production because tenants are soft boundaries and current tenant-memory behavior has an open upstream isolation defect.
2. **Separate boards + fully manual portfolio tracking** — rejected as too much repetitive operator work.
3. **Separate boards + bidirectional synchronization** — rejected initially because it adds conflict resolution and dual-authority complexity without a measured need.
4. **Duplicate every source task into Apex** — rejected because it creates stale mirrors and unclear ownership.

## Implementation consequence

Create/verify four boards. Implement rollup first as an on-demand deterministic read-only command. Only after identical repeated output and failure-handling tests may it be scheduled.

## Watch / revisit conditions

Revisit if Hermes ships and verifies a stronger native portfolio/cross-board primitive, or if asynchronous references prove insufficient for real cross-project dependencies.

## Evidence links

- Hermes Kanban: https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban
- Hermes CLI: https://hermes-agent.nousresearch.com/docs/reference/cli-commands
- Tenant memory issue #85497: https://github.com/NousResearch/hermes-agent/issues/85497
- Current analysis: `../04-KANBAN-TOPOLOGY-AND-APEX-ROLLUP.md`
