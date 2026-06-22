---
name: deterministic-file-promotion
description: >
  Use this skill when the operator asks to replace canonical repo files with
  already-created variant files while preserving the old canonical files in a
  backup folder. Applies deterministic filesystem moves only, verifies exact
  paths and hashes, and prevents overwrite or content rewriting.
---

# Deterministic File Promotion

## Objective

Promote variant files into canonical paths without rewriting bytes. Move old
canonical files into a backup root preserving repo-relative paths, then move
variant files into the canonical names.

Use `scripts/promote_file_variants.py` for the move operation. The script uses
filesystem rename/move semantics and verifies promoted hashes after the move.

## Accepted Inputs

- A set of variant files already present in the repo.
- The canonical target path for each variant.
- A backup root, defaulting to `source-knowledge/Apex&Claude_old`.
- Optional original source file used to verify the canonical files after
  promotion.

## Required Procedure

1. Identify the exact variant-to-canonical mapping.
2. Confirm each variant file exists and each canonical path is repo-relative.
3. Run a dry-run first:

```powershell
python scripts/promote_file_variants.py `
  --backup-root "source-knowledge/Apex&Claude_old" `
  --map "path/to/file.final.md=path/to/file.md"
```

4. If dry-run is clean, run with `--apply`.
5. Verify:
   - variant paths no longer exist,
   - canonical paths exist with the former variant SHA256,
   - old canonical files exist under the backup root when they existed before,
   - no backup target was overwritten.
6. If the promoted files came from a source document with demanded target paths,
   re-parse that source and compare every canonical file byte-for-byte against
   the source block.

## Safety Rules

- Do not copy text content into new files.
- Do not use shell redirection, `Set-Content`, `Out-File`, heredocs, or manual
  file writes for promotion.
- Do not overwrite an existing backup path.
- Do not silently skip a missing variant.
- Do not rename paths by inference when the source document declares exact
  target paths.
- If any move fails mid-run, stop and report completed moves; do not invent a
  rollback.

## Communication Rule

Say "moved" only for filesystem move/rename operations. Avoid saying "wrote
into" or "copied content" unless that actually happened.

## Completion Gate

The operation is complete only when the exact canonical paths exist, hashes
match the variants or original source blocks, old files are backed up when
applicable, and no temporary variant paths remain.
