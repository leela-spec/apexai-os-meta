# 13 — Source Verification Matrix

Status: **CURRENT RESEARCH SNAPSHOT**  
Verified: 2026-08-24

Purpose: prevent future executors from treating architecture recommendations as self-evident. Every consequential v2 claim below is tied to current primary upstream evidence and, where possible, an independent second source or live MasterOfArts evidence.

## Evidence grades

| Grade | Meaning |
|---|---|
| **A** | 2+ current primary sources and/or primary docs + current upstream implementation/issue evidence |
| **B** | 1 strong current primary source; live acceptance still required |
| **C** | design recommendation assembled from verified primitives; not itself an upstream product feature |
| **BLOCKED** | upstream evidence shows current behavior is unsafe/unreliable for the proposed use without mitigation |

## Verification matrix

| ID | Claim | Evidence | Grade | v2 consequence |
|---|---|---|:--:|---|
| V01 | Hermes supports multiple isolated boards, one per project/repo/domain. | Hermes Kanban official docs + source docs | A | Four separate repo boards. |
| V02 | Workers spawned on a board are pinned to that board and cannot see other boards via Kanban tools. | Hermes Kanban official docs + CLI source docs | A | Board is repo task-state isolation boundary. |
| V03 | Cross-board task links are intentionally forbidden. | Hermes Kanban official docs + source docs | A | Apex needs reference/rollup objects, not native dependency links. |
| V04 | Tenant is softer than board isolation. | Hermes docs explicitly call tenant soft, board hard. | A | Do not use tenants as repo security boundary. |
| V05 | Documented tenant memory isolation is currently contradicted by live upstream issue evidence. | Hermes docs + open issue #85497 with source inspection/runtime test | **BLOCKED** | Reject one-board-tenants as initial repo isolation. |
| V06 | A single Hermes profile is an agent/state boundary, not inherently one repository. | Hermes Profiles official docs | A | Reuse role profiles sequentially across repos. |
| V07 | Two independent processes must not share one Hermes profile concurrently. | Hermes Profiles explicit warning + automatic memory behavior | A | Sequential same-role operation initially. |
| V08 | Current multi-board dispatcher can multiply concurrency because limits are enforced per board. | Kanban config docs + open issue #78122 runtime reproduction | **BLOCKED** | Do not enable all-board background dispatch until proven fixed/safely bounded. |
| V09 | Hermes Projects can group folders/repos and bind a Kanban board. | Current CLI docs + tools reference | A | Optional one project object per repo improves navigation. |
| V10 | `project bind-board` currently has a validation bug in upstream issue history. | Current CLI docs + open #76285 | A | Verify board exists before/after binding; do not trust exit 0. |
| V11 | Docker backend is a persistent shared container and supports explicit cwd mounting/volumes/env controls. | Hermes configuration official/source docs | A | One Docker security policy is feasible. |
| V12 | Current Kanban Docker task-scoped workspace behavior has host-persistence risk. | Open issue #91568 with reproduction + expected invariant | **BLOCKED** | Direct sequential repo execution first; background Docker workers only after live persistence test. |
| V13 | Profile `terminal.cwd` can broaden a Kanban Docker task mount. | Open issue #73556 with reproduction/workaround | **BLOCKED** | Reusable role profiles must not hard-code repo cwd for Kanban. |
| V14 | Host/container cwd provenance can differ across terminal/file/code execution. | Open issue #83856 + current Docker configuration docs | **BLOCKED** | Acceptance-test all tool surfaces on same disposable workspace. |
| V15 | QMD collections are global and may point to absolute paths across unrelated directories/repos. | QMD README/config docs | A | One local QMD engine can index all managed repos. |
| V16 | QMD collection scoping works from any current directory. | QMD SYNTAX.md + README | A | Agent in Investment can query Investment collection without entering Apex. |
| V17 | QMD MCP uses plural `collections`; singular `collection` is ignored. | QMD SYNTAX.md + changelog | A | Machine-readable prompts/config must use plural field. |
| V18 | QMD can exclude collections from unscoped default search. | QMD README + syntax + example-index | A | Large project collections excluded by default; explicit scopes required. |
| V19 | QMD hybrid/vector/rerank runs locally without cloud dependencies. | QMD README + Hermes official QMD integration | A | Retrieval itself costs local compute, not provider tokens. |
| V20 | Once QMD MCP is configured, Hermes gets QMD tools automatically. | Hermes QMD integration + Hermes MCP docs | A | No QMD skill load needed for routine tool availability. |
| V21 | Hermes profile configuration/MCP is profile-scoped. | Hermes Profiles + Profile Distributions docs | A | Each retrieval-enabled reusable profile needs QMD MCP declaration. |
| V22 | Profile distributions can version SOUL/config/skills/cron/MCP while preserving memories/sessions/API keys. | Hermes Profile Distributions official docs | A | Promising Apex-controlled role-definition delivery mechanism; pilot before production. |
| V23 | Hermes skills support project-local, profile-local and external dirs with precedence. | Hermes Skills official docs | A | Shared generic procedures + project-local overrides are natively possible. |
| V24 | External skill dirs are not a write-protection boundary. | Hermes Skills official docs | A | Canonical Apex shared-skill Git source should not be routine self-improvement scratch. |
| V25 | Agent Skills use progressive disclosure. | Agent Skills specification + Hermes Skills | A | Shared procedures can be available without loading full instructions in every prompt. |
| V26 | Hermes MEMORY/USER are session-start context and bounded. | Hermes Memory + Which File Does What | A | Do not put project KB/status in raw profile memory. |
| V27 | Project needs/instructions belong in AGENTS/project context. | Hermes Which File Does What + context docs + MasterOfArts pilot | A | Repo-local facts/rules remain in source repo. |
| V28 | Hermes no-agent cron can run scripts with zero model calls. | Hermes Cron + no-agent cron guide | A | Candidate harvest/rollup can be deterministic and token-free. |
| V29 | Cron has current/recent silent/persistence/guard failure classes. | Cron docs + issues #20353/#77131/#80624 | A | Manual/idempotent test + health receipt before scheduler becomes authoritative. |
| V30 | Microsoft recommends Linux project files in WSL filesystem for Linux CLI workloads. | WSL filesystems docs + current WSL interop guide | A | Canonical managed repos move to `~/workspaces`. |
| V31 | `/mnt/c` Git/build access from Linux has cross-filesystem overhead. | Current Microsoft WSL interop | A | Avoid `/mnt/c/GitDev` as long-term Hermes/QMD worktree. |
| V32 | Docker recommends WSL/Linux source location for best Linux-container development experience. | Docker WSL development + Microsoft Dev Containers guidance | A | Independently corroborates D07. |
| V33 | Windows can access Linux repo files via `\\wsl$` / `\\wsl.localhost`. | Microsoft filesystems + interop docs | A | Operator can stay in Windows UI without second live checkout. |
| V34 | Windows high-frequency access to WSL files also crosses 9P and can be slower. | Current Microsoft WSL interop | A | Heavy tooling should run in WSL; Windows access is primarily operator/editor access. |
| V35 | BMAD installer is project-oriented and defaults to current/explicit project directory. | BMAD install docs + README | A | BMAD stays per repo where needed. |
| V36 | Global BMAD link/install is still an open proposal. | BMAD issue #1728 + current installer docs | A | Do not invent global BMAD linker. |
| V37 | MarketingSkills supports per-project `.agents/skills/` installation and `.agents/product-marketing.md`. | Official MarketingSkills README | A | Keep MarketingSkills MasterOfArts-local for current need. |
| V38 | Multi-repo status aggregation into Apex is not a native Hermes portfolio feature. | Absence of native cross-board aggregate/dependency surface; verified board/project primitives | C | Implement a small deterministic read-only rollup, clearly labeled derived state. |
| V39 | Cross-agent reviewed skill promotion through Apex is not a native automatic Hermes feature. | Hermes skills/profile primitives + Agent Skills standard | C | Build only candidate-detection/review/deployment glue; never claim native auto-learning sync. |
| V40 | One repo per active task avoids inherent provider-token cost from multi-repo storage. | QMD/skills/context mechanisms only load/retrieve selected context; separate Git repos themselves create no model call | B | Main efficiency costs are context/retrieval/sync, not repo count itself. |

## Primary-source set

### Hermes

- Kanban: https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban
- Kanban source docs: https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/kanban.md
- CLI: https://hermes-agent.nousresearch.com/docs/reference/cli-commands
- Profiles: https://hermes-agent.nousresearch.com/docs/user-guide/profiles
- Profile Distributions: https://hermes-agent.nousresearch.com/docs/user-guide/profile-distributions
- Skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/
- Memory: https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/memory.md
- Which File Does What: https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/which-file-does-what.md
- MCP: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- QMD integration: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-qmd
- Cron: https://hermes-agent.nousresearch.com/docs/user-guide/features/cron
- Docker/config: https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/configuration.md

### Hermes risk evidence

- tenant memory #85497: https://github.com/NousResearch/hermes-agent/issues/85497
- cross-board concurrency #78122: https://github.com/NousResearch/hermes-agent/issues/78122
- project bind #76285: https://github.com/NousResearch/hermes-agent/issues/76285
- Docker cwd override #73556: https://github.com/NousResearch/hermes-agent/issues/73556
- Docker cwd provenance #83856: https://github.com/NousResearch/hermes-agent/issues/83856
- host-backed Kanban workspace #91568: https://github.com/NousResearch/hermes-agent/issues/91568
- cron silent output #20353: https://github.com/NousResearch/hermes-agent/issues/20353
- cron Python guard #77131: https://github.com/NousResearch/hermes-agent/issues/77131
- cron persistence #80624: https://github.com/NousResearch/hermes-agent/issues/80624

### Retrieval / Skills

- QMD README: https://github.com/tobi/qmd/blob/main/README.md
- QMD syntax: https://github.com/tobi/qmd/blob/main/docs/SYNTAX.md
- QMD example registry: https://github.com/tobi/qmd/blob/main/example-index.yml
- Agent Skills: https://agentskills.io/specification

### Filesystem/runtime

- Microsoft WSL filesystems: https://learn.microsoft.com/en-us/windows/wsl/filesystems
- Microsoft WSL interop: https://learn.microsoft.com/en-us/windows/dev-environment/wsl-interop
- Docker WSL development: https://docs.docker.com/desktop/features/wsl/use-wsl/
- Docker WSL backend: https://docs.docker.com/desktop/features/wsl/
- Microsoft Dev Containers: https://learn.microsoft.com/en-us/windows/dev-environment/docker/dev-containers

### Project frameworks

- BMAD install: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/how-to/install-bmad.md
- BMAD README: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/README.md
- BMAD global proposal #1728: https://github.com/bmad-code-org/BMAD-METHOD/issues/1728
- MarketingSkills: https://github.com/coreyhaines31/marketingskills/blob/main/README.md

## Implementation rule

This matrix is a research snapshot, not eternal truth.

Before any phase that depends on a current upstream bug/feature, the executor must re-check:

```text
installed runtime version/help
+ current official docs
+ current issue state/fix release
```

If an upstream issue has been fixed, the architecture may simplify—but only after a live regression test proves the fixed behavior on the installed version.
