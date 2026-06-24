Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$Root = (Resolve-Path (Join-Path $PSScriptRoot "../../..")).Path
$Out = Join-Path $Root "_verification/apex-kb-chatgpt-20260624"
$BackupRef = "origin/backup/apex-kb-before-chatgpt-20260624"
$Commits = @(
  "ac259b632f77d0836aef722b1b640392f623f24d",
  "96b21e861c738fd2ccb2eaa7abecf509a924a487",
  "daa8e25e1758192ffc9632e9629070a38d7c1d8d",
  "cc9f69ad44280615368877d6234bc3983d7fba54",
  "ae59348c953b9a946638c4bd25f1a1f013e2c064",
  "d5e9dd0eac2ec44797764a3558f5087ff62c503d",
  "84757a7b0498b76710c78bae0b1e25d48c2bfc48"
)
$AddedFiles = @(
  ".claude/skills/apex-kb/references/source-custody-and-read-verification.md",
  ".claude/skills/apex-kb/templates/source-intake-lock-template.md"
)
$ModifiedFiles = @(
  ".claude/skills/apex-kb/SKILL.md",
  ".claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md",
  ".claude/skills/apex-kb/templates/ingest-analysis-template.md",
  ".claude/skills/apex-kb/package-manifest.md",
  ".claude/skills/apex-kb/references/kb-contract.md"
)

function Invoke-Git {
  param([Parameter(ValueFromRemainingArguments = $true)][string[]]$Args)
  & git @Args
  if ($LASTEXITCODE -ne 0) {
    throw "git $($Args -join ' ') failed with exit code $LASTEXITCODE"
  }
}

Set-Location $Root

$Status = (& git status --short)
$BadStatus = $Status | Where-Object { $_ -and ($_ -notlike "?? _verification/*") -and ($_ -ne "?? _verification/") }
if ($BadStatus) {
  throw "Working tree is not clean except for _verification/: $($BadStatus -join '; ')"
}

Invoke-Git rev-parse $BackupRef | Out-Null
foreach ($Commit in $Commits) {
  $Type = (& git cat-file -t $Commit)
  if ($LASTEXITCODE -ne 0 -or $Type.Trim() -ne "commit") {
    throw "Expected commit is missing: $Commit"
  }
}

$Dirs = @("before", "after", "diffs", "reports", "scripts")
foreach ($Dir in $Dirs) {
  New-Item -ItemType Directory -Force -Path (Join-Path $Out $Dir) | Out-Null
}

$Readme = @"
# Apex KB ChatGPT Edit Verification

This folder records deterministic verification material for the accidental Apex KB ChatGPT edits from 2026-06-24.

Backup branch: `$BackupRef`

Audited commits:
$($Commits | ForEach-Object { "- $_" } | Out-String)
Touched files:
$($AddedFiles + $ModifiedFiles | ForEach-Object { "- $_" } | Out-String)
Safe next actions:
- Review files under `diffs/` and reports under `reports/`.
- Compare `before/` and `after/` with `git diff --no-index`.
- Decide whether to keep, revert, or branch from `$BackupRef`.

Unsafe next actions:
- Do not continue Apex KB design/update work until the operator decides.
- Do not modify `.claude/skills/apex-kb/` as part of this verification.
- Do not run ingestion for this verification task.

If a user stash needs restoration later, inspect it first with `git stash list` and `git stash show --stat <stash>`, then restore only after operator approval. This script does not restore stashes.
"@
Set-Content -Path (Join-Path $Out "README.md") -Value $Readme -Encoding UTF8

$Verify = @"
# Verification Checklist

1. Check local status:
   ````powershell
   git status --short
   ````
   Expected: only `_verification/` changes before commit, or clean after archival.

2. Check backup branch:
   ````powershell
   git rev-parse $BackupRef
   ````
   Expected: resolves to a commit SHA.

3. Inspect each audited commit:
$($Commits | ForEach-Object { "   ````powershell`n   git show --name-status --oneline --no-renames $_`n   ````" } | Out-String)
   Expected: combined changed file set is exactly the seven Apex KB files in `changed-files-ledger.json`.

4. Compare exported before/after files:
   ````powershell
   git diff --no-index before/<path> after/<path>
   ````
   Expected: differences match the generated files in `diffs/`.
"@
Set-Content -Path (Join-Path $Out "VERIFY.md") -Value $Verify -Encoding UTF8

$LedgerLines = @("# ChatGPT Commit Ledger", "")
foreach ($Commit in $Commits) {
  $Subject = (& git show -s --format="%H%n%h%n%s%n%aI" $Commit)
  $LedgerLines += "## $($Subject[1])"
  $LedgerLines += ""
  $LedgerLines += "- Commit: $($Subject[0])"
  $LedgerLines += "- Subject: $($Subject[2])"
  $LedgerLines += "- Author date: $($Subject[3])"
  $LedgerLines += ""
  $LedgerLines += "### Changed Files"
  $LedgerLines += '```text'
  $LedgerLines += (& git show --name-status --format= --no-renames $Commit)
  $LedgerLines += '```'
  $LedgerLines += ""
  $LedgerLines += "### Stat"
  $LedgerLines += '```text'
  $LedgerLines += (& git show --stat --oneline --no-renames $Commit)
  $LedgerLines += '```'
  $LedgerLines += ""
}
Set-Content -Path (Join-Path $Out "chatgpt-commit-ledger.md") -Value $LedgerLines -Encoding UTF8

foreach ($Rel in $ModifiedFiles) {
  $Before = Join-Path (Join-Path $Out "before") $Rel
  $After = Join-Path (Join-Path $Out "after") $Rel
  New-Item -ItemType Directory -Force -Path (Split-Path $Before -Parent) | Out-Null
  New-Item -ItemType Directory -Force -Path (Split-Path $After -Parent) | Out-Null
  & git show "$BackupRef`:$Rel" | Set-Content -Path $Before -Encoding UTF8
  Copy-Item -LiteralPath (Join-Path $Root $Rel) -Destination $After -Force
}

$DiffMap = @{
  "SKILL.md" = ".claude/skills/apex-kb/SKILL.md"
  "ingest-query-lint-audit-rules.md" = ".claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md"
  "ingest-analysis-template.md" = ".claude/skills/apex-kb/templates/ingest-analysis-template.md"
  "package-manifest.md" = ".claude/skills/apex-kb/package-manifest.md"
  "kb-contract.md" = ".claude/skills/apex-kb/references/kb-contract.md"
}
foreach ($Name in $DiffMap.Keys) {
  $Rel = $DiffMap[$Name]
  $Before = Join-Path (Join-Path $Out "before") $Rel
  $After = Join-Path (Join-Path $Out "after") $Rel
  & git diff --no-index $Before $After *> (Join-Path (Join-Path $Out "diffs") "$Name.diff")
  if ($LASTEXITCODE -gt 1) {
    throw "git diff --no-index failed for $Rel with exit code $LASTEXITCODE"
  }
}
& git diff --no-index (Join-Path $Out "before") (Join-Path $Out "after") *> (Join-Path (Join-Path $Out "diffs") "combined.diff")
if ($LASTEXITCODE -gt 1) {
  throw "combined git diff --no-index failed with exit code $LASTEXITCODE"
}

python (Join-Path $Out "scripts/create_apex_kb_verification.py")
if ($LASTEXITCODE -ne 0) {
  throw "Python helper failed with exit code $LASTEXITCODE"
}

$Ledger = Get-Content (Join-Path $Out "changed-files-ledger.json") -Raw | ConvertFrom-Json
$DiffCount = (Get-ChildItem (Join-Path $Out "diffs") -File).Count
$BeforeCount = (Get-ChildItem (Join-Path $Out "before") -Recurse -File).Count
$AfterCount = (Get-ChildItem (Join-Path $Out "after") -Recurse -File).Count
$Warnings = @()
if ($Status) { $Warnings += "Working tree had existing _verification changes before generation." }
if ($Ledger.verification_status -ne "pass") { $Warnings += "Touched file verification failed." }

$StatusReport = @"
# Status Report

- Backup branch status: present ($BackupRef -> $($Ledger.backup_commit))
- Local working tree status: only `_verification/` changes allowed
- Touched file set matches expected: $($Ledger.verification_status)
- Before exports created: $BeforeCount of 5
- After exports created: $AfterCount of 5
- Diff files created: $DiffCount of 6
- Added files confirmed as new: see reports/added-files-report.md
- Warnings: $(if ($Warnings.Count) { $Warnings -join "; " } else { "none" })

Recommended next action:

Review the generated diffs manually. Do not continue Apex KB design/update work until the operator decides whether to revert, keep, or branch from backup.
"@
Set-Content -Path (Join-Path $Out "reports/status-report.md") -Value $StatusReport -Encoding UTF8

Write-Host "Verification generation complete."
Write-Host "Status: $($Ledger.verification_status)"
Write-Host "Output: $Out"
