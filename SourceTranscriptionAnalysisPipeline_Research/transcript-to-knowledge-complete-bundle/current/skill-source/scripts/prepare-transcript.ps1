param(
    [Parameter(Mandatory = $true)]
    [string]$InputPath,

    [Parameter(Mandatory = $true)]
    [string]$OutputPath,

    [int]$TargetWords = 1100,
    [int]$MinWords = 700,
    [int]$MaxWords = 1500,
    [int]$ContextSegments = 1
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$Runner = Join-Path $ScriptDir "ttk.ps1"

& $Runner init $InputPath --output $OutputPath --target-words $TargetWords --min-words $MinWords --max-words $MaxWords --context-segments $ContextSegments
if ($LASTEXITCODE -ne 0) {
    throw "Transcript-to-knowledge initialization failed with exit code $LASTEXITCODE."
}
