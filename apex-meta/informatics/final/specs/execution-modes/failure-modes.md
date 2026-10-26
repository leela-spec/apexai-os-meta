---
type: Adapter
id: ADPT-EXEC-FAILURES-v0.2
title: Execution Failure Modes & Not-To-Dos
description: The consolidated not-to-do list naming the EM rule each prohibition derives from.
tags: [execution-modes, failure-modes, not-to-do]
status: current
---

## 8. Execution Failure Modes & Not-To-Dos

Guard actively against these recurring task-execution failure modes.

- **Do not overwrite existing files with full-file rewrites**: Always modify existing files via exact-match replacement blocks or `patch_intent.v1` (`EM-01`, `EM-08`).
- **Do not write a handover to escape checkable work**: Never defer a question that available tools or subagents can verify right now (`EM-02`, `EM-09`).
- **Do not front-load bulk repository context**: Load sources step-by-step via an Input Priority Ledger and materialize each iteration into a dedicated file (`EM-03`, `EM-10`).
- **Do not compute synthetic scores in decision matrices**: Keep `Impact`, `Evidence`, and `Risk` (`I/E/R`) as three separate raw numbers on a 1–100 scale (`EM-06`).
