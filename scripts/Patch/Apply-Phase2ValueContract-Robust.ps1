param(
  [string]$RepoRoot = "C:\GitDev\apexai-os-meta",
  [string]$PatchDir = "apex-meta\handoff\Apex-Kb_Lifecycle_Analysis\phase2-value-contract",
  [switch]$NoPush,
  [switch]$ForceFallback
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

function Find-Python {
  $candidates = @(
    @("py", "-3"),
    @("python", ""),
    @("python3", "")
  )

  foreach ($candidate in $candidates) {
    $exe = $candidate[0]
    $arg = $candidate[1]
    try {
      if ($arg -eq "") {
        & $exe --version *> $null
      } else {
        & $exe $arg --version *> $null
      }
      if ($LASTEXITCODE -eq 0) {
        return $candidate
      }
    } catch {
      continue
    }
  }

  throw "No Python executable found. Install Python or make py/python/python3 available on PATH."
}

Set-Location -LiteralPath $RepoRoot

$scriptPath = Join-Path $RepoRoot "scripts\apply_phase2_value_contract_robust.py"
if (-not (Test-Path -LiteralPath $scriptPath)) {
  throw "Missing helper script: $scriptPath"
}

$python = Find-Python
$exe = $python[0]
$prefixArg = $python[1]

$argsList = @()
if ($prefixArg -ne "") { $argsList += $prefixArg }
$argsList += $scriptPath
$argsList += "--repo-root"
$argsList += $RepoRoot
$argsList += "--patch-dir"
$argsList += $PatchDir
if ($NoPush) { $argsList += "--no-push" }
if ($ForceFallback) { $argsList += "--force-fallback" }

Write-Host "Running deterministic robust patch applier:"
Write-Host ($exe + " " + ($argsList -join " "))

& $exe @argsList
if ($LASTEXITCODE -ne 0) {
  throw "Robust patch applier failed with exit code $LASTEXITCODE"
}
