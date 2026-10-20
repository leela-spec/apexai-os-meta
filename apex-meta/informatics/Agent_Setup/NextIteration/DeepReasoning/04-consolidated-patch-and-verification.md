---
type: Reference
id: DR-CONSOLIDATED-VERIFICATION-v1.0
title: Consolidated Patch Ledger & Verification Report
description: Master execution-order patch ledger, measured before/after scorecard, mutation-tested invariant guards, and the 5-component forensic report for the Apex Informatics compression pass.
status: current
tags: [research, patch-ledger, verification, forensic-report, scorecard]
---

# Consolidated Patch Ledger & Verification Report

**Bottom line:** 9 defects closed, 3 rules added, 3 durable invariant guards installed and
mutation-tested. The suite drops **129 lines and 807 tokens (−14% / −5%)**, concentrated almost
entirely in one file. The headline number is smaller than projected, and §4 explains honestly why.

## 1. Patch Ledger (execution order)

| # | Target | Change | Module | Defect |
|---|---|---|---|---|
| 1 | `writing-profile.md` | `WP-07` absorbs priority-tier table + I/E/R dimension definitions | [M02](modules/M02-writing-profile.md) | B3 |
| 2 | `writing-profile.md` | `WP-14` reconciles authoring target with the advisory gate | M02 | **D5** |
| 3 | `writing-profile.md` | `WP-04`/`WP-08`/`WP-16` gain canonical markers | M02 | `CROSS_LINK` |
| 4 | `writing-profile.md` | `WP-23` Single-Owner Instruction Reuse added | M02 | new |
| 5 | `writing-profile.md` | `WP-24` Clickable File References added | M02 | new |
| 6 | `writing-profile.md` | `WP-25` Terminal-Position Operative Content added | M02 | new |
| 7 | `writing-profile.md` | §4/§5 swapped; Future Architecture Note removed; links relativized; 5th Not-To-Do added | M02 | `WP-25`, `FA-01`, `RBL-05` |
| 8 | `file-architecture.md` | Duplicate `FA-04` renumbered to `FA-13` | [M03](modules/M03-file-architecture.md) | **D1** |
| 9 | `file-architecture.md` | `FA-02`/`FA-04`/`FA-07`/`FA-09` gain canonical markers | M03 | `CROSS_LINK` |
| 10 | `file-architecture.md` | `FA-05`/`FA-06` declared canonical frontmatter contract; `tags` + optional `version` reconciled | M03 | **D2** |
| 11 | `file-architecture.md` | §4 topology tree corrected to the live bundle | M03 | **D4** |
| 12 | `file-architecture.md` | §5 significance architecture deleted; §6 collapsed into `FA-12` | M03 | B3, B5 |
| 13 | `governance-schemas.md` | Inline `patch_intent.v1` schema → operative contract + authoritative link | [M06](modules/M06-governance-schemas.md) | **D9** |
| 14 | `governance-schemas.md` | Frontmatter YAML contracts deleted; `GS-06`/`GS-07` → validation-side rules | M06 | **D2** |
| 15 | `governance-schemas.md` | Q&A dictionary + bake-off phases deleted; `GS-12`/`GS-13` → conformance rules | M06 | B4 |
| 16 | `governance-schemas.md` | `GS-18` folded into `GS-04`; `GS-17` absorbed `GS-19`; `GS-16` deleted; tier table removed | M06 | **D6**, B3 |
| 17 | `governance-schemas.md` | §1 canonical markers; §4/§5 swapped; advisory gate reconciled; links relativized | M06 | `WP-25`, **D5**, `RBL-05` |
| 18 | `index.md` | `tags` added to frontmatter | [M01](modules/M01-routers-and-index.md) | **D3** |
| 19 | `index.md` | §3 descriptions → rule ranges + ownership summary | M01 | B6 |
| 20 | `standard.md` | §2 precedence ladder: modular suite inserted at rank 2 and given governing authority | M01 | **D7** |
| 21 | `.claude/rules/informatics.md` | Routes through `<informatics>` gates; names the modular suite as owner of local profile rules | M01 | **D7** |
| 22 | `execution-modes.md` | `EM-04`/`EM-05` markers; §4.2 distinguishes contract / schema / worked example | [M04](modules/M04-execution-modes.md) | `CROSS_LINK`, `WP-23` |
| 23 | `anti-drift-rules.md` | Six canonical markers; `AD-27` links relativized and rule extended | [M05](modules/M05-anti-drift-rules.md) | `CROSS_LINK`, `RBL-05` |
| 24 | `test_tier5_adversarial.py` | `test_tas_02` retargeted at the authoritative schema + spec cross-check | M06 | **D9** |
| 25 | `tests/test_canonical_ownership.py` | **New** — 11 invariant tests across 4 guard classes | Iteration 4 | **D1**, **D9**, `RBL-05` |
| — | `general-informatics-router.md` | **Reverted to baseline** — see [M01](modules/M01-routers-and-index.md) §3 | M01 | Q3 |

All live-file mutations were applied by exact-match replacement, one logical change per operation,
with `<old>` taken from in-session file inspection (`EM-08`). No file was regenerated.

## 2. Measured Scorecard

Baseline at commit `6b7f54ee`; after-values measured with the same `estimate_tokens` helper
(`AD-11` reuse-before-build).

| File | Lines before | Lines after | Δ | Tokens before | Tokens after | Δ |
|---|---:|---:|---:|---:|---:|---:|
| `index.md` | 60 | 65 | +5 | 994 | 959 | −4% |
| `general-informatics-router.md` | 43 | 43 | 0 | 500 | 500 | 0% |
| `writing-profile.md` | 79 | 93 | +14 | 2,300 | 2,845 | +24% |
| `file-architecture.md` | 170 | 152 | −18 | 2,543 | 2,498 | −2% |
| `execution-modes.md` | 242 | 242 | 0 | 4,144 | 4,216 | +2% |
| `anti-drift-rules.md` | 75 | 75 | 0 | 2,452 | 2,457 | 0% |
| `governance-schemas.md` | 264 | 134 | **−130** | 4,068 | 2,719 | **−33%** |
| **Total** | **933** | **804** | **−129 (−14%)** | **17,001** | **16,194** | **−807 (−5%)** |

## 3. Verification

### 3.1 Deterministic gates

```bash
python apex-meta/scripts/okf_validator.py --target apex-meta/informatics
```
`Summary: OKF Errors: 0 | Apex Profile Errors: 0 | Advisories: 12` — baseline was 13; one advisory
removed, none added.

```bash
python -m pytest apex-meta/informatics/tests/ -q
```
`196 passed, 96 subtests passed` — baseline 185. Net **+11 tests**, zero failures, one assertion
rewritten (ledger #24, justified in [M06](modules/M06-governance-schemas.md) §4).

```bash
python -c "import sys,pathlib; sys.path.insert(0,'apex-meta/informatics/tests'); from test_tier5_adversarial import estimate_tokens; [print(p.name, len(p.read_text(encoding='utf-8').splitlines()), estimate_tokens(p.read_text(encoding='utf-8'))) for p in sorted(pathlib.Path('apex-meta/informatics').glob('*.md'))]"
```

### 3.2 Mutation testing of the new guards

A guard that has never failed is not evidence (`AD` No Self-Verifying Scripts). Each defect class
was re-injected into the live suite, the relevant guard run, and the file restored:

| Injected defect | Guard | Result |
|---|---|---|
| `FA-13` renamed back to a duplicate `FA-05` | `TestDurableRuleIdUniqueness` | **CAUGHT** |
| `AD-27` link reverted to `file:///c:/GitDev/...` | `TestLinkPortability` | **CAUGHT** |
| A JSON Schema block re-appended to `governance-schemas.md` | `TestNoReEmbeddedUpstreamSchema` | **CAUGHT** |
| `AD-08` pointer changed to the non-existent `WP-99` | `TestCanonicalPointerIntegrity` | **CAUGHT** |

All four fired; all four files were restored and re-verified green.

### 3.3 Single-gate self-sufficiency

The behavioral acceptance criterion from [00-master-matrix.md](00-master-matrix.md) §5 — an agent
routed by one `<informatics>` gate must execute that domain without following a pointer — is
checked per module in the M01–M06 `Behavioral Check` tables and enforced mechanically by
`test_cis_01`–`test_cis_05`, which remain green.

## 4. Forensic Report

### Observation

9 defects (**D1**–**D9**) confirmed by direct inspection, 8 fixed and 1 (**D8**) deliberately
declined. 25 ledger entries applied across 7 live files plus `standard.md`, `.claude/rules/informatics.md`,
and 2 test files. Suite measures 804 lines / 16,194 tokens against a 933 / 17,001 baseline.
Validator 0/0 with advisories 13→12; pytest 185→196 passing.

### Logic Chain

1. Direct inspection — not inference — found that `governance-schemas.md` restated ~95 of its 264
   lines from `FA`, `WP`, and `EM`, and that two of those restatements **contradicted** their
   originals (**D2**, **D9**).
2. External research established the asymmetry that drove every decision: redundancy costs tokens
   and some interference ([Instruction Stacking Collapse](https://arxiv.org/pdf/2608.02639)), but
   *contradiction* produces the sharp compliance declines ([IHEval](https://aclanthology.org/2025.naacl-long.425.pdf)).
3. The router loads exactly one module per task, and `test_cis_01`–`cis_05` assert that isolation.
   So pointer-ifying short rules would convert one file read into two on the most common tasks.
4. Therefore: delete duplicated **blocks**, retain duplicated **rules** with their wording bound to
   a named owner. 85% of recoverable tokens were in six blocks; one of them (**D9**) was 93 lines.
5. The absence of a rule forbidding cross-file copying is what produced **D2**, **D6** and **D9**
   independently. `WP-23` closes that; the patches are the one-time repair, the rule is the durable
   fix, and the invariant tests make it enforceable rather than aspirational.

### Caveats

- **The token result is well under projection.** [01](01-system-wide-overlap-and-token-audit.md) §5
  projected −13%; measured is −5%. Decomposed: duplication removal −1,429 tokens, ownership
  relocation into `WP` +290, three new rules +255, `EM`/`AD` marker text +77. The projection was
  built before `WP-23`/`24`/`25` existed and before the **D4** topology fix was known to *add*
  lines. Pure deduplication delivered ≈ **−1,139 tokens (−6.7%)**; the suite then deliberately spent
  ≈332 of those on new capability. Reporting the net as if it were all compression would misstate it.
- **`writing-profile.md` grew 24%.** Intended: one canonical tier table at +290 tokens replaced two
  duplicates worth −420, and the file gained three rules. Per-file movement is not the metric.
- **`execution-modes.md` is the largest file and was barely touched.** Its bulk is worked examples
  mandated by `WP-17` and asserted by ~20 test literals. Compressing it would trade behavior for a
  few hundred tokens. See [M04](modules/M04-execution-modes.md) §2.
- **The router is byte-identical to baseline.** It sat exactly at its 500-token ceiling, so the Q3
  provenance note was applied and then reverted rather than relaxing a tested gate. Reasoning in
  [M01](modules/M01-routers-and-index.md) §3.
- **`estimate_tokens` is a ~4-chars-per-token heuristic**, not a tokenizer. It is consistent across
  before and after, so the deltas are sound, but absolute figures are approximate.
- **D5 was overstated in the original register** and is corrected in
  [M02](modules/M02-writing-profile.md) §3: the `GS` catalog already matched the validator; only the
  target-versus-gate relationship was unstated.
- **8 items deferred** to [03-research-backlog](03-research-backlog-and-open-questions.md),
  including `RBL-07`, a plaintext credential in a tracked file that is outside this pass's scope and
  needs operator action.

### Conclusion

The suite is ready. Every live rule has a named owner, every cross-file restatement is explicitly
bound to that owner, the two contract contradictions are resolved, and the specification no longer
publishes a weaker patch contract than the tool enforces. The compression is real but modest; the
correctness repair is the material outcome, and `WP-23` plus the four mutation-tested guards are
what stop the defect class from recurring.

### Verification Method

```bash
python apex-meta/scripts/okf_validator.py --target apex-meta/informatics   # expect 0 | 0
python -m pytest apex-meta/informatics/tests/ -q                           # expect 196 passed
python -m pytest apex-meta/informatics/tests/test_canonical_ownership.py -v # the 4 guard classes
git diff 6b7f54ee -- apex-meta/informatics/                                # every applied patch
```

Invalidation conditions: any `OKF_ERROR` or `APEX_PROFILE_ERROR`; any guard class in
`test_canonical_ownership.py` failing; a `Canonical:` marker resolving to an undefined rule; or a
module failing its single-gate self-sufficiency check in the M01–M06 behavioral tables.
