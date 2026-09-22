param([int]$TimeoutSeconds = 180, [ValidateSet('private')][string]$Instance = 'private')
$ErrorActionPreference='Stop'
$root=Split-Path -Parent $PSScriptRoot
$compose=Join-Path $root 'compose.yaml'
$envFile=Join-Path $root '.env.private'
$project='ki-basis'
$argsBase=@('--context','desktop-linux','compose','-p',$project,'--project-directory',$root,'-f',$compose,'--env-file',$envFile)
if(-not (Test-Path -LiteralPath $envFile)) { throw "Missing environment file: $envFile" }
& docker @argsBase config --quiet
if($LASTEXITCODE -ne 0) { throw 'Compose configuration is invalid.' }
& docker @argsBase up -d --pull never
if($LASTEXITCODE -ne 0) { throw "$project could not start." }
$ports=@(8010,8082,8086)
$deadline=(Get-Date).AddSeconds($TimeoutSeconds)
do {
    $pending=@()
    foreach($port in $ports) {
        try { $null=Invoke-WebRequest -Uri "http://127.0.0.1:$port" -UseBasicParsing -TimeoutSec 3 } catch { $pending+=$port }
    }
    if($pending.Count -eq 0) { break }
    Start-Sleep -Seconds 3
} while((Get-Date) -lt $deadline)
if($pending.Count -gt 0) { throw "Applications not ready on ports: $($pending -join ', '). Inspect docker compose logs." }
& docker @argsBase ps
if($LASTEXITCODE -ne 0) { throw 'Could not verify container status.' }
