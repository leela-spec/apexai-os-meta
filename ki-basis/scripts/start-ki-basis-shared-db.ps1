<#
.SYNOPSIS
    Start the PRIVATE ki-basis stack on the WSL2-native "Apex" engine (post-ADR-002 / T10).

.DESCRIPTION
    Correct replacement for the superseded start-ki-basis.ps1 (which targeted the pre-consolidation
    compose.yaml and is now fail-closed). Brings the private stack up from compose.shared-db.yaml,
    project 'ki-basis', against the shared PostgreSQL cluster (external network shared-db-net).

    Docker Desktop is retired, so the engine lives inside WSL; every docker call is routed through
    wsl.exe. Hermes uses BIND mounts under this file, so `up` re-attaches the live ~7.9 GB of bot
    state and never wipes it (see FINDINGS-t10-hermes-compose-drift-2026-09-28.md).

    The COMMUNITY stack is a separate compose project managed from C:\GitDev\lika-community and is
    NOT touched by this script.

.PARAMETER TimeoutSeconds
    How long to wait for Hermes /health to return 200 (default 90).
.PARAMETER Distro
    WSL distro hosting the Apex engine (default 'Ubuntu').

.EXAMPLE
    powershell -ExecutionPolicy Bypass -File .\start-ki-basis-shared-db.ps1
#>
[CmdletBinding()]
param(
    [int]$TimeoutSeconds = 90,
    [string]$Distro = "Ubuntu"
)
$ErrorActionPreference = "Stop"

# Absolute paths as seen INSIDE WSL. The live ki-basis-hermes was created from exactly this file
# (verified via its com.docker.compose.project.config_files label), so `up` here matches live.
$ComposeFile = "/mnt/c/GitDev/apexai-os-meta/ki-basis/compose.shared-db.yaml"
$EnvFile     = "/mnt/c/GitDev/apexai-os-meta/ki-basis/.env.shared-db"
$Project     = "ki-basis"

# Run a docker/CLI command as root in the Apex engine, suppress its output, return its exit code.
function Invoke-WslQuiet {
    param([string[]]$CmdArgs)
    & wsl.exe -d $Distro -u root -- @CmdArgs *> $null
    return $LASTEXITCODE
}

Write-Host "==> Checking the WSL2 '$Distro' Apex Docker engine..." -ForegroundColor Cyan
if ((Invoke-WslQuiet @('docker','info')) -ne 0) {
    throw "Docker engine in WSL ($Distro) is unreachable. Try:  wsl -d $Distro -u root -- docker info"
}

Write-Host "==> Verifying external 'shared-db-net' (shared PostgreSQL cluster network)..." -ForegroundColor Cyan
if ((Invoke-WslQuiet @('docker','network','inspect','shared-db-net')) -ne 0) {
    throw "External network 'shared-db-net' not found. Start the shared Postgres stack (owns 'ki-basis-shared-postgres') first, then re-run."
}

Write-Host "==> Starting PRIVATE stack '$Project' from compose.shared-db.yaml ..." -ForegroundColor Cyan
& wsl.exe -d $Distro -u root -- docker compose -f $ComposeFile --env-file $EnvFile -p $Project up -d
if ($LASTEXITCODE -ne 0) { throw "docker compose up failed - see output above." }

Write-Host "==> Waiting for Hermes health (timeout ${TimeoutSeconds}s)..." -ForegroundColor Cyan
$deadline = (Get-Date).AddSeconds($TimeoutSeconds)
$ready = $false
while ((Get-Date) -lt $deadline) {
    $code = & wsl.exe -d $Distro -u root -- curl -s -o /dev/null -w '%{http_code}' --max-time 3 http://127.0.0.1:8642/health 2>$null
    if ($code -eq "200") { $ready = $true; break }
    Start-Sleep -Seconds 3
}
if ($ready) {
    Write-Host "[PASS] Hermes gateway healthy at http://127.0.0.1:8642/health" -ForegroundColor Green
} else {
    Write-Warning "Stack started, but Hermes /health did not return 200 within ${TimeoutSeconds}s (it may still be booting)."
}

Write-Host "==> Private stack state:" -ForegroundColor Cyan
& wsl.exe -d $Distro -u root -- docker compose -f $ComposeFile --env-file $EnvFile -p $Project ps

Write-Host "`n==> Done. Community stack is separate (C:\GitDev\lika-community)." -ForegroundColor Green
