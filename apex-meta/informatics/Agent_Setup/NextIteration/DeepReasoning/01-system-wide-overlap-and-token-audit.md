---
type: Reference
id: DR-OVERLAP-AUDIT-v1.0
title: System-Wide Overlap Map & Token Compression Audit
description: Concept-to-canonical-owner map for every repeated concept in the live Apex Informatics suite, with duplication sites, compression treatment, and the before/after token scorecard.
status: current
tags: [research, overlap, deduplication, token-audit, ownership]
---

# System-Wide Overlap Map & Token Compression Audit

**Bottom line:** 85% of the recoverable tokens sit in **six duplicated blocks**, not in the 96 rule
statements. The largest single item — a 93-line JSON schema copied into `governance-schemas.md` —
has already drifted from the authoritative file it copies, making it a correctness defect rather
than a size problem.

## 1. Why "pointer-ify every duplicate" was rejected

The original plan treated all ~18 repeated concepts as merge candidates. Direct measurement
rejected that:

| Duplicate class | Example | Cost of the duplicate | Benefit of the duplicate |
|---|---|---:|---|
| Short rule restated | `WP-04` / `AD-19` grounding | ~22 tokens | Module stays self-sufficient under single-gate JIT routing |
| Block restated | `GS` §2.1 frontmatter YAML vs `FA` §3 | ~380 tokens | None — and the two copies **contradict** each other |

The `<informatics>` gates route a task to **exactly one** module, and
`test_tier5_adversarial.py` (`test_cis_01`–`test_cis_05`) asserts that no sibling module loads.
Replacing a short rule with a bare pointer therefore converts a one-file read into a two-file read
for the most common tasks — spending more tokens than it saves while adding a hop.

External evidence agrees on the direction but not on indiscriminate removal: instruction
interference research finds that stacking instructions collapses compliance through *interference*,
and that **conflicting** instructions produce the sharp declines
([Instruction Stacking Collapse](https://arxiv.org/pdf/2608.02639),
[IHEval](https://aclanthology.org/2025.naacl-long.425.pdf)). Contradiction is the expensive failure
mode; benign restatement of a one-line invariant is not.

**Resulting policy:** delete duplicated **blocks** (≥8 lines: schemas, tables, JSON, catalogs,
worked examples). Retain duplicated **rules** (≤2 lines) but force their wording into agreement
with the designated owner, so restatement never becomes contradiction.

## 2. Canonical Ownership Map

### 2.1 Block-level duplicates — `MERGE_DUPLICATE`

| # | Block | Owner (keeps full) | Deleted from | Lines cut |
|---|---|---|---|---:|
| B1 | `patch_intent.v1` JSON Schema | **External file** `patch-intent-schema.json` — `GS` §2.2 keeps the operative contract + link | `GS` §2.2 inline copy | ~80 |
| B2 | Root-index + concept frontmatter YAML contracts | **`FA`** §3 (`FA-05`, `FA-06`) | `GS` §2.1 contracts | ~25 |
| B3 | Priority tier table + raw 3-metric dimensions | **`WP`** §1 (`WP-07`) | `FA` §5, `GS` §3.2 | ~26 |
| B4 | Q&A data dictionary + bake-off phase list | **`EM`** §2.1, §3.1 | `GS` §2.3 | ~15 |
| B5 | Plane token orientations | **`FA`** §2 plane table (column already exists) | `FA-12` bullet list | ~6 |
| B6 | Module descriptions | **`index`** §2 gate payloads | `index` §3 repeated descriptions | ~6 |

> **B1 rationale — ownership moves out of the bundle.** `GS` §5 already cites
> [patch-intent-schema.json](file:///c:/GitDev/apexai-os-meta/.claude/skills/deterministic-markdown-patcher2/references/patch-intent-schema.json)
> as the "Patch Intent Source Schema" while simultaneously embedding a full copy of it. A spec that
> names an upstream source and then restates it has created a drift channel, and the drift already
> happened (see **D9** in §4). The authoritative JSON is what the patcher skill validates against;
> the spec's job is to state the *contract*, not to mirror the artifact.

> **B2 rationale — owner is the authoring surface, not the validation surface.** `FA` is what the
> `file_creation_or_structure` gate loads, which is precisely when an agent needs frontmatter
> inline. Giving the schema to `GS` would force a second file load on the single most common
> authoring task. `GS` keeps what only `GS` has: the concept-type table, the diagnostics catalog,
> and the conformance gate.

> **B3 rationale.** The tier definitions are needed when *authoring a rule tag*, which is the
> writing profile's domain. `WP-07` already owns the syntax; it absorbs the semantics.

### 2.2 Rule-level duplicates — `CROSS_LINK` (retained, wording aligned)

| Concept | Owner | Aligned restatements |
|---|---|---|
| Substance Over Ceremony | `WP-01` | `FA-04`, `AD-08`, `index` §1, router §1 |
| Top-loaded primacy | `WP-06` | `FA-02`, `GS-03` |
| Durable IDs | `WP-15` | `FA-07`, `GS-08` |
| Universal instruction parsimony | `WP-18` | `FA-12`, `GS-14`, `AD-26` |
| Residual name eradication | `AD-15` | `WP-08`, `FA-09` |
| Primary grounding | `AD-19` | `WP-04` |
| Command-carrying claims | `AD-20` | `WP-16` |
| Minto BLUF | `WP-12` | `AD-17` |
| Whole-file rewrite prohibition | `EM-01` | `AD-03`, `GS-02`, `index` §1, router §1 |
| Step-by-step context | `EM-03` | `AD-04`, `index` §1, router §1 |
| TARGET dominance | `AD-01` | `EM-04`, `index` §1, router §1 |
| Two-strike pivot | `AD-02` | `EM-05` |
| Checkable ambiguity | `EM-02` | `AD-06` |
| Reuse before build | `AD-11` | `EM-07` trigger clause |
| Flat YAML frontmatter | `FA` (`FA-13` after renumber) | `GS-05` |
| Sub-bundle boundary | `FA-08` | `GS-22` |
| No default-behavior rules | `WP-20` | `GS-16` → delete (GS is not an authoring surface) |

### 2.3 Intra-file duplicates — `COLLAPSE_INTRA`

| Site | Finding |
|---|---|
| `GS-04` + `GS-18` | Same rule — raw 3-metric tagging — stated twice in one file (**D6**) |
| `GS-17` + `GS-19` | Tier classification and sort order; fold into the single `WP-07`-aligned restatement |
| `FA` §2 table + `FA-12` | Plane token orientations listed twice in one file (**B5**) |

Intra-file duplication has no isolation benefit whatsoever and matches a defect pattern the
operator's own prior forensic review already named — *"Internal duplication inside `AGENTS.md`'s own
Git-and-branches section (the preserve-dirty-files rule and the packet-authority rule each stated
twice in the same file)"* ([2Dos Ai Instructions.md:144-145](file:///c:/GitDev/apexai-os-meta/apex-meta/AI-Snippets/Orga/2Dos%20Ai%20Instructions.md)).

## 3. Precedent: the operator's own prior design used this model

The canonical-owner-plus-pointer treatment is not imported from outside. The prior forensic
analysis of the `CLAUDE.md` / `AGENTS.md` stack resolved its duplicate "Single source of truth"
section by making it *"owned here, pointer-only in `AGENTS.md`"*
([2Dos Ai Instructions.md:235](file:///c:/GitDev/apexai-os-meta/apex-meta/AI-Snippets/Orga/2Dos%20Ai%20Instructions.md)),
and diagnosed the root cause of instruction bloat as a **placement defect** — content sitting in an
always-loaded file when it is only relevant to one task domain (lines 116-121). The same document
records the operator's direct complaint about this suite's ancestor: *"too much overlap"* (line 28).

`Snippets.md` states the governing principle outright: **"Reuse existing instructions instead of
restating them. Prefer one direct rule over a defensive procedure."**
([Snippets.md:60-61](file:///c:/GitDev/apexai-os-meta/apex-meta/AI-Snippets/Snippets.md)). That
directive is **not currently codified anywhere in the live suite** — see new rule `WP-23` in
[02-new-rules-discovery-and-qa-bakeoff.md](02-new-rules-discovery-and-qa-bakeoff.md).

## 4. Defect D9 — schema drift (discovered during this audit)

| | |
|---|---|
| **ID** | **D9** `[P0 | I94/E100/R08]` |
| **Defect** | `governance-schemas.md` §2.2 embeds a 93-line copy of `patch-intent-schema.json` that has already diverged from the authoritative file |
| **Divergence** | Inline copy omits `$id`, flattens the `$defs` indirection, and **drops every `maxLength` bound the real schema enforces** (`target_file_guess` ≤500, `heading_path` items ≤200, `nearby_phrases` items ≤300) |
| **Equivalent parts** | `required` fields, the 9-value `operation` enum, and all four `safety` const invariants match |
| **Consequence** | An agent authoring a patch intent from the specification can emit a document the actual patcher rejects — the spec is a weaker contract than the tool |
| **Evidence** | `json.loads` of both, structural diff = 482 lines; command recorded in [04](04-consolidated-patch-and-verification.md) |
| **Fix** | `GS` §2.2 states the operative contract (required fields, operation enum, four safety invariants) in ~12 lines and links the authoritative JSON as the single source |

This raises the register to **D1–D9**; [00-master-matrix.md](00-master-matrix.md) §4 carries D1–D8.

## 5. Token Scorecard

Baseline measured at commit `6b7f54ee`. Projected column is the arithmetic consequence of §2;
the **measured after** column is filled in Iteration 4 and governs.

| File | Baseline lines | Baseline tokens | Projected after | Projected Δ | Measured after |
|---|---:|---:|---:|---:|---:|
| `index.md` | 60 | 994 | ~940 | −5% | *pending* |
| `general-informatics-router.md` | 43 | 500 | ~510 | +2% | *pending* |
| `writing-profile.md` | 79 | 2,300 | ~2,480 | +8% | *pending* |
| `file-architecture.md` | 170 | 2,543 | ~2,250 | −12% | *pending* |
| `execution-modes.md` | 242 | 4,144 | ~4,060 | −2% | *pending* |
| `anti-drift-rules.md` | 75 | 2,452 | ~2,400 | −2% | *pending* |
| `governance-schemas.md` | 264 | 4,068 | ~2,100 | **−48%** | *pending* |
| **Total** | **933** | **17,001** | **~14,740** | **−13%** | *pending* |

`writing-profile.md` and the router **grow**. That is the intended consequence of consolidating
ownership: the tier table has to live somewhere, and one canonical copy at +180 tokens replaces two
duplicates at −420. Net suite movement is what matters, not per-file movement.

## 6. What is deliberately **not** deduplicated

| Retained duplication | Reason |
|---|---|
| Router ≈ `index.md` §1/§2/§5 | The router is a deliberate embeddable artifact for *other* repositories' root instruction surfaces. Resolved in [02](02-new-rules-discovery-and-qa-bakeoff.md) Q3 — the fix is to *declare* the derivation, not remove it. |
| 4 P0 invariants in both `index.md` and modules | Primacy research shows mid-file rules lose substantial compliance; the dispatch surface restating four invariants is cheap insurance, not waste. |
| `EM` §2.2 canonical decision-matrix example | A worked example is not a duplicate of the rule it illustrates. `WP-17` explicitly mandates it. |
| `standard.md` §3 Five-Plane vs `FA` §3 | Out of scope by operator decision — resolved by a precedence note, not a rewrite. |
