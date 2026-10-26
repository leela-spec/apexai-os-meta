# Plane 4 Infrastructure Modules Audit Survey Report

> **Specification Miner Survey Report — Task 2**
> **Date:** 2026-10-22  
> **Working Directory:** `c:\GitDev\apexai-os-meta\.agents\teamwork\spec_miner_survey_4_2`  
> **Author:** Spec Miner (Survey Task 2: Plane 4 Infrastructure Modules Audit Survey)  
> **Target Scope:** 5 Canonical Plane 4 Modules in `apex-meta/informatics/` + Cross-Traceability to `13-candidate-3A-xml.md` & `16-candidate-3A-ultra.md`

---

## 1. Executive Summary

This survey report delivers a comprehensive, evidence-grounded audit of the five canonical **Plane 4 Infrastructure Modules** within the Apex Informatics Architecture:
1. `writing-profile.md` (`WP-01`..`WP-25`, 25 rules)
2. `file-architecture.md` (`FA-01`..`FA-13`, 13 rules)
3. `execution-modes.md` (`EM-01`..`EM-12`, 12 rules)
4. `anti-drift-rules.md` (`AD-01`..`AD-28`, 28 rules; note expansion from initial `AD-01..AD-26` specification)
5. `governance-schemas.md` (`GS-01`..`GS-22`, 19 defined rules, with `GS-16`, `GS-18`, and `GS-19` cleanly retired)

Across the five modules, **97 governed rules** were probed and verified. The audit evaluated Single-Ownership Discipline (`WP-23`), identified cross-module redundancy clusters and stale terms, mapped bidirectional cross-traceability against the 22 semantic tags in `<apex_contract v="1.0">` (`13-candidate-3A-xml.md`) and the upcoming `16-candidate-3A-ultra.md`, and formulated concrete authoring recommendations for the five downstream audit-module files (`audit-module-01` through `audit-module-05`).

All findings are backed by direct tool inspection, execution of the deterministic test suites (`test_canonical_ownership.py`, `test_informatics_e2e.py`, `test_tier5_adversarial.py` — 196 passed), and validation via `okf_validator.py`.

---

## 2. Features Discovered & Rule Inventory

The five canonical Plane 4 modules define 97 rules categorized by architectural domain.

### 2.1 Writing Profile & Prose Ergonomics (`writing-profile.md`)
- **File ID:** `apex-informatics-writing-profile` | **Type:** `Profile` | **Status:** `current`
- **Canonical Domain:** Technical prose ergonomics, Information Mapping, Simplified Technical English (STE), visual block sizing, durable identifiers, and significance ranking.

| # | Category | Rule ID | Tier & Metrics | Title | Description & Scope | Inputs / Preconditions | Outputs / Behaviors | Error / Halt Behavior | Canonical Owner |
|---|---|---|:---:|---|---|---|---|---|:---:|
| 1 | Prose Core | `WP-01` | `[P0 \| I98/E98/R05]` | Substance Over Ceremony Invariant | Technical accuracy overrides mechanical metric compliance. | Drafting or reviewing any text. | Authorizes relaxing limits when accuracy demands. | Reject mechanical cuts that harm correctness. | **WP-01 (Owner)** |
| 2 | Syntax | `WP-02` | `[P0 \| I96/E95/R08]` | Single Command Invariant | One clear imperative command per procedural sentence. | Authoring procedural steps. | Splits compound instructions into single imperatives. | Flag compound sentences with multiple commands. | **WP-02 (Owner)** |
| 3 | Syntax | `WP-03` | `[P0 \| I95/E96/R05]` | Imperative Verbs & Zero Modal Hedging | Active imperative verbs; no empty modal hedges (`should`, `may`). | Authoring directives. | Uses RFC 2119 imperatives; plain warranted uncertainty. | Flag weak modal suggestions. | **WP-03 (Owner)** |
| 4 | Grounding | `WP-04` | `[P0 \| I95/E98/R05]` | Grounded Evidence vs Unanchored Citation | Ground factual assertions in primary inspection (`path:line`). | Making factual claims. | Cites primary file/tool output directly. | Reject unanchored memory citations. | `AD-19` |
| 5 | Register | `WP-05` | `[P0 \| I94/E95/R07]` | Clear Active-Voice Language | Active voice with explicit actors; Cool Blue analytical register. | Any communication/text. | High density, objective, no flattery or unearned agreement. | Flag passive voice and conversational filler. | **WP-05 (Owner)** |
| 6 | Layout | `WP-06` | `[P0 \| I94/E97/R06]` | Top-Loaded Positional Primacy | Front-load critical invariants in first ~500 tokens. | Ordering document sections. | P0 rules placed near the top before attention decays. | Flag inverted priority ordering. | **WP-06 (Owner)** |
| 7 | Ranking | `WP-07` | `[P0 \| I93/E95/R07]` | Raw 3-Metric Significance Ranking | Tag governed rules with `[P<tier> \| I<val>/E<val>/R<val>]` (1–100). | Defining rules or options. | Keeps Impact, Evidence, Risk distinct and unaggregated. | Reject synthetic calculated formulas. | **WP-07 (Owner)** |
| 8 | Hygiene | `WP-08` | `[P0 \| I92/E95/R06]` | Stale Residual Eradication | Purge residual traces of deleted components/aliases. | Documenting active systems. | Removes dead component names from active rules. | Flag mentions of retired architectures. | `AD-15` |
| 9 | Boundary | `WP-09` | `[P0 \| I92/E95/R08]` | Adaptive Scope Boundary | Apply profile only to governed repository knowledge artifacts. | Writing code, logs, or chat. | Exempts chat, source code, and logs from formal rules. | Flag imposing OKF rules on casual chat. | **WP-09 (Owner)** |
| 10 | Structure | `WP-10` | `[P1 \| I92/E95/R08]` | Information Mapping ("One Chunk, One Job") | Partition documents into modular labeled visual blocks. | Formatting complex topics. | One cognitive task per visual block. | Flag intermingling theory, steps, and reference. | **WP-10 (Owner)** |
| 11 | Structure | `WP-11` | `[P1 \| I91/E94/R08]` | Table vs List vs Prose Selection | Tables for comparisons/schemas, bullets for criteria, numbers for sequence. | Organizing data. | Selects optimal Markdown visual vehicle. | Flag using numbered lists for unordered items. | **WP-11 (Owner)** |
| 12 | Primacy | `WP-12` | `[P1 \| I90/E94/R08]` | Minto Bottom Line Up Front (BLUF) | Lead sections and blocks with the conclusion in sentence one. | Structuring paragraphs. | Conclusion first; background and evidence follow. | Flag bury-the-lede narrative introductions. | **WP-12 (Owner)** |
| 13 | Sizing | `WP-13` | `[P1 \| I89/E92/R10]` | Visual Block Prose Orientation (~150 Words) | Break prose into tables/lists when approaching ~150 words. | Writing narrative paragraphs. | Converts dense paragraphs into structured blocks. | Advisory warning if prose is bloated. | **WP-13 (Owner)** |
| 14 | Sizing | `WP-14` | `[P1 \| I88/E92/R10]` | Concise Sentence Orientation (~20–25 Words) | Target ~20 words in procedural and ~25 in descriptive sentences. | Authoring sentences. | Keeps sentences scannable; expands when precision demands. | Advisory gate fires at >30 words. | **WP-14 (Owner)** |
| 15 | Identifiers | `WP-15` | `[P1 \| I91/E93/R08]` | Tier-Agnostic Durable IDs | Immutable canonical identifiers (`WP-01`, `FA-01`). | Assigning rule IDs. | Keeps ID string constant even when priority tier evolves. | Flag embedding priority in ID (`WP-P2-01`). | **WP-15 (Owner)** |
| 16 | Grounding | `WP-16` | `[P1 \| I89/E92/R08]` | Command-Carrying Claims | Accompany absence/zero/count claims with reproduction command. | Reporting zero/absence findings. | Includes exact command and scope with the claim. | Flag unverified negative claims. | `AD-20` |
| 17 | Reuse | `WP-23` | `[P1 \| I90/E92/R08]` | Single-Owner Instruction Reuse | Reuse canonical instruction; never duplicate schemas/tables. | Referring to existing rule. | Links owner; keeps only one-line operative imperative. | Reject copying full schemas into second file. | **WP-23 (Owner)** |
| 18 | Examples | `WP-17` | `[P2 \| I86/E90/R08]` | High-Signal Compact Examples | 1-line `<correct>` vs `<wrong>` micro-examples. | Clarifying ambiguous rules. | Delivers paired micro-examples; avoids narrative stories. | Flag verbose narrative examples. | **WP-17 (Owner)** |
| 19 | Sizing | `WP-18` | `[P2 \| I85/E90/R10]` | Universal Instruction Parsimony | Target ~30–50 active directives max per standalone file. | Authoring specification files. | Offloads specialized logic to JIT sub-modules. | Flag monolithic rule-walls. | **WP-18 (Owner)** |
| 20 | Syntax | `WP-19` | `[P2 \| I84/E92/R08]` | Syntax Exemptions | Code blocks, tables, URLs, paths, and logs exempt from limits. | Sizing validation. | Excludes structured blocks from prose word counts. | Prevents false-positive length violations. | **WP-19 (Owner)** |
| 21 | Efficiency | `WP-20` | `[P2 \| I82/E88/R08]` | No Default-Behavior Rules | Codify only non-obvious rules preventing recurring errors. | Adding instructions. | Omits directives models already follow by default. | Flag spending tokens on RLHF truisms. | **WP-20 (Owner)** |
| 22 | Layout | `WP-21` | `[P2 \| I80/E86/R10]` | Heading Depth Orientation (~3 Levels) | Prefer up to ~3 heading levels (`#`, `##`, `###`). | Structuring document outline. | Uses bold run-in labels or tables for deep hierarchy. | Flag gratuitous 4+ heading nesting. | **WP-21 (Owner)** |
| 23 | Links | `WP-24` | `[P2 \| I82/E90/R06]` | Clickable File References | Render every repository file listed as a clickable Markdown link. | Listing file paths. | Wraps paths in `[Name](path)` for instant navigation. | Flag raw unclickable file paths. | **WP-24 (Owner)** |
| 24 | Primacy | `WP-25` | `[P2 \| I80/E86/R06]` | Terminal-Position Operative Content | Close files with operative content (failure modes / guards). | Structuring file conclusion. | Puts references before closing block; ends on guard. | Flag wasting terminal position on link lists. | **WP-25 (Owner)** |
| 25 | Appendix | `WP-22` | `[P3 \| I72/E80/R10]` | Non-Normative Appendix & Typographic Cleanliness | Historical rationale in dedicated appendices; backtick quotes. | Formatting appendices. | Isolates history; formats commands and code cleanly. | Flag inline historical digressions. | **WP-22 (Owner)** |

---

### 2.2 File Architecture & Bundle Specification (`file-architecture.md`)
- **File ID:** `SPEC-FILE-ARCH-v0.2` | **Type:** `Specification` | **Status:** `current` | **Version:** `2.0.0`
- **Canonical Domain:** Five-Plane Information Architecture, OKF v0.2 bundle layouts, flat YAML serialization, current-truth separation, and attention primacy.

| # | Category | Rule ID | Tier & Metrics | Title | Description & Scope | Inputs / Preconditions | Outputs / Behaviors | Error / Halt Behavior | Canonical Owner |
|---|---|---|:---:|---|---|---|---|---|:---:|
| 26 | History | `FA-01` | `[P0 \| I95/E95/R08]` | Strict Current-Truth Separation | Live files state active current truth only; history in `log.md`. | Editing live specifications. | Zero inline changelogs; history isolated in `log.md`. | Reject inline version histories. | **FA-01 (Owner)** |
| 27 | Primacy | `FA-02` | `[P0 \| I95/E92/R08]` | Top-Loaded Attention Primacy | Front-load P0 invariants in first ~500 tokens; order P0→P3. | Structuring file sections. | Critical boundaries read before attention decays. | Flag inverted rule tiers. | `WP-06`, `WP-07` |
| 28 | Architecture | `FA-03` | `[P0 \| I92/E90/R12]` | Five-Plane Information Separation | Maintain strict separation across the five architecture planes. | Organizing repository files. | Separates Control, Scoped, Skills, Bundles, Evidence. | Reject mixed-plane monoliths. | **FA-03 (Owner)** |
| 29 | Authority | `FA-04` | `[P0 \| I98/E98/R05]` | Substance Over Ceremony Exception Authority | Target realization overrides mechanical metric compliance. | Evaluating metric ceilings. | Authorizes exceeding limits when required for safety/truth. | Reject mechanical cuts that compromise truth. | `WP-01` |
| 30 | Frontmatter | `FA-13` | `[P1 \| I90/E95/R10]` | Flat/Inline YAML Frontmatter Serialization | Flat key-value pairs or inline bracket lists; colon on every line. | Writing frontmatter. | Ensures custom zero-dependency parsers succeed. | Reject multiline hyphenated lists (`- item`). | **FA-13 (Owner)** |
| 31 | Frontmatter | `FA-05` | `[P1 \| I88/E92/R12]` | Root Index Specification (`index.md`) | Root `index.md` frontmatter (`okf_version: "0.2"`, title, desc, tags). | Bundle root index creation. | Establishes bundle identity and navigation links. | Reject bundle root without `okf_version: "0.2"`. | **FA-05 (Owner)** |
| 32 | Frontmatter | `FA-06` | `[P1 \| I88/E92/R12]` | Concept Document Specification (`*.md`) | Mandatory frontmatter: `type`, unique `id`, `title`, `description`, `status`. | Concept document authoring. | Defines concept document metadata contract. | Validator rejects missing `type` or duplicate `id`. | **FA-06 (Owner)** |
| 33 | Identifiers | `FA-07` | `[P1 \| I85/E88/R15]` | Unique Durable Identifiers | Immutable durable ID assigned to every governed concept file. | Creating concept files. | Provides stable cross-referencing targets. | Validator rejects duplicate IDs across bundle. | `WP-15` |
| 34 | Boundaries | `FA-08` | `[P1 \| I85/E90/R15]` | Sub-Bundle Isolation Boundary | Subdirectory with its own `index.md` forms an isolated sub-bundle. | Directory topology. | Validator stops recursion at sub-bundle boundaries. | Prevents draft leakage into root bundle. | **FA-08 (Owner)** |
| 35 | Hygiene | `FA-09` | `[P1 \| I82/E85/R18]` | Residual Name Eradication | Purge all residual mentions of obsolete names from live docs. | Renaming or deleting tools. | Eradicates dead names to prevent model hallucinations. | Flag references to retired systems. | `AD-15` |
| 36 | Structure | `FA-10` | `[P2 \| I78/E82/R20]` | Single-Purpose Topic Files | Structure every concept document around a single responsibility. | Designing new modules. | Partitions content into focused topic files. | Flag multi-topic monolithic documents. | **FA-10 (Owner)** |
| 37 | History | `FA-11` | `[P2 \| I75/E80/R18]` | Dedicated Changelog Allocation | Record version history and milestones exclusively in `log.md`. | Updating bundle history. | Exempts `log.md` from mandatory concept frontmatter. | Flag placing changelogs in concept docs. | **FA-11 (Owner)** |
| 38 | Sizing | `FA-12` | `[P2 \| I82/E88/R10]` | Plane Sizing & Instruction Parsimony | Keep surfaces within plane token ceilings; two-layer carrier structure. | Packaging instructions. | Layer 1 universal contract + Layer 2 repo-specific. | Flag overloaded rule-walls. | `WP-18` |

---

### 2.3 Execution Modes & Task Adapters Specification (`execution-modes.md`)
- **File ID:** `ADPT-EXEC-MODES-v0.2` | **Type:** `Adapter` | **Status:** `current`
- **Canonical Domain:** Pluggable operational task adapters for Q&A Decision Matrices, Comparison Bake-Offs, Exact-Match Patching, Handover Protocols, and MMM Iterative Execution.

| # | Category | Rule ID | Tier & Metrics | Title | Description & Scope | Inputs / Preconditions | Outputs / Behaviors | Error / Halt Behavior | Canonical Owner |
|---|---|---|:---:|---|---|---|---|---|:---:|
| 39 | Mutation | `EM-01` | `[P0 \| I98/E96/R05]` | Whole-File Rewrite Prohibition | Never overwrite existing files via full-file rewrites. | Modifying existing files. | Enforces surgical exact-match patches or AST intents. | Halt on full-file overwrites. | **EM-01 (Owner)** |
| 40 | Handover | `EM-02` | `[P0 \| I96/E95/R05]` | Handover Non-Paralysis Invariant | Never write a handover to defer what tools can resolve now. | Checkable ambiguity arises. | Resolves facts immediately using tools/subagents. | Reject handovers that escape immediate work. | **EM-02 (Owner)** |
| 41 | Context | `EM-03` | `[P0 \| I96/E95/R06]` | Step-by-Step Context & File Iteration Invariant | Never bulk-read directories upfront; load context per active step. | Starting a complex task. | Reads only active step context; writes step files. | Flag upfront bulk directory reading. | **EM-03 (Owner)** |
| 42 | Target | `EM-04` | `[P0 \| I95/E95/R08]` | Target Dominance | Optimize for user outcome; no process ceremony substitution. | Executing tasks. | Focuses on product delivery over procedural overhead. | Halt when ceremony replaces deliverable. | `AD-01` |
| 43 | Recovery | `EM-05` | `[P0 \| I94/E92/R10]` | Two-Strike Pivot Rule | Stop repairing a failing subsystem after 2 failed fix attempts. | Subsystem repair fails. | Halts and pivots to alternative architecture. | Forbid entering a 3rd repair attempt. | `AD-02`, `AD-24` |
| 44 | Decision | `EM-06` | `[P1 \| I92/E94/R10]` | Conditional Q&A Trigger | Structure high-stakes trade-offs using Q&A Decision Matrix. | High-stakes architectural choice. | Emits Question, Options, Grounding, I/E/R, Recommendation, Notes. | Reject ungrounded choices or synthetic scores. | **EM-06 (Owner)** |
| 45 | Comparison | `EM-07` | `[P1 \| I88/E90/R12]` | Conditional Bake-Off Trigger | 4-Phase Comparison Bake-Off for competing technologies. | Comparing libraries/tools. | 4 phases: Hard Gating, Matrix with Failure Mode, Verdicts, Prototypes. | Reject skipping gating or failure mode column. | **EM-07 (Owner)** |
| 46 | Patching | `EM-08` | `[P1 \| I98/E96/R05]` | Conditional Patch Trigger | Exact-match block replacement (Mode A) or AST patch (Mode B). | Modifying repository files. | Verbatim `<old>` context; `git mv`/`cp` for moves; no line numbers. | Reject guessed lines or non-unique matches. | **EM-08 (Owner)** |
| 47 | Handover | `EM-09` | `[P1 \| I92/E95/R08]` | Conditional Handover Trigger | 4-Dimensional Contract + 5-Component Report. | Session end or delegation. | Input/Process/Output/DoD + Obs/Logic/Caveats/Conclusion/Verify. | Reject vague unstructured handovers. | **EM-09 (Owner)** |
| 48 | Iteration | `EM-10` | `[P1 \| I95/E95/R08]` | Conditional Iterative & MMM Trigger | Route ladder (0 direct, 1 preflight, 2 MMM file loop). | Multi-module or research task. | Each iteration creates files (00-matrix, 01-map, step-XX). | Flag unmaterialized mental state loops. | **EM-10 (Owner)** |
| 49 | Validation | `EM-11` | `[P2 \| I82/E86/R12]` | Upward Invalidation Rule | Invalidate only specific layer disproven by concrete evidence. | Low-level test failure. | Fixes Micro realization without abandoning Macro intent. | Flag rewriting system goals on micro bugs. | **EM-11 (Owner)** |
| 50 | Sync | `EM-12` | `[P2 \| I80/E90/R08]` | Conditional Sync & Scoped Push Trigger | Scoped push (`git push <paths>`) vs full `sync`/`synch`. | Git synchronization. | Preserves unrelated dirty files; rebase on non-fast-forward. | Reject dropping unrequested dirty work. | **EM-12 (Owner)** |

---

### 2.4 Anti-Drift Laws & Operational Lore (`anti-drift-rules.md`)
- **File ID:** `GOV-ANTI-DRIFT-v0.2` | **Type:** `Governance` | **Status:** `current` | **Version:** `2.0.0`
- **Canonical Domain:** The 8 Anti-Drift Laws, Two-Strike Rule, Sunk-Cost Prohibition, Operator Challenge Boundary, Task Minimalism, Anti-Overcorrection, and Context Hygiene.

| # | Category | Rule ID | Tier & Metrics | Title | Description & Scope | Inputs / Preconditions | Outputs / Behaviors | Error / Halt Behavior | Canonical Owner |
|---|---|---|:---:|---|---|---|---|---|:---:|
| 51 | Target | `AD-01` | `[P0 \| I100/E95/R05]` | TARGET Dominance Invariant | TARGET dominates everything; verify requirements; no-op permission. | Executing any task. | Prioritizes product path; reports no-op if already met. | Halt if meta-ceremony displaces target. | **AD-01 (Owner)** |
| 52 | Recovery | `AD-02` | `[P0 \| I98/E95/R05]` | Two-Strike Subsystem Rule | If 2 iterations fail on a subsystem, stop and change approach. | Subsystem failure. | Caps attempts at 2; forces architecture pivot. | Reject entering 3rd fix attempt. | **AD-02 (Owner)** |
| 53 | Mutation | `AD-03` | `[P0 \| I98/E96/R05]` | Whole-File Rewrite Prohibition | Modify files via surgical patch blocks or verified tool edits. | File modifications. | Prevents full-file wipes; surgical replacements. | Halt on whole-file regeneration. | `EM-01`, `EM-08` |
| 54 | Context | `AD-04` | `[P0 \| I96/E95/R05]` | Step-by-Step Context & File Iteration Invariant | Never front-load massive files; Source Priority Ledger. | Multi-file research/task. | Reads per active step; externalizes findings to disk. | Halt on upfront context bloat. | `EM-03`, `EM-10` |
| 55 | Detour | `AD-05` | `[P0 \| I96/E95/R05]` | Operator Challenge Boundary | Must this be fixed before testing product? If not, defer. | Proposing refactor/detour. | Halts speculative architecture; defers in one line. | Reject speculative unblocking work. | **AD-05 (Owner)** |
| 56 | Ambiguity | `AD-06` | `[P0 \| I96/E95/R05]` | Checkable Ambiguity Resolution | Verify checkable facts immediately; never defer checkable items. | Ambiguity encountered. | Invocates tools immediately; eliminates handoff escapism. | Reject handoffs deferring checkable facts. | `EM-02` |
| 57 | Sunk Cost | `AD-07` | `[P0 \| I95/E95/R05]` | Sunk-Cost Prohibition Invariant | Prior investment gives failing approach zero authority. | Deciding whether to continue. | Abandons dead-end branches without regret. | Reject continuing failing branch on sunk cost. | **AD-07 (Owner)** |
| 58 | Authority | `AD-08` | `[P0 \| I95/E95/R05]` | Substance Over Ceremony Exception Authority | Substantive realization of target overrides mechanical ceilings. | Evaluating constraints. | Authorizes exceeding ceilings for correctness. | Reject mechanical cuts that damage truth. | `WP-01` |
| 59 | Drift | `AD-09` | `[P0 \| I95/E95/R08]` | Stop on Drift Invariant | Halt if work becomes ceremony, wrappers, or meta-docs. | Monitoring ongoing work. | Stops drifting work; redirects to core deliverable. | Halt on self-indulgent ceremony drift. | **AD-09 (Owner)** |
| 60 | Product | `AD-10` | `[P0 \| I95/E94/R08]` | Product Before Infrastructure Invariant | Fix only execution/data-loss blockers before first working slice. | Pre-product development. | Blocks pre-mature test/infra building. | Reject scaffolding before working slice runs. | **AD-10 (Owner)** |
| 61 | Reuse | `AD-11` | `[P0 \| I95/E92/R08]` | Reuse Before Build Invariant | Try existing alternative before building new abstraction. | Facing new problem. | Inspects existing repo tools, skills, libraries. | Reject building new without trying existing. | **AD-11 (Owner)** |
| 62 | Product | `AD-12` | `[P0 \| I94/E92/R08]` | Product Advancement Invariant | Every work unit must run something, teach quality, or advance target. | Task execution. | Defer any work that does not advance product. | Reject busy-work that doesn't advance product. | **AD-12 (Owner)** |
| 63 | Machinery | `AD-13` | `[P0 \| I92/E90/R10]` | Evidence Proportionality Invariant | Do not build more verification machinery than risk justifies. | Designing tests/gates. | Scales verification effort to failure downside. | Reject heavy test harnesses for trivial risks. | **AD-13 (Owner)** |
| 64 | Minimalism | `AD-14` | `[P1 \| I94/E95/R08]` | Gall's Law & Single Flat Artifact | Default to single flat file before nested packages/modules. | System design. | Keeps initial implementation simple and flat. | Flag premature multi-package architectures. | **AD-14 (Owner)** |
| 65 | Hygiene | `AD-15` | `[P1 \| I93/E95/R05]` | Residual Name Eradication | Purge all residual mentions of deleted names from live docs. | Deleting/renaming code. | Eradicates dead names; prevents ghost reasoning. | Flag zombie references in active rules. | **AD-15 (Owner)** |
| 66 | Recovery | `AD-16` | `[P1 \| I93/E95/R07]` | Pre-Existing Red vs Regression Boundary | Halt only if test was green on HEAD and broken by current edits. | Running test suites. | Records pre-existing failures with command; continues. | Halt only on new regressions. | **AD-16 (Owner)** |
| 67 | Primacy | `AD-17` | `[P1 \| I93/E94/R07]` | Minto BLUF Directive | Deliver definitive bottom line up front in sentence one. | Reporting findings. | Eliminates wind-up greetings and preambles. | Flag bury-the-lede narrative openings. | `WP-12` |
| 68 | Scope | `AD-18` | `[P1 \| I92/E93/R08]` | Zero-Speculation Scope Boundary | Out of scope by default unless requested or strictly required. | Defining task scope. | No precautionary guardrails for hypothetical risks. | Reject speculative features or roadmaps. | **AD-18 (Owner)** |
| 69 | Grounding | `AD-19` | `[P1 \| I91/E96/R05]` | Primary Grounding vs Secondary Citation | Ground facts in originating artifact (`path:line`) or tool. | Verifying claims. | Opens primary source; never relies on memory. | Reject ungrounded citations. | **AD-19 (Owner)** |
| 70 | Grounding | `AD-20` | `[P1 \| I90/E94/R06]` | Command-Carrying Claims | Statements of zero/absence must carry reproducible command. | Negative/absence claims. | Attaches command and exact scope to claim. | Reject unverified "none found" claims. | **AD-20 (Owner)** |
| 71 | Path | `AD-21` | `[P1 \| I90/E92/R08]` | Balanced Viable Path | Direct step first before elaborate multi-layer architecture. | Choosing solution path. | Executes simple value-efficient path first. | Reject over-engineered detour solutions. | **AD-21 (Owner)** |
| 72 | Feedback | `AD-22` | `[P2 \| I88/E91/R08]` | Surgical Edits & Anti-Overcorrection (Hold Position) | Update only on evidence, never pushback alone; narrow edits. | Operator feedback. | Resists sycophancy; confines changes to what was challenged. | Reject whole-module rewrites on pushback. | **AD-22 (Owner)** |
| 73 | Asset | `AD-23` | `[P2 \| I87/E92/R08]` | Asset Preservation & Deterministic Moves | Treat code/scripts as assets; move via `git mv`/`cp`. | Managing files. | Preserves existing assets; never regenerates. | Reject destroying working code during moves. | **AD-23 (Owner)** |
| 74 | Recovery | `AD-24` | `[P2 \| I86/E90/R08]` | Two-Strike Subsystem Tracker Mechanics | Track failure counts per distinct subsystem independently. | Multiple subsystems failing. | Success resets count to 0; 2 strikes triggers pivot. | Prevent mixing failure counts across modules. | **AD-24 (Owner)** |
| 75 | Machinery | `AD-25` | `[P2 \| I85/E90/R09]` | Pre-Addition Gate & Machinery Rule | Name requirement/blocker before adding abstraction/gate. | Adding new machinery. | Confirms problem isn't surfaced in ~2 steps of use. | Reject adding machinery without named blocker. | **AD-25 (Owner)** |
| 76 | Sizing | `AD-26` | `[P2 \| I85/E90/R10]` | Universal Instruction Parsimony | Standalone file concise (~30–50 rules max); JIT links. | Managing rule sets. | Routes specialized domains JIT to prevent dilution. | Flag rule-wall bloat. | `WP-18` |
| 77 | Linkage | `AD-27` | `[P2 \| I84/E89/R08]` | Sibling Module Linkage | Coordinate with WP, FA, EM, GS via repository-relative links. | Cross-module referencing. | Relative links ensure resolution across all runners. | Flag broken or absolute links. | **AD-27 (Owner)** |
| 78 | Metrics | `AD-28` | `[P3 \| I68/E82/R10]` | Objective Run Outcome Classification | Classify session close: `product-shipped`, `governance-only`, etc. | Post-mortem session audit. | Checks git log and deliverable state objectively. | Flag unclassified session outcomes. | **AD-28 (Owner)** |

---

### 2.5 Governance Schemas & Directive Ceilings (`governance-schemas.md`)
- **File ID:** `GOV-SCHEMAS-v0.2` | **Type:** `Governance` | **Status:** `current` | **Version:** `2.0.0`
- **Canonical Domain:** OKF v0.2 frontmatter schemas, AST patch intent schemas, decision matrix formats, model directive ceilings, and significance ranking.

| # | Category | Rule ID | Tier & Metrics | Title | Description & Scope | Inputs / Preconditions | Outputs / Behaviors | Error / Halt Behavior | Canonical Owner |
|---|---|---|:---:|---|---|---|---|---|:---:|
| 79 | Conformance | `GS-01` | `[P0 \| I98/E98/R05]` | Mandatory Schema Conformance | Governed artifacts must conform to declared schema. | Emitting structured data. | Rejects unregistered fields, missing keys, ungrounded claims. | Reject non-conforming artifacts. | **GS-01 (Owner)** |
| 80 | Mutation | `GS-02` | `[P0 \| I98/E96/R05]` | Prohibited Whole-File Patch Rewrites | Never generate full-file rewrites for existing files. | Patching files. | Enforces AST patch intents or exact-match search/replace. | Halt on whole-file patch intent. | `EM-01` |
| 81 | Primacy | `GS-03` | `[P0 \| I96/E95/R05]` | Top-Loaded Attention Primacy | Front-load P0 invariants in first ~500 tokens. | Structuring schemas/specs. | Position critical rules near top before attention decays. | Flag inverted rule ordering. | `WP-06` |
| 82 | Ranking | `GS-04` | `[P0 \| I95/E95/R06]` | Raw 3-Metric Significance Tagging | Tag rules with raw unaggregated `[P<tier> \| I/E/R]` (1–100). | Tagging rules/options. | Keeps dimensions distinct; no composite math scores. | Reject synthetic math score calculations. | `WP-07` |
| 83 | Frontmatter | `GS-05` | `[P0 \| I94/E96/R06]` | Flat YAML Frontmatter Serialization | Flat key-value pairs or inline bracketed lists; colon on every line. | Validating frontmatter. | Ensures compatibility with zero-dependency parsers. | Reject multiline hyphenated lists. | `FA-13` |
| 84 | Validation | `GS-06` | `[P1 \| I92/E95/R08]` | Root Index Schema (`index.md`) | Validation view of root index schema (`okf_version: "0.2"`). | Validating root index. | Rejects bundle root failing `FA-05` frontmatter contract. | Fail validation on invalid root index. | `FA-05` |
| 85 | Validation | `GS-07` | `[P1 \| I92/E95/R08]` | Concept Document Schema (`*.md`) | Validation view of concept schema (non-empty `type`, unique `id`). | Validating concept files. | Field-level contract owned by `FA-06`; concept types table. | Fail validation on missing type or id. | `FA-06` |
| 86 | Identifiers | `GS-08` | `[P1 \| I90/E94/R07]` | Bundle-Wide Durable ID Uniqueness | Enforce unique durable identifiers across all docs in bundle. | Validating bundle IDs. | Rejects duplicate IDs that cause collision. | Fail validation on ID duplication. | `WP-15` |
| 87 | Patch Intent | `GS-09` | `[P1 \| I96/E96/R05]` | Deterministic AST Patch Intent Specification | Structure automated mutations using `patch_intent.v1` schema. | Emitting patch intents. | Target edits by heading path and hints, not line numbers. | Reject line-offset patching. | **GS-09 (Owner)** |
| 88 | Patch Safety | `GS-10` | `[P1 \| I95/E95/R05]` | AST Safety Threshold Invariants | Mandatory safety invariants: unique match, fail on ambiguity, max 1 file. | Validating patch intent. | Enforces `require_unique_match: true`, `max_files_touched: 1`. | Reject intent with unsafe thresholds. | **GS-10 (Owner)** |
| 89 | Patch Safety | `GS-11` | `[P1 \| I93/E94/R06]` | Prohibited Brittle Identifiers | Forbid `line_number`, `line_start`, `line_range`, `hunk` in intents. | Authoring patch intent. | Forbids volatile line numbers that break on concurrent edits. | Reject patch intents with line numbers. | **GS-11 (Owner)** |
| 90 | Decision | `GS-12` | `[P1 \| I90/E92/R10]` | Structured Decision Matrix Protocol | Validation contract for Q&A Decision Matrix format. | Validating decision records. | Format owned by `execution-modes.md` §2.1. | Reject records missing question/options/notes. | `EM-06` |
| 91 | Comparison | `GS-13` | `[P1 \| I88/E90/R12]` | 4-Phase Comparison Bake-Off Rubric | Validation contract for 4-phase comparison bake-off. | Validating bake-offs. | Rubric owned by `execution-modes.md` §3.1. | Reject bake-offs skipping gating or failure mode. | `EM-07` |
| 92 | Sizing | `GS-14` | `[P2 \| I88/E92/R08]` | Universal Instruction Parsimony | Standalone file must not exceed directive ceiling (~30–50). | Validating instruction files. | Rejects overloaded rule-walls without JIT decomposition. | Flag files exceeding directive ceiling. | `WP-18` |
| 93 | Sizing | `GS-15` | `[P2 \| I86/E90/R08]` | Directive Accounting Separation | Count imperative directives separately from declarative content. | Measuring directive count. | Establishes the exact accounting method for `WP-18`. | Prevents miscounting tables/schemas as rules. | **GS-15 (Owner)** |
| — | *Retired* | `GS-16` | *Retired* | *Retired (Duplicate of `WP-20`)* | Retired during canonical compression pass; gap preserved. | — | — | — | *Retired* |
| 94 | Ranking | `GS-17` | `[P2 \| I90/E94/R08]` | Ranking Conformance | Reject rules lacking `[P<tier> \| I/E/R]` or out of descending order. | Validating rule blocks. | Tier semantics owned by `WP-07` in `writing-profile.md`. | Fail validation on invalid tier/metric tags. | `WP-07` |
| — | *Retired* | `GS-18` | *Retired* | *Retired (Duplicate of `GS-04`)* | Retired during canonical compression pass; gap preserved. | — | — | — | *Retired* |
| — | *Retired* | `GS-19` | *Retired* | *Retired (Folded into `GS-17`)* | Retired during canonical compression pass; gap preserved. | — | — | — | *Retired* |
| 95 | Diagnostics | `GS-20` | `[P3 \| I80/E88/R10]` | Tri-Class Diagnostic Classification | Classify findings into `OKF_ERROR`, `APEX_PROFILE_ERROR`, `ADVISORY_WARNING`. | Tooling validation runs. | Categorizes severity of linter/validator findings. | Standardizes diagnostic taxonomy. | **GS-20 (Owner)** |
| 96 | Gates | `GS-21` | `[P3 \| I82/E89/R08]` | Deterministic Conformance Gate | Enforce zero `OKF_ERROR` and zero `APEX_PROFILE_ERROR` to pass gate. | CI/pre-commit ratification. | Advisory warnings do not block ratification. | Block ratification on error count > 0. | **GS-21 (Owner)** |
| 97 | Boundaries | `GS-22` | `[P3 \| I75/E82/R10]` | Sub-Bundle Boundary Pruning | Isolate untracked subdirectories using boundary `index.md`. | Validating directory trees. | Stops validator recursion at sub-bundle boundaries. | Prevents staging noise in bundle audit. | `FA-08` |

---

## 3. Single-Ownership Discipline Audit (`WP-23`)

### 3.1 The Principle & Operational Intent of `WP-23`
`WP-23` (*Single-Owner Instruction Reuse*) states:
> *"Reuse an existing instruction instead of restating it. When a concept already has a canonical owner in this suite, reference that owner; never copy its schema, table, JSON block, or worked example into a second file. Restate only the one-line operative imperative a module needs to remain self-sufficient when loaded alone. Copies drift, and drifted copies become contradictions that degrade instruction-following far more than their token cost."*

The operational tension resolved by `WP-23` is:
- **JIT Self-Sufficiency:** When an agent loads a specialized module just-in-time (e.g. `file-architecture.md`), it must understand foundational invariants (e.g. *Substance Over Ceremony*, *Current-Truth Separation*, *Primacy*) without being forced to load the entire repository.
- **Drift Prevention:** If two files independently define a schema or worked example, they will inevitably diverge during maintenance (as occurred in defect `D9`, where an inline schema copy in `governance-schemas.md` silently dropped `maxLength` bounds enforced by the authoritative JSON schema).

### 3.2 Canonical Cross-Reference Ledger (All 28 Delegations)
The following table documents all 28 delegations where a rule in one module explicitly delegates its definition to a canonical owner in another module.

| Calling Rule | Calling File | Target Rule | Canonical Owner File | Delegation Scope & Relationship | `WP-23` Compliant? |
|---|---|---|---|---|:---:|
| `WP-04` | `writing-profile.md` | `AD-19` | `anti-drift-rules.md` | Primary Grounding vs Secondary Citation | Yes (one-line operative rule) |
| `WP-08` | `writing-profile.md` | `AD-15` | `anti-drift-rules.md` | Stale Residual Eradication | Yes (one-line operative rule) |
| `WP-16` | `writing-profile.md` | `AD-20` | `anti-drift-rules.md` | Command-Carrying Claims | Yes (one-line operative rule) |
| `FA-02` | `file-architecture.md` | `WP-06`, `WP-07` | `writing-profile.md` | Top-Loaded Positional Primacy & Metric Definitions | Yes (cites canonical owner) |
| `FA-04` | `file-architecture.md` | `WP-01` | `writing-profile.md` | Substance Over Ceremony Exception Authority | Yes (one-line operative rule) |
| `FA-07` | `file-architecture.md` | `WP-15` | `writing-profile.md` | Unique Durable ID Grammar | Yes (cites grammar owner) |
| `FA-09` | `file-architecture.md` | `AD-15` | `anti-drift-rules.md` | Residual Name Eradication | Yes (one-line operative rule) |
| `FA-12` | `file-architecture.md` | `WP-18` | `writing-profile.md` | Instruction Parsimony Directive Ceiling | Yes (cites ceiling owner) |
| `EM-04` | `execution-modes.md` | `AD-01` | `anti-drift-rules.md` | Target Dominance Invariant | Yes (one-line operative rule) |
| `EM-05` | `execution-modes.md` | `AD-02`, `AD-24` | `anti-drift-rules.md` | Two-Strike Pivot Rule & Tracker Mechanics | Yes (one-line operative rule) |
| `EM-08` | `execution-modes.md` | `GS-09..11` | `governance-schemas.md` | Cites `patch-intent-schema.json` and GS §2.2 | Yes (worked example only) |
| `EM-09` | `execution-modes.md` | `EM-02` | `execution-modes.md` | Handover Non-Paralysis (intra-file delegation) | Yes (local cross-reference) |
| `AD-03` | `anti-drift-rules.md` | `EM-01`, `EM-08` | `execution-modes.md` | Whole-File Rewrite Prohibition Protocol | Yes (one-line operative rule) |
| `AD-04` | `anti-drift-rules.md` | `EM-03`, `EM-10` | `execution-modes.md` | Step-by-Step Context & File Iteration Loop | Yes (one-line operative rule) |
| `AD-06` | `anti-drift-rules.md` | `EM-02` | `execution-modes.md` | Checkable Ambiguity Resolution | Yes (one-line operative rule) |
| `AD-08` | `anti-drift-rules.md` | `WP-01` | `writing-profile.md` | Substance Over Ceremony Exception Authority | Yes (one-line operative rule) |
| `AD-17` | `anti-drift-rules.md` | `WP-12` | `writing-profile.md` | Minto BLUF Directive | Yes (one-line operative rule) |
| `AD-26` | `anti-drift-rules.md` | `WP-18` | `writing-profile.md` | Universal Instruction Parsimony | Yes (cites ceiling owner) |
| `GS-02` | `governance-schemas.md` | `EM-01` | `execution-modes.md` | Prohibited Whole-File Patch Rewrites | Yes (one-line operative rule) |
| `GS-03` | `governance-schemas.md` | `WP-06` | `writing-profile.md` | Top-Loaded Attention Primacy | Yes (one-line operative rule) |
| `GS-04` | `governance-schemas.md` | `WP-07` | `writing-profile.md` | Raw 3-Metric Significance Tagging | Yes (cites definition owner) |
| `GS-05` | `governance-schemas.md` | `FA-13` | `file-architecture.md` | Flat YAML Frontmatter Serialization | Yes (one-line operative rule) |
| `GS-06` | `governance-schemas.md` | `FA-05` | `file-architecture.md` | Root Index Schema Validation View | Yes (cites schema owner) |
| `GS-07` | `governance-schemas.md` | `FA-06` | `file-architecture.md` | Concept Document Schema Validation View | Yes (cites field owner) |
| `GS-08` | `governance-schemas.md` | `WP-15` | `writing-profile.md` | Bundle-Wide Durable ID Uniqueness | Yes (cites grammar owner) |
| `GS-12` | `governance-schemas.md` | `EM-06` | `execution-modes.md` | Decision Matrix Format Contract | Yes (cites format owner) |
| `GS-13` | `governance-schemas.md` | `EM-07` | `execution-modes.md` | 4-Phase Comparison Bake-Off Rubric Contract | Yes (cites rubric owner) |
| `GS-14` | `governance-schemas.md` | `WP-18` | `writing-profile.md` | Universal Instruction Parsimony Ceiling | Yes (cites ceiling owner) |
| `GS-17` | `governance-schemas.md` | `WP-07` | `writing-profile.md` | Ranking Conformance Validation View | Yes (cites tier owner) |
| `GS-22` | `governance-schemas.md` | `FA-08` | `file-architecture.md` | Sub-Bundle Boundary Pruning | Yes (cites boundary owner) |

### 3.3 Verification of Mechanical Ownership Guards
The mechanical guarantees tested by `test_canonical_ownership.py` confirm:
1. **D1 Guard (Rule ID Uniqueness):** Zero duplicate IDs exist within any file, and zero duplicate IDs exist across the suite. Every rule prefix strictly matches its home file (`WP` $\rightarrow$ `writing-profile.md`, `FA` $\rightarrow$ `file-architecture.md`, `EM` $\rightarrow$ `execution-modes.md`, `AD` $\rightarrow$ `anti-drift-rules.md`, `GS` $\rightarrow$ `governance-schemas.md`).
2. **Canonical Pointer Integrity:** 100% of canonical pointers resolve to active rules defined in the suite. Zero pointers target their own file.
3. **Link Portability (RBL-05):** Zero machine-specific absolute `file:///` links exist in live documentation. All links use portable repository-relative Markdown paths.
4. **D9 Guard (No Re-Embedded Upstream Schemas):** `governance-schemas.md` cites `patch-intent-schema.json` without embedding the full JSON schema block, preventing schema drift while declaring all required safety invariants (`require_unique_match`, `fail_on_ambiguity`, `allow_full_file_rewrite`, `max_files_touched`).

---

## 4. Semantic Redundancies, Stale Terms & Structural Nuances

### 4.1 Cross-Module Redundancy Clusters
The audit identified 15 distinct functional concepts that appear in multiple modules. While `WP-23` permits restating a one-line operative imperative for standalone JIT self-sufficiency, these clusters represent the primary areas of potential token fat:

1. **Substance Over Ceremony Exception Authority:**
   - Canonical Owner: `WP-01` [P0]
   - Pointers / Operative Restatements: `FA-04` [P0], `AD-08` [P0], `index.md` §1, `general-informatics-router.md` §1.
   - *Observation:* Three separate P0 rules across three files embody the identical principle (*"Technical accuracy overrides mechanical metric compliance"*). In the layered KB, this traces back to Universal Research `A01-substance-over-ceremony.md`.
2. **Whole-File Rewrite Prohibition:**
   - Canonical Owner: `EM-01` [P0]
   - Pointers / Operative Restatements: `AD-03` [P0], `GS-02` [P0], and contract `<surgical>`.
   - *Observation:* `EM-01`, `AD-03`, and `GS-02` are all P0 invariants prohibiting whole-file rewrites.
3. **Target Dominance:**
   - Canonical Owner: `AD-01` [P0] (`I100/E95/R05`)
   - Pointer: `EM-04` [P0] (`I95/E95/R08`), plus router headers in `index.md` and `general-informatics-router.md`.
4. **Step-by-Step Context & File Iteration (Anti-Bloat):**
   - Canonical Owner: `EM-03` [P0] and `EM-10` [P1]
   - Pointer: `AD-04` [P0].
5. **Two-Strike Pivot Rule:**
   - Canonical Owner: `AD-02` [P0] and `AD-24` [P2]
   - Pointer: `EM-05` [P0].
6. **Handover Non-Paralysis / Checkable Ambiguity:**
   - Canonical Owner: `EM-02` [P0]
   - Pointers: `AD-06` [P0], `EM-09` [P1].
7. **Residual Name Eradication:**
   - Canonical Owner: `AD-15` [P1]
   - Pointers: `WP-08` [P0], `FA-09` [P1].
   - *Nuance:* Notice that `WP-08` is ranked **P0** in `writing-profile.md`, whereas its canonical owner `AD-15` is ranked **P1** in `anti-drift-rules.md`. This is intentional: in technical writing, referencing retired names creates immediate agent hallucination risk (P0 invariant), whereas in broad operational lore it is a core hygiene method (P1).
8. **Top-Loaded Positional Primacy:**
   - Canonical Owner: `WP-06` [P0]
   - Pointers: `FA-02` [P0], `GS-03` [P0].
9. **Raw 3-Metric Significance Tagging:**
   - Canonical Owner: `WP-07` [P0]
   - Pointers: `FA-02` [P0], `GS-04` [P0], `GS-17` [P2].
10. **Flat YAML Serialization:**
    - Canonical Owner: `FA-13` [P1]
    - Pointer: `GS-05` [P0].
    - *Nuance:* `GS-05` elevates flat serialization to **P0** because custom frontmatter parsers fail immediately on multiline hyphens during governance validation, whereas in file architecture it is a **P1** frontmatter syntax rule.
11. **Universal Instruction Parsimony:**
    - Canonical Owner: `WP-18` [P2] (~30–50 directives)
    - Pointers: `FA-12` [P2], `AD-26` [P2], `GS-14` [P2]; measured by `GS-15` [P2].
12. **Durable Identifier Grammar:**
    - Canonical Owner: `WP-15` [P1]
    - Pointers: `FA-07` [P1], `GS-08` [P1].
13. **Primary Grounding vs Secondary Citation:**
    - Canonical Owner: `AD-19` [P1]
    - Pointer: `WP-04` [P0].
14. **Command-Carrying Claims:**
    - Canonical Owner: `AD-20` [P1]
    - Pointer: `WP-16` [P1].
15. **Minto BLUF Directive:**
    - Canonical Owner: `WP-12` [P1]
    - Pointer: `AD-17` [P1].

### 4.2 Stale Terms, Legacy Mechanisms & Structural Irregularities

1. **Deprecated `deepen_when="..."` Attributes in Routers:**
   - In `general-informatics-router.md` (lines 19–37) and `index.md` (lines 21–39), the `<informatics>` routing gates still carry `deepen_when="..."` attributes (e.g., `deepen_when="prose_tables_or_ranking"`, `deepen_when="five_plane_isolation"`).
   - Research Packet `RESULTS-08-deepen-when-mechanics.md` formally proved that `deepen_when` has no automated runtime parser, introduces redundant subjective gating checks, and was entirely stripped from the `v1.0-3A` contract (`13-candidate-3A-xml.md`).
   - *Recommendation:* Document in audit reports that `general-informatics-router.md` and `index.md` carry legacy `deepen_when` attributes that should be deprecated in a future router sync.
2. **Rule Range Discrepancies in Upstream Task Descriptions:**
   - The original user prompt and dispatch task referenced `AD-01..AD-26` and `GS-01..GS-17`.
   - The live canonical files define **`AD-01..AD-28`** (28 rules, including `AD-27` *Sibling Module Linkage* and `AD-28` *Objective Run Outcome Classification*) and **`GS-01..GS-22`** (19 active rules, including `GS-20` *Tri-Class Diagnostic Classification*, `GS-21` *Deterministic Conformance Gate*, and `GS-22` *Sub-Bundle Boundary Pruning*).
   - This survey confirms that `AD-27..AD-28` and `GS-20..GS-22` are fully legitimate, passing test-suite members.
3. **Out-of-Numerical-Sequence Rule Placements:**
   - In `file-architecture.md` §3, `FA-13` (*Flat/Inline YAML Frontmatter*) appears at line 59, directly **before** `FA-05` at line 68. This occurred because `FA-13` was added during the compression pass as a general syntax rule governing all frontmatter blocks in §3.
   - In `writing-profile.md` §3, `WP-23` (*Single-Owner Instruction Reuse*) appears at line 59, directly **after** `WP-16` and before `WP-17`. In addition, `WP-24` and `WP-25` appear before `WP-22`.
   - *Recommendation:* Audit files must explain that durable IDs are immutable cross-reference anchors (`WP-15`) and must never be renumbered to restore mechanical numerical ordering.
4. **Documented Retired IDs:**
   - In `governance-schemas.md` §3, a dedicated callout explicitly documents retired IDs:
     - `GS-16` (retired: duplicated `WP-20`)
     - `GS-18` (retired: duplicated `GS-04`)
     - `GS-19` (retired: folded into `GS-17`)
   - Leaving explicit gaps rather than renumbering live IDs is an exemplary implementation of `WP-15`.

---

## 5. Cross-Traceability Matrix: Plane 4 <-> Contract Blocks

### 5.1 Upward Mapping: The 22 Contract Tags to Plane 4 Canonical Rules
Every tag in `<apex_contract v="1.0">` (`13-candidate-3A-xml.md`) and the upcoming `16-candidate-3A-ultra.md` traces directly to one or more Plane 4 rules.

| Tag # | Semantic Tag | Mode | Canonical Plane 4 Rule Owners | Key Semantic Obligations Codified in Contract |
|:---:|---|---|---|---|
| 1 | `<target>` | Unconditional | `AD-01`, `EM-04`, `WP-01` | Deliver result; positive requirement check; anti-self-authored criteria; no-op permission. |
| 2 | `<product_first>` | Unconditional | `AD-10`, `AD-09`, `AD-12` | Build working thing before machinery; fix only blockers before first working slice; product > script. |
| 3 | `<scope>` | Unconditional | `AD-18`, `AD-05`, `WP-09` | Do authorized task; report adjacent work; analyzing does not authorize implementing. |
| 4 | `<communication>` | Unconditional | `WP-02`, `WP-03`, `WP-04`, `WP-05`, `WP-12`, `AD-17` | Active voice; 1 imperative/sentence; conclusion first; Cool Blue register; plain uncertainty. |
| 5 | `<hold_position>` | Unconditional | `AD-22` | Do not reverse on pushback without evidence; treat narrow correction as narrow; state disagreement. |
| 6 | `<ground>` | Unconditional | `AD-19`, `AD-20`, `AD-06`, `WP-04`, `WP-16` | Verify against artifact (path:line); command with absence claims; check now; ~3 authoritative sources. |
| 7 | `<reuse>` | Unconditional | `AD-11`, `AD-14`, `WP-23` | Check existing scripts/tools/skills; modular composition; single-owner instruction reuse. |
| 8 | `<context>` | Unconditional | `AD-04`, `EM-03`, `EM-10` | Load JIT; no bulk reading at start; rank sources; write findings to disk per step. |
| 9 | `<recovery>` | Unconditional | `AD-07`, `AD-16`, `AD-21` | Narrow safe alternative preserving intent; halt only on genuine target/safety/integrity blockers. |
| 10 | `<stop_repairing>` | Unconditional | `AD-02`, `AD-07`, `AD-24`, `EM-05` | Stop after 2 failed attempts; pivot approach; no sunk-cost claim. |
| 11 | `<current_truth>` | Unconditional | `FA-01`, `FA-09`, `FA-11`, `WP-08`, `AD-15` | State active truth only; history/options in changelog; purge retired component names. |
| 12 | `<surgical>` | Unconditional Stub | `EM-01`, `AD-03`, `GS-02` | Never regenerate or overwrite a whole existing file. |
| 13 | `<editing>` | Gated (`execution-modes.md`) | `EM-01`, `EM-08`, `AD-23`, `GS-09`..`GS-11` | Replace exact lines verbatim; one change per edit; `git mv`/`cp`; open ref for AST patch. |
| 14 | `<new_machinery>` | Gated | `AD-25`, `AD-10`, `AD-13` | Name requirement/blocker before adding machinery; fix logic if surfaced in ~2 steps; risk proportionality. |
| 15 | `<detour>` | Gated | `AD-05`, `AD-10`, `AD-12` | Ask if needed before testing product; defer in one line if not. |
| 16 | `<authoring>` | Gated (`index.md`) | `FA-13`, `FA-06`, `FA-02`, `FA-10`, `WP-06`, `WP-07`, `WP-10`, `WP-19`, `WP-24`, `WP-25`, `GS-03`, `GS-04`, `GS-14`..`GS-17` | Flat YAML; concept frontmatter fields; front-load rules; tag `[P \| I/E/R]`; link every file; open ref for tiers. |
| 17 | `<trade_off>` | Gated (`execution-modes.md`) | `EM-06`, `EM-07`, `GS-12`, `GS-13` | Decide routine choices autonomously; material choice gets mechanism, grounding, raw I/E/R, recommendation, notes. |
| 18 | `<handover>` | Gated (`execution-modes.md`) | `EM-09`, `EM-02`, `AD-06` | Never defer checkable facts; 5-component report (Obs, Logic, Caveats, Conclusion, Verify); delegation contract. |
| 19 | `<iterative>` | Gated (`execution-modes.md`) | `EM-10`, `EM-11`, `AD-04` | Direct single-step; preflight for multi-step; file-producing loop for multi-module; MMM ladder. |
| 20 | `<schemas>` | Gated (`governance-schemas.md`) | `GS-01`, `GS-09`, `GS-10`, `GS-11` | Satisfy declared schema exactly; target edits by heading path and hints, never line numbers. |
| 21 | `<sync>` | Gated | `EM-12`, `AD-23` | Git commands first; preserve unrelated dirty files; pull with rebase and retry. |
| 22 | `<pointers>` | Terminal Guard | `general-informatics-router.md`, `WP-25`, `WP-18`, `AD-26` | Relative paths to base_ref; open ref only when condition matches and inline summary is insufficient. |

---

### 5.2 Analysis of the 24 "Unmapped" Plane 4 Rules
While 73 of the 97 Plane 4 rules are directly referenced in the contract provenance table, 24 rules are not explicitly named in the Layer 0 contract block. An audit of these 24 rules reveals why they exist in Plane 4 without being duplicated in Layer 0:

1. **`writing-profile.md` (8 unmapped rules):**
   - `WP-11` (Table vs List selection), `WP-13` (Visual block ~150 words), `WP-14` (Sentence ~20–25 words), `WP-15` (Durable ID grammar), `WP-17` (Micro-examples), `WP-20` (No default-behavior rules), `WP-21` (Heading depth ~3 levels), `WP-22` (Appendix formatting).
   - *Role:* Granular ergonomic heuristics. The contract's `<authoring>` tag encapsulates their core intent without burdening always-on prompt carriers with prose word count orientations.
2. **`file-architecture.md` (6 unmapped rules):**
   - `FA-03` (Five-Plane IA), `FA-04` (Substance Over Ceremony pointer), `FA-05` (Root `index.md` schema), `FA-07` (Durable ID pointer), `FA-08` (Sub-bundle boundary), `FA-12` (Plane sizing pointer).
   - *Role:* Repository bundle topology and validation boundaries. `FA-04`, `FA-07`, and `FA-12` are canonical pointers to `WP` rules; `FA-05` and `FA-08` govern directory structure and offline validator crawling.
3. **`execution-modes.md` (0 unmapped rules):**
   - 100% of execution modes (`EM-01` through `EM-12`) are directly cited in the contract!
4. **`anti-drift-rules.md` (3 unmapped rules):**
   - `AD-08` (Substance Over Ceremony pointer to `WP-01`), `AD-27` (Sibling module linkage), `AD-28` (Objective run outcome classification).
   - *Role:* Meta-coordination and post-session forensics.
5. **`governance-schemas.md` (7 unmapped rules):**
   - `GS-05` (Flat YAML pointer to `FA-13`), `GS-06` (Root index validation view), `GS-07` (Concept validation view), `GS-08` (Durable ID validation view), `GS-20` (Diagnostic classification), `GS-21` (Deterministic conformance gate), `GS-22` (Sub-bundle boundary validation view).
   - *Role:* Tooling diagnostics and validator gate enforcement (`okf_validator.py`).

---

## 6. Edge Cases & Observed Validator Behaviors

The table below documents specific edge cases probed during this audit and the observed behavior of the authoritative validator (`okf_validator.py`) and test suites (`test_canonical_ownership.py`).

| # | Feature / Contract | Input Edge Case | Observed Behavior | Underlying Mechanism |
|---|---|---|---|---|
| 1 | Durable ID Uniqueness (`WP-15`) | Assigning identical ID (`FA-04`) to two rules in `file-architecture.md`. | Test suite failure in `TestDurableRuleIdUniqueness`. | `test_canonical_ownership.py` mechanically extracts and checks set collision across all 7 governed files. |
| 2 | Prefix-Home Alignment (`WP-15`) | Defining a rule with `WP-` prefix inside `file-architecture.md`. | Test suite failure in `test_rule_id_prefix_matches_its_home_file`. | Prefix mapping table checks that `WP-` lives only in `writing-profile.md`. |
| 3 | Link Portability (`WP-24`) | Embedding an absolute `file:///c:/GitDev/...` link in a live specification. | Test suite failure in `TestLinkPortability.test_no_machine_specific_absolute_links`. | Regex scans non-code blocks for `file://` prefixes; requires relative Markdown links. |
| 4 | JSON Schema Re-Embedding (`WP-23`, `D9`) | Re-embedding a full JSON Schema definition inside `governance-schemas.md`. | Test suite failure in `TestNoReEmbeddedUpstreamSchema`. | Explicit assertion checks that `"$schema"` fenced blocks do not appear in `governance-schemas.md`. |
| 5 | Frontmatter Syntax (`FA-13`) | Multiline YAML list (`- item`) inside concept frontmatter. | `OKF_ERROR: OKF-FRONTMATTER-PARSE` emitted by `okf_validator.py`. | Zero-dependency line parser expects every non-comment line to contain a colon (`:`). |
| 6 | Sentence Sizing (`WP-14`, `GS-20`) | Prose sentence with 32 words (>30 words). | `ADVISORY_WARNING: STE-SENTENCE-LENGTH` emitted. | Validator warns above 30 words; does NOT fail the conformance gate (`GS-21`). |
| 7 | Sub-Bundle Boundary (`FA-08`) | Subdirectory containing an unformatted draft with its own `index.md`. | Validator stops recursion at subdirectory; reports zero errors for parent bundle. | Boundary pruning prunes sub-bundles containing their own `index.md`. |
| 8 | Canonical Pointer Integrity (`WP-23`) | `Canonical: XX-99` pointing to a non-existent rule ID. | Test suite failure in `TestCanonicalPointerIntegrity.test_every_canonical_pointer_resolves`. | Set intersection checks all `Canonical: `XX-NN`` against set of defined rules. |
| 9 | Self-Referential Pointer (`WP-23`) | `Canonical: WP-02` placed inside `writing-profile.md`. | Test suite failure in `test_canonical_pointer_never_targets_its_own_file`. | Asserts target ID is not defined in the local file. |
| 10 | Immutable ID Retirement (`WP-15`) | Retiring a duplicate rule (`GS-18`) and leaving a numerical gap. | Test suite passes 100%; durable IDs remain immutable without renumbering. | Documented retirement note explains gap; avoids breaking external cross-references. |

---

## 7. Concrete Authoring Recommendations for the 5 Module Audit Files

To fulfill Requirement R2 of `ORIGINAL_REQUEST.md`, five module audit files must be authored in `apex-meta/informatics/final/research/06-layered-rule-kb/`:
1. `audit-module-01-writing-profile.md`
2. `audit-module-02-file-architecture.md`
3. `audit-module-03-execution-modes.md`
4. `audit-module-04-anti-drift-rules.md`
5. `audit-module-05-governance-schemas.md`

### 7.1 Standardized Audit-Module File Architecture
Every audit module must strictly adhere to the following 5-chapter structure:

```yaml
---
type: Reference
id: V2-AUDIT-MODULE-0X-[MODULE-NAME]
title: Module Audit 0X — [Module Title] Semantic Block & Ownership Audit
description: Comprehensive rule-by-rule semantic block decomposition, WP-23 single-ownership ledger, redundancy purge, and cross-traceability audit for [module-name.md].
status: current_truth
tags: [module-audit, plane-4, [module-name], single-owner, semantic-blocks, traceability]
---
```

- **§1 Scope, Architectural Role & Live Rule Inventory:**
  - Plane 4 domain boundary and loading lifecycle.
  - Complete inventory table covering every defined rule: ID, Priority Tier, 3-Metric `[P | I/E/R]`, Title, Line Count, Chars, Words, and BPE Token estimate.
  - Atomic Semantic Block breakdown for each rule (`SB-XX.1`..`SB-XX.N`).
- **§2 Single-Ownership Audit (`WP-23`):**
  - Section A: Rules canonically owned by this module.
  - Section B: Sibling rules referencing this module's definitions.
  - Section C: Rules within this module delegating to external canonical owners.
  - Section D: Mechanical verification evidence (`test_canonical_ownership.py` assertions).
- **§3 Semantic Redundancies, Stale Terms & Optimization Opportunities:**
  - Identification of cross-rule and cross-module overlapping phrasing.
  - Audit of retired terms, legacy attributes (e.g. `deepen_when=`), and numerical sequencing quirks.
  - Recommended Option B surgical simplifications for downstream library module updates.
- **§4 Bidirectional Cross-Traceability Matrix:**
  - Upward mapping to `<apex_contract v="1.0">` (`13-candidate-3A-xml.md`) and `16-candidate-3A-ultra.md`.
  - Upstream empirical grounding (mapping to `ResearchOfFile10`, `module-deepening/`, `2Dos Ai Instructions.md`, `Snippets.md`).
  - Unmapped / Module-Internal Rules Ledger with rationale for inclusion in Plane 4.
- **§5 Module Failure Modes & Not-To-Dos (`WP-25`):**
  - Invariants that must NEVER be cut during refactoring.
  - Strict anti-patterns and safe compression boundaries.

---

### 7.2 Detailed Per-File Audit Authoring Recommendations

#### Module Audit 01: `audit-module-01-writing-profile.md`
- **Target File:** `apex-meta/informatics/writing-profile.md` (`WP-01`..`WP-25`, 25 rules)
- **Durable ID:** `V2-AUDIT-MODULE-01-WRITING-PROFILE`
- **Key Analysis Required:**
  1. *Significance Table Ownership:* Deepen analysis of `WP-07` as the single canonical owner of the `P0`–`P3` priority definitions and raw `I/E/R` 1–100 scales across the entire repository.
  2. *Single-Ownership Ledger:* Document `WP-23` itself as the governing meta-law of instruction reuse. Map delegations from `WP-04` $\rightarrow$ `AD-19`, `WP-08` $\rightarrow$ `AD-15`, and `WP-16` $\rightarrow$ `AD-20`. Note the deliberate tier inversion where `WP-04` and `WP-08` are P0 within the writing domain.
  3. *Unmapped Rules Rationale:* Detail the 8 unmapped rules (`WP-11`, `WP-13`, `WP-14`, `WP-15`, `WP-17`, `WP-20`, `WP-21`, `WP-22`) and justify why they belong in Plane 4 rather than Layer 0.
  4. *Downstream Optimization:* Evaluate whether `WP-13` (~150 words) and `WP-14` (~20–25 words) can be tightened into a unified sizing heuristic.

#### Module Audit 02: `audit-module-02-file-architecture.md`
- **Target File:** `apex-meta/informatics/file-architecture.md` (`FA-01`..`FA-13`, 13 rules)
- **Durable ID:** `V2-AUDIT-MODULE-02-FILE-ARCHITECTURE`
- **Key Analysis Required:**
  1. *Five-Plane IA Governance:* Deepen `FA-03` and the plane loading lifecycle table (§2), emphasizing the progressive loading sequence and token orientations (~2,000 Control, ~1,500 Scoped, ~4,000 Skills).
  2. *Frontmatter Canonical Contract:* Formalize `FA-05` and `FA-06` as the authoritative frontmatter schemas, detailing how `GS-06` and `GS-07` provide only the validation view without re-declaring fields.
  3. *Sequencing Quirks:* Audit the placement of `FA-13` before `FA-05` in §3, explaining why immutable durable IDs (`WP-15`) forbid renumbering `FA-13` to `FA-04b`.
  4. *Two-Layer Carrier Portability:* Analyze `FA-12` in light of `RP-09`/`RP-10` prompt caching (Layer 1 universal contract + Layer 2 repo-specific context).

#### Module Audit 03: `audit-module-03-execution-modes.md`
- **Target File:** `apex-meta/informatics/execution-modes.md` (`EM-01`..`EM-12`, 12 rules)
- **Durable ID:** `V2-AUDIT-MODULE-03-EXECUTION-MODES`
- **Key Analysis Required:**
  1. *100% Contract Traceability:* Highlight that all 12 `EM` rules are directly codified in `<apex_contract v="1.0">`, proving `execution-modes.md` has the highest contract density of any module.
  2. *IF-Routing Dispatch Table:* Audit the `<execution_dispatch>` table (§1) and verify that each of the 6 task adapters has a distinct conditional trigger.
  3. *Worked Example vs Authoritative Schema:* Audit `EM-08` Mode B, proving that the inline JSON block is a worked example that complies with `WP-23` by delegating the authoritative contract to `governance-schemas.md` §2.2 and `patch-intent-schema.json`.
  4. *Dual `<sync>` Mechanics:* Audit `EM-12`, documenting both the scoped push branch (`git push <paths>`) and the full sync branch (`sync`/`synch` with dirty file preservation).

#### Module Audit 04: `audit-module-04-anti-drift-rules.md`
- **Target File:** `apex-meta/informatics/anti-drift-rules.md` (`AD-01`..`AD-28`, 28 rules)
- **Durable ID:** `V2-AUDIT-MODULE-04-ANTI-DRIFT-RULES`
- **Key Analysis Required:**
  1. *Expanded Rule Inventory:* Document the presence of `AD-27` (*Sibling Module Linkage*) and `AD-28` (*Objective Run Outcome Classification*), clarifying the expansion beyond the historical `AD-01..AD-26` scope.
  2. *Highest-Impact Invariant:* Deepen analysis of `AD-01` (`[P0 | I100/E95/R05] TARGET Dominance`), documenting the `RP-05` (SpecBench positive requirement check) and `RP-07` (FixedBench no-op permission) research integration.
  3. *Hold Position & Anti-Sycophancy:* Deepen `AD-22`, analyzing how it fuses anti-sycophancy (*"Update only on new evidence, never pushback alone"*) with narrow correction discipline.
  4. *Operational Lore Grounding:* Trace the origin of `AD-02` (Two-Strike rule), `AD-07` (Sunk cost), `AD-10` (Product before infrastructure), and `AD-14` (Gall's Law) directly to `2Dos Ai Instructions.md` and `Snippets.md`.

#### Module Audit 05: `audit-module-05-governance-schemas.md`
- **Target File:** `apex-meta/informatics/governance-schemas.md` (`GS-01`..`GS-22`, 19 active rules)
- **Durable ID:** `V2-AUDIT-MODULE-05-GOVERNANCE-SCHEMAS`
- **Key Analysis Required:**
  1. *Clean ID Retirement:* Audit lines 96–98, documenting why `GS-16` (duplicate of `WP-20`), `GS-18` (duplicate of `GS-04`), and `GS-19` (folded into `GS-17`) were retired, proving that ID immutability was upheld.
  2. *Tooling & Diagnostics Catalog:* Audit §5 (`GS-20`, `GS-21`, `GS-22`), mapping the Diagnostic Rule Catalog table directly to the implementation in `okf_validator.py`.
  3. *Validation View vs Authoritative Ownership:* Audit how `governance-schemas.md` enforces schema validation (`GS-06`, `GS-07`, `GS-12`, `GS-13`) without re-declaring the schemas, citing `FA-05`, `FA-06`, and `EM-06`/`EM-07` in accordance with `WP-23`.
  4. *AST Patch Invariants:* Deepen `GS-09`, `GS-10`, `GS-11`, analyzing why brittle line-offset patching is forbidden in favor of structural AST heading paths.

---

## 8. Conclusion & Handoff Readiness

The Plane 4 Infrastructure Modules in `apex-meta/informatics/` constitute a robust, highly disciplined, and rigorously tested knowledge and governance foundation.
- **Single-Ownership Discipline (`WP-23`):** Confirmed across all 28 cross-references and verified by `test_canonical_ownership.py`.
- **Contract Traceability:** All 22 contract tags in `13-candidate-3A-xml.md` map cleanly to Plane 4 rules, with 100% representation of execution modes and clear separation of offline/tooling heuristics.
- **Audit-Module Blueprint:** The architectural blueprint, section requirements, and specific analytical foci for `audit-module-01` through `audit-module-05` are completely established.

This survey report provides the authoritative specification baseline for the next phase of authoring the five module audit files in `apex-meta/informatics/final/research/06-layered-rule-kb/`.
