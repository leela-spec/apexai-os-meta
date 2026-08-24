# D08 Appendix — One QMD Engine, Explicit Multi-Repo Collections

**Decision status:** ACCEPTED / LIVE MULTI-PROFILE ACCEPTANCE PENDING  
**Decision ledger:** `../DECISIONS.md`  
**Primary subject file:** `../08-QMD-MULTI-REPO-RETRIEVAL.md`

## Decision

Use one local QMD installation and registry with curated named collections pointing into all managed repositories. Every Hermes profile that needs QMD receives the QMD MCP declaration. Routine tasks explicitly query only the relevant repo collections.

## Forces

- local retrieval should be reusable across repos without separate QMD installations;
- repository files must remain canonical truth;
- global unscoped retrieval over the whole estate would introduce stale/irrelevant context and local indexing cost;
- an agent working inside one repo must be able to retrieve that repo without entering Apex;
- Hermes profile configuration is isolated, so MCP availability must be explicit per profile.

## Verified reasoning

QMD collections can point at absolute paths and are selected by collection name independently of the shell's current repo directory. Hermes can expose QMD through its native MCP connection. Therefore one process/index registry can serve Investment, ACIM, MasterOfArts and Apex without merging those repos.

## Normal project flow

```text
cd ~/workspaces/Investment
research-strategist
  -> QMD MCP configured in profile
  -> collections=[investment-control, investment-evidence]
  -> local retrieval/reranking
  -> bounded selected passages enter reasoning context
```

## Portfolio flow

Only selected small control collections are queried together for cross-project questions. Do not use one whole-estate collection.

## Risks

- wrong or unscoped collection selection can contaminate a task with another repo's information;
- stale QMD indexes can return obsolete evidence;
- very large collections waste local embedding/index resources and reduce authority precision;
- a new Hermes profile will not necessarily inherit QMD config unless deliberately configured/distributed;
- QMD itself is local, but selected retrieved passages can still be sent to the configured remote model.

## Shortcomings

- collection design/freshness needs per-repo maintenance;
- every profile needing retrieval requires MCP setup or a tested profile-distribution mechanism;
- QMD is derived retrieval state, not a cross-project decision/task system.

## Rejected alternatives

1. **One QMD install per repo** — rejected: unnecessary duplicate engine/runtime/model state.
2. **One giant whole-estate collection** — rejected: retrieval/authority pollution and indexing waste.
3. **Copy repo content into Apex for retrieval** — rejected: duplicate truth.
4. **Assume all profiles automatically see QMD** — rejected: Hermes profile config is isolated.

## Implementation consequence

Define curated collection registry and explicit collection scopes before onboarding each repo. Acceptance-test QMD from at least two different role profiles while each is launched from its source repo.

## Watch / revisit conditions

Revisit collection layout when measured retrieval benchmarks show missed authority, stale results or excessive local indexing cost; do not reorganize solely by intuition.

## Evidence links

- QMD: https://github.com/tobi/qmd
- Hermes QMD integration: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-qmd
- Hermes profiles: https://hermes-agent.nousresearch.com/docs/user-guide/profiles
- Current design: `../08-QMD-MULTI-REPO-RETRIEVAL.md`
