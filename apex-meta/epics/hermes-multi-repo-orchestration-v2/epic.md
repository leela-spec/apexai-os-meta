# Hermes Multi-Repo Orchestration v2

Status: **RESEARCH / OPERATOR DECISIONS REQUIRED / NO MIGRATION AUTHORIZED**  
Created: 2026-08-24  
Control repository: `leela-spec/apexai-os-meta`  
Branch: `main`

## Objective

Evolve the proven MasterOfArts Hermes pilot into one machine-level operating system for multiple repositories without cloning the pilot architecture per repository.

Initial repository estate:

| Repository | Default branch | Role in v2 |
|---|---|---|
| `leela-spec/apexai-os-meta` | `main` | Durable portfolio/control-plane repository and one managed project |
| `leela-spec/MasterOfArts` | `main` | Managed project/repository; source of proven Hermes pilot evidence |
| `leela-spec/acim-secular` | `master` | Managed project/repository |
| `leela-spec/Investment` | `main` | Managed project/repository |

## Verified architectural boundary

Apex AIOS Meta may become the **durable control plane**, but it must not become a copied mirror of every other repository or of Hermes runtime state.

### Apex should own

- portfolio/repository registry;
- orchestration architecture and ADRs;
- approved role/profile specifications;
- reviewed shared-skill source and promotion policy;
- cross-repository operating policy;
- durable portfolio decisions and cross-project summaries;
- migration manifests and implementation evidence for the orchestration layer;
- future-development backlog.

### Each managed repository should continue to own

- its actual source files and deliverables;
- repo/family/project `AGENTS.md` context and authority pointers;
- repo-specific facts, evidence, decisions and outputs;
- repo-specific Agent Skills and product context where required;
- its Git history and native default branch.

### Hermes local runtime should continue to own

- profile-local memory and sessions;
- credentials;
- Hermes local/learned skills;
- Kanban SQLite task state;
- runtime logs/checkpoints/sandbox state.

### QMD local runtime should continue to own

- its collection registry/configuration;
- derived search index;
- local embeddings/reranking models;
- rebuildable retrieval state.

The control repository may record the intended configuration and durable decisions, but must not copy runtime databases, credentials, raw profile memory, or QMD indexes into Git.

## Current recommended candidate architecture

```text
WINDOWS USER ENVIRONMENT
  |
  +-- WSL2 canonical AI workspace
      |
      +-- ~/workspaces/
      |   +-- apexai-os-meta/
      |   +-- MasterOfArts/
      |   +-- acim-secular/
      |   +-- Investment/
      |
      +-- ONE Hermes installation
      |   +-- portfolio/orchestrator profile
      |   +-- research-strategist profile
      |   +-- marketing-executive profile
      |   +-- workshop-designer profile
      |   +-- independent-reviewer profile
      |
      +-- ONE Hermes Kanban portfolio board (candidate)
      |   +-- tenant: apex
      |   +-- tenant: masterofarts
      |   +-- tenant: acim
      |   +-- tenant: investment
      |
      +-- ONE local QMD installation
      |   +-- scoped collections across the four repos
      |
      +-- ONE Docker execution boundary
          +-- only explicitly authorized workspace root mounted
```

Profiles represent durable **roles/agents**. Repositories represent **workspaces and project truth**. Tenants represent candidate per-repository Kanban namespaces inside one portfolio board.

## Why the Kanban topology is still a human decision

Current Hermes supports both:

1. many separate boards, including one per repo/domain; and
2. tenant namespaces inside a board.

However, Hermes explicitly forbids task links across separate boards. Therefore the naive topology "one board per repo plus one Apex aggregate board" does **not** provide a native single dependency graph. It would require manual duplicate summary tasks or a synchronization layer.

The current candidate is therefore one portfolio board with one tenant per repo, because it preserves one durable task graph while allowing tenant filters. This must still be acceptance-tested with real cross-repository tasks before being locked.

## Non-negotiables

- Do not move/copy the project contents of managed repos into Apex merely to make them visible to Apex.
- Do not create one Hermes profile per repo; profiles are agent-state boundaries, not project boundaries.
- Do not share one Hermes profile concurrently across multiple worker processes.
- Do not put profile memories/sessions/API keys in Git.
- Do not invent a custom cross-board synchronizer merely to preserve the phrase "one board per repo".
- Do not add an external memory service until built-in profile memory + shared reviewed skills are shown insufficient.
- Do not index giant repositories wholesale in QMD without authority/collection design and retrieval benchmarks.
- Do not maintain duplicate Windows and WSL live checkouts as parallel sources of truth.

## Current verified upstream evidence

- Hermes profiles: https://hermes-agent.nousresearch.com/docs/user-guide/profiles
- Hermes Kanban / boards / tenants: https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban
- Hermes skills / external dirs / project skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/
- Hermes built-in memory: https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/
- Hermes external memory providers: https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers/
- Hermes profile distributions: https://hermes-agent.nousresearch.com/docs/user-guide/profile-distributions
- QMD: https://github.com/tobi/qmd
- Claude Code setup: https://code.claude.com/docs/en/setup
- Codex Windows/WSL: https://developers.openai.com/codex/windows
- BMAD platform mappings: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/tools/installer/ide/platform-codes.yaml
- BMAD global-link proposal/open issue: https://github.com/bmad-code-org/BMAD-METHOD/issues/1728
- MarketingSkills: https://github.com/coreyhaines31/marketingskills

## Files in this epic

- `01-VERIFIED-ARCHITECTURE.md` — evidence-backed architecture, user stories and process flows.
- `02-MASTEROFARTS-SOURCE-MIGRATION-MANIFEST.md` — exact MasterOfArts source material another AI must preserve/re-home later.
- `FUTURE-DEVELOPMENT.md` — explicitly deferred ideas, including external memory.
- `state.yaml` — machine-readable decisions/open gates.

## Operator decision gates

- **D01 — Apex ownership:** Accept Apex as durable portfolio/control-plane repo while project truth remains in the source repos.
- **D02 — Kanban:** Select one portfolio board + repo tenants (recommended candidate) versus isolated boards + explicitly accepted lack of native aggregate dependency graph.
- **D03 — Profiles:** Accept durable role profiles reused across repos rather than repo-specific profile copies.
- **D04 — Learning:** Accept role-local raw memory plus reviewed shared-skill promotion as the initial spillover mechanism.
- **D05 — Shared skills:** Decide the first shared-skill source and promotion workflow in Apex after a live multi-repo test.
- **D06 — BMAD:** Decide which repos actually need full BMAD project state; do not assume one global `_bmad` installation is available today.
- **D07 — WSL workspace:** Converge managed repos to one canonical WSL workspace root while Windows accesses those same files through `\\wsl.localhost`.
- **D08 — QMD:** Accept one local QMD installation with curated cross-repo collections and explicit retrieval scopes.
- **D09 — External memory:** Keep external memory deferred until a measured cross-profile memory gap exists.

No repo migration, deletion, runtime reconfiguration, or source-file movement is authorized by creating this epic.
