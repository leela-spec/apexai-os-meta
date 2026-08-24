# 01 — Verified Architecture — Hermes Multi-Repo Orchestration v2

Status: **RESEARCH VERIFIED / D02 OPERATOR DECISION REMAINS / IMPLEMENTATION NOT AUTHORIZED**  
Date: 2026-08-24

## 1. Current architecture in one view

```text
Apex AIOS Meta = durable portfolio/control plane
|
+-- Project truth remains in four independent Git repositories
|   +-- apexai-os-meta
|   +-- MasterOfArts
|   +-- acim-secular
|   +-- Investment
|
+-- One machine-level Hermes runtime in WSL2
|   +-- reusable role profiles, used sequentially across repos
|   +-- separate repo Kanban boards (current D02 recommendation)
|   +-- no automatic all-board dispatcher initially
|
+-- One local QMD engine
|   +-- curated named collections per repo
|   +-- QMD MCP configured only in profiles that need retrieval
|
+-- Docker execution boundary
|   +-- workspace/mount provenance must pass live host-persistence tests
|
+-- Apex asynchronous exchange
    +-- read-only board rollup
    +-- cross-repo decision/dependency objects
    +-- reviewed generic skill promotion
    +-- health/freshness metadata
```

## 2. Verified principles

### V1 — one Hermes installation, many repos

Hermes project context/workspace and project-local skills are discovered from the active working directory/project, while profiles and runtime configuration are separate from project truth. One Hermes installation can therefore serve multiple repositories; no install clone is required per repo.

### V2 — profile = role, not repo

Hermes profiles own identity/state such as SOUL/config/memory/sessions/skills/credentials. A profile does not inherently belong to one Git repository.

Target reusable roles:

```text
portfolio-orchestrator
research-strategist
independent-reviewer
workshop-designer       # where useful
marketing-executive     # where useful
```

Critical constraint: Hermes explicitly warns never to point two independent processes at the same profile. Current open issue #78122 also reports multi-board concurrency limits are per-board rather than gateway-wide. Therefore same-role reuse is sequential in initial v2.

### V3 — repo = facts, evidence, project rules and outputs

Repo-local ownership:

```text
AGENTS.md
project/source facts
accepted decisions
code/content
project-specific skills
BMAD state where used
outputs/evidence
Git history
```

Do not put this corpus in reusable role MEMORY.

### V4 — separate repo boards are now recommended

Current Hermes docs describe boards as the hard isolation boundary: separate DB, workspaces and logs; spawned workers are pinned to their board; cross-board links are forbidden.

Tenants are soft namespaces. Open issue #85497 reports the documented tenant memory namespace is not implemented and memory can pollute across tenants.

Therefore current recommendation:

```text
board=apex
board=masterofarts
board=acim
board=investment
```

Apex obtains portfolio visibility through an **asynchronous deterministic read-only rollup**, not a second live task database.

D02 remains a human gate because this trades native cross-project dependency links for stronger project isolation.

### V5 — Apex is control plane, not warehouse

Apex may own:

```text
project registry
portfolio priorities
orchestration ADRs
profile specifications
shared-skill governance
cross-project decisions
cross-project dependency references
derived board rollups
health/freshness status
migration/implementation evidence
```

Apex must not automatically own/copy:

```text
all project files
raw profile MEMORY/USER
sessions
API credentials
Kanban SQLite DBs
QMD index DB/vectors
project BMAD state
project-specific skills
```

### V6 — QMD is one engine, explicit corpus per task

QMD's collection registry can point at absolute paths across independent repos. Its `-c` / MCP `collections` scoping works from any directory.

Thus:

```text
Investment task
  cwd = ~/workspaces/Investment
  QMD = investment-control + investment-evidence

ACIM task later
  cwd = ~/workspaces/acim-secular
  QMD = acim-control + acim-site-docs
```

Both use the same local QMD engine.

But Hermes profiles isolate MCP/config. Every profile that needs QMD must have the QMD MCP declaration. A future tested profile distribution can deliver the common MCP declaration while preserving local memory/session/auth.

### V7 — cross-repo learning = procedure promotion, not memory sync

Initial spillover:

```text
repo task
  -> facts remain repo-local
  -> role learns locally
  -> generic procedure candidate detected later
  -> independent review/generalization
  -> accepted Agent Skill in Apex Git
  -> controlled deployment to applicable profiles
```

No cron copies `MEMORY.md` between repos/profiles.

### V8 — WSL is canonical runtime filesystem

Microsoft independently recommends keeping Linux-heavy Git/build files in the Linux filesystem; its current interop guide explicitly flags `/mnt/c` Git/build use as slow via cross-filesystem 9P. Docker independently recommends code inside the Linux distribution for WSL2 Linux-container development.

Target:

```text
~/workspaces/
  apexai-os-meta/
  MasterOfArts/
  acim-secular/
  Investment/
```

Windows accesses the same files with `\\wsl.localhost\...`.

Migration must reconcile Windows/WSL divergence before freezing old copies; no automatic bidirectional sync is part of v2.

### V9 — Docker is still the single execution-isolation concept, but Kanban integration is gated

Official Hermes Docker backend supports a persistent hardened container and explicit workspace/env configuration.

However current open upstream issues document:

- profile `terminal.cwd` overriding a Kanban workspace and broadening a mount (#73556);
- host workspace mounted under `/workspace` while container cwd remains host path (#83856);
- Kanban Docker worker changes/commits disappearing because task workspace was not actually host-backed (#91568).

Initial v2 therefore runs one repo/role sequentially and proves Docker mount/cwd/host persistence before background Kanban dispatch is enabled.

## 3. Detailed user stories

### US-01 — Research Strategist works Investment

```text
operator selects Investment
  -> board: investment
  -> repo: ~/workspaces/Investment
  -> profile: research-strategist
  -> project context: Investment AGENTS.md
  -> QMD: investment-control, investment-evidence
  -> Docker: exact active workspace verified
  -> result written to Investment
  -> task state written to investment board
```

If the task discovers:

```text
"Provider X is stale"
```

that is Investment project truth and stays in Investment.

If it discovers:

```text
"When two time-series sources disagree, compare observation date, release date and vintage before declaring contradiction"
```

that is a reusable research procedure candidate.

### US-02 — same Research Strategist later works ACIM

```text
Investment execution finishes
  -> no research-strategist process remains

later:

repo: ~/workspaces/acim-secular
board: acim
same profile: research-strategist
QMD: acim-control, acim-site-docs
```

The role retains general research capability/learning but project authority comes from ACIM context/retrieval.

### US-03 — daily portfolio overview

```text
deterministic rollup
  -> hermes kanban --board apex list --json
  -> hermes kanban --board masterofarts list --json
  -> hermes kanban --board acim list --json
  -> hermes kanban --board investment list --json
  -> normalize only current status/ID/owner/blocker metadata
  -> write derived Apex snapshot
```

Portfolio orchestrator reads this snapshot first. QMD control collections are queried only if deeper evidence is required.

### US-04 — cross-repo dependency

Investment source task cannot depend natively on an Apex-board task.

Instead:

```text
Investment task
  -> blocked: "needs Apex portfolio decision D42"

Apex
  -> one cross-repo decision/dependency object
  -> references investment board/task ID
  -> decision recorded durably in Apex

then
  -> explicit follow-up updates Investment source task
```

No task mirroring.

### US-05 — learning spills over overnight

```text
18:00 source work completes
  -> role-local learned skill candidate

23:00 deterministic no-agent scan
  -> detects only new/changed candidate hashes
  -> zero model calls

next review window
  -> independent-reviewer sees changed candidates only
  -> rejects project-specific fact
  -> promotes generic method

accepted method
  -> Apex shared skill source
  -> deterministic deployment
  -> applicable roles discover it later
```

Synchronization is delayed by design.

## 4. Shared-skill classes

### S1 — project-specific

Lives in source repo.

Examples:

```text
Apex KB
ACIM content pipeline
Investment/IPOS-specific procedure
MasterOfArts product context
```

### S2 — role-local learned procedure

Lives with role until proven general.

Examples:

```text
research-strategist/learned/source-comparison-technique
```

### S3 — shared reviewed procedure

Apex becomes canonical Git source only after review.

Examples:

```text
authority-first-navigation
exact-match-patch-generation
evidence-contradiction-review
```

Hermes supports external skill dirs and project/local/external precedence. External directories are not inherently read-only, so runtime deployment must not expose canonical Apex source to uncontrolled self-modification.

## 5. Framework/domain-skill placement

### BMAD

```text
repo needs BMAD -> install BMAD in that repo
repo does not -> no BMAD
```

Current BMAD installer is project-oriented. Global install/link remains an open upstream proposal (#1728).

### MarketingSkills

Current v2 decision:

```text
MasterOfArts = YES
ACIM         = NO
Investment   = NO
Apex         = NO
```

Do not infer global domain skills from global role names.

### Apex KB

Remains Apex-specific. One authoritative skill source must be established across Hermes/Claude/Codex without behavior drift.

## 6. Current runtime modes

### Safe Mode A — approved implementation target

```text
one active execution repo
one reusable profile process
explicit repo board
explicit QMD collections
Docker mount/cwd inspected and host persistence verified
background all-board dispatch off
```

### Mode B — future only after tests

```text
background multi-board dispatch
+ task-scoped Docker mounts
+ concurrency safety
```

Required to re-check open Hermes issues before enabling.

## 7. Token/efficiency model

Multi-repo Git storage itself creates no model call.

Costs come from what is loaded/retrieved:

| Mechanism | Provider context/cost behavior |
|---|---|
| repo exists on disk | none |
| AGENTS/project context | loaded as project context; keep concise |
| role MEMORY/USER | recurring session-start context; keep small |
| skill catalog | metadata only until activation |
| full skill | on-demand |
| QMD BM25/vector/rerank | local compute, no provider tokens |
| returned QMD passages | may enter provider prompt |
| deterministic rollup | zero model calls |
| deterministic learning harvest | zero model calls |
| semantic learning review | model call only when changed candidates exist |

Efficiency therefore comes from **siloing by default and promoting/querying only what is needed**, not from physically merging repositories.

## 8. What is explicitly not claimed/proven

- Hermes does not natively provide an Apex-style portfolio control plane.
- Hermes does not natively create one aggregate cross-board dependency graph.
- Hermes does not natively promote one role's learned skill into a reviewed Git library shared by all roles.
- BMAD does not currently have a proven production global-link model we rely on.
- current Kanban Docker task mounts are not assumed safe merely because direct Docker works.
- global cross-board same-profile concurrency is not assumed safe.
- profile distributions are promising but must be acceptance-tested before becoming Apex's production delivery mechanism.

## 9. Detailed authority files

Use these rather than expanding this file indefinitely:

- `03-MULTI-REPO-EFFICIENCY-RISKS-AND-SAFETY.md`
- `04-KANBAN-TOPOLOGY-AND-APEX-ROLLUP.md`
- `05-REUSABLE-PROFILES-LEARNING-AND-MEMORY.md`
- `06-SHARED-SKILL-PROMOTION-AND-CRON.md`
- `07-APEX-CROSS-PROJECT-EXCHANGE-CONTRACT.md`
- `08-QMD-MULTI-REPO-RETRIEVAL.md`
- `09-WSL-CANONICAL-WORKSPACE-MIGRATION-PLAN.md`
- `10-BMAD-AND-DOMAIN-SKILL-POLICY.md`
- `11-IMPLEMENTATION-ROADMAP.md`
- `12-RISK-REGISTER.yaml`
- `13-SOURCE-VERIFICATION-MATRIX.md`

`13-SOURCE-VERIFICATION-MATRIX.md` is the claim-level evidence index and must be refreshed against current upstream versions before implementation phases that depend on rapidly changing Hermes/QMD behavior.
