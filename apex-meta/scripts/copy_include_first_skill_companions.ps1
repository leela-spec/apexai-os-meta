param(
  [switch]$WhatIfOnly
)

$ErrorActionPreference = "Stop"

$RepoRoot = (Get-Location).Path
$AllowlistPath = Join-Path $RepoRoot "apex-meta/kb/claude-skill-design/manifests/large-corpus-prework-projectrepos/curated-import-allowlist.json"
$SourceRoot = Join-Path $RepoRoot "source-knowledge/ProjectRepos"
$DestRoot = Join-Path $RepoRoot "apex-meta/kb/claude-skill-design/sources/curated/high-impact-repos"
$ReportMd = Join-Path $RepoRoot "apex-meta/kb/claude-skill-design/manifests/include-first-companion-import-report.md"
$ReportJson = Join-Path $RepoRoot "apex-meta/kb/claude-skill-design/manifests/include-first-companion-import-report.json"

$AllowedExt = @(
  ".md",".mdx",".txt",".json",".yaml",".yml",".toml",
  ".py",".js",".ts",".tsx",".jsx",".sh",".ps1",".bat",
  ".sql",".csv",".html",".css"
)

$SkipDirNames = @(
  ".git","node_modules","dist","build","coverage","__pycache__",
  ".venv","venv",".cache","assets","images","logos","fonts"
)

$StandardDirs = @(
  "references","reference","refs","scripts","script",
  "templates","template","examples","example","samples","sample",
  "prompts","prompt","schemas","schema"
)

$StandardFiles = @(
  "README.md","readme.md","package-manifest.md","manifest.md",
  "manifest.json","metadata.json","config.json"
)

$MaxFileBytes = 500000
$MaxCompanionFilesPerSkill = 40
$MaxTotalCompanionFiles = 1200

function Normalize-PathString {
  param([string]$Path)
  return ($Path -replace "\\","/").Trim()
}

function Get-RelativePath {
  param(
    [string]$Base,
    [string]$Path
  )
  $baseFull = [System.IO.Path]::GetFullPath($Base).TrimEnd('\','/')
  $pathFull = [System.IO.Path]::GetFullPath($Path)
  $uriBase = [System.Uri]::new($baseFull + [System.IO.Path]::DirectorySeparatorChar)
  $uriPath = [System.Uri]::new($pathFull)
  return [System.Uri]::UnescapeDataString($uriBase.MakeRelativeUri($uriPath).ToString())
}

function Test-SkippedDir {
  param([string]$Path)
  $parts = (Normalize-PathString $Path).Split("/")
  foreach ($p in $parts) {
    if ($SkipDirNames -contains $p) { return $true }
  }
  return $false
}

function Test-AllowedFile {
  param([System.IO.FileInfo]$File)

  if (Test-SkippedDir $File.FullName) {
    return @{ ok = $false; reason = "skipped_dir" }
  }

  if ($AllowedExt -notcontains $File.Extension.ToLowerInvariant()) {
    return @{ ok = $false; reason = "disallowed_extension" }
  }

  if ($File.Length -gt $MaxFileBytes) {
    return @{ ok = $false; reason = "too_large" }
  }

  return @{ ok = $true; reason = "ok" }
}

function Resolve-InPackagePath {
  param(
    [string]$PackageRoot,
    [string]$Candidate
  )

  $clean = $Candidate.Trim().Trim('"').Trim("'")
  if ([string]::IsNullOrWhiteSpace($clean)) { return $null }
  if ($clean -match "^[a-zA-Z]+://") { return $null }
  if ($clean.StartsWith("#")) { return $null }
  if ($clean.StartsWith("/")) { return $null }
  if ($clean.Contains("..")) { return $null }

  $resolved = [System.IO.Path]::GetFullPath((Join-Path $PackageRoot $clean))
  $rootFull = [System.IO.Path]::GetFullPath($PackageRoot).TrimEnd('\','/')

  if (-not $resolved.StartsWith($rootFull, [System.StringComparison]::OrdinalIgnoreCase)) {
    return $null
  }

  return $resolved
}

function Extract-LocalReferences {
  param([string]$SkillFile)

  $content = Get-Content -Raw -LiteralPath $SkillFile
  $refs = New-Object System.Collections.Generic.List[string]

  $patterns = @(
    '\[[^\]]+\]\(([^)]+)\)',
    '(references/[A-Za-z0-9_\-./]+)',
    '(reference/[A-Za-z0-9_\-./]+)',
    '(refs/[A-Za-z0-9_\-./]+)',
    '(scripts/[A-Za-z0-9_\-./]+)',
    '(script/[A-Za-z0-9_\-./]+)',
    '(templates/[A-Za-z0-9_\-./]+)',
    '(template/[A-Za-z0-9_\-./]+)',
    '(examples/[A-Za-z0-9_\-./]+)',
    '(example/[A-Za-z0-9_\-./]+)',
    '(samples/[A-Za-z0-9_\-./]+)',
    '(sample/[A-Za-z0-9_\-./]+)',
    '(prompts/[A-Za-z0-9_\-./]+)',
    '(prompt/[A-Za-z0-9_\-./]+)',
    '(schemas/[A-Za-z0-9_\-./]+)',
    '(schema/[A-Za-z0-9_\-./]+)',
    '([A-Za-z0-9_\-./]+\.(?:md|mdx|txt|json|ya?ml|toml|py|js|ts|tsx|jsx|sh|ps1|bat|sql|csv|html|css))'
  )

  foreach ($pattern in $patterns) {
    foreach ($m in [regex]::Matches($content, $pattern, "IgnoreCase")) {
      if ($m.Groups.Count -gt 1) {
        $refs.Add(($m.Groups[1].Value -split '#')[0])
      }
    }
  }

  return $refs | Where-Object { -not [string]::IsNullOrWhiteSpace($_) } | Select-Object -Unique
}

function Add-CandidateFile {
  param(
    [System.Collections.Generic.List[object]]$Candidates,
    [string]$FilePath,
    [string]$PackageRoot,
    [string]$Reason,
    [int]$Priority
  )

  if (-not (Test-Path -LiteralPath $FilePath -PathType Leaf)) { return }

  $file = Get-Item -LiteralPath $FilePath
  $allowed = Test-AllowedFile $file
  if (-not $allowed.ok) {
    $script:Skipped.Add([ordered]@{
      source_path = Get-RelativePath $RepoRoot $file.FullName
      reason = $allowed.reason
      package_root = Get-RelativePath $RepoRoot $PackageRoot
    })
    return
  }

  $Candidates.Add([ordered]@{
    source_full_path = $file.FullName
    source_path = Get-RelativePath $RepoRoot $file.FullName
    package_root = Get-RelativePath $RepoRoot $PackageRoot
    reason = $Reason
    priority = $Priority
    size_bytes = $file.Length
  })
}

if (-not (Test-Path -LiteralPath $AllowlistPath)) {
  throw "Allowlist not found: $AllowlistPath"
}
if (-not (Test-Path -LiteralPath $SourceRoot)) {
  throw "Source root not found: $SourceRoot"
}

$allowlist = Get-Content -Raw -LiteralPath $AllowlistPath | ConvertFrom-Json
$includeFirst = @($allowlist.include_first)

$Copied = New-Object System.Collections.Generic.List[object]
$Planned = New-Object System.Collections.Generic.List[object]
$Skipped = New-Object System.Collections.Generic.List[object]
$PackageRows = New-Object System.Collections.Generic.List[object]
$PackageRoots = New-Object System.Collections.Generic.HashSet[string]

$totalPlanned = 0
$existingEntrypoints = 0

foreach ($record in $includeFirst) {
  $sourcePath = [string]$record.source_path
  if ([string]::IsNullOrWhiteSpace($sourcePath)) {
    $Skipped.Add([ordered]@{ source_path = ""; reason = "missing_source_path" })
    continue
  }

  $sourceFull = Join-Path $SourceRoot $sourcePath
  if (-not (Test-Path -LiteralPath $sourceFull -PathType Leaf)) {
    $Skipped.Add([ordered]@{ source_path = $sourcePath; reason = "include_first_source_missing" })
    continue
  }

  $existingEntrypoints++
  $entryFile = Get-Item -LiteralPath $sourceFull
  $packageRoot = $entryFile.Directory.FullName
  $packageRel = Get-RelativePath $SourceRoot $packageRoot
  [void]$PackageRoots.Add($packageRel)
  $entrypointType = if ($entryFile.Name -ieq "SKILL.md") { "skill_entrypoint" } else { "non_skill_entrypoint" }

  $candidates = New-Object System.Collections.Generic.List[object]

  foreach ($ref in (Extract-LocalReferences $entryFile.FullName)) {
    $resolved = Resolve-InPackagePath $packageRoot $ref
    if ($null -ne $resolved) {
      if (Test-Path -LiteralPath $resolved -PathType Leaf) {
        Add-CandidateFile $candidates $resolved $packageRoot "direct_reference" 1
      } elseif (Test-Path -LiteralPath $resolved -PathType Container) {
        Get-ChildItem -LiteralPath $resolved -Recurse -File | ForEach-Object {
          Add-CandidateFile $candidates $_.FullName $packageRoot "direct_reference_dir" 1
        }
      }
    }
  }

  foreach ($dirName in $StandardDirs) {
    $dir = Join-Path $packageRoot $dirName
    if (Test-Path -LiteralPath $dir -PathType Container) {
      Get-ChildItem -LiteralPath $dir -Recurse -File | ForEach-Object {
        $priority = switch ($dirName) {
          {$_ -in @("references","reference","refs")} { 2; break }
          {$_ -in @("scripts","script")} { 3; break }
          {$_ -in @("templates","template")} { 4; break }
          {$_ -in @("examples","example")} { 5; break }
          {$_ -in @("samples","sample","prompts","prompt","schemas","schema")} { 7; break }
          default { 6 }
        }
        Add-CandidateFile $candidates $_.FullName $packageRoot "standard_dir:$dirName" $priority
      }
    }
  }

  foreach ($fileName in $StandardFiles) {
    $f = Join-Path $packageRoot $fileName
    if (Test-Path -LiteralPath $f -PathType Leaf) {
      Add-CandidateFile $candidates $f $packageRoot "standard_file:$fileName" 6
    }
  }

  $unique = $candidates |
    Sort-Object @{Expression="priority";Ascending=$true}, @{Expression="source_path";Ascending=$true} |
    Group-Object source_path |
    ForEach-Object { $_.Group[0] }

  $truncated = $false
  if (@($unique).Count -gt $MaxCompanionFilesPerSkill) {
    foreach ($extra in @($unique)[$MaxCompanionFilesPerSkill..(@($unique).Count - 1)]) {
      $Skipped.Add([ordered]@{
        source_path = $extra.source_path
        reason = "max_companion_files_per_skill_truncated"
        package_root = $extra.package_root
      })
    }
    $unique = @($unique)[0..($MaxCompanionFilesPerSkill - 1)]
    $truncated = $true
  }

  $packageCopied = 0
  $packageSkippedBefore = $Skipped.Count
  $directRefs = 0
  $scripts = 0
  $references = 0
  $templates = 0
  $examples = 0

  foreach ($candidate in $unique) {
    if ($totalPlanned -ge $MaxTotalCompanionFiles) {
      $Skipped.Add([ordered]@{
        source_path = $candidate.source_path
        reason = "max_total_companion_files_reached"
        package_root = $candidate.package_root
      })
      continue
    }

    $relFromProjectRepos = Get-RelativePath $SourceRoot $candidate.source_full_path
    $dest = Join-Path $DestRoot $relFromProjectRepos
    $destDir = Split-Path -Parent $dest

    $plannedRow = [ordered]@{
      source_path = $candidate.source_path
      destination_path = Get-RelativePath $RepoRoot $dest
      package_root = $candidate.package_root
      reason = $candidate.reason
      size_bytes = $candidate.size_bytes
    }
    $Planned.Add($plannedRow)
    $totalPlanned++

    if ($candidate.reason -like "direct_reference*") { $directRefs++ }
    if ($candidate.reason -like "standard_dir:script*") { $scripts++ }
    if ($candidate.reason -like "standard_dir:ref*") { $references++ }
    if ($candidate.reason -like "standard_dir:template*") { $templates++ }
    if ($candidate.reason -like "standard_dir:example*" -or $candidate.reason -like "standard_dir:sample*") { $examples++ }

    if (-not $WhatIfOnly) {
      New-Item -ItemType Directory -Force -Path $destDir | Out-Null
      Copy-Item -LiteralPath $candidate.source_full_path -Destination $dest -Force
      $Copied.Add($plannedRow)
      $packageCopied++
    }
  }

  $PackageRows.Add([ordered]@{
    package_root = $packageRel
    entrypoint = Get-RelativePath $SourceRoot $entryFile.FullName
    entrypoint_type = $entrypointType
    companion_candidates = @($unique).Count
    copied = $packageCopied
    direct_refs = $directRefs
    scripts = $scripts
    references = $references
    templates = $templates
    examples = $examples
    skipped = $Skipped.Count - $packageSkippedBefore
    truncated = $truncated
    notes = if (@($unique).Count -eq 0) { "no companions discovered" } elseif ($truncated) { "truncated by per-skill limit" } else { "" }
  })
}

$skippedReasons = @{}
foreach ($s in $Skipped) {
  $r = [string]$s.reason
  if (-not $skippedReasons.ContainsKey($r)) { $skippedReasons[$r] = 0 }
  $skippedReasons[$r]++
}

$packagesWithNoCompanions = @($PackageRows | Where-Object { $_.companion_candidates -eq 0 })
$packagesTruncated = @($PackageRows | Where-Object { $_.truncated })

$report = [ordered]@{
  generated_at = (Get-Date).ToUniversalTime().ToString("o")
  what_if_only = [bool]$WhatIfOnly
  include_first_records_seen = $includeFirst.Count
  include_first_existing_source_files = $existingEntrypoints
  package_roots_detected = $PackageRoots.Count
  companion_files_planned = $Planned.Count
  companion_files_copied = $Copied.Count
  skipped_existing_destination = 0
  skipped_missing = (($skippedReasons["include_first_source_missing"] + $skippedReasons["missing_source_path"]) -as [int])
  skipped_binary_or_disallowed = (($skippedReasons["disallowed_extension"] + $skippedReasons["skipped_dir"]) -as [int])
  skipped_too_large = ($skippedReasons["too_large"] -as [int])
  skipped_outside_package_root = 0
  packages_with_no_companions = $packagesWithNoCompanions.Count
  packages_truncated_by_limit = $packagesTruncated.Count
  destination_root = Get-RelativePath $RepoRoot $DestRoot
  max_file_bytes = $MaxFileBytes
  max_companion_files_per_skill = $MaxCompanionFilesPerSkill
  max_total_companion_files = $MaxTotalCompanionFiles
  package_rows = $PackageRows
  copied_files = $Copied
  planned_files = $Planned
  skipped_files = $Skipped
}

New-Item -ItemType Directory -Force -Path (Split-Path -Parent $ReportJson) | Out-Null
$report | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $ReportJson -Encoding UTF8

$md = New-Object System.Collections.Generic.List[string]
$md.Add("# Include-First Companion Import Report")
$md.Add("")
$md.Add(("- Generated: ``{0}``" -f $report.generated_at))
$md.Add(("- WhatIfOnly: ``{0}``" -f $report.what_if_only))
$md.Add(("- Include-first records seen: ``{0}``" -f $report.include_first_records_seen))
$md.Add(("- Existing source files: ``{0}``" -f $report.include_first_existing_source_files))
$md.Add(("- Package roots detected: ``{0}``" -f $report.package_roots_detected))
$md.Add(("- Companion files planned: ``{0}``" -f $report.companion_files_planned))
$md.Add(("- Companion files copied: ``{0}``" -f $report.companion_files_copied))
$md.Add(("- Skipped too large: ``{0}``" -f $report.skipped_too_large))
$md.Add(("- Skipped binary/disallowed: ``{0}``" -f $report.skipped_binary_or_disallowed))
$md.Add(("- Packages with no companions: ``{0}``" -f $report.packages_with_no_companions))
$md.Add(("- Packages truncated by limit: ``{0}``" -f $report.packages_truncated_by_limit))
$md.Add("")
$md.Add("## Package Summary")
$md.Add("")
$md.Add("| package | entrypoint | companions copied | direct refs copied | scripts | references | templates | examples | skipped | notes |")
$md.Add("|---|---|---:|---:|---:|---:|---:|---:|---:|---|")

foreach ($row in $PackageRows) {
  $md.Add(("| ``{0}`` | ``{1}`` | {2} | {3} | {4} | {5} | {6} | {7} | {8} | {9} |" -f $row.package_root, $row.entrypoint, $row.copied, $row.direct_refs, $row.scripts, $row.references, $row.templates, $row.examples, $row.skipped, $row.notes))
}

$md.Add("")
$md.Add("## Planned / Copied Files")
$md.Add("")
$md.Add("| source | destination | reason | bytes |")
$md.Add("|---|---|---|---:|")

foreach ($row in $Planned) {
  $md.Add(("| ``{0}`` | ``{1}`` | {2} | {3} |" -f $row.source_path, $row.destination_path, $row.reason, $row.size_bytes))
}

if ($Skipped.Count -gt 0) {
  $md.Add("")
  $md.Add("## Skipped Files")
  $md.Add("")
  $md.Add("| source | reason |")
  $md.Add("|---|---|")
  foreach ($row in $Skipped) {
    $md.Add(("| ``{0}`` | {1} |" -f $row.source_path, $row.reason))
  }
}

$md -join "`n" | Set-Content -LiteralPath $ReportMd -Encoding UTF8

$report | ConvertTo-Json -Depth 4
