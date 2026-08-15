[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$RequestPath,

    [Parameter(Mandatory = $true)]
    [string]$ScriptId
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

function Get-ValidatedRequest {
    param([string]$Path)

    $validator = Join-Path $PSScriptRoot 'validate-execution-request.py'
    $pythonRuntime = 'C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.12_3.12.2800.0_x64__qbz5n2kfra8p0\python3.12.exe'
    $pythonSha256 = '5365b422ee178f691988eb937b7abca5f48910b148f76fcce6dbaf5585c948d0'
    $validatorSha256 = 'cce138185b16149b36e9971d2f565ab51a9e0c7741014823fb43da7a079056dd'
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
$scriptStream = $null
try {
    $request = Get-ValidatedRequest -Path $RequestPath
    $matches = @($request.grants.scripts | Where-Object { $_.id -ceq $ScriptId })
    if ($matches.Count -ne 1) {
        throw "Script id is not granted exactly once: $ScriptId"
    }

    $grant = $matches[0]
    $executable = (Get-Item -LiteralPath ([string]$grant.executable) -ErrorAction Stop).FullName
    $script = (Get-Item -LiteralPath ([string]$grant.path) -ErrorAction Stop).FullName
    $executableStream = [IO.File]::Open(
        $executable, [IO.FileMode]::Open, [IO.FileAccess]::Read, [IO.FileShare]::Read
    )
    $scriptStream = [IO.File]::Open(
        $script, [IO.FileMode]::Open, [IO.FileAccess]::Read, [IO.FileShare]::Read
    )
    $sha256 = [Security.Cryptography.SHA256]::Create()
    try {
        $executableHash = ([BitConverter]::ToString($sha256.ComputeHash($executableStream))).Replace('-', '').ToLowerInvariant()
        $scriptHash = ([BitConverter]::ToString($sha256.ComputeHash($scriptStream))).Replace('-', '').ToLowerInvariant()
    }
    finally {
        $sha256.Dispose()
    }
    if ($executableHash -cne ([string]$grant.executable_sha256).ToLowerInvariant()) {
        throw 'Executable identity changed after request validation'
    }
    if ($scriptHash -cne ([string]$grant.sha256).ToLowerInvariant()) {
        throw 'Script identity changed after request validation'
    }
    $declaredArgs = @($grant.argv | ForEach-Object { [string]$_ })
    $executableName = [IO.Path]::GetFileNameWithoutExtension($executable).ToLowerInvariant()
    $extension = [IO.Path]::GetExtension($script).ToLowerInvariant()

    switch ($extension) {
        '.ps1' {
            if ($executableName -notin @('powershell', 'pwsh')) {
                throw 'A .ps1 grant requires powershell.exe or pwsh.exe'
            }
            & $executable -NoProfile -NonInteractive -ExecutionPolicy Bypass -File $script @declaredArgs
        }
        '.py' {
            if ($executableName -notin @('python', 'python3', 'py')) {
                throw 'A .py grant requires an explicitly granted Python executable'
            }
            & $executable $script @declaredArgs
        }
        '.js' {
            if ($executableName -ne 'node') {
                throw 'A .js grant requires an explicitly granted Node executable'
            }
            & $executable $script @declaredArgs
        }
        default {
            throw "Unsupported script extension: $extension"
        }
    }
    if ($LASTEXITCODE -ne 0) {
        throw "Declared script exited with code $LASTEXITCODE"
    }
}
catch {
    Write-Error $_.Exception.Message
    exit 2
}
finally {
    if ($null -ne $scriptStream) { $scriptStream.Dispose() }
    if ($null -ne $executableStream) { $executableStream.Dispose() }
}

exit 0
