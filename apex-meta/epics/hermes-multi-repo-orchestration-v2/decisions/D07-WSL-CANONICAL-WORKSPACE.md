# D07 Appendix — Canonical WSL Workspace

**Decision status:** ACCEPTED / MIGRATION NOT AUTHORIZED  
**Decision ledger:** `../DECISIONS.md`  
**Primary subject file:** `../09-WSL-CANONICAL-WORKSPACE-MIGRATION-PLAN.md`

## Decision

Converge each managed repository to one canonical WSL-native checkout under a common workspace root such as:

```text
~/workspaces/
  apexai-os-meta/
  MasterOfArts/
  acim-secular/
  Investment/
```

Windows accesses the same files through WSL interop. Do not maintain Windows and WSL copies as parallel live sources of truth.

## Forces

- Hermes, QMD, Docker, Git and Linux-oriented AI tooling perform their heavy repo work on the Linux side;
- Microsoft recommends storing Linux-tool workloads in the WSL filesystem;
- Docker recommends source in the Linux distribution for Linux-container development;
- duplicate live checkouts create divergence/synchronization ambiguity;
- operator still needs normal Windows access.

## Verified reasoning

Microsoft documents the WSL filesystem as the recommended location when Linux tools operate on the project and documents cross-filesystem `/mnt/c` access as slower for Git/build-heavy workloads. Docker independently recommends Linux-distribution storage for WSL2 Linux-container development. Windows can browse WSL files through `\\wsl.localhost`.

## Migration law

```text
inventory
 -> compare Windows/WSL HEAD + dirty/untracked/ignored state
 -> reconcile deliberately
 -> verify canonical WSL repo
 -> repoint Hermes/QMD/Docker/client tools
 -> acceptance test
 -> freeze old copy
 -> delete only later with explicit approval
```

## Risks

- Windows and WSL copies may already have divergent uncommitted data;
- Windows applications doing heavy recursive scans over `\\wsl.localhost` can incur interop cost;
- file permissions/case sensitivity may expose assumptions hidden by NTFS;
- migrating secrets/ignored files without inventory can lose local-only state.

## Shortcomings

- Windows paths change for tools/bookmarks currently tied to `C:\GitDev`;
- some Windows-only workflows may need reconfiguration;
- migration requires repo-by-repo care rather than a single bulk move.

## Rejected alternatives

1. **Keep two live copies and sync them** — rejected: dual-authority and conflict risk.
2. **Use only `/mnt/c/GitDev` for Linux-heavy tools** — rejected as the default because it keeps cross-filesystem overhead in the critical path.
3. **Delete Windows copies immediately** — rejected: no safe rollback/divergence audit.

## Implementation consequence

Migrate one repo at a time. Apex/Investment/ACIM/MasterOfArts must each have an explicit inventory and acceptance result before the old copy is frozen.

## Watch / revisit conditions

Revisit a repo's placement only if a measured Windows-only workload performs materially worse through WSL interop than the Linux-heavy workflow gains.

## Evidence links

- Microsoft WSL filesystem guidance: https://learn.microsoft.com/en-us/windows/wsl/filesystems
- Microsoft WSL interop: https://learn.microsoft.com/en-us/windows/dev-environment/wsl-interop
- Docker WSL guidance: https://docs.docker.com/desktop/features/wsl/use-wsl/
- Migration plan: `../09-WSL-CANONICAL-WORKSPACE-MIGRATION-PLAN.md`
