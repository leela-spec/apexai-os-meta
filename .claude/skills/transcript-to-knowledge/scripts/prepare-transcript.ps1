param(
    [Parameter(Mandatory = $true)]
    [string]$InputPath,

    [Parameter(Mandatory = $true)]
    [string]$OutputPath,

    [int]$ChunkWords = 1200,
    [int]$OverlapWords = 120
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$PythonScript = Join-Path $ScriptDir "prepare_transcript.py"

if (Get-Command py -ErrorAction SilentlyContinue) {
    & py -3 $PythonScript prepare $InputPath --output $OutputPath --chunk-words $ChunkWords --overlap-words $OverlapWords
}
elseif (Get-Command python -ErrorAction SilentlyContinue) {
    & python $PythonScript prepare $InputPath --output $OutputPath --chunk-words $ChunkWords --overlap-words $OverlapWords
}
else {
    throw "Python 3.10+ was not found. Install Python or make 'py'/'python' available on PATH."
}

if ($LASTEXITCODE -ne 0) {
    throw "Transcript preparation failed with exit code $LASTEXITCODE."
}
