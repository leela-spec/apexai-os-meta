---
type: Adapter
id: ADPT-EXEC-SYNC-v0.2
title: Adapter 6 — Git Sync & File Preservation (EM-12)
description: Immediate-execution sync behaviour, preservation of unrelated dirty files, and rebase retry on non-fast-forward.
tags: [execution-modes, git, sync, em-12]
status: current
---

## 7. Adapter 6: Git Sync & File Preservation

- **EM-12 [P2 | I80/E90/R08] Conditional Sync (`Synch`) & Scoped Push Trigger**:
  - **IF** pushing named files (`git push <paths>`) → **THEN** stage only those paths, commit, and push (`git pull --rebase` on non-fast-forward), ignoring unrelated dirty files.
  - **IF** the operator calls for a `sync` / `synch` → **THEN** execute a full push-and-pull synchronization (`git pull --rebase` and `git push`) paired with a quick status check to ensure no files are accidentally lost in the process.
  - **IF** files have been explicitly marked for deletion → **THEN** allow their deletion during sync; **ELSE** preserve all files and never drop or exclude remaining dirty files just because they were outside the current task scope (commit unrelated files in a separate commit if needed so all work is safely preserved).

---
