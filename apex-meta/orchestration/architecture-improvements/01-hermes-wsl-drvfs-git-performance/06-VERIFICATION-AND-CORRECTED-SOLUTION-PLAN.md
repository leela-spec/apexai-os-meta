# 06 — Independent Verification & Corrected Solution Plan

**Module ID:** `ARCH-IMP-06-VERIFICATION-AND-CORRECTED-PLAN`
**Parent Package:** `01-hermes-wsl-drvfs-git-performance`
**Date:** 2026-08-25
**Role:** Independent detective review of modules 00–05, verified against the live repository.

---

## 0. Read this first (plain language)

You asked whether this analysis is sane, simple, effective, and efficient — and you said you can't
tell. That is a fair worry, so this section is written so **you do not have to trust anyone**. Every
important number below can be checked by copy-pasting one command and comparing the result. If the
numbers match, the analysis is grounded in fact. If they don't, something is wrong and you should
stop.

### What actually went wrong, in one paragraph

The Hermes agent tried to save a file to Git. A normal save takes under a second. This one took
**two minutes just to check status**, then **froze for five more minutes** and could not be stopped.
The report blames the right *core reason* (the agent was working on files that physically live on the
Windows side of the machine, and reaching them from the Linux side is like phoning a librarian in
another building to fetch every book one at a time — with 53,000 files, that's 53,000 phone calls).
**That core diagnosis is correct.** But the report *also* tells a second story — that recent
"simulation" files bloated the project — and **that second story is wrong**. The bloat is real, but it
comes from something else entirely: 80% of the project is copies of other people's downloaded code.

### Is the fix safe and simple?

Yes. The real fix is not risky surgery. It is: **make the agent work on the fast (Linux-native)
copy of the files instead of the slow (Windows) copy.** Everything else is a safety net. Nothing in
this plan deletes your work or changes what your project *does* — it changes *where the agent stands
while it works*.

---

## 1. Verify me yourself (run these; compare the numbers)

Open the project folder and run each command. The "Expected" column is what my analysis is based on.

| # | Command (PowerShell, run in the project folder) | Expected result | What it proves |
|---|---|---|---|
| 1 | `git ls-files \| Measure-Object -Line` | ~**53,872** | Repo really is huge (report said 53,866 ✅) |
| 2 | `git ls-files -- source-knowledge \| Measure-Object -Line` | ~**43,008** | 80% of everything lives here — the *real* bloat |
| 3 | `git ls-files -- apex-meta/orchestration/simulation \| Measure-Object -Line` | ~**485** | The files the report blamed are <1% — a red herring |
| 4 | `git ls-files -- "source-knowledge/ProjectRepos/crewAI-main" \| Measure-Object -Line` | ~**18,035** | A single downloaded outside project = 1/3 of the repo |
| 5 | `git ls-files -- "source-knowledge/ProjectRepos/antigravity-awesome-skills-main" \| Measure-Object -Line` | ~**17,250** | A second downloaded project = another 1/3 |

If #2 and #3 come back roughly as shown, my correction is proven: **the scale problem is real, but the
original report pointed at the wrong pile of files.**

---

## 2. Verdict table (what holds, what doesn't)

| # | Claim in modules 00–05 | Status | Evidence |
|---|---|---|---|
| 1 | Repo has ~53,866 tracked files | ✅ TRUE | Live count: 53,872 |
| 2 | Root cause = Linux Git over the Windows filesystem bridge (9P/DrvFs) | ✅ SOUND | Matches documented WSL2 behavior and the symptoms |
| 3 | Frozen process can't be killed (`D`/uninterruptible state) | ✅ TRUE | Correct kernel behavior |
| 4 | A path filter (`-- artifacts/…`) does NOT stop the slowdown | ✅ TRUE | Correct and non-obvious |
| 5 | Commit `414e4170` added 401 files | ✅ TRUE | Exactly 401 |
| 6 | Commit `db55b79d` added 88 files | ❌ WRONG | Actually **412** |
| 7 | Commit `81ec2730` added 124 files | ❌ WRONG | Actually **80** |
| 8 | Per-subtree file breakdown (module 03 §1) | ❌ MOSTLY WRONG | See §3 |
| 9 | "Simulation logs caused the bloat" | ❌ MISDIAGNOSIS | Simulation = 485 files = 0.9% |
| 10 | Benchmark table (296×, 602×, 720× slower) | ⚠️ UNVERIFIED | Presented as measured; actually illustrative |
| 11 | The failing session ran over the Windows bridge (9P) | ✅ CONFIRMED (2026-08-25) | Proven: Hermes commit `654d1fcc` landed in the `/mnt/c` clone; live probe shows `/mnt/c` = 9p and the config mounts the launch cwd; measured `git status` = 6m11s on `/mnt/c` vs 0.557s on ext4 |

**Bottom line:** the *root cause and the primary fix are correct*. The *scale narrative and several
counts are wrong* and must be corrected before anyone acts on module 04's Proposal 4.

---

## 3. The one big error: wrong pile of files

Module 03 blames recent simulation commits. The live repository disagrees:

| Subtree | Report claimed | Actual | Off by |
|---|---|---|---|
| `ApexDefinition&OldVersions/` | ~18,200 | **590** | 30× too high |
| `source-knowledge/ProjectRepos/` | ~14,350 | **42,773** | 3× too low |
| `apex-meta/kb/` | ~12,100 | **5,691** | 2× too high |
| `artifacts/` | ~4,850 | **1,137** | 4× too high |
| `apex-meta/orchestration/simulation/` | ~1,250 | **485** | 2.5× too high |

**The true driver:** `source-knowledge/` = 43,008 files = **79.8% of the repo**. Two downloaded
third-party projects dominate: `crewAI-main` (18,035) + `antigravity-awesome-skills-main` (17,250) =
**65% of everything**. The simulation logs the report told you to clean up are a **0.9% rounding
error**.

---

## 4. Two cautions before acting

1. **The "which mount" claim — now CONFIRMED (2026-08-25).** Originally an inference; since proven by
   direct probe: `/mnt/c` is a `9p` mount, the Hermes config mounts the launch cwd into `/workspace`
   (`docker_mount_cwd_to_workspace: true`), Hermes commit `654d1fcc` was found in the `/mnt/c` clone,
   and `git status` measured 6m11s on `/mnt/c` vs 0.557s on ext4. Root cause and remedy are settled.
2. **The benchmark numbers are synthetic.** They are the right order of magnitude but were not
   measured on this machine. If they justify any decision, replace them with one real timing:
   `time git status` on the fast (ext4) copy vs. the slow (`/mnt/c`) copy of this repo.

---

## 5. Corrected solution plan (prioritized)

Ordered by leverage. Tier 0 alone resolves the incident; everything below is defense-in-depth.

### Tier 0 — Stop it from happening again (the actual cure)
1. **Make the agent work on the fast copy.** Enforce that Linux agents run in the native Linux
   workspace (`/root/workspaces/<repo>`), never on `/mnt/c/...`. Add a launch-time guard: if the
   working path starts with `/mnt/`, refuse to run (or auto-redirect to Windows-native `git.exe`).
   *This makes the file count irrelevant — status returns in well under a second even at 53k files.*
2. **Scope the Git commands** the agent issues, added to `AGENTS.md`.
   - Important mechanical note: `CLAUDE.md`, `GEMINI.md`, and `.hermes.md` are all **symbolic links to
     `AGENTS.md`** — so editing `AGENTS.md` updates the instructions for *every* agent at once.
   - The new rules must be **merged into the existing `## Git Dispatch` section**, not pasted as a
     duplicate.

### Tier 1 — Fix the real bloat (the true 80%)
3. **Decide what to do with the downloaded outside projects** in `source-knowledge/ProjectRepos/`
   (35,000+ files). Options, simplest first:
   - stop tracking them in Git and keep a short list of what they are (recommended if they're just
     reference copies), or
   - convert them to Git "submodules" (links to the originals instead of full copies), or
   - leave them but exclude them from the agent's fast working copy.
   *Your own project rules already say "never write into `source-knowledge/`", which suggests it's a
   staging area that doesn't need to be fully version-controlled.*
4. **Keep the simulation-log ignore rules** from module 04 — they're harmless and correct — but
   **re-label them as minor cleanup, not the scale fix.**

### Tier 2 — Safety nets (keep as-is from modules 04–05)
5. The Windows `git.exe` fallback shim — good for occasional manual sessions.
6. The incident recovery runbook (module 05 §2) — sound; keep the "check for the frozen state before
   trying to kill it" and "kill it from the Windows side" steps.

### Correct the record
7. Fix the two commit counts and the subtree table in modules 00 and 03, and re-anchor the scale
   story on `source-knowledge` vendor clones. (Do this via the repo's exact-match patch process with
   operator approval — not a silent rewrite.)

---

## 5a. The fix must be two-sided — and you do not "repair" the bridge

The bridge (WSL2's 9P/DrvFs layer between Windows and Linux) is **not broken**. It works as designed.
Crossing the OS boundary is *inherently* slow — this is documented Microsoft behavior, not a defect.
You cannot make it fast; you avoid routing heavy Git work through it.

The two required sides:

| Side | What it is | What it achieves | Alone? |
| :--- | :--- | :--- | :--- |
| **A. Location (the cure)** | Agents run on native ext4 (`/root/workspaces/`), never across `/mnt/c/` | Eliminates the failure; Git is instant even at 53k files | Cures this incident, but one future mis-launch on `/mnt/c` reproduces it at full severity |
| **B. Reduction + hard guardrail (the safety net)** | Shrink the repo (untrack the 35k vendor files) **and** add an automatic check that refuses to run on `/mnt/c` | Makes even a mistake survivable; speeds all Git work | 18k files across the bridge is still ~30–40s — better, not safe |

**Neither side alone is acceptable. The acceptable end-state is A + B together**, so that no single
human error can cause an outage (defense in depth).

---

## 5b. Root cause of the PROCESS gap — the rule existed; enforcement did not

The question "how did our architecture research miss such an important failure?" has a precise,
evidence-backed answer: **it was not missed in design. It was missed in enforcement.**

The architecture showcase already states the rule, verbatim (line 264 of
`apex-meta/orchestration/docs/HERMES_MULTI_REPO_ORCHESTRATION_V2_ARCHITECTURE_SHOWCASE.md`):

> "Work in Native ext4 (`/root/workspaces/`)... **Never run heavy agent tools directly across
> `/mnt/c/`.**"

Yet a real control was absent in all three places one would live:

1. **Operating instructions (`AGENTS.md`)** — the file agents actually load — contain **zero**
   filesystem rules. Its only "guardrails" line reads *"Do not invent extra guardrails."*
2. **Runtime** — **no** check refuses to start when the working path is under `/mnt/`.
3. **Tests / CI** — **nothing** would catch a wrong-filesystem launch.

Corroborating drift: this working copy lives at `C:\GitDev\apexai-os-meta` (the slow `/mnt/c/` side),
while the architecture claims migration to `/root/workspaces/` was complete. **The document said
"done"; the runtime reality diverged.**

**Lesson (the durable takeaway):** *A rule that lives only as prose in a design document the runtime
never reads is not a control — it is a wish.* The system had the correct knowledge and no mechanism
to enforce it. Closing the process gap therefore means converting that one sentence into (a) a rule
in `AGENTS.md`, and (b) an automatic launch-time guard, plus (c) one preflight/test that fails loudly
on the wrong filesystem.

---

## 6. What I did NOT do (so you know the limits)

- I did **not** edit modules 00–05. Correcting them requires the operator-approved patch process.
- I did **not** change any configuration, `AGENTS.md`, or `.gitignore`. This module is analysis only.
- I could **not** directly observe the original Hermes session's mount point (that session is gone);
  claim #11 is a strong inference, flagged as such.

---

## 7. Suggested next decision for the operator

The acceptable *target* is both sides (§5a): location cure **plus** reduction and a hard guardrail.
These options are ordered as safe, reversible steps toward that target — not as either/or substitutes.

- **A. Stop the pain now** → Tier 0 (agents use the fast ext4 copy + scoped Git). Resolves the
  incident. Safe and reversible. *Necessary but not sufficient on its own.*
- **B. Add the safety net** → Tier 1 (untrack the ~35k vendor files, keep them on disk) **plus** the
  hard guardrail from §5b (a launch check that refuses `/mnt/c`). This is what makes the fix
  two-sided and a single mistake non-fatal.
- **C. Full closure** → Tiers 0–2 + write the filesystem rule into `AGENTS.md` + correct modules
  00/03 so the record matches reality.

Recommended path: do **A immediately**, then **B** to reach the acceptable end-state, then **C** to
close the record. A alone stops today's pain; A + B is the minimum that is actually *safe*.
