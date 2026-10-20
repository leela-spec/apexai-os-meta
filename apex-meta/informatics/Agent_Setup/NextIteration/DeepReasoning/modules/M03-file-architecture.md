---
type: Reference
id: DR-M03-FILE-ARCHITECTURE-v1.0
title: M03 — File Architecture Audit & Patch Record
description: Module audit and applied patch record for file-architecture.md, including the FA-04 durable ID collision, the stale bundle topology, and the frontmatter contract reconciliation.
status: current
tags: [research, module-audit, file-architecture, durable-ids, frontmatter]
---

# M03 — File Architecture Audit & Patch Record

**Verdict:** `file-architecture.md` −18 lines / −45 tokens, and three defects closed — a duplicate
durable ID, a stale topology tree, and a frontmatter contract that contradicted `GS`.

## 1. Input & Context Scope Ledger

| Source | Why loaded |
|---|---|
| [file-architecture.md](../../../../file-architecture.md) | Module under audit, `FA-01..12` |
| [governance-schemas.md](../../../../governance-schemas.md) §2.1 | Conflicting frontmatter contract (**D2**) |
| `okf_validator.py:150-230` | What the validator actually enforces |
| Live bundle directory listing | Ground truth for the topology tree (**D4**) |
| `test_tier5_adversarial.py:339` | Asserts "Residual Name Eradication" stays present in this file |

## 2. Applied Patches

| # | Change | Defect |
|---|---|---|
| 1 | Second `FA-04` ("Flat/Inline YAML Frontmatter Serialization") renumbered to **`FA-13`** | **D1** |
| 2 | `FA-05` root-index schema gains `tags`; declared the canonical frontmatter contract | **D2** |
| 3 | `FA-06` gains an explicit `version` field (optional) and a required-vs-expected statement reconciled against the validator | **D2** |
| 4 | §4 topology tree rewritten to list all 10 live files plus `tests/` and the `Agent_Setup/` boundary | **D4** |
| 5 | §5 "Significance & Ranking Architecture" (15 lines) deleted; semantics owned by `WP-07` | B3 |
| 6 | §6 collapsed — `FA-12` reduced to a sizing/parsimony rule pointing at the §2 plane table and `WP-18` | B5 |
| 7 | `FA-02`, `FA-04`, `FA-07`, `FA-09` gain canonical markers (`WP-06`, `WP-01`, `WP-15`, `AD-15`) | `CROSS_LINK` |

Diff: `+25/−43`.

## 3. D1 — Why renumbering chose `FA-13`

Baseline defined 13 rules under 12 IDs: `FA-04` labelled both "Substance Over Ceremony Exception
Authority" (§1, P0) and "Flat/Inline YAML Frontmatter Serialization" (§3, P1). The collision
survived a green validator and 185 tests because `okf_validator.py` enforces uniqueness on
frontmatter `id:` only, never on in-body rule IDs (`RBL-06`).

Per [02](../02-new-rules-discovery-and-qa-bakeoff.md) Q7, the first occurrence keeps `FA-04` and the
serialization rule moves to `FA-13` — appending outside document order, which looks untidy, instead
of renumbering `FA-05`..`FA-12` and invalidating eight live cross-references. Durable IDs exist so
references survive revision (`WP-15`); disturbing one ID beats disturbing eight.

Verified: 13 `### FA-` headings, 13 distinct IDs, no gaps or repeats.

## 4. D2 — The reconciled contract

The two files disagreed on two fields. The merged contract, owned here and stated from the
validation side in `GS-06`/`GS-07`, matches what `okf_validator.py` actually enforces:

| Field | Root `index.md` | Concept `*.md` | Enforced by |
|---|---|---|---|
| `okf_version` | Required (`"0.2"`) | — | `OKF-VERSION-DECLARATION` |
| `type` | — | Required, non-empty | `OKF-TYPE-REQUIRED` |
| `id` | — | Required, bundle-unique | `APEX-UNIQUE-DURABLE-ID` |
| `title`, `description` | Required | Required | Profile |
| `status` | — | Required | Profile |
| `tags` | Expected | Expected | Profile |
| `version` | — | **Optional** — absence is never a failure | Profile |

`version` was the sharper half of the defect: `GS-07`'s contract showed it in the canonical block,
so an agent copying that block into a new concept file would invent a version number for a document
that is not independently versioned.

## 5. Behavioral Check

| Scenario | Expected | Observed |
|---|---|---|
| Agent creates a concept file loading `FA` alone | Has the full YAML schema inline, no second load | `FA-05`/`FA-06` retain their blocks |
| Agent cross-references `FA-04` | Resolves to exactly one rule | 13 unique IDs confirmed |
| Agent reads §4 to locate a module | Finds `anti-drift-rules.md` and `governance-schemas.md` | Tree now complete |
| Agent needs `P2` semantics while in `FA` | Follows one marker to `WP-07` | Accepted cost — tier semantics are authoring-time, not file-creation-time |
| Agent must not resurrect deleted names | `FA-09` still present | `test_tier5_adversarial.py:339` green |

## 6. Open Items

`RBL-06` — promote in-body rule-ID uniqueness into `okf_validator.py` as an `APEX_PROFILE_ERROR`.
Partially closed this pass by `test_canonical_ownership.py::TestDurableRuleIdUniqueness`, which is
pytest-scoped rather than repo-wide.
