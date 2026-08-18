<#
.SYNOPSIS
    YouTube-to-Whisper Autonomous Pipeline
.DESCRIPTION
    Downloads audio-only from a YouTube video/channel, runs local Whisper transcription,
    saves structured transcripts (.txt, .srt, .json, .md), and generates a downstream AI trigger payload.
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory=$false)]
    [string]$VideoUrl,

    [string]$Model = "base",
    [string]$Language = "",
    [string]$AudioDir = "artifacts\audio",
    [string]$OutputDir = "artifacts\transcripts",
    [string]$StateFile = "state\processed_videos.json",
    [switch]$KeepAudio
)

$ErrorActionPreference = "Stop"

$repoRoot = $PSScriptRoot | Split-Path -Parent
$globalBin = "C:\ProgramData\AI-Tools\bin"
$localToolsDir = Join-Path $PSScriptRoot "tools"

# Resolve tools from Global AI-Tools, Local Tools, or PATH
$ytdlpCmd = Get-Command yt-dlp.exe -ErrorAction SilentlyContinue
$ffmpegCmd = Get-Command ffmpeg.exe -ErrorAction SilentlyContinue

$ytdlp = if (Test-Path (Join-Path $globalBin "yt-dlp.exe")) { Join-Path $globalBin "yt-dlp.exe" } elseif (Test-Path (Join-Path $localToolsDir "yt-dlp.exe")) { Join-Path $localToolsDir "yt-dlp.exe" } elseif ($ytdlpCmd) { $ytdlpCmd.Source } else { $null }
$ffmpeg = if (Test-Path (Join-Path $globalBin "ffmpeg.exe")) { Join-Path $globalBin "ffmpeg.exe" } elseif (Test-Path (Join-Path $localToolsDir "ffmpeg.exe")) { Join-Path $localToolsDir "ffmpeg.exe" } elseif ($ffmpegCmd) { $ffmpegCmd.Source } else { $null }
$transcribeScript = if (Test-Path (Join-Path $globalBin "transcribe_audio.py")) { Join-Path $globalBin "transcribe_audio.py" } elseif (Test-Path (Join-Path $localToolsDir "transcribe_audio.py")) { Join-Path $localToolsDir "transcribe_audio.py" } else { (Join-Path $globalBin "transcribe_audio.py") }
$ffmpegDir = if ($ffmpeg) { Split-Path -Parent $ffmpeg } else { $globalBin }

# Validate tools
if (-not $ytdlp -or -not (Test-Path $ytdlp)) { throw "yt-dlp.exe not found in $globalBin or PATH" }
if (-not $ffmpeg -or -not (Test-Path $ffmpeg)) { throw "ffmpeg.exe not found in $globalBin or PATH" }
if (-not (Test-Path $transcribeScript)) { throw "transcribe_audio.py not found at $transcribeScript" }

# Find node runtime if available
$nodePath = "C:\Users\gehma\AppData\Local\Programs\ApexNode\node-v24.18.0-win-x64\node.exe"
$jsRuntimeArg = @()
if (Test-Path $nodePath) {
    $jsRuntimeArg = @("--js-runtimes", "node:$nodePath")
} else {
    $nodeCmd = Get-Command node -ErrorAction SilentlyContinue
    if ($nodeCmd) {
        $jsRuntimeArg = @("--js-runtimes", "node:$($nodeCmd.Source)")
    }
}

# Ensure directories exist
$audioPath = Join-Path $repoRoot $AudioDir
$outputPath = Join-Path $repoRoot $OutputDir
$statePath = Join-Path $repoRoot $StateFile

if (-not (Test-Path $audioPath)) { New-Item -ItemType Directory -Path $audioPath -Force | Out-Null }
if (-not (Test-Path $outputPath)) { New-Item -ItemType Directory -Path $outputPath -Force | Out-Null }

# Load state
$state = @{ processed = @() }
if (Test-Path $statePath) {
    try {
        $state = Get-Content $statePath -Raw | ConvertFrom-Json
        if (-not $state.processed) { $state = @{ processed = @() } }
    } catch {
        $state = @{ processed = @() }
    }
}

if ([string]::IsNullOrWhiteSpace($VideoUrl)) {
    throw "Please provide a -VideoUrl to process."
}

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "  YouTube-to-Whisper Local Execution Pipeline" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "Target URL:    $VideoUrl" -ForegroundColor Yellow
Write-Host "Whisper Model: $Model (Local CPU / CTranslate2)" -ForegroundColor Yellow

# Step 1: Query Video Metadata
Write-Host "`n[1/4] Fetching video metadata..." -ForegroundColor Cyan
$metaArgs = @("--dump-json", "--no-playlist") + $jsRuntimeArg + @($VideoUrl)
$metaJsonRaw = & $ytdlp $metaArgs
if (-not $metaJsonRaw) {
    throw "Failed to fetch metadata for $VideoUrl"
}
$meta = $metaJsonRaw | ConvertFrom-Json
$videoId = $meta.id
$videoTitle = $meta.title
$channel = if ($meta.uploader) { $meta.uploader } else { $meta.channel }
$duration = $meta.duration

Write-Host "  -> Video ID:    $videoId" -ForegroundColor Green
Write-Host "  -> Title:       $videoTitle" -ForegroundColor Green
Write-Host "  -> Channel:     $channel" -ForegroundColor Green
Write-Host "  -> Duration:    $($meta.duration_string) ($duration seconds)" -ForegroundColor Green

# Step 2: Download Audio Only
Write-Host "`n[2/4] Downloading audio stream (AUDIO ONLY - NO VIDEO)..." -ForegroundColor Cyan
$targetAudioFile = Join-Path $audioPath "$videoId.mp3"

$dlArgs = @(
    "--extract-audio",
    "--audio-format", "mp3",
    "--audio-quality", "0",
    "--ffmpeg-location", $ffmpegDir,
    "--extractor-args", "youtube:player_client=android,mweb",
    "--output", (Join-Path $audioPath "%(id)s.%(ext)s"),
    "--no-playlist",
    "--no-warnings"
) + $jsRuntimeArg + @($VideoUrl)

& $ytdlp $dlArgs
if (-not (Test-Path $targetAudioFile)) {
    throw "Audio file download failed. File not found at $targetAudioFile"
}

$audioSizeMB = [math]::Round((Get-Item $targetAudioFile).Length / 1MB, 2)
Write-Host "  -> Audio downloaded: $targetAudioFile ($audioSizeMB MB)" -ForegroundColor Green

# Step 3: Run Local Whisper Transcription
Write-Host "`n[3/4] Running 100% Local Whisper Transcription..." -ForegroundColor Cyan
$videoOutputDir = Join-Path $outputPath $videoId
if (-not (Test-Path $videoOutputDir)) { New-Item -ItemType Directory -Path $videoOutputDir -Force | Out-Null }

$pyArgs = @(
    $transcribeScript,
    "--input", $targetAudioFile,
    "--output_dir", $videoOutputDir,
    "--model", $Model,
    "--device", "cpu",
    "--compute_type", "int8"
)

if (-not [string]::IsNullOrWhiteSpace($Language)) {
    $pyArgs += @("--language", $Language)
}

$proc = Start-Process -FilePath "python" -ArgumentList $pyArgs -NoNewWindow -Wait -PassThru
if ($proc.ExitCode -ne 0) {
    throw "Whisper transcription failed with exit code $($proc.ExitCode)"
}

# Step 4: Macro -> Meso -> Micro Knowledge Synthesis
Write-Host "`n[4/5] Synthesizing Macro/Meso/Micro Knowledge Wiki..." -ForegroundColor Cyan
$synthScript = Join-Path $PSScriptRoot "synthesize_transcript.py"
$transcriptSrtFile = Join-Path $videoOutputDir "$videoId.srt"
$transcriptJsonFile = Join-Path $videoOutputDir "$videoId.json"
$transcriptMdFile = Join-Path $videoOutputDir "$videoId.md"

if (Test-Path $synthScript) {
    $titleArg = "$videoTitle - Knowledge Synthesis"
    $synthArgs = @(
        $synthScript,
        "--transcript", $transcriptSrtFile,
        "--output_dir", $videoOutputDir,
        "--slug", $videoId,
        "--title", $titleArg
    )
    $procSynth = Start-Process -FilePath "python" -ArgumentList $synthArgs -NoNewWindow -Wait -PassThru
}

# Step 5: Downstream AI Task Payload Generation & State Update
Write-Host "`n[5/5] Generating Downstream AI Trigger Payload and Updating State..." -ForegroundColor Cyan

$transcriptText = ""
if (Test-Path (Join-Path $videoOutputDir "$videoId.txt")) {
    $transcriptText = Get-Content (Join-Path $videoOutputDir "$videoId.txt") -Raw -Encoding utf8
}

$knowledgeWikiFile = Join-Path $videoOutputDir "$($videoId)_knowledge_wiki.md"

$aiTaskPayload = [PSCustomObject]@{
    event_type       = "YOUTUBE_TRANSCRIPT_AND_SYNTHESIS_COMPLETED"
    timestamp        = (Get-Date).ToUniversalTime().ToString("o")
    video_id         = $videoId
    video_title      = $videoTitle
    channel          = $channel
    video_url        = "https://www.youtube.com/watch?v=$videoId"
    duration_seconds = $duration
    model_used       = $Model
    transcript_files = [PSCustomObject]@{
        knowledge_wiki = if (Test-Path $knowledgeWikiFile) { $knowledgeWikiFile } else { $null }
        markdown = $transcriptMdFile
        subtitles = $transcriptSrtFile
        raw_json = $transcriptJsonFile
    }
    transcript_preview = if ($transcriptText.Length -gt 500) { $transcriptText.Substring(0, 500) + "..." } else { $transcriptText }
    downstream_guardrail_prompt = "Review the synthesized knowledge wiki for $channel ('$videoTitle') and update project context."
}

$aiPayloadFile = Join-Path $repoRoot "artifacts\pending_ai_task.json"
$aiTaskPayload | ConvertTo-Json -Depth 6 | Set-Content -Path $aiPayloadFile -Encoding utf8

# Update State File
$stateEntry = [PSCustomObject]@{
    id           = $videoId
    title        = $videoTitle
    channel      = $channel
    url          = "https://www.youtube.com/watch?v=$videoId"
    duration_str = $meta.duration_string
    processed_at = (Get-Date).ToUniversalTime().ToString("o")
    model        = $Model
    artifacts_dir = $videoOutputDir
}

$existing = @($state.processed | Where-Object { $_.id -ne $videoId })
$existing += $stateEntry
$state.processed = $existing
$state | ConvertTo-Json -Depth 5 | Set-Content -Path $statePath -Encoding utf8

# Cleanup audio if requested
if (-not $KeepAudio) {
    Remove-Item $targetAudioFile -Force -ErrorAction SilentlyContinue
    Write-Host "  -> Cleaned up temporary audio cache file." -ForegroundColor Gray
}

Write-Host "`n==========================================================" -ForegroundColor Green
Write-Host "  PIPELINE COMPLETE - 100% LOCAL AND FREE" -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Green
Write-Host "Transcript Artifacts: $videoOutputDir" -ForegroundColor White
Write-Host "Downstream AI Task:   $aiPayloadFile" -ForegroundColor White

return $aiTaskPayload
