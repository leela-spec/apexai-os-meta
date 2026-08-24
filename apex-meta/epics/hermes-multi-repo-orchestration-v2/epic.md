# Hermes Multi-Repo Orchestration v2

Status: **RESEARCH VERIFIED / D02 OPERATOR DECISION REMAINS / IMPLEMENTATION NOT AUTHORIZED**  
Created: 2026-08-24  
Last research update: 2026-08-24  
Control repository: `leela-spec/apexai-os-meta`  
Branch: `main`

## Objective

Evolve the proven MasterOfArts Hermes pilot into one machine-level operating system for multiple repositories without cloning the pilot architecture per repository and without turning Apex into a mirror of every project.

Initial repository estate:

| Repository | Default branch | Role in v2 |
|---|---|---|
| `leela-spec/apexai-os-meta` | `main` | Durable portfolio/control-plane repository and managed project |
| `leela-spec/MasterOfArts` | `main` | Managed project; source of proven Hermes pilot evidence |
| `leela-spec/acim-secular` | `master` | Managed project |
| `leela-spec/Investment` | `main` | Managed project |

## Current verified target

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
      |   +-- reusable role profiles
      |   |   +-- portfolio-orchestrator
      |   |   +-- research-strategist
      |   |   +-- independent-reviewer
      |   |   +-- workshop-designer where useful
      |   |   +-- marketing-executive where useful
      |   |
      |   +-- SEPARATE repo Kanban boards (recommended D02)
      |       +-- apex
      |       +-- masterofarts
      |       +-- acim
      |       +-- investment
      |
      +-- ONE local QMD installation
      |   +-- profile-specific MCP declarations for roles that need retrieval
      |   +-- curated named collections per repo
      |
      +-- Docker execution boundary
      |   +-- exact task/repo workspace must be proven host-backed and bounded
      |
      +-- delayed deterministic portfolio/learning jobs
          +-- source boards -> read-only Apex rollup
          +-- local learned skills -> candidate scan -> review -> shared skill
```

## Core ownership law

### Apex owns durable portfolio/control-plane state

- repository/project registry;
- orchestration architecture and ADRs;
- reviewed role/profile specifications;
- shared-skill promotion policy and accepted generic procedures;
- cross-repository operating/safety policy;
- cross-project decisions/dependency objects;
- derived portfolio snapshots and health/freshness metadata;
- migration manifests and orchestration implementation evidence;
- future-development backlog.

### Each source repo owns its project truth

- source files/deliverables;
- repo/project `AGENTS.md` context and authority pointers;
- project facts/evidence/decisions/outputs;
- project-specific Agent Skills;
- BMAD/project framework state where used;
- native Git history/default branch.

### Hermes local runtime owns

- profile-local memory and sessions;
- credentials;
- local/learned skills before promotion;
- per-board Kanban SQLite state;
- runtime logs/checkpoints/sandbox state;
- per-profile MCP/config state.

### QMD local runtime owns

- collection registry/config;
- derived indexes/vectors;
- local models;
- rebuildable retrieval state.

Apex may record desired state and health metadata. It must not copy runtime DBs, credentials, raw profile memory, sessions or QMD indexes into Git.

## Major research correction — D02 Kanban

The original candidate `one board + repo tenants` is superseded.

Current Hermes evidence shows:

1. boards are the hard isolation boundary with separate DB/workspaces/logs;
2. tenants are soft namespaces;
3. cross-board dependency links are intentionally forbidden;
4. open issue #85497 reports tenant memory namespacing described by documentation is not actually implemented;
5. open issue #78122 reports concurrency limits can multiply per board rather than protect the gateway globally.

Therefore the current **recommended** D02 is:

```text
one board per repo
+ no background multi-board dispatch initially
+ asynchronous deterministic read-only Apex rollup
+ explicit Apex cross-repo dependency/decision objects
```

D02 remains the only primary architecture choice awaiting explicit operator acceptance.

## Verified learning model

```text
PROJECT FACT
  -> source repo / source board / QMD

ROLE-LOCAL LEARNING
  -> small profile MEMORY when truly session-global
  OR role-local learned skill for procedure

CROSS-REPO/CROSS-ROLE PROCEDURE
  -> deterministic candidate harvest later
  -> independent review/generalization
  -> accepted shared Agent Skill in Apex
  -> controlled runtime deployment
```

Raw `MEMORY.md` is never synchronized between repos/profiles.

Same role may work multiple repos **sequentially**. Do not concurrently run independent workers against the same writable profile state.

## Verified QMD model

One QMD engine can index absolute paths from all managed repos. Collection scoping is name-based and works from any current directory.

A role working only in `Investment` can therefore use:

```text
QMD MCP configured in that Hermes profile
collections=[investment-control, investment-evidence]
```

without opening Apex.

Important: Hermes profiles isolate their config/MCP connections, so every profile that should use QMD needs the QMD MCP declaration. A future tested profile distribution may carry this shared declaration without distributing memory/session/auth.

## Domain-framework policy

### BMAD

Project-local wherever actually used. Current BMAD installer is project-oriented; global link/install remains an upstream proposal (#1728), not a production capability to assume.

### MarketingSkills

MasterOfArts only for now. Do not globalize MarketingSkills or install it in ACIM/Investment/Apex without a real future need.

### Apex KB

Apex-specific. Current Apex root instructions point to `.claude/skills/apex-kb/`; Hermes project skill paths differ. The v2 implementation must establish one authoritative source with verified adapters/re-homing rather than duplicate divergent copies.

### Generic shared skills

Only reviewed project-neutral procedures belong in the Apex shared-skill layer.

## Safety/runtime constraint

Current upstream Hermes issues show task-scoped Kanban Docker workspaces can be mis-mounted, non-host-backed or overridden by a profile cwd in some configurations.

Initial v2 therefore uses **safe sequential execution mode**:

```text
select one repo
-> select explicit board/project
-> launch reusable role from canonical repo/workspace
-> verify Docker effective mount/cwd
-> explicit QMD collections
-> execute
-> verify host-side artifact/commit
-> update source board
-> later roll up to Apex
```

Background Kanban dispatch becomes a later gate only after the installed Hermes version proves task-scoped host persistence, mount isolation and machine-wide profile concurrency behavior.

## Files in this epic

1. `epic.md` — current authority/index.
2. `01-VERIFIED-ARCHITECTURE.md` — concise current architecture/user stories.
3. `02-MASTEROFARTS-SOURCE-MIGRATION-MANIFEST.md` — pilot provenance to preserve/re-home.
4. `03-MULTI-REPO-EFFICIENCY-RISKS-AND-SAFETY.md` — cost/complexity and safety analysis.
5. `04-KANBAN-TOPOLOGY-AND-APEX-ROLLUP.md` — D02 option analysis and recommended separate-board rollup.
6. `05-REUSABLE-PROFILES-LEARNING-AND-MEMORY.md` — D03/D04 profile/memory/concurrency model.
7. `06-SHARED-SKILL-PROMOTION-AND-CRON.md` — delayed reviewed learning spillover.
8. `07-APEX-CROSS-PROJECT-EXCHANGE-CONTRACT.md` — exact information buses/owners.
9. `08-QMD-MULTI-REPO-RETRIEVAL.md` — one-engine/per-profile MCP/scoped retrieval design.
10. `09-WSL-CANONICAL-WORKSPACE-MIGRATION-PLAN.md` — D07 data-safe filesystem migration.
11. `10-BMAD-AND-DOMAIN-SKILL-POLICY.md` — framework/domain skill placement.
12. `11-IMPLEMENTATION-ROADMAP.md` — phased executor plan and acceptance gates.
13. `12-RISK-REGISTER.yaml` — machine-readable risk controls/watch conditions.
14. `13-SOURCE-VERIFICATION-MATRIX.md` — claim-by-claim upstream verification.
15. `FUTURE-DEVELOPMENT.md` — deferred architecture including external shared memory.
16. `state.yaml` — machine-readable current decisions.

## Current operator decisions

- **D01 — Apex control plane:** accepted. Apex owns portfolio/orchestration state; project truth stays in source repos.
- **D02 — Kanban topology:** **decision pending**. Current verified recommendation = separate repo boards + asynchronous Apex rollup.
- **D03 — Reusable role profiles:** accepted with constraint: sequential same-profile use until global concurrency is proven safe.
- **D04 — Learning spillover:** accepted with constraint: raw memory stays local; reviewed generalized procedures spill over as skills.
- **D05 — Shared skill source:** accepted direction; Apex becomes reviewed canonical source only after promotion/deployment pilot.
- **D06 — BMAD/domain skills:** accepted: BMAD per repo where needed; MarketingSkills MasterOfArts-only now.
- **D07 — WSL workspace:** research verified/accepted direction; migration requires per-repo divergence audit and is not yet authorized.
- **D08 — QMD:** research verified/accepted direction: one engine, curated named collections, QMD MCP configured only for intended profiles; live multi-profile acceptance pending.
- **D09 — External memory:** deferred until a measured cross-profile memory gap exists.

## Current upstream evidence

Primary source map and issue evidence are maintained in `13-SOURCE-VERIFICATION-MATRIX.md` and `12-RISK-REGISTER.yaml`.

Key current sources:

- Hermes Kanban: https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban
- Hermes Profiles: https://hermes-agent.nousresearch.com/docs/user-guide/profiles
- Hermes Profile Distributions: https://hermes-agent.nousresearch.com/docs/user-guide/profile-distributions
- Hermes Skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/
- Hermes QMD: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-qmd
- QMD: https://github.com/tobi/qmd
- Agent Skills: https://agentskills.io/specification
- Microsoft WSL filesystems: https://learn.microsoft.com/en-us/windows/wsl/filesystems
- Microsoft WSL interop: https://learn.microsoft.com/en-us/windows/dev-environment/wsl-interop
- Docker WSL development: https://docs.docker.com/desktop/features/wsl/use-wsl/
- BMAD install: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/how-to/install-bmad.md
- MarketingSkills: https://github.com/coreyhaines31/marketingskills/blob/main/README.md

## Implementation status

```text
research: substantially complete
D02 human architecture gate: OPEN
runtime migration: NOT AUTHORIZED
repo file movement: NOT AUTHORIZED
background multi-board dispatch: NOT APPROVED
external memory: DEFERRED
```

No repo migration, deletion, runtime reconfiguration, source-file movement or scheduler installation is authorized by these research files.
