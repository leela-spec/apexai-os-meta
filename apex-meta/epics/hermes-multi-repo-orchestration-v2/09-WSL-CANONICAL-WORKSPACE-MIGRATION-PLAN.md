# 09 — WSL Canonical Workspace Migration Plan

Status: **D07 VERIFIED / MIGRATION NOT AUTHORIZED**  
Date: 2026-08-24

## Decision

For the managed Hermes estate, converge to **one canonical Linux-native checkout per repository** under a common WSL workspace root.

Candidate:

```text
/home/<operator>/workspaces/
  apexai-os-meta/
  MasterOfArts/
  acim-secular/
  Investment/
```

Windows remains the operator UI and can access the same files through:

```text
\\wsl.localhost\Ubuntu\home\<operator>\workspaces\...
```

Do not maintain Windows and WSL checkouts as two live writable sources of truth.

## Triple-source verification

### Microsoft — WSL filesystem guidance

Microsoft recommends storing project files in the WSL Linux filesystem when using Linux command-line tools. It explicitly recommends `/home/<user>/Project` rather than `/mnt/c/...` for fastest performance.

Source: https://learn.microsoft.com/en-us/windows/wsl/filesystems

### Microsoft — current WSL interop guidance

Current Microsoft interop guidance classifies:

```text
Linux process -> Linux files (/home/...)      fast/native ext4
Linux process -> Windows files (/mnt/c/...)   slow/cross-filesystem 9P
Windows process -> Linux files (\\wsl$\...)   cross-filesystem; use for occasional access
```

It specifically says avoid `/mnt/c` for build systems, `node_modules`, and Git repos when the main tools run in Linux.

Source: https://learn.microsoft.com/en-us/windows/dev-environment/wsl-interop

### Docker — WSL development guidance

Docker recommends storing code inside the default Linux distribution for the best development experience with WSL2 and Linux containers.

Sources:
- https://docs.docker.com/desktop/features/wsl/use-wsl/
- https://docs.docker.com/desktop/features/wsl/

This independently aligns with Hermes/QMD/Codex/Claude Linux-side operation.

## What this decision does NOT mean

It does not mean:

- Windows is replaced by Linux;
- the operator must use Linux desktop apps;
- repositories are merged;
- every Windows application is expected to perform high-frequency edits across `\\wsl$`;
- old Windows checkouts are deleted immediately;
- a fixed Linux username of `root` is required.

The target should preferably use a normal WSL user home instead of `/root` for long-term operator usability, subject to live migration testing.

## Why migrate carefully

A repository can differ between its Windows and WSL copies in ways Git remote state does not capture:

```text
modified tracked files
untracked files
ignored but locally important files
local config
unpublished commits
branch divergence
submodules
worktrees
line-ending differences
permissions/executable bits
symlinks
local-only generated data
secrets/.env
large ignored artifacts
```

A simple delete/reclone can lose local state.

## Repository branch registry

Current GitHub defaults:

| Repo | Default branch |
|---|---|
| `leela-spec/apexai-os-meta` | `main` |
| `leela-spec/MasterOfArts` | `main` |
| `leela-spec/acim-secular` | `master` |
| `leela-spec/Investment` | `main` |

Do not impose a global `main` assumption. Preserve each repo's native branch contract unless the repo itself is separately migrated.

## Migration law

For **each repo independently**:

```text
INVENTORY
  -> COMPARE
  -> CLASSIFY DIFFERENCES
  -> RECONCILE
  -> CREATE/VERIFY CANONICAL WSL COPY
  -> RECONFIGURE TOOLS
  -> ACCEPTANCE TEST
  -> FREEZE OLD COPY
  -> DELETE OLD COPY only later and only with explicit approval
```

Never migrate all four simultaneously.

## Phase W0 — runtime identity

Before moving files record:

```yaml
wsl_distribution:
wsl_user:
linux_home:
workspace_root:
windows_unc_path:
git_version:
case_sensitivity:
```

Target:

```text
workspace_root = ~/workspaces
```

Prefer normal-user ownership of repos and generated files.

## Phase W1 — per-repo inventory

For both candidate copies, collect read-only evidence:

```bash
git rev-parse --show-toplevel
git remote -v
git branch --show-current
git rev-parse HEAD
git status --porcelain=v1 --untracked-files=all
git log -1 --oneline --decorate
```

Also inspect:

```text
.gitignore-sensitive local files
.env and credential files
submodules
worktrees
LFS status if used
large local ignored folders
```

Produce a migration record:

```yaml
repo: acim-secular
windows_copy: C:\GitDev\acim-secular
wsl_copy: ...
remote: ...
default_branch: master
windows_head: ...
wsl_head: ...
windows_dirty: ...
wsl_dirty: ...
unpublished_commits: ...
untracked_count: ...
divergence_class: identical|remote-ahead|windows-only|wsl-only|both-diverged|unknown
```

## Phase W2 — reconcile without data loss

Allowed classes:

### Case A — both copies clean and same SHA

Choose WSL copy as canonical, no content merge required.

### Case B — Windows has unpublished changes, WSL clean

Do not overwrite. Reconcile the intentional Windows changes first using ordinary Git or a deliberate file-level migration after review.

### Case C — WSL has unpublished changes, Windows clean

Treat WSL as the candidate source; push/commit only under normal repo policy before freezing Windows.

### Case D — both have changes

Stop automatic migration for that repo. Produce a diff/divergence report and reconcile deliberately.

### Case E — ignored/local-only data

Classify:

```text
needed runtime data
rebuildable cache
secret
obsolete artifact
unknown
```

Never copy secrets into Git merely to make migration easier.

## Phase W3 — canonical WSL checkout

If no valid Linux-native checkout exists, create one using normal Git from the canonical remote or a verified local transfer that preserves Git history.

Requirements:

```text
correct remote
correct native default branch
expected HEAD
expected tags/submodules where relevant
normal Linux file ownership
clean status after intended migration
```

Do not use `/mnt/c/GitDev/...` as the long-term Hermes/QMD/Docker working tree.

## Phase W4 — Windows operator access

Verify from normal Windows Explorer:

```text
\\wsl.localhost\Ubuntu\home\<operator>\workspaces
```

Recommended operator ergonomics:

- pin workspace root to Quick Access;
- optionally create shortcuts per project;
- use `explorer.exe .` from WSL when needed;
- do not run high-I/O Windows build tooling against `\\wsl$` if the same workload can run in WSL.

The architecture is Linux-runtime-first, Windows-UI-friendly—not dual-live-storage.

## Phase W5 — reconfigure AI/runtime tools

Only after one repo canonicalization passes:

### Hermes

- repo board workspace points to WSL path;
- reusable role profiles contain no stale `C:\...` or `/root/MasterOfArts` hard-coded repo assumptions;
- repo-specific `AGENTS.md` loads from canonical checkout.

### QMD

- collection paths updated to canonical WSL directories;
- run `qmd update`;
- run `qmd embed` only as needed for pending/new semantic chunks;
- verify known queries after path change.

### Docker

- only canonical intended WSL path is host source;
- verify file + Git commit persistence host-side;
- verify terminal/file/execute_code agree on workspace;
- verify unrelated sibling/host paths not exposed beyond intended mount policy.

### Codex / Claude / Antigravity

- launch inside the canonical WSL checkout when using Linux-side workflows;
- no copy-to-Windows synchronization step in normal operation.

## Phase W6 — old Windows copy freeze

After the WSL copy passes:

1. rename old Windows copy to an explicit frozen name, e.g. `_OLD-READONLY-2026-...`, or otherwise make its status unmistakable;
2. add a short local marker indicating the canonical location;
3. do not edit it;
4. keep for a bounded verification period;
5. delete only under explicit operator approval.

Do not create an automatic bidirectional rsync/robocopy layer. It creates two writers and reintroduces the source-of-truth problem.

## Migration order

Recommended order minimizes risk:

1. **acim-secular** — small, clean pilot if current local audit confirms;
2. **Investment** — smaller and mostly current Git content;
3. **MasterOfArts** — existing WSL Hermes pilot; reconcile its current Windows/WSL dual-copy state;
4. **apexai-os-meta** — largest/highest-control-value repo; migrate last after process is proven and current dirty/untracked state is fully audited.

This is a candidate order; live local status may change it.

## Rollback

Until old copy deletion:

```text
rollback = stop using new WSL checkout
         + restore tool pointers to prior known-good copy
         + do not merge divergent edits blindly
```

Migration must not leave both copies receiving autonomous writes.

## Acceptance tests per repo

- [ ] Git remote correct;
- [ ] branch correct;
- [ ] HEAD matches intended authority;
- [ ] all intentional untracked/local data accounted for;
- [ ] Windows Explorer opens canonical path;
- [ ] Git operation from WSL works;
- [ ] repo tests/build relevant to project work;
- [ ] Hermes project context loads correct `AGENTS.md`;
- [ ] QMD collection points to canonical path and retrieval benchmark passes;
- [ ] Docker disposable file persists to canonical host path;
- [ ] Docker disposable Git commit persists;
- [ ] unrelated host path denial test passes;
- [ ] Codex/Claude can operate on same checkout where enabled;
- [ ] no routine copy/sync step remains;
- [ ] old Windows copy is frozen, not automatically deleted.

## Known trade-off

Windows programs that repeatedly scan/edit many files through `\\wsl$` can themselves incur cross-filesystem overhead. Microsoft recommends keeping files with the OS/tooling that performs the heavy operations.

Our target selects WSL as canonical because the heavy operational stack is Linux-side:

```text
Hermes
QMD
Docker
Git/Node/Python build tools
Codex/Claude when operating this architecture
```

Occasional Windows Explorer/editor access remains supported.

## Primary sources

- Microsoft WSL filesystems: https://learn.microsoft.com/en-us/windows/wsl/filesystems
- Microsoft current WSL interop: https://learn.microsoft.com/en-us/windows/dev-environment/wsl-interop
- Docker WSL development: https://docs.docker.com/desktop/features/wsl/use-wsl/
- Docker WSL backend: https://docs.docker.com/desktop/features/wsl/
- Microsoft Dev Containers storage guidance: https://learn.microsoft.com/en-us/windows/dev-environment/docker/dev-containers
