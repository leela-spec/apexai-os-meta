---
type: Reference
id: DR-M06-GOVERNANCE-SCHEMAS-v1.0
title: M06 — Governance Schemas Audit & Patch Record
description: Module audit and applied patch record for governance-schemas.md, the suite's highest-waste file and the site of the drifted patch-intent schema copy.
status: current
tags: [research, module-audit, governance-schemas, patch-intent, schema-drift]
---

# M06 — Governance Schemas Audit & Patch Record

**Verdict:** the pass's decisive result. `governance-schemas.md` goes from **264 lines / 4,068
tokens to 134 lines / 2,719 tokens — −49% lines, −33% tokens** — while *gaining* contract accuracy,
because the block that dominated it had already drifted into a weaker contract than the one the
tooling enforces.

## 1. Input & Context Scope Ledger

| Source | Why loaded |
|---|---|
| [governance-schemas.md](../../../../governance-schemas.md) | Module under audit, `GS-01..22` |
| `.claude/skills/deterministic-markdown-patcher2/references/patch-intent-schema.json` | Authoritative schema (**D9**) |
| [file-architecture.md](../../../../file-architecture.md) §3 | Competing frontmatter contract (**D2**) |
| [execution-modes.md](../../../../execution-modes.md) §2.1, §3.1 | Owner of Q&A and bake-off formats |
| `okf_validator.py:100-127` | Real `STE-SENTENCE-LENGTH` threshold (**D5**) |
| `test_tier5_adversarial.py:414-466` | The one test that parsed the inline schema |

## 2. Applied Patches

| # | Change | Lines cut | Defect |
|---|---|---:|---|
| 1 | 93-line inline `patch_intent.v1` JSON Schema replaced by an 8-row operative contract table plus a link to the authoritative JSON | ~80 | **D9** |
| 2 | Root-index and concept frontmatter YAML contracts deleted; `GS-06`/`GS-07` rewritten as validation-side rejection rules pointing at `FA-05`/`FA-06` | ~25 | **D2** |
| 3 | Q&A data-dictionary table and bake-off phase list deleted; `GS-12`/`GS-13` rewritten as conformance rules pointing at `EM` §2.1/§3.1 | ~15 | B4 |
| 4 | Priority-tier table and 3-metric dimension definitions deleted; owned by `WP-07` | ~11 | B3 |
| 5 | `GS-18` folded into `GS-04`; `GS-17` absorbed `GS-19`; `GS-16` deleted as a duplicate of `WP-20` | ~6 | **D6** |
| 6 | `GS-02`, `GS-03`, `GS-04`, `GS-05`, `GS-08`, `GS-22` gain canonical markers | — | `CROSS_LINK` |
| 7 | §4/§5 swapped — traceability moved above the diagnostics catalog so the file ends on the conformance gate | — | `WP-25` |
| 8 | Advisory gate (>30 words) reconciled with the `WP-14` authoring target | — | **D5** |
| 9 | Four absolute `file:///` links converted to relative | — | `RBL-05` |

Diff: `+46/−176`.

## 3. D9 — The defect behind the big number

`GS` §2.2 embedded a full copy of `patch-intent-schema.json`, the file `GS` §5 simultaneously cited
as the "Patch Intent Source Schema." A specification that names an upstream source and then
restates it has created a drift channel, and the drift had already happened.

Structural diff of the two JSON documents: **482 lines**. Decomposed:

| Aspect | Authoritative | Inline copy | Impact |
|---|---|---|---|
| `required` per intent | `intent_id`, `operation`, `target`, `safety` | identical | none |
| `operation` enum | 9 values | identical 9 values | none |
| `safety` consts | all four | identical | none |
| `$id` | present | **absent** | schema not addressable |
| `$defs` / `$ref` | normalized | flattened inline | cosmetic |
| `maxLength` bounds | `target_file_guess` ≤500, `heading_path` items ≤200, `nearby_phrases` items ≤300 | **all dropped** | **spec is a weaker contract than the tool** |

So the published contract accepted intents the real validator rejects. An agent authoring strictly
from the specification could emit a document the patcher refuses — the specification was lying by
omission, and no gate could see it.

The replacement states the operative contract (envelope, required fields, operation enum, the four
safety invariants, closed-object rule, and the existence of length ceilings) in 8 table rows, and
names the JSON file as the single source for the exact bounds.

## 4. Test Update — justified, and strictly stronger

`test_tas_02_patch_intent_v1_json_schema_validation` extracted the schema from `gov_text` by regex.
That test could not survive patch 1, so it was rewritten rather than deleted:

| Before | After |
|---|---|
| Parsed the inline markdown copy | Loads `patch-intent-schema.json` — the artifact the patcher actually uses — and resolves its `$ref`/`$defs` indirection |
| Asserted safety consts on the copy | Asserts the same consts on the authoritative schema |
| — | **Additionally** asserts `governance-schemas.md` states every safety invariant and every one of the 9 operation enum values |

The old test could pass while the spec and the tool disagreed. The new one fails in exactly that
case. This is the handover's sanctioned category — updating an assertion so it validates a real
architectural invariant rather than outdated wording — not a test weakened to make a patch pass.

Diff: `test_tier5_adversarial.py +27/−6`.

## 5. Retired IDs

`GS-16`, `GS-18`, `GS-19` are retired and **not reused**. The file states this inline so a future
reader does not read the gap as an authoring error. Reusing a retired durable ID would break
`WP-15` the same way **D1** did.

## 6. Behavioral Check

| Scenario | Expected | Observed |
|---|---|---|
| Agent authors a patch intent from `GS` alone | Knows the four safety invariants, all 9 operations, and that bounds exist | Contract table; `test_tas_02` asserts every value |
| Agent needs an exact `maxLength` | Follows one link to the authoritative JSON | Linked and test-verified to exist |
| Schema file changes upstream | Spec does not silently diverge | `TestNoReEmbeddedUpstreamSchema` blocks re-embedding; `test_tas_02` cross-checks the stated contract |
| Agent validates a bundle | Finds the tri-class catalog and the zero-error gate | §5 intact, now in the recency slot |
| Agent looks up `P2` semantics in `GS` | One hop to `WP-07` | Accepted — `GS` is a validation surface, not an authoring one |
| Agent writes a 28-word sentence | Not a violation | §5 reconciliation note |

## 7. Open Items

- **D8** (`estimate_tokens` duplicated across two test files) — **deliberately not fixed.** Removing
  it means creating a shared helper module to deduplicate a 4-line function. `AD-25` (confirm
  ordinary use doesn't already surface the problem) and `AD-13` (evidence proportionality) both say
  no. Recorded rather than actioned.
- `RBL-08` — whether a mechanical spec-vs-upstream-artifact consistency gate is warranted. Deferred
  under `AD-25` until a second instance appears.
