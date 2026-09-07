<#
.SYNOPSIS
    Invokes Hermes Agent LLM Gateway via loopback REST API with dual-instance support.
.PARAMETER Prompt
    The user prompt text to send to Hermes.
.PARAMETER Instance
    The instance to target: 'private' (port 8642) or 'community' (port 9642). Default: 'private'.
.PARAMETER HermesUrl
    Explicit Hermes Gateway base URL (e.g. http://127.0.0.1:8642). Overrides -Instance.
.PARAMETER ApiKey
    Explicit Hermes API key. Overrides environment file.
.PARAMETER RepoRoot
    Root directory of the repository.
.PARAMETER Model
    Model identifier to request. Default: 'hermes-agent'.
#>
param(
    [Parameter(Mandatory=$true)]
    [string]$Prompt,

    [ValidateSet("private", "community")]
    [string]$Instance = "private",

    [string]$HermesUrl,

    [string]$ApiKey,

    [string]$RepoRoot = "C:\GitDev\apexai-os-meta",

    [string]$Model = "hermes-agent"
)

$ErrorActionPreference = "Stop"

# Determine target URL
if (-not [string]::IsNullOrWhiteSpace($HermesUrl)) {
    $targetBaseUrl = $HermesUrl.TrimEnd('/')
} elseif (-not [string]::IsNullOrWhiteSpace($env:HERMES_URL)) {
    $targetBaseUrl = $env:HERMES_URL.TrimEnd('/')
} else {
    $port = if ($Instance -eq "community") { "9642" } else { "8642" }
    $targetBaseUrl = "http://127.0.0.1:$port"
}

# Determine target environment file
$instanceEnvFile = Join-Path $RepoRoot "ki-basis\.env.$Instance"
$legacyEnvFile = Join-Path $RepoRoot "ki-basis\.env"
$envFile = if (Test-Path $instanceEnvFile) { $instanceEnvFile } elseif (Test-Path $legacyEnvFile) { $legacyEnvFile } else { $null }

function Get-DotEnvValue([string]$Path, [string]$Name) {
    if (-not (Test-Path $Path)) { return $null }
    $line = Get-Content -LiteralPath $Path |
        Where-Object { $_ -match "^\s*$([regex]::Escape($Name))=" } |
        Select-Object -Last 1
    if (-not $line) { return $null }
    $value = ($line -split "=", 2)[1].Trim()
    if (($value.StartsWith('"') -and $value.EndsWith('"')) -or
        ($value.StartsWith("'") -and $value.EndsWith("'"))) {
        $value = $value.Substring(1, $value.Length - 2)
    }
    return $value
}

$key = $ApiKey
if ([string]::IsNullOrWhiteSpace($key)) {
    $key = $env:HERMES_API_SERVER_KEY
}
if ([string]::IsNullOrWhiteSpace($key) -and $envFile) {
    $key = Get-DotEnvValue -Path $envFile -Name "HERMES_API_SERVER_KEY"
}
if ([string]::IsNullOrWhiteSpace($key)) {
    throw "HERMES_API_SERVER_KEY could not be resolved from -ApiKey, env:HERMES_API_SERVER_KEY, or $instanceEnvFile"
}

$headers = @{
    Authorization = "Bearer $key"
    "Content-Type" = "application/json"
}

$body = @{
    model = $Model
    messages = @(
        @{
            role = "user"
            content = $Prompt
        }
    )
    stream = $false
} | ConvertTo-Json -Depth 8

$endpoint = "$targetBaseUrl/v1/chat/completions"

try {
    $response = Invoke-RestMethod `
        -Method Post `
        -Uri $endpoint `
        -Headers $headers `
        -Body $body `
        -TimeoutSec 120
} catch {
    Write-Error "Hermes API request to $endpoint failed: $($_.Exception.Message)"
    exit 1
}

$content = $response.choices[0].message.content
if ([string]::IsNullOrWhiteSpace($content)) {
    Write-Error "Hermes returned no assistant content."
    exit 1
}

$content
