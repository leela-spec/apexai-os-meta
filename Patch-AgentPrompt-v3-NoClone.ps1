# Patch-AgentPrompt-v3-NoClone.ps1
# Purpose: surgically replace the bad clone/patchwork setup block in AgentPrompt_v3_PATCHED.md.
# Scope: one block only. No target lists, patch lists, validation logic, or final report schema are changed.

$ErrorActionPreference = "Stop"

$Path = "C:\GitDev\apexai-os-meta\apex-meta\handoff\WeklyFlow\AgentPrompt_v3_PATCHED.md"

if (-not (Test-Path -LiteralPath $Path)) {
  throw "File not found: $Path"
}

$text = Get-Content -LiteralPath $Path -Raw -Encoding UTF8

$startMarker = "MANDATORY REAL REPO SETUP — DO THIS FIRST"
$endMarker = "Primary source plan to read first:"

$start = $text.IndexOf($startMarker)
$end = $text.IndexOf($endMarker)

if ($start -lt 0) {
  throw "Start marker not found. Refusing to patch because the expected clone setup block is not present."
}
if ($end -lt 0 -or $end -le $start) {
  throw "End marker not found after start marker. Refusing to patch."
}

$oldBlock = $text.Substring($start, $end - $start)

# Guard: confirm this is the known bad block, not an unknown prompt version.
$requiredOldFragments = @(
  "Start by opening or cloning the real repository:",
  "git clone https://github.com/leela-spec/apexai-os-meta.git apexai-os-meta",
  "cd /home/oai/share",
  "real cloned repo"
)

foreach ($fragment in $requiredOldFragments) {
  if ($oldBlock -notlike "*$fragment*") {
    throw "Expected old fragment not found in block: $fragment. Refusing to patch."
  }
}

$newBlock = @'
MANDATORY START DIRECTORY

This prompt must be run from inside the existing local Git checkout:

  C:\GitDev\apexai-os-meta

Do not clone the repository.
Do not run git init.
Do not create or use /home/oai/share/patchwork.
Do not create a substitute local repository.
Do not reconstruct files from GitHub API snippets.
Do not create placeholder target files.

First run:

  pwd
  git rev-parse --show-toplevel
  git rev-parse --is-inside-work-tree
  git remote get-url origin
  git branch --show-current
  git status --porcelain

The git root must be the existing apexai-os-meta checkout.
The origin must point to leela-spec/apexai-os-meta.
The source plan must exist at:

  apex-meta/patch-plans/2026-07-07-step1-prompt-blocker-cleanup-plan.okf.md

If any of these checks fail:

  FINAL_REPORT:
    verdict: FAIL
    failed_step: repo_preflight
    reason: "Prompt was not run from inside the existing apexai-os-meta Git checkout."
    patch_generation_started: false
    patch_files_created: []

Do not clone.
Do not enter fallback archive mode.
Do not generate patches.

'@

$before = $text.Substring(0, $start)
$after = $text.Substring($end)
$newText = $before + $newBlock + $after

# Drift guards: the patch must remove clone behavior and preserve the real task structure.
$forbiddenAfter = @(
  "git clone https://github.com/leela-spec/apexai-os-meta.git apexai-os-meta",
  "Start by opening or cloning the real repository:",
  "cd /home/oai/share"
)

foreach ($fragment in $forbiddenAfter) {
  if ($newText -like "*$fragment*") {
    throw "Forbidden clone/setup fragment still present after patch: $fragment"
  }
}

$requiredAfter = @(
  "MANDATORY START DIRECTORY",
  "C:\GitDev\apexai-os-meta",
  "Do not clone the repository.",
  "Do not enter fallback archive mode.",
  "Primary source plan to read first:",
  "Target files for patch generation:",
  "PER-PATCH CHECKPOINT PROCEDURE",
  "FINAL REPORT FORMAT"
)

foreach ($fragment in $requiredAfter) {
  if ($newText -notlike "*$fragment*") {
    throw "Required prompt fragment missing after patch: $fragment"
  }
}

# Structural guards copied from the working-prompt pattern: explicit targets + explicit patch artifacts remain present.
$targetCount = ([regex]::Matches($newText, "target_file:")).Count
if ($targetCount -ne 22) {
  throw "Expected 22 target_file entries, found $targetCount. Refusing to write."
}

$patchEntryCount = ([regex]::Matches($newText, "patch_file:")).Count
if ($patchEntryCount -ne 22) {
  throw "Expected 22 patch_file entries in target map, found $patchEntryCount. Refusing to write."
}

# Create backup, then write patched prompt.
$backup = "$Path.bak-before-no-clone-patch"
Copy-Item -LiteralPath $Path -Destination $backup -Force
Set-Content -LiteralPath $Path -Value $newText -NoNewline -Encoding UTF8

Write-Host "PASS: patched $Path"
Write-Host "Backup: $backup"
Write-Host "Changed exactly one block: '$startMarker' -> before '$endMarker'"
Write-Host "Target entries preserved: $targetCount"
Write-Host "Patch entries preserved: $patchEntryCount"
