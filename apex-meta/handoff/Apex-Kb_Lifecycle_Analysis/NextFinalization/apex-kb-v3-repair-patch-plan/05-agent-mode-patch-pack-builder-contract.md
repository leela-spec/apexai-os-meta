# Agent Mode Patch-Pack Builder Contract

## 1. Role

```yaml
agent_mode_role:
  role: "Git-native patch-pack builder"
  patch_pack_root: "apex-meta/patches/apex-kb-v3-repair/"
  branch: main
````

## 2. Must

```yaml
must:
  - "operate inside a real terminal Git worktree"
  - "use live main as source of truth"
  - "read target files from the worktree, not from connector reconstruction"
  - "create one Git-generated patch per target file or one cumulative Git-generated patch for apex_kb.py if required for apply stability"
  - "validate every patch with git apply --check"
  - "validate cumulative patch application"
  - "run py_compile on changed Python scripts during temporary cumulative application"
  - "run smoke behavior checks for repaired features during temporary cumulative application"
  - "revert target files after patch generation"
  - "leave final repo state with patch artifacts only"
```

## 3. Must not

```yaml
must_not:
  - "directly apply final target-file changes"
  - "manually apply failed patches"
  - "create synthetic repo files from API snippets"
  - "use abbreviated hunk headers"
  - "hand-edit hunk headers"
  - "self-report pass if git apply --check fails"
  - "use marker-only implementation"
  - "use the invalid apex-kb-v3-p0-p2-closure patch files as implementation source"
```

## 4. Preflight

```yaml
preflight_commands:
  - "git rev-parse --show-toplevel"
  - "git rev-parse --is-inside-work-tree"
  - "git remote get-url origin"
  - "git branch --show-current"
  - "git status --porcelain"
  - "git checkout main"
  - "git pull --ff-only origin main"

hard_stop_if:
  - "not a Git worktree"
  - "target files unreadable"
  - "source plan package unreadable"
  - "git unavailable"
```

## 5. Dirty tree policy

```yaml
dirty_tree_policy:
  block_if_dirty_overlaps:
    - "target files"
    - "apex-meta/patches/apex-kb-v3-repair/"
    - "forbidden paths"
  allow_if_dirty_unrelated: true
  requirement: "report unrelated dirty files and leave them untouched"
```

## 6. Per-target patch loop

```yaml
per_target_loop:
  - "git checkout -- <target-file>"
  - "verify target file clean"
  - "modify only that target file"
  - "git diff --no-ext-diff -- <target-file> > <patch-file>"
  - "test -s <patch-file>"
  - "verify exactly one diff --git header unless cumulative apex_kb.py patch is intentionally one target-file patch"
  - "git checkout -- <target-file>"
  - "git apply --check <patch-file>"
  - "git apply <patch-file>"
  - "verify only intended target file changed"
  - "run relevant smoke checks"
  - "git checkout -- <target-file>"
  - "verify target file clean"
```

## 7. Final artifact set

```yaml
required_artifacts:
  - "000-patch-manifest.md"
  - "NNN-*.patch"
  - "validation-report.md"
  - "999-codex-apply-handoff.md"
  - "patch-plan-source-ledger.md"
```
