param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$RemainingArgs
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$PythonScript = Join-Path $ScriptDir "ttk.py"

if (Get-Command py -ErrorAction SilentlyContinue) {
    & py -3 $PythonScript @RemainingArgs
}
elseif (Get-Command python -ErrorAction SilentlyContinue) {
    & python $PythonScript @RemainingArgs
}
else {
    throw "Python 3.10+ was not found. Install Python or make 'py'/'python' available on PATH."
}

if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}
