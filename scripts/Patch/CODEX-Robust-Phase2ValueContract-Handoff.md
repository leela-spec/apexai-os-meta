# Codex Handoff - Robust Apply of Apex KB Phase 2 Value Contract Patch Pack

## 0. Operator intent

Apply the already-extracted Phase 2 value-contract patch pack to the local repository.

Use deterministic tools first. Do not rely on Codex patch editing. Codex is the terminal executor and failure reporter.

Repository:

```text
C:\GitDev\apexai-os-meta
```

Patch pack:

```text
C:\GitDev\apexai-os-meta\apex-meta\handoff\Apex-Kb_Lifecycle_Analysis\phase2-value-contract
```

Branch:

```text
main
```

## 1. Files to place first

Place these two files exactly:

```text
scripts\apply_phase2_value_contract_robust.py
scripts\Apply-Phase2ValueContract-Robust.ps1
```

Do not edit the nine Apex KB target files manually before running the script.

## 2. Execute exactly

```powershell
Set-Location C:\GitDev\apexai-os-meta

powershell -NoProfile -ExecutionPolicy Bypass -File scripts\Apply-Phase2ValueContract-Robust.ps1 `
  -RepoRoot C:\GitDev\apexai-os-meta `
  -PatchDir apex-meta\handoff\Apex-Kb_Lifecycle_Analysis\phase2-value-contract
```

## 3. Expected fast-path behavior

The script should:

1. verify `origin` ends in `leela-spec/apexai-os-meta`
2. check out `main`
3. pull `origin main` with `--ff-only`
4. stop if the worktree is dirty
5. parse each patch and verify it touches exactly one expected target file
6. compare each patch old blob prefix with the current Git blob hash
7. try `git apply --check`
8. try `git apply`
9. verify only the nine expected target files changed
10. verify required value-contract strings
11. verify forbidden strings are absent
12. commit with:

```text
Strengthen Apex KB Phase 2 value contract
```

13. push `origin main`

## 4. Built-in fallback behavior

If normal `git apply` fails, the script automatically tries:

```text
git apply --whitespace=nowarn --recount
git apply --ignore-space-change --ignore-whitespace --whitespace=nowarn --recount
git apply --3way --whitespace=nowarn --recount
```

If all Git apply modes fail, the script resets the worktree and applies the unified-diff hunks with its own deterministic Python hunk matcher:

```text
fallback strategy:
  - parse diff headers
  - parse index old/new blob IDs
  - parse hunk headers and validate hunk line counts
  - locate old hunk blocks by exact expected line
  - if needed, search near expected location
  - if needed, search entire file
  - if needed, repeat with whitespace-normalized matching
  - if new hunk block is already present, treat the hunk as already applied
  - write backups under .phase2-value-contract-backups/
```

## 5. Failure-mode instructions for Codex

### 5.1 Dirty tree before start

If the script fails because the tree is dirty:

```powershell
git status --short
```

Then stop and report the dirty files. Do not stash, reset, or delete files unless the operator explicitly approves.

### 5.2 Missing patch directory

Check whether the operator extracted the files here:

```text
apex-meta\handoff\Apex-Kb_Lifecycle_Analysis\phase2-value-contract
```

If the folder is absent, stop and report. Do not search unrelated directories except:

```text
apex-meta\patches\phase2-value-contract
```

### 5.3 Patch target mismatch

If the script says a patch target differs from the expected target, stop. Do not reinterpret the patch. Report the exact diff header and expected target.

### 5.4 Old blob mismatch

If old blob hashes mismatch, do not panic. The script will still attempt apply/fallback.

But before any manual repair, run:

```powershell
git hash-object -- .claude/skills/apex-kb/templates/wiki-page-templates.md
git hash-object -- .claude/skills/apex-kb/templates/ingest-analysis-template.md
git hash-object -- .claude/skills/apex-kb/references/kb-contract.md
git hash-object -- .claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md
git hash-object -- .claude/skills/apex-kb/references/acceptance-tests.md
git hash-object -- .claude/skills/apex-kb/SKILL.md
git hash-object -- .claude/skills/apex-kb/references/lifecycle-state-machine.md
git hash-object -- .claude/skills/apex-kb/references/knowledge-promotion-rules.md
git hash-object -- .claude/skills/apex-kb/templates/kb-schema-template.md
```

Then report the mismatch table.

### 5.5 `git apply` fails but fallback succeeds

This is acceptable. The script's final verification is the authority:

```text
FINAL_REPORT:
  verdict: PASS
```

Do not rerun with manual patch edits.

### 5.6 `git apply` and fallback both fail

Do not start broad reasoning.

Run this diagnostic set only:

```powershell
git status --short
git diff --name-only

git apply --stat apex-meta\handoff\Apex-Kb_Lifecycle_Analysis\phase2-value-contract\001-wiki-page-templates.patch
git apply --check --verbose apex-meta\handoff\Apex-Kb_Lifecycle_Analysis\phase2-value-contract\001-wiki-page-templates.patch
```

Then repeat `git apply --check --verbose` only for the failed patch named by the script.

Stop and report:
- failed patch name
- failed target file
- exact hunk header
- exact terminal error
- `git status --short`

### 5.7 Use of `git apply --reject`

Only use `--reject` in a disposable scratch copy if the operator explicitly asks for manual diagnosis. Do not run `--reject` in the final worktree, because it creates partial files and `.rej` artifacts.

### 5.8 Manual repair rule

Manual repair is allowed only after all deterministic paths fail.

If forced to repair manually:
1. modify only the single target file named by the failed patch
2. make the smallest local edit matching the added/removed lines from that patch
3. run the script again with `-ForceFallback`
4. verify the final changed-file scope is exactly the nine target files
5. do not modify `apex-meta/scripts/`
6. do not modify any `apex-meta/kb/*/wiki/`
7. do not modify `.claude/skills/apex-kb2/`

## 6. Final report format

Return exactly:

```yaml
FINAL_REPORT:
  verdict: PASS | FAIL
  repo: leela-spec/apexai-os-meta
  branch: main
  pushed: true | false
  script_used:
    - scripts/apply_phase2_value_contract_robust.py
    - scripts/Apply-Phase2ValueContract-Robust.ps1
  apply_mode: plain_git_apply | ignore_space_git_apply | three_way_git_apply | python_hunk_fallback | failed
  changed_files:
    - .claude/skills/apex-kb/templates/wiki-page-templates.md
    - .claude/skills/apex-kb/templates/ingest-analysis-template.md
    - .claude/skills/apex-kb/references/kb-contract.md
    - .claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md
    - .claude/skills/apex-kb/references/acceptance-tests.md
    - .claude/skills/apex-kb/SKILL.md
    - .claude/skills/apex-kb/references/lifecycle-state-machine.md
    - .claude/skills/apex-kb/references/knowledge-promotion-rules.md
    - .claude/skills/apex-kb/templates/kb-schema-template.md
  validation:
    target_scope_only: pass | fail
    required_strings_present: pass | fail
    forbidden_strings_absent: pass | fail
    final_git_status_clean: pass | fail
  failure_reason: null | <exact reason>
```
