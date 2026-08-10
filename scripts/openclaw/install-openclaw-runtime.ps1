[CmdletBinding()]
param(
    [string]$NodePath = 'C:\Users\gehma\AppData\Local\Programs\ApexNode\node-v24.18.0-win-x64\node.exe',
    [string]$ModulesPath = 'C:\Users\gehma\AppData\Local\Programs\ApexNpm\node_modules',
    [string]$TargetPath = 'C:\ProgramData\ApexExecutor\runtime',
    [switch]$SkipAcl
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

function Assert-NoReparseTree {
    param([string]$Path, [string]$Label)
    $root = Get-Item -LiteralPath $Path -Force -ErrorAction Stop
    if ($root.Attributes -band [IO.FileAttributes]::ReparsePoint) {
        throw "$Label contains a prohibited reparse point: $($root.FullName)"
    }
    if ($root.PSIsContainer) {
        $reparse = Get-ChildItem -LiteralPath $root.FullName -Recurse -Force |
            Where-Object { $_.Attributes -band [IO.FileAttributes]::ReparsePoint } |
            Select-Object -First 1
        if ($null -ne $reparse) {
            throw "$Label contains a prohibited reparse point: $($reparse.FullName)"
        }
    }
}

function Get-RelativeRuntimePath {
    param([string]$Root, [string]$Path)
    $relative = $Path.Substring($Root.Length).TrimStart([char]'\')
    return 'node_modules/' + $relative.Replace('\', '/')
}

function Get-RuntimeHashes {
    param([string]$RuntimePath)
    $hashes = [ordered]@{}
    $runtimeNode = Join-Path $RuntimePath 'node.exe'
    $runtimeModules = Join-Path $RuntimePath 'node_modules'
    $hashes['node.exe'] = (Get-FileHash -Algorithm SHA256 -LiteralPath $runtimeNode).Hash.ToLowerInvariant()
    foreach ($file in Get-ChildItem -LiteralPath $runtimeModules -Recurse -File | Sort-Object FullName) {
        $relative = Get-RelativeRuntimePath -Root $runtimeModules.TrimEnd('\') -Path $file.FullName
        $hashes[$relative] = (Get-FileHash -Algorithm SHA256 -LiteralPath $file.FullName).Hash.ToLowerInvariant()
    }
    return $hashes
}

function Get-RuntimeIdentity {
    param([System.Collections.IDictionary]$Hashes)
    $identityText = ($Hashes.GetEnumerator() | ForEach-Object { "$($_.Key):$($_.Value)" }) -join "`n"
    $hasher = [Security.Cryptography.SHA256]::Create()
    try {
        $bytes = [Text.Encoding]::UTF8.GetBytes($identityText)
        return ([BitConverter]::ToString($hasher.ComputeHash($bytes))).Replace('-', '').ToLowerInvariant()
    }
    finally { $hasher.Dispose() }
}

function Assert-RuntimeMatches {
    param(
        [string]$RuntimePath,
        [System.Collections.IDictionary]$ExpectedHashes
    )
    $actualHashes = Get-RuntimeHashes -RuntimePath $RuntimePath
    $expectedKeys = @($ExpectedHashes.Keys | Sort-Object)
    $actualKeys = @($actualHashes.Keys | Sort-Object)
    if ($expectedKeys.Count -ne $actualKeys.Count -or
        @(Compare-Object -ReferenceObject $expectedKeys -DifferenceObject $actualKeys).Count -ne 0) {
        throw 'Runtime file set mismatch: protected runtime has missing or unmanifested files'
    }
    foreach ($relative in $expectedKeys) {
        if ([string]$actualHashes[$relative] -cne [string]$ExpectedHashes[$relative]) {
            throw "Runtime file identity mismatch: $relative"
        }
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
    $propagation = [Security.AccessControl.PropagationFlags]::None
    foreach ($entry in @(
        @($system, [Security.AccessControl.FileSystemRights]::FullControl),
        @($admin, [Security.AccessControl.FileSystemRights]::FullControl),
        @($operator, [Security.AccessControl.FileSystemRights]::ReadAndExecute)
    )) {
        $rule = [Security.AccessControl.FileSystemAccessRule]::new(
            $entry[0], $entry[1], $inheritance, $propagation, [Security.AccessControl.AccessControlType]::Allow
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
        throw "Runtime ACL owner/protection mismatch: $Path"
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
            throw "Runtime ACL contains an unapproved rule: $Path ($sid)"
        }
        if ($sid -ceq $OperatorSid -and ($rule.FileSystemRights -band $forbidden)) {
            throw "Runtime ACL grants operator write authority: $Path"
        }
        $seen[$sid] = $true
    }
    foreach ($sid in $allowed) {
        if (-not $seen.ContainsKey($sid)) { throw "Runtime ACL lacks required principal: $Path ($sid)" }
    }
}

try {
    $node = (Get-Item -LiteralPath $NodePath -ErrorAction Stop).FullName
    $modules = (Get-Item -LiteralPath $ModulesPath -ErrorAction Stop).FullName.TrimEnd('\')
    $entry = Join-Path $modules 'openclaw\openclaw.mjs'
    $packageJson = Join-Path $modules 'openclaw\package.json'
    if (-not (Test-Path -LiteralPath $entry -PathType Leaf) -or
        -not (Test-Path -LiteralPath $packageJson -PathType Leaf)) {
        throw 'The source does not contain a complete OpenClaw package entry and package.json'
    }
    $package = Get-Content -Raw -LiteralPath $packageJson | ConvertFrom-Json
    if ([string]$package.version -cne '2026.7.1-2') {
        throw "Unexpected OpenClaw package version: $($package.version)"
    }
    Assert-NoReparseTree -Path $node -Label 'Runtime node source'
    Assert-NoReparseTree -Path $modules -Label 'Runtime module source'

    $targetRoot = [IO.Path]::GetFullPath($TargetPath)
    [IO.Directory]::CreateDirectory($targetRoot) | Out-Null
    # Copy first, then derive the manifest and identity from the exact staged
    # tree. Source changes during installation therefore cannot introduce an
    # installed file that is absent from the manifest.
    $staging = Join-Path $targetRoot ('.s-' + [Guid]::NewGuid().ToString('N').Substring(0, 8))
    [IO.Directory]::CreateDirectory($staging) | Out-Null
    Copy-Item -LiteralPath $node -Destination (Join-Path $staging 'node.exe')
    Copy-Item -LiteralPath $modules -Destination (Join-Path $staging 'node_modules') -Recurse
    # Re-scan the exact copied tree before reading package metadata or hashing.
    # This closes the source-swap window between the source scan and Copy-Item.
    Assert-NoReparseTree -Path (Join-Path $staging 'node.exe') -Label 'Staged runtime node'
    Assert-NoReparseTree -Path (Join-Path $staging 'node_modules') -Label 'Staged runtime modules'
    $stagedPackage = Get-Content -Raw -LiteralPath (Join-Path $staging 'node_modules\openclaw\package.json') | ConvertFrom-Json
    if ([string]$stagedPackage.version -cne '2026.7.1-2') {
        throw "Staged OpenClaw package version changed during copy: $($stagedPackage.version)"
    }
    $fileHashes = Get-RuntimeHashes -RuntimePath $staging
    $identity = Get-RuntimeIdentity -Hashes $fileHashes
    $versionPath = Join-Path $targetRoot ('openclaw-2026.7.1-2-' + $identity.Substring(0, 16))
    $alreadyExisted = Test-Path -LiteralPath $versionPath
    $userSid = [Security.Principal.WindowsIdentity]::GetCurrent().User.Value
    $administratorsSid = '*S-1-5-32-544'

    if ($alreadyExisted -and -not $SkipAcl) {
        $output = @(& takeown.exe '/F' $versionPath '/A' '/R' '/D' 'Y' 2>&1)
        if ($LASTEXITCODE -ne 0) { throw "Could not recover runtime ownership: $($output -join [Environment]::NewLine)" }
        $output = @(& icacls.exe $versionPath '/grant:r' "$administratorsSid`:F" '*S-1-5-18:F' "*$userSid`:RX" '/T' '/C' 2>&1)
        if ($LASTEXITCODE -ne 0) { throw "Could not recover runtime traversal: $($output -join [Environment]::NewLine)" }
    }

    if ($alreadyExisted) {
        Remove-Item -LiteralPath $staging -Recurse -Force
        $manifestPath = Join-Path $versionPath 'runtime-manifest.json'
        if (-not (Test-Path -LiteralPath $manifestPath -PathType Leaf)) {
            throw 'Existing runtime is incomplete and will not be overwritten'
        }
        $existingManifest = Get-Content -Raw -LiteralPath $manifestPath | ConvertFrom-Json
        if ([string]$existingManifest.identity -cne $identity) {
            throw 'Existing runtime identity mismatch and will not be overwritten'
        }
        $expectedHashes = [ordered]@{}
        foreach ($property in $existingManifest.files.PSObject.Properties) {
            $expectedHashes[$property.Name] = [string]$property.Value
        }
        Assert-RuntimeMatches -RuntimePath $versionPath -ExpectedHashes $expectedHashes
    }
    else {
        try {
            $manifest = [ordered]@{
                schema_version = 'apex.openclaw-runtime-manifest/v1'
                identity = $identity
                openclaw_version = '2026.7.1-2'
                acl_policy = 'admin-system-full-operator-rx/v1'
                files = $fileHashes
            }
            [IO.File]::WriteAllText(
                (Join-Path $staging 'runtime-manifest.json'),
                ($manifest | ConvertTo-Json -Depth 5),
                [Text.UTF8Encoding]::new($false)
            )
            Move-Item -LiteralPath $staging -Destination $versionPath
        }
        finally {
            if (Test-Path -LiteralPath $staging) { Remove-Item -LiteralPath $staging -Recurse -Force }
        }
    }

    $attestedManifest = [ordered]@{
        schema_version = 'apex.openclaw-runtime-manifest/v1'
        identity = $identity
        openclaw_version = '2026.7.1-2'
        acl_policy = 'admin-system-full-operator-rx/v1'
        files = $fileHashes
    }
    [IO.File]::WriteAllText(
        (Join-Path $versionPath 'runtime-manifest.json'),
        ($attestedManifest | ConvertTo-Json -Depth 5),
        [Text.UTF8Encoding]::new($false)
    )

    if (-not $SkipAcl) {
        Set-ExactRootAcl -Path $targetRoot -OperatorSid $userSid
        $output = @(& icacls.exe $versionPath '/inheritance:e' '/T' '/C' 2>&1)
        if ($LASTEXITCODE -ne 0) { throw "Could not enable exact runtime inheritance: $($output -join [Environment]::NewLine)" }
        $output = @(& icacls.exe $versionPath '/reset' '/T' '/C' 2>&1)
        if ($LASTEXITCODE -ne 0) { throw "Could not reset runtime DACLs: $($output -join [Environment]::NewLine)" }
        $output = @(& icacls.exe $versionPath '/setowner' $administratorsSid '/T' '/C' 2>&1)
        if ($LASTEXITCODE -ne 0) { throw "Could not transfer runtime ownership: $($output -join [Environment]::NewLine)" }
        # Establish explicit traversal before removing inheritance. Without
        # this pass, a deep tree can become inaccessible partway through the
        # recursive inheritance removal.
        $output = @(& icacls.exe $versionPath '/grant:r' "*$userSid`:RX" '*S-1-5-18:F' "$administratorsSid`:F" '/T' '/C' 2>&1)
        if ($LASTEXITCODE -ne 0) { throw "Could not establish runtime traversal: $($output -join [Environment]::NewLine)" }
        $output = @(& icacls.exe $versionPath '/inheritance:r' '/T' '/C' 2>&1)
        if ($LASTEXITCODE -ne 0) { throw "Could not remove runtime inheritance: $($output -join [Environment]::NewLine)" }
        $output = @(& icacls.exe $versionPath '/grant:r' "*$userSid`:RX" '*S-1-5-18:F' "$administratorsSid`:F" '/T' '/C' 2>&1)
        if ($LASTEXITCODE -ne 0) { throw "Could not protect runtime: $($output -join [Environment]::NewLine)" }
        Assert-ExactAcl -Path $targetRoot -OperatorSid $userSid
        Assert-ExactAcl -Path $versionPath -OperatorSid $userSid
        foreach ($item in Get-ChildItem -LiteralPath $versionPath -Recurse -Force) {
            Assert-ExactAcl -Path $item.FullName -OperatorSid $userSid
        }
    }

    Assert-RuntimeMatches -RuntimePath $versionPath -ExpectedHashes $fileHashes

    [ordered]@{
        installed_path = $versionPath
        identity = $identity
        openclaw_version = '2026.7.1-2'
        file_count = $fileHashes.Count
        acl_protected = -not [bool]$SkipAcl
        already_existed = [bool]$alreadyExisted
    } | ConvertTo-Json -Compress
}
catch {
    if ((Get-Variable -Name staging -ErrorAction SilentlyContinue) -and
        -not [string]::IsNullOrWhiteSpace($staging) -and
        (Split-Path -Leaf $staging).StartsWith('.s-', [StringComparison]::Ordinal) -and
        (Test-Path -LiteralPath $staging)) {
        Remove-Item -LiteralPath $staging -Recurse -Force -ErrorAction SilentlyContinue
    }
    Write-Error $_.Exception.Message
    exit 2
}

exit 0
