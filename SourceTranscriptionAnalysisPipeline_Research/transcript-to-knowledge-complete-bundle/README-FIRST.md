# Transcript-to-Knowledge Complete Transfer Bundle

Snapshot date: 2026-08-18
Repository: leela-spec/apexai-os-meta
Branch: main
Authoritative v2 commit: 5858f1fa8102c22a007560f2a91914a3299d7ea9
Commit message: feat: rebuild transcript knowledge pipeline standalone

## What this bundle preserves

This archive is intended to be a lossless transfer/recovery bundle for the transcript-to-knowledge work from the ChatGPT execution environment.

It contains:

1. `current/skill-source/`
   - Exact unpacked source of the current v2 Skill.
   - This is the editable/recoverable source of truth inside the bundle.

2. `current/package/skill.zip`
   - The validated installable Skill package produced from the same v2 source.
   - Its files were compared against `current/skill-source/` before this bundle was made.

3. `current/research-v2/`
   - Macro architecture decision.
   - Detailed Meso module evaluation.
   - Micro implementation contract.
   - Validation report.
   - Research source ledger.
   - CLI handover.

4. `history/v1-skill-source/`
   - The superseded v1 Skill source preserved for architectural history.

5. `history/v1-research/`
   - The original v1 research/implementation report and upstream clone script.
   - This preserves the earlier Apex-KB-dependent assumption so the reason for the v2 redesign remains inspectable.

6. `checksums/SHA256SUMS.txt`
   - SHA-256 for every other file in the bundle.

7. `BUNDLE-MANIFEST.json`
   - Machine-readable provenance and restoration paths.

## Durable copies already outside ChatGPT

The current v2 files are already committed to GitHub at the immutable commit above.

Repository paths:

- Skill: `.claude/skills/transcript-to-knowledge/`
- Research: `apex-meta/validation/transcript-to-knowledge-20260818/v2/`

The repository remains the preferred long-term source of truth. This ZIP is an offline snapshot and transfer artifact.

## Restore into a checkout

From a checkout of `leela-spec/apexai-os-meta`, either pull the authoritative commit or copy from this bundle.

Preferred Git route:

```powershell
git switch main
git pull --ff-only origin main
```

Offline copy route, from the extracted bundle root:

```powershell
$Repo = "C:\path\to\apexai-os-meta"
Copy-Item ".\current\skill-source" "$Repo\.claude\skills\transcript-to-knowledge" -Recurse -Force
Copy-Item ".\current\research-v2\*" "$Repo\apex-meta\validation\transcript-to-knowledge-20260818\v2" -Recurse -Force
```

A safer scripted version is included as `RESTORE-TO-REPO.ps1` and requires `-Force` before it overwrites an existing Skill/research snapshot.

## Use the Skill without copying it elsewhere

Inside the repository, the Skill is already repository-local. Follow:

`current/research-v2/CLI-HANDOVER.md`

The public deterministic CLI is:

```text
.claude/skills/transcript-to-knowledge/scripts/ttk.py
```

## Verify this bundle

On PowerShell 7+:

```powershell
Get-ChildItem -Recurse -File | ForEach-Object {
  [PSCustomObject]@{
    Path = $_.FullName
    SHA256 = (Get-FileHash $_.FullName -Algorithm SHA256).Hash.ToLower()
  }
}
```

The canonical expected hashes are in `checksums/SHA256SUMS.txt`.

## Why both v1 and v2 are included

v1 is not current and should not be installed. It is retained because it documents the earlier reasoning and the architectural mistake of depending on Apex KB. v2 is the current implementation and intentionally works without Apex KB.
