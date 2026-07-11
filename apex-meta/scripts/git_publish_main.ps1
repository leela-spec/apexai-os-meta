param(
  [Parameter(Mandatory = $true)]
  [string[]]$Path,

  [Parameter(Mandatory = $true)]
  [string]$Message
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$env:GIT_EDITOR = 'true'

function Invoke-Git {
  param(
    [Parameter(Mandatory = $true)]
    [string[]]$Args
  )

  & git @Args
  if ($LASTEXITCODE -ne 0) {
    throw "git $($Args -join ' ') failed with exit code $LASTEXITCODE"
  }
}

Invoke-Git @('rev-parse', '--show-toplevel') | Out-Null
$addArgs = @('add', '--') + $Path
Invoke-Git $addArgs

$staged = & git diff --cached --name-only
if ($LASTEXITCODE -ne 0) {
  throw 'git diff --cached --name-only failed'
}

if (-not $staged) {
  Write-Host 'Nothing staged; skipping commit and push.'
  exit 0
}

Invoke-Git @('commit', '-m', $Message)

try {
  $pushOutput = & git push origin main 2>&1
  $pushExit = $LASTEXITCODE
  if ($pushExit -eq 0) {
    exit 0
  }

  $pushText = ($pushOutput | Out-String)
  if ($pushText -notmatch 'non-fast-forward|fetch first|rejected') {
    throw $pushText
  }
} catch {
  if ($_.Exception.Message -notmatch 'non-fast-forward|fetch first|rejected') {
    throw
  }
}

Invoke-Git @('pull', '--rebase', '--autostash', 'origin', 'main')
Invoke-Git @('push', 'origin', 'main')
