param([ValidateSet('private')][string]$Instance = 'private')
$ErrorActionPreference='Stop'
$root=Split-Path -Parent $PSScriptRoot
$compose=Join-Path $root 'compose.yaml'
$envFile=Join-Path $root '.env.private'
$project='ki-basis'
$argsBase=@('--context','desktop-linux','compose','-p',$project,'--project-directory',$root,'-f',$compose,'--env-file',$envFile)
if(-not (Test-Path -LiteralPath $envFile)) { throw "Missing environment file: $envFile" }
& docker @argsBase stop
if($LASTEXITCODE -ne 0) { throw "$project could not stop cleanly." }
& docker @argsBase ps
if($LASTEXITCODE -ne 0) { throw 'Could not verify container status.' }
