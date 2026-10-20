---
type: Reference
id: DR-M01-ROUTERS-INDEX-v1.0
title: M01 — Routers, Index & Authority Precedence
description: Module audit and applied patch record for index.md, general-informatics-router.md, and the standard.md authority reconciliation.
status: current
tags: [research, module-audit, router, index, authority]
---

# M01 — Routers, Index & Authority Precedence

**Verdict:** `index.md` −35 tokens, router unchanged by design, and the dual-authority conflict
between `standard.md` and the modular suite is closed.

## 1. Input & Context Scope Ledger

| Source | Why loaded |
|---|---|
| [index.md](../../../../index.md) | Dispatch surface under audit |
| [general-informatics-router.md](../../../../general-informatics-router.md) | Embeddable derivative under audit |
| [standard.md](../../../../standard.md) §2 | Precedence ladder (**D7**) |
| `.claude/rules/informatics.md` | Scoped rule naming `standard.md` as overriding canon (**D7**) |
| `test_tier5_adversarial.py` `test_rcb_01`, `test_informatics_e2e.py` `test_live_07` | Router ceilings |

Shared reasoning lives in [01-overlap audit](../01-system-wide-overlap-and-token-audit.md) and
[02-bake-off](../02-new-rules-discovery-and-qa-bakeoff.md) Q3/Q8. Not restated here (`WP-23`).

## 2. Applied Patches

| # | File | Change | Defect |
|---|---|---|---|
| 1 | `index.md` | Added `tags: [informatics, index, router, okf-v0.2]` to frontmatter | **D3** |
| 2 | `index.md` | §3 module descriptions replaced with rule-ID ranges and a one-line canonical-ownership summary; the gate payloads in §2 already carry the descriptions | B6 |
| 3 | `standard.md` | §2 precedence ladder extended from 4 to 5 layers; the modular suite inserted at rank 2 and explicitly governs any subject it covers | **D7** |
| 4 | `.claude/rules/informatics.md` | Points 1–3 rewritten to route through the `<informatics>` gates and to name the modular suite as the owner of local profile rules | **D7** |

Diff: `index.md +11/−6`, `standard.md +4/−3`, `.claude/rules/informatics.md +3/−3`.

## 3. Router Decision — reverted, deliberately

Q3 selected "declare the derivation in the router." **That patch was applied and then reverted.**

The router measured exactly **500 tokens at baseline** — precisely its tested ceiling
(`test_live_07` asserts ≤500 tokens and ≤120 lines; `test_rcb_01` duplicates the check). Every
phrasing of a provenance note, down to a 74-character single line folded into the frontmatter
`description`, pushed it to 518–533 tokens and turned both tests red.

Two options existed: relax the ceiling, or drop the note. The ceiling was kept, because:

1. `index.md` §3 **already declares** the derivation — "standalone embeddable derivative of §1–2 for
   use in other repositories" — so an auditor reading the bundle finds the answer. Adding it again
   in the router would duplicate a statement that already has an owner, violating `WP-23`, the rule
   this very pass introduced.
2. The ceiling is the only thing protecting the router's single purpose. Weakening a gate to admit
   a nice-to-have comment is how ceilings stop meaning anything.

Net effect: `general-informatics-router.md` is **byte-identical to baseline**. That is the correct
outcome, not an omission.

## 4. Behavioral Check

| Scenario | Expected | Observed |
|---|---|---|
| Agent loads `index.md` and routes a pure writing task | Resolves `writing-profile.md` only | `test_cis_01` green |
| Agent reads §3 after compression | Can still name every module and its rule range | Ranges `WP-01..25`, `FA-01..13`, `EM-01..12`, `AD-01..28`, `GS-01..22` present |
| Agent edits a file under `apex-meta/informatics/` | Scoped rule routes it to `index.md` gates, not to `standard.md` prose | `.claude/rules/informatics.md` point 1 rewritten |
| Agent finds a `standard.md` §6 prose rule conflicting with `WP-14` | `WP-14` governs | `standard.md` §2 rank 2 states this explicitly |
| Router pasted into another repository | Self-contained, no unresolvable relative links | Unchanged from baseline |

## 5. Open Items

- `RBL-02` — plane token orientations vs 2026 convention.
- The root `CLAUDE.md` "Informatics & Knowledge Routing" section still names `standard.md` as the
  authority over ad-hoc conventions. **Left unpatched deliberately:** that claim is now correct by
  transitivity, since `standard.md` §2 defers to the modular suite. Changing it would be scope
  creep into the always-on control plane.
