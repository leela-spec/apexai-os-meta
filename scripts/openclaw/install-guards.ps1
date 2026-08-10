[CmdletBinding()]
param(
    [string]$SourcePath,
    [string]$TargetPath = 'C:\ProgramData\ApexExecutor\guards',
    [switch]$SkipAcl
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

function Assert-NoReparseEntry {
    param([string]$Path, [string]$Label)
    $item = Get-Item -LiteralPath $Path -Force -ErrorAction Stop
    if ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) {
        throw "$Label contains a prohibited reparse point: $($item.FullName)"
    }
}

function Set-ExactRootAcl {
    param([string]$Path, [string]$OperatorSid)
    $admin = [Security.Principal.SecurityIdentifier]::new('S-1-5-32-544')
    $system = [Security.Principal.SecurityIdentifier]::new('S-1-5-18')
    $operator = [Security.Principal.SecurityIdentifier]::new($OperatorSid)
    $acl = [Security.AccessControl.DirectorySecurity]::new()
    $acl.SetAccessRuleProtection($true, $false)
    $acl.SetOwner($admin)
    $inheritance = [Security.AccessControl.InheritanceFlags]'ContainerInherit, ObjectInherit'
    foreach ($entry in @(
        @($system, [Security.AccessControl.FileSystemRights]::FullControl),
        @($admin, [Security.AccessControl.FileSystemRights]::FullControl),
        @($operator, [Security.AccessControl.FileSystemRights]::ReadAndExecute)
    )) {
        $rule = [Security.AccessControl.FileSystemAccessRule]::new(
            $entry[0], $entry[1], $inheritance,
            [Security.AccessControl.PropagationFlags]::None,
            [Security.AccessControl.AccessControlType]::Allow
        )
        [void]$acl.AddAccessRule($rule)
    }
    Set-Acl -LiteralPath $Path -AclObject $acl
}

function Assert-ExactAcl {
    param([string]$Path, [string]$OperatorSid)
    $allowed = @('S-1-5-18', 'S-1-5-32-544', $OperatorSid)
    $acl = Get-Acl -LiteralPath $Path
    $owner = ([Security.Principal.NTAccount]$acl.Owner).Translate([Security.Principal.SecurityIdentifier]).Value
    if ($owner -cne 'S-1-5-32-544' -or -not $acl.AreAccessRulesProtected) {
        throw "Guard ACL owner/protection mismatch: $Path"
    }
    $seen = @{}
    $forbidden = [Security.AccessControl.FileSystemRights]::WriteData -bor
        [Security.AccessControl.FileSystemRights]::AppendData -bor
        [Security.AccessControl.FileSystemRights]::WriteExtendedAttributes -bor
        [Security.AccessControl.FileSystemRights]::WriteAttributes -bor
        [Security.AccessControl.FileSystemRights]::DeleteSubdirectoriesAndFiles -bor
        [Security.AccessControl.FileSystemRights]::Delete -bor
        [Security.AccessControl.FileSystemRights]::ChangePermissions -bor
        [Security.AccessControl.FileSystemRights]::TakeOwnership
    foreach ($rule in $acl.GetAccessRules($true, $false, [Security.Principal.SecurityIdentifier])) {
        $sid = $rule.IdentityReference.Value
        if ($rule.AccessControlType -ne [Security.AccessControl.AccessControlType]::Allow -or $sid -notin $allowed) {
            throw "Guard ACL contains an unapproved rule: $Path ($sid)"
        }
        if ($sid -ceq $OperatorSid -and ($rule.FileSystemRights -band $forbidden)) {
            throw "Guard ACL grants operator write authority: $Path"
        }
        $seen[$sid] = $true
    }
    foreach ($sid in $allowed) {
        if (-not $seen.ContainsKey($sid)) { throw "Guard ACL lacks required principal: $Path ($sid)" }
    }
}

if ([string]::IsNullOrWhiteSpace($SourcePath)) {
    $SourcePath = $PSScriptRoot
}

$guardFiles = @(
    'validate-execution-request.py',
    'run-script-safe.ps1',
    'run-command-safe.ps1',
    'git-safe.ps1',
    'dispatch-execution-request.ps1'
)

try {
    $source = (Get-Item -LiteralPath $SourcePath -ErrorAction Stop).FullName
    $fileHashes = [ordered]@{}
    foreach ($name in $guardFiles) {
        $path = Join-Path $source $name
        if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
            throw "Required guard source is missing: $path"
        }
        Assert-NoReparseEntry -Path $path -Label 'Guard source'
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
                $copiedPath = Join-Path $stagingPath $name
                Assert-NoReparseEntry -Path $copiedPath -Label 'Staged guard'
                $copiedHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $copiedPath).Hash.ToLowerInvariant()
                if ($copiedHash -cne $fileHashes[$name]) {
                    throw "Copied guard identity mismatch: $name"
                }
            }
            $manifest = [ordered]@{
                schema_version = 'apex.guard-manifest/v1'
                identity = $identity
                acl_policy = 'admin-system-full-operator-rx/v1'
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

    $attestedManifest = [ordered]@{
        schema_version = 'apex.guard-manifest/v1'
        identity = $identity
        acl_policy = 'admin-system-full-operator-rx/v1'
        files = $fileHashes
    }
    [IO.File]::WriteAllText(
        (Join-Path $versionPath 'guard-manifest.json'),
        ($attestedManifest | ConvertTo-Json -Depth 4),
        [Text.UTF8Encoding]::new($false)
    )

    if (-not $SkipAcl) {
        Set-ExactRootAcl -Path $targetRoot -OperatorSid $userSid
        $aclOutput = @(& icacls.exe $versionPath '/inheritance:e' '/T' '/C' 2>&1)
        if ($LASTEXITCODE -ne 0) {
            throw "Could not enable exact guard inheritance: $($aclOutput -join [Environment]::NewLine)"
        }
        $aclOutput = @(& icacls.exe $versionPath '/reset' '/T' '/C' 2>&1)
        if ($LASTEXITCODE -ne 0) {
            throw "Could not reset guard DACLs: $($aclOutput -join [Environment]::NewLine)"
        }
        $aclOutput = @(& icacls.exe $versionPath '/setowner' $administratorsSid '/T' '/C' 2>&1)
        if ($LASTEXITCODE -ne 0) {
            throw "Could not transfer guard ownership: $($aclOutput -join [Environment]::NewLine)"
        }
        $aclOutput = @(& icacls.exe $versionPath '/grant:r' "*$userSid`:RX" '*S-1-5-18:F' "$administratorsSid`:F" '/T' '/C' 2>&1)
        if ($LASTEXITCODE -ne 0) {
            throw "Could not establish guard traversal: $($aclOutput -join [Environment]::NewLine)"
        }
        $aclOutput = @(& icacls.exe $versionPath '/inheritance:r' '/T' '/C' 2>&1)
        if ($LASTEXITCODE -ne 0) {
            throw "Could not remove guard inheritance: $($aclOutput -join [Environment]::NewLine)"
        }
        $aclOutput = @(& icacls.exe $versionPath '/grant:r' "*$userSid`:RX" '*S-1-5-18:F' "$administratorsSid`:F" '/T' '/C' 2>&1)
        if ($LASTEXITCODE -ne 0) {
            throw "Could not protect installed guards: $($aclOutput -join [Environment]::NewLine)"
        }
        Assert-ExactAcl -Path $targetRoot -OperatorSid $userSid
        Assert-ExactAcl -Path $versionPath -OperatorSid $userSid
        foreach ($item in Get-ChildItem -LiteralPath $versionPath -Recurse -Force) {
            Assert-ExactAcl -Path $item.FullName -OperatorSid $userSid
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
