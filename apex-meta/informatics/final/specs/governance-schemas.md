---
type: Governance
id: GOV-SCHEMAS-v0.2
title: Apex Governance Schemas & Directive Ceilings Specification
description: Canonical specification governing OKF v0.2 frontmatter schemas, AST patch intent schemas, decision matrix formats, model directive ceilings, and significance ranking.
status: current
version: "2.0.0"
tags: [governance, schemas, patch-intent, okf-v0.2, decision-matrix, directive-ceilings]
---

# Apex Governance Schemas & Directive Ceilings Specification

This specification establishes the authoritative schemas, machine-readable contracts, evaluation frameworks, and cognitive directive ceilings across Apex OS.

---

## 1. Critical Governance Invariants

All files, patches, and instructions governed by Apex Informatics satisfy these top-loaded invariants (aiming for roughly the first ~500 tokens):

- **GS-01 [P0 | I98/E98/R05] Mandatory Schema Conformance**: Every governed artifact must conform to its declared schema. Reject any artifact that contains unregistered fields, missing mandatory keys, or ungrounded claims.
- **GS-02 [P0 | I98/E96/R05] Prohibited Whole-File Patch Rewrites**: Never generate or apply full-file rewrites for existing files. Enforce surgical AST patch intents (`patch_intent.v1`) or exact-match search/replace blocks with unique surrounding context. Canonical: `EM-01`.
- **GS-03 [P0 | I96/E95/R05] Top-Loaded Attention Primacy**: Front-load critical P0 invariants near the beginning of every instruction and specification file (aiming for roughly the first ~500 tokens as a practical orientation) before attention density decays. Canonical: `WP-06`.
- **GS-04 [P0 | I95/E95/R06] Raw 3-Metric Significance Tagging**: Tag governed rules, options, and trade-offs with raw unaggregated 3-metric estimates `[P<tier> | I<impact>/E<evidence>/R<risk>]` on a 1–100 scale, keeping all three dimensions distinct. Never aggregate them into a composite score. Canonical: `WP-07`.
- **GS-05 [P0 | I94/E96/R06] Flat YAML Frontmatter Serialization**: Write all YAML frontmatter headers as flat key-value pairs or inline bracketed lists. Never use multiline hyphenated lists (`- item`), as they cause zero-dependency parsers to fail. Canonical: `FA-13`.

---

## 2. Core Governance Schemas & Contracts

This section defines the formal structural schemas for repository metadata, patch mutations, and trade-off evaluations.

### 2.1 OKF v0.2 Frontmatter Governance Schema

- **GS-06 [P1 | I92/E95/R08] Root Index Schema (`index.md`)**: Reject any bundle whose root index fails the canonical OKF v0.2 frontmatter contract in [file-architecture.md](file-architecture.md) `FA-05`. Enforce `okf_version: "0.2"` as the bundle-identity gate.
- **GS-07 [P1 | I92/E95/R08] Concept Document Schema (`*.md`)**: Reject any concept file lacking valid YAML frontmatter with a non-empty `type` and a bundle-unique `id` on line 1. The field-level contract is owned by `FA-06`.
- **GS-08 [P1 | I90/E94/R07] Bundle-Wide Durable ID Uniqueness**: Enforce unique, tier-agnostic durable identifiers across all documents within an OKF bundle. Duplicate IDs cause index collision and validator failure. Canonical ID grammar: `WP-15`.

#### Valid Concept Types:
| Type | Intended Scope | Example Target |
|---|---|---|
| `Specification` | Formal technical contracts, protocols, and data models | `file-architecture.md` |
| `Standard` | Repository-wide mandatory policies and conformance baselines | `standard.md` |
| `Profile` | Scoped formatting, prose ergonomics, and style rules | `writing-profile.md` |
| `Adapter` | Task-specific execution modes and operational workflows | `execution-modes.md` |
| `Governance` | Machine-readable schemas, validation contracts, and ceilings | `governance-schemas.md` |
| `Policy` | System migration, compliance, and deprecation policies | `migration.md` |
| `Reference` | Deep technical reference manuals, lexicons, and catalogues | `working-method.md` |

---

### 2.2 Patch Intent Schema (`patch_intent.v1`)

- **GS-09 [P1 | I96/E96/R05] Deterministic AST Patch Intent Specification**: Structure automated file mutations using the `patch_intent.v1` JSON Schema. Target edits by structural AST heading paths and context hints rather than volatile line numbers.
- **GS-10 [P1 | I95/E95/R05] AST Safety Threshold Invariants**: Enforce mandatory safety invariants on every patch intent: `require_unique_match: true`, `fail_on_ambiguity: true`, `allow_full_file_rewrite: false`, and `max_files_touched: 1`.
- **GS-11 [P1 | I93/E94/R06] Prohibited Brittle Identifiers**: Forbid `line_number`, `line_start`, `line_end`, `line_range`, `hunk`, and `unified_diff` within patch intents. Brittle line offsets cause silent patch corruption across concurrent edits.

#### `patch_intent.v1` Operative Contract:

The machine-readable schema is owned by
[patch-intent-schema.json](../../../../.claude/skills/deterministic-markdown-patcher2/references/patch-intent-schema.json),
which the deterministic patcher validates against. Never restate that schema here (`WP-23`) — an
embedded copy silently weakens into a different contract. Satisfy the following when authoring an
intent:

| Element | Contract |
|---|---|
| Envelope | `schema_version` must equal `"patch_intent.v1"`; `intents` is a non-empty array |
| Required per intent | `intent_id`, `operation`, `target`, `safety` |
| `intent_id` | Matches `^[a-z0-9][a-z0-9_-]{2,80}$` |
| `operation` | One of `inspect`, `locate`, `extract-span`, `replace-once`, `replace-heading-section`, `frontmatter-set`, `diff`, `apply-intent`, `validate-intent` |
| `target` | `target_file_guess` mandatory; locate by `heading_path` (≤12 levels) and `hints`, never by line offset |
| Safety invariants | `require_unique_match: true`, `fail_on_ambiguity: true`, `allow_full_file_rewrite: false`, `max_files_touched: 1` |
| Closed objects | Every object rejects unregistered fields (`additionalProperties: false`) |
| Bounded strings | The authoritative schema enforces length ceilings on paths, hints, and notes; keep hint phrases short and specific |

A conforming worked example is maintained in [execution-modes.md](execution-modes.md) §4.2.

---

### 2.3 Decision Matrix & Bake-Off Governance Schemas

- **GS-12 [P1 | I90/E92/R10] Structured Decision Matrix Protocol**: Reject a decision record that omits any mandatory field of the Q&A matrix — `Question`, ≥2 `Options` each carrying mechanism, `Grounding`, and a raw `(I/E/R)` tag, plus `Recommendation`, `Reasoning`, and one-line rejection `Notes`. Format owned by [execution-modes.md](execution-modes.md) §2.1.
- **GS-13 [P1 | I88/E90/R12] 4-Phase Comparison Bake-Off Rubric**: Reject a bake-off that skips or reorders the four phases — gating filters, weighted evaluation matrix with a `Primary Failure Mode`, ranked verdicts, then prototypes with explicit decision triggers. Rubric owned by [execution-modes.md](execution-modes.md) §3.1.

---

## 3. Universal Instruction Parsimony & Significance Ranking

This section establishes model-agnostic instruction sizing and sorting discipline to prevent attention dilution.

- **GS-14 [P2 | I88/E92/R08] Universal Instruction Parsimony**: Reject a standalone instruction file that exceeds its directive ceiling instead of decomposing into conditional JIT modules. Canonical ceiling (~30–50 directives): `WP-18`.
- **GS-15 [P2 | I86/E90/R08] Directive Accounting Separation**: Count compliance directives (imperative DO / DO NOT statements) separately from declarative reference content, schemas, tables, and code snippets. This rule defines how `WP-18` is measured.
- **GS-17 [P2 | I90/E94/R08] Ranking Conformance**: Reject governed rules that carry no `[P<tier> | I/E/R]` tag, use a tier outside `P0`–`P3`, or appear out of descending tier order within a section. Tier semantics and metric dimensions are owned by `WP-07` in [writing-profile.md](writing-profile.md).

> Retired IDs `GS-16`, `GS-18`, and `GS-19` are not reused. `GS-16` duplicated `WP-20`; `GS-18`
> duplicated `GS-04` inside this file; `GS-19` folded into `GS-17`. Durable IDs stay immutable
> (`WP-15`), so retirement leaves a gap rather than renumbering live references.

---

## 4. Traceability & Reference Grounding

- **Upstream Standard**: [Apex Informatics Standard](standard.md) (Sections 4, 10, 12, 14)
- **Patch Intent Source Schema**: [patch-intent-schema.json](../../../../.claude/skills/deterministic-markdown-patcher2/references/patch-intent-schema.json)
- **Operational Lore**: [Snippets.md](../../../AI-Snippets/Snippets.md) & [2Dos Ai Instructions.md](../../../AI-Snippets/Orga/2Dos%20Ai%20Instructions.md)
- **Deterministic Validation Engine**: [okf_validator.py](../tools/okf_validator.py)

---

## 5. Conformance Diagnostics & Validation Mapping

This section defines the diagnostic categories enforced by automated validation tooling.

- **GS-20 [P3 | I80/E88/R10] Tri-Class Diagnostic Classification**: Classify validation findings into `OKF_ERROR` (format violation), `APEX_PROFILE_ERROR` (repository profile violation), or `ADVISORY_WARNING` (style orientation).
- **GS-21 [P3 | I82/E89/R08] Deterministic Conformance Gate**: Enforce zero `OKF_ERROR` and zero `APEX_PROFILE_ERROR` findings as the gate for bundle ratification. Advisory warnings do not block ratification.
- **GS-22 [P3 | I75/E82/R10] Sub-Bundle Boundary Pruning**: Isolate untracked subdirectories or staging folders using boundary `index.md` files to prevent validator leakage. Canonical: `FA-08`.

#### Diagnostic Rule Catalog:
| Diagnostic Severity | Rule ID | Scope | Trigger Condition |
|---|---|---|---|
| **`OKF_ERROR`** | `OKF-ROOT-INDEX-EXISTS` | Bundle root | Root `index.md` file is missing. |
| **`OKF_ERROR`** | `OKF-INDEX-FRONTMATTER` | Root `index.md` | Frontmatter missing closing `---` or contains syntax error. |
| **`OKF_ERROR`** | `OKF-VERSION-DECLARATION`| Root `index.md` | Frontmatter fails to declare `okf_version: "0.2"`. |
| **`OKF_ERROR`** | `OKF-FRONTMATTER-PARSE` | Concept `*.md` | Frontmatter contains line missing `:` (e.g. Multiline `- list`). |
| **`OKF_ERROR`** | `OKF-FRONTMATTER-MISSING`| Concept `*.md` | Concept file lacks YAML frontmatter block. |
| **`OKF_ERROR`** | `OKF-TYPE-REQUIRED` | Concept `*.md` | Frontmatter missing mandatory non-empty `type` field. |
| **`APEX_PROFILE_ERROR`** | `APEX-LINK-INTEGRITY` | Root `index.md` | Relative markdown link fails to resolve to target file. |
| **`APEX_PROFILE_ERROR`** | `APEX-UNIQUE-DURABLE-ID`| Concept `*.md` | Duplicate `id` encountered in another bundle concept document. |
| **`ADVISORY_WARNING`** | `STE-SENTENCE-LENGTH` | Body prose | Prose sentence exceeds 30 words (exempting tables, lists, and code). |

The advisory gate fires above 30 words. The `WP-14` authoring target is deliberately tighter
(~20 procedural, ~25 descriptive). Sentences between target and gate are acceptable. Treat a clean
advisory count as a floor for prose quality, never a ceiling.
