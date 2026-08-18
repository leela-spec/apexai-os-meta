<#
.SYNOPSIS
    Syncs and queries the latest video links from configured YouTube channels and playlists.
.DESCRIPTION
    Reads state/watched_sources.json, queries yt-dlp for the latest uploads, and outputs state/latest_discovered_videos.json.
#>

[CmdletBinding()]
param(
    [string]$ConfigFile = "state\watched_sources.json",
    [string]$OutputFile = "state\latest_discovered_videos.json",
    [int]$LimitPerSource = 5
)

$ErrorActionPreference = "Stop"
$skillRoot = $PSScriptRoot | Split-Path -Parent
$globalBin = "C:\ProgramData\AI-Tools\bin"
$localToolsDir = Join-Path $PSScriptRoot "tools"
$ytdlpCmd = Get-Command yt-dlp.exe -ErrorAction SilentlyContinue
$ytdlp = if (Test-Path (Join-Path $globalBin "yt-dlp.exe")) { Join-Path $globalBin "yt-dlp.exe" } elseif (Test-Path (Join-Path $localToolsDir "yt-dlp.exe")) { Join-Path $localToolsDir "yt-dlp.exe" } elseif ($ytdlpCmd) { $ytdlpCmd.Source } else { $null }

if (-not $ytdlp -or -not (Test-Path $ytdlp)) {
    throw "yt-dlp binary not found at $globalBin or PATH"
}

$resolvedConfigFile = if ([System.IO.Path]::IsPathRooted($ConfigFile)) { $ConfigFile } else { Join-Path $skillRoot $ConfigFile }
if (-not (Test-Path $resolvedConfigFile)) {
    # Fallback to config folder
    $resolvedConfigFile = Join-Path $skillRoot "config\watched_sources.json"
}

$resolvedOutputFile = if ([System.IO.Path]::IsPathRooted($OutputFile)) { $OutputFile } else { Join-Path $skillRoot $OutputFile }

if (-not (Test-Path $resolvedConfigFile)) {
    throw "Config file not found at $resolvedConfigFile"
}

$config = Get-Content $resolvedConfigFile -Raw | ConvertFrom-Json
$allDiscovered = @()

Write-Host "=== Polling Configured YouTube Sources ===" -ForegroundColor Cyan

foreach ($source in $config.sources) {
    if (-not $source.enabled) {
        Write-Host "Skipping disabled source: $($source.name)" -ForegroundColor Yellow
        continue
    }

    Write-Host "Checking [$($source.type)]: $($source.name) ($($source.url))..." -ForegroundColor Gray
    
    $argsList = @(
        "--flat-playlist",
        "--dump-json",
        "--playlist-items", "1-$LimitPerSource",
        $source.url
    )

    $output = & $ytdlp $argsList
    $items = @()

    foreach ($line in ($output -split "`r?`n")) {
        if ([string]::IsNullOrWhiteSpace($line)) { continue }
        try {
            $json = $line | ConvertFrom-Json
            $items += [PSCustomObject]@{
                id           = $json.id
                title        = $json.title
                url          = "https://www.youtube.com/watch?v=$($json.id)"
                duration     = $json.duration
                duration_str = $json.duration_string
                uploader     = if ($json.uploader) { $json.uploader } else { $source.name }
                source_id    = $source.id
                source_name  = $source.name
                discovered_at = (Get-Date).ToUniversalTime().ToString("o")
            }
        } catch {
            Write-Warning "Failed to parse metadata line: $line"
        }
    }

    Write-Host "  -> Found $($items.Count) recent video(s)" -ForegroundColor Green
    $allDiscovered += $items
}

$result = [PSCustomObject]@{
    synced_at = (Get-Date).ToUniversalTime().ToString("o")
    total_videos = $allDiscovered.Count
    videos = $allDiscovered
}

$resultJson = $result | ConvertTo-Json -Depth 5
Set-Content -Path $resolvedOutputFile -Value $resultJson -Encoding utf8

Write-Host "Successfully saved latest $($allDiscovered.Count) video links to $resolvedOutputFile" -ForegroundColor Green
return $allDiscovered
