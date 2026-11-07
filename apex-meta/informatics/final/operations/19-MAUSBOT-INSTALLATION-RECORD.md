---
type: Reference
id: OPS-19-MAUSBOT-INSTALLATION-RECORD
title: MausBot Installation Record
description: What OpenMausBot's MausBot did with the Apex contract on 2026-11-04, why its apex skills exist only there, how they differ from the master, and what to do about it.
status: current
tags: [apex, mausbot, openmausbot, skills, codex, record]
---

# MausBot Installation Record

## 1. What happened on 2026-11-04

Source for every row: `C:/Users/gehma/.openmausbot/workspaces/bb2f252e-4050-4dac-a7ad-3ca3161f55ce/memory/log/2026-11-04.md` (MausBot's own log) and the files in `C:/Users/gehma/.openmausbot/task-workspaces/bb2f252e-4050-4dac-a7ad-3ca3161f55ce/765bdb86-c44d-46d9-9450-3d4938909e34/`.

| Time | What MausBot did | Evidence |
|---|---|---|
| 15:43 | Put the full contract block into MausBot's own standing instructions. Only `base_ref` was localized. | `apex-installed-instructions.txt` (9,581 bytes), `apex-installation-report.md` |
| 16:04 | Recommended replacing the block with a short core plus task skills ("kept too much procedure permanently loaded"). | log, 16:04 |
| 16:10 | Applied it: a 1,025-byte core (`SOUL.md`) and four enabled skills: `apex-governance`, `apex-file-changes`, `openproject-operations`, `openmausbot-operations`. Rollback copy kept. | log, 16:10; `modular-instructions/` |
| 16:25 | **Applied the same change to the global Codex file** `~/.codex/AGENTS.md`: replaced the embedded block with a short core and "read the skill" routing. The log states this affects "MausBot and other Codex conversations". | log, 16:25; rollback `codex-AGENTS.before-routing-2026-11-04.md` (9,931 bytes) |
| 16:38 and 17:39 | Tested with six fresh agents. Later it wrote that it had no evidence the iterative workflow is followed, and that its earlier "migration passed" wording was too broad. | log, 16:38 and 17:39 |

On 2026-11-06 the Codex block was restored from the rollback copy and Codex became a synced carrier (see `18-APEX-CARRIER-MAP.md`).

## 2. Why the apex skills exist only in MausBot

- MausBot wrote them from an operator-approved "modularization proposal" (provenance lines in both `SKILL.md` files). They sit in MausBot's workspace: `.../workspaces/bb2f252e.../skills/` and mirrors under `.agents/`, `.claude/`, `.grok/`.
- They are not in `C:/GitDev/agent-skills/skills/` (only `openmausbot`, `openproject`, `weekly-orchestrator`) and not in `~/.claude/skills`. Command: `find /c/Users/gehma /c/GitDev -maxdepth 6 -name 'apex-governance*'`.
- Claude, Codex and Gemini never needed them: each carries the block inline and opens the gated refs. MausBot has no inline block after 16:10, so the skills are its only route to the master.

## 3. How they relate to the master

| MausBot piece | Master equivalent | Difference |
|---|---|---|
| `apex-file-changes` | `<editing>` and `specs/execution-modes/patch-discipline.md` | Adds "do not commit or push unless authorized". Leela's `AGENTS.md` grants standing commit and push, so this must not spread to other agents. |
| `apex-governance` step 2 | `<align>` | **Deviates.** It says approved plans need no repeated approval and the six fields appear only when the user asks. The master restates by default unless a previous step defined the task. |
| `apex-governance` steps 4-6 | `<authoring>`, `<schemas>`, `verification/` | **Adds facts the master lacks:** `okf_validator.py` takes `--target <bundle root>` and `--json`; `check_decision_bakeoff_shape.py` takes file paths, not `--target`; baseline failures are reported apart from introduced ones. |
| Core (`SOUL.md`) | `<target>`, `<scope>`, `<communication>`, `<ground>`, `<reuse>`, `<context>` in shortened form | Wording differs; no check compares it. |

Two lines from this material were added to Completion Reporting in all three global files (precedence; baseline vs introduced failures). The validator interface facts are not carried anywhere yet.

## 4. Decision: what to do with the skills

Level L2 (`I85/E55/R35`, scored by the author). Evidence labels: measured = a file or command; inferred = reasoning.

| Option | Mechanism | I/E/R |
|---|---|---|
| A. Leave them MausBot-only | Nothing changes. | I40/E70/R55 |
| B. Promote to `agent-skills` and link into every agent | Same pattern as `openproject`. | I55/E40/R50 |
| C. Keep MausBot-only but thin; move the validator facts into this bundle; resolve the `<align>` deviation | See handover `HANDOVER-09`. | I75/E70/R25 |

**Recommendation: C.** A leaves an unreviewed deviation from `<align>` (measured, section 3). B gives Claude, Codex and Gemini a second route to rules they already read through the block, and two routes drift (inferred; the deviation is the example). Cost to reverse C: low, the skills stay in MausBot's workspace. What would change the recommendation: a measurement showing the other agents follow skills but ignore gated refs, which favours B.

## 5. Not verified

- MausBot's profile cannot be read back (installation report), so the live `SOUL.md` and skills were read from disk only.
- A second bot, `c68d0dad-b3d0-4baf-8505-8f4eadbd7141`, exists; I did not inspect it.
- Whether the installed skill files are byte-equal to the `modular-instructions/` copies: a `cmp` printed no match message, not investigated.

## 6. Links

- `operations/18-APEX-CARRIER-MAP.md`, `operations/handovers/HANDOVER-09-MAUSBOT-ALIGNMENT-WITH-MASTER.md`
- `C:/GitDev/agent-skills/skills/openmausbot/TRANSFORMATION-GUIDE.md` (the architecture MausBot cites, sections 2.2-2.4 and 4)
