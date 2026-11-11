<#
    Phase 0 host capability probe for the multi-CLI harness evaluation.
    Read-only. Installs nothing, contacts no network service, spends no provider quota.

    Usage:
        powershell -ExecutionPolicy Bypass -File probe-host.ps1
        powershell -ExecutionPolicy Bypass -File probe-host.ps1 -IncludeWsl

    -IncludeWsl additionally boots the default WSL2 distro to read python3, tmux and uv
    versions there. That boot can take minutes on a cold distro, so it is opt-in. It is
    required only if CAO (awslabs/cli-agent-orchestrator) reaches Phase 4, since CAO
    raises ImportError on win32 and needs tmux 3.3 or later.
#>

[CmdletBinding()]
param(
    [switch]$IncludeWsl
)

$ErrorActionPreference = 'Continue'

function Get-ToolVersion {
    param([string]$Name, [string]$VersionArg)
    $cmd = Get-Command $Name -ErrorAction SilentlyContinue
    if (-not $cmd) { return 'ABSENT' }
    try {
        $out = & $Name $VersionArg 2>&1 | Select-Object -First 1
        if ($out) { return "$out" } else { return 'present (no version output)' }
    } catch {
        return 'present (version call failed)'
    }
}

Write-Output "# Host capability probe - $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
Write-Output ''

Write-Output '## Operating system'
$os = Get-CimInstance Win32_OperatingSystem
Write-Output ("{0} build {1}" -f $os.Caption, $os.BuildNumber)
Write-Output ''

Write-Output '## Native Windows toolchain'
$tools = [ordered]@{
    node   = '--version'   # Paseo plugins are npm packages
    npm    = '--version'
    git    = '--version'
    claude = '--version'   # must be the unmodified Claude Code binary
    codex  = '--version'
    tmux   = '-V'          # CAO prerequisite; no native Windows build exists
    uv     = '--version'   # CAO installer
    paseo  = '--version'
}
foreach ($t in $tools.GetEnumerator()) {
    Write-Output ("{0,-8} {1}" -f $t.Key, (Get-ToolVersion -Name $t.Key -VersionArg $t.Value))
}
Write-Output ''

Write-Output '## Account-home environment variables'
Write-Output '(each must be unset, or set per account - never shared across accounts)'
foreach ($v in 'CLAUDE_CONFIG_DIR', 'CLAUDE_HOME', 'CODEX_HOME') {
    $val = [Environment]::GetEnvironmentVariable($v)
    if ($val) { Write-Output "$v=$val" } else { Write-Output "$v=<unset>" }
}
Write-Output ''

Write-Output '## Provider and harness homes'
foreach ($d in '.claude', '.codex', '.paseo', '.openmausbot', '.orca') {
    $p = Join-Path $env:USERPROFILE $d
    if (Test-Path $p) {
        $n = (Get-ChildItem $p -ErrorAction SilentlyContinue | Measure-Object).Count
        Write-Output ("present: {0}  ({1} entries)" -f $p, $n)
    } else {
        Write-Output ("absent : {0}" -f $p)
    }
}
Write-Output ''

Write-Output '## Symlink creation without elevation'
Write-Output '(Developer Mode; CAO falls back to copying skill content when unavailable)'
$tmp = Join-Path $env:TEMP ("probe-" + [guid]::NewGuid().ToString('N').Substring(0, 8))
try {
    New-Item -ItemType Directory -Path $tmp -Force | Out-Null
    New-Item -ItemType SymbolicLink -Path (Join-Path $tmp 'lnk') -Target $tmp -ErrorAction Stop | Out-Null
    Write-Output 'symlink: OK'
} catch {
    Write-Output 'symlink: DENIED (enable Developer Mode, or accept the copy fallback)'
} finally {
    if (Test-Path $tmp) { Remove-Item $tmp -Recurse -Force -ErrorAction SilentlyContinue }
}
Write-Output ''

if ($IncludeWsl) {
    Write-Output '## WSL2 (CAO requires POSIX APIs and tmux 3.3 or later)'
    if (Get-Command wsl.exe -ErrorAction SilentlyContinue) {
        (wsl.exe -l -v 2>&1) -replace "`0", '' | Write-Output
        Write-Output '-- inside the default distro --'
        wsl.exe -e bash -lc 'echo "python3: $(python3 --version 2>&1)"; echo "tmux   : $(tmux -V 2>&1 || echo ABSENT)"; echo "uv     : $(uv --version 2>&1 || echo ABSENT)"' 2>&1 | Write-Output
    } else {
        Write-Output 'wsl.exe ABSENT'
    }
} else {
    Write-Output '## WSL2'
    Write-Output 'skipped - pass -IncludeWsl to probe the default distro (slow on a cold boot)'
}
