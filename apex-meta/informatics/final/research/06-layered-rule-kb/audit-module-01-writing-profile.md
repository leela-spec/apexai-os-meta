---
type: Reference
id: V2-AUDIT-MODULE-01-WRITING-PROFILE
title: Module Audit 01 — Writing Profile & Prose Ergonomics Semantic Block & Ownership Audit
description: Comprehensive rule-by-rule semantic block decomposition, WP-23 single-ownership ledger, redundancy purge, and cross-traceability audit for writing-profile.md.
status: current_truth
tags: [module-audit, plane-4, writing-profile, single-owner, semantic-blocks, traceability]
---

# Module Audit 01: Writing Profile & Prose Ergonomics (`writing-profile.md`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (`<communication>`, `<authoring>`, `<target>`, `<ground>`, `<reuse>`)
> - **Layer 1 (Layered Rule KB):** [rule-01-target.md](rule-01-target.md), [rule-04-communication.md](rule-04-communication.md), [rule-06-ground.md](rule-06-ground.md), [rule-07-reuse.md](rule-07-reuse.md), [rule-16-authoring.md](rule-16-authoring.md)
> - **Layer 2 (Audited Canonical Module):** [writing-profile.md](../../../writing-profile.md) (`WP-01` through `WP-25`)
> - **Upstream Research & Empirical Lore:** [standard.md](../../../standard.md), [RESULTS-09-efficiency-audit.md](../03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md), [RESULTS-04-register-terminology.md](../03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-04-register-terminology.md), [A01-target-outcome-alignment/README.md](../01-universal-instruction-research/module-deepening/A01-target-outcome-alignment/README.md), [Snippets.md](../../../../AI-Snippets/Snippets.md), [2Dos Ai Instructions.md](../../../../AI-Snippets/Orga/2Dos%20Ai%20Instructions.md)

---

## 1. Module Scope, Architectural Role & Governed Rule Inventory

### 1.1 Architectural Domain & Loading Lifecycle
`writing-profile.md` is the canonical Plane 4 specification governing technical prose ergonomics, Information Mapping, Simplified Technical English (STE), visual block sizing, durable identifiers, and significance ranking across Apex OS.

Within the **Five-Plane Information Architecture** ([file-architecture.md](../../../file-architecture.md) `FA-03`), `writing-profile.md` operates as a specialized knowledge module:
- **JIT Activation Trigger:** An autonomous agent loads `writing-profile.md` when drafting, refactoring, or auditing repository documentation, technical specifications, governance schemas, prompt cards, or architectural decision records.
- **Scope Containment (`WP-09`):** Formal writing profile constraints are strictly restricted to governed repository knowledge artifacts. Casual chat interactions, raw application source code, and unformatted execution logs are explicitly exempt.
- **Top-Loaded Ergonomics:** The module front-loads its non-negotiable clarity invariants (`WP-01` through `WP-09`) in the first ~500 tokens, establishing substance over ceremony, imperative single-command sentences, active voice, and raw 3-metric significance tagging.

---

### 1.2 Comprehensive Governed Rule Inventory

The live `writing-profile.md` defines **25 governed rules** across three functional sections. The table below documents every rule, its priority tier, raw 3-metric significance rating, formal scope, inputs, outputs, halt conditions, and canonical ownership.

| # | Category | Rule ID | Tier & Metrics | Title | Description & Scope | Inputs / Preconditions | Outputs / Behaviors | Error / Halt Behavior | Canonical Owner |
|---|---|---|:---:|---|---|---|---|---|:---:|
| 1 | Prose Core | `WP-01` | `[P0 \| I98/E98/R05]` | Substance Over Ceremony Invariant | Technical accuracy and target intent strictly override mechanical metric compliance. | Drafting or reviewing any text. | Authorizes relaxing limits when accuracy demands. | Reject mechanical cuts that compromise correctness. | **WP-01 (Owner)** |
| 2 | Syntax | `WP-02` | `[P0 \| I96/E95/R08]` | Single Command Invariant | Encode one clear imperative command per procedural sentence. | Authoring procedural steps. | Splits compound instructions into single imperatives. | Flag compound sentences with multiple commands. | **WP-02 (Owner)** |
| 3 | Syntax | `WP-03` | `[P0 \| I95/E96/R05]` | Imperative Verbs & Zero Modal Hedging | Active imperative verbs; no empty modal hedges (`should`, `may`, `might`). | Authoring directives. | Uses RFC 2119 imperatives; plain warranted uncertainty. | Flag weak modal suggestions. | **WP-03 (Owner)** |
| 4 | Grounding | `WP-04` | `[P0 \| I95/E98/R05]` | Grounded Evidence vs Unanchored Citation | Ground factual assertions in direct primary inspection (`path:line` or tool output). | Making factual claims. | Cites primary file/tool output directly. | Reject unanchored memory citations. | `AD-19` |
| 5 | Register | `WP-05` | `[P0 \| I94/E95/R07]` | Clear Active-Voice Language | Active voice with explicit actors; Cool Blue analytical register. | Any communication/text. | High density, objective, no flattery or unearned agreement. | Flag passive voice and conversational filler. | **WP-05 (Owner)** |
| 6 | Layout | `WP-06` | `[P0 \| I94/E97/R06]` | Top-Loaded Positional Primacy | Front-load critical invariants in first ~500 tokens before attention decays. | Ordering document sections. | P0 rules placed near the top before attention decays. | Flag inverted priority ordering. | **WP-06 (Owner)** |
| 7 | Ranking | `WP-07` | `[P0 \| I93/E95/R07]` | Raw 3-Metric Significance Ranking | Tag governed rules with `[P<tier> \| I<val>/E<val>/R<val>]` (1–100 scale). | Defining rules or options. | Keeps Impact, Evidence, Risk distinct and unaggregated. | Reject synthetic calculated formulas. | **WP-07 (Owner)** |
| 8 | Hygiene | `WP-08` | `[P0 \| I92/E95/R06]` | Stale Residual Eradication | Purge all residual traces of deleted component names, old concepts, or aliases. | Documenting active systems. | Removes dead component names from active rules. | Flag mentions of retired architectures. | `AD-15` |
| 9 | Boundary | `WP-09` | `[P0 \| I92/E95/R08]` | Adaptive Scope Boundary | Apply profile only to governed repository knowledge artifacts. | Writing code, logs, or chat. | Exempts chat, source code, and logs from formal rules. | Flag imposing OKF rules on casual chat. | **WP-09 (Owner)** |
| 10 | Structure | `WP-10` | `[P1 \| I92/E95/R08]` | Information Mapping ("One Chunk, One Job") | Partition documents into modular, labeled visual blocks. | Formatting complex topics. | One cognitive task per visual block. | Flag intermingling theory, steps, and reference. | **WP-10 (Owner)** |
| 11 | Structure | `WP-11` | `[P1 \| I91/E94/R08]` | Table vs List vs Prose Selection | Tables for comparisons/schemas, bullets for criteria, numbers for sequence. | Organizing data. | Selects optimal Markdown visual vehicle. | Flag using numbered lists for unordered items. | **WP-11 (Owner)** |
| 12 | Primacy | `WP-12` | `[P1 \| I90/E94/R08]` | Minto Bottom Line Up Front (BLUF) | Lead sections and blocks with the conclusion or directive in sentence one. | Structuring paragraphs. | Conclusion first; background and evidence follow. | Flag bury-the-lede narrative introductions. | **WP-12 (Owner)** |
| 13 | Sizing | `WP-13` | `[P1 \| I89/E92/R10]` | Visual Block Prose Orientation (~150 Words) | Break continuous prose into tables/lists when approaching ~150 words. | Writing narrative paragraphs. | Converts dense paragraphs into structured blocks. | Advisory warning if prose is bloated. | **WP-13 (Owner)** |
| 14 | Sizing | `WP-14` | `[P1 \| I88/E92/R10]` | Concise Sentence Orientation (~20–25 Words) | Target ~20 words in procedural and ~25 in descriptive sentences. | Authoring sentences. | Keeps sentences scannable; expands when precision demands. | Advisory gate fires at >30 words. | **WP-14 (Owner)** |
| 15 | Identifiers | `WP-15` | `[P1 \| I91/E93/R08]` | Tier-Agnostic Durable IDs | Assign immutable canonical identifiers (`WP-01`, `FA-01`). | Assigning rule IDs. | Keeps ID string constant even when priority tier evolves. | Flag embedding priority in ID (`WP-P2-01`). | **WP-15 (Owner)** |
| 16 | Grounding | `WP-16` | `[P1 \| I89/E92/R08]` | Command-Carrying Claims | Accompany absence/zero/count claims with reproduction command and scope. | Reporting zero/absence findings. | Includes exact command and scope with the claim. | Flag unverified negative claims. | `AD-20` |
| 17 | Reuse | `WP-23` | `[P1 \| I90/E92/R08]` | Single-Owner Instruction Reuse | Reuse canonical instruction; never duplicate schemas, tables, or examples. | Referring to existing rule. | Links owner; keeps only one-line operative imperative. | Reject copying full schemas into second file. | **WP-23 (Owner)** |
| 18 | Examples | `WP-17` | `[P2 \| I86/E90/R08]` | High-Signal Compact Examples | Include compact 1-line `<correct>` vs `<wrong>` micro-examples. | Clarifying ambiguous rules. | Delivers paired micro-examples; avoids narrative stories. | Flag verbose narrative examples. | **WP-17 (Owner)** |
| 19 | Sizing | `WP-18` | `[P2 \| I85/E90/R10]` | Universal Instruction Parsimony | Keep active directives concise (~30–50 max per standalone file). | Authoring specification files. | Offloads specialized logic to JIT sub-modules. | Flag monolithic rule-walls. | **WP-18 (Owner)** |
| 20 | Syntax | `WP-19` | `[P2 \| I84/E92/R08]` | Syntax Exemptions | Code blocks, tables, URLs, paths, and logs exempt from prose limits. | Sizing validation. | Excludes structured blocks from prose word counts. | Prevents false-positive length violations. | **WP-19 (Owner)** |
| 21 | Efficiency | `WP-20` | `[P2 \| I82/E88/R08]` | No Default-Behavior Rules | Codify only non-obvious rules preventing recurring errors. | Adding instructions. | Omits directives models already follow by default. | Flag spending tokens on RLHF truisms. | **WP-20 (Owner)** |
| 22 | Layout | `WP-21` | `[P2 \| I80/E86/R10]` | Heading Depth Orientation (~3 Levels) | Prefer up to ~3 heading levels (`#`, `##`, `###`) for scannability. | Structuring document outline. | Uses bold run-in labels or tables for deep hierarchy. | Flag gratuitous 4+ heading nesting. | **WP-21 (Owner)** |
| 23 | Links | `WP-24` | `[P2 \| I82/E90/R06]` | Clickable File References | Render every repository file listed as a clickable Markdown link. | Listing file paths. | Wraps paths in `[Name]` (path) for instant navigation. | Flag raw unclickable file paths. | **WP-24 (Owner)** |
| 24 | Primacy | `WP-25` | `[P2 \| I80/E86/R06]` | Terminal-Position Operative Content | Close files with operative content (failure modes / guards). | Structuring file conclusion. | Puts references before closing block; ends on guard. | Flag wasting terminal position on link lists. | **WP-25 (Owner)** |
| 25 | Appendix | `WP-22` | `[P3 \| I72/E80/R10]` | Non-Normative Appendix & Typographic Cleanliness | Historical rationale in dedicated appendices; backtick quotes for code. | Formatting appendices. | Isolates history; formats commands and code cleanly. | Flag inline historical digressions. | **WP-22 (Owner)** |

---

### 1.3 Atomic Semantic Block Inventory (`SB-WP-01`..`SB-WP-25`)

Every rule in `writing-profile.md` decomposes into atomic semantic blocks that isolate discrete obligations:

- **`WP-01` (Substance Over Ceremony Invariant):**
  - `SB-WP-01.1` (*Outcome Dominance*): Realize substantive technical accuracy and target intent above mechanical metric compliance.
  - `SB-WP-01.2` (*Exception Authority*): Authors and agents possess explicit authority to exceed approximate ceilings or relax stylistic constraints when required for correctness.
  - `SB-WP-01.3` (*Anti-Mechanical-Harm Guard*): Forbid arbitrary mechanical cuts that omit load-bearing context, compromise safety, or produce unnatural prose.
- **`WP-02` (Single Command Invariant):**
  - `SB-WP-02.1` (*Imperative Atomicity*): Encode one clear imperative command per procedural sentence.
  - `SB-WP-02.2` (*Compound Ban*): Do not bundle multiple mutating or procedural instructions into compound sentences with commas or conjunctions.
- **`WP-03` (Imperative Verbs & Zero Modal Hedging):**
  - `SB-WP-03.1` (*Active Opening*): Start procedural directives with an active imperative verb.
  - `SB-WP-03.2` (*Modal Ban*): Avoid empty modal hedges (`should`, `may`, `might`, `could`); express mandatory requirements using direct imperatives or RFC 2119 keywords (`MUST`, `MUST NOT`).
  - `SB-WP-03.3` (*Epistemic Warrant*): State genuine uncertainty plainly when empirical evidence is incomplete.
- **`WP-04` (Grounded Evidence vs Unanchored Citation):**
  - `SB-WP-04.1` (*Primary Anchor*): Ground every factual assertion in direct primary inspection (`path:line` or verified tool output).
  - `SB-WP-04.2` (*Secondary Ban*): Never cite secondary summaries, self-referential audits, or ungrounded model memory (delegates to `AD-19`).
- **`WP-05` (Clear Active-Voice Language):**
  - `SB-WP-05.1` (*Active Actor*): Write in clear, plain active voice with explicit actors for every action.
  - `SB-WP-05.2` (*Cool Blue Register*): Maintain a crisp analytical register: direct, structured, objective, and evidence-led, without flattery or sycophancy.
  - `SB-WP-05.3` (*Comprehension Primacy*): Prioritize immediate human and machine comprehension over dense academic ornamentation.
- **`WP-06` (Top-Loaded Positional Primacy):**
  - `SB-WP-06.1` (*Positional Primacy*): Front-load critical invariants, non-negotiable boundaries, and BLUF conclusions near the document top.
  - `SB-WP-06.2` (*Attention Budget*): Target the first ~500 tokens before attention density decays.
- **`WP-07` (Raw 3-Metric Significance Ranking):**
  - `SB-WP-07.1` (*Tagging Syntax*): Tag governed rules and options with `[P<tier> | I<impact>/E<evidence>/R<risk>]` on a raw 1–100 scale.
  - `SB-WP-07.2` (*Unaggregated Dimensions*): Keep Impact, Evidence, and Risk distinct; forbid synthetic mathematical aggregation formulas.
  - `SB-WP-07.3` (*Sorting Order*): Order rules descending by priority tier (`P0` → `P3`).
  - `SB-WP-07.4` (*Canonical Metric Ownership*): Act as the suite's canonical owner of tier classifications (P0–P3) and dimension definitions.
- **`WP-08` (Stale Residual Eradication):**
  - `SB-WP-08.1` (*Dead Alias Purge*): Purge all residual traces of deleted component names, retired concepts, or obsolete aliases from active documentation.
  - `SB-WP-08.2` (*Hallucination Guard*): Prevent downstream ghost-reasoning and drift caused by referencing retired names (delegates to `AD-15`).
- **`WP-09` (Adaptive Scope Boundary):**
  - `SB-WP-09.1` (*Governed Scope*): Enforce writing profile constraints exclusively on governed repository knowledge artifacts.
  - `SB-WP-09.2` (*Casual Exemption*): Never impose formal frontmatter, STE limits, or block structures onto casual chat, application source code, or raw logs.
- **`WP-10` (Information Mapping "One Chunk, One Job"):**
  - `SB-WP-10.1` (*Visual Block Partitioning*): Partition documents into modular, labeled visual blocks.
  - `SB-WP-10.2` (*Single Cognitive Task*): Assign each block a single cognitive task; do not intermingle theory, steps, and reference data in the same block.
- **`WP-11` (Table vs List vs Prose Selection):**
  - `SB-WP-11.1` (*Vehicle Calibration*): Use Markdown tables for comparisons/schemas, bullets for unordered criteria, and numbers strictly for sequential workflows.
- **`WP-12` (Minto Bottom Line Up Front - BLUF):**
  - `SB-WP-12.1` (*Sentence-One Conclusion*): Lead sections and blocks with the definitive conclusion or directive in sentence one; support rationale follows.
- **`WP-13` (Visual Block Prose Orientation):**
  - `SB-WP-13.1` (*Paragraph Ceiling*): Break continuous prose into tables, lists, or sub-blocks when approaching ~150 words.
- **`WP-14` (Concise Sentence Orientation):**
  - `SB-WP-14.1` (*Target Word Budget*): Target ~20 words in procedural directives and ~25 words in descriptive statements.
  - `SB-WP-14.2` (*Target vs Gate Calibration*): Clarify that the advisory gate fires at >30 words; sentences between target and gate are acceptable.
- **`WP-15` (Tier-Agnostic Durable IDs):**
  - `SB-WP-15.1` (*Immutable Identifier*): Assign immutable canonical IDs (`WP-01`, `FA-01`) without embedding mutable priority tiers inside the ID string.
  - `SB-WP-15.2` (*Cross-Reference Stability*): Allow headings, titles, and tiers to evolve while durable IDs remain fixed.
- **`WP-16` (Command-Carrying Claims):**
  - `SB-WP-16.1` (*Reproducibility Command*): Accompany every statement of absence, zero count, or benchmark metric with the reproducible command and scope (delegates to `AD-20`).
- **`WP-23` (Single-Owner Instruction Reuse):**
  - `SB-WP-23.1` (*Reference Over Duplication*): Reference canonical owners; never duplicate schemas, tables, JSON blocks, or worked examples into a second file.
  - `SB-WP-23.2` (*Operative Restatement*): Restate only the one-line operative imperative needed for JIT self-sufficiency.
  - `SB-WP-23.3` (*Drift Prevention*): Prevent copies from drifting into contradictions that degrade instruction-following.
- **`WP-17` (High-Signal Compact Examples):**
  - `SB-WP-17.1` (*Micro-Example Pairs*): Include compact 1-line `<correct>` vs `<wrong>` micro-examples; avoid multi-paragraph narrative stories.
- **`WP-18` (Universal Instruction Parsimony):**
  - `SB-WP-18.1` (*Directive Ceiling*): Keep active imperative directives concise (~30–50 max per standalone file); offload specialized domains JIT.
- **`WP-19` (Syntax Exemptions):**
  - `SB-WP-19.1` (*Block Sizing Exemption*): Code blocks, inline code, tables, URLs, paths, and logs are exempt from prose word-count orientations.
- **`WP-20` (No Default-Behavior Rules):**
  - `SB-WP-20.1` (*Token Economy on Truisms*): Codify only directives preventing recurring failure modes; omit generic rules models already follow by default.
- **`WP-21` (Heading Depth Orientation):**
  - `SB-WP-21.1` (*Heading Hierarchy Ceiling*): Prefer up to ~3 heading levels (`#`, `##`, `###`) for scannability; use bold run-in labels for deeper structures.
- **`WP-24` (Clickable File References):**
  - `SB-WP-24.1` (*Direct Navigation*): Render every repository file listed or cited as a clickable Markdown link (`[Name]` (path)).
- **`WP-25` (Terminal-Position Operative Content):**
  - `SB-WP-25.1` (*Closing Primacy*): Close governed specification files with operative content (failure modes or actionable guards); place reference links before closing block.
- **`WP-22` (Non-Normative Appendix & Typographic Cleanliness):**
  - `SB-WP-22.1` (*Historical Isolation*): Place extensive historical rationale in dedicated appendices or separate files; maintain consistent backtick quoting.

---

## 2. Single-Ownership Verification Ledger (`WP-23`)

### 2.1 Rules Canonically Owned by `writing-profile.md` (22 Rules)
`writing-profile.md` canonically defines 22 rules that establish repository-wide standards:
1. `WP-01` — Substance Over Ceremony Invariant (root authority for pragmatic metric relaxing)
2. `WP-02` — Single Command Invariant (STE procedural syntax)
3. `WP-03` — Imperative Verbs & Zero Modal Hedging (RFC 2119 directive register)
4. `WP-05` — Clear Active-Voice Language (Insights Discovery Cool Blue register)
5. `WP-06` — Top-Loaded Positional Primacy (attention curve optimization)
6. `WP-07` — Raw 3-Metric Significance Ranking (canonical owner of P0–P3 and I/E/R 1–100 scales)
7. `WP-09` — Adaptive Scope Boundary (formal boundary between repo docs and casual chat)
8. `WP-10` — Information Mapping ("One Chunk, One Job" modular visual blocks)
9. `WP-11` — Table vs List vs Prose Selection (structural vehicle calibration)
10. `WP-12` — Minto Bottom Line Up Front (BLUF leading directive)
11. `WP-13` — Visual Block Prose Orientation (~150 words per paragraph)
12. `WP-14` — Concise Sentence Orientation (~20–25 words per sentence)
13. `WP-15` — Tier-Agnostic Durable IDs (canonical grammar owner for `XX-NN` identifiers)
14. `WP-23` — Single-Owner Instruction Reuse (meta-rule for instruction deduplication)
15. `WP-17` — High-Signal Compact Examples (paired micro-example discipline)
16. `WP-18` — Universal Instruction Parsimony (~30–50 directive ceiling)
17. `WP-19` — Syntax Exemptions (validator sizing exemptions for code/tables)
18. `WP-20` — No Default-Behavior Rules (ban on token-wasting RLHF truisms)
19. `WP-21` — Heading Depth Orientation (~3 heading levels max)
20. `WP-24` — Clickable File References (all cited repo files must be links)
21. `WP-25` — Terminal-Position Operative Content (closing positions must contain actionable guards)
22. `WP-22` — Non-Normative Appendix & Typographic Cleanliness (isolation of historical rationale)

---

### 2.2 The Meta-Governance Role of `WP-23`
`writing-profile.md` is the constitutional home of `WP-23` (*Single-Owner Instruction Reuse*). This rule is the foundational architectural invariant that governs instruction deduplication across all Plane 4 modules:
> *"Reuse an existing instruction instead of restating it. When a concept already has a canonical owner in this suite, reference that owner; never copy its schema, table, JSON block, or worked example into a second file. Restate only the one-line operative imperative a module needs to remain self-sufficient when loaded alone."*

The single-ownership discipline resolves the trade-off between **JIT Self-Sufficiency** (an agent loading a single file must understand critical constraints) and **Drift Prevention** (duplicate multi-line blocks diverge, introducing silent system bugs).

---

### 2.3 Sibling Rules Referencing `writing-profile.md` Definitions (12 Delegations)
Twelve rules across the other four Plane 4 modules explicitly cite definitions canonically owned by `writing-profile.md`:

| Sibling File | Sibling Rule | Delegated Definition from `writing-profile.md` | Relationship & Scope |
|---|---|---|---|
| `file-architecture.md` | `FA-02` | `WP-06` & `WP-07` | Cites top-loaded primacy and `WP-07` for priority tier & metric definitions. |
| `file-architecture.md` | `FA-04` | `WP-01` | Cites substance over ceremony exception authority for file architecture. |
| `file-architecture.md` | `FA-07` | `WP-15` | Cites durable identifier grammar for concept document metadata. |
| `file-architecture.md` | `FA-12` | `WP-18` | Cites instruction parsimony directive ceiling for plane sizing. |
| `anti-drift-rules.md` | `AD-08` | `WP-01` | Restates substance over ceremony operative imperative for operational lore. |
| `anti-drift-rules.md` | `AD-17` | `WP-12` | Restates Minto BLUF operative directive for engineering communications. |
| `anti-drift-rules.md` | `AD-26` | `WP-18` | Cites instruction parsimony directive ceiling for standalone rule files. |
| `governance-schemas.md` | `GS-03` | `WP-06` | Restates top-loaded primacy for schema specifications. |
| `governance-schemas.md` | `GS-04` | `WP-07` | Cites raw 3-metric significance tagging syntax and rules. |
| `governance-schemas.md` | `GS-08` | `WP-15` | Cites durable identifier uniqueness validation. |
| `governance-schemas.md` | `GS-14` | `WP-18` | Enforces universal instruction parsimony directive ceiling. |
| `governance-schemas.md` | `GS-17` | `WP-07` | Enforces ranking conformance based on `WP-07` tier definitions. |

---

### 2.4 Rules Within `writing-profile.md` Delegating to External Canonical Owners (3 Delegations)
`writing-profile.md` delegates 3 rules to external canonical owners in `anti-drift-rules.md`:

| Local Rule | Priority Tier | Target Canonical Owner | Owner File | Delegation Scope & Deliberate Priority Nuance |
|---|:---:|---|---|---|
| `WP-04` | **P0** | `AD-19` | `anti-drift-rules.md` | Grounded Evidence vs Unanchored Citation. *Deliberate Priority Elevation:* In technical writing, ungrounded citations immediately corrupt knowledge documents (P0 invariant); in broad operational lore, it is a standard grounding method (P1). |
| `WP-08` | **P0** | `AD-15` | `anti-drift-rules.md` | Stale Residual Eradication. *Deliberate Priority Elevation:* Mentioning retired components in active specifications triggers model hallucinations and resurrection of dead workflows (P0 invariant); in general repository cleanup, it is ranked P1. |
| `WP-16` | **P1** | `AD-20` | `anti-drift-rules.md` | Command-Carrying Claims. Both files rank this P1 method: claims of absence or zero metrics must carry reproducible commands. |

---

### 2.5 Mechanical Verification Evidence (`test_canonical_ownership.py`)
Deterministic verification via `test_canonical_ownership.py` confirms 100% adherence to `WP-23` across `writing-profile.md`:
1. **Rule Prefix Integrity:** All 25 rules begin with `WP-`, and no `WP-` rules are defined in any other file (`test_rule_id_prefix_matches_its_home_file`).
2. **Rule ID Uniqueness:** Zero duplicate IDs exist within `writing-profile.md` (`test_no_duplicate_rule_id_within_a_file`).
3. **Pointer Resolution:** All 3 canonical pointers (`AD-19`, `AD-15`, `AD-20`) resolve to active rules defined in `anti-drift-rules.md` (`TestCanonicalPointerIntegrity`).
4. **Zero Self-Referential Pointers:** `writing-profile.md` contains zero `Canonical: `WP-xx`` references (`test_canonical_pointer_never_targets_its_own_file`).

---

## 3. Redundancy & Stale Terminology Remediation Plan

### 3.1 Cross-Module Redundancy Clusters Involving `writing-profile.md`
The audit identified 6 prominent concept clusters where `writing-profile.md` intersects with other modules:

1. **Substance Over Ceremony Invariant (`WP-01` [P0] vs `FA-04` [P0] vs `AD-08` [P0]):**
   - *Current State:* Three separate files define a P0 invariant asserting that technical accuracy and target realization override mechanical metric compliance.
   - *Assessment:* Fully compliant with `WP-23`. Each file restates only the one-line operative imperative necessary for JIT self-sufficiency without duplicating historical rationale.
2. **Positional Primacy & BLUF (`WP-06` [P0] & `WP-12` [P1] vs `FA-02` [P0], `GS-03` [P0], `AD-17` [P1]):**
   - *Current State:* `WP-06` and `WP-12` govern the cognitive principles of top-loaded primacy and Minto BLUF. Sibling files cite or restate these principles for their respective domains.
   - *Remediation Plan:* In future consolidations, keep `WP-06` as the single canonical statement of token-decay attention curves, and ensure sibling files maintain single-line pointers.
3. **Raw 3-Metric Significance Ranking (`WP-07` [P0] vs `GS-04` [P0], `GS-17` [P2], `FA-02` [P0]):**
   - *Current State:* `WP-07` owns the definition of the 3 metrics (`I/E/R`) and 4 tiers (`P0–P3`). `GS-04` and `GS-17` enforce the validation view in CI.
   - *Remediation Plan:* Maintain `WP-07` as the single authoritative table of metric dimensions. `governance-schemas.md` should purely state the parsing regex and rejection conditions.
4. **Instruction Parsimony Ceiling (`WP-18` [P2] vs `FA-12` [P2], `AD-26` [P2], `GS-14` [P2], `GS-15` [P2]):**
   - *Current State:* Five files reference the ~30–50 directive ceiling. `GS-15` defines how directives are counted.
   - *Remediation Plan:* Unify the operational ceiling under `WP-18`, with `GS-15` serving strictly as the measurement methodology.
5. **Durable Identifier Grammar (`WP-15` [P1] vs `FA-07` [P1], `GS-08` [P1]):**
   - *Current State:* `WP-15` defines the grammar (`XX-NN` tier-agnostic), `FA-07` mandates it for frontmatter, and `GS-08` checks bundle uniqueness.
   - *Remediation Plan:* Clean functional division; no remediation required.
6. **Prose and Sentence Sizing Calibration (`WP-13` ~150 words & `WP-14` ~20–25 words):**
   - *Current State:* `WP-13` targets paragraph sizing (~150 words), while `WP-14` targets sentence sizing (~20–25 words).
   - *Remediation Opportunity:* Both rules operate as scannability heuristics. In downstream library refactoring, they can be presented as a paired "Scannability Sizing Duo" to reduce prose token overhead.

---

### 3.2 Stale Terminology & Legacy Structural Nuances

1. **Out-of-Numerical-Sequence Rule Placements:**
   - In §3 of `writing-profile.md`, `WP-23` (*Single-Owner Instruction Reuse*) appears at line 59, directly between `WP-16` and `WP-17`.
   - In addition, `WP-24` (*Clickable File References*) and `WP-25` (*Terminal-Position Operative Content*) appear before `WP-22` (*Non-Normative Appendix*).
   - *Explanation:* Rules `WP-23`, `WP-24`, and `WP-25` were introduced during the canonical ownership and ergonomics compression passes. Per `WP-15`, durable rule IDs are immutable anchors. Renumbering existing IDs to restore chronological sequencing would break external cross-references and test oracles.
   - *Remediation Plan:* Keep durable IDs strictly immutable. Document the thematic grouping in section headers rather than modifying ID strings.
2. **Simplified Technical English (STE) Terminology:**
   - The diagnostic rule is named `STE-SENTENCE-LENGTH`, but `writing-profile.md` applies a pragmatic adaptation of ASD-STE100 tailored for AI prompt engineering.
   - *Remediation Plan:* Clarify in upstream reference documentation that Apex STE is an engineering adaptation emphasizing cognitive density rather than pure aerospace compliance.

---

## 4. Cross-Traceability Matrix to XML `<apex_contract>` and Ultra Contract

### 4.1 Upward Mapping to Contract Tags
Every writing rule relevant to always-on agent execution maps directly to tags in `<apex_contract v="1.0">` ([13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md)) and the upcoming `16-candidate-3A-ultra.md`:

| Semantic Contract Tag | Mode | Mapped `WP` Rules | Key Semantic Obligations Codified in Contract |
|---|---|---|---|
| `<communication>` | Unconditional | `WP-02`, `WP-03`, `WP-04`, `WP-05`, `WP-12` | Active voice; 1 imperative per sentence; conclusion first; Cool Blue register; plain uncertainty. |
| `<authoring>` | Gated (`index.md`) | `WP-06`, `WP-07`, `WP-10`, `WP-19`, `WP-24`, `WP-25` | Front-load rules; Information Mapping blocks; tag `[P \| I/E/R]`; link every file; terminal guards. |
| `<target>` | Unconditional | `WP-01` | Technical accuracy overrides mechanical compliance; substance over ceremony. |
| `<scope>` | Unconditional | `WP-09` | Adaptive scope boundary: formal rules govern repo knowledge artifacts, not casual chat or code. |
| `<ground>` | Unconditional | `WP-04`, `WP-16` | Ground facts in primary artifacts (`path:line`); command-carrying absence claims. |
| `<reuse>` | Unconditional | `WP-23` | Single-owner instruction reuse; reference canonical owner; never duplicate schemas. |
| `<current_truth>` | Unconditional | `WP-08` | Eradicate stale residual names to prevent ghost reasoning. |
| `<pointers>` | Terminal Guard | `WP-25`, `WP-18` | Terminal position for operative guards; instruction parsimony. |

---

### 4.2 Analysis of the 8 "Unmapped" Rules
Eight rules in `writing-profile.md` are not explicitly cited in the Layer 0 contract block:
1. `WP-11` (Table vs List selection)
2. `WP-13` (Visual block ~150 words)
3. `WP-14` (Concise sentence ~20–25 words)
4. `WP-15` (Tier-agnostic durable ID grammar)
5. `WP-17` (High-signal compact examples)
6. `WP-20` (No default-behavior rules)
7. `WP-21` (Heading depth ~3 levels)
8. `WP-22` (Non-normative appendix & typographic cleanliness)

**Inclusion Rationale for Plane 4:**
These 8 rules represent **authoring heuristics and offline editing standards** rather than always-on execution boundaries. Embedding prose word counts (~150 words) or heading depth limits (~3 levels) into an always-on prompt carrier would waste high-value attention tokens on rules irrelevant to code modification or tool execution. They rightfully reside in Plane 4, where an agent drafting or refactoring documentation retrieves them just-in-time via `<authoring>`.

---

### 4.3 Upstream Empirical Grounding & Research Links
The rules in `writing-profile.md` synthesize foundational findings from the empirical research corpus:
- **`WP-01` & `WP-05`:** Grounded in [A01-target-outcome-alignment/README.md](../01-universal-instruction-research/module-deepening/A01-target-outcome-alignment/README.md) and [RESULTS-04-register-terminology.md](../03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-04-register-terminology.md), proving that Cool Blue analytical register reduces conversational sycophancy by 84%.
- **`WP-06` & `WP-25`:** Grounded in [RESULTS-09-efficiency-audit.md](../03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md), demonstrating that model attention is parabolic (highest at the first ~500 tokens and the terminal block).
- **`WP-07` & `WP-15`:** Grounded in operational lore from [Snippets.md](../../../../AI-Snippets/Snippets.md) and [2Dos Ai Instructions.md](../../../../AI-Snippets/Orga/2Dos%20Ai%20Instructions.md), establishing the raw `[P | I/E/R]` syntax without calculated composite scores.
- **`WP-20`:** Grounded in the Universal AI Instruction System parsimony research ([RESULTS-09-efficiency-audit.md](../03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md) §2), showing that codifying default RLHF assistant behaviors dilutes instruction-following for non-default constraints.

---

## 5. Module Failure Modes & Not-To-Dos (`WP-25`)

In accordance with `WP-25` (*Terminal-Position Operative Content*), this audit concludes with non-negotiable operational boundaries and anti-patterns for authors and agents editing or applying `writing-profile.md`:

- **Never Treat Approximate Ceilings as Rigid Walls (`WP-01` Violation):** Do not truncate critical technical parameters, delete safety warnings, or produce stilted, unnatural prose simply to stay under ~20 words per sentence or ~150 words per visual block. Substantive realization of the target always overrides mechanical metrics.
- **Never Embed Priority Tiers Inside Durable Identifiers (`WP-15` Violation):** Authoring `WP-P0-01` or `WP-P2-06` violates durable ID immutability. Priority tiers evolve as architectures mature; durable IDs must remain constant anchors across all revisions.
- **Never Calculate Synthetic Math Scores From `I/E/R` Metrics (`WP-07` Violation):** Do not compute `(I * E) / R` or aggregate `[P0 | I95/E95/R05]` into a single composite number. The three dimensions represent orthogonal operational qualities that must remain unaggregated.
- **Never Duplicate Schemas or Worked Examples Across Modules (`WP-23` Violation):** Never copy a JSON schema, markdown table, or formatting template from another Plane 4 module into `writing-profile.md`. Reference the canonical owner and state only the single-line operative imperative needed for standalone self-sufficiency.
- **Never Leave Residual Traces of Deleted Components in Active Rules (`WP-08` Violation):** Do not write migration rules such as "Do not use `<OldDeletedSystem>`" inside permanent specifications. State only the active current truth, and isolate migration guidance in dedicated changelogs or external notes.
- **Never Close a Specification File With Static Link Lists (`WP-25` Violation):** Never place upstream bibliography links or navigation footers at the bottom of a specification. Attention favors the terminal position; always close files with actionable failure-mode guards or operative execution rules.
