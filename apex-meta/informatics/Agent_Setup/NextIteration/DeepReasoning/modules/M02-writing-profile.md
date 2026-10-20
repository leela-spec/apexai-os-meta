---
type: Reference
id: DR-M02-WRITING-PROFILE-v1.0
title: M02 — Writing Profile Audit & Patch Record
description: Module audit and applied patch record for writing-profile.md, which becomes canonical owner of prose ergonomics, significance ranking, and the three newly discovered rules.
status: current
tags: [research, module-audit, writing-profile, new-rules]
---

# M02 — Writing Profile Audit & Patch Record

**Verdict:** `writing-profile.md` grows **+14 lines / +545 tokens (+24%)** and that growth is the
point — it absorbs ownership of the priority-tier semantics previously duplicated in two other
files, and gains the three rules the suite was missing.

## 1. Input & Context Scope Ledger

| Source | Why loaded |
|---|---|
| [writing-profile.md](../../../../writing-profile.md) | Module under audit, all 22 baseline rules |
| [Snippets.md](../../../../../AI-Snippets/Snippets.md) | Operator lore; source of `WP-23` |
| [2Dos Ai Instructions.md](../../../../../AI-Snippets/Orga/2Dos%20Ai%20Instructions.md) line 41 | Source of `WP-24` |
| `okf_validator.py:100-127` | Actual `STE-SENTENCE-LENGTH` threshold (**D5**) |
| `test_informatics_e2e.py` `validate_tags_descending_order` | Tier-order constraint on insertions |

## 2. Applied Patches

| # | Change | Rationale |
|---|---|---|
| 1 | `WP-07` gains the **Priority Tiers table** and the **Impact/Evidence/Risk dimension definitions** as a labeled block under §1 | Canonical owner per [01](../01-system-wide-overlap-and-token-audit.md) B3; deleted from `FA` §5 and `GS` §3.2 |
| 2 | `WP-04`, `WP-08`, `WP-16` gain `(canonical: AD-19 / AD-15 / AD-20)` markers | `CROSS_LINK` — rule retained for single-gate self-sufficiency, wording bound to its owner |
| 3 | `WP-14` states the relationship between the ~20/25 authoring target and the >30-word advisory gate | **D5** |
| 4 | **`WP-23` Single-Owner Instruction Reuse** added (P1) | New rule — [02](../02-new-rules-discovery-and-qa-bakeoff.md) §4 |
| 5 | **`WP-24` Clickable File References** added (P2) | New rule from operator lore |
| 6 | **`WP-25` Terminal-Position Operative Content** added (P2) | New rule from positional-attention research |
| 7 | §4 and §5 swapped; file now ends on Failure Modes, traceability moved above | `WP-25` self-applied |
| 8 | Speculative "Future Architecture Note" removed | Violated `FA-01`; relocated to `RBL-03` |
| 9 | Four `file:///c:/GitDev/...` links converted to repository-relative | `RBL-05` |
| 10 | Fifth Not-To-Do added: "Do not copy a canonical block into a second file" | Gives `WP-23` a recency-slot guard |

Diff: `+31/−17`.

## 3. D5 Correction — the register overstated this

The master matrix originally recorded **D5** as "sentence-length stated three ways: ~20–25 / ~30 /
25-30." Direct inspection of `okf_validator.py:119` shows `if len(words) > 30`, so the gate fires
above **30** and the `GS` catalog's "~30 words" was already correct.

The real defect was narrower: two deliberately different numbers — an authoring target (`WP-14`)
and an advisory gate — that no file reconciled, plus a validator **message string** that prints
"> 25-30 words" while testing `> 30`. Patch 3 states the relationship in `WP-14`, and `GS` §5 now
says the same thing from the gate's side. The misleading message string is cosmetic and left alone.

## 4. Tier-Order Constraint on Insertions

`test_live_02` asserts significance tags appear in non-increasing tier order across the file, so
new rules could not simply be appended. Placement:

- `WP-23` (P1) → inserted before `WP-17`, at the P1/P2 boundary in §3.
- `WP-24`, `WP-25` (P2) → inserted before `WP-22` (P3), at the P2/P3 boundary.

Within-tier `I/E/R` ordering is **not** enforced (`validate_tags_descending_order` compares
`tier_rank` only), so `WP-24`'s `I82` following `WP-21`'s `I80` is legal. Verified green.

## 5. Behavioral Check

| Scenario | Expected | Observed |
|---|---|---|
| Agent tags a new rule, loads `WP` alone | Finds tier semantics and metric definitions inline | `WP-07` block present; no pointer to follow |
| Agent writes a 27-word descriptive sentence | Not treated as a violation | `WP-14` states target-vs-gate explicitly |
| Agent lists four files in a report | Renders them as clickable links | `WP-24` |
| Agent is tempted to copy the frontmatter schema into a new module | Blocked | `WP-23` plus the §5 Not-To-Do |
| Agent reads only the tail of `WP` | Encounters anti-patterns, not link boilerplate | §5 is now Failure Modes |

## 6. Open Items

`RBL-03` (root-surface consolidation of `WP-02`/`03`/`05`), `RBL-04` (empirical directive ceiling).
