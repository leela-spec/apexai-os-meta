# Project: Next-Generation Apex Informatics Architecture & Instruction System

## Architecture
The Next-Generation Apex Informatics Architecture provides an ultra-token-efficient, modular instruction system for AI agents. It replaces monolithic instruction documents with a high-primacy JIT routing layer that dynamically directs agents into modular, single-responsibility specification files based on conditional action triggers.

### Component Layers
1. **Root Router Layer (`index.md` / `general-informatics-router.md`)**:
   - Ultra-compact entry surface (~100 lines / ~400 tokens / <= 2,000 characters).
   - Top-loaded P0 invariants in first ~500 tokens (token 50).
   - Lean XML dispatch tags (`<informatics when="..." ref="..." deepen_when="...">`).
   - Zero eager `@path` imports; strict tool-based JIT retrieval.
2. **Foundational Specification Triad**:
   - `writing-profile.md`: Prose ergonomics, Information Mapping, "One Chunk, One Job", visual block targets, STE sentence length guidelines, durable IDs vs. ordinary labels.
   - `file-architecture.md`: OKF v0.2 frontmatter schemas, Five-Plane Information Architecture, concept/index/changelog layout, strict current-truth separation (zero inline changelogs), top-loaded primacy.
   - `execution-modes.md`: Deterministic task adapters for Q&A Decision Matrices, Comparison/Bake-offs, Exact-Match Patch Intent, Handover protocols, and MMM iterative execution.
3. **Specialized Governance & Behavioral Modules**:
   - `anti-drift-rules.md`: 8 Anti-Drift Laws, Two-Strike Rule, Sunk-Cost Prohibition, Operator Challenge Boundary, Task Minimalism, Anti-Overcorrection, Context Hygiene, Residual Name Eradication, and Substance-Over-Ceremony Exception Authority.
   - `governance-schemas.md`: Frontmatter schemas, AST patch intent specifications (`patch-intent-schema.json`), Decision Matrix schemas, and model-calibrated directive ceilings.
4. **Scaffolding & Isolation**:
   - `Agent_Setup/index.md`: OKF v0.2 sub-bundle boundary pruning for legacy setup artifacts.
5. **E2E Test & Validation Suite**:
   - Standalone test runner and automated test suites verifying deterministic OKF conformance, tag parsing, token ceilings, context isolation, and operational snippet codification (`test_informatics_e2e.py`).

---

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | Sub-Bundle Isolation (`Agent_Setup/index.md`) | OKF v0.2 sub-bundle index pruning untracked directory from validator traversal | M1 | Survey 3 / Codebase |
| 2 | P0–P3 Priority Tier Classification | Formal definition of P0 (Invariants), P1 (Core Methods), P2 (Standard Practices), P3 (Advisories) | M1 | ORIGINAL_REQUEST R1 |
| 3 | Raw 3-Metric Estimates `[P<tier> \| I/E/R]` | Qualitative uncomputed estimates (1–100 scale) for Impact, Evidence, Risk without mathematical formulas | M1 | ORIGINAL_REQUEST R1 |
| 4 | Top-Loaded Primacy Structure | Positioning critical invariants within first ~500 tokens across all specification files | M1 | ORIGINAL_REQUEST R1 / Survey 1 |
| 5 | Information Mapping & "One Chunk, One Job" | Modular section design with ~150-word prose chunks before tables/lists | M1 | ORIGINAL_REQUEST R2, R4 |
| 6 | Simplified Technical English (STE) Word Limits | Guidelines targeting ~20 words/procedural sentence, ~25 words/descriptive sentence, active voice | M1 | ORIGINAL_REQUEST R2, R4 |
| 7 | Heading Depth Hierarchy | Scannable headers constrained to <= 3 levels (`#`, `##`, `###`) unless technical complexity requires deeper | M1 | ORIGINAL_REQUEST R2 |
| 8 | Durable IDs vs. Ordinary Labels | Syntax and uniqueness requirements for durable section and rule identifiers | M1 | ORIGINAL_REQUEST R4 / Survey 1 |
| 9 | OKF v0.2 Frontmatter Specification | Strict flat/inline YAML frontmatter (`type: ...`, unique `id: ...`, inline lists) compatible with custom line parser | M1 | ORIGINAL_REQUEST R4 / Survey 3 |
| 10 | Five-Plane Information Architecture | Separation of Control, Scoped Instructions, Procedures, Knowledge Bundles, and Evidence/History | M1 | ORIGINAL_REQUEST R4 / standard.md |
| 11 | Strict Current-Truth Separation | Zero inline changelogs in active specification files; dedicated logs and archives | M1 | ORIGINAL_REQUEST R4 / Survey 1 |
| 12 | Q&A Decision Matrix Adapter | Structured decision format with Grounding, raw `(I<val>/E<val>/R<val>)`, recommendation, one-line rejection notes | M1 | ORIGINAL_REQUEST R4 / Snippets.md |
| 13 | Comparison & Bake-Off Adapter | Multi-metric candidate matrix, common criteria, calibrated qualitative scoring | M1 | ORIGINAL_REQUEST R4 / Snippets.md |
| 14 | Exact-Match Patch Discipline | Deterministic block replacement syntax (`<file>/<old>/<new>`), exact whitespace, zero hallucinated rewrites | M1 | ORIGINAL_REQUEST R4 / Snippets.md |
| 15 | Handover / Handoff Adapter | Intent/outcome focus, input/process/output, Definition of Done, and anti-drift boundary | M1 | ORIGINAL_REQUEST R4 / 2Dos Ai Instructions |
| 16 | MMM Iterative Execution Adapter | Complexity routing (Route 0 direct, Route 1 compact preflight, Route 2 full spec), top-down decomposition, bottom-up verification | M1 | ORIGINAL_REQUEST R4 / Snippets.md |
| 17 | 8 Anti-Drift Laws Codification | TARGET dominates, 2-strike rule, no sunk-cost reasoning, product before ceremony, stop on drift | M2 | ORIGINAL_REQUEST R5 / Snippets.md |
| 18 | Operator Challenge Boundary | Formal prompt asking "Does this need to be fixed before we can test the actual product?" | M2 | ORIGINAL_REQUEST R5 / Snippets.md |
| 19 | Task Minimalism & Anti-Overcorrection | Gall's Law, Minto BLUF, Minimal Viable Artifact, Zero-Speculation Scope Ceiling, single-step execution | M2 | ORIGINAL_REQUEST R5 / AnitOverEng.md |
| 20 | Context Hygiene & Residual Name Eradication | Conscious context loading, eradication of residual confusing names post-refactor, prevention of whole-file rewrites | M2 | ORIGINAL_REQUEST R5 / 2Dos Ai Instructions |
| 21 | Substance Over Ceremony Exception Authority | Explicit agent authority to relax approximate ceilings when technical accuracy and clarity require it | M2 | ORIGINAL_REQUEST R2 / Survey 2 |
| 22 | Model Directive Ceilings | Calibrated directive limits (50 for GPT-4o, 80 for Claude Reasoning, 100 for Gemini/o3) | M2 | ORIGINAL_REQUEST R2 / Survey 1 |
| 23 | Governance Frontmatter & Patch Schemas | Schema specifications for OKF v0.2, Patch Intent (`patch_intent.v1`), and decision matrices | M2 | ORIGINAL_REQUEST R4 / Survey 1 |
| 24 | Consolidated General Router Design | Compact entry surface (~100 lines / ~400 tokens / <= 2,000 chars) with top-loaded P0 invariants | M2 | ORIGINAL_REQUEST R2, R3 |
| 25 | Lean XML IF-Clause Routing Tags | Tags formatted as `<informatics when="..." ref="..." deepen_when="...">` with clean Markdown bodies | M2 | ORIGINAL_REQUEST R3 |
| 26 | Zero Eager `@path` Imports Enforcement | Enforcing tool-based JIT retrieval instead of auto-expanding context | M2 | ORIGINAL_REQUEST R3 / Global Snippet Grammar |
| 27 | Root Index Conformance & Link Integrity | `okf_version: "0.2"` frontmatter and fully resolvable relative links in `index.md` | M2 | ORIGINAL_REQUEST R3 / okf_validator |
| 28 | Deterministic Conformance Verification | Execution of `okf_validator.py` reporting 0 OKF Errors and 0 APEX_PROFILE Errors | M3 | Acceptance Criteria 1 |
| 29 | Significance Ranking & Syntax Audit | Automated verification that all rules bear valid uncomputed `[P<tier> \| I/E/R]` tags and descending sort | M3 | Acceptance Criteria 2 |
| 30 | Router Compactness & Token Budget Audit | Automated verification confirming router is ~100 lines / ~400 tokens with top-loaded logic | M3 | Acceptance Criteria 3 |
| 31 | Context Isolation Verification | Simulated test demonstrating agent executing pure writing task loads only `writing-profile.md` | M3 | Acceptance Criteria 4 |
| 32 | Operational Lore Traceability Verification | Automated verification that all critical snippets from `Snippets.md` and `2Dos Ai Instructions.md` are codified | M3 | Acceptance Criteria 5 |
| 33 | Adversarial Coverage Hardening (Tier 5) | White-box adversarial testing of boundary conditions, edge cases, and parser quirks | M3 | Acceptance Criteria / Pattern |

---

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Scaffolding & Core Triad Specification | Author `Agent_Setup/index.md` (isolation), `writing-profile.md`, `file-architecture.md`, and `execution-modes.md` | None | DONE |
| M2 | Governance, Anti-Drift & Consolidated Router | Author `anti-drift-rules.md`, `governance-schemas.md`, `index.md`, and `general-informatics-router.md` | M1 | DONE |
| M3 | Final Acceptance: 100% E2E Test Suite Pass, Adversarial Hardening (Tier 5), and Forensic Audit | Pass 100% of E2E test suite (Tiers 1-4), execute Tier 5 adversarial hardening, and pass Forensic Integrity Audit | M2, E2E Test Suite | DONE |

---

## Parallel Track: E2E Testing Track
- **Goal**: Design and build comprehensive opaque-box E2E test suite derived from `ORIGINAL_REQUEST.md` (Tiers 1–4).
- **Status**: DONE (Published `TEST_READY.md`; 146 automated tests in `test_informatics_e2e.py`).

---

## Interface Contracts
### `index.md` (Router) ↔ Modular Specification Suite
- Tags format: `<informatics when="<action_trigger>" ref="<relative_path>" deepen_when="<deepening_trigger>">`
- File paths: Plain relative markdown links (`writing-profile.md`, `file-architecture.md`, `execution-modes.md`, `anti-drift-rules.md`, `governance-schemas.md`).
- Semantics: Agent reads ONLY the top-level trigger `when="..."`. If condition is not met, do NOT open the referenced file. If met, open plain path JIT via file viewing tool.

### YAML Frontmatter Contract (All Modules)
- Format: Flat key-value pairs or inline bracket lists (`tags: [a, b]`). No multiline `- list` items (causes `okf_validator.py` parse failure).
- Mandatory Fields:
  - Root `index.md`: `okf_version: "0.2"`
  - Concept files: `type: <string>` (e.g. `Specification`, `Profile`, `Adapter`, `Governance`), `title: <string>`, `description: <string>`
  - Optional unique `id: <string>` (must be unique across bundle if present).

### Significance Tag Contract
- Syntax: `[P<0-3> | I<1-100>/E<1-100>/R<1-100>]` (e.g. `[P0 | I95/E95/R10]`).
- Math formulas strictly prohibited (no computed scores).
- Ordering: Descending priority tier (P0 -> P1 -> P2 -> P3) with highest Impact/Evidence and lowest Risk top-loaded.

---

## Code Layout
- Target Directory: `c:\GitDev\apexai-os-meta\apex-meta\informatics\`
  - `Agent_Setup/index.md` — Sub-bundle boundary index [DONE]
  - `file-architecture.md` — File creation & bundle structure specification [DONE]
  - `writing-profile.md` — Writing & prose ergonomics specification [DONE]
  - `execution-modes.md` — Task adapters & execution if-clauses [DONE]
  - `anti-drift-rules.md` — Operational lore, anti-drift laws & minimalism [DONE]
  - `governance-schemas.md` — Frontmatter, patch intent, and decision schemas [DONE]
  - `index.md` — Consolidated general router [DONE]
  - `general-informatics-router.md` — Agent-facing embedded router template [DONE]
  - `tests/test_informatics_e2e.py` — Comprehensive E2E test suite runner [DONE]
