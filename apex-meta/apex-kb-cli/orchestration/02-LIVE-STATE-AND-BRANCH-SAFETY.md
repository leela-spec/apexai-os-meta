# Live state and branch safety

## Canonical implementation surface

All continuation work must use:

```yaml
repository: leela-spec/apexai-os-meta
branch: codex/apex-kb-cli-phase0-integration
phase0_integration_commit: 93c6b5342c48fb1dd97688f47eeb3f3b24450677
package_root: apex-meta/apex-kb-cli
```

The branch is a direct descendant of `main` at `8d29bfa40f092ffaa24b3ae619a584ee76334986`. It contains the 21-commit CLI line plus the selected Phase 0 Start-contract integration.

The orchestration files added after `93c6b534...` are coordination documents only. Every worker must record the exact branch HEAD it evaluated.

## Known repository confusion

The patch execution report established:

| Path | Classification | Rule |
|---|---|---|
| `C:\GitDev\akb-ready` | Independent clone containing the pushed integration branch and Phase 0 patch | The only known valid local execution clone from the report |
| `C:\GitDev\apexai-os-meta` | Main checkout; CLI package was absent when the patch was attempted | Do not assume it contains the integration branch or package |
| `C:\GitDev\apexai-os-meta-apex-kb-cli-ready` | Separate clone with 49,358 staged deletions | Quarantine; never touch |
| release-candidate prepared folders | Historical donor/preparation surfaces | Do not treat as implementation truth |

A worker may use another path only after proving with commands that it is the same repository, exact locked branch, and expected commit.

## Required startup probe for every execution or patch task

Run read-only commands first:

```powershell
$repo = "<explicit-local-repository-path>"
git -C $repo rev-parse --show-toplevel
git -C $repo remote get-url origin
git -C $repo branch --show-current
git -C $repo rev-parse HEAD
git -C $repo status --short --branch
git -C $repo worktree list --porcelain
```

Verify all of these:

- remote resolves to `leela-spec/apexai-os-meta`;
- branch is exactly the branch named in the task;
- HEAD equals the task's expected starting commit or a stated descendant;
- package root exists at `apex-meta/apex-kb-cli`;
- unrelated tracked, staged, and untracked changes are enumerated before writes;
- the path is not the quarantined deletion-heavy clone.

Stop with `WRONG_REPOSITORY_SURFACE` when any check fails. Never repair the mismatch automatically.

## Write safety

### Always

- stage explicit allowlisted paths only;
- display `git diff --cached --name-status` before commit;
- compare the staged path set with the task allowlist;
- run `git diff --check`;
- record the commit SHA and changed paths;
- push only the named task branch;
- preserve unrelated changes and temporary artifacts.

### Never

- `git add -A` or `git add .` in a mixed tree;
- `git reset --hard`;
- `git clean`;
- silent `git stash`;
- force push;
- delete unknown files;
- move work between clones by copying entire trees;
- create a new worktree or clone without explicit operator approval;
- merge or fast-forward `main` without a separate explicit operator instruction;
- interpret absence of a file on `main` as absence on the locked integration branch.

## Branch strategy

The orchestrator assigns one branch per approved implementation iteration:

```text
codex/apex-kb-cli-<bounded-outcome>
```

The new branch must start from the current canonical integration branch HEAD. Research tasks do not create branches. Patch-author tasks do not apply changes. Execution tasks may create and push the approved iteration branch only after startup validation.

## Pull and reconciliation safety for the final product

The planned Apex KB semantic workflow must not perform an uncontrolled pull. The implementation should eventually provide or generate a bounded procedure that:

1. records local HEAD and dirty state;
2. fetches the named remote branch;
3. verifies the expected semantic commit exists and descends from the recorded base;
4. refuses divergence or unexpected changed paths;
5. fast-forwards only a clean or explicitly approved local branch;
6. validates the expected semantic artifacts after the fast-forward;
7. records the imported commit in run evidence;
8. generates the next exact prompt or deterministic action.

This Git round trip is part of the product target, not permission for orchestration workers to mutate branches casually.

## Authority order

When sources conflict, use this order:

1. explicit operator decisions in this orchestration folder;
2. live files on the locked integration branch;
3. selected final workflow contracts and templates;
4. executed canary/test evidence;
5. older research and historical implementations;
6. chat summaries and model memory.

Historical files remain evidence. They do not override the live branch or selected decisions merely because they contain words such as `final`, `canonical`, or `complete`.
