param(
  [Parameter(Mandatory=$true)]
  [string]$SourceEngineId
)
$ErrorActionPreference = 'Stop'

function Fail([string]$Message, [int]$Code = 1) {
  Write-Error $Message
  exit $Code
}

$desktopCandidates = @(
  (Join-Path $env:ProgramFiles 'Docker\Docker\Docker Desktop.exe'),
  (Join-Path ${env:ProgramFiles(x86)} 'Docker\Docker\Docker Desktop.exe')
) | Where-Object { $_ -and (Test-Path $_) }
if ($desktopCandidates.Count -eq 0) {
  Fail 'Docker Desktop is not installed in a standard Windows location.' 2
}

try { $null = docker version --format '{{.Server.Version}}' } catch { Fail 'Docker CLI cannot reach a target Engine.' 3 }
$engineId = (docker info --format '{{.ID}}').Trim()
$osType = (docker info --format '{{.OSType}}').Trim()
$kernel = (docker info --format '{{.KernelVersion}}').Trim()
$operatingSystem = (docker info --format '{{.OperatingSystem}}').Trim()
$context = (docker context show).Trim()

if (-not $engineId) { Fail 'Docker target Engine ID is empty.' 4 }
if ($engineId -eq $SourceEngineId) { Fail 'Docker Desktop is addressing the same Engine ID as the Ubuntu WSL source.' 5 }
if ($osType -ne 'linux') { Fail "Docker Desktop is not in Linux-container mode: $osType" 6 }
if ($operatingSystem -notmatch 'Docker Desktop') { Fail "Target Engine does not identify as Docker Desktop: $operatingSystem" 7 }
if ($kernel -match '(?i)microsoft.*WSL|WSL2') {
  Fail "Docker Desktop appears to use the WSL2 backend ($kernel). Configure Docker Desktop to use Hyper-V before continuing." 8
}

Write-Host "DOCKER_DESKTOP_PATH=$($desktopCandidates[0])"
Write-Host "DOCKER_CONTEXT=$context"
Write-Host "SOURCE_ENGINE_ID=$SourceEngineId"
Write-Host "TARGET_ENGINE_ID=$engineId"
Write-Host "TARGET_OS_TYPE=$osType"
Write-Host "TARGET_KERNEL=$kernel"
Write-Host "TARGET_OPERATING_SYSTEM=$operatingSystem"
Write-Host 'DOCKER DESKTOP TARGET GATE PASS'
