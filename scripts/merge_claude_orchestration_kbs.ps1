[CmdletBinding()]
param(
  [string]$KbRoot = "apex-meta/kb",
  [string]$DestinationSlug = "claude-code-orchestration-design",
  [switch]$DryRun
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function UtcStamp { (Get-Date).ToUniversalTime().ToString("yyyyMMdd_HHmmss") }
function UtcIso { (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ") }
function FullPath([string]$p) { [System.IO.Path]::GetFullPath($p) }
function RelPath([string]$p) { [System.IO.Path]::GetRelativePath((Get-Location).Path, (FullPath $p)).Replace("\", "/") }
function EnsureDir([string]$p) { if (-not $DryRun -and -not (Test-Path -LiteralPath $p -PathType Container)) { New-Item -ItemType Directory -Path $p -Force | Out-Null } }
function Sha256([string]$p) { if (Test-Path -LiteralPath $p -PathType Leaf) { return (Get-FileHash -LiteralPath $p -Algorithm SHA256).Hash.ToLowerInvariant() }; return $null }

function RootScore($root) {
  $name = $root.Name.ToLowerInvariant()
  $sample = ""
  foreach ($n in @("kb-schema.md", "README.md", "source-manifest.json", "source-inventory.json")) {
    $p = Join-Path $root.FullName $n
    if (Test-Path -LiteralPath $p -PathType Leaf) {
      try {
        $txt = Get-Content -LiteralPath $p -Raw -Encoding UTF8
        if ($txt.Length -gt 30000) { $txt = $txt.Substring(0, 30000) }
        $sample += "`n" + $txt
      } catch {}
    }
  }
  $hay = ($name + "`n" + $sample).ToLowerInvariant()
  $score = 0
  $reasons = @()
  foreach ($x in @(
    @("claude",5), @("skill",4), @("agent",4), @("orchestrat",5),
    @("workflow",3), @("prompt",3), @("hook",2), @("subagent",3),
    @("claude code",5), @("skill package",5), @("agent skills",5)
  )) {
    if ($hay.Contains([string]$x[0])) { $score += [int]$x[1]; $reasons += [string]$x[0] }
  }
  return [pscustomobject]@{ score = $score; reasons = @($reasons | Select-Object -Unique) }
}

function DomainHints([string]$name) {
  $n = $name.ToLowerInvariant()
  $d = @()
  if ($n -match "skill") { $d += "skill-package-design" }
  if ($n -match "agent|claude") { $d += "agent-subagent-design" }
  if ($n -match "orchestrat|workflow|bmad") { $d += "workflow-design" }
  if ($n -match "command|hook|rule|memory|claude") { $d += "commands-hooks-rules-memory" }
  if ($n -match "prompt") { $d += "prompt-pack-and-artifact-contracts" }
  if ($n -match "claude|orchestrat") { $d += "external-repo-patterns" }
  if ($d.Count -eq 0) { $d += "external-repo-patterns" }
  return @($d | Select-Object -Unique)
}

function WriteTextSafe($path, $text, $stamp, $ledger, $role) {
  EnsureDir (Split-Path -Parent $path)
  $target = $path
  $action = "created"
  if (Test-Path -LiteralPath $path -PathType Leaf) {
    $old = Get-Content -LiteralPath $path -Raw -Encoding UTF8
    if ($old -eq $text) { $action = "skipped_identical" } else { $target = "$path.incoming.$stamp"; $action = "conflict_preserved_as_incoming" }
  }
  if (-not $DryRun -and $action -ne "skipped_identical") { Set-Content -LiteralPath $target -Value $text -Encoding UTF8 -NoNewline }
  $outHash = $null
  if ((-not $DryRun) -and (Test-Path -LiteralPath $target -PathType Leaf)) { $outHash = Sha256 $target }
  $ledger.Add([pscustomobject]@{ role=$role; action=$action; source=$null; target=(RelPath $target); bytes=[Text.Encoding]::UTF8.GetByteCount($text); sha256=$outHash })
}

function CopyRoot($sourceRoot, $targetRoot, $stamp, $ledger) {
  $files = @(Get-ChildItem -LiteralPath $sourceRoot.FullName -Recurse -File -Force -ErrorAction SilentlyContinue)
  $bytes = 0; $copied = 0; $skipped = 0; $conflicts = 0
  foreach ($f in $files) {
    $rel = [System.IO.Path]::GetRelativePath($sourceRoot.FullName, $f.FullName)
    $target = Join-Path $targetRoot $rel
    $final = $target
    $action = "copied"
    $srcHash = Sha256 $f.FullName
    $bytes += $f.Length
    if (Test-Path -LiteralPath $target -PathType Leaf) {
      $dstHash = Sha256 $target
      if ($srcHash -and $dstHash -and $srcHash -eq $dstHash) { $action = "skipped_identical"; $skipped++ }
      else { $final = "$target.incoming.$stamp"; $action = "conflict_preserved_as_incoming"; $conflicts++ }
    }
    if ($action -ne "skipped_identical") {
      if (-not $DryRun) { EnsureDir (Split-Path -Parent $final); Copy-Item -LiteralPath $f.FullName -Destination $final -Force:$false }
      $copied++
    }
    if ($action -ne "copied") { $ledger.Add([pscustomobject]@{ role="source_copy"; action=$action; source=(RelPath $f.FullName); target=(RelPath $final); bytes=$f.Length; source_sha256=$srcHash }) }
  }
  return [pscustomobject]@{ source_root=(RelPath $sourceRoot.FullName); target_root=(RelPath $targetRoot); file_count=$files.Count; bytes_total=$bytes; files_copied=$copied; files_skipped_identical=$skipped; conflicts=$conflicts }
}

$stamp = UtcStamp
$now = UtcIso
$repo = (Get-Location).Path
$kbRootAbs = FullPath (Join-Path $repo $KbRoot)
$dest = Join-Path $kbRootAbs $DestinationSlug
$rawGroups = Join-Path $dest "raw/source-groups"
$migration = Join-Path $dest "manifests/migration"

if (-not (Test-Path -LiteralPath $kbRootAbs -PathType Container)) { throw "KB root not found: $KbRoot" }

$branch = "unknown"; $statusBefore = ""
try { $branch = ((& git rev-parse --abbrev-ref HEAD 2>$null) -join "`n").Trim() } catch {}
try { $statusBefore = (& git status --short 2>$null) -join "`n" } catch {}

$ledger = [System.Collections.Generic.List[object]]::new()
$summaries = [System.Collections.Generic.List[object]]::new()
$sourceMap = [System.Collections.Generic.List[object]]::new()
$missing = [System.Collections.Generic.List[string]]::new()

$domains = @("skill-package-design","agent-subagent-design","workflow-design","commands-hooks-rules-memory","prompt-pack-and-artifact-contracts","apex-application-patterns","external-repo-patterns")
$dirs = @($dest,$rawGroups,$migration,(Join-Path $dest "wiki/summaries"),(Join-Path $dest "wiki/concepts"),(Join-Path $dest "wiki/entities"),(Join-Path $dest "ingest-analysis"),(Join-Path $dest "audit"),(Join-Path $dest "log"),(Join-Path $dest "derived/search"),(Join-Path $dest "outputs/queries"))
foreach ($d in $domains) { $dirs += (Join-Path $dest "domains/$d") }
foreach ($d in $dirs) { EnsureDir $d }

$schema = @"
# Claude Code Orchestration Design KB Schema

````yaml
kb_schema:
  kb_slug: claude-code-orchestration-design
  kb_topic_title: "Claude Code Orchestration Design"
  architecture: hybrid_integrated_kb_with_modular_domains
  internal_domains:
    - skill-package-design
    - agent-subagent-design
    - workflow-design
    - commands-hooks-rules-memory
    - prompt-pack-and-artifact-contracts
    - apex-application-patterns
    - external-repo-patterns
  lifecycle_policy:
    this_migration_task_runs_lifecycle: false
    phase0_allowed_after_operator_review: true
    phase1_allowed_after_operator_command: true
    phase2_requires_exact_phrase: "approve ingest"
  source_custody_policy:
    source_roots_are_copied_not_moved: true
    old_roots_are_preserved: true
    duplicate_sources_are_preserved_and_reported_not_removed: true
````
"@
$readme = "# Claude Code Orchestration Design KB`n`nIntegrated source-preserving KB for Claude skill design, agents/subagents, Claude Code workflows, hooks, rules, memory, prompt-pack design, Apex application patterns, and external repo patterns.`n`nThis migration only copies source groups and writes ledgers. It does not run Phase 0, Phase 1, Phase 2, retrieval, lint, or audit.`n"
$wikiIndex = "# Claude Code Orchestration Design Wiki Index`n`nStatus: scaffolded only. No Phase 2 wiki synthesis has been run.`n"

WriteTextSafe (Join-Path $dest "kb-schema.md") $schema $stamp $ledger "kb_schema"
WriteTextSafe (Join-Path $dest "README.md") $readme $stamp $ledger "readme"
WriteTextSafe (Join-Path $dest "wiki/index.md") $wikiIndex $stamp $ledger "wiki_index_placeholder"
foreach ($d in $domains) { WriteTextSafe (Join-Path $dest "domains/$d/README.md") "# $d`n`nCreated during source-preserving integration. Semantic pages require later ingest.`n" $stamp $ledger "domain_readme" }

$expectedCore = @("claude-skill-design","claude-orchestration-agents","skill-design-best-practices")
$expectedOptional = @("prompt-engineer-research-base")
$candidates = @{}
foreach ($name in ($expectedCore + $expectedOptional)) {
  $p = Join-Path $kbRootAbs $name
  if (Test-Path -LiteralPath $p -PathType Container) { $candidates[$name] = Get-Item -LiteralPath $p }
  elseif ($expectedCore -contains $name) { $missing.Add("$KbRoot/$name") }
}
foreach ($child in @(Get-ChildItem -LiteralPath $kbRootAbs -Directory -Force | Where-Object { $_.Name -ne $DestinationSlug -and $_.Name -ne "_source-acquisitions" })) {
  if ($candidates.ContainsKey($child.Name)) { continue }
  $sc = RootScore $child
  if ($sc.score -ge 7) { $candidates[$child.Name] = $child }
}
$acq = Join-Path $kbRootAbs "_source-acquisitions"
if (Test-Path -LiteralPath $acq -PathType Container) {
  foreach ($child in @(Get-ChildItem -LiteralPath $acq -Directory -Force)) {
    $sc = RootScore $child
    if ($child.Name.ToLowerInvariant() -match "skill|claude|agent|orchestrat|workflow|prompt" -or $sc.score -ge 5) { $candidates["_source-acquisitions/$($child.Name)"] = $child }
  }
}

foreach ($key in ($candidates.Keys | Sort-Object)) {
  $root = $candidates[$key]
  $sc = RootScore $root
  $target = Join-Path $rawGroups ($key.Replace("\", "/"))
  $dh = DomainHints $root.Name
  $sourceMap.Add([pscustomobject]@{ source_root=(RelPath $root.FullName); included=$true; score=$sc.score; reasons=@($sc.reasons); domains=@($dh); target_root=(RelPath $target) })
  $summaries.Add((CopyRoot $root $target $stamp $ledger))
}

$hashRows = [System.Collections.Generic.List[object]]::new()
if (Test-Path -LiteralPath $rawGroups -PathType Container) {
  foreach ($f in @(Get-ChildItem -LiteralPath $rawGroups -Recurse -File -Force -ErrorAction SilentlyContinue)) {
    $h = Sha256 $f.FullName
    if ($h) { $hashRows.Add([pscustomobject]@{ hash=$h; path=(RelPath $f.FullName); bytes=$f.Length }) }
  }
}
$dupes = @($hashRows | Group-Object hash | Where-Object { $_.Count -gt 1 } | ForEach-Object { [pscustomobject]@{ sha256=$_.Name; count=$_.Count; paths=@($_.Group | Select-Object -ExpandProperty path) } })
$conflicts = @($ledger | Where-Object { $_.action -eq "conflict_preserved_as_incoming" })

$sourceRootMap = [pscustomobject]@{ generated_at=$now; destination_root=(RelPath $dest); source_roots=@($sourceMap); missing_expected_roots=@($missing) }
$copyLedger = [pscustomobject]@{ generated_at=$now; dry_run=[bool]$DryRun; destination_root=(RelPath $dest); copy_summaries=@($summaries); entries=@($ledger); duplicate_hash_groups=@($dupes) }

$mapMd = "# Source Root Map`n`n| Source root | Score | Domains | Reasons | Target |`n|---|---:|---|---|---|`n"
foreach ($r in $sourceMap) { $mapMd += "| ``$($r.source_root)`` | $($r.score) | ``$([string]::Join(', ', $r.domains))`` | ``$([string]::Join(', ', $r.reasons))`` | ``$($r.target_root)`` |`n" }
$ledgerMd = "# Copy Ledger`n`n| Source root | Files | Bytes | Copied | Skipped identical | Conflicts |`n|---|---:|---:|---:|---:|---:|`n"
foreach ($s in $summaries) { $ledgerMd += "| ``$($s.source_root)`` | $($s.file_count) | $($s.bytes_total) | $($s.files_copied) | $($s.files_skipped_identical) | $($s.conflicts) |`n" }

$verdictText = if ($missing.Count -eq 0 -and $conflicts.Count -eq 0) { "PASS" } else { "PARTIAL" }
$missingText = if ($missing.Count -eq 0) { "None." } else { ($missing | ForEach-Object { "- ``$_``" }) -join "`n" }
$conflictText = if ($conflicts.Count -eq 0) { "None." } else { ($conflicts | Select-Object -First 200 | ForEach-Object { "- ``$($_.target)``" }) -join "`n" }
$destRel = RelPath $dest
$report = @"
# Claude Code Orchestration Design KB Migration Report

Generated: ``$now``

## Verdict

$verdictText

## Git context

````yaml
branch: $branch
destination_root: $destRel
lifecycle_executed: false
phase1_executed: false
phase2_executed: false
old_roots_deleted_or_moved: false
````

## Git status before

````text
$statusBefore
````

## Missing expected roots

$missingText

## Included source roots

$mapMd

## Copy summary

$ledgerMd

## Conflicts

$conflictText

## Duplicate hash groups

Reported in ``manifests/migration/duplicate-hash-report.json``. Duplicates were preserved, not removed.

## Next allowed step

Run deterministic Phase 0 for ``apex-meta/kb/claude-code-orchestration-design/`` only after operator review.
"@

WriteTextSafe (Join-Path $migration "source-root-map.json") (($sourceRootMap | ConvertTo-Json -Depth 20) + "`n") $stamp $ledger "migration_report"
WriteTextSafe (Join-Path $migration "source-root-map.md") $mapMd $stamp $ledger "migration_report"
WriteTextSafe (Join-Path $migration "copy-ledger.json") (($copyLedger | ConvertTo-Json -Depth 30) + "`n") $stamp $ledger "migration_report"
WriteTextSafe (Join-Path $migration "copy-ledger.md") $ledgerMd $stamp $ledger "migration_report"
WriteTextSafe (Join-Path $migration "duplicate-hash-report.json") (([pscustomobject]@{ generated_at=$now; duplicate_hash_groups=@($dupes) } | ConvertTo-Json -Depth 20) + "`n") $stamp $ledger "migration_report"
WriteTextSafe (Join-Path $migration "migration-report.md") $report $stamp $ledger "migration_report"

$required = @($dest,(Join-Path $dest "kb-schema.md"),(Join-Path $dest "README.md"),(Join-Path $migration "migration-report.md"),(Join-Path $migration "source-root-map.json"),(Join-Path $migration "copy-ledger.json"))
$hard = @($required | Where-Object { -not $DryRun -and -not (Test-Path -LiteralPath $_) })
$verdict = if ($hard.Count -gt 0) { "FAIL" } elseif ($missing.Count -gt 0 -or $conflicts.Count -gt 0) { "PARTIAL" } else { "PASS" }

Write-Host "FINAL_REPORT:"
Write-Host "  verdict: $verdict"
Write-Host "  destination_root: $(RelPath $dest)"
Write-Host "  source_roots_copied: $($summaries.Count)"
Write-Host "  missing_expected_roots: $($missing.Count)"
Write-Host "  conflicts: $($conflicts.Count)"
Write-Host "  duplicate_hash_groups_reported: $($dupes.Count)"
Write-Host "  old_roots_preserved: true"
Write-Host "  lifecycle_executed: false"
Write-Host "  next_step: operator review, then deterministic Phase 0"
if ($hard.Count -gt 0) { exit 1 }
exit 0
