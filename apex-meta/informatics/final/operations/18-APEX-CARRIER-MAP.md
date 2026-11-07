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
- **Five carriers hold an inline copy and equal the master:** Claude global, Gemini/Antigravity global, Codex global, the Leela vendored copy, and Mindful Bar's root `AGENTS.md`. Each differs only in the allowed `base_ref` (and, in Leela, one `ref`). All three global files use the absolute `base_ref`.
- **The three global files also share Layer 2 text** (QMD protocol, workstation, completion reporting, Windows defaults). Its owner is `specs/carrier-layer2-shared.md`; the tool compares and repairs it.
- **One tool compares everything:** `apex-meta/informatics/final/tools/apex_carrier_sync.py`. It reads the master from `main`, not from the checked-out branch.
- **Not a Leela document.** Leela keeps only its vendored copy (`docs/apex/`) and pointers. Anything about the contract, its carriers or its sync lives here.

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
| Claude global | `C:/Users/gehma/.claude/CLAUDE.md` | Yes (block and Layer 2) | absolute `base_ref` | `--sync` |
| Gemini/Antigravity global | `C:/Users/gehma/.gemini/GEMINI.md` | Yes (block and Layer 2) | absolute `base_ref` | `--sync` |
| Codex global | `C:/Users/gehma/.codex/AGENTS.md` | Yes (block and Layer 2) | absolute `base_ref` | `--sync` |
| Leela vendored copy | `C:/GitDev/Leela-Cloud-2026/docs/apex/apex-contract.md` | Yes | `base_ref="docs/apex/"`, `authoring` ref `specs/file-architecture.md` | `--sync`, then `check_vendor_drift.py --write` |
| Mindful Bar `AGENTS.md` | `C:/GitDev/mindful-bar/AGENTS.md` | Yes (uncommitted in that repo) | `base_ref="systems/apex/"`, `authoring` ref `specs/file-architecture.md` | `--sync` |
| Claude accounts `agehm`, `wimmer` | `C:/Users/gehma/.claude-agehm/CLAUDE.md`, `.claude-wimmer/CLAUDE.md` | **No file.** Launched through the PowerShell functions `claude-agehm` and `claude-wimmer`, which set `CLAUDE_CONFIG_DIR`. | n/a | `HANDOVER-10` |
| Codex accounts 1 and 2 | `C:/Users/gehma/.codex-acc1/AGENTS.md`, `.codex-acc2/AGENTS.md` | Folders do not exist; no `CODEX_HOME` set | n/a | `HANDOVER-10` |
| Antigravity second file | `C:/Users/gehma/.gemini/config/GEMINI.md` | Carries no block (OpenProject routing only) | n/a | `HANDOVER-10` |
| MausBot | `C:/Users/gehma/.openmausbot/bots/bb2f252e-4050-4dac-a7ad-3ca3161f55ce/SOUL.md` and its skills | Not a carrier: short core plus skills that read the master live. Deviates on `<align>`. | n/a | `HANDOVER-09`, `19-MAUSBOT-INSTALLATION-RECORD.md` |
| Modules | `C:/GitDev/Leela-Cloud-2026/docs/apex/specs/`, `C:/GitDev/mindful-bar/systems/apex/specs/` | In sync (`tools/check_vendor_drift.py`, vendored byte for byte into both; reads `main`; line-ending insensitive) | none | copy, then `check_vendor_drift.py --write` in that folder |

Hand-written text around the block (OpenProject routing, harness facts) is per carrier and never touched by the script.

## 3. Open gaps

| # | Gap | Evidence | Next step |
|---|---|---|---|
| G4 | The Claude accounts are launched with their own config dirs, and those dirs hold no `CLAUDE.md`. | PowerShell profile functions; `ls ~/.claude-agehm`. Whether Claude Code then also reads `~/.claude/CLAUDE.md` is not verified. | `HANDOVER-10`, probes P1 and P2, then the symlink fix. |
| G5 | Two Gemini files, one block. | `~/.gemini/GEMINI.md` has the block; `~/.gemini/config/GEMINI.md` does not. | `HANDOVER-10`, probe P3. |
| G8 | The JIT compliance hook covers `handover`, `trade_off` and (new) `authoring`. It has no trigger for `align`, `iterative`, `schemas`, `editing`. It lives in `Leela-Cloud-2026/scripts/`, wired for Claude only, and has no Codex or Gemini adapter. | `scripts/check_jit_gate_compliance.py`; tests in `scripts/tests/test_check_jit_gate_compliance.py`. | Decide whether the hook should move here, and whether Codex and Gemini need adapters. |
| G13 | Codex's Layer 2 still names Leela paths for OpenProject tooling. | `~/.codex/AGENTS.md`. | None. |
| G18 | MausBot's `<align>` rule is weaker than the master. | `19-MAUSBOT-INSTALLATION-RECORD.md`, section 3. | `HANDOVER-09`. |

Closed on 2026-11-07: G3 (Claude `base_ref` is absolute), G6 (monolith section 2 points at `qa-decision-matrix.md`), G9 (`<trade_off>` names the intensity lever), G10 (`qmd search "EM-06a"` finds the rule), G14 (shared Layer 2 text has one owner and a check), G15 (the meta checkout contains the archive), G16 (templates name the master), G17 (the two style-audit files moved to `research/07-ultra-style-audit/`), and the line-ending fragility of the drift check. Earlier: G1, G2, G7, G11, G12.

## 4. Changing a rule, step by step

1. Edit the master XML (and the module file, if the rule has a ref) in `apexai-os-meta`. For shared workstation text, edit `specs/carrier-layer2-shared.md` instead.
2. Commit it to `main` and push. The script compares against `main`.
3. Run `python apex-meta/informatics/final/tools/apex_carrier_sync.py` and read the output. `--source worktree` previews an uncommitted change.
4. Run it with `--sync` to rewrite each drifted carrier. It replaces only the block and the shared Layer 2 sections, and keeps a `.apex-sync.bak` next to each file.
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
- **Not verified:** which Gemini file Antigravity reads; whether a `claude-agehm` session also loads `~/.claude/CLAUDE.md`; the script has no automated tests.

## 7. Links

- Master modules: `C:/GitDev/apexai-os-meta/apex-meta/informatics/final/specs/execution-modes/`
- Multi-environment runbook: `operations/12-MULTI-ENVIRONMENT-INTEGRATION-HANDOVERS.md`
- Closeout and enforcement arc: `operations/16-PROJECT-CLOSEOUT-ADHERENCE-AND-DETERMINISTIC-ENFORCEMENT.md`
- MausBot record: `operations/19-MAUSBOT-INSTALLATION-RECORD.md`. Handovers: `operations/handovers/HANDOVER-09-MAUSBOT-ALIGNMENT-WITH-MASTER.md`, `HANDOVER-10-ACCOUNTS-AND-ANTIGRAVITY-PROBES.md`. Shared Layer 2: `specs/carrier-layer2-shared.md`.
- Archived 22-rule candidate: `candidates/_archive/16-candidate-3A-ultra.md` and its `README.md`
- Q&A matrix and intensity lever: `specs/execution-modes/qa-decision-matrix.md`
- Codex overwrite on 2026-11-04 (MausBot installation) and rollback copy: `C:/Users/gehma/.openmausbot/task-workspaces/bb2f252e-4050-4dac-a7ad-3ca3161f55ce/765bdb86-c44d-46d9-9450-3d4938909e34/` (`apex-installation-report.md`, `codex-AGENTS.before-routing-2026-11-04.md`)
- Leela side: `C:/GitDev/Leela-Cloud-2026/docs/apex/README.md`, `apex-contract.md`, `check_vendor_drift.py`, `MANIFEST.sha256`
- Global files: `C:/Users/gehma/.claude/CLAUDE.md`, `C:/Users/gehma/.gemini/GEMINI.md`, `C:/Users/gehma/.gemini/config/GEMINI.md`, `C:/Users/gehma/.codex/AGENTS.md`
