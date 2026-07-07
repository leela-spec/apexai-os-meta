# Connector Detective Audit and Repair Plan — Apex KB v3 P0-P2 Closure

## Status

This report was prepared through the GitHub connector to reduce Codex/Agent token usage.

## Verified repo facts

```yaml
repo: leela-spec/apexai-os-meta
branch: main
bad_patch_commit: 0c747db41bc5028d815ae0321f76ace144244738
pre_patch_base: 554e767f94129afa6165ff30a347538a62e417c0
latest_checked_main: 9eb3ab39dbf529c46b4f3d79acb1eb3e32573660
```

## Verdict

```yaml
verdict: PARTIAL_FAIL
reason: >
  Codex applied manual equivalent changes because the patch files had abbreviated
  hunk headers and failed git apply --check. Some useful changes landed, but several
  intended P0-P2 closure items are currently marker-level or stub-level.
```

## Keep from current patch

```yaml
keep:
  - CLI flag normalization in apex_kb.py
  - CLI flag normalization in apex_kb_retrieval.py
  - --output-json support in both scripts
  - status freshness split: wiki_index_status, retrieval_index_status, source_payload_manifest_status
```

## Repair targets

```yaml
repair_targets:
  pointer_only_phase0:
    current: reports pointer-only fields but does not include resolved pointer files in phase0 scanning
    required: scan safe repo-local / kb-local resolved pointer text files or explicitly report unresolved pointers

  quality_coverage:
    current: source_to_page_map/page_to_source_map exist but are empty stubs
    required: populate maps by reading wiki page frontmatter source_refs and manifest sources

  shell_page_detection:
    current: shell_page_candidates always empty
    required: detect missing Phase 2 value headings, very low body density, empty source_refs, and weak source routing

  query_eval:
    current: query-eval --init returns fields but does not write or validate an eval pack
    required: create deterministic starter pack under outputs/queries/evals/query-eval-pack.json and validate existing pack shape

  graph_process_flow:
    current: graph/process-graph returns empty arrays
    required: extract deterministic markdown links, wikilinks, repo path references, and simple YAML/path/process edges

  docs:
    current: script-command-contract describes behavior more strongly than code implements
    required: update docs only after implementation behavior matches
```

## Commands the operator must run locally

The GitHub connector cannot execute Python, `git apply --check`, or inspect local PowerShell behavior. Run these locally:

```powershell
cd C:\GitDev\apexai-os-meta

git checkout main
git pull --ff-only origin main

python -m py_compile apex-meta/scripts/apex_kb.py
python -m py_compile apex-meta/scripts/apex_kb_retrieval.py

$KbRoot = "apex-meta/kb/claude-skill-design"
$OutDir = "log/post-codex-p0-p2-audit"
New-Item -ItemType Directory -Force -Path (Join-Path $KbRoot $OutDir) | Out-Null

python apex-meta/scripts/apex_kb.py --kb-root $KbRoot status --json --output-json "$OutDir/status-after-patch.json"
python apex-meta/scripts/apex_kb.py --kb-root $KbRoot quality --json --output-json "$OutDir/quality-after-patch.json"
python apex-meta/scripts/apex_kb.py --kb-root $KbRoot query-eval --init --json --output-json "$OutDir/query-eval-after-patch.json"
python apex-meta/scripts/apex_kb.py --kb-root $KbRoot graph --json --output-json "$OutDir/graph-after-patch.json"
python apex-meta/scripts/apex_kb_retrieval.py --kb-root $KbRoot stale --json --output-json "$OutDir/retrieval-stale-after-patch.json"

Get-Content "$KbRoot\$OutDir\quality-after-patch.json" -Raw
Get-Content "$KbRoot\$OutDir\query-eval-after-patch.json" -Raw
Get-Content "$KbRoot\$OutDir\graph-after-patch.json" -Raw
```

## Local original/current target retrieval

Run this if you want file snapshots for Agent Mode:

```powershell
cd C:\GitDev\apexai-os-meta

git checkout main
git pull --ff-only origin main

$Base = "554e767f94129afa6165ff30a347538a62e417c0"
$Patch = "0c747db41bc5028d815ae0321f76ace144244738"
$AuditRoot = "apex-meta\handoff\Apex-Kb_Lifecycle_Analysis\NextFinalization\post-codex-p0-p2-closure-audit"

$OriginalRoot = Join-Path $AuditRoot "original-targets-$($Base.Substring(0,8))"
$CurrentRoot  = Join-Path $AuditRoot "current-targets-main"
$PatchRoot    = Join-Path $AuditRoot "patched-targets-$($Patch.Substring(0,8))"
$DiffRoot     = Join-Path $AuditRoot "diffs"

New-Item -ItemType Directory -Force -Path $OriginalRoot | Out-Null
New-Item -ItemType Directory -Force -Path $CurrentRoot | Out-Null
New-Item -ItemType Directory -Force -Path $PatchRoot | Out-Null
New-Item -ItemType Directory -Force -Path $DiffRoot | Out-Null

$Targets = @(
  "apex-meta/scripts/apex_kb.py",
  "apex-meta/scripts/apex_kb_retrieval.py",
  ".claude/skills/apex-kb/references/script-command-contract.md"
)

foreach ($Target in $Targets) {
  $SafeName = $Target -replace "[/\\]", "__"
  $OriginalFile = Join-Path $OriginalRoot $SafeName
  $CurrentFile  = Join-Path $CurrentRoot $SafeName
  $PatchFile    = Join-Path $PatchRoot $SafeName

  git show "${Base}:${Target}" | Set-Content -LiteralPath $OriginalFile -Encoding utf8
  git show "HEAD:${Target}" | Set-Content -LiteralPath $CurrentFile -Encoding utf8
  git show "${Patch}:${Target}" | Set-Content -LiteralPath $PatchFile -Encoding utf8

  git diff --no-index $OriginalFile $CurrentFile | Set-Content -LiteralPath (Join-Path $DiffRoot "$SafeName.base-vs-current.diff") -Encoding utf8
  git diff --no-index $OriginalFile $PatchFile | Set-Content -LiteralPath (Join-Path $DiffRoot "$SafeName.base-vs-patchcommit.diff") -Encoding utf8
}

git diff --name-status $Base HEAD -- $Targets | Set-Content -LiteralPath (Join-Path $AuditRoot "changed-target-files.txt") -Encoding utf8
```

## Next Agent Mode instruction shape

Use Agent Mode only after the local audit outputs exist. The Agent should create a Git-native patch pack only. It must not manually apply equivalent changes, and it must fail if `git apply --check` fails.

```yaml
agent_mode_scope:
  job: create repair patch pack only
  source_of_truth:
    - live terminal Git repo
    - this audit report
    - local behavioral audit outputs
    - original/current target diffs
  patch_pack_root: apex-meta/patches/apex-kb-v3-p0-p2-closure-repair/
  target_files:
    - apex-meta/scripts/apex_kb.py
    - apex-meta/scripts/apex_kb_retrieval.py
    - .claude/skills/apex-kb/references/script-command-contract.md
    - .claude/skills/apex-kb/references/acceptance-tests.md
    - .claude/skills/apex-kb/examples/powershell-commands.md
  required_validation:
    - git apply --check every patch
    - cumulative git apply --check
    - py_compile both scripts
    - behavioral checks for quality, query-eval, graph, status
  forbidden:
    - manual equivalent edits claimed as patch success
    - abbreviated hunk headers
    - marker-only validation
    - touching apex-kb2
```
