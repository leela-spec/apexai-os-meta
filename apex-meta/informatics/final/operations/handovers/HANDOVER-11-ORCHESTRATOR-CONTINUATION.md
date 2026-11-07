---
type: Handover
id: HANDOVER-11-ORCHESTRATOR-CONTINUATION
title: Handover 11 — Orchestrate the Remaining Apex Carrier Work
description: Contract for a new chat to become the orchestrator of the open Apex carrier, MausBot and enforcement tasks, with the task ledger, the decisions already made, the traps found, and links to every source and chat session instead of copies.
status: current
tags: [handover, orchestrator, ledger, carriers, mausbot, enforcement]
---

# Handover 11 — Orchestrate the Remaining Apex Carrier Work

Written 2026-11-07 at the end of the chat `e648bd63`. State at writing: meta repo `main` = `1170db14` plus the commit that adds this file; Leela `master` = `479d985b` or later.

## Role

You orchestrate. You sequence the ledger below, delegate each task to the sub-handover or subagent named, check what comes back yourself, ask the operator for decisions in one batch, and keep the ledger current. You do not redo finished work and you do not recreate the reasoning: read the linked sources.

## Input and priority ledger

Read in this order, and open only what the active task needs.

1. **Task ledger** (section below). Authoritative for what is open.
2. `C:/GitDev/apexai-os-meta/apex-meta/informatics/final/operations/20-CHANGE-RECORD-2026-11-06-07.md`: every change with before, problem, solution, after, and the mistakes found. Read C1-C16 and F.
3. `…/operations/18-APEX-CARRIER-MAP.md`: carrier table, open gaps, change runbook.
4. `…/operations/19-MAUSBOT-INSTALLATION-RECORD.md`: what MausBot did and why.
5. `…/operations/handovers/HANDOVER-09-MAUSBOT-ALIGNMENT-WITH-MASTER.md` and `HANDOVER-10-ACCOUNTS-AND-ANTIGRAVITY-PROBES.md`: ready-to-run delegations.
6. `…/specs/apex_contract_v1.0_ultra.xml` (the master), `…/specs/carrier-layer2-shared.md`, `…/tools/apex_carrier_sync.py`.
7. Leela side: `C:/GitDev/Leela-Cloud-2026/docs/apex/README.md` (what the vendored layer and the drift gate do), `scripts/check_jit_gate_compliance.py` and `scripts/tests/test_check_jit_gate_compliance.py` (the hook), `docs/ssot/architecture/AGENT-INSTRUCTION-LAYERS-2026-10-27.md` (the operator's 2026-11-05 deferral of the hook).
8. Memory: `C:/Users/gehma/.claude/projects/C--GitDev-Leela-Cloud-2026/memory/MEMORY.md`, entry `feedback_apex_material_lives_in_apex_repo.md`.
- **Ignore:** the 16 historical copies of the old block (candidates `06`, `07`, `09`, `13`-`15`, handover templates `01`-`05`, `11`); `*.apex-sync.bak` files; the `ki-basis` material.

### Chat sessions and logs (read for reasoning; do not copy)

Claude Code transcripts in `C:/Users/gehma/.claude/projects/C--GitDev-Leela-Cloud-2026/`:

| File | What it holds |
|---|---|
| `e648bd63-0772-4b21-8852-0ec3afd204f4.jsonl` | **This chat.** Style audit, intensity lever, carrier sync, Codex restore, G3/G6/G9/G14, the MausBot findings, the operator's corrections (Apex material belongs in the Apex repo). The operator's decisions are in the user turns. |
| `a293673b-52b0-43a6-8583-306184027502.jsonl` | 2026-11-06. Ran `HANDOVER-07-PRE-ROLLOUT-ADHERENCE-TEST`. Evidence on whether agents follow the gated refs. |
| `fead0e68-9b2f-4760-bea1-39b411d28e38.jsonl` | 2026-11-06. Parallel Leela session (SSOT purpose block). Its commit `f74ca739` swept my staged deletions; see traps. |
| `f41f0ea4-ede8-4c92-a5dc-e4723de34ee8.jsonl` | 2026-11-03. Executed `HANDOVER-2026-10-28-INSTRUCTION-LAYER-SYSTEM`; origin of the three-layer system. |
| `5cfc414d-5e07-4c16-9902-bf1ec7b0efdb.jsonl` | 2026-11-04. Meta-repo work from the adherence test results (`operations/14-ADHERENCE-TEST-RESULTS.md`). |
| `061d6839-c650-4005-9d89-ebcf4e8f7032.jsonl` | 2026-11-04. A continuation ("Confirmed, go") of that work. |
| `64877cf1-7b0d-4108-96d2-77815b8a8cd2.jsonl` | 2026-11-04. Validated `tools/check_decision_bakeoff_shape.py` against two real decisions. |

MausBot (`C:/Users/gehma/.openmausbot/`): `workspaces/bb2f252e-4050-4dac-a7ad-3ca3161f55ce/memory/log/2026-11-04.md` (its own log), `events/765bdb86-c44d-46d9-9450-3d4938909e34.ndjson` and `native/765bdb86-…ndjson` (the instruction-migration conversation), `events/191b52a9-f933-4255-8afb-de7b60f61461.ndjson` (spawn test), `task-workspaces/bb2f252e-…/765bdb86-…/` (installation report, rollback copies, `modular-instructions/`).

## Decisions already made by the operator (do not reopen)

| Decision | Source |
|---|---|
| Codex carries the full block again, synced like Claude and Gemini. | chat `e648bd63`, 2026-11-06 |
| Anything that is not Leela lives in the Apex repo, never in Leela documents or `STATE.md`. | same chat, 2026-11-06; memory entry |
| The carrier map and sync tool are Apex material and stay in the meta repo. | same chat, 2026-11-07 |
| Commit contract changes to the meta repo `main` and push. | same chat |
| Candidate 16 is archived; the master XML is the only live source. | same chat |
| The signal-bullet rewrites of the ultra block add tokens for scannability only and are not wanted. | same chat, first turns |

## Process

1. **Ground first.** Run the verification commands below and compare with this file. Trust the files, not this text.
2. **Set up a working copy outside the dirty checkout.** `C:/GitDev/apexai-os-meta` is on branch `codex/ki-basis-amd64-features` with other sessions' uncommitted work: do not edit or reset it. Use a short path (the 260-character limit breaks the verification suites and the OKF validator):
   ```bash
   git clone https://github.com/leela-spec/apexai-os-meta.git C:/tmp/meta-work
   git -C C:/tmp/meta-work config user.name AlexOG
   git -C C:/tmp/meta-work config user.email gehmalexander@gmail.com
   ```
3. **Order:** T1 first (it makes the real-path tool current), then the checkable tasks (T6, T7, T13), then the delegations (T2-T4), then the decisions (T5, T8-T12) as one batch to the operator, each with its depth level per `qa-decision-matrix.md` §2.3.
4. **Delegate.** Run `HANDOVER-09` and `-10` as written. Subagents of type `Explore` and `Plan` receive no repository instructions: restate the constraints below inside their prompts.
5. **Write changes the way the change record does:** before, problem, solution, after, with a commit hash. Edit research files surgically (an update block, not a rewrite).
- **Boundaries:** never write a handover for work you can check now. Edit existing files with exact-match patches. Commit with explicit paths (`git commit -- <paths>`), never `git add -A`: Leela's git index is shared between parallel sessions. Push meta with `git push https://github.com/leela-spec/apexai-os-meta.git HEAD:main` after `git fetch` of that URL and a rebase. Never force-push, never commit credentials (the account folders hold `.credentials.json`: do not open it).

## Task ledger

Status values: `open`, `needs operator`, `ready to delegate`. Update the status column in place and add a dated line to `operations/log.md` per batch.

| # | Task | Status | Next step | Source |
|---|---|---|---|---|
| T1 | Merge `main` into `codex/ki-basis-amd64-features` so the real-path tool and files are current. | needs operator (asked, no answer yet) | After a yes: inspect `git status`, then `git -C C:/GitDev/apexai-os-meta merge main`. Until then the real-path `tools/apex_carrier_sync.py` is the old version and reports Claude as drifted. | change record C9 |
| T2 | G4: Claude accounts `claude-agehm`, `claude-wimmer` are launched with config dirs that hold no `CLAUDE.md`. | ready to delegate; needs operator approval for the symlinks | Run probes P1, P2 of `HANDOVER-10`, then the symlink fix. | `HANDOVER-10`, map G4 |
| T3 | G5: which Gemini file does Antigravity read? | ready to delegate | Probe P3 in Antigravity. | `HANDOVER-10`, map G5 |
| T4 | MausBot: list deviations of its apex skills from the master (notably `<align>`), propose exact patches. Operator picks option A, B or C (recommended: C). | needs operator for the option; the handover itself can run | Run `HANDOVER-09` in a MausBot conversation. | record 19 section 4 |
| T5 | G8: hook ownership (Leela or here), Codex and Gemini adapters, gates with no trigger (`align`, `iterative`, `schemas`, `editing`). | needs operator | Decision sheet at level L2. Context: the operator deferred this on 2026-11-05; the hook was changed on 2026-11-07 (C13). | map G8 |
| T6 | About 20 verification tests in the meta repo fail at baseline (stale after the monolith split). | open, checkable | List with `python -m pytest -q apex-meta/informatics/final/verification/suites` in the short-path clone; fix, or archive with a README. | change record M12 |
| T7 | The OKF validator is unmeasured (crashed on long paths). | open, checkable | Run `python apex-meta/informatics/final/tools/okf_validator.py --target apex-meta/informatics/final` in the short-path clone at `5a316e6b` and at `main`; compare error counts. | change record G |
| T8 | The Layered Rule KB is a 22-rule snapshot that lags the master; `<align>` has no semantic block audit; "already defined by a previous step" is undefined. | needs operator | Decide: refresh rules 1-22 to the master text, or declare the KB historical. Then audit `<align>`. | change record M6-M9, M11; `rule-23-align.md` |
| T9 | Old block text in handover templates `01`-`05`, `11` and candidates `06`, `07`, `09`, `13`-`15`. | needs operator | Replace with a pointer to the master and the sync tool, or keep as dated records. | change record M17 |
| T10 | `EM-06a` thresholds are unmeasured. | open | Calibrate against past decision sheets in `C:/GitDev/Leela-Cloud-2026/docs/ssot/decisions/DECISION-SHEET-*.md`. | change record C2 |
| T11 | Continuous drift detection (map section 5, option B: session-start advisory in Leela's `.claude/hooks/session-start-git-status.py`). | needs operator | Build only after T1; read-only, prints on drift. | map section 5 |
| T12 | Per-carrier Layer 2 sections (OpenProject routing, harness facts) are not compared. | open | Decide if the tool should check them. | change record C12 |
| T13 | Clean up backups: `~/.claude/CLAUDE.md.apex-sync.bak`, `~/.gemini/GEMINI.md.apex-sync.bak`, `~/.codex/AGENTS.md.apex-sync.bak`, `~/.codex/AGENTS.md.pre-restore-2026-11-06.bak`. | open, needs operator (deletes files) | Offer archive-or-delete; keep the pre-restore copy until T2-T4 are done. | change record C11 |
| T14 | QMD: new files are not in the real checkout until T1; `qmd embed` (1,445 hashes) not run. | open | After T1: `qmd update`, then `qmd search "carrier-layer2-shared" -c apex-informatics-final`. | map G10 |
| T15 | A second MausBot bot `c68d0dad-b3d0-4baf-8505-8f4eadbd7141` was not inspected. | open | Read its `SOUL.md`; report only. | record 19 section 5 |
| T16 | Two bullets carried over from MausBot sit under "Completion Reporting"; the first is about precedence. | open | Move to a fitting heading in `specs/carrier-layer2-shared.md`, then `--sync`. | change record C11 |
| T17 | Confirm `prior-research-and-rule-proposal.md` stays in Leela (accepted decision SSOT-D-068 depends on it). | needs operator | One question. | change record C14 |

## Output

- The ledger above, updated in place.
- One entry per batch in `operations/log.md` (newest first, same style).
- A final report appended below under `## Orchestrator report`, in the five components of `specs/execution-modes/handover.md` 5.2.

## Definition of done

- Every ledger row is closed with evidence, or deferred in the operator's words.
- `python apex-meta/informatics/final/tools/apex_carrier_sync.py` prints `OK` for the four carriers and the three Layer 2 checks, and "in sync" for modules.
- `python scripts/gates.py --full` passes in Leela when Leela was touched.
- The meta verification suites show no failure beyond the baseline list from T6.
- Independent check: a fresh chat answers three questions from its own instructions: its first always-on rule (`<target>`); when it must restate a task (the new `<align>` trigger); where `<trade_off>` points for depth (`qa-decision-matrix.md`, levels `L0`-`L3`). A script that only greps for strings does not count.

## Traps found

- **Shared git index (Leela).** A parallel session committed my staged deletions; I had to restore and re-delete. Stage and commit explicit paths.
- **Line endings.** The meta checkout converts to CRLF; the drift check now hashes content, but new files written by tools may be LF. Preserve each file's endings when editing.
- **260-character paths** break the verification suites and the OKF validator in deep scratch folders. Use `C:/tmp/meta-work`.
- **Pushing meta.** The clone's `origin` may be the local checkout, which is not GitHub. Use the GitHub URL explicitly, and `git fetch origin main:main` in the real checkout afterwards.
- **The Stop hook** checks only reads made after the latest user message: a keyword like "handover" in the operator's message requires reading `handover.md` again that turn, and an edit under `apex-meta/informatics/` requires reading `index.md`.
- **`--sync` rewrites the operator's global instruction files.** It keeps one `.apex-sync.bak` per file per run; never run it without saying which files will change.
- **MausBot's profile cannot be read back** from outside. Only MausBot can show what is installed.

## Verification commands (run before trusting this file)

```bash
git -C C:/GitDev/apexai-os-meta ls-remote https://github.com/leela-spec/apexai-os-meta.git main
python C:/tmp/meta-work/apex-meta/informatics/final/tools/apex_carrier_sync.py
python C:/GitDev/Leela-Cloud-2026/docs/apex/check_vendor_drift.py
git -C C:/GitDev/Leela-Cloud-2026 log --oneline -8 -- docs/apex scripts/check_jit_gate_compliance.py
```

## Orchestrator report

Not started.
