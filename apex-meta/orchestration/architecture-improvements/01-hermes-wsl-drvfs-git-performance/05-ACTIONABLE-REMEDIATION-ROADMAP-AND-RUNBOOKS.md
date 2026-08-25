# 05 — Actionable Remediation Roadmap & Incident Runbooks

**Module ID:** `ARCH-IMP-05-ROADMAP-AND-RUNBOOKS`  
**Parent Package:** `01-hermes-wsl-drvfs-git-performance`  
**Date:** 2026-08-25  

---

## 1. Actionable Remediation Steps

The following steps define the concrete execution sequence to permanently remediate the Hermes DrvFs Git performance bottleneck:

### Step 1: Enforce Repository-Level Git Optimization Configuration
Apply performance tuning parameters to all local repository clones (both Windows and WSL2):

```bash
# Optimize index preloading across threads
git config core.preloadindex true

# Enable file system cache (Windows / Git for Windows)
git config core.fscache true

# Disable executable bit tracking across OS boundaries
git config core.fileMode false

# Enable untracked cache for rapid status queries
git config core.untrackedCache true

# Optimize garbage collection threshold
git config gc.auto 256
```

---

### Step 2: Patch `AGENTS.md` with Scoped Git Dispatch Guardrails
Update the root `AGENTS.md` operating note to explicitly mandate scoped Git execution and suppress full-tree untracked scans.

#### Proposed Exact-Match Patch for `AGENTS.md`:

```markdown
## Git Dispatch
- Trigger: A request to push known files starts with the Git commands, not repository analysis.
- Sequence: Run `git add -- <requested paths>`, `git commit -m "<msg>" -- <requested paths>`, and `git push`.
- Scoping: In large repositories or WSL cross-mounts, avoid broad `git status`; use `git status --short -uno` or direct file commits (`git commit -o <paths>`).
- Filesystem Law: Linux agents (Hermes, Codex in WSL) must execute in canonical ext4 workspaces (`/root/workspaces/...`). If operating on `/mnt/c/`, use `git.exe` or strict path scoping.
- Retry: On non-fast-forward, run `git pull --rebase` and retry the push.
- Ignore: Unrelated dirty files are irrelevant and must not trigger inspection, stashing, worktrees, branches, or discussion.
- Escalate: Investigate only an actual command failure involving the requested files, validation, authentication, or merge conflicts.
- Stop: Report success immediately after the push completes.
```

---

### Step 3: Update `.gitignore` for Ephemeral Simulation Logs
Add rules to ignore transient simulation raw logs in future runs to avoid inflating the Git index:

```gitignore
# Ephemeral Simulation Logs & Dumps
apex-meta/orchestration/simulation/**/raw-evidence/*.log
apex-meta/orchestration/simulation/**/raw-dump-*.log
```

---

## 2. Emergency Incident Recovery Runbook

If an agent or operator encounters a frozen Git process or a stale `.git/index.lock`, execute the following deterministic recovery sequence:

### Diagnostic & Recovery Sequence:

1. **Step 1: Check Process State (`ps aux`)**
   ```bash
   ps aux | grep -i git | grep -v grep
   ```
   - If the `STAT` column shows `D` (uninterruptible disk wait), **DO NOT issue `kill -9` repeatedly**. The process is waiting for Windows host I/O.
   - Wait 15–30 seconds for the underlying I/O to flush.

2. **Step 2: Terminate Stuck Process from Windows Host (if on DrvFs)**
   If running on `/mnt/c/`, the lock is held by the Windows host filesystem driver. Run in Windows PowerShell:
   ```powershell
   Get-Process -Name "git*" | Stop-Process -Force -ErrorAction SilentlyContinue
   ```

3. **Step 3: Remove Stale Index Lock**
   ```bash
   rm -f .git/index.lock
   ```

4. **Step 4: Verify Repository Health**
   ```bash
   git status --short -uno
   ```

---

## 3. Verification & Compliance Checklist

| Verification Task | Target Command | Expected Output | Status |
| :--- | :--- | :--- | :---: |
| **Git Status Speed** | `git status --short -uno` | Execution time < 0.5s | READY |
| **Index Lock Integrity** | `test -f .git/index.lock` | Returns false (no stale lock) | PASS |
| **Handover Artifact Presence** | `git log -n 1 --oneline` | Shows `9fa466c3 docs(campaign): reviewer handover...` | PASS |
| **Documentation Integrity** | `ls apex-meta/orchestration/architecture-improvements/01-hermes-wsl-drvfs-git-performance/` | All 6 modules present and indexed | PASS |
