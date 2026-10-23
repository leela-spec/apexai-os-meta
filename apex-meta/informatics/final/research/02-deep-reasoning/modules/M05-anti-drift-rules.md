---
type: Reference
id: DR-M05-ANTI-DRIFT-v1.0
title: M05 — Anti-Drift Rules Audit & Patch Record
description: Module audit and applied patch record for anti-drift-rules.md, the suite's densest and already best-structured file.
status: current
tags: [research, module-audit, anti-drift, operational-lore]
---

# M05 — Anti-Drift Rules Audit & Patch Record

**Verdict:** the best-compressed file in the suite at baseline — 28 rules in 2,452 tokens
(~88 tokens/rule) — and it already satisfied `WP-25` before `WP-25` existed. Net change: `+7/−7`
lines, `+5` tokens.

## 1. Input & Context Scope Ledger

| Source | Why loaded |
|---|---|
| [anti-drift-rules.md](../../../../anti-drift-rules.md) | Module under audit, `AD-01..28` |
| [Snippets.md](../../../../../AI-Snippets/Snippets.md) §anti-drift 1–8, §overcorrecting | Upstream source of `AD-01`..`AD-13` |
| [2Dos Ai Instructions.md](../../../../../AI-Snippets/Orga/2Dos.md) | Incident record behind `AD-05`, `AD-06`, `AD-25` |
| `test_tier5_adversarial.py:260-362` | Asserts the 8 Anti-Drift Laws by name |

## 2. Applied Patches

| # | Change | Rationale |
|---|---|---|
| 1 | `AD-03` gains `(canonical: EM-01, EM-08)` | Patch protocol owned by `EM` |
| 2 | `AD-04` gains `(canonical: EM-03, EM-10)` | Iteration loop owned by `EM` |
| 3 | `AD-06` gains `(canonical: EM-02)` | Handover non-paralysis owned by `EM` |
| 4 | `AD-08` gains `(canonical: WP-01)` | Substance Over Ceremony owned by `WP` |
| 5 | `AD-17` gains `(canonical: WP-12)` | BLUF owned by `WP` |
| 6 | `AD-26` gains `(canonical: WP-18)` | Parsimony ceiling owned by `WP` |
| 7 | `AD-27` four absolute `file:///` links converted to relative; rule extended to require relative links | `RBL-05` |

Diff: `+7/−7`. No rule removed, no rule reworded beyond the marker suffix.

## 3. Why Nothing Was Deleted Here

Six `AD` rules restate concepts owned elsewhere (`AD-03`, `04`, `06`, `08`, `17`, `26`), which under
a naive dedup policy would be six deletions. All six were retained as `CROSS_LINK`:

1. **Tests encode the requirement.** `test_olt_07` asserts "Substance Over Ceremony" appears in
   `anti-drift-rules.md`, `writing-profile.md`, `file-architecture.md`, `index.md`, *and* the
   router. `test_olt_06` asserts four more by name in this file. These tests exist because a
   single-gate agent routed to `operational_anti_drift` must get the whole drift contract.
2. **Cost is negligible.** The six restatements total ~140 tokens. The marker suffixes added ~35.
   Deleting them would save ~105 tokens and cost a file hop on the suite's highest-stakes module.
3. **`AD` is the module an agent loads when it is already drifting.** That is the worst moment to
   send it to a second file.

What the markers *do* buy is anti-contradiction: each restatement is now explicitly bound to an
owner, so the next editor knows which file to change first. That addresses the mechanism behind
**D2** and **D9** without paying the hop.

## 4. `AD-26` Parsimony — the file audits itself

`AD-26` orients at ~30–50 active directives per standalone file. This file carries 28 rules plus
6 Not-To-Dos = **34 directives** — inside its own band, with no headroom narrative needed. Logged
as `RBL-04` for empirical measurement rather than pre-emptive restructuring: splitting a file that
satisfies its own rule, on the strength of a convention nobody has measured, is exactly the
over-correction `AD-22` forbids.

## 5. Behavioral Check

| Scenario | Expected | Observed |
|---|---|---|
| Agent routed to `operational_anti_drift` alone | Has all 8 laws, two-strike, sunk-cost, and the Not-To-Dos without a hop | All 28 rules intact |
| Agent reads the file tail | Hits Failure Modes / Not-To-Dos | §4 already last at baseline — `WP-25` compliant |
| Agent follows `AD-27` sibling links from a Linux checkout | Links resolve | Converted to relative |
| Operator corrects one sentence | Agent makes a surgical edit, not a sweep | `AD-22` intact |
| Agent considers a third repair attempt on a failing subsystem | Stops | `AD-02` + `AD-24` intact |

## 6. Open Items

`RBL-04` (empirical directive ceiling), `RBL-01` (single-gate isolation premise).
