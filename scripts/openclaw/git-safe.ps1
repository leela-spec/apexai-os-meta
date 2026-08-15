[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$RequestPath,

    [Parameter(Mandatory = $true)]
    [ValidateSet('status', 'diff', 'add', 'commit', 'push')]
    [string]$Operation,

    [string[]]$Path = @(),

    [string]$Message
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$GitExe = 'C:\Program Files\Git\cmd\git.exe'
$GitSha256 = '7b7971dd13f0c3a284e538601f2f9770b3a87dfaccb5fb52d68141c67ed22364'
$CredentialHelper = 'C:\Program Files\Git\mingw64\bin\git-credential-manager.exe'
$CredentialHelperSha256 = '593dfd29885443e70255cdf4038988f831d939218aea950e32f2a356ac3b00f5'
if (-not (Test-Path -LiteralPath $GitExe -PathType Leaf)) {
    throw "Pinned Git executable is unavailable: $GitExe"
}
if ((Get-FileHash -Algorithm SHA256 -LiteralPath $GitExe).Hash.ToLowerInvariant() -cne $GitSha256) {
    throw 'Pinned Git executable identity does not match the reviewed version'
}
if (-not (Test-Path -LiteralPath $CredentialHelper -PathType Leaf) -or
    (Get-FileHash -Algorithm SHA256 -LiteralPath $CredentialHelper).Hash.ToLowerInvariant() -cne $CredentialHelperSha256) {
    throw 'Pinned Git credential helper identity does not match the reviewed version'
}
$GitBaseArgs = @(
    '--no-optional-locks',
    '-c', 'core.hooksPath=NUL',
    '-c', 'core.fsmonitor=false',
    '-c', 'diff.external=',
    '-c', 'commit.gpgSign=false',
    '-c', 'protocol.allow=never',
    '-c', 'protocol.file.allow=always',
    '-c', 'protocol.https.allow=always',
    '-c', 'credential.helper=',
    '-c', "credential.helper=$CredentialHelper"
)

function Get-ValidatedRequest {
    param([string]$RequestFile)

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
        $validatorOutput = @(& $pythonRuntime $validator $RequestFile 2>&1)
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

function Invoke-Git {
    param([string[]]$Arguments)

    & $script:GitExe @GitBaseArgs @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "git exited with code $LASTEXITCODE"
    }
}

$savedGitEnvironment = @{}
$gitEnvironmentNames = @(
    [Environment]::GetEnvironmentVariables('Process').Keys |
        Where-Object { ([string]$_).StartsWith('GIT_', [StringComparison]::OrdinalIgnoreCase) }
)
$gitEnvironmentNames += @('GIT_CONFIG_GLOBAL', 'GIT_CONFIG_NOSYSTEM', 'SSH_ASKPASS')
$gitEnvironmentNames = @($gitEnvironmentNames | Sort-Object -Unique)
foreach ($name in $gitEnvironmentNames) {
    $savedGitEnvironment[$name] = [Environment]::GetEnvironmentVariable($name, 'Process')
    [Environment]::SetEnvironmentVariable($name, $null, 'Process')
}
$env:GIT_CONFIG_GLOBAL = 'NUL'
$env:GIT_CONFIG_NOSYSTEM = '1'

try {
    $request = Get-ValidatedRequest -RequestFile $RequestPath
    $grant = $request.grants.git
    if (@($grant.operations | Where-Object { $_ -ceq $Operation }).Count -ne 1) {
        throw "Git operation is not granted: $Operation"
    }

    $repo = (Get-Item -LiteralPath ([string]$grant.repo) -ErrorAction Stop).FullName
    $dangerousConfig = @(& $GitExe @GitBaseArgs -C $repo config --local --includes --get-regexp '^(core\.hooksPath|core\.fsmonitor|core\.sshCommand|diff\.|filter\.|include\.|includeIf\.|protocol\.|url\.|credential\.|http\..*proxy|remote\..*\.proxy|commit\.gpgSign|gpg\.)' 2>$null)
    if ($LASTEXITCODE -notin @(0, 1)) {
        throw 'Could not inspect repository-local Git configuration'
    }
    if ($dangerousConfig.Count -ne 0) {
        throw 'Repository-local Git configuration contains an executable or authority-widening key'
    }

    $insideWorkTree = (& $GitExe @GitBaseArgs -C $repo rev-parse --is-inside-work-tree 2>$null).Trim()
    if ($LASTEXITCODE -ne 0 -or $insideWorkTree -cne 'true') {
        throw "Granted Git path is not a work tree: $repo"
    }
    $topLevel = (& $GitExe @GitBaseArgs -C $repo rev-parse --show-toplevel 2>$null).Trim()
    if ($LASTEXITCODE -ne 0 -or -not [StringComparer]::OrdinalIgnoreCase.Equals(
        [IO.Path]::GetFullPath($topLevel), [IO.Path]::GetFullPath($repo)
    )) {
        throw "Granted Git repo is not the exact work-tree root: $repo"
    }
    $branch = (& $GitExe @GitBaseArgs -C $repo branch --show-current 2>$null).Trim()
    if ($LASTEXITCODE -ne 0 -or $branch -cne [string]$grant.branch -or $branch -cne 'main') {
        throw "Current branch is not the granted main branch: $branch"
    }

    switch ($Operation) {
        'status' {
            if ($Path.Count -ne 0 -or $PSBoundParameters.ContainsKey('Message')) {
                throw 'status accepts no paths or message'
            }
            Invoke-Git -Arguments @('-C', $repo, 'status', '--short', '--branch')
        }
        'diff' {
            if ($Path.Count -ne 0 -or $PSBoundParameters.ContainsKey('Message')) {
                throw 'diff accepts no paths or message'
            }
            Invoke-Git -Arguments @('-C', $repo, 'diff', '--no-ext-diff', '--no-textconv', '--')
        }
        'add' {
            if ($Path.Count -eq 0 -or $PSBoundParameters.ContainsKey('Message')) {
                throw 'add requires declared paths and accepts no message'
            }
            $allowed = @($grant.add_paths | ForEach-Object {
                [IO.Path]::GetFullPath([string]$_)
            })
            $resolved = @($Path | ForEach-Object { [IO.Path]::GetFullPath($_) })
            foreach ($candidate in $resolved) {
                if (@($allowed | Where-Object {
                    [StringComparer]::OrdinalIgnoreCase.Equals($_, $candidate)
                }).Count -ne 1) {
                    throw "Git add path is not granted: $candidate"
                }
            }
            Invoke-Git -Arguments (@('-C', $repo, 'add', '--') + $resolved)
        }
        'commit' {
            if ($Path.Count -ne 0) {
                throw 'commit accepts no paths'
            }
            if (-not $PSBoundParameters.ContainsKey('Message') -or $Message -cne [string]$grant.commit_message) {
                throw 'Commit message does not exactly match the grant'
            }
            $allowed = @($grant.add_paths | ForEach-Object { [IO.Path]::GetFullPath([string]$_) })
            $staged = @(& $GitExe @GitBaseArgs -c 'core.quotePath=true' -C $repo diff --cached --no-renames --name-only --diff-filter=ACMRDTUXB)
            if ($LASTEXITCODE -ne 0 -or $staged.Count -eq 0) {
                throw 'No bounded staged changes are available to commit'
            }
            foreach ($relativePath in $staged) {
                $candidate = [IO.Path]::GetFullPath((Join-Path $repo ([string]$relativePath)))
                if (@($allowed | Where-Object {
                    [StringComparer]::OrdinalIgnoreCase.Equals($_, $candidate)
                }).Count -ne 1) {
                    throw "Staged Git path is not granted: $relativePath"
                }
            }
            Invoke-Git -Arguments @('-C', $repo, 'commit', '--no-verify', '-m', $Message, '--')
        }
        'push' {
            if ($Path.Count -ne 0 -or $PSBoundParameters.ContainsKey('Message')) {
                throw 'push accepts no paths or message'
            }
            $fetchRemotes = @(& $GitExe @GitBaseArgs -C $repo remote get-url --all origin 2>$null)
            if ($LASTEXITCODE -ne 0 -or $fetchRemotes.Count -ne 1) {
                throw 'The granted origin remote is missing'
            }
            $pushRemotes = @(& $GitExe @GitBaseArgs -C $repo remote get-url --push --all origin 2>$null)
            if ($LASTEXITCODE -ne 0 -or $pushRemotes.Count -ne 1) {
                throw 'The granted origin must have exactly one push destination'
            }
            $expectedRemote = [string]$grant.remote_url
            if ([IO.Path]::IsPathRooted($expectedRemote)) {
                $expectedRemote = [IO.Path]::GetFullPath($expectedRemote)
                $fetchRemote = [IO.Path]::GetFullPath([string]$fetchRemotes[0])
                $pushRemote = [IO.Path]::GetFullPath([string]$pushRemotes[0])
                $remoteMatches = (
                    [StringComparer]::OrdinalIgnoreCase.Equals($fetchRemote, $expectedRemote) -and
                    [StringComparer]::OrdinalIgnoreCase.Equals($pushRemote, $expectedRemote)
                )
            }
            else {
                $remoteMatches = (
                    [StringComparer]::Ordinal.Equals([string]$fetchRemotes[0], $expectedRemote) -and
                    [StringComparer]::Ordinal.Equals([string]$pushRemotes[0], $expectedRemote)
                )
            }
            if (-not $remoteMatches) {
                throw 'The origin remote identity does not match the grant'
            }
            Invoke-Git -Arguments @(
                '-C', $repo, 'push', '--no-verify', '--', $expectedRemote,
                'refs/heads/main:refs/heads/main'
            )
        }
    }
}
catch {
    Write-Error $_.Exception.Message
    exit 2
}
finally {
    foreach ($name in $savedGitEnvironment.Keys) {
        [Environment]::SetEnvironmentVariable($name, $savedGitEnvironment[$name], 'Process')
    }
}

exit 0
