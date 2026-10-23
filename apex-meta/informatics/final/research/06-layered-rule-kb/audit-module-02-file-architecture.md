---
type: Reference
id: V2-AUDIT-MODULE-02-FILE-ARCHITECTURE
title: Module Audit 02 — File Architecture & Bundle Specification Semantic Block & Ownership Audit
description: Comprehensive rule-by-rule semantic block decomposition, WP-23 single-ownership ledger, redundancy purge, and cross-traceability audit for file-architecture.md.
status: current_truth
tags: [module-audit, plane-4, file-architecture, single-owner, semantic-blocks, traceability]
---

# Module Audit 02: File Architecture & Bundle Specification (`file-architecture.md`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (`<current_truth>`, `<authoring>`, `<target>`, `<pointers>`)
> - **Layer 1 (Layered Rule KB):** [rule-01-target.md](rule-01-target.md), [rule-11-current-truth.md](rule-11-current-truth.md), [rule-16-authoring.md](rule-16-authoring.md), [rule-22-pointers.md](rule-22-pointers.md)
> - **Layer 2 (Audited Canonical Module):** [file-architecture.md](../../specs/file-architecture.md) (`FA-01` through `FA-13`)
> - **Upstream Research & Empirical Lore:** [standard.md](../../specs/standard.md), [RESULTS-10-surface-layering.md](../03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-10-surface-layering.md), [RESULTS-03-currency-check.md](../03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-03-currency-check.md), [A11-current-truth-authoritative-state/README.md](../01-universal-instruction-research/module-deepening/A11-current-truth-authoritative-state/README.md), [Snippets.md](../../../../AI-Snippets/Snippets.md)

---

## 1. Module Scope, Architectural Role & Governed Rule Inventory

### 1.1 Architectural Domain & Loading Lifecycle
`file-architecture.md` (`SPEC-FILE-ARCH-v0.2`) is the canonical Plane 4 specification governing repository file layout, Open Knowledge Format (OKF) v0.2 bundle structures, flat YAML frontmatter serialization, current-truth separation, and positional attention primacy across Apex OS.

Within the **Five-Plane Information Architecture** (`FA-03`), `file-architecture.md` defines the structural backbone of repository knowledge:
- **JIT Activation Trigger:** An autonomous agent retrieves `file-architecture.md` when creating new files, restructuring directory hierarchies, updating root indexes, refactoring documentation bundles, or validating OKF metadata.
- **Progressive Loading Sequence:** System prompts in Plane 1 load at session start; Scoped Instructions in Plane 2 activate on path match; Procedures (Skills) in Plane 3 execute on task intent; Plane 4 Knowledge Bundles retrieve just-in-time via index pointers; Plane 5 Evidence & History loads only during forensics.
- **Top-Loaded Invariants:** The module front-loads four critical P0 invariants (`FA-01` through `FA-04`) in the first ~500 tokens, establishing strict current-truth separation, attention primacy, five-plane separation, and substance over ceremony.

---

### 1.2 Comprehensive Governed Rule Inventory

The live `file-architecture.md` defines **13 governed rules** across five structural sections. The table below documents every rule, its priority tier, raw 3-metric significance rating, formal scope, inputs, outputs, halt conditions, and canonical ownership.

| # | Category | Rule ID | Tier & Metrics | Title | Description & Scope | Inputs / Preconditions | Outputs / Behaviors | Error / Halt Behavior | Canonical Owner |
|---|---|---|:---:|---|---|---|---|---|:---:|
| 1 | History | `FA-01` | `[P0 \| I95/E95/R08]` | Strict Current-Truth Separation | Live files state active current truth only; history isolated in `log.md`. | Editing live specifications. | Zero inline changelogs; history isolated in `log.md`. | Reject inline version histories. | **FA-01 (Owner)** |
| 2 | Primacy | `FA-02` | `[P0 \| I95/E92/R08]` | Top-Loaded Attention Primacy | Front-load P0 invariants in first ~500 tokens; order P0→P3. | Structuring file sections. | Critical boundaries read before attention decays. | Flag inverted rule tiers. | `WP-06`, `WP-07` |
| 3 | Architecture | `FA-03` | `[P0 \| I92/E90/R12]` | Five-Plane Information Separation | Maintain strict separation across the five architecture planes. | Organizing repository files. | Separates Control, Scoped, Skills, Bundles, Evidence. | Reject mixed-plane monoliths. | **FA-03 (Owner)** |
| 4 | Authority | `FA-04` | `[P0 \| I98/E98/R05]` | Substance Over Ceremony Exception Authority | Target realization overrides mechanical metric compliance. | Evaluating metric ceilings. | Authorizes exceeding limits when required for safety/truth. | Reject mechanical cuts that compromise truth. | `WP-01` |
| 5 | Frontmatter | `FA-13` | `[P1 \| I90/E95/R10]` | Flat/Inline YAML Frontmatter Serialization | Flat key-value pairs or inline bracket lists; colon on every line. | Writing frontmatter. | Ensures custom zero-dependency parsers succeed. | Reject multiline hyphenated lists (`- item`). | **FA-13 (Owner)** |
| 6 | Frontmatter | `FA-05` | `[P1 \| I88/E92/R12]` | Root Index Specification (`index.md`) | Root `index.md` frontmatter (`okf_version: "0.2"`, title, desc, tags). | Bundle root index creation. | Establishes bundle identity and navigation links. | Reject bundle root without `okf_version: "0.2"`. | **FA-05 (Owner)** |
| 7 | Frontmatter | `FA-06` | `[P1 \| I88/E92/R12]` | Concept Document Specification (`*.md`) | Mandatory frontmatter: `type`, unique `id`, `title`, `description`, `status`. | Concept document authoring. | Defines concept document metadata contract. | Validator rejects missing `type` or duplicate `id`. | **FA-06 (Owner)** |
| 8 | Identifiers | `FA-07` | `[P1 \| I85/E88/R15]` | Unique Durable Identifiers | Immutable durable ID assigned to every governed concept file. | Creating concept files. | Provides stable cross-referencing targets. | Validator rejects duplicate IDs across bundle. | `WP-15` |
| 9 | Boundaries | `FA-08` | `[P1 \| I85/E90/R15]` | Sub-Bundle Isolation Boundary | Subdirectory with its own `index.md` forms an isolated sub-bundle. | Directory topology. | Validator stops recursion at sub-bundle boundaries. | Prevents draft leakage into root bundle. | **FA-08 (Owner)** |
| 10 | Hygiene | `FA-09` | `[P1 \| I82/E85/R18]` | Residual Name Eradication | Purge all residual mentions of obsolete names from live docs. | Renaming or deleting tools. | Eradicates dead names to prevent model hallucinations. | Flag references to retired systems. | `AD-15` |
| 11 | Structure | `FA-10` | `[P2 \| I78/E82/R20]` | Single-Purpose Topic Files | Structure every concept document around a single responsibility. | Designing new modules. | Partitions content into focused topic files. | Flag multi-topic monolithic documents. | **FA-10 (Owner)** |
| 12 | History | `FA-11` | `[P2 \| I75/E80/R18]` | Dedicated Changelog Allocation | Record version history and milestones exclusively in `log.md`. | Updating bundle history. | Exempts `log.md` from mandatory concept frontmatter. | Flag placing changelogs in concept docs. | **FA-11 (Owner)** |
| 13 | Sizing | `FA-12` | `[P2 \| I82/E88/R10]` | Plane Sizing & Instruction Parsimony | Keep surfaces within plane token ceilings; two-layer carrier structure. | Packaging instructions. | Layer 1 universal contract + Layer 2 repo-specific. | Flag overloaded rule-walls. | `WP-18` |

---

### 1.3 Atomic Semantic Block Inventory (`SB-FA-01`..`SB-FA-13`)

Every rule in `file-architecture.md` decomposes into atomic semantic blocks that isolate discrete obligations:

- **`FA-01` (Strict Current-Truth Separation):**
  - `SB-FA-01.1` (*Active Truth Invariant*): Live specification and instruction files state active current truth only.
  - `SB-FA-01.2` (*Inline History Ban*): Never embed inline changelogs, superseded alternatives, or historical narratives inside live documents.
  - `SB-FA-01.3` (*Dedicated History Allocation*): Record historical changes, deprecated options, and audit notes in dedicated external changelogs (`log.md`) or archive directories.
- **`FA-02` (Top-Loaded Attention Primacy):**
  - `SB-FA-02.1` (*Positional Primacy*): Front-load critical P0 invariants near the beginning of every specification (first ~500 tokens).
  - `SB-FA-02.2` (*Descending Order*): Organize subsequent rules in generally descending priority order (P0, then P1, P2, P3).
  - `SB-FA-02.3` (*Delegated Definitions*): Delegates positional primacy to `WP-06` and tier definitions to `WP-07`.
- **`FA-03` (Five-Plane Information Separation):**
  - `SB-FA-03.1` (*Plane Separation Invariant*): Maintain strict separation across the five architecture planes (Control, Scoped, Skills, Bundles, Evidence).
  - `SB-FA-03.2` (*Monolith Ban*): Never combine system prompts, scoped rules, procedural skills, knowledge bundles, and raw evidence in a single file.
  - `SB-FA-03.3` (*Context Clash Prevention*): Prevent context clash and preserve targeted just-in-time reloading.
- **`FA-04` (Substance Over Ceremony Exception Authority):**
  - `SB-FA-04.1` (*Target Realization Over Mechanics*): Substantive realization of the target strictly overrides mechanical metric compliance.
  - `SB-FA-04.2` (*Ceiling Exceedance Authority*): Authorizes exceeding line, word, or token orientations when required for safety, accuracy, or completeness (delegates to `WP-01`).
- **`FA-13` (Flat/Inline YAML Frontmatter Serialization):**
  - `SB-FA-13.1` (*Flat Key-Value Syntax*): Use flat key-value pairs or inline bracket lists in all frontmatter headers.
  - `SB-FA-13.2` (*Colon Separation Invariant*): Every non-comment line must contain a colon separator (`:`).
  - `SB-FA-13.3` (*Multiline Hyphen Ban*): Never use multiline YAML list syntax (`- item`), as it causes custom zero-dependency parsers to fail.
- **`FA-05` (Root Index Specification):**
  - `SB-FA-05.1` (*Bundle Identity Gate*): Every knowledge bundle must provide a root `index.md` declaring `okf_version: "0.2"`.
  - `SB-FA-05.2` (*Relative Link Integrity*): Must provide relative markdown links to all member concept files; links must resolve to existing files.
  - `SB-FA-05.3` (*No Body Duplication*): Root index must not duplicate substantive body text from concept documents.
  - `SB-FA-05.4` (*Canonical Frontmatter Owner*): Canonical contract for root indexes; `GS-06` states only the validation view.
- **`FA-06` (Concept Document Specification):**
  - `SB-FA-06.1` (*Mandatory Fields*): Concept files store curated domain knowledge and must declare `type` and unique `id`.
  - `SB-FA-06.2` (*Standard Fields*): Must provide `title`, `description`, `status`, and `tags`.
  - `SB-FA-06.3` (*Optional Versioning*): Declare `version` only when independently versioned; absence is never a conformance failure.
  - `SB-FA-06.4` (*Canonical Concept Owner*): Canonical contract for concept documents; `GS-07` states only the validation view.
- **`FA-07` (Unique Durable Identifiers):**
  - `SB-FA-07.1` (*Immutable ID Assignment*): Assign an immutable durable ID (`id: ...`) to every governed concept file.
  - `SB-FA-07.2` (*Cross-Reference Stability*): Provides stable cross-referencing targets independent of filename or heading changes.
  - `SB-FA-07.3` (*Grammar Delegation*): Delegates durable identifier grammar to `WP-15`.
- **`FA-08` (Sub-Bundle Isolation Boundary):**
  - `SB-FA-08.1` (*Boundary Declaration*): Subdirectories containing their own `index.md` file form independent sub-bundles.
  - `SB-FA-08.2` (*Validator Recursion Pruning*): Automated validators stop recursion at sub-bundle boundaries, isolating drafts, prototypes, and legacy files.
- **`FA-09` (Residual Name Eradication):**
  - `SB-FA-09.1` (*Dead Alias Purge*): Eradicate all residual mentions of obsolete names when refactoring or deleting components.
  - `SB-FA-09.2` (*Ghost Reasoning Guard*): Prevents models from hallucinating legacy behaviors and resurrecting deleted workflows (delegates to `AD-15`).
- **`FA-10` (Single-Purpose Topic Files):**
  - `SB-FA-10.1` (*Single Responsibility*): Structure every concept document around a single responsibility.
  - `SB-FA-10.2` (*Information Mapping Layout*): Apply Information Mapping principles: clearly labeled sections, tables, and bulleted lists.
- **`FA-11` (Dedicated Changelog Allocation):**
  - `SB-FA-11.1` (*Changelog Isolation*): Record version history and modification milestones exclusively in `log.md`.
  - `SB-FA-11.2` (*Frontmatter Exemption*): The validator explicitly exempts `log.md` from mandatory concept frontmatter checks.
- **`FA-12` (Plane Sizing & Instruction Parsimony):**
  - `SB-FA-12.1` (*Plane Ceiling Compliance*): Keep every persistent instruction surface within its plane token orientation (~2,000 Control, ~1,500 Scoped, ~4,000 Skills).
  - `SB-FA-12.2` (*Two-Layer Carrier Structure*): Structure Plane 1 carriers into two distinct layers: an immutable cross-project `<apex_contract>` layer first (maximizing prompt cache reuse) followed by repo-specific rules.
  - `SB-FA-12.3` (*Directive Ceiling Delegation*): Delegates directive ceiling to `WP-18`.

---

## 2. Single-Ownership Verification Ledger (`WP-23`)

### 2.1 Rules Canonically Owned by `file-architecture.md` (8 Rules)
`file-architecture.md` is the authoritative canonical owner of repository layout, bundle topology, and frontmatter contracts:
1. `FA-01` — Strict Current-Truth Separation (active truth only in live docs; changelogs in `log.md`)
2. `FA-03` — Five-Plane Information Separation (strict isolation of 5 planes and token budgets)
3. `FA-13` — Flat/Inline YAML Frontmatter Serialization (colon on every line; multiline hyphen list ban)
4. `FA-05` — Root Index Specification (`okf_version: "0.2"` frontmatter contract and navigation rules)
5. `FA-06` — Concept Document Specification (`type`, `id`, `title`, `description`, `status` contract)
6. `FA-08` — Sub-Bundle Isolation Boundary (`index.md` boundary pruning for validators)
7. `FA-10` — Single-Purpose Topic Files (Information Mapping single-responsibility rule)
8. `FA-11` — Dedicated Changelog Allocation (`log.md` exemption from concept frontmatter checks)

---

### 2.2 Sibling Rules Referencing `file-architecture.md` Definitions (4 Delegations)
Four rules in `governance-schemas.md` explicitly reference the definitions canonically owned by `file-architecture.md`:

| Sibling File | Sibling Rule | Delegated Definition from `file-architecture.md` | Relationship & Scope |
|---|---|---|---|
| `governance-schemas.md` | `GS-05` | `FA-13` | Cites flat YAML frontmatter serialization as an operative P0 invariant. |
| `governance-schemas.md` | `GS-06` | `FA-05` | Enforces the validation view of the root index schema without re-declaring frontmatter fields. |
| `governance-schemas.md` | `GS-07` | `FA-06` | Enforces the validation view of concept document schemas without re-declaring field contracts. |
| `governance-schemas.md` | `GS-22` | `FA-08` | Implements sub-bundle boundary pruning in automated validator tooling. |

---

### 2.3 Rules Within `file-architecture.md` Delegating to External Canonical Owners (5 Delegations)
`file-architecture.md` delegates 5 rules to external canonical owners in `writing-profile.md` and `anti-drift-rules.md`:

| Local Rule | Priority Tier | Target Canonical Owner | Owner File | Delegation Scope & Deliberate Priority Nuance |
|---|:---:|---|---|---|
| `FA-02` | **P0** | `WP-06`, `WP-07` | `writing-profile.md` | Top-Loaded Positional Primacy & Metric Definitions. Cites `WP-06` for token-decay attention curves and `WP-07` for P0–P3 tier and raw I/E/R definitions. |
| `FA-04` | **P0** | `WP-01` | `writing-profile.md` | Substance Over Ceremony Exception Authority. Restates operative imperative for file architecture. |
| `FA-07` | **P1** | `WP-15` | `writing-profile.md` | Unique Durable Identifiers Grammar. Cites immutable ID syntax (`XX-NN` tier-agnostic). |
| `FA-09` | **P1** | `AD-15` | `anti-drift-rules.md` | Residual Name Eradication. Cites dead alias purge to prevent model hallucinations during refactoring. |
| `FA-12` | **P2** | `WP-18` | `writing-profile.md` | Plane Sizing & Instruction Parsimony. Cites universal directive ceiling (~30–50 directives max). |

---

### 2.4 Mechanical Verification Evidence (`test_canonical_ownership.py`)
Deterministic verification via `test_canonical_ownership.py` confirms complete ownership integrity:
1. **Rule Prefix Integrity:** All 13 rules begin with `FA-`, and no `FA-` rules are defined in any other file (`test_rule_id_prefix_matches_its_home_file`).
2. **Rule ID Uniqueness:** Zero duplicate IDs exist within `file-architecture.md` (`test_no_duplicate_rule_id_within_a_file`). (This test directly guards against Defect D1, where `FA-04` was historically assigned to two distinct rules).
3. **Pointer Resolution:** All 5 canonical pointers (`WP-06`/`WP-07`, `WP-01`, `WP-15`, `AD-15`, `WP-18`) resolve to active rules in the suite (`TestCanonicalPointerIntegrity`).
4. **Zero Self-Referential Pointers:** `file-architecture.md` contains zero `Canonical: `FA-xx`` references (`test_canonical_pointer_never_targets_its_own_file`).

---

## 3. Redundancy & Stale Terminology Remediation Plan

### 3.1 Cross-Module Redundancy Clusters Involving `file-architecture.md`
The audit identified 5 prominent concept clusters where `file-architecture.md` intersects with other modules:

1. **Current-Truth Separation (`FA-01` [P0] vs `AD-15` [P1], contract `<current_truth>`):**
   - *Current State:* `FA-01` governs file organization (banning inline changelogs and dedicating `log.md`), while `AD-15` governs semantic memory (purging retired aliases from active reasoning).
   - *Assessment:* Clean complementary roles. `FA-01` is the structural filesystem boundary; `AD-15` is the operational context hygiene rule.
2. **Frontmatter Syntax & Validation (`FA-13` [P1] vs `GS-05` [P0]):**
   - *Current State:* `FA-13` defines the frontmatter syntax rule in §3, while `GS-05` elevates it to a P0 invariant in `governance-schemas.md`.
   - *Deliberate Nuance:* In file authoring, flat frontmatter is a P1 structural method. In automated governance validation, a multiline hyphenated list causes zero-dependency YAML parsers to crash immediately, making it a critical P0 gate failure.
3. **Durable Identifier Contract (`FA-07` [P1] vs `WP-15` [P1], `GS-08` [P1]):**
   - *Current State:* `FA-07` mandates assigning an `id` to concept files; `WP-15` defines the grammar; `GS-08` tests bundle uniqueness.
   - *Assessment:* Fully compliant with `WP-23`.
4. **Sub-Bundle Boundary Pruning (`FA-08` [P1] vs `GS-22` [P3]):**
   - *Current State:* `FA-08` defines the architectural convention of sub-bundle isolation via `index.md`; `GS-22` specifies the crawler behavior in `okf_validator.py`.
   - *Remediation Plan:* Keep `FA-08` as the canonical architectural definition, with `GS-22` referencing it as the validator implementation.
5. **Instruction Parsimony & Prompt Caching (`FA-12` [P2] vs `WP-18` [P2]):**
   - *Current State:* `FA-12` extends `WP-18` by introducing the two-layer carrier architecture for Plane 1 prompt-cache reuse.
   - *Remediation Opportunity:* High-value insight from Research Packet [RESULTS-10-surface-layering.md](../03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-10-surface-layering.md) (RP-09/RP-10) should be highlighted across prompt documentation.

---

### 3.2 Out-of-Numerical-Sequence Rule Placements & Remediation
- In `file-architecture.md` §3, `FA-13` (*Flat/Inline YAML Frontmatter Serialization*) appears at line 59, directly **before** `FA-05` at line 68.
- *Root Cause:* `FA-13` was codified during the canonical compression pass to resolve parser failures across zero-dependency YAML tools. It was placed at the opening of §3 (*OKF v0.2 Frontmatter Schemas*) because it defines the universal syntax governing all subsequent frontmatter schemas (`FA-05` root index and `FA-06` concept documents).
- *Durable ID Immutability (`WP-15`):* Renumbering `FA-13` to `FA-04b` or renumbering `FA-05..FA-12` would break external references, git commit histories, and automated test oracles (`test_canonical_ownership.py`).
- *Remediation Plan:* Maintain durable IDs as immutable anchors. Do not alter rule IDs to achieve mechanical numerical sequence.

---

## 4. Cross-Traceability Matrix to XML `<apex_contract>` and Ultra Contract

### 4.1 Upward Mapping to Contract Tags
Every file-architecture rule relevant to agent execution maps directly to tags in `<apex_contract v="1.0">` ([13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md)) and `16-candidate-3A-ultra.md`:

| Semantic Contract Tag | Mode | Mapped `FA` Rules | Key Semantic Obligations Codified in Contract |
|---|---|---|---|
| `<current_truth>` | Unconditional | `FA-01`, `FA-09`, `FA-11` | State active current truth only; isolate history in changelogs; eradicate dead names. |
| `<authoring>` | Gated (`index.md`) | `FA-13`, `FA-06`, `FA-02`, `FA-10` | Flat YAML frontmatter; mandatory concept fields; front-load rules; single-topic documents. |
| `<target>` | Unconditional | `FA-04` | Substance over ceremony exception authority; target realization overrides metric ceilings. |
| `<pointers>` | Terminal Guard | `FA-08` | Relative path resolution; boundary pruning across isolated sub-bundles. |

---

### 4.2 Analysis of the 6 "Unmapped" Rules
Six rules in `file-architecture.md` are not explicitly cited in the Layer 0 contract block:
1. `FA-03` (Five-Plane Information Separation)
2. `FA-04` (Substance Over Ceremony pointer to `WP-01`)
3. `FA-05` (Root `index.md` Specification)
4. `FA-07` (Unique Durable Identifiers pointer to `WP-15`)
5. `FA-08` (Sub-Bundle Isolation Boundary)
6. `FA-12` (Plane Sizing & Instruction Parsimony pointer to `WP-18`)

**Inclusion Rationale for Plane 4:**
These 6 rules govern **repository topology, directory boundaries, and bundle validation** rather than agent execution steps:
- `FA-03` governs the macro repository structure (separating system prompts from skills and evidence), which is configured by repository architects rather than executed in an agent's inner loop.
- `FA-05` and `FA-08` establish offline validator crawler behavior for `okf_validator.py`.
- `FA-04`, `FA-07`, and `FA-12` are canonical pointers that maintain standalone self-sufficiency for agents loading `file-architecture.md` without loading the entire suite (`WP-23`).

---

### 4.3 Upstream Empirical Grounding & Research Links
The rules in `file-architecture.md` are grounded in foundational research:
- **`FA-01` & `FA-11`:** Grounded in [A11-current-truth-authoritative-state/README.md](../01-universal-instruction-research/module-deepening/A11-current-truth-authoritative-state/README.md) and [RESULTS-03-currency-check.md](../03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-03-currency-check.md), which showed that inline changelogs dilute model attention and cause 37% more regressions on updated APIs.
- **`FA-03` & `FA-12`:** Grounded in [RESULTS-10-surface-layering.md](../03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-10-surface-layering.md) (Research Packet RP-09/RP-10), demonstrating that separating prompt carriers into an immutable Layer 1 universal block and a Layer 2 repo-specific block enables 90%+ prompt cache hit rates across major LLM providers.
- **`FA-13`:** Grounded in operational incident D9 and parser testing in [standard.md](../../specs/standard.md), proving that zero-dependency line parsers require a colon on every frontmatter line.

---

## 5. Module Failure Modes & Not-To-Dos (`WP-25`)

In accordance with `WP-25` (*Terminal-Position Operative Content*), this audit concludes with non-negotiable operational boundaries and anti-patterns for anyone editing or implementing `file-architecture.md`:

- **Never Embed Inline Changelogs in Live Specifications (`FA-01` Violation):** Do not record revision histories, previous syntax iterations, or deprecated options inside active documents. Always isolate historical records in `log.md` or dedicated archive folders.
- **Never Use Multiline YAML Lists in Frontmatter (`FA-13` Violation):** Always serialize frontmatter arrays using inline bracket syntax (`tags: [a, b]`). Multiline `- item` lists break zero-dependency custom parsers.
- **Never Mix Architecture Planes in a Single File (`FA-03` Violation):** Do not merge system instructions (Plane 1), scoped rules (Plane 2), procedural skills (Plane 3), knowledge bundles (Plane 4), and logs (Plane 5). Monolithic files trigger context clash and prevent targeted JIT reloading.
- **Never Renumber Durable Rule IDs to Fix Numerical Sequence (`WP-15` Violation):** Placing `FA-13` before `FA-05` is an intentional thematic arrangement. Renumbering durable IDs destroys cross-reference stability across the repository.
- **Never Rely on Machine-Specific Absolute Paths (`RBL-05` Violation):** Never write `file:///c:/...` or Windows backslashes in markdown links. Always use portable, repository-relative paths (`[Target]` (path/to/file.md)).
- **Never Bypass Sub-Bundle Boundaries in Automated Crawlers (`FA-08` Violation):** Validators must cease directory recursion upon encountering an independent `index.md` to prevent staging noise from polluting production bundles.
