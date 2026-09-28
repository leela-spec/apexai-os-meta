<#
.SYNOPSIS
    Stop the PRIVATE ki-basis stack on the WSL2-native "Apex" engine (post-ADR-002 / T10).

.DESCRIPTION
    Correct replacement for the superseded stop-ki-basis.ps1 (now fail-closed). Operates on
    compose.shared-db.yaml / project 'ki-basis' via the WSL2 engine.

    Default action is `stop` (containers halted, kept). `-Down` uses `docker compose down`
    (removes the private containers and the ki-basis-net bridge). Neither action removes:
      * the external 'shared-db-net' (external networks are never removed by `down`),
      * the shared 'ki-basis-shared-postgres' (a different compose project), or
      * any data - Hermes is on BIND mounts and the other services use named volumes,
        which `down` leaves intact (no `-v` is ever passed).

    The COMMUNITY stack (C:\GitDev\lika-community) is a separate project and is NOT touched.

.PARAMETER Down
    Use `docker compose down` instead of `stop`.
.PARAMETER Distro
    WSL distro hosting the Apex engine (default 'Ubuntu').
#>
[CmdletBinding()]
param(
    [switch]$Down,
    [string]$Distro = "Ubuntu"
)
$ErrorActionPreference = "Stop"

$ComposeFile = "/mnt/c/GitDev/apexai-os-meta/ki-basis/compose.shared-db.yaml"
$EnvFile     = "/mnt/c/GitDev/apexai-os-meta/ki-basis/.env.shared-db"
$Project     = "ki-basis"
$verb = if ($Down) { "down" } else { "stop" }

Write-Host "==> ${verb}: private stack '$Project' via compose.shared-db.yaml ..." -ForegroundColor Cyan
& wsl.exe -d $Distro -u root -- docker compose -f $ComposeFile --env-file $EnvFile -p $Project $verb
if ($LASTEXITCODE -ne 0) { throw "docker compose $verb failed - see output above." }

Write-Host "[PASS] private stack ${verb}ped. Data (Hermes binds + named volumes), shared-db-net, and the shared Postgres are untouched." -ForegroundColor Green
Write-Host "Community stack is separate (C:\GitDev\lika-community)." -ForegroundColor Green
