---
type: Handover
id: HANDOVER-10-ACCOUNTS-AND-ANTIGRAVITY-PROBES
title: Handover 10 — Account Folders and Antigravity File Probes (G4, G5)
description: What is already verified about the extra Claude and Codex account folders and the two Gemini files, and the probes and fixes that need a live authenticated session.
status: current
tags: [handover, carriers, claude-accounts, codex-accounts, antigravity, g4, g5]
---

# Handover 10 — Account Folders and Antigravity File Probes (G4, G5)

Why this is a handover: the open questions need a running, signed-in agent in each environment. Files cannot answer them. Everything else was checked first.

## Verified now (read from files, 2026-11-07)

- **G4, Claude accounts are launched with their own config dirs.** The PowerShell profile `C:/Users/gehma/OneDrive/Dokumente/WindowsPowerShell/Microsoft.PowerShell_profile.ps1` defines `claude-agehm` and `claude-wimmer`; each sets `CLAUDE_CONFIG_DIR` to `~/.claude-agehm` or `~/.claude-wimmer` (created by `C:/Users/gehma/bin/setup-claude-accounts.ps1`). Command: `Select-String -Path $PROFILE -Pattern claude-agehm -SimpleMatch`.
- **Those dirs hold no `CLAUDE.md`.** A session started with `claude-agehm` or `claude-wimmer` therefore gets no always-on block, no OpenProject routing and no QMD protocol. (Whether Claude Code also reads `~/.claude/CLAUDE.md` in that case is the first probe below.) The dirs hold `.credentials.json`; do not open it.
- **G4, Codex accounts do not exist.** `~/.codex-acc1` and `~/.codex-acc2` are absent and no `CODEX_HOME` is set at user scope. Handover 03 only planned them.
- **G5, two Gemini files.** `~/.gemini/GEMINI.md` carries the block and the shared Layer 2 text. `~/.gemini/config/GEMINI.md` (929 bytes, dated 2025-10-09, titled "Global Antigravity Agent Directives") carries OpenProject routing only.

## Input and priority ledger

1. `operations/18-APEX-CARRIER-MAP.md`, gaps G4 and G5.
2. `tools/apex_carrier_sync.py` (the carrier list, the `optional` flag on these entries).
3. The files named above. Ignore everything else.

## Process

Run each probe in the environment named, with the exact prompt, and paste the reply into the report.

| # | Environment | Prompt | Pass condition |
|---|---|---|---|
| P1 | `claude-agehm` in an empty folder | "Quote the first rule of your always-on contract, word for word, and name the file it came from." | Quotes `<target>` and names a `CLAUDE.md`. |
| P2 | `claude-wimmer`, same prompt | same | same |
| P3 | Antigravity, any workspace | same | Names `~/.gemini/GEMINI.md` or `~/.gemini/config/GEMINI.md`. |

If P1 or P2 fails, apply the fix below. If P3 names the `config/` file, add the block to it with the sync tool; if it names the other file, delete nothing and mark G5 closed.

**Fix for P1/P2 (operator approval needed, creates files in the account dirs):** link one source file so the accounts cannot drift.

```powershell
New-Item -ItemType SymbolicLink -Path "$HOME\.claude-agehm\CLAUDE.md"  -Target "$HOME\.claude\CLAUDE.md"
New-Item -ItemType SymbolicLink -Path "$HOME\.claude-wimmer\CLAUDE.md" -Target "$HOME\.claude\CLAUDE.md"
```

Developer Mode allows this without an elevated shell. The sync tool reads through the link; edits to `~/.claude/CLAUDE.md` reach all three accounts.

## Output

A short report appended below this handover under `## Report`: the three probe replies, whether the fix was applied, and the sync tool's output.

## Definition of done

- P1 to P3 have recorded replies.
- `python apex-meta/informatics/final/tools/apex_carrier_sync.py` prints `OK` for the Claude account carriers, or the carriers are removed from the tool's list with the reason written in G4.
- The check is the pass condition of each probe, not a script that greps for the account files.

## Report

Not run yet.
