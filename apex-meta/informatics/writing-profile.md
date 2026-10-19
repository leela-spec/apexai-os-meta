---
type: Profile
id: apex-informatics-writing-profile
title: Apex Informatics Writing Profile & Prose Ergonomics
description: Canonical Apex OS specification governing technical prose ergonomics, Information Mapping, Simplified Technical English (STE), visual block sizing, durable identifiers, and significance ranking.
status: current
tags: [informatics, writing-profile, ste, information-mapping, ergonomics, ranking]
---

# Apex Informatics Writing Profile & Prose Ergonomics

## 1. Core Language, Clarity & Primacy Invariants

This section establishes the foundational prose, grounding, and significance rules governing technical writing and instruction authoring across Apex OS.

- **WP-01 [P0 | I98/E98/R05] Substance Over Ceremony Invariant**: Realize substantive technical accuracy and target intent above mechanical metric compliance. Authors and agents possess explicit authority to exceed approximate ceilings or relax stylistic constraints whenever strict adherence would omit load-bearing context, compromise correctness, or produce unnatural prose.
- **WP-02 [P0 | I96/E95/R08] Single Command Invariant**: Encode one clear imperative command per procedural sentence. Do not bundle multiple mutating or procedural instructions into compound sentences with commas or conjunctions.
- **WP-03 [P0 | I95/E96/R05] Imperative Verbs & Zero Modal Hedging**: Start procedural directives with an active imperative verb. Avoid modal hedging (`should`, `may`, `might`, `could`) in normative specifications; express mandatory behavior with direct imperative verbs or RFC 2119 keywords (`MUST`, `MUST NOT`).
- **WP-04 [P0 | I95/E98/R05] Grounded Evidence vs Unanchored Citation**: Ground every factual assertion in direct primary inspection (`path:line` or verified tool output). Never cite secondary summaries, self-referential audits, or ungrounded model memory.
- **WP-05 [P0 | I94/E95/R07] Clear Active-Voice Language**: Write in clear, plain active voice with explicit actors for every action (e.g., "The compiler builds the binary", not "The binary is built"). Prioritize immediate human and machine comprehension over dense academic phrasing.
- **WP-06 [P0 | I94/E97/R06] Top-Loaded Positional Primacy**: Front-load critical invariants, non-negotiable boundaries, and BLUF conclusions near the top of the document (aiming for roughly the first ~500 tokens as an orientation) before positional attention decays.
- **WP-07 [P0 | I93/E95/R07] Raw 3-Metric Significance Ranking**: Tag governed specification rules and decision options with raw qualitative/quantitative estimates `[P<tier> | I<impact>/E<evidence>/R<risk>]` on a 1–100 scale, keeping all three dimensions distinct and unaggregated. Order rules descending by priority tier (`P0` → `P3`).
- **WP-08 [P0 | I92/E95/R06] Stale Residual Eradication**: Purge all residual traces of deleted component names, retired concepts, or obsolete aliases from active documentation. Mentioning retired names in live rules triggers downstream ghost-reasoning and drift.
- **WP-09 [P0 | I92/E95/R08] Adaptive Scope Boundary**: Enforce formal writing profile constraints only on governed repository knowledge artifacts. Never impose formal frontmatter, STE limits, or block structures onto casual chat, application source code, or raw logs.

---

## 2. Information Mapping, Tables, Lists & Sentence Ergonomics

This section defines how to structure visual blocks, choose between tables and lists, and size sentences for rapid scanning.

- **WP-10 [P1 | I92/E95/R08] Information Mapping ("One Chunk, One Job")**: Structure every document into modular, labeled visual blocks. Assign each block a single cognitive task; do not intermingle conceptual theory, procedural steps, and reference data in the same paragraph.
- **WP-11 [P1 | I91/E94/R08] Table vs List vs Prose Selection**: Use Markdown tables for multi-attribute comparisons, routing maps, and structured schemas; use bullet lists for unordered criteria or inventories; use numbered lists strictly for sequential procedures.
- **WP-12 [P1 | I90/E94/R08] Minto Bottom Line Up Front (BLUF)**: Lead every section and block with the definitive conclusion, primary finding, or core directive in sentence one. Background rationale supports the conclusion and follows it.
- **WP-13 [P1 | I89/E92/R10] Visual Block Prose Orientation (~150 Words)**: Break continuous prose into structured tables, bullet lists, or sub-blocks when a paragraph approaches roughly ~150 words, unless continuous narrative is essential for a complex explanation.
- **WP-14 [P1 | I88/E92/R10] Concise Sentence Orientation (~20–25 Words)**: Keep sentences focused and scannable—aiming for roughly ~20 words in procedural directives and ~25 words in descriptive statements—while expanding naturally whenever technical precision requires it.

---

## 3. Identification, Examples & Instruction Parsimony

This section governs durable rule identifiers, evidence-backed claims, example design, and directive parsimony.

- **WP-15 [P1 | I91/E93/R08] Tier-Agnostic Durable IDs**: Assign immutable canonical identifiers (`WP-01`, `FA-01`, `AD-01`) to governed requirements without embedding mutable priority tiers inside the ID string. Headings, section titles, and priority tiers may evolve across revisions while durable IDs remain fixed.
- **WP-16 [P1 | I89/E92/R08] Command-Carrying Claims**: Accompany every statement of absence, zero count, or benchmark metric with the exact reproducible command and scope that produced it.
- **WP-17 [P2 | I86/E90/R08] High-Signal Compact Examples**: Include compact 1-line `<correct>` vs `<wrong>` micro-examples or concrete output templates whenever a rule or deliverable format could be misinterpreted; avoid multi-paragraph narrative stories.
- **WP-18 [P2 | I85/E90/R10] Universal Instruction Parsimony**: Keep active imperative directives per file concise (aiming for roughly ~30–50 directives max per standalone file) and offload specialized domains into JIT modules before a single file becomes an overloaded rule-wall.
- **WP-19 [P2 | I84/E92/R08] Syntax Exemptions**: Fenced code blocks, inline code, tables, URLs, file paths, and raw logs are exempt from prose word-count orientations.
- **WP-20 [P2 | I82/E88/R08] No Default-Behavior Rules**: Codify only directives that prevent recurring failure modes or establish non-obvious repository conventions; omit generic instructions that models already follow by default.
- **WP-21 [P2 | I80/E86/R10] Heading Depth Orientation (~3 Levels)**: Prefer up to ~3 Markdown heading levels (`#`, `##`, `###`) for scannability; use bold run-in labels or tables for finer subdivisions unless deep technical nesting genuinely aids clarity.
- **WP-22 [P3 | I72/E80/R10] Non-Normative Appendix & Typographic Cleanliness**: Place extensive historical rationale in dedicated appendices or separate files, and maintain consistent backtick quoting for identifiers, paths, and commands.

### Paired Directive Micro-Examples:

| Rule ID | Correct Example | Wrong Example |
|---|---|---|
| **WP-02** | `Validate the schema. Write the file.` | `Validate the schema, write the file, and notify the user.` |
| **WP-03** | `Return a single JSON object.` | `You should try to return a JSON object if possible.` |
| **WP-05** | `The executor verifies the hash.` | `The hash is verified.` |

---

## 4. Writing Failure Modes & Not-To-Dos

- **Do not treat approximate word/token targets as hard walls**: Never truncate a critical safety condition or write unnatural, broken sentences just to stay under ~20 words or ~500 tokens (`WP-01` Substance Over Ceremony always governs).
- **Do not embed priority levels inside Durable IDs**: Writing `WP-P2-01` breaks ID immutability the moment the rule's priority changes.
- **Do not aggregate or compute synthetic scores from `I/E/R` metrics**: Always keep Impact, Evidence, and Risk as three distinct raw numbers (`I90/E95/R10`); never combine them into a single calculated number.
- **Do not leave retired names in live rules**: Do not write "Stop using `<OldDeletedSystem>`" inside a permanent specification; state only the active current truth, or isolate migration warnings in a dedicated migration/changelog file.

---

## 5. Future Architecture Note & Traceability

> **Candidate Idea for Universal Always-On Root Instructions (`CLAUDE.md` / `AGENTS.md` / Router):**
> While `WP-02` (Single Command), `WP-03` (Imperative Verbs & Zero Modal Hedging), and `WP-05` (Clear Active-Voice Language) must remain separate, granular rules inside this dedicated writing profile, they can be rolled into a single ultra-compact P0 directive exclusively inside the always-on root agent instruction surface to save root control-plane tokens.

- **Upstream Reference**: [Apex Informatics Standard](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/standard.md) (Sections 5, 6, 10, 12, 13)
- **Operational Lore**: [Snippets.md](file:///c:/GitDev/apexai-os-meta/apex-meta/AI-Snippets/Snippets.md) & [2Dos Ai Instructions.md](file:///c:/GitDev/apexai-os-meta/apex-meta/AI-Snippets/Orga/2Dos%20Ai%20Instructions.md)
- **Conformance Engine**: [okf_validator.py](file:///c:/GitDev/apexai-os-meta/apex-meta/scripts/okf_validator.py)
