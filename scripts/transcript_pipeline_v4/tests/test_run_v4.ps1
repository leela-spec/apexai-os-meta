$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$script:SourceRunner = Join-Path (Split-Path $PSScriptRoot -Parent) 'run_v4.ps1'
$script:Runner = $script:SourceRunner
$script:Failures = [System.Collections.Generic.List[string]]::new()
$script:Checks = 0

function Assert-True {
    param([bool]$Condition, [string]$Message)
    $script:Checks++
    if (-not $Condition) {
        $script:Failures.Add($Message)
    }
}

function Assert-Equal {
    param([AllowNull()]$Actual, [AllowNull()]$Expected, [string]$Message)
    $script:Checks++
    if ($Actual -cne $Expected) {
        $script:Failures.Add("$Message`nEXPECTED: <$Expected>`nACTUAL:   <$Actual>")
    }
}

function Get-InvocationCount {
    param([string]$LiteralPath)
    if (-not (Test-Path -LiteralPath $LiteralPath -PathType Leaf)) { return 0 }
    return (Get-Content -LiteralPath $LiteralPath | Measure-Object).Count
}

function Test-GitIgnored {
    param([string]$RepoRelativePath)
    & git -C (Resolve-Path (Join-Path $PSScriptRoot '..\..\..')) check-ignore --quiet -- $RepoRelativePath
    return $LASTEXITCODE -eq 0
}

function ConvertTo-TestCommandLineArgument {
    param([AllowEmptyString()][string]$Value)
    if ($Value.Length -gt 0 -and $Value -notmatch '[\s"]') { return $Value }
    return ('"' + ($Value -replace '(\\*)"', '$1$1\"' -replace '(\\+)$', '$1$1') + '"')
}

function Invoke-Runner {
    param([string[]]$Arguments)

    $stdout = Join-Path $script:TempRoot ([System.IO.Path]::GetRandomFileName())
    $stderr = Join-Path $script:TempRoot ([System.IO.Path]::GetRandomFileName())
    $commandLine = ((@('-NoProfile', '-NonInteractive', '-File', $script:Runner) + $Arguments | ForEach-Object { ConvertTo-TestCommandLineArgument $_ }) -join ' ')
    $process = Start-Process -FilePath 'powershell.exe' -ArgumentList $commandLine -WindowStyle Hidden -Wait -PassThru -RedirectStandardOutput $stdout -RedirectStandardError $stderr
    [pscustomobject]@{
        ExitCode = $process.ExitCode
        Stdout = if (Test-Path $stdout) { Get-Content -Raw $stdout } else { '' }
        Stderr = if (Test-Path $stderr) { Get-Content -Raw $stderr } else { '' }
    }
}

function New-FakeTools {
    param([string]$Path)

    $source = @'
using System;
using System.IO;
using System.Linq;
using System.Text;

public static class FakeTools
{
    public static int Main(string[] args)
    {
        var tool = Path.GetFileNameWithoutExtension(Environment.GetCommandLineArgs()[0]).ToLowerInvariant();
        if (tool == "yt-dlp")
            return RunYtDlp(args);
        if (tool == "python")
            return RunPython(args);
        return 0;
    }

    private static void Append(string environmentName, string value)
    {
        var path = Environment.GetEnvironmentVariable(environmentName);
        if (!string.IsNullOrEmpty(path))
            File.AppendAllText(path, value, new UTF8Encoding(false));
    }

    private static string FindValue(string[] args, string name)
    {
        for (var index = 0; index + 1 < args.Length; index++)
            if (args[index] == name)
                return args[index + 1];
        return null;
    }

    private static int RunYtDlp(string[] args)
    {
        Append("FAKE_YTDLP_CAPTURE", string.Join("\n", args) + "\n---\n");
        Append("FAKE_YTDLP_COUNT", "1\n");
        if (args.Contains("--skip-download"))
        {
            int metadataExit;
            if (int.TryParse(Environment.GetEnvironmentVariable("FAKE_YTDLP_METADATA_EXIT_CODE"), out metadataExit) && metadataExit != 0)
            {
                Console.Error.Write(Environment.GetEnvironmentVariable("FAKE_YTDLP_METADATA_ERROR") ?? "metadata failure");
                return metadataExit;
            }
            Console.Out.WriteLine(Environment.GetEnvironmentVariable("FAKE_YTDLP_ID") ?? "fake-url-id");
            return 0;
        }

        var template = FindValue(args, "--output");
        if (string.IsNullOrEmpty(template))
            return 31;
        var media = template.Replace("%(ext)s", "m4a");
        var metadata = template.Replace("%(ext)s", "info.json");
        Directory.CreateDirectory(Path.GetDirectoryName(media));
        File.WriteAllText(media, "fake downloaded media", new UTF8Encoding(false));
        File.WriteAllText(metadata, "{\"id\":\"" + (Environment.GetEnvironmentVariable("FAKE_YTDLP_ID") ?? "fake-url-id") + "\"}", new UTF8Encoding(false));
        return 0;
    }

    private static int RunPython(string[] args)
    {
        Append("FAKE_PYTHON_CAPTURE", string.Join("\n", args) + "\n---\n");
        Append("FAKE_PYTHON_COUNT", "1\n");
        var textOutput = FindValue(args, "--text-out");
        var srtOutput = FindValue(args, "--srt-out");
        var segmentsJsonOutput = FindValue(args, "--segments-json-out");
        if (string.IsNullOrEmpty(textOutput) || string.IsNullOrEmpty(srtOutput))
            return 37;
        Directory.CreateDirectory(Path.GetDirectoryName(textOutput));
        var body = Environment.GetEnvironmentVariable("FAKE_TRANSCRIPT_BODY") ?? "fake transcript";
        File.WriteAllText(textOutput, body + "\n", new UTF8Encoding(false));
        File.WriteAllText(srtOutput, "1\n00:00:00,000 --> 00:00:01,000\n" + body + "\n", new UTF8Encoding(false));
        if (!string.IsNullOrEmpty(segmentsJsonOutput))
            File.WriteAllText(segmentsJsonOutput, "{\"schema_version\":\"1.0\",\"segments\":[]}", new UTF8Encoding(false));
        return 0;
    }
}
'@
    Add-Type -TypeDefinition $source -OutputAssembly $Path -OutputType ConsoleApplication -Language CSharp
}

$script:TempRoot = Join-Path ([System.IO.Path]::GetTempPath()) ("transcript pipeline v4 tests-" + [guid]::NewGuid().ToString('N'))
$oldPath = $env:PATH
$oldLocalAppData = $env:LOCALAPPDATA
$oldOutputRoot = $env:TRANSCRIPT_PIPELINE_V4_OUTPUT_ROOT
$oldYtDlpCapture = $env:FAKE_YTDLP_CAPTURE
$oldYtDlpCount = $env:FAKE_YTDLP_COUNT
$oldYtDlpId = $env:FAKE_YTDLP_ID
$oldYtDlpExit = $env:FAKE_YTDLP_METADATA_EXIT_CODE
$oldYtDlpError = $env:FAKE_YTDLP_METADATA_ERROR
$oldPythonCapture = $env:FAKE_PYTHON_CAPTURE
$oldPythonCount = $env:FAKE_PYTHON_COUNT
$oldTranscriptBody = $env:FAKE_TRANSCRIPT_BODY

try {
    $bin = Join-Path $script:TempRoot 'bin'
    $inputRoot = Join-Path $script:TempRoot 'input files'
    $outputRoot = Join-Path $script:TempRoot 'output files'
    $isolatedScriptRoot = Join-Path $script:TempRoot 'isolated repo\scripts\transcript_pipeline_v4'
    New-Item -ItemType Directory -Path $bin, $inputRoot, $outputRoot, $isolatedScriptRoot -Force | Out-Null
    New-FakeTools -Path (Join-Path $bin 'fake-tools.exe')
    Copy-Item -LiteralPath (Join-Path $bin 'fake-tools.exe') -Destination (Join-Path $bin 'yt-dlp.exe')
    Copy-Item -LiteralPath (Join-Path $bin 'fake-tools.exe') -Destination (Join-Path $bin 'python.exe')
    $script:Runner = Join-Path $isolatedScriptRoot 'run_v4.ps1'
    Copy-Item -LiteralPath $script:SourceRunner -Destination $script:Runner

    $env:LOCALAPPDATA = Join-Path $script:TempRoot 'localappdata-without-winget-link'
    $env:PATH = "$bin;$oldPath"
    $env:TRANSCRIPT_PIPELINE_V4_OUTPUT_ROOT = $outputRoot
    $env:FAKE_YTDLP_CAPTURE = Join-Path $script:TempRoot 'yt-dlp-args.txt'
    $env:FAKE_YTDLP_COUNT = Join-Path $script:TempRoot 'yt-dlp-count.txt'
    $env:FAKE_YTDLP_ID = 'url-source-42'
    $env:FAKE_YTDLP_METADATA_EXIT_CODE = '0'
    $env:FAKE_YTDLP_METADATA_ERROR = 'metadata exploded'
    $env:FAKE_PYTHON_CAPTURE = Join-Path $script:TempRoot 'python-args.txt'
    $env:FAKE_PYTHON_COUNT = Join-Path $script:TempRoot 'python-count.txt'
    $env:FAKE_TRANSCRIPT_BODY = 'fake transcript'

    # Generated text and metadata remain stageable while local environments, models, and downloaded media stay ignored.
    foreach ($stageablePath in @(
        'artifacts/transcript_pipeline_v4/example/transcript.txt',
        'artifacts/transcript_pipeline_v4/example/run.log',
        'artifacts/transcript_pipeline_v4/example/source/source.info.json'
    )) {
        Assert-True (-not (Test-GitIgnored $stageablePath)) "Required result artifact is ignored: $stageablePath"
    }
    Assert-True (Test-GitIgnored 'artifacts/transcript_pipeline_v4/example/source/source.m4a') 'Downloaded media is not ignored.'
    Assert-True (Test-GitIgnored 'scripts/transcript_pipeline_v4/.venv/pyvenv.cfg') 'V4 virtual environment is not ignored.'
    Assert-True (Test-GitIgnored 'scripts/transcript_pipeline_v4/models/model.bin') 'V4 model cache is not ignored.'

    # A missing mandatory source must be rejected before any artifacts are created.
    $missing = Invoke-Runner -Arguments @()
    Assert-True ($missing.ExitCode -ne 0) 'Runner accepted a missing -Source argument.'
    Assert-True (($missing.Stdout + $missing.Stderr) -match 'Source') 'Missing-source error did not identify Source.'
    Assert-Equal ((Get-ChildItem $outputRoot -Force | Measure-Object).Count) 0 'Missing-source rejection created output artifacts.'

    # SRT normalization must remove timing, numbering, and inline markup without rewriting words.
    $srt = Join-Path $inputRoot 'marked-up.srt'
    [IO.File]::WriteAllText($srt, "1`r`n00:00:01,000 --> 00:00:03,000`r`n<i>Hello</i>`r`nworld`r`n`r`n2`r`n00:00:04.250 --> 00:00:05.000`r`nSecond line`r`n", [Text.UTF8Encoding]::new($false))
    $srtRun = Invoke-Runner -Arguments @('-Source', $srt)
    Assert-Equal $srtRun.ExitCode 0 "SRT run failed: $($srtRun.Stderr)"
    $srtTranscript = Join-Path $outputRoot 'marked-up\transcript.txt'
    Assert-Equal ([IO.File]::ReadAllText($srtTranscript)) "Hello`nworld`n`nSecond line`n" 'SRT normalization was not deterministic.'

    # VTT metadata, cue identifiers, timing settings, and voice tags must not enter transcript text.
    $vtt = Join-Path $inputRoot 'captions.vtt'
    [IO.File]::WriteAllText($vtt, "WEBVTT`nKind: captions`nLanguage: en`n`nintro-cue`n00:01.000 --> 00:03.000 align:start position:0%`n<v Alice>Hi there</v>`n`nNOTE ignored note`nignore this too`n`n00:04.000 --> 00:05.000`nFinal`n", [Text.UTF8Encoding]::new($false))
    $vttRun = Invoke-Runner -Arguments @('-Source', $vtt)
    Assert-Equal $vttRun.ExitCode 0 "VTT run failed: $($vttRun.Stderr)"
    Assert-Equal ([IO.File]::ReadAllText((Join-Path $outputRoot 'captions\transcript.txt'))) "Hi there`n`nFinal`n" 'VTT normalization retained metadata or lost cue text.'

    $runLog = [IO.File]::ReadAllText((Join-Path $outputRoot 'captions\run.log'))
    Assert-True ($runLog -match 'source locator=.*captions\.vtt; source ID=captions') 'Run log omitted its source locator or source ID.'

    # Non-empty outputs resume; empty outputs never count as complete; Force regenerates downstream files.
    $plain = Join-Path $inputRoot 'resume.txt'
    [IO.File]::WriteAllText($plain, "original transcript`n", [Text.UTF8Encoding]::new($false))
    $first = Invoke-Runner -Arguments @('-Source', $plain)
    Assert-Equal $first.ExitCode 0 "Initial resume run failed: $($first.Stderr)"
    $runDir = Join-Path $outputRoot 'resume'

    [IO.File]::WriteAllText($plain, "changed source`n", [Text.UTF8Encoding]::new($false))
    $second = Invoke-Runner -Arguments @('-Source', $plain)
    Assert-Equal $second.ExitCode 0 "Resume run failed: $($second.Stderr)"
    Assert-Equal ([IO.File]::ReadAllText((Join-Path $runDir 'transcript.txt'))) "original transcript`n" 'Resume replaced a non-empty transcript.'

    $forced = Invoke-Runner -Arguments @('-Source', $plain, '-Force')
    Assert-Equal $forced.ExitCode 0 "Forced run failed: $($forced.Stderr)"
    Assert-Equal ([IO.File]::ReadAllText((Join-Path $runDir 'transcript.txt'))) "changed source`n" 'Force did not regenerate transcript.txt.'

    # URL input exercises metadata ID lookup, acquisition arguments, ASR, final logs, and media reuse.
    Remove-Item -LiteralPath $env:FAKE_YTDLP_CAPTURE, $env:FAKE_YTDLP_COUNT, $env:FAKE_PYTHON_CAPTURE, $env:FAKE_PYTHON_COUNT -Force -ErrorAction SilentlyContinue
    $url = 'https://video.example/watch?v=42'
    $env:FAKE_YTDLP_ID = 'url-source-42'
    $env:FAKE_TRANSCRIPT_BODY = 'url transcript'
    $urlRun = Invoke-Runner -Arguments @('-Source', $url, '-Language', 'en')
    Assert-Equal $urlRun.ExitCode 0 "URL run failed: $($urlRun.Stderr)"
    $urlRunDir = Join-Path $outputRoot 'url-source-42'
    Assert-True (Test-Path -LiteralPath (Join-Path $urlRunDir 'source\source.m4a') -PathType Leaf) 'URL acquisition did not create source media.'
    Assert-True (Test-Path -LiteralPath (Join-Path $urlRunDir 'source\source.info.json') -PathType Leaf) 'URL acquisition did not retain source metadata JSON.'
    Assert-Equal ([IO.File]::ReadAllText((Join-Path $urlRunDir 'transcript.txt'))) "url transcript`n" 'URL media did not reach ASR output.'
    $ytDlpReceipt = [IO.File]::ReadAllText($env:FAKE_YTDLP_CAPTURE)
    foreach ($argument in @('--no-playlist', '--skip-download', '--print', '%(id)s', '--format', 'bestaudio/best', '--extract-audio', '--audio-format', 'm4a', '--write-info-json', '--output', $url)) {
        Assert-True (($ytDlpReceipt -split "`n") -ccontains $argument) "yt-dlp receipt omitted exact argument: $argument"
    }
    Assert-Equal (Get-InvocationCount $env:FAKE_YTDLP_COUNT) 2 'First URL run did not perform exactly metadata and download calls.'
    Assert-Equal (Get-InvocationCount $env:FAKE_PYTHON_COUNT) 1 'First URL run did not invoke ASR exactly once.'
    $urlLog = [IO.File]::ReadAllText((Join-Path $urlRunDir 'run.log'))
    Assert-True ($urlLog -match 'source identification started; tool=yt-dlp') 'Successful URL log omitted metadata lookup start.'
    Assert-True ($urlLog -match 'source identification completed; tool=yt-dlp; source ID=url-source-42') 'Successful URL log omitted metadata lookup completion.'

    $urlResume = Invoke-Runner -Arguments @('-Source', $url, '-Language', 'en')
    Assert-Equal $urlResume.ExitCode 0 "URL resume failed: $($urlResume.Stderr)"
    Assert-Equal (Get-InvocationCount $env:FAKE_YTDLP_COUNT) 3 'URL resume redownloaded media instead of only resolving its stable ID.'
    Assert-Equal (Get-InvocationCount $env:FAKE_PYTHON_COUNT) 1 'URL resume reran ASR despite a non-empty transcript.'
    Assert-True (([IO.File]::ReadAllText((Join-Path $urlRunDir 'run.log'))) -match 'acquisition reused non-empty media') 'URL resume did not log media reuse.'

    # A pre-ID URL failure gets its own deterministic durable run.log with exact lookup error facts.
    $failureUrl = 'https://failure.example/watch?v=bad'
    $env:FAKE_YTDLP_METADATA_EXIT_CODE = '47'
    $env:FAKE_YTDLP_METADATA_ERROR = 'metadata exploded'
    $metadataFailure = Invoke-Runner -Arguments @('-Source', $failureUrl)
    Assert-True ($metadataFailure.ExitCode -ne 0) 'yt-dlp metadata failure incorrectly returned success.'
    $failureRunDir = Join-Path $outputRoot 'url-failure-5a3704c12b83'
    $failureLogPath = Join-Path $failureRunDir 'run.log'
    Assert-True (Test-Path -LiteralPath $failureLogPath -PathType Leaf) 'Pre-ID metadata failure did not create a durable run.log.'
    if (Test-Path -LiteralPath $failureLogPath -PathType Leaf) {
        $failureLog = [IO.File]::ReadAllText($failureLogPath)
        Assert-True ($failureLog -match 'source locator=https://failure\.example/watch\?v=bad') 'Failure log omitted source locator.'
        Assert-True ($failureLog -match 'provisional source ID=url-failure-5a3704c12b83') 'Failure log omitted provisional source ID.'
        Assert-True ($failureLog -match 'source identification started; tool=yt-dlp') 'Failure log omitted metadata lookup stage/tool.'
        Assert-True ($failureLog -match 'exit error=.*exit 47.*metadata exploded') 'Failure log omitted exact metadata exit error.'
    }
    $env:FAKE_YTDLP_METADATA_EXIT_CODE = '0'

    # Local media stays in place and ASR receives language/resume/Force behavior through the real runner.
    Remove-Item -LiteralPath $env:FAKE_PYTHON_CAPTURE, $env:FAKE_PYTHON_COUNT -Force -ErrorAction SilentlyContinue
    $media = Join-Path $inputRoot 'local recording.wav'
    [IO.File]::WriteAllText($media, 'fake local media bytes', [Text.UTF8Encoding]::new($false))
    $env:FAKE_TRANSCRIPT_BODY = 'local transcript de'
    $localRun = Invoke-Runner -Arguments @('-Source', $media, '-Language', 'de')
    Assert-Equal $localRun.ExitCode 0 "Local-media run failed: $($localRun.Stderr)"
    $localRunDir = Join-Path $outputRoot 'local-recording'
    Assert-Equal ([IO.File]::ReadAllText((Join-Path $localRunDir 'transcript.txt'))) "local transcript de`n" 'Local media did not produce fake ASR transcript.'
    Assert-True (Test-Path -LiteralPath (Join-Path $localRunDir 'transcript.segments.json') -PathType Leaf) 'Local media did not preserve ASR segment metadata.'
    Assert-True (-not (Test-Path -LiteralPath (Join-Path $localRunDir 'source'))) 'Local media was unnecessarily copied into the run directory.'
    $pythonReceipt = [IO.File]::ReadAllText($env:FAKE_PYTHON_CAPTURE)
    foreach ($argument in @('--input', $media, '--text-out', '--srt-out', '--segments-json-out', '--language', 'de')) {
        Assert-True (($pythonReceipt -split "`n") -ccontains $argument) "Local-media Python receipt omitted exact argument: $argument"
    }
    Assert-Equal (Get-InvocationCount $env:FAKE_PYTHON_COUNT) 1 'Initial local-media run did not invoke ASR exactly once.'

    $env:FAKE_TRANSCRIPT_BODY = 'must stay resumed'
    $localResume = Invoke-Runner -Arguments @('-Source', $media, '-Language', 'de')
    Assert-Equal $localResume.ExitCode 0 "Local-media resume failed: $($localResume.Stderr)"
    Assert-Equal (Get-InvocationCount $env:FAKE_PYTHON_COUNT) 1 'Local-media resume reran ASR.'
    Assert-Equal ([IO.File]::ReadAllText((Join-Path $localRunDir 'transcript.txt'))) "local transcript de`n" 'Local-media resume replaced transcript.'

    $env:FAKE_TRANSCRIPT_BODY = 'forced local transcript'
    $localForce = Invoke-Runner -Arguments @('-Source', $media, '-Language', 'de', '-Force')
    Assert-Equal $localForce.ExitCode 0 "Forced local-media run failed: $($localForce.Stderr)"
    Assert-Equal (Get-InvocationCount $env:FAKE_PYTHON_COUNT) 2 'Force did not rerun local-media ASR exactly once.'
    Assert-Equal ([IO.File]::ReadAllText((Join-Path $localRunDir 'transcript.txt'))) "forced local transcript`n" 'Force did not promote new local-media transcript.'

    if ($script:Failures.Count -gt 0) {
        $script:Failures | ForEach-Object { Write-Error $_ -ErrorAction Continue }
        throw "$($script:Failures.Count) of $($script:Checks) checks failed."
    }
    Write-Host "PASS: $($script:Checks) behavioral checks"
}
finally {
    $env:PATH = $oldPath
    $env:LOCALAPPDATA = $oldLocalAppData
    $env:TRANSCRIPT_PIPELINE_V4_OUTPUT_ROOT = $oldOutputRoot
    $env:FAKE_YTDLP_CAPTURE = $oldYtDlpCapture
    $env:FAKE_YTDLP_COUNT = $oldYtDlpCount
    $env:FAKE_YTDLP_ID = $oldYtDlpId
    $env:FAKE_YTDLP_METADATA_EXIT_CODE = $oldYtDlpExit
    $env:FAKE_YTDLP_METADATA_ERROR = $oldYtDlpError
    $env:FAKE_PYTHON_CAPTURE = $oldPythonCapture
    $env:FAKE_PYTHON_COUNT = $oldPythonCount
    $env:FAKE_TRANSCRIPT_BODY = $oldTranscriptBody
    if (Test-Path $script:TempRoot) {
        Remove-Item -LiteralPath $script:TempRoot -Recurse -Force
    }
}
