[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$RequestPath,

    [Parameter(Mandatory = $true)]
    [string]$CommandId
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

function Get-ValidatedRequest {
    param([string]$Path)

    $validator = Join-Path $PSScriptRoot 'validate-execution-request.py'
    $pythonRuntime = 'C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.12_3.12.2800.0_x64__qbz5n2kfra8p0\python3.12.exe'
    $pythonSha256 = '5365b422ee178f691988eb937b7abca5f48910b148f76fcce6dbaf5585c948d0'
    $validatorSha256 = 'adea70a8596b7ab4ac7c3af65a54c94093f655de0b5f3fb721dc503b4cfcd050'
    $runtimeStream = [IO.File]::Open(
        $pythonRuntime, [IO.FileMode]::Open, [IO.FileAccess]::Read, [IO.FileShare]::Read
    )
    $validatorStream = [IO.File]::Open(
        $validator, [IO.FileMode]::Open, [IO.FileAccess]::Read, [IO.FileShare]::Read
    )
    try {
        $sha256 = [Security.Cryptography.SHA256]::Create()
        try {
            $runtimeHash = ([BitConverter]::ToString($sha256.ComputeHash($runtimeStream))).Replace('-', '').ToLowerInvariant()
            $validatorHash = ([BitConverter]::ToString($sha256.ComputeHash($validatorStream))).Replace('-', '').ToLowerInvariant()
        }
        finally { $sha256.Dispose() }
        if ($runtimeHash -cne $pythonSha256) {
            throw 'Pinned Python runtime identity does not match the reviewed version'
        }
        if ($validatorHash -cne $validatorSha256) {
            throw 'Execution request validator identity does not match the reviewed version'
        }
        $validatorOutput = @(& $pythonRuntime $validator $Path 2>&1)
        $validatorExit = $LASTEXITCODE
    }
    finally {
        $validatorStream.Dispose()
        $runtimeStream.Dispose()
    }
    $validatorText = $validatorOutput -join [Environment]::NewLine
    if ($validatorExit -ne 0) {
        throw "Execution request rejected: $validatorText"
    }
    $envelope = $validatorText | ConvertFrom-Json
    if (-not $envelope.valid) {
        throw 'Execution request validator did not return a valid request'
    }
    return $envelope.request
}

$executableStream = $null
try {
    $request = Get-ValidatedRequest -Path $RequestPath
    $matches = @($request.grants.commands | Where-Object { $_.id -ceq $CommandId })
    if ($matches.Count -ne 1) {
        throw "Command id is not granted exactly once: $CommandId"
    }
    $grant = $matches[0]
    $executable = (Get-Item -LiteralPath ([string]$grant.executable) -ErrorAction Stop).FullName
    $executableStream = [IO.File]::Open(
        $executable, [IO.FileMode]::Open, [IO.FileAccess]::Read, [IO.FileShare]::Read
    )
    $sha256 = [Security.Cryptography.SHA256]::Create()
    try {
        $actualHash = ([BitConverter]::ToString($sha256.ComputeHash($executableStream))).Replace('-', '').ToLowerInvariant()
    }
    finally {
        $sha256.Dispose()
    }
    if ($actualHash -cne ([string]$grant.executable_sha256).ToLowerInvariant()) {
        throw 'Command executable identity changed after request validation'
    }
    $declaredArgs = @($grant.argv | ForEach-Object { [string]$_ })
    & $executable @declaredArgs
    if ($LASTEXITCODE -ne 0) {
        throw "Declared command exited with code $LASTEXITCODE"
    }
}
catch {
    Write-Error $_.Exception.Message
    exit 2
}
finally {
    if ($null -ne $executableStream) { $executableStream.Dispose() }
}

exit 0
