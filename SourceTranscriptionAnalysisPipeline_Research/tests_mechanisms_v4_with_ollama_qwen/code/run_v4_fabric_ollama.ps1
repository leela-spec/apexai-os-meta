<#
.SYNOPSIS
Turns a URL, local media file, or existing transcript into local transcript and knowledge artifacts.

.DESCRIPTION
Uses yt-dlp/FFmpeg for URL acquisition, faster-whisper through transcribe.py for ASR,
and Fabric with local Ollama qwen3.5:9b for the extract_wisdom transform.

.PARAMETER Source
An HTTP/HTTPS media URL or a local audio, video, TXT, Markdown, SRT, or VTT file.

.PARAMETER Language
Optional ASR language hint. Supported values are en and de.

.PARAMETER Force
Regenerates transcript and knowledge artifacts. Downloaded source media remains reusable.

.EXAMPLE
.\scripts\transcript_pipeline_v4\run_v4.ps1 -Source .\recording.mp3 -Language en

.EXAMPLE
.\scripts\transcript_pipeline_v4\run_v4.ps1 -Source 'https://example.test/video' -Force
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [ValidateNotNullOrEmpty()]
    [string]$Source,

    [ValidateSet('en', 'de')]
    [string]$Language,

    [switch]$Force
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

function Test-NonEmptyFile {
    param([Parameter(Mandatory = $true)][string]$LiteralPath)
    return (Test-Path -LiteralPath $LiteralPath -PathType Leaf) -and ((Get-Item -LiteralPath $LiteralPath).Length -gt 0)
}

function ConvertTo-WindowsCommandLineArgument {
    param([Parameter(Mandatory = $true)][AllowEmptyString()][string]$Value)

    if ($Value.Length -gt 0 -and $Value -notmatch '[\s"]') {
        return $Value
    }

    $builder = [Text.StringBuilder]::new()
    [void]$builder.Append('"')
    $backslashes = 0
    foreach ($character in $Value.ToCharArray()) {
        if ($character -eq '\') {
            $backslashes++
            continue
        }
        if ($character -eq '"') {
            [void]$builder.Append(('\' * (($backslashes * 2) + 1)))
            [void]$builder.Append('"')
            $backslashes = 0
            continue
        }
        if ($backslashes -gt 0) {
            [void]$builder.Append(('\' * $backslashes))
            $backslashes = 0
        }
        [void]$builder.Append($character)
    }
    if ($backslashes -gt 0) {
        [void]$builder.Append(('\' * ($backslashes * 2)))
    }
    [void]$builder.Append('"')
    return $builder.ToString()
}

function Invoke-ExternalCommand {
    param(
        [Parameter(Mandatory = $true)][string]$FilePath,
        [Parameter(Mandatory = $true)][string[]]$ArgumentList,
        [string]$StandardInputPath,
        [hashtable]$EnvironmentVariables
    )

    $startInfo = [Diagnostics.ProcessStartInfo]::new()
    $startInfo.FileName = $FilePath
    $startInfo.Arguments = (($ArgumentList | ForEach-Object { ConvertTo-WindowsCommandLineArgument $_ }) -join ' ')
    $startInfo.UseShellExecute = $false
    $startInfo.CreateNoWindow = $true
    $startInfo.RedirectStandardOutput = $true
    $startInfo.RedirectStandardError = $true
    $startInfo.RedirectStandardInput = -not [string]::IsNullOrEmpty($StandardInputPath)
    if ($EnvironmentVariables) {
        foreach ($entry in $EnvironmentVariables.GetEnumerator()) {
            $startInfo.EnvironmentVariables[$entry.Key] = [string]$entry.Value
        }
    }

    $process = [Diagnostics.Process]::new()
    $process.StartInfo = $startInfo
    if (-not $process.Start()) {
        throw "Failed to start executable: $FilePath"
    }

    $stdoutTask = $process.StandardOutput.ReadToEndAsync()
    $stderrTask = $process.StandardError.ReadToEndAsync()
    if ($startInfo.RedirectStandardInput) {
        $inputStream = [IO.File]::OpenRead($StandardInputPath)
        try {
            $inputStream.CopyTo($process.StandardInput.BaseStream)
        }
        finally {
            $inputStream.Dispose()
            $process.StandardInput.Close()
        }
    }
    $process.WaitForExit()
    $stdout = $stdoutTask.GetAwaiter().GetResult()
    $stderr = $stderrTask.GetAwaiter().GetResult()

    return [pscustomobject]@{
        ExitCode = $process.ExitCode
        Stdout = $stdout
        Stderr = $stderr
        DisplayCommand = "$FilePath $($startInfo.Arguments)"
    }
}

function Resolve-Executable {
    param(
        [Parameter(Mandatory = $true)][string]$Name,
        [string]$PreferredPath
    )

    if ($PreferredPath -and (Test-Path -LiteralPath $PreferredPath -PathType Leaf)) {
        return (Get-Item -LiteralPath $PreferredPath).FullName
    }
    $command = Get-Command $Name -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
    if (-not $command) {
        throw "Required executable '$Name' was not found."
    }
    return $command.Source
}

function ConvertTo-SourceId {
    param([Parameter(Mandatory = $true)][string]$Value)

    $identifier = $Value.Trim()
    $identifier = [regex]::Replace($identifier, '[<>:"/\\|?*\x00-\x1F]', '-')
    $identifier = [regex]::Replace($identifier, '\s+', '-')
    $identifier = $identifier.Trim(' ', '.', '-')
    if ([string]::IsNullOrEmpty($identifier)) {
        return 'source'
    }
    return $identifier
}

function Get-ProvisionalUrlSourceId {
    param([Parameter(Mandatory = $true)][string]$Url)

    $sha256 = [Security.Cryptography.SHA256]::Create()
    try {
        $hash = $sha256.ComputeHash([Text.Encoding]::UTF8.GetBytes($Url))
        $suffix = ([BitConverter]::ToString($hash) -replace '-', '').Substring(0, 12).ToLowerInvariant()
        return "url-failure-$suffix"
    }
    finally {
        $sha256.Dispose()
    }
}

function Add-RunLogLine {
    param(
        [Parameter(Mandatory = $true)][string]$LiteralPath,
        [Parameter(Mandatory = $true)][string]$Message
    )
    $line = "{0} {1}" -f ([DateTimeOffset]::Now.ToString('o')), $Message
    Add-Content -LiteralPath $LiteralPath -Value $line -Encoding UTF8
}

function Write-Utf8NoBom {
    param([Parameter(Mandatory = $true)][string]$LiteralPath, [Parameter(Mandatory = $true)][AllowEmptyString()][string]$Content)
    [IO.File]::WriteAllText($LiteralPath, $Content, [Text.UTF8Encoding]::new($false))
}

function Convert-TranscriptFile {
    param([Parameter(Mandatory = $true)][string]$LiteralPath)

    $content = [IO.File]::ReadAllText($LiteralPath, [Text.Encoding]::UTF8)
    $content = $content.TrimStart([char]0xFEFF) -replace "`r`n?", "`n"
    $extension = [IO.Path]::GetExtension($LiteralPath).ToLowerInvariant()
    if ($extension -notin @('.srt', '.vtt')) {
        return ($content.TrimEnd("`n") + "`n")
    }

    $lines = $content -split "`n", -1
    $cues = [System.Collections.Generic.List[string]]::new()
    $index = 0
    if ($extension -eq '.vtt' -and $lines.Count -gt 0 -and $lines[0].Trim() -match '^WEBVTT(?:\s|$)') {
        $index++
        while ($index -lt $lines.Count -and -not [string]::IsNullOrWhiteSpace($lines[$index])) { $index++ }
    }

    while ($index -lt $lines.Count) {
        while ($index -lt $lines.Count -and [string]::IsNullOrWhiteSpace($lines[$index])) { $index++ }
        if ($index -ge $lines.Count) { break }

        if ($extension -eq '.vtt' -and $lines[$index].Trim() -match '^(NOTE|STYLE|REGION)(?:\s|$)') {
            while ($index -lt $lines.Count -and -not [string]::IsNullOrWhiteSpace($lines[$index])) { $index++ }
            continue
        }

        $block = [System.Collections.Generic.List[string]]::new()
        while ($index -lt $lines.Count -and -not [string]::IsNullOrWhiteSpace($lines[$index])) {
            $block.Add($lines[$index])
            $index++
        }
        $timingIndex = -1
        for ($lineIndex = 0; $lineIndex -lt $block.Count; $lineIndex++) {
            if ($block[$lineIndex] -match '^\s*(?:\d{2}:)?\d{2}:\d{2}[,.]\d{3}\s+-->\s+(?:\d{2}:)?\d{2}:\d{2}[,.]\d{3}(?:\s|$)') {
                $timingIndex = $lineIndex
                break
            }
        }
        if ($timingIndex -lt 0) { continue }

        $textLines = [System.Collections.Generic.List[string]]::new()
        for ($lineIndex = $timingIndex + 1; $lineIndex -lt $block.Count; $lineIndex++) {
            $text = [regex]::Replace($block[$lineIndex], '<[^>]*>', '')
            $text = [Net.WebUtility]::HtmlDecode($text).Trim()
            if ($text.Length -gt 0) { $textLines.Add($text) }
        }
        if ($textLines.Count -gt 0) { $cues.Add(($textLines -join "`n")) }
    }
    if ($cues.Count -eq 0) { return '' }
    return (($cues -join "`n`n") + "`n")
}

$scriptRoot = $PSScriptRoot
$repoRoot = [IO.Path]::GetFullPath((Join-Path $scriptRoot '..\..'))
$defaultOutputRoot = Join-Path $repoRoot 'artifacts\transcript_pipeline_v4'
$outputRoot = if ($env:TRANSCRIPT_PIPELINE_V4_OUTPUT_ROOT) {
    if ([IO.Path]::IsPathRooted($env:TRANSCRIPT_PIPELINE_V4_OUTPUT_ROOT)) {
        [IO.Path]::GetFullPath($env:TRANSCRIPT_PIPELINE_V4_OUTPUT_ROOT)
    }
    else {
        [IO.Path]::GetFullPath((Join-Path $repoRoot $env:TRANSCRIPT_PIPELINE_V4_OUTPUT_ROOT))
    }
}
else { $defaultOutputRoot }

$sourceUri = $null
$isUrl = [Uri]::TryCreate($Source, [UriKind]::Absolute, [ref]$sourceUri) -and $sourceUri.Scheme -in @('http', 'https')
$localSource = $null
if (-not $isUrl) {
    if (-not (Test-Path -LiteralPath $Source -PathType Leaf)) {
        throw "Source does not exist or is not an HTTP/HTTPS URL: $Source"
    }
    $localSource = (Get-Item -LiteralPath $Source).FullName
}

$ytDlp = $null
if ($isUrl) {
    $provisionalSourceId = Get-ProvisionalUrlSourceId -Url $Source
    try {
        $ytDlp = Resolve-Executable -Name 'yt-dlp'
        $idResult = Invoke-ExternalCommand -FilePath $ytDlp -ArgumentList @('--no-playlist', '--skip-download', '--print', '%(id)s', '--', $Source)
        if ($idResult.ExitCode -ne 0) {
            throw "yt-dlp metadata lookup failed with exit $($idResult.ExitCode): $($idResult.Stderr.Trim())"
        }
        $rawId = ($idResult.Stdout -split "`r?`n" | Where-Object { $_.Trim() } | Select-Object -Last 1)
        if (-not $rawId) { throw 'yt-dlp did not return a source ID.' }
        $sourceId = ConvertTo-SourceId $rawId
    }
    catch {
        $failureRunDirectory = Join-Path $outputRoot $provisionalSourceId
        New-Item -ItemType Directory -Path $failureRunDirectory -Force | Out-Null
        $failureLogPath = Join-Path $failureRunDirectory 'run.log'
        Add-RunLogLine -LiteralPath $failureLogPath -Message "run started; source locator=$Source; provisional source ID=$provisionalSourceId"
        Add-RunLogLine -LiteralPath $failureLogPath -Message 'source identification started; tool=yt-dlp'
        Add-RunLogLine -LiteralPath $failureLogPath -Message "run error; exit error=$($_.Exception.Message)"
        throw
    }
}
else {
    $sourceId = ConvertTo-SourceId ([IO.Path]::GetFileNameWithoutExtension($localSource))
}

$runDirectory = Join-Path $outputRoot $sourceId
New-Item -ItemType Directory -Path $runDirectory -Force | Out-Null
$logPath = Join-Path $runDirectory 'run.log'
$transcriptPath = Join-Path $runDirectory 'transcript.txt'
$srtPath = Join-Path $runDirectory 'transcript.srt'
$knowledgePath = Join-Path $runDirectory 'knowledge.md'

function Write-RunLog {
    param([Parameter(Mandatory = $true)][string]$Message)
    Add-RunLogLine -LiteralPath $logPath -Message $Message
}

Write-RunLog "run started; source locator=$Source; source ID=$sourceId"
if ($isUrl) {
    Write-RunLog 'source identification started; tool=yt-dlp'
    Write-RunLog "source identification completed; tool=yt-dlp; source ID=$sourceId"
}

try {
    $mediaPath = $null
    $sourceExtension = if ($isUrl) { '' } else { [IO.Path]::GetExtension($localSource).ToLowerInvariant() }
    $isExistingTranscript = -not $isUrl -and $sourceExtension -in @('.txt', '.md', '.srt', '.vtt')

    if ($isUrl) {
        $sourceDirectory = Join-Path $runDirectory 'source'
        New-Item -ItemType Directory -Path $sourceDirectory -Force | Out-Null
        $mediaPath = Get-ChildItem -LiteralPath $sourceDirectory -File -ErrorAction SilentlyContinue |
            Where-Object { $_.Length -gt 0 -and $_.Name -notlike '*.info.json' -and $_.Extension -in @('.aac', '.flac', '.m4a', '.mp3', '.ogg', '.opus', '.wav', '.webm', '.mp4', '.mkv') } |
            Select-Object -First 1 -ExpandProperty FullName
        if (-not $mediaPath) {
            Write-RunLog 'acquisition started; tool=yt-dlp; audio conversion=FFmpeg; format=m4a'
            $downloadTemplate = Join-Path $sourceDirectory 'source.%(ext)s'
            $downloadResult = Invoke-ExternalCommand -FilePath $ytDlp -ArgumentList @('--no-playlist', '--format', 'bestaudio/best', '--extract-audio', '--audio-format', 'm4a', '--write-info-json', '--output', $downloadTemplate, '--', $Source)
            if ($downloadResult.ExitCode -ne 0) {
                throw "yt-dlp acquisition failed with exit $($downloadResult.ExitCode): $($downloadResult.Stderr.Trim())"
            }
            $mediaPath = Get-ChildItem -LiteralPath $sourceDirectory -File |
                Where-Object { $_.Length -gt 0 -and $_.Name -notlike '*.info.json' -and $_.Extension -in @('.aac', '.flac', '.m4a', '.mp3', '.ogg', '.opus', '.wav', '.webm', '.mp4', '.mkv') } |
                Select-Object -First 1 -ExpandProperty FullName
            if (-not $mediaPath) { throw 'yt-dlp completed without creating non-empty source media.' }
            Write-RunLog "acquisition completed; media=$mediaPath"
        }
        else {
            Write-RunLog "acquisition reused non-empty media; media=$mediaPath"
        }
    }
    elseif (-not $isExistingTranscript) {
        $mediaPath = $localSource
        Write-RunLog "acquisition skipped; local media=$mediaPath"
    }
    else {
        Write-RunLog "acquisition and ASR skipped; existing transcript=$localSource"
    }

    if ($isExistingTranscript) {
        if ($Force -or -not (Test-NonEmptyFile $transcriptPath)) {
            Write-RunLog "transcript normalization started; format=$sourceExtension"
            $normalized = Convert-TranscriptFile -LiteralPath $localSource
            if ([string]::IsNullOrWhiteSpace($normalized)) { throw 'Transcript normalization produced empty output.' }
            Write-Utf8NoBom -LiteralPath $transcriptPath -Content $normalized
            Write-RunLog 'transcript normalization completed; encoding=UTF-8'
        }
        else {
            Write-RunLog 'transcript reused; reason=non-empty existing output'
        }
    }
    elseif ($Force -or -not (Test-NonEmptyFile $transcriptPath)) {
        $pythonPreferred = Join-Path $scriptRoot '.venv\Scripts\python.exe'
        $usingPythonFallback = -not (Test-Path -LiteralPath $pythonPreferred -PathType Leaf)
        $python = Resolve-Executable -Name 'python' -PreferredPath $pythonPreferred
        if ($usingPythonFallback) { Write-RunLog "fallback used; component=python; source=PATH; executable=$python" }
        $tempTranscript = "$transcriptPath.tmp"
        $tempSrt = "$srtPath.tmp"
        Remove-Item -LiteralPath $tempTranscript, $tempSrt -Force -ErrorAction SilentlyContinue
        $transcribeArguments = @((Join-Path $scriptRoot 'transcribe.py'), '--input', $mediaPath, '--text-out', $tempTranscript, '--srt-out', $tempSrt)
        if ($Language) { $transcribeArguments += @('--language', $Language) }
        Write-RunLog 'ASR started; implementation=faster-whisper; model=large-v3-turbo; device=cpu; compute_type=int8; vad_filter=true'
        $transcribeResult = Invoke-ExternalCommand -FilePath $python -ArgumentList $transcribeArguments
        if ($transcribeResult.ExitCode -ne 0) {
            throw "Transcription failed with exit $($transcribeResult.ExitCode): $($transcribeResult.Stderr.Trim())"
        }
        if (-not (Test-NonEmptyFile $tempTranscript)) { throw 'Transcription completed without a non-empty transcript.' }
        Move-Item -LiteralPath $tempTranscript -Destination $transcriptPath -Force
        if (Test-NonEmptyFile $tempSrt) { Move-Item -LiteralPath $tempSrt -Destination $srtPath -Force }
        Write-RunLog 'ASR completed; transcript=transcript.txt; subtitles=transcript.srt'
    }
    else {
        Write-RunLog 'ASR skipped; transcript reused; reason=non-empty existing output'
    }

    if (-not (Test-NonEmptyFile $transcriptPath)) { throw 'No non-empty transcript is available for Fabric.' }

    if ($Force -or -not (Test-NonEmptyFile $knowledgePath)) {
        $fabricPreferred = Join-Path $env:LOCALAPPDATA 'Microsoft\WinGet\Links\fabric.exe'
        $usingFabricFallback = -not (Test-Path -LiteralPath $fabricPreferred -PathType Leaf)
        $fabric = Resolve-Executable -Name 'fabric' -PreferredPath $fabricPreferred
        if ($usingFabricFallback) { Write-RunLog "fallback used; component=fabric; source=PATH; executable=$fabric" }
        $tempKnowledgePath = "$knowledgePath.tmp"
        Remove-Item -LiteralPath $tempKnowledgePath -Force -ErrorAction SilentlyContinue
        try {
            $fabricArguments = @('-p', 'extract_wisdom', '-V', 'Ollama', '-m', 'qwen3.5:9b', '--modelContextLength=65536', '--thinking=off', '-o', $tempKnowledgePath)
            Write-RunLog 'Fabric started; pattern=extract_wisdom; vendor=Ollama; model=qwen3.5:9b; modelContextLength=65536; thinking=off; OLLAMA_HTTP_TIMEOUT=60m'
            $fabricResult = Invoke-ExternalCommand -FilePath $fabric -ArgumentList $fabricArguments -StandardInputPath $transcriptPath -EnvironmentVariables @{ OLLAMA_HTTP_TIMEOUT = '60m' }
            if ($fabricResult.ExitCode -ne 0) {
                throw "Fabric failed with exit $($fabricResult.ExitCode): $($fabricResult.Stderr.Trim())"
            }
            if (-not (Test-NonEmptyFile $tempKnowledgePath)) { throw 'Fabric completed without a non-empty knowledge.md.' }
            Move-Item -LiteralPath $tempKnowledgePath -Destination $knowledgePath -Force
        }
        finally {
            Remove-Item -LiteralPath $tempKnowledgePath -Force -ErrorAction SilentlyContinue
        }
        Write-RunLog 'Fabric completed; output=knowledge.md'
    }
    else {
        Write-RunLog 'Fabric skipped; knowledge reused; reason=non-empty existing output'
    }
    Write-RunLog 'run completed'
    Write-Output $knowledgePath
}
catch {
    Write-RunLog "run error; exit error=$($_.Exception.Message)"
    throw
}
