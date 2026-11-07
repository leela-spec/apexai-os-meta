---
type: Handover
id: HANDOVER-09-MAUSBOT-ALIGNMENT-WITH-MASTER
title: Handover 09 — Align MausBot's Apex Skills With the Master
description: Delegation contract for MausBot to compare its two apex skills with the master contract, list deviations, and propose exact patches for operator approval.
status: current
tags: [handover, mausbot, openmausbot, skills, alignment]
---

# Handover 09 — Align MausBot's Apex Skills With the Master

Why this is a handover: only MausBot can read and change its own profile and skills (no supported read-back from outside). Everything checkable from files was checked first, see `operations/19-MAUSBOT-INSTALLATION-RECORD.md`.

## Input and priority ledger

1. `C:/GitDev/apexai-os-meta/apex-meta/informatics/final/specs/apex_contract_v1.0_ultra.xml` (branch `main`). The only authority. Use `<align>`, `<editing>`, `<authoring>`, `<schemas>` and `<trade_off>`.
2. `operations/19-MAUSBOT-INSTALLATION-RECORD.md`, section 3 (the deviations already found). Read it second.
3. Your own `skills/apex-governance/SKILL.md` and `skills/apex-file-changes/SKILL.md`.
4. `operations/18-APEX-CARRIER-MAP.md` for how the other agents carry the contract.
- **Ignore:** Codex, Claude and Gemini instruction files; the OpenProject and OpenMausBot skills.

## Process

1. Read the master block once. Resolve its refs against `C:/GitDev/apexai-os-meta/apex-meta/informatics/final/`.
2. Compare each sentence of your two skills with the matching tag. Mark each as same, narrower, wider, or unrelated.
3. Report the `<align>` deviation as found: your step 2 restates only on request; the master restates by default unless a previous step defined the task.
4. Draft exact-match patches for your skill files. Do not apply them.
- **Boundaries:** do not edit `~/.codex/AGENTS.md`, `~/.claude/CLAUDE.md` or `~/.gemini/GEMINI.md`, and do not touch any contract block. A change to the contract goes through the meta repo and `tools/apex_carrier_sync.py`. Do not repair unrelated source-bundle defects. Do not state compliance you did not check.

## Output

- One file: `C:/Users/gehma/.openmausbot/task-workspaces/bb2f252e-4050-4dac-a7ad-3ca3161f55ce/apex-alignment-report.md`.
- Structure: a table `skill sentence | master tag | same/narrower/wider/unrelated | proposed patch`, then the five components of `specs/execution-modes/handover.md` §5.2 (observation, logic chain, caveats, conclusion, verification method).
- Example row: `"User-approved plans need no repeated alignment approval" | <align> | narrower | add "unless the task is already defined by a previous step", as the master now reads`.

## Definition of done

- Every sentence of both skills has a row.
- The proposed patches quote live text exactly.
- Independent check by the operator or another agent: ask a fresh MausBot conversation "when must you restate a task before acting?" after the patches are applied. The answer must match the master's `<align>`. A script that only greps for strings does not count.
