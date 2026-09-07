# ext4 Startup Optimization & Zero-Touch 9p Eradication Guide

**Document ID:** ALR-005  
**Date:** 2026-09-07  
**Location:** `apex-meta/orchestration/new_final_v4/learnings_and_corrections/`  
**Target Architecture Level:** Tier 1 CLI Invocation & Host WSL Boundary  

---

## 1. Background & The ARCH-IMP-01 Guardrail

During the execution of WF02, WF03, and WF10, the CLI output contained the following diagnostic line:
```
[apex] Launched on /mnt (slow 9p bridge); switching to ext4: /root/workspaces/apexai-os-meta
```

### Clarification of Actual Behavior:
1. **The slow 9p bridge was NOT used for execution.**
2. The active safeguard script (`ARCH-IMP-01`) embedded in `/usr/local/bin/hermes` checked `$PWD`.
3. Seeing that the shell was launched from a Windows directory (`/mnt/c/...`), it immediately issued a `cd /root/workspaces/$__apex_repo` before starting Python.
4. All git operations, file reads, tool executions, and file writes occurred 100% natively on the ext4 Linux virtual hard disk (`/dev/sdd`).

---

## 2. The Lingering Startup Penalty

While execution is native ext4, spawning a subshell with an initial working directory on `/mnt/c/` still incurs a small initialization delay:
- WSL has to mount the Windows DrvFs filesystem driver.
- Bash resolves paths and environment variables across the Windows-Linux 9p bridge.
- The wrapper script executes the conditional branch and path translation before switching.

---

## 3. The Zero-Touch 9p Solution: Direct `--cd` Spawning

To completely eradicate the 9p bridge from the process startup lifecycle:

### Anti-Pattern (Inherited Windows Working Directory):
```powershell
# SPAWNS ON /mnt/c/ FIRST, FORCING WRAPPER PIVOT
wsl.exe -d Ubuntu -u root -e bash -c "/usr/local/bin/hermes ..."
```

### Optimized Pattern (Direct ext4 Launch):
```powershell
# SPAWNS DIRECTLY ON NATIVE EXT4; NEVER TOUCHES /mnt/
wsl.exe -d Ubuntu -u root --cd /root/workspaces/apexai-os-meta -e /usr/local/bin/hermes ...
```

### Verification
When launched with `--cd /root/workspaces/<repo>`, `/usr/local/bin/hermes` evaluates:
```bash
if [[ "$PWD" == /mnt/* ]]; then ...
```
Since `$PWD` is `/root/workspaces/apexai-os-meta`, the condition is false. Zero diagnostic messages are emitted, and execution begins instantly with zero filesystem translation overhead.
