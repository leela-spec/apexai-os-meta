# D01 Appendix — Apex AIOS Meta as Portfolio Control Plane

**Decision status:** ACCEPTED  
**Decision ledger:** `../DECISIONS.md`  
**Primary subject files:** `../01-VERIFIED-ARCHITECTURE.md`, `../07-APEX-CROSS-PROJECT-EXCHANGE-CONTRACT.md`

## Decision

`leela-spec/apexai-os-meta` is the durable portfolio/orchestration control plane. MasterOfArts, ACIM, Investment and Apex itself remain independent project repositories and retain canonical ownership of their own project truth.

## Forces

- one place is needed for portfolio-level priorities, orchestration policy, cross-repo decisions and reusable-agent governance;
- project repositories already have independent Git history, authority, workflows and project facts;
- copying all project content into Apex would create duplicate truth and synchronization burden;
- Hermes/QMD can operate across independent workspaces without physical repo merging.

## Verified reasoning

- Hermes separates profile/runtime state from project/workspace context;
- QMD can index multiple absolute-path collections without merging repositories;
- Git repositories already provide the durable versioned source-of-truth boundary;
- the existing Apex repo already contains orchestration/epic infrastructure suitable for portfolio-level state.

## Apex owns

- repository/project registry;
- orchestration architecture and decisions;
- reviewed reusable profile specifications;
- reviewed generic shared-skill source after pilot;
- cross-project dependency/decision objects;
- derived board rollups;
- orchestration implementation evidence and health/freshness metadata.

## Apex does not own

- mirrored copies of every managed repo;
- raw Hermes memory/session state;
- credentials;
- Kanban SQLite databases;
- QMD indexes;
- repo-local BMAD state;
- repo-specific factual KBs merely for visibility.

## Risks

- Apex can become a second source of truth if rollups start copying full project facts;
- stale rollups can look current unless freshness is explicit;
- operators/agents may wrongly treat portfolio summaries as authoritative project detail;
- cross-project decision objects can drift from source tasks if no explicit references are preserved.

## Shortcomings

- Apex does not provide native transactional synchronization across Git repos or Hermes boards;
- portfolio state is intentionally derived/asynchronous;
- a portfolio question may require explicit QMD retrieval from source repos rather than reading Apex alone.

## Rejected alternatives

1. **Monorepo all managed projects into Apex** — rejected: unnecessary migration, scope/security blast radius, independent project history lost/complicated.
2. **Copy project KBs into Apex nightly** — rejected: duplicate truth and stale-copy failure mode.
3. **Use Hermes raw memory as the portfolio layer** — rejected: memory is profile-local runtime state, not durable project governance.

## Implementation consequence

Build pointers, summaries, dependency objects and reviewed procedures in Apex; leave source files in their repos. Every derived portfolio object must identify its source repo/board and freshness timestamp.

## Watch / revisit conditions

Revisit only if independent repos create a measured workflow cost that cannot be solved through board rollups, QMD retrieval and shared skills, or if a future upstream Hermes portfolio primitive supplies stronger native cross-repo state without duplicate truth.

## Evidence links

- Hermes profiles: https://hermes-agent.nousresearch.com/docs/user-guide/profiles
- Hermes Kanban: https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban
- QMD: https://github.com/tobi/qmd
- Project source verification: `../13-SOURCE-VERIFICATION-MATRIX.md`
