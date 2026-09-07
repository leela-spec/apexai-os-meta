<#
.SYNOPSIS
    Starts ki-basis infrastructure instances with dual-instance support.
.DESCRIPTION
    Supports starting Private Entrepreneurship, Community Operations, or both stacks concurrently.
    Ensures Docker engine is active, validates environment files, starts compose services with
    explicit project namespaces and .env isolation, and verifies HTTP endpoints.
.PARAMETER Instance
    The instance(s) to start: 'private', 'community', or 'all' (default: 'all').
.PARAMETER RepoRoot
    Root path of the apexai-os-meta repository.
.PARAMETER TimeoutSeconds
    Maximum seconds to wait for Docker engine to become responsive.
#>
param(
    [ValidateSet("private", "community", "all")]
    [string]$Instance = "all",
    [string]$RepoRoot = "C:\GitDev\apexai-os-meta",
    [int]$TimeoutSeconds = 90
)

$ErrorActionPreference = "Stop"
$kiBasisDir = Join-Path $RepoRoot "ki-basis"
$composeFile = Join-Path $kiBasisDir "compose.yaml"
$envPrivate = Join-Path $kiBasisDir ".env.private"
$envCommunity = Join-Path $kiBasisDir ".env.community"

if (-not (Test-Path $composeFile)) {
    throw "Compose file not found at: $composeFile"
}

Write-Host "==> Checking Docker engine status..." -ForegroundColor Cyan
$dockerReady = $false
try {
    $ver = docker info --format "{{.ServerVersion}}" 2>$null
    if ($LASTEXITCODE -eq 0 -and (-not [string]::IsNullOrWhiteSpace($ver))) {
        $dockerReady = $true
    }
} catch {
    $dockerReady = $false
}

if (-not $dockerReady) {
    Write-Host "Docker is not running. Starting Docker Desktop in background..." -ForegroundColor Yellow
    $dockerExe = "C:\Program Files\Docker\Docker\Docker Desktop.exe"
    if (-not (Test-Path $dockerExe)) {
        throw "Docker Desktop executable not found at: $dockerExe"
    }
    Start-Process -FilePath $dockerExe -WindowStyle Hidden

    $elapsed = 0
    while ($elapsed -lt $TimeoutSeconds) {
        Start-Sleep -Seconds 3
        $elapsed += 3
        try {
            $ver = docker info --format "{{.ServerVersion}}" 2>$null
            if ($LASTEXITCODE -eq 0 -and (-not [string]::IsNullOrWhiteSpace($ver))) {
                $dockerReady = $true
                break
            }
        } catch {}
        Write-Host "Waiting for Docker engine to become responsive ($elapsed s)..."
    }

    if (-not $dockerReady) {
        throw "Timed out waiting for Docker engine after $TimeoutSeconds seconds."
    }
}

function Start-Stack {
    param(
        [string]$ProjectName,
        [string]$EnvFile,
        [string]$HermesPort,
        [string]$NginxPort
    )

    if (-not (Test-Path $EnvFile)) {
        throw "Required environment file not found: $EnvFile"
    }

    Write-Host "`n==> Starting stack: $ProjectName using $EnvFile..." -ForegroundColor Cyan
    docker compose -p $ProjectName -f $composeFile --env-file $EnvFile up -d

    Write-Host "==> Verifying loopback endpoints for $ProjectName (Hermes :$HermesPort, Nginx :$NginxPort)..." -ForegroundColor Cyan
    $endpointReady = $false
    for ($i = 0; $i -lt 15; $i++) {
        try {
            $res = Invoke-WebRequest -Uri "http://127.0.0.1:$NginxPort/healthz" -UseBasicParsing -TimeoutSec 2 -ErrorAction SilentlyContinue
            if ($res.StatusCode -eq 200) {
                $endpointReady = $true
                break
            }
        } catch {}
        Start-Sleep -Seconds 2
    }

    if ($endpointReady) {
        Write-Host "[PASS] $ProjectName edge reverse proxy is healthy at http://127.0.0.1:$NginxPort" -ForegroundColor Green
    } else {
        Write-Warning "$ProjectName started, but Nginx healthz did not report ready within timeout."
    }

    docker compose -p $ProjectName -f $composeFile --env-file $EnvFile ps --format "table {{.Name}}\t{{.Status}}\t{{.Ports}}"
}

if ($Instance -eq "private" -or $Instance -eq "all") {
    Start-Stack -ProjectName "ki-basis-private" -EnvFile $envPrivate -HermesPort "8642" -NginxPort "8084"
}

if ($Instance -eq "community" -or $Instance -eq "all") {
    Start-Stack -ProjectName "ki-basis-community" -EnvFile $envCommunity -HermesPort "9642" -NginxPort "9084"
}

Write-Host "`n==> All requested ki-basis instances have been processed." -ForegroundColor Green
