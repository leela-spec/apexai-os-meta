<#
.SYNOPSIS
    Stops ki-basis infrastructure instances with dual-instance safety.
.DESCRIPTION
    Stops Private Entrepreneurship, Community Operations, or both stacks gracefully.
    Stopping an individual instance (-Instance private or community) NEVER terminates Docker Desktop.
    Docker Desktop engine is only stopped when -Instance all AND -StopEngine are explicitly passed.
.PARAMETER Instance
    The instance(s) to stop: 'private', 'community', or 'all' (default: 'all').
.PARAMETER RepoRoot
    Root directory of the repository.
.PARAMETER StopEngine
    Explicit switch to terminate the host Docker Desktop engine. Only active when -Instance all.
#>
param(
    [ValidateSet("private", "community", "all")]
    [string]$Instance = "all",
    [string]$RepoRoot = "C:\GitDev\apexai-os-meta",
    [switch]$StopEngine
)

$ErrorActionPreference = "Stop"
$kiBasisDir = Join-Path $RepoRoot "ki-basis"
$composeFile = Join-Path $kiBasisDir "compose.yaml"

if (-not (Test-Path $composeFile)) {
    throw "Compose file not found at: $composeFile"
}

function Stop-Stack {
    param([string]$ProjectName, [string]$EnvFile)
    if (Test-Path $EnvFile) {
        Write-Host "==> Gracefully stopping stack: $ProjectName..." -ForegroundColor Cyan
        docker compose -p $ProjectName -f $composeFile --env-file $EnvFile stop
    }
}

if ($Instance -eq "private" -or $Instance -eq "all") {
    Stop-Stack -ProjectName "ki-basis-private" -EnvFile (Join-Path $kiBasisDir ".env.private")
}

if ($Instance -eq "community" -or $Instance -eq "all") {
    Stop-Stack -ProjectName "ki-basis-community" -EnvFile (Join-Path $kiBasisDir ".env.community")
}

if ($Instance -eq "all" -and $StopEngine) {
    Write-Host "==> Shutting down Docker Desktop engine (-StopEngine requested)..." -ForegroundColor Cyan
    $dockerCli = "C:\Program Files\Docker\Docker\DockerCli.exe"
    if (Test-Path $dockerCli) {
        & $dockerCli -Shutdown 2>$null
    } else {
        Stop-Process -Name "Docker Desktop", "com.docker.backend" -Force -ErrorAction SilentlyContinue
    }
    Write-Host "==> Docker Desktop shutdown signal sent." -ForegroundColor Green
} else {
    Write-Host "==> Containers stopped; Docker Desktop left running in background." -ForegroundColor Green
}
