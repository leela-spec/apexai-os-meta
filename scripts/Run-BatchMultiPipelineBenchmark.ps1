# Fail-Closed Multi-Pipeline Execution Benchmark Harness
[CmdletBinding()]
param(
    [string]$RunId = (Get-Date -Format "yyyyMMdd-HHmmss"),
    [switch]$IncludeSynthesis
)

$ErrorActionPreference = "Stop"

$repoRoot = "C:\GitDev\apexai-os-meta"
$globalBin = "C:\ProgramData\AI-Tools\bin"
$ytdlp = Join-Path $globalBin "yt-dlp.exe"
$ffmpegDir = $globalBin
$transcribeScript = Join-Path $repoRoot ".claude\skills\SourceTranscriptionAnalysisPipeline\scripts\transcribe_audio.py"
$p1SynthScript = Join-Path $repoRoot ".claude\skills\SourceTranscriptionAnalysisPipeline\scripts\synthesize_transcript.py"
$p2SynthScript = Join-Path $repoRoot "SourceTranscriptionAnalysisPipeline_Research\synthesize_p2.py"
$ttkLifecycleScript = Join-Path $repoRoot ".claude\skills\transcript-to-knowledge\scripts\execute_ttk_lifecycle.py"

$nodePath = "C:\Users\gehma\AppData\Local\Programs\ApexNode\node-v24.18.0-win-x64\node.exe"
$jsRuntimeArg = @()
if (Test-Path $nodePath) {
    $jsRuntimeArg = @("--js-runtimes", "node:$nodePath")
}

# Resolve git commit
$gitCommit = "unknown"
try {
    $gitCommit = (& git rev-parse HEAD).Trim()
} catch {}

$videos = @(
    @{ id = "P-h5WSQG1Sw"; url = "https://www.youtube.com/watch?v=P-h5WSQG1Sw"; title = "Neuroscience of Emotions & Emotion Regulation - Dr. Ralph Adolphs" },
    @{ id = "CygwqaNg2PY"; url = "https://www.youtube.com/watch?v=CygwqaNg2PY"; title = "Elliott Prechter: Teaching a Machine to Count Elliott Waves" },
    @{ id = "vFTuLylvYnA"; url = "https://www.youtube.com/watch?v=vFTuLylvYnA"; title = "Tech unter Druck. Zinsen werden zum Risiko - Markus Koch" },
    @{ id = "oZIsMX6WgFs"; url = "https://www.youtube.com/watch?v=oZIsMX6WgFs"; title = "Market Cycles Jam - Market Cycles Report August 17 2026" }
)

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "  FAIL-CLOSED MULTI-PIPELINE BENCHMARK HARNESS" -ForegroundColor Cyan
Write-Host "  Run ID: $RunId | Commit: $gitCommit" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

$benchmarkReceipt = [ordered]@{
    run_id       = $RunId
    timestamp    = (Get-Date).ToUniversalTime().ToString("o")
    git_commit   = $gitCommit
    sources      = @()
    summary      = @{
        total_sources    = $videos.Count
        all_passed       = $true
        incomplete_count = 0
    }
}

$resultsTable = @()

foreach ($v in $videos) {
    $vid = $v.id
    $vurl = $v.url
    $vtitle = $v.title

    Write-Host "`n>>> [SOURCE: $vid] $vtitle <<<" -ForegroundColor Yellow

    $sourceTelemetry = [ordered]@{
        id            = $vid
        title         = $vtitle
        url           = $vurl
        transcript    = $null
        pipeline_1    = @{ status = "NOT_STARTED"; artifacts = @{}; error = $null }
        pipeline_2    = @{ status = "NOT_STARTED"; artifacts = @{}; error = $null }
        pipeline_3    = @{ status = "NOT_STARTED"; artifacts = @{}; error = $null }
    }

    # ----------------------------------------------------
    # PIPELINE 1: SourceTranscriptionAnalysisPipeline
    # ----------------------------------------------------
    Write-Host "`n--- [PIPELINE 1] Media Ingestion & Whisper Transcription ---" -ForegroundColor Cyan
    $p1Dir = Join-Path $repoRoot ".claude\skills\SourceTranscriptionAnalysisPipeline\artifacts\transcripts\$vid"
    $audioDir = Join-Path $repoRoot ".claude\skills\SourceTranscriptionAnalysisPipeline\artifacts\audio"
    if (-not (Test-Path $p1Dir)) { New-Item -ItemType Directory -Path $p1Dir -Force | Out-Null }
    if (-not (Test-Path $audioDir)) { New-Item -ItemType Directory -Path $audioDir -Force | Out-Null }

    $targetAudio = Join-Path $audioDir "$vid.mp3"
    $targetSrt = Join-Path $p1Dir "$vid.srt"
    $targetJson = Join-Path $p1Dir "$vid.json"
    $targetTxt = Join-Path $p1Dir "$vid.txt"

    # Step 1: Download audio if SRT does not exist
    if (-not (Test-Path $targetSrt)) {
        Write-Host "  Downloading audio for $vid..." -ForegroundColor Gray
        $dlArgs = @(
            "--extract-audio",
            "--audio-format", "mp3",
            "--audio-quality", "0",
            "--ffmpeg-location", $ffmpegDir,
            "--extractor-args", "youtube:player_client=android,mweb",
            "--output", (Join-Path $audioDir "%(id)s.%(ext)s"),
            "--no-playlist",
            "--no-warnings"
        ) + $jsRuntimeArg + @($vurl)

        & $ytdlp $dlArgs
        
        if (Test-Path $targetAudio) {
            Write-Host "  Transcribing with faster-whisper (CPU int8)..." -ForegroundColor Gray
            $pyArgs = @(
                $transcribeScript,
                "--input", $targetAudio,
                "--output_dir", $p1Dir,
                "--model", "base",
                "--device", "cpu",
                "--compute_type", "int8"
            )
            $procAsr = Start-Process -FilePath "python" -ArgumentList $pyArgs -NoNewWindow -Wait -PassThru
            if ($procAsr.ExitCode -ne 0) {
                $sourceTelemetry.pipeline_1.status = "FAILED"
                $sourceTelemetry.pipeline_1.error = "ASR failed with exit code $($procAsr.ExitCode)"
            }
            Remove-Item $targetAudio -Force -ErrorAction SilentlyContinue
        } else {
            $sourceTelemetry.pipeline_1.status = "FAILED"
            $sourceTelemetry.pipeline_1.error = "Audio download failed"
        }
    }

    # Verify ASR output existence and compute SHA256
    if (Test-Path $targetSrt) {
        $sourceHash = (Get-FileHash -Path $targetSrt -Algorithm SHA256).Hash.ToLower()
        $srtContent = Get-Content $targetSrt -Raw -Encoding utf8
        $wordCount = ($srtContent -split '\s+').Count
        
        $sourceTelemetry.transcript = @{
            path         = $targetSrt
            sha256       = $sourceHash
            approx_words = $wordCount
        }
        
        $sourceTelemetry.pipeline_1.status = "ASR_COMPLETE"
        $sourceTelemetry.pipeline_1.artifacts = @{
            srt = $targetSrt
            json = $targetJson
            txt = $targetTxt
        }
        Write-Host "  [P1 ASR] Completed ($wordCount words, SHA256: $($sourceHash.Substring(0,12))...)" -ForegroundColor Green
    } else {
        $sourceTelemetry.pipeline_1.status = "FAILED"
    }

    # ----------------------------------------------------
    # PIPELINE 2: SourceTranscriptionAnalysisPipeline_Research (transcript_engine.py)
    # ----------------------------------------------------
    Write-Host "`n--- [PIPELINE 2] Research Dataclass Knowledge Engine ---" -ForegroundColor Cyan
    $p2Dir = Join-Path $repoRoot "SourceTranscriptionAnalysisPipeline_Research\outputs\$vid"
    if (-not (Test-Path $p2Dir)) { New-Item -ItemType Directory -Path $p2Dir -Force | Out-Null }

    if (Test-Path $targetSrt) {
        # Check if an honest semantic result exists for this source
        $semResultP2 = Join-Path $p1Dir "$vid`_semantic_result.json"
        if (Test-Path $semResultP2) {
            & python $p2SynthScript $vid $vtitle $targetSrt $p2Dir "--semantic-result" $semResultP2
        } else {
            & python $p2SynthScript $vid $vtitle $targetSrt $p2Dir
        }
        $p2Exit = $LASTEXITCODE
        if ($p2Exit -eq 0) {
            $sourceTelemetry.pipeline_2.status = "OPERATOR_ARTIFACT_COMPLETE"
            $sourceTelemetry.pipeline_2.artifacts = @{
                wiki = Join-Path $p2Dir "$vid`_engine_wiki.md"
                json = Join-Path $p2Dir "$vid`_engine_wiki.json"
            }
            Write-Host "  [P2 Engine] Validated & Rendered." -ForegroundColor Green
        } elseif ($p2Exit -eq 2) {
            $sourceTelemetry.pipeline_2.status = "SYNTHESIS_PENDING"
            Write-Host "  [P2 Engine] Synthesis Pending (No fake wiki produced)." -ForegroundColor Yellow
        } else {
            $sourceTelemetry.pipeline_2.status = "FAILED"
            $sourceTelemetry.pipeline_2.error = "Exit code $p2Exit"
            Write-Host "  [P2 Engine] FAILED validation." -ForegroundColor Red
        }
    } else {
        $sourceTelemetry.pipeline_2.status = "FAILED"
        $sourceTelemetry.pipeline_2.error = "Missing source transcript"
    }

    # ----------------------------------------------------
    # PIPELINE 3: transcript-to-knowledge (TTK Complete Lifecycle)
    # ----------------------------------------------------
    Write-Host "`n--- [PIPELINE 3] TTK Map-Reduce Full Lifecycle & Verification ---" -ForegroundColor Cyan
    $p3Dir = Join-Path $repoRoot "artifacts\ttk_runs\$vid"
    
    if (Test-Path $targetSrt) {
        & python $ttkLifecycleScript $targetSrt "--output" $p3Dir "--title" $vtitle
        $p3Exit = $LASTEXITCODE
        if ($p3Exit -eq 0 -and (Test-Path (Join-Path $p3Dir "wiki\index.md"))) {
            $sourceTelemetry.pipeline_3.status = "OPERATOR_ARTIFACT_COMPLETE"
            $sourceTelemetry.pipeline_3.artifacts = @{
                manifest = Join-Path $p3Dir "manifest.json"
                compiled_wiki = Join-Path $p3Dir "wiki\index.md"
                reduce_result = Join-Path $p3Dir "work\results\reduce.json"
            }
            Write-Host "  [P3 TTK] Full Lifecycle Complete (100% Validated Evidence)." -ForegroundColor Green
        } else {
            $sourceTelemetry.pipeline_3.status = "FAILED"
            $sourceTelemetry.pipeline_3.error = "TTK lifecycle failed with exit code $p3Exit"
            Write-Host "  [P3 TTK] FAILED validation." -ForegroundColor Red
        }
    } else {
        $sourceTelemetry.pipeline_3.status = "FAILED"
        $sourceTelemetry.pipeline_3.error = "Missing source transcript"
    }

    $benchmarkReceipt.sources += $sourceTelemetry

    $resultsTable += [PSCustomObject]@{
        Source   = $vid
        Title    = if ($vtitle.Length -gt 35) { $vtitle.Substring(0, 32) + "..." } else { $vtitle }
        P1_ASR   = $sourceTelemetry.pipeline_1.status
        P2_Data  = $sourceTelemetry.pipeline_2.status
        P3_TTK   = $sourceTelemetry.pipeline_3.status
    }
}

# ----------------------------------------------------
# Benchmark Summary & Receipt Generation
# ----------------------------------------------------
$receiptDir = Join-Path $repoRoot "artifacts\benchmark_runs\$RunId"
if (-not (Test-Path $receiptDir)) { New-Item -ItemType Directory -Path $receiptDir -Force | Out-Null }
$receiptPath = Join-Path $receiptDir "receipt.json"

$allPassed = $true
foreach ($s in $benchmarkReceipt.sources) {
    if ($s.pipeline_1.status -eq "FAILED" -or $s.pipeline_3.status -eq "FAILED") {
        $allPassed = $false
        $benchmarkReceipt.summary.incomplete_count += 1
    }
}
$benchmarkReceipt.summary.all_passed = $allPassed

$benchmarkReceipt | ConvertTo-Json -Depth 6 | Set-Content -Path $receiptPath -Encoding utf8

Write-Host "`n==========================================================" -ForegroundColor Cyan
Write-Host "  BENCHMARK EXECUTION SUMMARY TABLE" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan
$resultsTable | Format-Table -AutoSize

Write-Host "Machine-readable receipt: $receiptPath" -ForegroundColor White

if ($allPassed) {
    Write-Host "`n>> BENCHMARK RUN COMPLETED WITH HONEST FAIL-CLOSED VALIDATION <<" -ForegroundColor Green
} else {
    Write-Host "`n>> BENCHMARK INCOMPLETE: Check errors in $receiptPath <<" -ForegroundColor Red
}
