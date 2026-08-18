param(
    [Parameter(Mandatory = $true)]
    [string]$RepoRoot,
    [switch]$Force
)

$ErrorActionPreference = "Stop"
$BundleRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$SourceSkill = Join-Path $BundleRoot "current\skill-source"
$SourceResearch = Join-Path $BundleRoot "current\research-v2"
$TargetSkill = Join-Path $RepoRoot ".claude\skills\transcript-to-knowledge"
$TargetResearch = Join-Path $RepoRoot "apex-meta\validation\transcript-to-knowledge-20260818\v2"

if (-not (Test-Path $RepoRoot)) {
    throw "RepoRoot does not exist: $RepoRoot"
}

if ((Test-Path $TargetSkill) -and -not $Force) {
    throw "Target Skill already exists. Re-run with -Force only if you intend to replace it: $TargetSkill"
}

if ((Test-Path $TargetResearch) -and -not $Force) {
    throw "Target research folder already exists. Re-run with -Force only if you intend to replace it: $TargetResearch"
}

if ($Force) {
    if (Test-Path $TargetSkill) { Remove-Item $TargetSkill -Recurse -Force }
    if (Test-Path $TargetResearch) { Remove-Item $TargetResearch -Recurse -Force }
}

New-Item -ItemType Directory -Force -Path (Split-Path -Parent $TargetSkill) | Out-Null
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $TargetResearch) | Out-Null
Copy-Item $SourceSkill $TargetSkill -Recurse
Copy-Item $SourceResearch $TargetResearch -Recurse

Write-Host "Restored transcript-to-knowledge v2 Skill and research snapshot."
Write-Host "Skill:    $TargetSkill"
Write-Host "Research: $TargetResearch"
