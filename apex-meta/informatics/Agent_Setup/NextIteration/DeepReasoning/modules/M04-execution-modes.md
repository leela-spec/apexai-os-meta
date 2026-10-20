---
type: Reference
id: DR-M04-EXECUTION-MODES-v1.0
title: M04 — Execution Modes Audit & Patch Record
description: Module audit and applied patch record for execution-modes.md, the suite's largest file and its lowest-yield compression target.
status: current
tags: [research, module-audit, execution-modes, task-adapters]
---

# M04 — Execution Modes Audit & Patch Record

**Verdict:** largest file in the suite (4,216 tokens) and correctly left almost untouched —
`+3/−3` lines, `+72` tokens. Its bulk is load-bearing worked examples, not duplication.

## 1. Input & Context Scope Ledger

| Source | Why loaded |
|---|---|
| [execution-modes.md](../../../../execution-modes.md) | Module under audit, `EM-01..12` |
| [Snippets.md](../../../../../AI-Snippets/Snippets.md) §patch format, §Research & Output, §MMM | Upstream source of Adapters 2, 3, 5 |
| `test_tier5_adversarial.py:478-528` | Asserts ~20 literal strings from this file |

## 2. Why This File Resisted Compression

`execution-modes.md` carries 4,216 tokens across 12 rules — the worst tokens-per-rule ratio in the
suite — yet yields almost nothing. The volume is in four blocks that are each mandated by a rule:

| Block | Lines | Why it stays |
|---|---:|---|
| Canonical Q&A decision-matrix example (Bloc/Riverpod/SetState) | 12 | `WP-17` mandates compact worked examples; `test_tas_03` asserts six literals from it |
| `<execution_dispatch>` IF-routing block | 10 | The dispatch contract itself; XML justified per [02](../02-new-rules-discovery-and-qa-bakeoff.md) Q6 |
| `patch_intent.v1` worked example JSON | 26 | A conforming *instance*, not a copy of the schema — the distinction `WP-23` draws |
| MMM Macro/Meso/Micro table | 6 | Unique to this file |

A worked example is not a duplicate of the rule it illustrates. Compressing here would have traded
measurable behavior for a few hundred tokens — rejected under `WP-01`.

## 3. Applied Patches

| # | Change | Rationale |
|---|---|---|
| 1 | `EM-04` gains `(canonical: AD-01)` | Target dominance owned by `AD` |
| 2 | `EM-05` gains `(canonical: AD-02; mechanics AD-24)` | Two-strike owned by `AD` |
| 3 | §4.2 preamble rewritten: absolute `file:///` link replaced with a relative one, the authoritative schema path named, and the block explicitly labelled a worked example rather than a schema copy | `RBL-05` + `WP-23` |

Diff: `+3/−3`.

## 4. The §4.2 Distinction That Matters

Before: §4.2 said "output JSON conforming to `patch_intent.v1` (see Governance Schemas)" and then
showed an example — while `GS` showed the full schema. A reader could reasonably conclude the
example *was* the contract.

After: §4.2 names three distinct artifacts — the operative contract (`GS` §2.2), the authoritative
machine-readable schema (`patch-intent-schema.json`), and this worked example — and states that the
example is not a second copy of the schema. That is the structural lesson of **D9** written into
the file where the next author will hit it.

## 5. Behavioral Check

| Scenario | Expected | Observed |
|---|---|---|
| Agent authors a patch intent loading `EM` alone | Gets a complete conforming example inline | §4.2 JSON unchanged |
| Agent needs the full field contract | One hop to `GS` §2.2, then the JSON file if needed | Both paths named in §4.2 |
| Agent runs a bake-off | Finds all four phases and both decision triggers | `test_tas_04` green |
| Agent hits a failing subsystem twice | Stops; `EM-05` points to `AD-02`/`AD-24` for tracking mechanics | Marker added |
| Agent routed only by `task_execution_adapter` | Executes any of the six adapters without a second load | All adapter bodies intact |

## 6. Open Items

None specific to this module. `RBL-01` (does single-gate isolation hold in production routing?)
would, if it resolves against the premise, reopen whether `EM-04`/`EM-05` should be pointers rather
than restatements.
