[CmdletBinding()]
param(
  [string]$KbRoot = "apex-meta/kb",
  [string]$DestinationSlug = "claude-code-orchestration-design",
  [switch]$DryRun
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Get-UtcIso {
  return (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
}

function Get-UtcStamp {
  return (Get-Date).ToUniversalTime().ToString("yyyyMMdd_HHmmss")
}

function Get-FullPath {
  param([Parameter(Mandatory = $true)][string]$Path)
  return [System.IO.Path]::GetFullPath($Path)
}

function Get-RepoRelativePath {
  param([Parameter(Mandatory = $true)][string]$Path)
  $repoRoot = [System.IO.Path]::GetFullPath((Get-Location).Path)
  $full = [System.IO.Path]::GetFullPath($Path)
  $repoRootWithSlash = $repoRoot.TrimEnd([System.IO.Path]::DirectorySeparatorChar, [System.IO.Path]::AltDirectorySeparatorChar) + [System.IO.Path]::DirectorySeparatorChar
  $rootUri = [System.Uri]::new($repoRootWithSlash)
  $fullUri = [System.Uri]::new($full)
  return [System.Uri]::UnescapeDataString($rootUri.MakeRelativeUri($fullUri).ToString()).Replace("\", "/")
}

function New-DirectoryIfMissing {
  param([Parameter(Mandatory = $true)][string]$Path)
  if ($DryRun) { return }
  if (-not (Test-Path -LiteralPath $Path -PathType Container)) {
    New-Item -ItemType Directory -Path $Path -Force | Out-Null
  }
}

function Get-Sha256OrNull {
  param([Parameter(Mandatory = $true)][string]$Path)
  if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) { return $null }
  return (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash.ToLowerInvariant()
}

function Write-TextFileWithCollisionPolicy {
  param(
    [Parameter(Mandatory = $true)][string]$Path,
    [Parameter(Mandatory = $true)][string]$Content,
    [Parameter(Mandatory = $true)][string]$Stamp,
    [Parameter(Mandatory = $true)]$Ledger,
    [Parameter(Mandatory = $true)][string]$Role
  )

  New-DirectoryIfMissing -Path (Split-Path -Parent $Path)
  $target = $Path
  $action = "created"

  if (Test-Path -LiteralPath $Path -PathType Leaf) {
    $existing = Get-Content -LiteralPath $Path -Raw -Encoding UTF8
    if ($existing -eq $Content) {
      $action = "skipped_identical"
    } else {
      $target = "$Path.incoming.$Stamp"
      $action = "conflict_preserved_as_incoming"
    }
  }

  if (-not $DryRun -and $action -ne "skipped_identical") {
    Set-Content -LiteralPath $target -Value $Content -Encoding UTF8 -NoNewline
  }

  $targetHash = $null
  if (-not $DryRun -and (Test-Path -LiteralPath $target -PathType Leaf)) {
    $targetHash = Get-Sha256OrNull -Path $target
  }

  $Ledger.Add([pscustomobject]@{
    role = $Role
    action = $action
    source = $null
    target = Get-RepoRelativePath -Path $target
    bytes = [System.Text.Encoding]::UTF8.GetByteCount($Content)
    sha256 = $targetHash
  }) | Out-Null
}

function Copy-DirectoryWithCollisionPolicy {
  param(
    [Parameter(Mandatory = $true)][string]$SourceRoot,
    [Parameter(Mandatory = $true)][string]$TargetRoot,
    [Parameter(Mandatory = $true)][string]$Stamp,
    [Parameter(Mandatory = $true)]$Ledger
  )

  $files = @(Get-ChildItem -LiteralPath $SourceRoot -Recurse -File -Force -ErrorAction SilentlyContinue)
  $bytesTotal = 0
  $filesCopied = 0
  $filesSkipped = 0
  $conflicts = 0

  foreach ($file in $files) {
    $sourceRootWithSlash = ([System.IO.Path]::GetFullPath($SourceRoot)).TrimEnd([System.IO.Path]::DirectorySeparatorChar, [System.IO.Path]::AltDirectorySeparatorChar) + [System.IO.Path]::DirectorySeparatorChar
    $sourceRootUri = [System.Uri]::new($sourceRootWithSlash)
    $fileUri = [System.Uri]::new([System.IO.Path]::GetFullPath($file.FullName))
    $relative = [System.Uri]::UnescapeDataString($sourceRootUri.MakeRelativeUri($fileUri).ToString()).Replace("/", [System.IO.Path]::DirectorySeparatorChar)
    $target = Join-Path $TargetRoot $relative
    $finalTarget = $target
    $sourceHash = Get-Sha256OrNull -Path $file.FullName
    $action = "copied"
    $bytesTotal += $file.Length

    if (Test-Path -LiteralPath $target -PathType Leaf) {
      $targetHash = Get-Sha256OrNull -Path $target
      if ($sourceHash -and $targetHash -and $sourceHash -eq $targetHash) {
        $action = "skipped_identical"
        $filesSkipped++
      } else {
        $finalTarget = "$target.incoming.$Stamp"
        $action = "conflict_preserved_as_incoming"
        $conflicts++
      }
    }

    if ($action -ne "skipped_identical") {
      if (-not $DryRun) {
        New-DirectoryIfMissing -Path (Split-Path -Parent $finalTarget)
        Copy-Item -LiteralPath $file.FullName -Destination $finalTarget -Force:$false
      }
      $filesCopied++
    }

    $Ledger.Add([pscustomobject]@{
      role = "source_copy"
      action = $action
      source = Get-RepoRelativePath -Path $file.FullName
      target = Get-RepoRelativePath -Path $finalTarget
      bytes = $file.Length
      source_sha256 = $sourceHash
    }) | Out-Null
  }

  return [pscustomobject]@{
    source_root = Get-RepoRelativePath -Path $SourceRoot
    target_root = Get-RepoRelativePath -Path $TargetRoot
    file_count = $files.Count
    bytes_total = $bytesTotal
    files_copied = $filesCopied
    files_skipped_identical = $filesSkipped
    conflicts = $conflicts
  }
}

$repoRoot = (Get-Location).Path
$kbRootAbs = Get-FullPath -Path (Join-Path $repoRoot $KbRoot)
$destinationRoot = Join-Path $kbRootAbs $DestinationSlug
$rawSourceGroupsRoot = Join-Path $destinationRoot "raw/source-groups"
$migrationRoot = Join-Path $destinationRoot "manifests/migration"
$stamp = Get-UtcStamp
$generatedAt = Get-UtcIso

if (-not (Test-Path -LiteralPath $kbRootAbs -PathType Container)) {
  throw "KB root not found: $KbRoot. Run from repository root."
}

$branch = "unknown"
$statusBefore = ""
try { $branch = ((& git rev-parse --abbrev-ref HEAD 2>$null) -join "`n").Trim() } catch {}
try { $statusBefore = (& git status --short 2>$null) -join "`n" } catch {}

$ledger = [System.Collections.Generic.List[object]]::new()
$copySummaries = [System.Collections.Generic.List[object]]::new()
$sourceRootMap = [System.Collections.Generic.List[object]]::new()
$missingRequired = [System.Collections.Generic.List[object]]::new()

$domains = @(
  "skill-package-design",
  "agent-subagent-design",
  "workflow-design",
  "commands-hooks-rules-memory",
  "prompt-pack-and-artifact-contracts",
  "apex-application-patterns",
  "external-repo-patterns"
)

$requiredDirs = @(
  $destinationRoot,
  $rawSourceGroupsRoot,
  $migrationRoot,
  (Join-Path $destinationRoot "raw/source-groups/_source-acquisitions"),
  (Join-Path $destinationRoot "wiki/summaries"),
  (Join-Path $destinationRoot "wiki/concepts"),
  (Join-Path $destinationRoot "wiki/entities"),
  (Join-Path $destinationRoot "ingest-analysis"),
  (Join-Path $destinationRoot "audit"),
  (Join-Path $destinationRoot "log"),
  (Join-Path $destinationRoot "derived/search"),
  (Join-Path $destinationRoot "outputs/queries")
)

foreach ($domain in $domains) {
  $requiredDirs += (Join-Path $destinationRoot "domains/$domain")
}

foreach ($dir in $requiredDirs) {
  New-DirectoryIfMissing -Path $dir
}

$copyPlan = @(
  [pscustomobject]@{
    id = "claude-skill-design"
    source = "apex-meta/kb/claude-skill-design"
    target = "apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-skill-design"
    required = $true
    domains = @("skill-package-design", "commands-hooks-rules-memory")
    priority = "P0-P1"
    reason = "Main existing Claude skill-design KB with schema, source inventories, Phase 0 artifacts, official docs, operator notes, and large corpus intelligence."
  },
  [pscustomobject]@{
    id = "skill-design-best-practices"
    source = "apex-meta/kb/skill-design-best-practices"
    target = "apex-meta/kb/claude-code-orchestration-design/raw/source-groups/skill-design-best-practices"
    required = $true
    domains = @("skill-package-design")
    priority = "P0-P1"
    reason = "Focused earlier skill best-practices KB with Phase 1 analysis of official skill-package guidance."
  },
  [pscustomobject]@{
    id = "skill-best-practices-official-source-acquisition"
    source = "apex-meta/kb/_source-acquisitions/skill-best-practices-official-2026-06-23"
    target = "apex-meta/kb/claude-code-orchestration-design/raw/source-groups/_source-acquisitions/skill-best-practices-official-2026-06-23"
    required = $true
    domains = @("skill-package-design")
    priority = "P0"
    reason = "Raw official source-acquisition archive for Anthropic Agent Skills docs, official PDF, engineering article, Agent Skills specification, official repos, and academic/security sources."
  },
  [pscustomobject]@{
    id = "claude-orchestration-agents"
    source = "apex-meta/kb/claude-orchestration-agents"
    target = "apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents"
    required = $true
    domains = @("agent-subagent-design", "workflow-design", "commands-hooks-rules-memory", "external-repo-patterns")
    priority = "P1-P3"
    reason = "Downloaded Claude orchestration agent repo corpus, including Claude Code best practices, BMAD, personal-os, claude-agents, awesome-claude-code, Aider, and SWE-agent."
  },
  [pscustomobject]@{
    id = "prompt-engineer-research-base"
    source = "apex-meta/kb/prompt-engineer-research-base"
    target = "apex-meta/kb/claude-code-orchestration-design/raw/source-groups/prompt-engineer-research-base"
    required = $false
    domains = @("prompt-pack-and-artifact-contracts", "apex-application-patterns")
    priority = "P2"
    reason = "Prompt/workflow research KB. Relevant only as supporting material for prompt-pack design and artifact-contract patterns."
  }
)

$schemaText = @"
# Claude Code Orchestration Design KB Schema

````yaml
kb_schema:
  kb_slug: claude-code-orchestration-design
  kb_topic_title: "Claude Code Orchestration Design"
  architecture: hybrid_integrated_kb_with_modular_domains

  purpose: >
    Integrated source-preserving Apex KB for Claude Code skill package design,
    agents/subagents, workflows, commands, hooks, rules, memory, prompt-pack
    design, Apex application patterns, and external repo orchestration patterns.

  internal_domains:
    - skill-package-design
    - agent-subagent-design
    - workflow-design
    - commands-hooks-rules-memory
    - prompt-pack-and-artifact-contracts
    - apex-application-patterns
    - external-repo-patterns

  source_priority_policy:
    P0:
      - official Claude / Anthropic Agent Skills docs
      - official Agent Skills specification
      - official source-acquisition archives
      - accepted Apex contracts and process specs
    P1:
      - claude-skill-design KB
      - skill-design-best-practices KB
      - anthropics/skills official repo material
      - operator-supplied Apex skill/prompt/workflow guidance
    P2:
      - claude-code-best-practice
      - BMAD-METHOD
      - claude-agents
      - personal-os
      - prompt-engineer-research-base where relevant to prompt-pack patterns
    P3:
      - awesome-claude-code as discovery/reference only
      - Aider for repo-map/git/workflow comparison only
      - SWE-agent for conceptual agent-computer-interface comparison only

  migration_policy:
    source_roots_are_copied_not_moved: true
    old_roots_are_preserved: true
    duplicates_are_reported_not_deleted: true
    conflicts_are_preserved_as_incoming_files: true

  lifecycle_policy:
    this_script_runs_phase0: false
    this_script_runs_phase1: false
    this_script_runs_phase2: false
    phase0_allowed_after_operator_review: true
    phase1_allowed_after_operator_command: true
    phase2_requires_exact_phrase: "approve ingest"

  exclusions:
    - Hermes runtime
    - OpenCLAW runtime
    - generic autonomous swarm architecture
    - Apex Plan mutation
    - Apex Sync mutation
    - Apex Session mutation
    - PreCap mutation
    - FlowRecap mutation
    - APSU/status-merge mutation
````
"@

$readmeText = @"
# Claude Code Orchestration Design KB

This is the integrated Option C KB root for Claude-native Apex orchestration design.

It copies and preserves source custody from existing Apex KB roots related to:

- Claude skill design
- Agent Skills / SKILL.md package design
- Claude agents and subagents
- Claude Code workflows
- commands, hooks, rules, memory, and `.claude/` layout
- prompt-pack and artifact-contract design
- external repo orchestration patterns

This script only performs a source-preserving migration scaffold.

It does not run:

- deterministic Phase 0
- Phase 1 semantic ingest
- Phase 2 wiki synthesis
- retrieval index build
- lint/audit maintenance

Next step: review `manifests/migration/migration-report.md`, then run deterministic Phase 0 for this KB root.
"@

$wikiIndexText = @"
# Claude Code Orchestration Design Wiki Index

Status: scaffolded only.

No Phase 2 wiki synthesis has been run.

Review migration reports first, then run deterministic Phase 0.
"@

Write-TextFileWithCollisionPolicy -Path (Join-Path $destinationRoot "kb-schema.md") -Content $schemaText -Stamp $stamp -Ledger $ledger -Role "kb_schema"
Write-TextFileWithCollisionPolicy -Path (Join-Path $destinationRoot "README.md") -Content $readmeText -Stamp $stamp -Ledger $ledger -Role "readme"
Write-TextFileWithCollisionPolicy -Path (Join-Path $destinationRoot "wiki/index.md") -Content $wikiIndexText -Stamp $stamp -Ledger $ledger -Role "wiki_index_placeholder"

foreach ($domain in $domains) {
  $domainReadme = "# $domain`n`nDomain scaffold created during source-preserving KB integration. Semantic pages require later ingest.`n"
  Write-TextFileWithCollisionPolicy -Path (Join-Path $destinationRoot "domains/$domain/README.md") -Content $domainReadme -Stamp $stamp -Ledger $ledger -Role "domain_readme"
}

foreach ($item in $copyPlan) {
  $sourceAbs = Get-FullPath -Path (Join-Path $repoRoot $item.source)
  $targetAbs = Get-FullPath -Path (Join-Path $repoRoot $item.target)

  if (-not (Test-Path -LiteralPath $sourceAbs -PathType Container)) {
    $row = [pscustomobject]@{
      id = $item.id
      source = $item.source
      target = $item.target
      required = $item.required
      copied = $false
      status = "missing"
      domains = $item.domains
      priority = $item.priority
      reason = $item.reason
    }
    $sourceRootMap.Add($row) | Out-Null
    if ($item.required) { $missingRequired.Add($row) | Out-Null }
    continue
  }

  $summary = Copy-DirectoryWithCollisionPolicy -SourceRoot $sourceAbs -TargetRoot $targetAbs -Stamp $stamp -Ledger $ledger
  $copySummaries.Add($summary) | Out-Null

  $sourceRootMap.Add([pscustomobject]@{
    id = $item.id
    source = $item.source
    target = $item.target
    required = $item.required
    copied = $true
    status = "copied"
    domains = $item.domains
    priority = $item.priority
    reason = $item.reason
    file_count = $summary.file_count
    bytes_total = $summary.bytes_total
    conflicts = $summary.conflicts
  }) | Out-Null
}

# Audit-only discovery. This does not copy anything. It warns Codex/operator if a relevant-looking KB root exists outside the explicit architecture map.
$explicitSourceSet = @{}
foreach ($item in $copyPlan) {
  $explicitSourceSet[$item.source.Replace("\", "/").TrimEnd("/")] = $true
}

$auditCandidates = [System.Collections.Generic.List[object]]::new()
$tokens = @("claude", "skill", "agent", "orchestrat", "workflow", "prompt", "hook", "subagent")

foreach ($child in @(Get-ChildItem -LiteralPath $kbRootAbs -Directory -Force | Where-Object { $_.Name -ne $DestinationSlug })) {
  $rel = Get-RepoRelativePath -Path $child.FullName
  if ($explicitSourceSet.ContainsKey($rel)) { continue }

  $nameLower = $child.Name.ToLowerInvariant()
  $hits = @()
  foreach ($token in $tokens) {
    if ($nameLower.Contains($token)) { $hits += $token }
  }

  if ($hits.Count -gt 0) {
    $auditCandidates.Add([pscustomobject]@{
      path = $rel
      reason = "folder_name_token_match"
      tokens = @($hits | Select-Object -Unique)
      copied = $false
      action = "operator_review_required_before_adding_to_copy_plan"
    }) | Out-Null
  }
}

# Duplicate hash report over copied material. Duplicates are preserved.
$hashRows = [System.Collections.Generic.List[object]]::new()
if (Test-Path -LiteralPath $rawSourceGroupsRoot -PathType Container) {
  foreach ($file in @(Get-ChildItem -LiteralPath $rawSourceGroupsRoot -Recurse -File -Force -ErrorAction SilentlyContinue)) {
    $hash = Get-Sha256OrNull -Path $file.FullName
    if ($hash) {
      $hashRows.Add([pscustomobject]@{
        sha256 = $hash
        path = Get-RepoRelativePath -Path $file.FullName
        bytes = $file.Length
      }) | Out-Null
    }
  }
}

$duplicateGroups = @(
  $hashRows |
    Group-Object sha256 |
    Where-Object { $_.Count -gt 1 } |
    ForEach-Object {
      [pscustomobject]@{
        sha256 = $_.Name
        count = $_.Count
        paths = @($_.Group | Select-Object -ExpandProperty path)
      }
    }
)

$conflicts = @($ledger | Where-Object { $_.action -eq "conflict_preserved_as_incoming" })

$sourceRootMapJson = [pscustomobject]@{
  generated_at = $generatedAt
  destination_root = Get-RepoRelativePath -Path $destinationRoot
  explicit_copy_plan = @($copyPlan)
  source_roots = @($sourceRootMap)
  missing_required = @($missingRequired)
  audit_only_unmapped_candidates = @($auditCandidates)
}

$copyLedgerJson = [pscustomobject]@{
  generated_at = $generatedAt
  dry_run = [bool]$DryRun
  destination_root = Get-RepoRelativePath -Path $destinationRoot
  copy_summaries = @($copySummaries)
  ledger_entries = @($ledger)
  duplicate_hash_groups = @($duplicateGroups)
}

$sourceMapMd = "# Source Root Map`n`n"
$sourceMapMd += "| ID | Source | Target | Required | Copied | Priority | Domains | Reason |`n"
$sourceMapMd += "|---|---|---|---:|---:|---|---|---|`n"
foreach ($row in $sourceRootMap) {
  $sourceMapMd += "| `$($row.id)` | `$($row.source)` | `$($row.target)` | $($row.required) | $($row.copied) | `$($row.priority)` | `$([string]::Join(', ', $row.domains))` | $($row.reason) |`n"
}

$copyLedgerMd = "# Copy Ledger`n`n"
$copyLedgerMd += "| Source root | Target root | Files | Bytes | Copied | Skipped identical | Conflicts |`n"
$copyLedgerMd += "|---|---|---:|---:|---:|---:|---:|`n"
foreach ($summary in $copySummaries) {
  $copyLedgerMd += "| `$($summary.source_root)` | `$($summary.target_root)` | $($summary.file_count) | $($summary.bytes_total) | $($summary.files_copied) | $($summary.files_skipped_identical) | $($summary.conflicts) |`n"
}

$unmappedMd = "# Audit-Only Unmapped Candidates`n`n"
$unmappedMd += "These were not copied. They require operator review before adding to the explicit copy plan.`n`n"
$unmappedMd += "| Path | Reason | Tokens | Action |`n"
$unmappedMd += "|---|---|---|---|`n"
foreach ($candidate in $auditCandidates) {
  $unmappedMd += "| `$($candidate.path)` | `$($candidate.reason)` | `$([string]::Join(', ', $candidate.tokens))` | `$($candidate.action)` |`n"
}

$verdict = "PASS"
if ($missingRequired.Count -gt 0) {
  $verdict = "FAIL"
} elseif ($conflicts.Count -gt 0 -or $auditCandidates.Count -gt 0) {
  $verdict = "PARTIAL"
}

$missingMd = "None."
if ($missingRequired.Count -gt 0) {
  $missingLines = @()
  foreach ($missingItem in $missingRequired) {
    $missingLines += "- ``$($missingItem.source)``"
  }
  $missingMd = [string]::Join([Environment]::NewLine, $missingLines)
}

$conflictMd = "None."
if ($conflicts.Count -gt 0) {
  $conflictLines = @()
  foreach ($conflictItem in @($conflicts | Select-Object -First 200)) {
    $conflictLines += "- ``$($conflictItem.target)``"
  }
  $conflictMd = [string]::Join([Environment]::NewLine, $conflictLines)
}

$reportMd = @"
# Claude Code Orchestration Design KB Migration Report

Generated: $generatedAt

## Verdict

$verdict

## Git context

````yaml
branch: $branch
destination_root: $(Get-RepoRelativePath -Path $destinationRoot)
dry_run: $([bool]$DryRun)
lifecycle_executed: false
phase0_executed: false
phase1_executed: false
phase2_executed: false
old_roots_deleted_or_moved: false
````

## Git status before

````text
$statusBefore
````

## Required source roots missing

$missingMd

## Source root map

$sourceMapMd

## Copy summary

$copyLedgerMd

## Conflicts

$conflictMd

## Audit-only unmapped candidates

$unmappedMd

## Duplicate hash groups

Duplicate hash groups are reported in:

````text
manifests/migration/duplicate-hash-report.json
````

Duplicates were preserved. Nothing was deleted.

## Next allowed step

Run deterministic Phase 0 for:

````text
apex-meta/kb/claude-code-orchestration-design/
````

only after operator review.
"@

Write-TextFileWithCollisionPolicy -Path (Join-Path $migrationRoot "source-root-map.json") -Content (($sourceRootMapJson | ConvertTo-Json -Depth 30) + "`n") -Stamp $stamp -Ledger $ledger -Role "migration_report"
Write-TextFileWithCollisionPolicy -Path (Join-Path $migrationRoot "source-root-map.md") -Content $sourceMapMd -Stamp $stamp -Ledger $ledger -Role "migration_report"
Write-TextFileWithCollisionPolicy -Path (Join-Path $migrationRoot "copy-ledger.json") -Content (($copyLedgerJson | ConvertTo-Json -Depth 40) + "`n") -Stamp $stamp -Ledger $ledger -Role "migration_report"
Write-TextFileWithCollisionPolicy -Path (Join-Path $migrationRoot "copy-ledger.md") -Content $copyLedgerMd -Stamp $stamp -Ledger $ledger -Role "migration_report"
Write-TextFileWithCollisionPolicy -Path (Join-Path $migrationRoot "audit-only-unmapped-candidates.md") -Content $unmappedMd -Stamp $stamp -Ledger $ledger -Role "migration_report"
Write-TextFileWithCollisionPolicy -Path (Join-Path $migrationRoot "duplicate-hash-report.json") -Content (([pscustomobject]@{ generated_at = $generatedAt; duplicate_hash_groups = @($duplicateGroups) } | ConvertTo-Json -Depth 40) + "`n") -Stamp $stamp -Ledger $ledger -Role "migration_report"
Write-TextFileWithCollisionPolicy -Path (Join-Path $migrationRoot "migration-report.md") -Content $reportMd -Stamp $stamp -Ledger $ledger -Role "migration_report"

$requiredOutputs = @(
  $destinationRoot,
  (Join-Path $destinationRoot "kb-schema.md"),
  (Join-Path $destinationRoot "README.md"),
  (Join-Path $destinationRoot "wiki/index.md"),
  (Join-Path $migrationRoot "source-root-map.json"),
  (Join-Path $migrationRoot "source-root-map.md"),
  (Join-Path $migrationRoot "copy-ledger.json"),
  (Join-Path $migrationRoot "copy-ledger.md"),
  (Join-Path $migrationRoot "audit-only-unmapped-candidates.md"),
  (Join-Path $migrationRoot "duplicate-hash-report.json"),
  (Join-Path $migrationRoot "migration-report.md")
)

$hardFailures = @($requiredOutputs | Where-Object { -not $DryRun -and -not (Test-Path -LiteralPath $_) })
if ($hardFailures.Count -gt 0) { $verdict = "FAIL" }

Write-Host "FINAL_REPORT:"
Write-Host "  verdict: $verdict"
Write-Host "  destination_root: $(Get-RepoRelativePath -Path $destinationRoot)"
Write-Host "  explicit_source_roots_in_plan: $($copyPlan.Count)"
Write-Host "  source_roots_copied: $($copySummaries.Count)"
Write-Host "  missing_required_roots: $($missingRequired.Count)"
Write-Host "  conflicts: $($conflicts.Count)"
Write-Host "  duplicate_hash_groups_reported: $($duplicateGroups.Count)"
Write-Host "  audit_only_unmapped_candidates: $($auditCandidates.Count)"
Write-Host "  old_roots_preserved: true"
Write-Host "  lifecycle_executed: false"
Write-Host "  next_step: operator review, then deterministic Phase 0"

if ($hardFailures.Count -gt 0) {
  Write-Host "  hard_failures:"
  foreach ($failure in $hardFailures) {
    Write-Host "    - $(Get-RepoRelativePath -Path $failure)"
  }
  exit 1
}

if ($missingRequired.Count -gt 0) { exit 1 }
exit 0
