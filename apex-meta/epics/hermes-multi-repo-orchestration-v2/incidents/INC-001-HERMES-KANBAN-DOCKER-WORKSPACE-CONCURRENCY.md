# INC-001 — Hermes Kanban / Docker Workspace / Concurrency Incident Cluster

**Status:** OPEN UPSTREAM RISK CLUSTER / MITIGATED BY D10  
**Recorded:** 2026-08-24  
**Decision link:** `../decisions/D10-BACKGROUND-MULTI-BOARD-AUTONOMY.md`

## Incident statement

The v2 design combines separate repo Kanban boards, reusable profiles and Docker-isolated execution. Current upstream Hermes issue evidence reports unresolved failures at the boundaries between those same mechanisms.

This incident does **not** claim Hermes is generally unusable. The MasterOfArts pilot passed direct Docker-backed execution. The incident specifically means we have insufficient evidence to trust **unattended concurrent multi-board Kanban workers** until the installed version passes explicit host-persistence/mount/concurrency tests.

## Affected architectural surfaces

```text
Kanban task/board
    ↓ chooses work
reusable Hermes profile
    ↓ supplies state/config
Docker backend
    ↓ supplies execution boundary
host repo/workspace
    ↓ must receive durable correct output
```

A defect at any arrow can make the agent appear successful while affecting the wrong state or non-durable state.

## Upstream issue A — profile cwd can override/broaden task workspace

**Issue:** NousResearch/hermes-agent #73556  
**URL:** https://github.com/NousResearch/hermes-agent/issues/73556

### Reported failure class

A profile-level terminal cwd can override the intended task/worktree workspace so the Docker worker receives a broader/different mount than expected.

### Relevance

Reusable role profiles must not carry fixed repo-specific `terminal.cwd` values when they are intended to move between repos. A task saying "work on repo X" is not sufficient evidence that Docker actually mounted only repo X.

### v2 mitigation

- no fixed repo cwd in reusable role profiles;
- verify effective cwd/mount before file mutation;
- D10 blocks unattended multi-board workers until acceptance passes.

## Upstream issue B — host/container cwd provenance mismatch

**Issue:** NousResearch/hermes-agent #83856  
**URL:** https://github.com/NousResearch/hermes-agent/issues/83856

### Reported failure class

A host path can be mounted into a container location while command/tool cwd semantics still refer to incompatible host/container paths, causing terminal/file/code tools to disagree about the effective workspace.

### Relevance

The v2 safety law requires terminal, file and code execution to operate against the same repo/workspace. A successful terminal command does not prove file/code tools are grounded identically.

### v2 mitigation

Acceptance tests compare all relevant tool paths and require one effective workspace identity.

## Upstream issue C — Kanban Docker worker workspace may not be host-backed

**Issue:** NousResearch/hermes-agent #91568  
**URL:** https://github.com/NousResearch/hermes-agent/issues/91568

### Reported failure class

A Kanban worker can apparently modify/commit successfully inside Docker while the task workspace is not truly host-backed, allowing completed work to disappear after sandbox/container lifecycle changes.

### Relevance

This is a critical integrity failure for autonomous implementation: `git commit` succeeding inside the worker is not enough. Durable host-side Git state must be verified outside the container.

### v2 mitigation

Every workspace acceptance test requires:

- host-visible disposable file;
- host-visible Git commit;
- persistence after worker/container exit/restart.

## Upstream issue D — concurrency limits can multiply per board

**Issue:** NousResearch/hermes-agent #78122  
**URL:** https://github.com/NousResearch/hermes-agent/issues/78122

### Reported failure class

Worker concurrency limits can be enforced per board rather than as a gateway-wide protection. Multiple boards may therefore create more workers than expected.

### Relevance

Hermes profile guidance warns against independent processes sharing one writable profile state. Four repo boards combined with one reusable `research-strategist` could therefore create concurrent profile writers if background dispatch is enabled naively.

### v2 mitigation

- initial same-role cross-repo use is sequential;
- background multi-board dispatcher off under D10;
- deliberate separate worker profiles are required for true same-role parallelism until global coordination is proven.

## Incident risk matrix

| Failure | Probability today | Impact | Primary risk |
|---|---|---|---|
| profile cwd broadens mount | unknown/open issue | high | wrong/broader filesystem access |
| host/container cwd mismatch | unknown/open issue | high | tools operate on inconsistent workspace |
| workspace not host-backed | unknown/open issue | critical | successful-looking work disappears |
| per-board concurrency multiplication | unknown/open issue | high | same profile/state concurrent writers |

Probability is intentionally not fabricated from issue counts. Presence of a current reproducible/open defect is enough to require acceptance testing for unattended writes.

## What remains verified despite this incident

The MasterOfArts pilot verified:

- Hermes itself operational on WSL2;
- direct Docker backend usable as isolation boundary;
- direct host-backed MasterOfArts mounts working in that tested configuration;
- QMD/Hermes integration;
- reusable specialist profiles in the pilot;
- restart/recovery of that pilot stack.

Therefore the incident changes the **autonomous multi-board execution rollout**, not the accepted Hermes/QMD/Docker architecture as a whole.

## Detection signals during future implementation

Treat any of the following as an incident recurrence:

- worker `pwd` differs from expected mapped workspace;
- file tool path and terminal cwd disagree;
- host cannot see a file immediately after container write;
- host Git HEAD does not contain worker's reported commit;
- worker can read an unrelated managed repo/host path not explicitly authorized;
- two workers for the same profile become active from different boards;
- successful worker status exists without durable host artifact/commit.

## Closure criteria

This incident can be marked `MITIGATED/SAFE_FOR_BACKGROUND_MODE` only after:

1. relevant upstream fixes are present in the installed Hermes release or local tests prove the defects do not affect our exact configuration;
2. D10's ten acceptance tests pass;
3. exact Hermes/Docker versions and configuration are recorded;
4. tests are repeated after a material Hermes workspace/Kanban/Docker upgrade.

Do not close the incident merely because the upstream GitHub issues are marked closed; verify the released version installed locally.

## Linked project files

- Decision: `../decisions/D10-BACKGROUND-MULTI-BOARD-AUTONOMY.md`
- Risk register: `../12-RISK-REGISTER.yaml`
- Multi-repo risk analysis: `../03-MULTI-REPO-EFFICIENCY-RISKS-AND-SAFETY.md`
- Implementation roadmap: `../11-IMPLEMENTATION-ROADMAP.md`
- MasterOfArts pilot evidence manifest: `../02-MASTEROFARTS-SOURCE-MIGRATION-MANIFEST.md`
