---
type: Search Log
title: How the old-plans / failure-history search was done (provenance for the next AI)
description: >
  Records the exact methods used to find the old/failed/superseded plans and reconstruct the ~2-month
  architecture rebuild/failure history — what was searched, what was found, what is genuinely missing
  (out-of-git), what was deliberately excluded, and the best NEXT searches. So another AI can extend the
  search without redoing covered ground.
created: 2026-09-29
companions: [INDEX.md, REBUILD-AND-FAILURE-HISTORY.md]
repo_span_searched: "apexai-os-meta git: 2026-04-29 → 2026-09-29, 1549 commits on main"
---

# Search log — old plans & failure history

**Purpose.** Provenance for [`INDEX.md`](INDEX.md) and [`REBUILD-AND-FAILURE-HISTORY.md`](REBUILD-AND-FAILURE-HISTORY.md).
If you're a later AI asked to "find the old plans / the rebuild history / the 9P work again," **start here** —
it tells you what was already covered so you don't repeat it, and where the unmined frontier is.

## 1. What we were looking for
- The project's own OLD / FAILED / SUPERSEDED / CORRECTED / DEFERRED implementation & execution plans.
- The truthful ~2-month Docker/ki-basis rebuild arc, including the **Docker Desktop → WSL2** pivot, the
  **separation → shared-Postgres** reversal, and the **9P (`/mnt/c`) filesystem bottleneck**.
- Out-of-git artifacts the operator remembers (e.g. the 2026-06-27 "Docker-Fließband" runbook PDF).

## 2. Methods used (reproducible)
Run from `C:\GitDev\apexai-os-meta` unless noted. (Tooling note for Windows: run non-trivial WSL/docker via a
script file piped `tr -d '\r' | bash` — inline `bash -c "…"` through `wsl.exe` mangles variables.)

**Git history**
- Span + volume: `git log --reverse --date=short --pretty='%ad %h %s' | head -1`; `git rev-list --count HEAD`;
  per-month: `git log --date=format:'%Y-%m' --pretty='%ad' | sort | uniq -c`.
- Topic timeline: `git log --reverse --date=short --pretty='%ad|%s' | grep -iE 'docker|ki-basis|hermes|openproject|architect|consolidat|separat|rebuild|fail|desktop|wsl|migrat|drift|compose|stack|postgres|runbook'` (excluding `flow-execution|weekly_plan|simulation`).
- 9P specifically: `git log --all --pretty='%ad|%h|%s' | grep -iE '9p|drvfs|v9fs|plan9|d-state|bottleneck|git.?perf'` → **only 2 hits** (`5d17c536`, `d0ec89c1`, both 2026-08-25). 9P lives in FILES, not commit messages.
- Branch inventory: `git branch -a`.

**File search (globs)**
- `**/*PLAN*.md`, `**/*[Ii]mplementation*.md`, `**/ImplementationPlans/**/*.md` (Glob tool).
- These hit heavy vendored noise — filtered out (see §4).

**Content search (grep / git grep)**
- `git grep -liE '9p|drvfs|v9fs|plan 9|D-state|uninterruptible' -- '*.md'` (then filtered out vendored trees).
- Keyword sweeps for `SECRET_KEY_BASE`, `ProjectMM/openproject`, etc. (used by sibling tasks).

**Sub-agent classification**
- One general-purpose agent read/classified ~70–75 of our plans into OLD/SUPERSEDED/CORRECTED/FAILED/DEFERRED
  → became [`INDEX.md`](INDEX.md). It respected the §4 excludes.

**Out-of-git artifact hunt**
- `find /c/GitDev /c/Users/gehma/Downloads /c/Users/gehma/Documents -iname '*.pdf' | grep -iE 'flie|fliess|band|docker|runbook|ki.?basis'` and `-iname '*flie*band*'` → **the 2026-06-27 PDF was NOT found.**
- Incident ledger read in full: `03-wsl2-native-stack-consolidation/02-decisions-log.md` (D-01…D-18).

## 3. What was FOUND (and where it lives)
- **The old/failed plans** → catalogued in [`INDEX.md`](INDEX.md) (12 groups, ~70–75 files).
- **The 9P bottleneck material** (this is the part the operator worried was lost — it is NOT lost):
  - Plan bundle: `apex-meta/orchestration/architecture-improvements/01-hermes-wsl-drvfs-git-performance/`
    (8 files: 00-INDEX, 01-INCIDENT-DIAGNOSIS, 02-KERNEL-FS-AND-WEB-BENCHMARKS, 03-COMMITS-SCALE-AUDIT,
    04-FIX-PROPOSALS, 05-REMEDIATION-ROADMAP, 06-VERIFICATION-AND-CORRECTED-SOLUTION, 07-EXECUTION-RUNBOOK).
  - Commits: `5d17c536` (the package) and `d0ec89c1` (ext4 workspace rule), both 2026-08-25.
  - Deep analysis (benchmarks, D-state, 350% CPU, OpenProject chown/fcntl crash): `ki-basis/docs/DUAL_INSTANCE_ARCHITECTURE.md` **§2**.
  - The standing rule: root `CLAUDE.md`/`AGENTS.md` ("never `/mnt/c`, the slow 9p bridge").
  - Now also ranked as **R1b** in [`REBUILD-AND-FAILURE-HISTORY.md`](REBUILD-AND-FAILURE-HISTORY.md).
- **The incident record** → `02-decisions-log.md` D-01…D-18.
- **The current target** → [`../INFRASTRUCTURE.md`](../INFRASTRUCTURE.md).

## 4. Deliberately EXCLUDED (so you don't waste time)
`source-knowledge/`, `apex-meta/kb/` and any `/raw/` tree (vendored KB), `ApexDefinition&OldVersions/`,
`antigravity-awesome-skills`, `bmad`, `node_modules`, `researcher-attachments-*` (evidence duplicates), and
~130 simulation fixtures (`flow-execution-card.md`, `weekly_plan.md`). These are third-party or output, not
our plans.

## 5. What is MISSING / not yet covered (the frontier)
1. **The 2026-06-27 "Docker-Fließband" runbook PDF** — not on disk, not in git (out-of-git). Only known from
   an operator screenshot (8 pp, 614 kB, "noch in Arbeit"). **Where to look next:** the operator's chat
   exports / cloud (Claude/ChatGPT uploads), OneDrive, `~/Downloads` history, email. If recovered, drop it in
   `OldPlans/` and index it.
2. **Out-of-git execution steps** — the manual Docker Desktop build (Sep 1) and the live WSL2 cutover
   (Sep 25–26) were hand-run in the terminal; only their *artifacts/decisions* are in git. Terminal history
   (WSL `~/.bash_history`, PowerShell `ConsoleHost_history.txt`) may hold the actual commands.
3. **Unmined branches** — history/plans may exist off `main`. Not yet searched per-branch:
   `codex/separate-community-stack` (the "separations" work), and many `origin/agent/*`, `origin/claude/*`
   branches. Try: `git log --all --oneline`, `git log origin/codex/separate-community-stack`,
   `git branch -a | grep -iE 'hermes|docker|kb|fee|community|stack'`.
4. **9P in commit messages is thin (2)** — do NOT conclude 9P work is small; it's in files (§3), not messages.
5. **Renames** — plans were moved between folders (e.g. "move docker tool stack implementation plans to
   Alpine/ImplementationPlans/"). Use `git log --all --follow -- <path>` to trace a plan's true origin/date.
6. **`.agents/` scratch** — many `.agents/**` files mention 9P/infra diagnostics; they're throwaway agent
   scratch but may hold incident detail not written up elsewhere.

## 6. Suggested next searches (copy-paste)
```
# branches that might hold lost plans
git log --all --oneline --date=short --pretty='%ad %h %d %s' | grep -iE '9p|drvfs|docker|hermes|separat|community|stack|kb'
git log origin/codex/separate-community-stack --oneline | head -40
# trace a plan's real origin across renames
git log --all --follow --date=short -- 'apex-meta/Alpine/ImplementationPlans/01-META-IMPLEMENTATION-PLAN-ANTIGRAVITY.md'
# out-of-git command history (inside WSL)
wsl -d Ubuntu -u root -- bash -lc 'grep -iE "docker|compose|pg_restore|wsl" ~/.bash_history | tail -80'
# recover the 27-Jun PDF from the host
find /c/Users/gehma -iname '*.pdf' -newermt 2026-06-20 ! -newermt 2026-07-05 2>/dev/null
```

_Anything a later search adds should be appended here so this log stays the single provenance record._

## 7. Results of the branch + out-of-git sweep (run 2026-09-29)
Actually ran the §6 searches. Recorded so the next AI doesn't redo them:
- **More 9P/ext4 commits exist than the message-search showed** (`git log --all`): `5d17c536` (DrvFs package),
  `d0ec89c1` (ext4 workspace rule), `cca426ef` (record ARCH-IMP-01 execution + ext4 launch enforcement + root-cause
  confirmation), `d389a1c5` (consolidate weekly artifacts on ext4) — **all 2026-08-25**. So the 9P remediation is
  ~4 commits + the 8-file bundle in `01-hermes-wsl-drvfs-git-performance/`. Not lost.
- **The "separations" work is on a BRANCH, not `main`:** `codex/separate-community-stack` — key commit
  `2026-09-22 feat(ki-basis): separate community stack to standalone repo and relocate meta workflows`, plus a
  Sep 18–22 agent-contract/integrity-recovery series. Branch header commit `2026-09-28 docs: mark branch
  SUPERSEDED — point to consolidated truth (do not merge)`. Surviving outcome = the standalone `lika-community`
  repo; the branch's *approach* was superseded by the WSL2 consolidation. Read via `git log codex/separate-community-stack`.
- **Out-of-git terminal history:** root `~/.bash_history` in WSL is empty/absent → the manual Docker Desktop
  build + live cutover commands are NOT recoverable there. Untried: other WSL users, Windows PowerShell
  `ConsoleHost_history.txt`.
- **27-Jun "Docker-Fließband" PDF:** time-windowed host search (20 Jun–05 Jul, all of `C:\Users\gehma`) found
  no matching PDF → confirmed **not on this machine**. Recover from chat/cloud only.
