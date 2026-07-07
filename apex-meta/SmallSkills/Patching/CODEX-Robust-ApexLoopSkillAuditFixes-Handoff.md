# Codex Handoff: Robust Apply of Apex Loop Skill Audit Fixes Patch Pack

## Operator Intent

Repair and apply the Apex loop-skill audit fixes patch pack deterministically.

Repository:

```text
C:\GitDev\apexai-os-meta
```

Downloaded patch pack:

```text
C:\Users\gehm7\Downloads\apex-loop-skill-audit-fixes-patch-pack\patches\apex-loop-skill-audit-fixes
```

Repo-local patch artifact destination:

```text
apex-meta\patches\apex-loop-skill-audit-fixes
```

## Why This Handoff Exists

The downloaded patch files are not Git-generated, blob-anchored diffs. They lack `diff --git` and `index <old>..<new>` headers, and the pack's own validation says full `git apply --check` was not run against a real clone.

Therefore Codex must not assume plain `git apply` will work.

## Execute

First run repair/check only:

```powershell
Set-Location C:\GitDev\apexai-os-meta

python apex-meta\SmallSkills\Patching\apply_apex_loop_skill_audit_fixes_robust.py `
  --repo-root C:\GitDev\apexai-os-meta `
  --download-patch-dir C:\Users\gehm7\Downloads\apex-loop-skill-audit-fixes-patch-pack\patches\apex-loop-skill-audit-fixes `
  --repo-patch-dir apex-meta\patches\apex-loop-skill-audit-fixes `
  --repair
```

Only after that reports `FINAL_REPORT: verdict: PASS`, run final apply:

```powershell
Set-Location C:\GitDev\apexai-os-meta

python apex-meta\SmallSkills\Patching\apply_apex_loop_skill_audit_fixes_robust.py `
  --repo-root C:\GitDev\apexai-os-meta `
  --download-patch-dir C:\Users\gehm7\Downloads\apex-loop-skill-audit-fixes-patch-pack\patches\apex-loop-skill-audit-fixes `
  --repo-patch-dir apex-meta\patches\apex-loop-skill-audit-fixes `
  --repair `
  --apply
```

Commit and push only if the operator explicitly asks for that run:

```powershell
python apex-meta\SmallSkills\Patching\apply_apex_loop_skill_audit_fixes_robust.py `
  --repo-root C:\GitDev\apexai-os-meta `
  --download-patch-dir C:\Users\gehm7\Downloads\apex-loop-skill-audit-fixes-patch-pack\patches\apex-loop-skill-audit-fixes `
  --repo-patch-dir apex-meta\patches\apex-loop-skill-audit-fixes `
  --repair `
  --apply `
  --commit `
  --push
```

## Expected Targets

The script reads these from `000-patch-manifest.md`:

```text
.claude/Claude.md
.claude/skills/raw-flow-dump-normalize/package-manifest.md
.claude/skills/flow-recap/package-manifest.md
.claude/skills/flow-recap/references/flow-recap-packet-contract.md
.claude/skills/flow-recap/examples/apex-minimal-flow-recap-example.md
.claude/skills/model-usage-log/package-manifest.md
.claude/skills/model-usage-log/references/model-usage-delta-contract.md
.claude/skills/status-merge/package-manifest.md
.claude/skills/status-merge/SKILL.md
.claude/skills/status-merge/references/status-merge-packet-contract.md
.claude/skills/status-merge/references/next-precaphandoff-context-contract.md
.claude/skills/status-merge/examples/apex-minimal-status-merge-example.md
```

## Safety Rules

- Do not use `git apply --reject`.
- Do not use `patch -p1`.
- Do not manually edit final target files as the final state.
- Do not spend a long live execution repairing one patch after another inside the final apply path.
- If repair is needed, repair patch artifacts first and prove the full repaired pack with `git apply --check`.
- Dirty unrelated files may exist, but dirty patch targets must stop the run.
- Repair only patch artifacts in the repo-local patch directory.
- Final target edits must come from `git apply` after repaired patches pass `git apply --check`.

## Success Criteria

```yaml
success:
  patch_pack_copied_to_repo: true
  dirty_target_overlap: none
  repair_phase_completed_before_final_apply: PASS
  repaired_patches_git_apply_check: PASS
  repaired_patches_git_apply: PASS
  changed_files_subset_of_manifest_targets: PASS
  commit: optional
  push: optional
```

## Failure Report Format

```yaml
FINAL_REPORT:
  verdict: FAIL
  failed_step: "<exact step>"
  reason: "<exact reason>"
  pushed: false
```
