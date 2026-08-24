# 03 — Multi-Repo Efficiency, Risks and Safety

Status: **VERIFIED RESEARCH / IMPLEMENTATION NOT AUTHORIZED**  
Date: 2026-08-24

## Executive decision

Working across separate Git repositories has **no inherent cloud-token surcharge** merely because the files live in different repos. The real costs come from boundaries that must be managed: context loading, QMD indexing/freshness, board aggregation, skill/version synchronization, Git state, and Docker workspace provenance.

The safest efficient operating model is therefore:

```text
ONE active repo per task
+ ONE explicit repo board
+ ONE explicit workspace
+ ONE explicit QMD collection set
+ ONE durable role profile
+ delayed reviewed learning promotion
```

Do not solve multi-repo by merging project files or live-syncing every runtime state.

## Cost matrix

| Cost | Why it appears | Provider tokens? | Mitigation |
|---|---|---:|---|
| Session bootstrap | Hermes loads profile identity, memory, skill index, project context | Yes | concise SOUL/MEMORY/AGENTS; role-relevant skills only; fresh focused sessions |
| Skill catalog | Metadata for available skills is indexed in prompt | Small recurring | progressive disclosure; do not install irrelevant domain packs globally |
| Full skill instructions | Loaded only when activated | Yes, on demand | keep SKILL.md focused; references on demand |
| QMD keyword search | Local SQLite/BM25 | No | use for exact/cheap lookup |
| QMD vector/rerank | Local models/CPU/RAM | No provider tokens | explicit collections; update/embed only when needed |
| Cross-repo QMD | Larger retrieval candidate set can reduce relevance | No direct provider cost; can increase returned context | explicit `collections` / `-c`; exclude large corpora from default search |
| Git/repo switching | branch/SHA/dirty-state verification | No | one canonical checkout per repo; repo registry in Apex |
| Board aggregation | Separate Hermes boards do not have one native dependency graph | No if scripted | deterministic asynchronous rollup to Apex |
| Learning promotion | candidate review/generalization can require model reasoning | Sometimes | deterministic candidate inventory first; invoke reviewer only for changed candidates |
| WSL/Windows crossing | 9P filesystem overhead when Linux tools use `/mnt/c` | No tokens, but time/I/O | canonical Linux filesystem for Linux-heavy tooling |
| Docker task mounting | incorrect dynamic workspace provenance can lose writes or broaden access | Potentially severe | static/explicit allowed mounts; live persistence/isolation acceptance tests |

## Verified token-efficiency primitives

### Hermes skills

Hermes and the Agent Skills standard use progressive disclosure:

```text
startup     -> skill name/description metadata
activation  -> full SKILL.md
need        -> references/scripts/assets
```

This means a centrally available skill does not imply its full contents enter every prompt. The Agent Skills specification recommends roughly ~100 tokens of metadata and loading full instructions only on activation.

### Hermes memory

Built-in `MEMORY.md` and `USER.md` are injected at session start. Current Hermes documents approximately 2,200 characters for MEMORY and 1,375 for USER. This makes raw persistent memory a recurring prompt cost and a poor place for large project knowledge.

### QMD

QMD runs keyword/vector/reranking locally and can index multiple named collections. There is no provider-token cost for indexing or retrieval itself. Provider context begins only when the agent includes selected retrieved material in a remote-model prompt.

## Multi-repo complexity risks

### R-MR-01 — Cross-project factual contamination

**Risk:** a reusable role profile learns project-specific facts into its own persistent MEMORY and carries them into another repo.

**Control:**
- project facts live in repo files/AGENTS/QMD;
- role memory stays small and procedural/operator-oriented;
- generalizable learning is promoted as a reviewed skill;
- do not cron-copy raw MEMORY between roles or repos.

### R-MR-02 — Concurrent writers to one role profile

Hermes explicitly warns never to run two agent processes against the same profile home concurrently because both automatically write memory/state.

**Control:** one active task per role profile initially. If genuine parallelism is required, create a separate worker profile rather than sharing one writable profile concurrently.

### R-MR-03 — Board bleed / tenant assumptions

Hermes documents boards as hard isolation and tenants as soft namespaces. An open upstream issue dated 2026-08-13 reports that tenant memory prefixing described by the docs is not implemented: workers can write to the same MEMORY store.

**Control:** use one board per repo as the initial v2 boundary. Do not rely on tenant namespacing for memory isolation.

### R-MR-04 — Cross-board orchestration gap

Hermes intentionally forbids `kanban_link` dependencies across boards. Current CLI supports explicit `--board <slug>` queries, but there is no single native cross-board dependency graph.

**Control:** Apex receives asynchronous read-only rollups plus explicit portfolio escalation tasks. Do not mirror every source task into Apex.

### R-MR-05 — Docker task workspace persistence

Current open upstream issue #91568 reports Docker-backed Kanban workers can commit inside a container while the host task directory was never correctly bind-mounted; artifacts disappear after cleanup.

**Control:** before multi-repo dispatch, prove host persistence with disposable read/write/commit tests for every workspace pattern actually used.

### R-MR-06 — Docker mount broadening

Open issue #73556 reports a profile's fixed `terminal.cwd` can override the dispatcher-provided Kanban task workspace and cause a broader host directory to be mounted.

**Control:** reusable role profiles must not hard-code a repo-specific `terminal.cwd` for Kanban work. Effective host/container mounts must be inspected during acceptance testing.

### R-MR-07 — Host/container cwd mismatch

Open issue #83856 reports workspace provenance can mount a host path at `/workspace` while commands still receive the original host path as container cwd.

**Control:** test terminal, file tools and code execution against the same disposable workspace; fail closed on mismatch.

### R-MR-08 — Shared external skill mutation

Hermes explicitly states writable `skills.external_dirs` can be edited in place by `skill_manage`.

**Control:** canonical Apex shared-skill source is reviewed/versioned. Runtime consumption should not imply unrestricted autonomous writes to the canonical source.

### R-MR-09 — Cron silent/stale automation

Hermes no-agent cron is zero-model/zero-token, but current issue history includes silent-success and scheduler persistence failures. Some were fixed; current installed version still needs a live acceptance test.

**Control:** fail non-zero on errors; persist last-success/fingerprint; monitor last run; do not treat empty stdout alone as proof of health.

### R-MR-10 — Duplicate Windows/WSL truth

Two live checkouts create divergence and manual synchronization overhead.

**Control:** one canonical operational checkout per repo after migration audit. Do not delete old copies until divergence is reconciled.

## Safety boundary recommendation

The multi-repo system should authorize a narrow machine workspace root rather than the laptop generally:

```text
~/workspaces/
  apexai-os-meta/
  MasterOfArts/
  acim-secular/
  Investment/
```

However, current Hermes Docker/Kanban bugs mean the exact mounting mechanism is an **implementation gate**, not an assumed fact. The runtime must prove:

1. intended repo is readable;
2. intended disposable file write persists host-side;
3. a disposable Git commit persists host-side;
4. unrelated host paths are inaccessible;
5. no Docker socket is exposed;
6. secrets are not forwarded unintentionally;
7. terminal/file/code-execution tools agree on the same workspace;
8. a role profile has no fixed repo-specific cwd overriding the task.

## Acceptance gate

Multi-repo execution is not production-approved until all of the following pass on the **installed Hermes version**, not just upstream docs:

- [ ] separate repo boards created and independently queryable;
- [ ] same role can sequentially work two boards without concurrent profile writers;
- [ ] project context changes correctly with workspace;
- [ ] QMD explicit collection scope returns only intended repo corpus;
- [ ] Docker host persistence test passes;
- [ ] Docker unrelated-path denial test passes;
- [ ] no raw-memory synchronization exists;
- [ ] Apex rollup can be regenerated deterministically from source boards;
- [ ] failure of the rollup is observable;
- [ ] no project file is duplicated into Apex merely for visibility.

## Primary sources

- Hermes profiles: https://hermes-agent.nousresearch.com/docs/user-guide/profiles
- Hermes memory: https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/memory.md
- Hermes file ownership guidance: https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/which-file-does-what.md
- Hermes Kanban: https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban
- Hermes CLI: https://hermes-agent.nousresearch.com/docs/reference/cli-commands
- Tenant memory issue #85497: https://github.com/NousResearch/hermes-agent/issues/85497
- Docker cwd override #73556: https://github.com/NousResearch/hermes-agent/issues/73556
- Docker workspace provenance #83856: https://github.com/NousResearch/hermes-agent/issues/83856
- Kanban host-backed workspace #91568: https://github.com/NousResearch/hermes-agent/issues/91568
- Hermes skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/
- Agent Skills specification: https://agentskills.io/specification
- QMD: https://github.com/tobi/qmd
- Microsoft WSL filesystem guidance: https://learn.microsoft.com/en-us/windows/wsl/filesystems
- Microsoft WSL interop: https://learn.microsoft.com/en-us/windows/dev-environment/wsl-interop
- Docker WSL best practices: https://docs.docker.com/desktop/features/wsl/best-practices/
