param(
  [string]$RepoRoot = "C:\GitDev\apexai-os-meta",
  [string]$AllowlistPath = "apex-meta/kb/claude-skill-design/manifests/large-corpus-prework-projectrepos/curated-import-allowlist.json",
  [string]$SourceRoot = "source-knowledge/ProjectRepos",
  [string]$DestinationRoot = "apex-meta/kb/claude-skill-design/sources/curated/high-impact-repos",
  [string]$ReportMarkdown = "apex-meta/kb/claude-skill-design/manifests/high-impact-repo-import-report.md",
  [string]$ReportJson = "apex-meta/kb/claude-skill-design/manifests/high-impact-repo-import-report.json",
  [switch]$IncludeMaybeLater,
  [switch]$WhatIfOnly
)

$ErrorActionPreference = "Stop"

function Resolve-InRepoPath {
  param([string]$Base, [string]$Child)
  return [System.IO.Path]::GetFullPath((Join-Path $Base $Child))
}

$repoRootFull = [System.IO.Path]::GetFullPath($RepoRoot)
$allowlistFull = Resolve-InRepoPath $repoRootFull $AllowlistPath
$sourceRootFull = Resolve-InRepoPath $repoRootFull $SourceRoot
$destinationRootFull = Resolve-InRepoPath $repoRootFull $DestinationRoot
$reportMarkdownFull = Resolve-InRepoPath $repoRootFull $ReportMarkdown
$reportJsonFull = Resolve-InRepoPath $repoRootFull $ReportJson

if (-not (Test-Path -LiteralPath $allowlistFull -PathType Leaf)) {
  throw "Allowlist not found: $allowlistFull"
}
if (-not (Test-Path -LiteralPath $sourceRootFull -PathType Container)) {
  throw "Source root not found: $sourceRootFull"
}

$allowlist = Get-Content -LiteralPath $allowlistFull -Raw | ConvertFrom-Json
$selected = @()
$selected += @($allowlist.include_first | ForEach-Object {
  $_ | Add-Member -NotePropertyName selection_group -NotePropertyValue "include_first" -Force
  $_
})
if ($IncludeMaybeLater) {
  $selected += @($allowlist.maybe_later | ForEach-Object {
    $_ | Add-Member -NotePropertyName selection_group -NotePropertyValue "maybe_later" -Force
    $_
  })
}

$validationErrors = @()
$planned = @()
foreach ($item in $selected) {
  $sourcePath = [string]$item.source_path
  if ([string]::IsNullOrWhiteSpace($sourcePath) -or $sourcePath.Contains("*") -or $sourcePath.EndsWith("/") -or $sourcePath.EndsWith("\")) {
    $validationErrors += "Not a single file path: $sourcePath"
    continue
  }

  $src = Resolve-InRepoPath $sourceRootFull $sourcePath
  if (-not $src.StartsWith($sourceRootFull, [System.StringComparison]::OrdinalIgnoreCase)) {
    $validationErrors += "Source escapes source root: $sourcePath"
    continue
  }
  if (-not (Test-Path -LiteralPath $src -PathType Leaf)) {
    $validationErrors += "Source is missing or not a file: $sourcePath"
    continue
  }

  $dest = Resolve-InRepoPath $destinationRootFull $sourcePath
  if (-not $dest.StartsWith($destinationRootFull, [System.StringComparison]::OrdinalIgnoreCase)) {
    $validationErrors += "Destination escapes destination root: $sourcePath"
    continue
  }

  $planned += [pscustomobject]@{
    selection_group = $item.selection_group
    bucket = $item.bucket
    repo = $item.repo
    source_path = $sourcePath
    source = $src
    destination = $dest
    priority = $item.priority
    reason = $item.reason
    expected_kb_value = $item.expected_kb_value
    risk = $item.risk
  }
}

if ($validationErrors.Count -gt 0) {
  $validationErrors | ForEach-Object { Write-Error $_ }
  throw "Validation failed; no files copied."
}

$copied = @()
$skipped = @()
foreach ($entry in $planned) {
  if ($WhatIfOnly) {
    $skipped += [pscustomobject]@{
      source_path = $entry.source_path
      destination = $entry.destination
      reason = "what_if_only"
    }
    continue
  }

  $destParent = Split-Path -Parent $entry.destination
  if (-not (Test-Path -LiteralPath $destParent -PathType Container)) {
    New-Item -ItemType Directory -Force -Path $destParent | Out-Null
  }
  Copy-Item -LiteralPath $entry.source -Destination $entry.destination -Force
  $copied += [pscustomobject]@{
    selection_group = $entry.selection_group
    bucket = $entry.bucket
    repo = $entry.repo
    source_path = $entry.source_path
    destination = $entry.destination.Substring($repoRootFull.Length + 1)
  }
}

$summary = [pscustomobject]@{
  generated_at = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
  target_kb = "claude-skill-design"
  source_root = $SourceRoot
  destination_root = $DestinationRoot
  allowlist_path = $AllowlistPath
  include_maybe_later = [bool]$IncludeMaybeLater
  what_if_only = [bool]$WhatIfOnly
  planned_count = $planned.Count
  copied_count = $copied.Count
  skipped_count = $skipped.Count
  validation_errors = $validationErrors
  copied = $copied
  skipped = $skipped
}

if (-not $WhatIfOnly) {
  $reportDir = Split-Path -Parent $reportJsonFull
  if (-not (Test-Path -LiteralPath $reportDir -PathType Container)) {
    New-Item -ItemType Directory -Force -Path $reportDir | Out-Null
  }
}

$summary | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $reportJsonFull -Encoding UTF8

$md = @()
$md += "# High Impact Repo Import Report"
$md += ""
$md += ("- generated_at: ``{0}``" -f $summary.generated_at)
$md += ("- allowlist_path: ``{0}``" -f $AllowlistPath)
$md += ("- source_root: ``{0}``" -f $SourceRoot)
$md += ("- destination_root: ``{0}``" -f $DestinationRoot)
$md += ("- include_maybe_later: ``{0}``" -f $summary.include_maybe_later)
$md += ("- what_if_only: ``{0}``" -f $summary.what_if_only)
$md += ("- planned_count: ``{0}``" -f $summary.planned_count)
$md += ("- copied_count: ``{0}``" -f $summary.copied_count)
$md += ("- skipped_count: ``{0}``" -f $summary.skipped_count)
$md += ""
$md += "## Copied Files"
$md += ""
$md += "| group | bucket | repo | source | destination |"
$md += "| --- | --- | --- | --- | --- |"
foreach ($entry in $copied) {
  $md += ("| {0} | {1} | {2} | ``{3}`` | ``{4}`` |" -f $entry.selection_group, $entry.bucket, $entry.repo, $entry.source_path, $entry.destination)
}
if ($copied.Count -eq 0) {
  $md += "| none | none | none | none | none |"
}
$md += ""
$md += "## Skipped Files"
$md += ""
$md += "| source | reason |"
$md += "| --- | --- |"
foreach ($entry in $skipped) {
  $md += ("| ``{0}`` | {1} |" -f $entry.source_path, $entry.reason)
}
if ($skipped.Count -eq 0) {
  $md += "| none | none |"
}
$md -join "`n" | Set-Content -LiteralPath $reportMarkdownFull -Encoding UTF8

Write-Output ($summary | ConvertTo-Json -Depth 4)
