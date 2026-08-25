# 07 — Execution Runbook: Untrack Vendor Repos + Filesystem Guardrail

**Module ID:** `ARCH-IMP-07-EXECUTION-RUNBOOK`
**Parent Package:** `01-hermes-wsl-drvfs-git-performance`
**Date:** 2026-08-25
**Status:** ✅ EXECUTED 2026-08-25 — see Execution Log below.

---

## EXECUTION LOG (2026-08-25)

All steps executed with Hermes stopped (`wsl --shutdown`, which also cleared a `git pull`
that had hung since Aug 24). Verified end-to-end.

| Step | What was done | Evidence |
| :--- | :--- | :--- |
| Untrack vendor repos | `git rm -r --cached source-knowledge/ProjectRepos` + `.gitignore` | commit `88377124`, pushed; tracked files 53,872 → 11,099; 42,772 files remain on disk in `C:\GitDev` |
| AGENTS.md rule | one-line ext4 filesystem rule | commit `d0ec89c1`, pushed |
| ext4 canonical copy | fast-forwarded `/root/workspaces/apexai-os-meta` to `d0ec89c1` | 11,099 files; stray pre-existing files saved in `stash@{0}`; ProjectRepos files removed from the ext4 copy's disk (still present in `C:\GitDev` + git history) |
| Launch guard (soft) | `/root/.bashrc` auto-cd off `/mnt` + `hermes` refusal function | backup `/root/.bashrc.bak.pre-archimp01` |
| **Launch enforcement (hard)** | ext4 gate inserted into **all three** launchers `/usr/local/bin/{hermes,hermes-acp,hermes-agent}` — auto-redirects a `/mnt` launch to the matching ext4 repo, else refuses and exits 1 | backups `*.orig.pre-archimp01`; refusal verified live |

**Measured proof** (`git status -uno`, same repo/commit, 11,099 files):
ext4 = **0.557s** vs `/mnt/c` = **6m 11s** (≈666×).

### ⚠️ Durability caveat
The hard gate lives in the shipped launcher binaries. A future `hermes` self-update may
overwrite `/usr/local/bin/hermes*` and remove the gate. After any Hermes update, re-apply the
gate (originals are backed up as `*.orig.pre-archimp01`), or re-run the enforcement step. The
`.bashrc` soft guard survives updates and remains as a secondary layer.

---

**Original runbook (retained for reference / re-application):**

> This runbook covers the two-sided fix from module 06:
> **Side B(i)** — untrack the downloaded vendor repos (repo reduction), and
> **Side A + B(ii)** — the filesystem guardrail so agents stop working across the slow `/mnt/c/` bridge.
>
> Operator confirmed decisions: untrack the **entire** `source-knowledge/ProjectRepos/` folder,
> keep every file **on disk**, execute **later** (Hermes is currently live).

---

## 0. WHY NOT NOW (read this first)

Hermes is running. Committing a 42,773-file removal while another agent touches the same `.git` is the
**exact condition that caused the original incident**: two writers racing for `.git/index.lock`. Doing
it now risks index corruption or a repeat deadlock. **Run this only when Hermes is fully stopped and
no git process is active.** Precondition checks are in §1.

**Verified facts this runbook is built on (as of 2026-08-25):**
- Remote: `https://github.com/leela-spec/apexai-os-meta.git`
- Branch: `main`
- Untrack scope: **42,773** files under `source-knowledge/ProjectRepos/`
- Must STAY tracked: the **235** other files under `source-knowledge/` (do NOT untrack all of
  `source-knowledge/` — only `ProjectRepos/`)
- Tracked total now: **53,872** → expected after: **~11,099**

---

## 1. PRECONDITIONS — confirm Hermes is stopped

Run in **WSL / the Hermes environment**:

```bash
# Expect NO hermes and NO git processes listed
ps aux | grep -iE 'hermes|[g]it ' | grep -v grep
```

Run in the repo folder (**Windows PowerShell**, `C:\GitDev\apexai-os-meta`):

```powershell
# Expect: False  (no stale lock)
Test-Path .git\index.lock
```

If either shows activity or a lock, **stop** — Hermes is still live. Do not proceed.

**Ordering vs. an in-flight Hermes commit:** If Hermes was mid-workflow (e.g. applying a patch pack
and pushing to `main`), let it fully finish and **end the session first**, then sync before untracking
so you don't push a stale `main`:

```powershell
git fetch origin
git status            # if it says "behind origin/main", pull before continuing:
git pull --rebase origin main
```

Only after this is clean, proceed to Part A. Never run Part A while any other agent can write to
this `.git`.

> Run everything below from **Windows PowerShell**, not from inside WSL. Windows PowerShell uses the
> native `git.exe` on NTFS (the fast path); running it from WSL on `/mnt/c/` is the slow path this
> whole package is about.

---

## 2. PART A — Untrack `source-knowledge/ProjectRepos/` (keep on disk)

Copy-paste this block into **Windows PowerShell** in `C:\GitDev\apexai-os-meta`:

```powershell
# --- 2.1 Safety branch (so review/rollback is trivial) ---
git checkout -b chore/untrack-projectrepos

# --- 2.2 Add the ignore rule BEFORE untracking (so the 42k files don't reappear as "untracked") ---
Add-Content -Path .gitignore -Encoding utf8 -Value @"

# Downloaded third-party reference repos - kept on disk, not version-controlled (ARCH-IMP-01, module 06).
# Re-enable tracking by deleting the next line, then: git add source-knowledge/ProjectRepos
source-knowledge/ProjectRepos/
"@

# --- 2.3 Untrack the folder. --cached keeps every file on disk; only Git stops watching them. ---
git rm -r --cached --quiet source-knowledge/ProjectRepos

# --- 2.4 VERIFY before committing (do NOT run a full `git status` - it would print 42k lines) ---
Write-Host "Staged deletions (expect 42773):"
(git diff --cached --name-only --diff-filter=D | Measure-Object -Line).Lines

Write-Host "Files still tracked after this change (expect ~11099):"
$after = (git ls-files | Measure-Object -Line).Lines - (git diff --cached --name-only --diff-filter=D | Measure-Object -Line).Lines
Write-Host $after

Write-Host "Files still PHYSICALLY on disk (expect a large number - proves nothing was deleted):"
(Get-ChildItem -Recurse -File source-knowledge\ProjectRepos | Measure-Object).Count
```

**Gate:** only continue if 2.4 shows ~42,773 staged deletions **and** the files are still on disk.

```powershell
# --- 2.5 Commit ---
git add .gitignore
git commit -m "chore(repo): untrack source-knowledge/ProjectRepos vendor clones; keep on disk (ARCH-IMP-01)"

# --- 2.6 Push the branch ---
git push -u origin chore/untrack-projectrepos
```

Then either merge `chore/untrack-projectrepos` into `main` via GitHub, or if you prefer committing
straight to main, skip step 2.1 and run 2.2–2.6 on `main` directly.

### Rollback (if anything looks wrong)
```powershell
# Before pushing / merging: undo the commit, keep files (they were never deleted)
git reset --soft HEAD~1        # undo commit, keep staged
git reset                      # unstage
# then delete the two added lines from .gitignore
```
Nothing in Part A ever deletes a file from disk. Worst case is a reverted commit.

> **Scope note (honest):** This makes Git *stop scanning* 42k files, which is what fixes
> `status`/`commit` speed. It does **not** shrink Git *history* — past commits still contain those
> files, so a fresh `clone` stays large. A history purge (`git filter-repo`) is a separate, more
> invasive operation; only do it later if clone size becomes a problem. It is NOT needed for the
> performance fix.

---

## 3. PART B — The filesystem fix (this is the side that actually cures the stall)

Untracking speeds Git up ~5×. But per module 06 §5a, the **cure** is to stop running agents across the
`/mnt/c/` bridge at all. Three layers, strongest first.

### 3.1 (Strategic cure) Move the live working copy to native ext4
Do this in **WSL Ubuntu**, Hermes stopped:

```bash
mkdir -p /root/workspaces
cd /root/workspaces
git clone https://github.com/leela-spec/apexai-os-meta.git apexai-os-meta
```

- All agents/Hermes then operate in `/root/workspaces/apexai-os-meta` (native ext4, git is instant).
- Windows tools (Obsidian, VS Code, Explorer) open it via UNC:
  `\\wsl.localhost\Ubuntu\root\workspaces\apexai-os-meta`
- The old `C:\GitDev\apexai-os-meta` copy becomes deprecated. **Before abandoning it, commit/push any
  uncommitted work from it first** (it currently has local modifications), so nothing is lost.

> This is a bigger change (two copies exist until you retire the old one). Treat it as its own gated
> step — but it is the real answer to "we need to fix that slow bridge."

### 3.2 (Guardrail) Runtime preflight that refuses the slow path
So no future launch can silently land on `/mnt/c/` again. Put this at the top of the Hermes container
entrypoint and/or `/root/.bashrc` **inside the WSL/Hermes environment** (not in this repo):

```bash
# ext4 guard — refuse heavy work on the slow 9P bridge
if pwd -P | grep -q '^/mnt/'; then
  echo "ABORT: working dir is on /mnt (slow WSL 9P bridge). Relocate to /root/workspaces/<repo>." >&2
  exit 1
fi
```

Fallback shim for unavoidable one-off host-path work (routes git to the fast Windows binary):

```bash
git() { if [[ "$(pwd -P)" == /mnt/* ]]; then git.exe "$@"; else command git "$@"; fi; }
```

> I cannot wire 3.1/3.2 from this repo — the Hermes launch/container config lives in the WSL
> environment, which I can't see from here. Candidate locations to place them: the Hermes container
> **entrypoint script**, the **Hermes launch/run config**, and `/root/.bashrc`. When Hermes is
> stopped, I can help you locate and edit the exact file in a WSL session.

### 3.3 (Policy) Write the rule into `AGENTS.md` so every agent obeys it
`AGENTS.md` is loaded by all agents (and `CLAUDE.md`/`GEMINI.md`/`.hermes.md` are symlinks to it, so
one edit covers everyone). Apply this **exact-match patch** later (repo patch-safety rule: copy the
`<old>` block byte-for-byte from the live file; it must match exactly once):

```text
<file>AGENTS.md</file>
<old>
- Stop: Report success immediately after the push completes.

## Directness
</old>
<new>
- Stop: Report success immediately after the push completes.
- Scoping: In large repos or WSL cross-mounts, avoid broad `git status`; use `git status --short -uno`, and stage/commit by path (`git add -- <paths>`; `git commit -o <paths>`).

## Filesystem Law
- Rule: Linux agents (Hermes, Codex/Claude in WSL) MUST operate in native ext4 workspaces (`/root/workspaces/<repo>`). NEVER run heavy git or file-scan tools across `/mnt/c/` (the WSL 9P bridge); it causes multi-minute stalls and unkillable D-state locks.
- Preflight: If the working path begins with `/mnt/`, abort and relocate to `/root/workspaces/<repo>` (or, for one-off host-path work, use `git.exe`).
- Recovery: If a git process hangs, check `ps aux | grep git` for STAT `D`; do NOT spam `kill -9`. Kill from Windows (`Get-Process git* | Stop-Process -Force`), then `rm -f .git/index.lock`.

## Directness
</new>
```

> Note: this intentionally adds a guardrail even though `## Directness` says "do not invent extra
> guardrails." That rule targets *incidental ceremony*; a filesystem law that prevents a total outage
> is a justified, load-bearing control — the exact gap module 06 §5b identified.

---

## 4. RECOMMENDED ORDER WHEN HERMES IS DOWN

1. §1 preconditions (confirm Hermes stopped, no lock).
2. §2 Part A — untrack `ProjectRepos` (fast, low-risk, reversible).
3. §3.3 — apply the `AGENTS.md` patch (documented rule, immediate).
4. §3.1 — migrate the working copy to `/root/workspaces/` (the real cure) — after committing any
   pending work from the old copy.
5. §3.2 — add the runtime guard in the WSL/Hermes launch path so it can never regress.

Steps 2–3 are safe and reversible. Steps 4–5 are the durable cure; do them once you're ready to make
`/root/workspaces/` the single working copy.

---

## 5. POST-EXECUTION VERIFICATION

```powershell
# Tracked count dropped
(git ls-files | Measure-Object -Line).Lines            # expect ~11,099

# ProjectRepos is now ignored
git check-ignore source-knowledge/ProjectRepos          # prints the path = ignored (correct)

# Files still on disk
(Get-ChildItem -Recurse -File source-knowledge\ProjectRepos | Measure-Object).Count   # large = intact
```

Optional speed proof in **WSL** (before vs after the ext4 migration):
```bash
cd /mnt/c/GitDev/apexai-os-meta && time git status -uno    # slow (old path)
cd /root/workspaces/apexai-os-meta && time git status -uno # fast (cured path)
```
