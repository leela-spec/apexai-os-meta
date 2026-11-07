---
type: Reference
id: V2-LAYERED-KB-RULE-23-ALIGN
title: Rule 23 Change Record — <align> Pre-Work Task Restatement
description: What the <align> rule says now, how its trigger changed on 2026-11-06, and what is still missing (no semantic block audit exists for it).
status: current_truth
tags: [layered-kb, rule-23, align, em-13, change-record]
---

# Rule 23: `<align>`

> **This is a change record, not a deep-dive.** Rules 01-22 were audited into semantic blocks. `<align>` was added after that audit and has none. Audit it before editing its wording again.

## 1. Current text (master, 2026-11-07)

```xml
<align when="the task is non-trivial, not a direct question, and not already defined by a previous step" ref="specs/execution-modes/task-specification.md">
Before acting, restate the task once and wait for confirmation. Six fields, no preamble:
- **Input**: the literal ask, verbatim.
- **Sources**: the artifacts you will open.
- **Process**: how you will get and verify the facts, and the reasoning framework if you use one.
- **Skills**: the tools or skills you will invoke, or none.
- **Output**: what you will change, and what the deliverable is.
- **Redraft**: the shape of the future output - its headers with what each will contain and the value it carries; or concrete examples where specific detail was asked for.
Open ref for definitions and the failure each field prevents.
</align>
```

Owner module: [`specs/execution-modes/task-specification.md`](../../specs/execution-modes/task-specification.md), `EM-13 [P0 | I94/E88/R10]`.

## 2. The 2026-11-06 change (record [`C1`](../../operations/20-CHANGE-RECORD-2026-11-06-07.md))

- **Before:** `when="the task is not a single trivial edit or a direct question"`; `EM-13`: "a task is anything other than a single trivial edit or a direct question".
- **Problem:** every non-trivial step is restated, including steps an approved plan already defines (*inferred* from MausBot's guidance, see [`19-MAUSBOT-INSTALLATION-RECORD.md`](../../operations/19-MAUSBOT-INSTALLATION-RECORD.md)). The author of the edit is unknown: it was uncommitted when found.
- **Solution:** both lines now say "non-trivial, not a direct question, and not already defined by a previous step".
- **After:** the block in Claude, Gemini, Codex and the Leela vendored copy carries the new trigger. MausBot's `apex-governance` skill restates only on request, which is weaker (`HANDOVER-09`).

## 3. Not done

- No `SB-23.k` semantic block inventory, no token measurement, no value critique.
- "Already defined by a previous step" is not defined anywhere; two agents can read it differently.
- `TODO-EM-13-A` in `task-specification.md` (ranked reasoning frameworks) is still open.
