param(
    [Parameter(Mandatory=$true)]
    [string]$Prompt,

    [string]$RepoRoot = "C:\GitDev\apexai-os-meta",

    [string]$Model = "hermes-agent"
)

$ErrorActionPreference = "Stop"

$envFile = Join-Path $RepoRoot "ki-basis\.env"
if (-not (Test-Path $envFile)) {
    throw "Missing ignored environment file: $envFile"
}

function Get-DotEnvValue([string]$Path, [string]$Name) {
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

$key = Get-DotEnvValue -Path $envFile -Name "HERMES_API_SERVER_KEY"
if ([string]::IsNullOrWhiteSpace($key)) {
    throw "HERMES_API_SERVER_KEY is missing from $envFile"
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

try {
    $response = Invoke-RestMethod `
        -Method Post `
        -Uri "http://127.0.0.1:8642/v1/chat/completions" `
        -Headers $headers `
        -Body $body `
        -TimeoutSec 120
} catch {
    Write-Error "Hermes API request failed: $($_.Exception.Message)"
    exit 1
}

$content = $response.choices[0].message.content
if ([string]::IsNullOrWhiteSpace($content)) {
    Write-Error "Hermes returned no assistant content."
    exit 1
}

$content
