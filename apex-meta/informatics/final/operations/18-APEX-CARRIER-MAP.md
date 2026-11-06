---
type: Reference
id: OPS-18-APEX-CARRIER-MAP
title: Apex Carrier Map
description: Which files carry the Apex always-on block, which of them match the master today and why, and how to change or repair each one.
status: current
tags: [apex, carriers, sync, always-on, gaps]
---

# Apex Carrier Map

## At a glance

- **Master:** `specs/apex_contract_v1.0_ultra.xml` on branch `main` of `leela-spec/apexai-os-meta`. 23 rules. Local copy: `C:/GitDev/apexai-os-meta/apex-meta/informatics/final/specs/apex_contract_v1.0_ultra.xml`.
- **Four carriers hold an inline copy, and all four equal the master:** Claude global, Gemini/Antigravity global, Codex global, and the Leela vendored copy. Each differs only in the allowed `base_ref` (and, in Leela, one `ref`).
- **One tool compares them:** `apex-meta/informatics/final/tools/apex_carrier_sync.py`. It reads the master from `main`, not from the checked-out branch.
- **Not a Leela document.** Leela keeps only its vendored copy (`docs/apex/`) and a pointer to this map. Anything about the contract, its carriers or its sync lives here.

## 1. Where things are

```text
MASTER  apexai-os-meta  specs/apex_contract_v1.0_ultra.xml   (branch main)
   | inline copy, same 23 rules (only base_ref / one ref differ, see table)
   |- ~/.claude/CLAUDE.md                      Claude global
   |- ~/.gemini/GEMINI.md                      Gemini / Antigravity global
   |- ~/.codex/AGENTS.md                       Codex global
   |- Leela-Cloud-2026/docs/apex/apex-contract.md   vendored copy (repo-relative base_ref)

MODULES (the files the gated refs open)
   apexai-os-meta .../specs/execution-modes/*.md --copy + MANIFEST.sha256--> Leela docs/apex/specs/execution-modes/*.md
   checked by Leela docs/apex/check_vendor_drift.py (fast gate, runs when docs/apex/ changes)
```

## 2. Carrier table

| Carrier | Path | Up to date? | Allowed departure | Repair |
|---|---|---|---|---|
| Claude global | `C:/Users/gehma/.claude/CLAUDE.md` | Yes | relative `base_ref` (open, see G3) | `--sync` |
| Gemini/Antigravity global | `C:/Users/gehma/.gemini/GEMINI.md` | Yes | absolute `base_ref` | `--sync` |
| Codex global | `C:/Users/gehma/.codex/AGENTS.md` | Yes | absolute `base_ref` | `--sync` |
| Leela vendored copy | `C:/GitDev/Leela-Cloud-2026/docs/apex/apex-contract.md` | Yes | `base_ref="docs/apex/"`, `authoring` ref `specs/file-architecture.md` | `--sync`, then `check_vendor_drift.py --write` |
| Claude accounts `agehm`, `wimmer` | `C:/Users/gehma/.claude-agehm/CLAUDE.md`, `.claude-wimmer/CLAUDE.md` | File does not exist | n/a | G4 |
| Codex accounts 1 and 2 | `C:/Users/gehma/.codex-acc1/AGENTS.md`, `.codex-acc2/AGENTS.md` | Folders do not exist | n/a | G4 |
| Antigravity second file | `C:/Users/gehma/.gemini/config/GEMINI.md` | Carries no block (OpenProject routing only) | n/a | G5 |
| Modules | `C:/GitDev/Leela-Cloud-2026/docs/apex/specs/execution-modes/` | In sync (`check_vendor_drift.py`: "in sync") | none | copy, then `check_vendor_drift.py --write` |

Hand-written text around the block (Layer 2: OpenProject routing, QMD, "Completion Reporting") is per carrier and never touched by the script.

## 3. Open gaps

| # | Gap | Evidence | Why it matters | Next step |
|---|---|---|---|---|
| G3 | Claude global uses a relative `base_ref`. | `~/.claude/CLAUDE.md` has `base_ref="apex-meta/informatics/final/"`. The script warns that 7 refs do not resolve outside the meta repo. Finding: `operations/17-READ-TRACE-PILOT-AND-BASE-REF-FRAGILITY-FINDINGS.md`. | In every other repo the 7 gated refs name files the agent has to guess. | Set an absolute `base_ref` for Claude in the script's `CARRIERS`, then `--sync`. Needs the operator's yes. |
| G4 | Account folders carry nothing. | `.claude-agehm` and `.claude-wimmer` hold only `backups` and `daemon`; `.codex-acc1` and `.codex-acc2` do not exist. | A launch that selects those config dirs gets no block. Whether any launch does is not knowable from files. | Operator names the accounts that are really launched. Entries already exist (optional). |
| G5 | Two Gemini files, one block. | `~/.gemini/GEMINI.md` has the block; `~/.gemini/config/GEMINI.md` does not. | If Antigravity reads the second, it gets no block. | Test with Antigravity, or read its docs. |
| G6 | Monolith `specs/execution-modes.md` §2 still holds an older Q&A matrix without `EM-06a`. | `.claude/rules/informatics.md` in this repo names the monolith as a module. | Agents in this repo can read an older Adapter 1 than agents elsewhere. | Replace §2 with a pointer, as commit `a6792617` did for other adapters. |
| G8 | The JIT compliance hook covers 2 of 9 gates (`handover`, `trade_off`), by keyword in the latest prompt. | `Leela-Cloud-2026/scripts/check_jit_gate_compliance.py:21-27`. | `align`, `iterative`, `authoring` gates are not checked, and the keyword match fires on file names. | Separate task with a per-gate adherence test. |
| G9 | `<trade_off>` has no pointer to the Q&A matrix. | `<trade_off ref=...bake-off.md>` in all carriers; the lever lives in `qa-decision-matrix.md`. | An agent that reads only the always-on block never finds `EM-06a`. | Add a clause or retarget the `ref` in the master, then `--sync`. |
| G10 | QMD does not index the new rule. | `qmd search "Intensity Lever" -c apex-informatics-final` returned nothing before this change. | `qmd search` is the standing first step. | Re-index the collection after this commit reaches the checked-out tree. |
| G13 | Codex depends on the state of the Leela checkout only for its vendored fallback. | The inline block no longer does; Layer 2 of `~/.codex/AGENTS.md` still names Leela paths. | Low. | None. |
| G14 | Layer 2 text is duplicated by hand across carriers. | The two "Completion Reporting" bullets added on 2026-11-06 exist in all three globals only because they were pasted. | They can drift apart with no check. | Extend the script to compare named Layer 2 sections, if it proves necessary. |
| G15 | This checkout is on a feature branch and does not yet contain the archive of candidate 16. | `git -C C:/GitDev/apexai-os-meta branch --show-current`. | The files here show the old layout until `main` is merged in. | Merge `main` into the working branch. |
| G16 | Three untracked handovers still name candidate 16. | `operations/handovers/HANDOVER-02`, `-03`, `-05` (untracked in this repo). | They are templates for carrier text. | Update them when they are committed. |
| G17 | Three Apex research files sit in the Leela repo. | `Leela-Cloud-2026/docs/ssot/architecture/spec-organization/`: `ultra-style-audit-findings.md` (untracked), `research-handover-ultra-style-audit.md`, `prior-research-and-rule-proposal.md`. | Apex material in a Leela folder. | Operator decides whether to move them here. |

Gap numbers are not a ranking. G1, G2, G7, G11, G12 are closed (see `log.md`, 2026-11-06).

## 4. Changing a rule, step by step

1. Edit the master XML (and the module file, if the rule has a ref) in `apexai-os-meta`.
2. Commit it to `main` and push. The script compares against `main`.
3. Run `python apex-meta/informatics/final/tools/apex_carrier_sync.py` and read the output. `--source worktree` previews an uncommitted change.
4. Run it with `--sync` to rewrite each drifted carrier. It replaces only the block and keeps a `.apex-sync.bak` next to each file.
5. Copy changed module files to `C:/GitDev/Leela-Cloud-2026/docs/apex/specs/`, then run `python docs/apex/check_vendor_drift.py --write` there.
6. In Leela, run `python scripts/gates.py --since origin/master`, then commit and push.
7. Add one entry to `operations/log.md`.

## 5. How the sync could run continuously

| Option | Mechanism | I/E/R | Verdict |
|---|---|---|---|
| A. Manual | Run the script (today). | I40/E85/R60 | Misses drift for days. |
| B. Session-start advisory | Add the check to the existing Leela hook `Leela-Cloud-2026/.claude/hooks/session-start-git-status.py`; print only on drift. | I80/E70/R20 | **Recommended.** Cheap, read-only. |
| C. Scheduled task | A scheduled task runs the script and writes a note. | I60/E50/R35 | Later, if B is not enough. |
| D. Gate | Add to `scripts/gates.py`. | I30/E60/R70 | Rejected: it reads files outside the repo, so a clean clone is red. |

`--sync` stays an explicit act. Rewriting global instruction files without anyone looking is a risk not worth taking.

## 6. Verification

- **Check:** `python apex-meta/informatics/final/tools/apex_carrier_sync.py`. Expected: `OK` for the four carriers, `ABSENT` for the optional ones.
- **Sabotage test (2026-11-06):** changing "Do only authorized work" to "Do any work" in a copy of the Claude global made the script report `<scope> body differs`; `--sync` repaired it; the next check reported identical.
- **Invalidation:** a carrier edited by hand inside the block that still reports `OK` means the comparison is broken.
- **Not verified:** which Gemini file Antigravity reads; whether any launch selects the account folders; the script has no automated tests.

## 7. Links

- Master modules: `C:/GitDev/apexai-os-meta/apex-meta/informatics/final/specs/execution-modes/`
- Multi-environment runbook: `operations/12-MULTI-ENVIRONMENT-INTEGRATION-HANDOVERS.md`
- Closeout and enforcement arc: `operations/16-PROJECT-CLOSEOUT-ADHERENCE-AND-DETERMINISTIC-ENFORCEMENT.md`
- Archived 22-rule candidate: `candidates/_archive/16-candidate-3A-ultra.md` and its `README.md`
- Q&A matrix and intensity lever: `specs/execution-modes/qa-decision-matrix.md`
- Codex overwrite on 2026-11-04 (MausBot installation) and rollback copy: `C:/Users/gehma/.openmausbot/task-workspaces/bb2f252e-4050-4dac-a7ad-3ca3161f55ce/765bdb86-c44d-46d9-9450-3d4938909e34/` (`apex-installation-report.md`, `codex-AGENTS.before-routing-2026-11-04.md`)
- Leela side: `C:/GitDev/Leela-Cloud-2026/docs/apex/README.md`, `apex-contract.md`, `check_vendor_drift.py`, `MANIFEST.sha256`
- Global files: `C:/Users/gehma/.claude/CLAUDE.md`, `C:/Users/gehma/.gemini/GEMINI.md`, `C:/Users/gehma/.gemini/config/GEMINI.md`, `C:/Users/gehma/.codex/AGENTS.md`
