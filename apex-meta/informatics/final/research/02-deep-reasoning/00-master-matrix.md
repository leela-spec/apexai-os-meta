---
type: Reference
id: DR-MASTER-MATRIX-v1.0
title: Informatics Suite Master Matrix & Defect Register
description: Meta-layer inventory of the live Apex Informatics suite, rule-level audit matrix across all 96 governed rules, and the confirmed defect register driving the compression pass.
status: current
tags: [research, master-matrix, audit, defect-register]
---

# Informatics Suite Master Matrix & Defect Register

**Bottom line:** the live suite is structurally sound. Its waste is concentrated in roughly
eight duplicated *blocks* (schemas, tables, JSON, catalogs), not in its rule text — and in three
places the duplicates have drifted into outright contradiction.

## 1. System Inventory (measured baseline)

Measured at baseline commit `6b7f54ee` by reusing `estimate_tokens` from the live test suite
(`AD-11` reuse-before-build). Command in [04-consolidated-patch-and-verification.md](04-consolidated-patch-and-verification.md).

| File | Lines | Bytes | Tokens | Rule IDs | Role after pass |
|---|---:|---:|---:|---|---|
| `index.md` | 60 | 3,996 | 994 | — (7 untagged bullets) | Canonical dispatch surface |
| `general-informatics-router.md` | 43 | 2,000 | 500 | — (7 untagged bullets) | Declared embeddable derivative of `index.md` |
| `writing-profile.md` | 79 | 9,212 | 2,300 | `WP-01..22` | **Owner:** prose, ranking syntax, P0–P3 tiers |
| `file-architecture.md` | 170 | 10,240 | 2,543 | `FA-01..12` | **Owner:** planes, topology, frontmatter schemas |
| `execution-modes.md` | 242 | 16,641 | 4,144 | `EM-01..12` | **Owner:** task adapters, Q&A/bake-off format |
| `anti-drift-rules.md` | 75 | 9,813 | 2,452 | `AD-01..28` | **Owner:** drift laws, operational discipline |
| `governance-schemas.md` | 264 | 16,315 | 4,068 | `GS-01..22` | **Owner:** `patch_intent.v1`, diagnostics catalog |
| **Total (governed)** | **933** | **68,217** | **17,001** | **96 rules** | — |

Out of scope for compression but in the bundle: `standard.md` (159L / 2,143T — precedence note
only), `migration.md` (29L), `log.md` (5L).

> **Correction to the plan's arithmetic:** the suite carries **96** tagged rules
> (22+12+12+28+22), not 84. The matrix below covers all 96.

## 2. Verdict Vocabulary

The plan's original verdict set treated every duplicate as a merge candidate. Direct measurement
rejected that: a 1-line rule restated in two files costs ~10–25 tokens and *buys* single-module
JIT self-sufficiency, while a 25-line schema restated in two files costs ~400 tokens and buys
nothing. Verdicts are therefore value-graded:

| Verdict | Meaning | Applied when |
|---|---|---|
| `KEEP` | Unique, correctly placed, no change | Rule has one home and reads cleanly |
| `KEEP_CANONICAL` | This file owns the full treatment of a shared concept | Owner designated in [01-overlap audit](01-system-wide-overlap-and-token-audit.md) |
| `CROSS_LINK` | Short duplicate retained for JIT self-sufficiency; wording aligned to owner | Duplicate is ≤2 lines and the hosting module genuinely needs it standalone |
| `MERGE_DUPLICATE` | Duplicated **block** (≥8 lines) deleted; 1-line operative rule + link remains | Schemas, tables, JSON, catalogs, worked examples |
| `COLLAPSE_INTRA` | Same rule stated twice inside one file; fold into one | Pure waste, no isolation benefit |
| `FIX_DEFECT` | Carries a confirmed defect from §4 | See Defect Register |
| `CHALLENGE` | Rule's value or placement is genuinely questionable | Resolved via Q&A matrix in [02-bake-off](02-new-rules-discovery-and-qa-bakeoff.md) |

## 3. Rule-Level Master Matrix

### 3.1 `writing-profile.md` — `WP-01..22` → [M02](modules/M02-writing-profile.md)

| ID | Tag | Summary | Verdict |
|---|---|---|---|
| WP-01 | P0 I98/E98/R05 | Substance Over Ceremony; authority to exceed ceilings | `KEEP_CANONICAL` |
| WP-02 | P0 I96/E95/R08 | One imperative command per procedural sentence | `KEEP` |
| WP-03 | P0 I95/E96/R05 | Imperative verbs; zero modal hedging | `KEEP` |
| WP-04 | P0 I95/E98/R05 | Ground assertions in primary inspection | `CROSS_LINK` → `AD-19` |
| WP-05 | P0 I94/E95/R07 | Clear active voice with explicit actors | `KEEP` |
| WP-06 | P0 I94/E97/R06 | Top-loaded positional primacy (~500 tokens) | `KEEP_CANONICAL` |
| WP-07 | P0 I93/E95/R07 | Raw 3-metric ranking, unaggregated | `KEEP_CANONICAL` (absorbs tier table) |
| WP-08 | P0 I92/E95/R06 | Stale residual eradication | `CROSS_LINK` → `AD-15` |
| WP-09 | P0 I92/E95/R08 | Adaptive scope boundary (governed artifacts only) | `KEEP` |
| WP-10 | P1 I92/E95/R08 | Information Mapping, one chunk one job | `KEEP` |
| WP-11 | P1 I91/E94/R08 | Table vs list vs prose selection | `KEEP` |
| WP-12 | P1 I90/E94/R08 | Minto BLUF | `KEEP_CANONICAL` |
| WP-13 | P1 I89/E92/R10 | Visual block prose orientation (~150 words) | `KEEP` |
| WP-14 | P1 I88/E92/R10 | Concise sentence orientation (~20–25 words) | `FIX_DEFECT` **D5** |
| WP-15 | P1 I91/E93/R08 | Tier-agnostic durable IDs | `KEEP_CANONICAL` |
| WP-16 | P1 I89/E92/R08 | Command-carrying claims | `CROSS_LINK` → `AD-20` |
| WP-17 | P2 I86/E90/R08 | High-signal compact examples | `KEEP` |
| WP-18 | P2 I85/E90/R10 | Universal instruction parsimony (~30–50 directives) | `KEEP_CANONICAL` |
| WP-19 | P2 I84/E92/R08 | Syntax exemptions from word counts | `KEEP` |
| WP-20 | P2 I82/E88/R08 | No default-behavior rules | `KEEP_CANONICAL` |
| WP-21 | P2 I80/E86/R10 | Heading depth orientation (~3 levels) | `KEEP` |
| WP-22 | P3 I72/E80/R10 | Non-normative appendix & typographic cleanliness | `KEEP` |

| **WP-23** | P1 I90/E92/R08 | **NEW** — Single-owner instruction reuse; never copy a canonical block | `ADD` |
| **WP-24** | P2 I82/E90/R06 | **NEW** — Clickable file references when listing files | `ADD` |
| **WP-25** | P2 I80/E86/R06 | **NEW** — Terminal-position operative content (recency slot) | `ADD` |

Non-rule content: §5 "Future Architecture Note" is speculative roadmap inside a live spec —
`CHALLENGE`, relocated to [03-backlog](03-research-backlog-and-open-questions.md) `RBL-03`.

The three additions are specified in
[02-new-rules-discovery-and-qa-bakeoff.md](02-new-rules-discovery-and-qa-bakeoff.md) §4. `WP-23` is
the rule whose absence produced defects **D2**, **D6** and **D9**; adding it is the durable fix,
while the patches are the one-time repair.

### 3.2 `file-architecture.md` — `FA-01..12` → [M03](modules/M03-file-architecture.md)

| ID | Tag | Summary | Verdict |
|---|---|---|---|
| FA-01 | P0 I95/E95/R08 | Strict current-truth separation | `KEEP_CANONICAL` |
| FA-02 | P0 I95/E92/R08 | Top-loaded attention primacy | `CROSS_LINK` → `WP-06` |
| FA-03 | P0 I92/E90/R12 | Five-plane information separation | `KEEP_CANONICAL` |
| FA-04 *(1st)* | P0 I98/E98/R05 | Substance Over Ceremony exception authority | `FIX_DEFECT` **D1** + `CROSS_LINK` → `WP-01` |
| FA-04 *(2nd)* | P1 I90/E95/R10 | Flat/inline YAML frontmatter serialization | `FIX_DEFECT` **D1** (renumber) |
| FA-05 | P1 I88/E92/R12 | Root index specification | `KEEP_CANONICAL` + `FIX_DEFECT` **D2** |
| FA-06 | P1 I88/E92/R12 | Concept document specification | `KEEP_CANONICAL` + `FIX_DEFECT` **D2** |
| FA-07 | P1 I85/E88/R15 | Unique durable identifiers | `CROSS_LINK` → `WP-15` |
| FA-08 | P1 I85/E90/R15 | Sub-bundle isolation boundary | `KEEP_CANONICAL` |
| FA-09 | P1 I82/E85/R18 | Residual name eradication | `CROSS_LINK` → `AD-15` |
| FA-10 | P2 I78/E82/R20 | Single-purpose topic files | `KEEP` |
| FA-11 | P2 I75/E80/R18 | Dedicated changelog allocation | `KEEP` |
| FA-12 | P2 I82/E88/R10 | Plane token orientations + parsimony | `COLLAPSE_INTRA` (numbers already in §2 table) |

Non-rule content: §4 topology tree `FIX_DEFECT` **D4**; §5 significance architecture
`MERGE_DUPLICATE` → `WP-07`.

### 3.3 `execution-modes.md` — `EM-01..12` → [M04](modules/M04-execution-modes.md)

| ID | Tag | Summary | Verdict |
|---|---|---|---|
| EM-01 | P0 I98/E96/R05 | Whole-file rewrite prohibition | `KEEP_CANONICAL` |
| EM-02 | P0 I96/E95/R05 | Handover non-paralysis | `KEEP_CANONICAL` |
| EM-03 | P0 I96/E95/R06 | Step-by-step context & file iteration | `KEEP_CANONICAL` |
| EM-04 | P0 I95/E95/R08 | Target dominance | `CROSS_LINK` → `AD-01` |
| EM-05 | P0 I94/E92/R10 | Two-strike pivot rule | `CROSS_LINK` → `AD-02` |
| EM-06 | P1 I92/E94/R10 | Conditional Q&A trigger | `KEEP_CANONICAL` (owns matrix format) |
| EM-07 | P1 I88/E90/R12 | Conditional bake-off trigger | `KEEP_CANONICAL` (owns 4-phase rubric) |
| EM-08 | P1 I98/E96/R05 | Conditional patch trigger + Mode A/B | `KEEP_CANONICAL` |
| EM-09 | P1 I92/E95/R08 | Conditional handover trigger | `KEEP` |
| EM-10 | P1 I95/E95/R08 | Route 0/1/2 iterative & MMM trigger | `KEEP` |
| EM-11 | P2 I82/E86/R12 | Upward invalidation rule | `KEEP` |
| EM-12 | P2 I80/E90/R08 | Conditional sync trigger & file preservation | `KEEP` |

Largest file in the suite (4,144T) but the lowest duplication density: its bulk is the canonical
worked examples and the `IF`-dispatch block, all of which are load-bearing. Expect small savings.

### 3.4 `anti-drift-rules.md` — `AD-01..28` → [M05](modules/M05-anti-drift-rules.md)

| ID | Tag | Summary | Verdict |
|---|---|---|---|
| AD-01 | P0 I100/E95/R05 | TARGET dominance | `KEEP_CANONICAL` |
| AD-02 | P0 I98/E95/R05 | Two-strike subsystem rule | `KEEP_CANONICAL` |
| AD-03 | P0 I98/E96/R05 | Whole-file rewrite prohibition | `CROSS_LINK` → `EM-01` |
| AD-04 | P0 I96/E95/R05 | Step-by-step context & file iteration | `CROSS_LINK` → `EM-03` |
| AD-05 | P0 I96/E95/R05 | Operator challenge boundary | `KEEP` |
| AD-06 | P0 I96/E95/R05 | Checkable ambiguity resolution | `CROSS_LINK` → `EM-02` |
| AD-07 | P0 I95/E95/R05 | Sunk-cost prohibition | `KEEP` |
| AD-08 | P0 I95/E95/R05 | Substance Over Ceremony exception authority | `CROSS_LINK` → `WP-01` |
| AD-09 | P0 I95/E95/R08 | Stop on drift | `KEEP` |
| AD-10 | P0 I95/E94/R08 | Product before infrastructure | `KEEP` |
| AD-11 | P0 I95/E92/R08 | Reuse before build | `KEEP_CANONICAL` |
| AD-12 | P0 I94/E92/R08 | Product advancement | `KEEP` |
| AD-13 | P0 I92/E90/R10 | Evidence proportionality | `KEEP` |
| AD-14 | P1 I94/E95/R08 | Gall's Law & single flat artifact | `KEEP` |
| AD-15 | P1 I93/E95/R05 | Residual name eradication | `KEEP_CANONICAL` |
| AD-16 | P1 I93/E95/R07 | Pre-existing red vs regression boundary | `KEEP` |
| AD-17 | P1 I93/E94/R07 | Minto BLUF directive | `CROSS_LINK` → `WP-12` |
| AD-18 | P1 I92/E93/R08 | Zero-speculation scope boundary | `KEEP` |
| AD-19 | P1 I91/E96/R05 | Primary grounding vs secondary citation | `KEEP_CANONICAL` |
| AD-20 | P1 I90/E94/R06 | Command-carrying claims | `KEEP_CANONICAL` |
| AD-21 | P1 I90/E92/R08 | Balanced viable path | `KEEP` |
| AD-22 | P2 I88/E91/R08 | Surgical edits & anti-overcorrection | `KEEP` |
| AD-23 | P2 I87/E92/R08 | Asset preservation & deterministic moves | `KEEP` |
| AD-24 | P2 I86/E90/R08 | Two-strike tracker mechanics | `KEEP` |
| AD-25 | P2 I85/E90/R09 | Pre-addition gate rule | `KEEP` |
| AD-26 | P2 I85/E90/R10 | Universal instruction parsimony | `CROSS_LINK` → `WP-18` |
| AD-27 | P2 I84/E89/R08 | Sibling module linkage | `CHALLENGE` (absolute `file:///` links) |
| AD-28 | P3 I68/E82/R10 | Objective run outcome classification | `KEEP` |

Highest rule density in the suite (28 rules / 2,452T) and already near-optimally compressed —
~88 tokens per rule. The `AD-26` parsimony ceiling (~30–50 directives) is itself under pressure
here: `CHALLENGE` logged to [03-backlog](03-research-backlog-and-open-questions.md).

### 3.5 `governance-schemas.md` — `GS-01..22` → [M06](modules/M06-governance-schemas.md)

| ID | Tag | Summary | Verdict |
|---|---|---|---|
| GS-01 | P0 I98/E98/R05 | Mandatory schema conformance | `KEEP` |
| GS-02 | P0 I98/E96/R05 | Prohibited whole-file patch rewrites | `CROSS_LINK` → `EM-01` |
| GS-03 | P0 I96/E95/R05 | Top-loaded attention primacy | `CROSS_LINK` → `WP-06` |
| GS-04 | P0 I95/E95/R06 | Raw 3-metric significance tagging | `COLLAPSE_INTRA` with `GS-18` (**D6**) |
| GS-05 | P0 I94/E96/R06 | Flat YAML frontmatter serialization | `CROSS_LINK` → `FA` |
| GS-06 | P1 I92/E95/R08 | Root index schema | `MERGE_DUPLICATE` → `FA-05` (**D2**) |
| GS-07 | P1 I92/E95/R08 | Concept document schema | `MERGE_DUPLICATE` → `FA-06` (**D2**) |
| GS-08 | P1 I90/E94/R07 | Bundle-wide durable ID uniqueness | `CROSS_LINK` → `WP-15` |
| GS-09 | P1 I96/E96/R05 | Deterministic AST patch intent spec | `KEEP_CANONICAL` |
| GS-10 | P1 I95/E95/R05 | AST safety threshold invariants | `KEEP_CANONICAL` |
| GS-11 | P1 I93/E94/R06 | Prohibited brittle identifiers | `KEEP_CANONICAL` |
| GS-12 | P1 I90/E92/R10 | Structured decision matrix protocol | `MERGE_DUPLICATE` → `EM-06` |
| GS-13 | P1 I88/E90/R12 | 4-phase comparison bake-off rubric | `MERGE_DUPLICATE` → `EM-07` |
| GS-14 | P2 I88/E92/R08 | Universal instruction parsimony | `CROSS_LINK` → `WP-18` |
| GS-15 | P2 I86/E90/R08 | Directive accounting separation | `KEEP` (unique) |
| GS-16 | P2 I84/E88/R08 | No default-behavior rules | `MERGE_DUPLICATE` → `WP-20` |
| GS-17 | P2 I90/E94/R08 | Priority tier classification | `MERGE_DUPLICATE` → `WP-07` |
| GS-18 | P2 I92/E95/R06 | Raw 3-metric tagging syntax | `COLLAPSE_INTRA` into `GS-04` (**D6**) |
| GS-19 | P2 I88/E92/R08 | Descending priority sort order | `MERGE_DUPLICATE` → `WP-07` |
| GS-20 | P3 I80/E88/R10 | Tri-class diagnostic classification | `KEEP_CANONICAL` |
| GS-21 | P3 I82/E89/R08 | Deterministic conformance gate | `KEEP_CANONICAL` |
| GS-22 | P3 I75/E82/R10 | Sub-bundle boundary pruning | `CROSS_LINK` → `FA-08` |

**Highest-waste file.** Of 264 lines, roughly 95 restate `FA`, `WP`, or `EM` content — including
two YAML contracts that *contradict* their `FA` counterparts. Its genuinely unique assets are the
`patch_intent.v1` JSON schema (93 lines), the concept-type table, and the diagnostic catalog.

### 3.6 `index.md` & `general-informatics-router.md` → [M01](modules/M01-routers-and-index.md)

Neither file carries durable rule IDs; both carry 4 P0 invariant bullets, 5 `<informatics>`
dispatch gates, and 3 sizing bullets. The router reproduces `index.md` §1, §2 and §5 almost
verbatim at ~500 tokens.

| Element | Verdict |
|---|---|
| `index.md` §1 invariants (4) | `KEEP` — dispatch surface needs them standalone |
| `index.md` §2 dispatch gates (5) | `KEEP_CANONICAL` |
| `index.md` §3 module list | `MERGE_DUPLICATE` — descriptions restate the gate payloads |
| `index.md` §4 supporting governance | `KEEP` (link integrity depends on it) |
| `index.md` §5 sizing bullets (3) | `KEEP` |
| `index.md` frontmatter | `FIX_DEFECT` **D3** |
| Router (whole file) | `CHALLENGE` — resolved in [02-bake-off](02-new-rules-discovery-and-qa-bakeoff.md) Q3 |

## 4. Defect Register

Confirmed by direct file inspection, not inference. Each is fixed in Iteration 3 regardless of
research outcomes.

| ID | Severity | Defect | Evidence | Owning module |
|---|---|---|---|---|
| **D1** | `P0` I95/E100/R05 | Duplicate durable ID `FA-04` across two unrelated rules | `file-architecture.md:28` and `:59` | [M03](modules/M03-file-architecture.md) |
| **D2** | `P0` I92/E100/R10 | Frontmatter contracts contradict: root `tags` present in GS absent in FA; concept `version` present in GS absent in FA | `file-architecture.md:71-107` vs `governance-schemas.md:39-60` | [M03](modules/M03-file-architecture.md) / [M06](modules/M06-governance-schemas.md) |
| **D3** | `P1` I80/E100/R05 | Root `index.md` omits `tags`, violating the contract the bundle publishes | `index.md:1-5` vs `GS-06` | [M01](modules/M01-routers-and-index.md) |
| **D4** | `P1` I85/E100/R08 | Bundle topology tree stale — omits 4 live files and `tests/`; violates its own `FA-09` | `file-architecture.md:118-129` | [M03](modules/M03-file-architecture.md) |
| **D5** | `P1` I78/E100/R10 | Sentence-length orientation stated three ways: `~20–25` / `~30` / `25-30` | `writing-profile.md:36`, `governance-schemas.md:255`, `okf_validator.py` | [M02](modules/M02-writing-profile.md) / [M06](modules/M06-governance-schemas.md) |
| **D6** | `P2` I70/E100/R05 | `GS-04` and `GS-18` state the same rule inside one file | `governance-schemas.md:24` and `:218` | [M06](modules/M06-governance-schemas.md) |
| **D7** | `P1` I88/E95/R12 | Dual-authority conflict: `.claude/rules/informatics.md` names `standard.md` as overriding canon | `.claude/rules/informatics.md`, `standard.md:36-45` | [M01](modules/M01-routers-and-index.md) |
| **D8** | `P3` I55/E100/R05 | `estimate_tokens` duplicated verbatim across both test files | `test_informatics_e2e.py:104`, `test_tier5_adversarial.py:62` | [M06](modules/M06-governance-schemas.md) / Iteration 4 |
| **D9** | `P0` I94/E100/R08 | Inline `patch_intent.v1` schema copy has **drifted** from the authoritative JSON — omits `$id`/`$defs` and drops every `maxLength` bound the real schema enforces | `governance-schemas.md:83-175` vs `.claude/skills/deterministic-markdown-patcher2/references/patch-intent-schema.json` | [M06](modules/M06-governance-schemas.md) |

**D9 is the highest-value item in the pass.** It is simultaneously the suite's largest block
(93 lines / ~1,200 tokens), a correctness defect (the published contract is weaker than the enforced
one), and a standing drift channel. Discovery and analysis in
[01-system-wide-overlap-and-token-audit.md](01-system-wide-overlap-and-token-audit.md) §4.

### Correction to a handover premise

The handover requires OKF frontmatter on `DeepReasoning/index.md` "so `okf_validator.py`
recognizes `DeepReasoning/` as a self-contained sub-bundle boundary." That isolation **already
exists**: `okf_validator.py:206` prunes recursion at any directory owning an `index.md`, and
`Agent_Setup/index.md` is such a boundary three levels up. The frontmatter is retained for
navigation value, but it is not what keeps this research tree out of bundle validation.

## 5. Verification Criteria for Iterations 2–4

| Iteration | Output | Passes when | Result |
|---|---|---|---|
| 2 | `01`, `02`, `03` | Every repeated concept has exactly one designated owner; every structural decision has a Q&A matrix with raw `(I/E/R)`; every deferred question has an `RBL-XX` | ✅ 6 blocks + 17 rule concepts assigned; 8 matrices; `RBL-01..08` |
| 3 | `M01`–`M06` + applied patches | Every one of the 96 rules carries a verdict and a disposition; all defects fixed; patches applied by exact match, never whole-file rewrite | ✅ 25 ledger entries; 8 of 9 defects fixed, **D8** declined with reasoning |
| 4 | `04` + tests | Validator `0 OKF / 0 Apex`; pytest ≥185 passed plus new invariant tests; measured token delta reported per file; every changed test assertion justified in the ledger | ✅ 0/0, advisories 13→12; 196 passed; −129 lines / −807 tokens; 1 assertion changed and justified |

### Final measured outcome

| | Baseline | After | Δ |
|---|---:|---:|---:|
| Lines (7 governed files) | 933 | 804 | **−129 (−14%)** |
| Tokens | 17,001 | 16,194 | **−807 (−5%)** |
| Rules | 96 | 96 (+3 new, −3 retired) | — |
| Tests passing | 185 | 196 | **+11** |
| Validator | 0 / 0 / 13 advisories | 0 / 0 / 12 advisories | −1 advisory |

Pure deduplication delivered ≈ −1,139 tokens; ≈332 were deliberately re-spent on `WP-23`/`24`/`25`
and the canonical markers. Full decomposition in
[04-consolidated-patch-and-verification.md](04-consolidated-patch-and-verification.md) §4 Caveats.

**Behavioral acceptance (overrides token targets):** an agent routed by a single
`<informatics>` gate to exactly one module must still be able to execute that module's domain
without following any pointer. Any compression that breaks this is reverted — `WP-01` governs.
