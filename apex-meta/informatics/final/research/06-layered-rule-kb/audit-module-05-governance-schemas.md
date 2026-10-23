---
type: Reference
id: V2-AUDIT-MODULE-05-GOVERNANCE-SCHEMAS
title: Module Audit 05 — Governance Schemas & Directive Ceilings Semantic Block & Ownership Audit
description: Comprehensive rule-by-rule semantic block decomposition, WP-23 single-ownership ledger, redundancy purge, and cross-traceability audit for governance-schemas.md.
status: current_truth
tags: [module-audit, plane-4, governance-schemas, single-owner, semantic-blocks, traceability]
---

# Module Audit 05: Governance Schemas & Directive Ceilings (`governance-schemas.md`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (`<schemas>`, `<surgical>`, `<editing>`, `<authoring>`, `<trade_off>`)
> - **Layer 1 (Layered Rule KB):** [rule-12-surgical.md](rule-12-surgical.md), [rule-13-editing.md](rule-13-editing.md), [rule-16-authoring.md](rule-16-authoring.md), [rule-17-trade-off.md](rule-17-trade-off.md), [rule-20-schemas.md](rule-20-schemas.md)
> - **Layer 2 (Audited Canonical Module):** [governance-schemas.md](../../../governance-schemas.md) (`GS-01` through `GS-22`)
> - **Machine-Readable Schema:** [patch-intent-schema.json](../../../../../.claude/skills/deterministic-markdown-patcher2/references/patch-intent-schema.json)
> - **Upstream Research & Empirical Lore:** [standard.md](../../../standard.md), [RESULTS-06-condition-syntax.md](../03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-06-condition-syntax.md), [RESULTS-09-efficiency-audit.md](../03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md), [C03-conditional-informatics-formal-authoring/README.md](../01-universal-instruction-research/module-deepening/C03-conditional-informatics-formal-authoring/README.md), [Snippets.md](../../../../AI-Snippets/Snippets.md)

---

## 1. Module Scope, Architectural Role & Governed Rule Inventory

### 1.1 Architectural Domain & Loading Lifecycle
`governance-schemas.md` (`GOV-SCHEMAS-v0.2`) is the canonical Plane 4 governance specification establishing machine-readable schemas, deterministic AST patch intent specifications (`patch_intent.v1`), validation rules for OKF metadata, decision matrix protocols, model directive accounting, and CI conformance diagnostics across Apex OS.

Within the **Five-Plane Information Architecture** ([file-architecture.md](../../../file-architecture.md) `FA-03`), `governance-schemas.md` serves as the repository's machine-governance contract:
- **JIT Activation Trigger:** Autonomous agents retrieve `governance-schemas.md` when generating structured AST patch intents, validating frontmatter compliance, measuring cognitive directive density, formatting architectural decisions, or debugging validation gate failures.
- **Top-Loaded Invariants:** The module front-loads five critical P0 invariants (`GS-01` through `GS-05`) in the first ~500 tokens: mandatory schema conformance, prohibited whole-file patch rewrites, attention primacy, raw 3-metric significance tagging, and flat YAML frontmatter serialization.
- **Active vs Retired Rules:** The module defines **19 active governed rules** and documents **3 retired rules** (`GS-16`, `GS-18`, `GS-19`). In strict accordance with `WP-15` (*Tier-Agnostic Durable IDs*), retired IDs are preserved as explicit gaps rather than renumbering subsequent rules.

---

### 1.2 Comprehensive Governed Rule Inventory

The table below documents every active and retired rule in `governance-schemas.md`, its priority tier, raw 3-metric significance rating, formal scope, inputs, outputs, halt conditions, and canonical ownership.

| # | Category | Rule ID | Tier & Metrics | Title | Description & Scope | Inputs / Preconditions | Outputs / Behaviors | Error / Halt Behavior | Canonical Owner |
|---|---|---|:---:|---|---|---|---|---|:---:|
| 1 | Conformance | `GS-01` | `[P0 \| I98/E98/R05]` | Mandatory Schema Conformance | Governed artifacts must conform to declared schema. | Emitting structured data. | Rejects unregistered fields, missing keys, ungrounded claims. | Reject non-conforming artifacts. | **GS-01 (Owner)** |
| 2 | Mutation | `GS-02` | `[P0 \| I98/E96/R05]` | Prohibited Whole-File Patch Rewrites | Never generate full-file rewrites for existing files. | Patching files. | Enforces AST patch intents or exact-match search/replace. | Halt on whole-file patch intent. | `EM-01` |
| 3 | Primacy | `GS-03` | `[P0 \| I96/E95/R05]` | Top-Loaded Attention Primacy | Front-load P0 invariants in first ~500 tokens. | Structuring schemas/specs. | Position critical rules near top before attention decays. | Flag inverted rule ordering. | `WP-06` |
| 4 | Ranking | `GS-04` | `[P0 \| I95/E95/R06]` | Raw 3-Metric Significance Tagging | Tag rules with raw unaggregated `[P<tier> \| I/E/R]` (1–100). | Tagging rules/options. | Keeps dimensions distinct; no composite math scores. | Reject synthetic math score calculations. | `WP-07` |
| 5 | Frontmatter | `GS-05` | `[P0 \| I94/E96/R06]` | Flat YAML Frontmatter Serialization | Flat key-value pairs or inline bracketed lists; colon on every line. | Validating frontmatter. | Ensures compatibility with zero-dependency parsers. | Reject multiline hyphenated lists. | `FA-13` |
| 6 | Validation | `GS-06` | `[P1 \| I92/E95/R08]` | Root Index Schema (`index.md`) | Validation view of root index schema (`okf_version: "0.2"`). | Validating root index. | Rejects bundle root failing `FA-05` frontmatter contract. | Fail validation on invalid root index. | `FA-05` |
| 7 | Validation | `GS-07` | `[P1 \| I92/E95/R08]` | Concept Document Schema (`*.md`) | Validation view of concept schema (non-empty `type`, unique `id`). | Validating concept files. | Field-level contract owned by `FA-06`; concept types table. | Fail validation on missing type or id. | `FA-06` |
| 8 | Identifiers | `GS-08` | `[P1 \| I90/E94/R07]` | Bundle-Wide Durable ID Uniqueness | Enforce unique durable identifiers across all docs in bundle. | Validating bundle IDs. | Rejects duplicate IDs that cause collision. | Fail validation on ID duplication. | `WP-15` |
| 9 | Patch Intent | `GS-09` | `[P1 \| I96/E96/R05]` | Deterministic AST Patch Intent Specification | Structure automated mutations using `patch_intent.v1` schema. | Emitting patch intents. | Target edits by heading path and hints, not line numbers. | Reject line-offset patching. | **GS-09 (Owner)** |
| 10 | Patch Safety | `GS-10` | `[P1 \| I95/E95/R05]` | AST Safety Threshold Invariants | Mandatory safety invariants: unique match, fail on ambiguity, max 1 file. | Validating patch intent. | Enforces `require_unique_match: true`, `max_files_touched: 1`. | Reject intent with unsafe thresholds. | **GS-10 (Owner)** |
| 11 | Patch Safety | `GS-11` | `[P1 \| I93/E94/R06]` | Prohibited Brittle Identifiers | Forbid `line_number`, `line_start`, `line_range`, `hunk` in intents. | Authoring patch intent. | Forbids volatile line numbers that break on concurrent edits. | Reject patch intents with line numbers. | **GS-11 (Owner)** |
| 12 | Decision | `GS-12` | `[P1 \| I90/E92/R10]` | Structured Decision Matrix Protocol | Validation contract for Q&A Decision Matrix format. | Validating decision records. | Format owned by `execution-modes.md` §2.1. | Reject records missing question/options/notes. | `EM-06` |
| 13 | Comparison | `GS-13` | `[P1 \| I88/E90/R12]` | 4-Phase Comparison Bake-Off Rubric | Validation contract for 4-phase comparison bake-off. | Validating bake-offs. | Rubric owned by `execution-modes.md` §3.1. | Reject bake-offs skipping gating or failure mode. | `EM-07` |
| 14 | Sizing | `GS-14` | `[P2 \| I88/E92/R08]` | Universal Instruction Parsimony | Standalone file must not exceed directive ceiling (~30–50). | Validating instruction files. | Rejects overloaded rule-walls without JIT decomposition. | Flag files exceeding directive ceiling. | `WP-18` |
| 15 | Sizing | `GS-15` | `[P2 \| I86/E90/R08]` | Directive Accounting Separation | Count imperative directives separately from declarative content. | Measuring directive count. | Establishes the exact accounting method for `WP-18`. | Prevents miscounting tables/schemas as rules. | **GS-15 (Owner)** |
| — | *Retired* | `GS-16` | *Retired* | *Retired (Duplicate of `WP-20`)* | Retired during canonical compression pass; gap preserved. | — | — | — | *Retired* |
| 16 | Ranking | `GS-17` | `[P2 \| I90/E94/R08]` | Ranking Conformance | Reject rules lacking `[P<tier> \| I/E/R]` or out of descending order. | Validating rule blocks. | Tier semantics owned by `WP-07` in `writing-profile.md`. | Fail validation on invalid tier/metric tags. | `WP-07` |
| — | *Retired* | `GS-18` | *Retired* | *Retired (Duplicate of `GS-04`)* | Retired during canonical compression pass; gap preserved. | — | — | — | *Retired* |
| — | *Retired* | `GS-19` | *Retired* | *Retired (Folded into `GS-17`)* | Retired during canonical compression pass; gap preserved. | — | — | — | *Retired* |
| 17 | Diagnostics | `GS-20` | `[P3 \| I80/E88/R10]` | Tri-Class Diagnostic Classification | Classify findings into `OKF_ERROR`, `APEX_PROFILE_ERROR`, `ADVISORY_WARNING`. | Tooling validation runs. | Categorizes severity of linter/validator findings. | Standardizes diagnostic taxonomy. | **GS-20 (Owner)** |
| 18 | Gates | `GS-21` | `[P3 \| I82/E89/R08]` | Deterministic Conformance Gate | Enforce zero `OKF_ERROR` and zero `APEX_PROFILE_ERROR` to pass gate. | CI/pre-commit ratification. | Advisory warnings do not block ratification. | Block ratification on error count > 0. | **GS-21 (Owner)** |
| 19 | Boundaries | `GS-22` | `[P3 \| I75/E82/R10]` | Sub-Bundle Boundary Pruning | Isolate untracked subdirectories using boundary `index.md`. | Validating directory trees. | Stops validator recursion at sub-bundle boundaries. | Prevents staging noise in bundle audit. | `FA-08` |

---

### 1.3 Atomic Semantic Block Inventory (`SB-GS-01`..`SB-GS-22`)

Every active rule in `governance-schemas.md` decomposes into atomic semantic blocks that isolate discrete obligations:

- **`GS-01` (Mandatory Schema Conformance):**
  - `SB-GS-01.1` (*Declared Schema Conformance*): Every governed artifact must conform to its declared schema.
  - `SB-GS-01.2` (*Rejection Gate*): Reject any artifact that contains unregistered fields, missing mandatory keys, or ungrounded claims.
- **`GS-02` (Prohibited Whole-File Patch Rewrites):**
  - `SB-GS-02.1` (*Full-File Overwrite Ban*): Never generate or apply full-file rewrites for existing files.
  - `SB-GS-02.2` (*Surgical Patch Enforcement*): Enforce surgical AST patch intents (`patch_intent.v1`) or exact-match search/replace blocks with unique context (delegates to `EM-01`).
- **`GS-03` (Top-Loaded Attention Primacy):**
  - `SB-GS-03.1` (*Positional Primacy in Schemas*): Front-load critical P0 invariants near the beginning of every instruction and specification file (first ~500 tokens) (delegates to `WP-06`).
- **`GS-04` (Raw 3-Metric Significance Tagging):**
  - `SB-GS-04.1` (*Unaggregated I/E/R Tagging*): Tag governed rules, options, and trade-offs with raw unaggregated 3-metric estimates `[P<tier> | I<impact>/E<evidence>/R<risk>]` on a 1–100 scale (delegates to `WP-07`).
  - `SB-GS-04.2` (*Synthetic Formula Ban*): Never aggregate dimensions into a composite mathematical score.
- **`GS-05` (Flat YAML Frontmatter Serialization):**
  - `SB-GS-05.1` (*Flat Key-Value Syntax*): Write all YAML frontmatter headers as flat key-value pairs or inline bracketed lists.
  - `SB-GS-05.2` (*Multiline Hyphen Ban*): Never use multiline hyphenated lists (`- item`), as they cause zero-dependency parsers to fail (delegates to `FA-13`).
- **`GS-06` (Root Index Schema):**
  - `SB-GS-06.1` (*Bundle Identity Gate*): Reject any bundle whose root index fails the canonical OKF v0.2 frontmatter contract in `file-architecture.md` `FA-05`.
  - `SB-GS-06.2` (*Version Declaration*): Enforce `okf_version: "0.2"` as the bundle-identity gate.
- **`GS-07` (Concept Document Schema):**
  - `SB-GS-07.1` (*Mandatory Type & ID*): Reject any concept file lacking valid YAML frontmatter with a non-empty `type` and a bundle-unique `id` on line 1 (contract owned by `FA-06`).
  - `SB-GS-07.2` (*Concept Types Taxonomy*): Enforce valid concept types: `Specification`, `Standard`, `Profile`, `Adapter`, `Governance`, `Policy`, `Reference`.
- **`GS-08` (Bundle-Wide Durable ID Uniqueness):**
  - `SB-GS-08.1` (*Collision Prevention*): Enforce unique, tier-agnostic durable identifiers across all documents within an OKF bundle.
  - `SB-GS-08.2` (*Validator Failure Condition*): Duplicate IDs trigger validator failure (grammar owned by `WP-15`).
- **`GS-09` (Deterministic AST Patch Intent Specification):**
  - `SB-GS-09.1` (*Machine-Readable Structure*): Structure automated file mutations using the `patch_intent.v1` JSON Schema.
  - `SB-GS-09.2` (*Structural Heading Targeting*): Target edits by structural AST heading paths and context hints rather than volatile line numbers.
- **`GS-10` (AST Safety Threshold Invariants):**
  - `SB-GS-10.1` (*Four Mandatory Invariants*): Enforce mandatory safety invariants on every patch intent: `require_unique_match: true`, `fail_on_ambiguity: true`, `allow_full_file_rewrite: false`, and `max_files_touched: 1`.
- **`GS-11` (Prohibited Brittle Identifiers):**
  - `SB-GS-11.1` (*Volatile Offset Ban*): Forbid `line_number`, `line_start`, `line_end`, `line_range`, `hunk`, and `unified_diff` within patch intents.
  - `SB-GS-11.2` (*Silent Corruption Prevention*): Prevent silent patch corruption across concurrent edits.
- **`GS-12` (Structured Decision Matrix Protocol):**
  - `SB-GS-12.1` (*Validation Contract*): Reject a decision record that omits any mandatory field of the Q&A matrix: `Question`, $\ge 2$ `Options` (each carrying mechanism, `Grounding`, raw `I/E/R`), `Recommendation`, `Reasoning`, and one-line rejection `Notes` (format owned by `execution-modes.md` §2.1).
- **`GS-13` (4-Phase Comparison Bake-Off Rubric):**
  - `SB-GS-13.1` (*Validation Contract*): Reject a bake-off that skips or reorders the four phases: gating filters, weighted matrix with `Primary Failure Mode`, ranked verdicts, and functional prototypes with decision triggers (rubric owned by `execution-modes.md` §3.1).
- **`GS-14` (Universal Instruction Parsimony):**
  - `SB-GS-14.1` (*Directive Ceiling Enforcement*): Reject a standalone instruction file that exceeds its directive ceiling instead of decomposing into conditional JIT modules (ceiling owned by `WP-18`).
- **`GS-15` (Directive Accounting Separation):**
  - `SB-GS-15.1` (*Accounting Methodology*): Count compliance directives (imperative DO / DO NOT statements) separately from declarative reference content, schemas, tables, and code snippets.
  - `SB-GS-15.2` (*Measurement Standard*): Defines the exact accounting method for `WP-18` directive ceiling audits.
- **`GS-17` (Ranking Conformance):**
  - `SB-GS-17.1` (*Tagging & Order Validation*): Reject governed rules that carry no `[P<tier> | I/E/R]` tag, use a tier outside `P0`–`P3`, or appear out of descending tier order within a section (tier semantics owned by `WP-07`).
- **`GS-20` (Tri-Class Diagnostic Classification):**
  - `SB-GS-20.1` (*Severity Categorization*): Classify validation findings into `OKF_ERROR` (format violation), `APEX_PROFILE_ERROR` (repository profile violation), or `ADVISORY_WARNING` (style orientation).
- **`GS-21` (Deterministic Conformance Gate):**
  - `SB-GS-21.1` (*Zero-Error Ratification Gate*): Enforce zero `OKF_ERROR` and zero `APEX_PROFILE_ERROR` findings as the gate for bundle ratification.
  - `SB-GS-21.2` (*Non-Blocking Advisories*): Advisory warnings do not block ratification.
- **`GS-22` (Sub-Bundle Boundary Pruning):**
  - `SB-GS-22.1` (*Crawler Boundary Isolation*): Isolate untracked subdirectories or staging folders using boundary `index.md` files to prevent validator leakage (canonical: `FA-08`).

---

## 2. Single-Ownership Verification Ledger (`WP-23`)

### 2.1 Rules Canonically Owned by `governance-schemas.md` (7 Rules)
`governance-schemas.md` canonically defines 7 rules that establish machine-readable schemas, patch safety invariants, and diagnostic classifications:
1. `GS-01` — Mandatory Schema Conformance (root schema validation gate)
2. `GS-09` — Deterministic AST Patch Intent Specification (`patch_intent.v1` operative contract)
3. `GS-10` — AST Safety Threshold Invariants (`require_unique_match`, `fail_on_ambiguity`, `allow_full_file_rewrite: false`, `max_files_touched: 1`)
4. `GS-11` — Prohibited Brittle Identifiers (ban on line numbers, ranges, and diff hunks)
5. `GS-15` — Directive Accounting Separation (methodology for counting imperative directives vs declarative text)
6. `GS-20` — Tri-Class Diagnostic Classification (`OKF_ERROR`, `APEX_PROFILE_ERROR`, `ADVISORY_WARNING` taxonomy)
7. `GS-21` — Deterministic Conformance Gate (zero-error ratification gate in CI)

---

### 2.2 Sibling Rules Referencing `governance-schemas.md` Definitions (1 Delegation)
One rule in `execution-modes.md` explicitly cites the AST patch contract canonically owned by `governance-schemas.md`:

| Sibling File | Sibling Rule | Delegated Definition from `governance-schemas.md` | Relationship & Scope |
|---|---|---|---|
| `execution-modes.md` | `EM-08` | `GS-09..11` | Mode B cites `patch_intent.v1` operative contract in `governance-schemas.md` §2.2 and delegates the schema to `patch-intent-schema.json`. |

---

### 2.3 Rules Within `governance-schemas.md` Delegating to External Canonical Owners (12 Delegations)
`governance-schemas.md` delegates 12 rules to external canonical owners in `writing-profile.md`, `file-architecture.md`, and `execution-modes.md`:

| Local Rule | Priority Tier | Target Canonical Owner | Owner File | Delegation Scope & Relationship |
|---|:---:|---|---|---|
| `GS-02` | **P0** | `EM-01` | `execution-modes.md` | Prohibited Whole-File Patch Rewrites. Restates surgical patch invariant for CI gating. |
| `GS-03` | **P0** | `WP-06` | `writing-profile.md` | Top-Loaded Attention Primacy. Restates first ~500 token orientation for schema documents. |
| `GS-04` | **P0** | `WP-07` | `writing-profile.md` | Raw 3-Metric Significance Tagging. Cites syntax and unaggregated dimension rules. |
| `GS-05` | **P0** | `FA-13` | `file-architecture.md` | Flat YAML Frontmatter Serialization. *Deliberate Priority Elevation:* Elevates flat serialization to P0 because multiline hyphens cause zero-dependency parsers to fail. |
| `GS-06` | **P1** | `FA-05` | `file-architecture.md` | Root Index Schema Validation View. Rejects bundle root failing `FA-05` without re-declaring fields. |
| `GS-07` | **P1** | `FA-06` | `file-architecture.md` | Concept Document Schema Validation View. Enforces concept frontmatter rules without duplicating schema. |
| `GS-08` | **P1** | `WP-15` | `writing-profile.md` | Bundle-Wide Durable ID Uniqueness. Enforces ID uniqueness checks based on `WP-15` grammar. |
| `GS-12` | **P1** | `EM-06` | `execution-modes.md` | Structured Decision Matrix Protocol. Validation contract enforcing `EM-06` format. |
| `GS-13` | **P1** | `EM-07` | `execution-modes.md` | 4-Phase Comparison Bake-Off Rubric. Validation contract enforcing `EM-07` workflow. |
| `GS-14` | **P2** | `WP-18` | `writing-profile.md` | Universal Instruction Parsimony. Rejects files exceeding directive ceiling. |
| `GS-17` | **P2** | `WP-07` | `writing-profile.md` | Ranking Conformance. Validates rule blocks against `WP-07` priority tiers. |
| `GS-22` | **P3** | `FA-08` | `file-architecture.md` | Sub-Bundle Boundary Pruning. Specifies automated crawler boundary pruning based on `FA-08`. |

---

### 2.4 Mechanical Verification Evidence (`test_canonical_ownership.py`)
Deterministic verification via `test_canonical_ownership.py` proves 100% adherence to single-ownership discipline:
1. **Rule Prefix Integrity:** All 19 active rules begin with `GS-`, and no `GS-` rules are defined in other files (`test_rule_id_prefix_matches_its_home_file`).
2. **Rule ID Uniqueness:** Zero duplicate IDs exist within `governance-schemas.md` (`test_no_duplicate_rule_id_within_a_file`).
3. **Pointer Resolution:** All 12 canonical pointers resolve to active rules across the suite (`TestCanonicalPointerIntegrity`).
4. **Zero Re-Embedded Upstream Schemas (`D9` Guard):** `test_canonical_ownership.py` contains an explicit test `TestNoReEmbeddedUpstreamSchema`:
   > It asserts that `"$schema"` fenced blocks do not appear in `governance-schemas.md`.
   By citing [patch-intent-schema.json](../../../../../.claude/skills/deterministic-markdown-patcher2/references/patch-intent-schema.json) without embedding the raw schema, `governance-schemas.md` eliminates schema drift while preserving full operational rigor.

---

## 3. Redundancy & Stale Terminology Remediation Plan

### 3.1 Cross-Module Redundancy Clusters Involving `governance-schemas.md`
The audit identified 5 prominent concept clusters where `governance-schemas.md` intersects with other modules:

1. **Validation Views vs Authoritative Owners (`GS-06`/`GS-07` vs `FA-05`/`FA-06`, `GS-12`/`GS-13` vs `EM-06`/`EM-07`):**
   - *Architecture Pattern:* `file-architecture.md` and `execution-modes.md` author the human-readable definitions and structural templates. `governance-schemas.md` provides the **validation view** for automated linters and CI pipelines.
   - *WP-23 Compliance:* `GS-06`, `GS-07`, `GS-12`, and `GS-13` cite their respective authoritative owners without re-declaring duplicate frontmatter blocks or decision templates.
2. **Flat YAML Frontmatter Serialization (`GS-05` [P0] vs `FA-13` [P1]):**
   - *Deliberate Tier Elevation:* In `file-architecture.md`, flat frontmatter is a P1 structural standard. In `governance-schemas.md`, it is elevated to **P0** because custom frontmatter parsers fail immediately on multiline lists, halting verification.
3. **Directive Parsimony vs Accounting (`GS-14` [P2], `GS-15` [P2] vs `WP-18` [P2]):**
   - *Current State:* `WP-18` defines the ceiling (~30–50 directives). `GS-14` enforces the gate. `GS-15` defines how directives are separated from declarative content.
   - *Remediation Plan:* Clean division of responsibilities; keep `GS-15` as the measurement specification.
4. **Ranking Conformance (`GS-17` [P2] vs `WP-07` [P0]):**
   - *Current State:* `WP-07` defines the tier semantics. `GS-17` specifies CI rejection when rules lack tags or appear out of order.
   - *Assessment:* Fully compliant with `WP-23`.
5. **AST Patch Safety Thresholds (`GS-10` [P1], `GS-11` [P1] vs `EM-08` [P1]):**
   - *Current State:* `EM-08` provides the worked example; `GS-10` and `GS-11` enforce the non-negotiable safety boundaries.
   - *Assessment:* Zero duplicate schemas; clean functional separation.

---

### 3.2 Documented Retired Rule IDs (`GS-16`, `GS-18`, `GS-19`)
In `governance-schemas.md` §3 (lines 96–98), three retired IDs are explicitly documented:
> *"Retired IDs `GS-16`, `GS-18`, and `GS-19` are not reused. `GS-16` duplicated `WP-20`; `GS-18` duplicated `GS-04` inside this file; `GS-19` folded into `GS-17`. Durable IDs stay immutable (`WP-15`), so retirement leaves a gap rather than renumbering live references."*

- **Audit Evaluation:** This explicit documentation is an exemplary implementation of `WP-15` (*Tier-Agnostic Durable IDs*). In fragile instruction architectures, authors often renumber subsequent rules (e.g. Renumbering `GS-20` to `GS-17`), which silently breaks external commit links, test fixtures, and agent cache references. Leaving documented gaps preserves complete repository stability.

---

### 3.3 Diagnostic Rule Catalog Alignment (`okf_validator.py`)
Section 5 of `governance-schemas.md` establishes the **Diagnostic Rule Catalog**. This audit verified that every diagnostic code defined in `governance-schemas.md` corresponds directly to an active check in `okf_validator.py`:

| Diagnostic Severity | Rule ID | Scope | Checked by Validator Function | Status in Tooling |
|---|---|---|---|:---:|
| `OKF_ERROR` | `OKF-ROOT-INDEX-EXISTS` | Bundle root | `validate_bundle_root_index_exists()` | Active |
| `OKF_ERROR` | `OKF-INDEX-FRONTMATTER` | Root `index.md` | `parse_yaml_frontmatter()` | Active |
| `OKF_ERROR` | `OKF-VERSION-DECLARATION` | Root `index.md` | `validate_okf_version_0_2()` | Active |
| `OKF_ERROR` | `OKF-FRONTMATTER-PARSE` | Concept `*.md` | `parse_flat_yaml_lines()` | Active |
| `OKF_ERROR` | `OKF-FRONTMATTER-MISSING` | Concept `*.md` | `check_frontmatter_delimiters()` | Active |
| `OKF_ERROR` | `OKF-TYPE-REQUIRED` | Concept `*.md` | `validate_mandatory_type_field()` | Active |
| `APEX_PROFILE_ERROR` | `APEX-LINK-INTEGRITY` | Root `index.md` | `verify_relative_markdown_links()` | Active |
| `APEX_PROFILE_ERROR` | `APEX-UNIQUE-DURABLE-ID` | Concept `*.md` | `check_bundle_durable_id_uniqueness()` | Active |
| `ADVISORY_WARNING` | `STE-SENTENCE-LENGTH` | Body prose | `audit_sentence_length_ceiling_30()` | Active |

---

## 4. Cross-Traceability Matrix to XML `<apex_contract>` and Ultra Contract

### 4.1 Upward Mapping to Contract Tags
Every governance rule relevant to agent execution maps directly to tags in `<apex_contract v="1.0">` ([13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md)) and `16-candidate-3A-ultra.md`:

| Semantic Contract Tag | Mode | Mapped `GS` Rules | Key Semantic Obligations Codified in Contract |
|---|---|---|---|
| `<schemas>` | Gated (`governance-schemas.md`) | `GS-01`, `GS-09`, `GS-10`, `GS-11` | Satisfy declared schema exactly; target edits by heading path and hints, never line numbers. |
| `<surgical>` | Unconditional Stub | `GS-02` | Never generate full-file rewrites for existing files. |
| `<editing>` | Gated (`execution-modes.md`) | `GS-09`, `GS-10`, `GS-11` | Replace exact lines verbatim; open ref for AST patch; no line numbers. |
| `<authoring>` | Gated (`index.md`) | `GS-03`, `GS-04`, `GS-05`, `GS-14`, `GS-15`, `GS-17` | Flat YAML; front-load rules; tag `[P \| I/E/R]`; instruction parsimony; ranking order. |
| `<trade_off>` | Gated (`execution-modes.md`) | `GS-12`, `GS-13` | Mandatory validation fields for Q&A matrices and 4-phase comparison bake-offs. |

---

### 4.2 Analysis of the 7 "Unmapped" Rules
Seven rules in `governance-schemas.md` are not explicitly cited in the Layer 0 contract block:
1. `GS-05` (Flat YAML frontmatter pointer to `FA-13`)
2. `GS-06` (Root index schema validation view)
3. `GS-07` (Concept document schema validation view)
4. `GS-08` (Bundle-wide durable ID uniqueness validation view)
5. `GS-20` (Tri-Class diagnostic classification)
6. `GS-21` (Deterministic conformance gate)
7. `GS-22` (Sub-bundle boundary pruning validation view)

**Inclusion Rationale for Plane 4:**
These 7 rules govern **offline CI validation, validator diagnostics, and test suite execution** (`okf_validator.py` and `test_canonical_ownership.py`) rather than prompt-level agent execution:
- `GS-20` and `GS-21` define the diagnostic severity taxonomy and the zero-error gate for CI ratification.
- `GS-06`, `GS-07`, and `GS-08` provide the validation view for the repository linter.
- `GS-22` specifies boundary pruning for automated tools crawling directories.
Embedding automated CI diagnostic codes into an always-on instruction contract would waste prompt tokens on compiler-level machinery. Plane 4 is their exact architectural home.

---

### 4.3 Upstream Empirical Grounding & Research Links
The governance schemas in `governance-schemas.md` codify critical empirical research:
- **`GS-09`, `GS-10` & `GS-11`:** Grounded in Research Packet [RESULTS-06-condition-syntax.md](../03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-06-condition-syntax.md), proving that structural AST heading targeting prevents 100% of line-offset drift errors across concurrent agent edits.
- **`GS-14` & `GS-15`:** Grounded in Research Packet [RESULTS-09-efficiency-audit.md](../03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md), demonstrating that directive density degrades instruction compliance when files exceed ~50 imperative rules.
- **`GS-01` & `GS-21`:** Grounded in [C03-conditional-informatics-formal-authoring/README.md](../01-universal-instruction-research/module-deepening/C03-conditional-informatics-formal-authoring/README.md) and [standard.md](../../../standard.md), establishing zero-error deterministic validation gates.

---

## 5. Module Failure Modes & Not-To-Dos (`WP-25`)

In accordance with `WP-25` (*Terminal-Position Operative Content*), this audit concludes with non-negotiable operational boundaries and anti-patterns for anyone editing or validating `governance-schemas.md`:

- **Never Re-Embed Full JSON Schema Definitions in Documentation (`WP-23`, `D9` Violation):** Do not copy raw JSON schema blocks into markdown specifications. Always reference the authoritative [patch-intent-schema.json](../../../../../.claude/skills/deterministic-markdown-patcher2/references/patch-intent-schema.json). Re-embedded copies inevitably drift and weaken constraints.
- **Never Author Patch Intents With Volatile Line Numbers (`GS-11` Violation):** Forbid `line_number`, `line_range`, or `hunk` inside patch intents. Target modifications strictly by structural AST heading paths and nearby context hints.
- **Never Relax AST Safety Invariants (`GS-10` Violation):** Never set `require_unique_match: false` or `allow_full_file_rewrite: true` to bypass an edit error. If a match is ambiguous, resolve the ambiguity by adding specific context hints.
- **Never Renumber Retired Rule IDs to Eliminate Gaps (`WP-15` Violation):** Preserving gaps for `GS-16`, `GS-18`, and `GS-19` is mandatory. Renumbering rules corrupts historical citations, git annotations, and external references.
- **Never Let Advisory Warnings Block Conformance Gates (`GS-21` Violation):** Advisory warnings (such as `STE-SENTENCE-LENGTH`) indicate stylistic polish orientations. Only `OKF_ERROR` and `APEX_PROFILE_ERROR` block ratification.
- **Never Allow Open Unregistered Fields in Governance Artifacts (`GS-01` Violation):** Structured governance documents must reject unexpected keys (`additionalProperties: false`). Loose dictionaries allow silent schema corruption.
