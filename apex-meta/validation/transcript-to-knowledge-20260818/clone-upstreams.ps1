param(
    [string]$Destination = ".\upstream-transcript-benchmark"
)

$ErrorActionPreference = "Stop"

$repos = @(
    @{ Name = "faster-whisper"; Url = "https://github.com/SYSTRAN/faster-whisper.git"; Ref = "ed9a06cd89a93e47838f564998a6c09b655d7f43" },
    @{ Name = "whisperX"; Url = "https://github.com/m-bain/whisperX.git"; Ref = "2cfd7b7c5c7bba144954364db747319b50e8232b" },
    @{ Name = "Fabric"; Url = "https://github.com/danielmiessler/Fabric.git"; Ref = "338b89cfe97ab2d12ce30ce8b5449857a841366d" },
    @{ Name = "raptor"; Url = "https://github.com/parthsarthi03/raptor.git"; Ref = "7da1d48a7e1d7dec61a63c9d9aae84e2dfaa5767" }
)

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw "git is required."
}

New-Item -ItemType Directory -Path $Destination -Force | Out-Null

foreach ($repo in $repos) {
    $target = Join-Path $Destination $repo.Name
    if (Test-Path $target) {
        Write-Host "Skipping existing directory: $target"
        continue
    }
    git clone --filter=blob:none --no-checkout $repo.Url $target
    if ($LASTEXITCODE -ne 0) { throw "Clone failed: $($repo.Name)" }
    git -C $target fetch --depth 1 origin $repo.Ref
    if ($LASTEXITCODE -ne 0) { throw "Fetch failed: $($repo.Name)" }
    git -C $target checkout --detach $repo.Ref
    if ($LASTEXITCODE -ne 0) { throw "Checkout failed: $($repo.Name)" }
    $actual = git -C $target rev-parse HEAD
    Write-Host "$($repo.Name): $actual"
}
