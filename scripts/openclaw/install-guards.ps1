[CmdletBinding()]
param(
    [string]$SourcePath,
    [string]$TargetPath = 'C:\ProgramData\ApexExecutor\guards',
    [switch]$SkipAcl
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

if ([string]::IsNullOrWhiteSpace($SourcePath)) {
    $SourcePath = $PSScriptRoot
}

$guardFiles = @(
    'validate-execution-request.py',
    'run-script-safe.ps1',
    'run-command-safe.ps1',
    'git-safe.ps1'
)

try {
    $source = (Get-Item -LiteralPath $SourcePath -ErrorAction Stop).FullName
    $fileHashes = [ordered]@{}
    foreach ($name in $guardFiles) {
        $path = Join-Path $source $name
        if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
            throw "Required guard source is missing: $path"
        }
        $fileHashes[$name] = (Get-FileHash -Algorithm SHA256 -LiteralPath $path).Hash.ToLowerInvariant()
    }

    $identityText = ($fileHashes.GetEnumerator() | ForEach-Object { "$($_.Key):$($_.Value)" }) -join "`n"
    $identityBytes = [Text.Encoding]::UTF8.GetBytes($identityText)
    $identityHasher = [Security.Cryptography.SHA256]::Create()
    try {
        $identity = ([BitConverter]::ToString($identityHasher.ComputeHash($identityBytes))).Replace('-', '').ToLowerInvariant()
    }
    finally { $identityHasher.Dispose() }

    $targetRoot = [IO.Path]::GetFullPath($TargetPath)
    [IO.Directory]::CreateDirectory($targetRoot) | Out-Null
    $versionPath = Join-Path $targetRoot ("guards-v1-" + $identity.Substring(0, 16))
    $alreadyExisted = Test-Path -LiteralPath $versionPath
    $userSid = [Security.Principal.WindowsIdentity]::GetCurrent().User.Value
    $administratorsSid = '*S-1-5-32-544'
    if ($alreadyExisted -and -not $SkipAcl) {
        # Recover an interrupted ACL transition before reading any child. /A
        # assigns ownership to Administrators rather than to the operator user.
        $recoveryOutput = @(& takeown.exe '/F' $versionPath '/A' '/R' '/D' 'Y' 2>&1)
        if ($LASTEXITCODE -ne 0) {
            throw "Could not recover interrupted guard ownership: $($recoveryOutput -join [Environment]::NewLine)"
        }
        $recoveryOutput = @(& icacls.exe $versionPath '/grant:r' "$administratorsSid`:F" '*S-1-5-18:F' "*$userSid`:RX" '/T' '/C' 2>&1)
        if ($LASTEXITCODE -ne 0) {
            throw "Could not recover interrupted guard traversal: $($recoveryOutput -join [Environment]::NewLine)"
        }
    }
    if ($alreadyExisted) {
        foreach ($name in $guardFiles) {
            $existingPath = Join-Path $versionPath $name
            if (-not (Test-Path -LiteralPath $existingPath -PathType Leaf)) {
                throw "Existing guard version is incomplete and will not be overwritten: $existingPath"
            }
            $existingHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $existingPath).Hash.ToLowerInvariant()
            if ($existingHash -cne $fileHashes[$name]) {
                throw "Existing guard version identity mismatch and will not be overwritten: $name"
            }
        }
    }
    else {
        $stagingPath = Join-Path $targetRoot ('.staging-' + [Guid]::NewGuid().ToString('N'))
        [IO.Directory]::CreateDirectory($stagingPath) | Out-Null
        try {
            foreach ($name in $guardFiles) {
                Copy-Item -LiteralPath (Join-Path $source $name) -Destination (Join-Path $stagingPath $name)
                $copiedHash = (Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $stagingPath $name)).Hash.ToLowerInvariant()
                if ($copiedHash -cne $fileHashes[$name]) {
                    throw "Copied guard identity mismatch: $name"
                }
            }
            $manifest = [ordered]@{
                schema_version = 'apex.guard-manifest/v1'
                identity = $identity
                files = $fileHashes
            }
            $manifestJson = $manifest | ConvertTo-Json -Depth 4
            [IO.File]::WriteAllText(
                (Join-Path $stagingPath 'guard-manifest.json'),
                $manifestJson,
                [Text.UTF8Encoding]::new($false)
            )
            Move-Item -LiteralPath $stagingPath -Destination $versionPath
        }
        finally {
            if (Test-Path -LiteralPath $stagingPath) {
                Remove-Item -LiteralPath $stagingPath -Recurse -Force
            }
        }
    }

    if (-not $SkipAcl) {
        $aclOutput = @(& icacls.exe $versionPath '/setowner' $administratorsSid '/T' '/C' 2>&1)
        if ($LASTEXITCODE -ne 0) {
            throw "Could not transfer guard ownership: $($aclOutput -join [Environment]::NewLine)"
        }
        $aclOutput = @(& icacls.exe $versionPath '/inheritance:r' '/T' '/C' 2>&1)
        if ($LASTEXITCODE -ne 0) {
            throw "Could not remove guard inheritance: $($aclOutput -join [Environment]::NewLine)"
        }
        $aclOutput = @(& icacls.exe $versionPath '/grant:r' "*$userSid`:RX" '*S-1-5-18:F' "$administratorsSid`:F" '/T' '/C' 2>&1)
        if ($LASTEXITCODE -ne 0) {
            throw "Could not protect installed guards: $($aclOutput -join [Environment]::NewLine)"
        }
        $aclOutput = @(& icacls.exe $targetRoot '/setowner' $administratorsSid 2>&1)
        if ($LASTEXITCODE -ne 0) {
            throw "Could not transfer guard-root ownership: $($aclOutput -join [Environment]::NewLine)"
        }
        $aclOutput = @(& icacls.exe $targetRoot '/inheritance:r' 2>&1)
        if ($LASTEXITCODE -ne 0) {
            throw "Could not remove guard-root inheritance: $($aclOutput -join [Environment]::NewLine)"
        }
        $aclOutput = @(& icacls.exe $targetRoot '/grant:r' "*$userSid`:RX" '*S-1-5-18:F' "$administratorsSid`:F" 2>&1)
        if ($LASTEXITCODE -ne 0) {
            throw "Could not protect guard root: $($aclOutput -join [Environment]::NewLine)"
        }
    }

    foreach ($name in $guardFiles) {
        $installedHash = (Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $versionPath $name)).Hash.ToLowerInvariant()
        if ($installedHash -cne $fileHashes[$name]) {
            throw "Protected guard identity mismatch: $name"
        }
    }
    if (-not $SkipAcl) {
        $adminSid = [Security.Principal.SecurityIdentifier]::new('S-1-5-32-544')
        foreach ($protectedPath in @($targetRoot, $versionPath, (Join-Path $versionPath 'guard-manifest.json'))) {
            $ownerSid = (Get-Acl -LiteralPath $protectedPath).Owner
            $resolvedOwnerSid = ([Security.Principal.NTAccount]$ownerSid).Translate(
                [Security.Principal.SecurityIdentifier]
            )
            if ($resolvedOwnerSid -ne $adminSid) {
                throw "Protected guard path has unexpected owner: $protectedPath ($ownerSid)"
            }
        }
    }

    [ordered]@{
        installed_path = $versionPath
        identity = $identity
        acl_protected = -not [bool]$SkipAcl
        already_existed = [bool]$alreadyExisted
    } | ConvertTo-Json -Compress
}
catch {
    Write-Error $_.Exception.Message
    exit 2
}

exit 0
