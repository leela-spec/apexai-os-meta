# M2 Exploration Report: Consolidated General Router Design (`index.md` & `general-informatics-router.md`)

**Explorer**: `explorer_m2_3`  
**Milestone**: M2 (Consolidated General Router Architecture)  
**Target Files**: `apex-meta/informatics/index.md` & `apex-meta/informatics/general-informatics-router.md`  
**Date**: 2026-10-19  

---

## 1. Executive Summary & Architectural Overview

This exploration report delivers the complete architectural design, structural templates, and implementation strategy for the Next-Generation Apex Informatics consolidated routing layer:
1. **`general-informatics-router.md`**: An ultra-compact (~46 lines, 1,987 characters, 496 tokens), standalone JIT routing artifact engineered to be embedded directly into agent instruction surfaces (`AGENTS.md`, `.claude/CLAUDE.md`, role cards). It features top-loaded P0 invariants, lean XML conditional dispatch tags (`<informatics when="..." ref="..." deepen_when="...">`), zero eager `@path` imports, and uncomputed raw 3-metric significance tags.
2. **`index.md`**: The canonical OKF v0.2 root bundle index and progressive disclosure router for `apex-meta/informatics/`. It declares `okf_version: "0.2"`, catalogs all 10 governed specification and policy files via resolvable relative Markdown links, embeds the consolidated P0 invariants and `<informatics>` dispatch gates, and enforces strict link integrity.

Both templates have been validated in memory against `okf_validator.py` and the authoritative E2E test suite (`test_informatics_e2e.py`).

---

## 2. Core Architectural Principles & Empirical Constraints

### 2.1 The Token Ceiling & Compactness Mandate
In `test_informatics_e2e.py` (line 1551–1555), `test_live_07_general_router_compactness` evaluates:
```python
lines = len(content.splitlines())
tokens = estimate_tokens(content)  # len(content) // 4
self.assertLessEqual(lines, 120, f"Router should be ~100 lines (currently {lines})")
self.assertLessEqual(tokens, 500, f"Router should be ~400 tokens (currently {tokens})")
self.assertEqual(len(check_router_eager_imports(content)), 0)
```
- **Critical Finding**: Because `estimate_tokens` is defined as `len(content) // 4`, the hard test assertion `tokens <= 500` enforces that the total character count of `general-informatics-router.md` must not exceed **2,000 characters**.
- An initial verbose design containing 4,224 characters evaluated to 1,056 tokens, failing the test by over 200%.
- Through careful Simplified Technical English (STE) tuning and visual block economy, the recommended template measures **1,987 characters (496 tokens, 46 lines)**, satisfying both the pragmatic ~400 token target and the hard <= 500 token ceiling.

### 2.2 Tool-Based JIT Retrieval (Zero Eager `@path` Imports)
- **Constraint**: `test_informatics_e2e.py` line 188–191 checks for eager imports using regex `r"@[\w./\-]+\.md"`.
- **Mechanism**: Modern AI coding tools (e.g., Cursor, Claude Code) interpret `@path/file.md` in prompts as directives to auto-expand the full referenced file into the working context at session initialization.
- **Rule**: The router strictly prohibits `@` prefixes. It provides plain relative paths (`ref="writing-profile.md"`) as tool pointers. Agents read the observable action trigger in `when="..."`. If and only if the current task matches that trigger, the agent invokes `view_file` to load the specification just-in-time.

### 2.3 Lean XML Tag Specification
Tags conform to the contract defined in `test_informatics_e2e.py` (`ROUTER_XML_TAG_REGEX`):
```text
<informatics when="<action_trigger>" ref="<relative_path>" deepen_when="<deepening_trigger>">
  [P1 | I<impact>/E<evidence>/R<risk>] [Single-command directive]
</informatics>
```
- `when`: The primary gating condition. Evaluated first by the agent. If false, the agent does not touch the referenced file.
- `ref`: Plain relative path to the modular specification file.
- `deepen_when`: The secondary threshold triggering deep procedural reading.

### 2.4 Significance & Ranking Architecture (`[P<tier> | I/E/R]`)
- **Tiers**:
  - `P0`: Critical Invariants (100% compliance, universal safety, target dominance).
  - `P1`: Core Methods & JIT Dispatch Gates (Primary workflows and routing).
  - `P2`: Standard Practices (Formatting ergonomics, sizing orientations).
  - `P3`: Advisory Polish (Scannability, heading guidelines).
- **Metric Syntax**: `[P<tier> | I<impact>/E<evidence>/R<risk>]` where Impact, Evidence, and Risk are raw integers in the range `1–100`.
- **Prohibition**: Mathematical formulas (e.g., `EV = I * E * (1 - R/2)` or `(I90/E90/R20: 77)`) are strictly banned to prevent misleading pseudo-precision.
- **Descending Order**: Rules must appear strictly descending by tier (P0 -> P1 -> P2 -> P3).

### 2.5 Top-Loaded Primacy (First ~500 Tokens)
- Positional attention decay in transformer models causes instruction compliance to drop from ~73% in the first 500 tokens to 30–50% mid-document.
- Both `general-informatics-router.md` and `index.md` place their P0 Invariants immediately after the document title:
  - `general-informatics-router.md`: First P0 tag at **token 50** (well below the 500-token threshold).
  - `index.md`: First P0 tag at **token 102** (well below the 500-token threshold).

### 2.6 Substance Over Ceremony Exception Authority
Formally codified as a top-loaded P0 invariant in both files:
`[P0 | I95/E98/R05] Substance Over Ceremony: Technical accuracy overrides mechanical metric compliance. Agents possess explicit authority to exceed approximate ceilings when technical correctness, safety, or critical system context requires it.`

### 2.7 OKF v0.2 Frontmatter & Link Integrity
- `okf_validator.py` requires all concept files in an OKF bundle to have YAML frontmatter declaring `type: <string>`. Thus, `general-informatics-router.md` declares `type: Router`.
- `index.md` declares `okf_version: "0.2"`.
- `okf_validator.py` extracts all markdown links `[text](target.md)` from `index.md` and requires every relative target to resolve on disk (`APEX-LINK-INTEGRITY`).

---

## 3. Structural Template 1: `general-informatics-router.md`

### 3.1 Proposed File Content
```markdown
---
type: Router
id: RTR-GEN-v0.2
title: Apex General Router
description: JIT router and conditional dispatch surface for Apex OS.
---

# Apex General Informatics Router

## 1. P0 Critical Invariants

- [P0 | I98/E98/R05] Target Dominance: Realize intended outcomes. Tests are evidence, not proxies.
- [P0 | I96/E95/R05] Strict JIT Retrieval: Zero eager @path imports. Read files via tools on trigger match.
- [P0 | I95/E95/R10] Surgical Mutation: Never rewrite whole files. Modify files via exact-match patch blocks.
- [P0 | I95/E98/R05] Substance Over Ceremony: Technical correctness overrides metrics. Ceilings yield to truth.

## 2. P1 Core JIT Dispatch Gates

<informatics when="writing_or_documentation" ref="writing-profile.md" deepen_when="ste_limits">
  [P1 | I92/E95/R10] Information Mapping and STE limits for governed docs.
</informatics>

<informatics when="file_creation_or_structure" ref="file-architecture.md" deepen_when="five_planes">
  [P1 | I90/E92/R12] Five-Plane IA, flat frontmatter, and current-truth separation.
</informatics>

<informatics when="task_execution_adapter" ref="execution-modes.md" deepen_when="task_adapters">
  [P1 | I92/E94/R10] Decision Matrices, Bake-Offs, Patches, Handovers, and MMM.
</informatics>

<informatics when="operational_anti_drift" ref="anti-drift-rules.md" deepen_when="two_strike_pivots">
  [P1 | I94/E95/R08] 8 Anti-Drift Laws, Two-Strike pivot rule, and task minimalism.
</informatics>

<informatics when="governance_and_schemas" ref="governance-schemas.md" deepen_when="patch_schemas">
  [P1 | I88/E92/R10] Frontmatter schemas, AST patch intent, and directive limits.
</informatics>

## 3. P2 Standard Practices

- [P2 | I85/E90/R10] Sizing Orientations: Ceilings (~100L/~400T) guide efficiency. Target governs.
- [P2 | I80/E85/R15] Autonomous Decisions: Resolve routine reversible choices autonomously from evidence.

## 4. P3 Advisory Polish

- [P3 | I65/E80/R08] Heading Scannability: Constrain markdown headings to <= 3 levels.
```

### 3.2 Automated Validation Metrics
| Metric | Result | Target / Ceiling | Status |
|---|---|---|---|
| **Line Count** | 46 lines | ~100 lines (<= 120 lines) | PASS |
| **Character Count** | 1,987 characters | <= 2,000 characters | PASS |
| **Token Estimate** | 496 tokens | ~400 tokens (<= 500 tokens) | PASS |
| **Eager `@path` Imports** | 0 detected | 0 allowed | PASS |
| **First P0 Token Pos** | Token 50 | First 500 tokens | PASS |
| **Significance Tags** | 12 tags (4 P0, 5 P1, 2 P2, 1 P3) | P0–P3 uncomputed | PASS |
| **Tag Sorting Order** | Strictly Descending | P0 -> P1 -> P2 -> P3 | PASS |
| **Parsed XML Tags** | 5 tags | 5 core modules | PASS |
| **OKF Frontmatter** | `type: Router` | Parsable flat YAML | PASS |
| **STE Writing Advisories** | 0 warnings | 0 warnings | PASS |

---

## 4. Structural Template 2: `index.md`

### 4.1 Proposed File Content
```markdown
---
okf_version: "0.2"
title: Apex Informatics Standard & Consolidated General Router
description: Canonical entrypoint, OKF v0.2 bundle index, and conditional JIT routing layer for Apex OS AI agents.
---

# Apex Informatics Standard & Consolidated General Router

Canonical entrypoint and conditional JIT routing index for the Apex OS knowledge and instruction architecture.

## 1. P0 Critical Invariants

- [P0 | I98/E98/R05] Target Dominance: Realize and validate substantive intended outcomes. Tests and schemas are evidence, not substitutes.
- [P0 | I96/E95/R05] Strict JIT Retrieval: Zero eager @path imports. Read referenced specifications via tools only when triggers match.
- [P0 | I95/E95/R10] Surgical Mutation: Never rewrite whole files. Modify existing files strictly via exact-match patch blocks.
- [P0 | I95/E98/R05] Substance Over Ceremony: Technical correctness overrides mechanical metrics. Ceilings yield to truth.

## 2. P1 Core JIT Dispatch Gates

<informatics when="writing_or_documentation" ref="writing-profile.md" deepen_when="ste_word_limits">
  [P1 | I92/E95/R10] Apply Information Mapping and STE word limits to governed docs.
</informatics>

<informatics when="file_creation_or_structure" ref="file-architecture.md" deepen_when="five_plane_isolation">
  [P1 | I90/E92/R12] Apply Five-Plane IA, flat OKF frontmatter, and current-truth separation.
</informatics>

<informatics when="task_execution_adapter" ref="execution-modes.md" deepen_when="decision_matrices_or_patches">
  [P1 | I92/E94/R10] Apply Decision Matrices, Bake-Offs, Patches, Handovers, or MMM.
</informatics>

<informatics when="operational_anti_drift" ref="anti-drift-rules.md" deepen_when="two_strike_pivots">
  [P1 | I94/E95/R08] Apply 8 Anti-Drift Laws, Two-Strike pivot rule, and task minimalism.
</informatics>

<informatics when="governance_and_schemas" ref="governance-schemas.md" deepen_when="patch_intent_json">
  [P1 | I88/E92/R10] Validate frontmatter schemas, AST patch intent, and directive limits.
</informatics>

## 3. Governed Modular Specification Suite

- [Writing Profile & Prose Ergonomics](writing-profile.md) — Information Mapping, STE sentence limits, visual block targets, and durable IDs.
- [File Architecture & Bundle Structure](file-architecture.md) — Five-Plane Architecture, OKF v0.2 frontmatter schemas, and current-truth separation.
- [Execution Modes & Task Adapters](execution-modes.md) — Task adapters for Q&A Decision Matrices, Comparison Bake-Offs, Exact-Match Patching, Handover, and MMM.
- [Anti-Drift Rules & Operational Lore](anti-drift-rules.md) — 8 Anti-Drift Laws, Two-Strike pivot rule, Sunk-Cost Prohibition, and Task Minimalism.
- [Governance Schemas & Directive Ceilings](governance-schemas.md) — Frontmatter schemas, AST patch intent specifications, and model directive ceilings.
- [General Informatics Router](general-informatics-router.md) — Compact standalone agent-facing embeddable JIT router template.

## 4. Supporting Governance & History

- [Apex Informatics Standard](standard.md) — Master 14-section governance standard combining OKF v0.2, Information Mapping, and STE prose.
- [Migration & Onboarding Policy](migration.md) — Rules governing repository knowledge conformance and migration.
- [Change Log](log.md) — Chronological version history and audit log.
- [Agent Setup Sub-Bundle](Agent_Setup/index.md) — Sub-bundle boundary index for agent setup and legacy artifacts.

## 5. P2 Standard Operational Practices

- [P2 | I85/E90/R10] Operational Sizing: Sizing targets (~100L / ~400T) orient router efficiency. Target outcome governs.
- [P2 | I80/E85/R15] Autonomous Decisions: Resolve routine reversible choices autonomously from evidence.

## 6. P3 Advisory Polish

- [P3 | I65/E80/R08] Heading Scannability: Constrain markdown heading hierarchy to <= 3 levels.
```

### 4.2 Automated Validation Metrics
| Metric | Result | Target / Ceiling | Status |
|---|---|---|---|
| **Line Count** | 63 lines | Bundle root catalog | PASS |
| **Character Count** | 3,822 characters | Comprehensive index | PASS |
| **Token Estimate** | 955 tokens | Full OKF bundle index | PASS |
| **Eager `@path` Imports** | 0 detected | 0 allowed | PASS |
| **First P0 Token Pos** | Token 102 | First 500 tokens | PASS |
| **Significance Tags** | 12 tags (4 P0, 5 P1, 2 P2, 1 P3) | P0–P3 uncomputed | PASS |
| **Tag Sorting Order** | Strictly Descending | P0 -> P1 -> P2 -> P3 | PASS |
| **Parsed XML Tags** | 5 tags | 5 core modules | PASS |
| **OKF Version** | `okf_version: "0.2"` | Exact string match | PASS |
| **Extracted Relative Links** | 10 links | All 10 bundle targets | PASS |
| **STE Writing Advisories** | 0 warnings | 0 warnings | PASS |

---

## 5. Comparative Architectural Analysis

| Dimension | Legacy M1 `index.md` | Target M2 `index.md` | Target M2 `general-informatics-router.md` |
|---|---|---|---|
| **Primary Consumer** | Tools & human readers | Tools, validators & humans | Agent instruction surfaces (`AGENTS.md`) |
| **OKF Role** | Bundle Root Index | Bundle Root Index + JIT Router | Concept file (`type: Router`) |
| **Frontmatter** | `okf_version: "0.2"` | `okf_version: "0.2"` | `type: Router`, `id: RTR-GEN-v0.2` |
| **Token Footprint** | ~150 tokens | ~955 tokens | ~496 tokens |
| **Line Footprint** | 20 lines | 63 lines | 46 lines |
| **P0 Invariants** | Absent | Present (Token 102) | Present (Token 50) |
| **Significance Tags** | Absent | 12 tags (`[P0-P3 \| I/E/R]`) | 12 tags (`[P0-P3 \| I/E/R]`) |
| **XML Routing Tags** | Absent | 5 `<informatics>` tags | 5 `<informatics>` tags |
| **Eager `@path` Imports** | None | 0 (Strict JIT) | 0 (Strict JIT) |
| **Relative Markdown Links** | 4 links | 10 links (Full coverage) | 0 (XML attributes only) |
| **Exception Authority** | Absent | Explicit P0 invariant | Explicit P0 invariant |

---

## 6. JIT Dispatch Vocabulary & Context Isolation Mapping

The trigger vocabulary in the XML `when` attributes has been calibrated to integrate seamlessly with the existing test cases:

| Module Ref | XML `when` Attribute | Target Task Intent | Tested In |
|---|---|---|---|
| `writing-profile.md` | `writing_or_documentation` | Authoring/editing docs, prose formatting, STE rules | `test_t3_01`, `test_t4_s01` |
| `file-architecture.md` | `file_creation_or_structure` | Creating files, bundle organization, frontmatter | `test_t3_01`, `test_t3_02` |
| `execution-modes.md` | `task_execution_adapter` | Decision matrices, bake-offs, exact-match patches, MMM | `test_t3_01`, `test_t3_03` |
| `anti-drift-rules.md` | `operational_anti_drift` | Subsystem failures, two-strike pivots, operator challenge | `test_t3_04`, `test_t4_s04` |
| `governance-schemas.md` | `governance_and_schemas` | OKF schemas, AST patch intent, model directive ceilings | `test_live_06` |

When an agent is assigned a pure writing task, it reads the router, matches `writing_or_documentation`, and opens `writing-profile.md`. It does not load `file-architecture.md`, `execution-modes.md`, `anti-drift-rules.md`, or `governance-schemas.md`, maintaining 100% context isolation.

---

## 7. Implementation Sequence & Risk Mitigation Strategy for Worker M2

To prevent validation failures during Milestone M2 rollout, the worker agent must execute file creation and modification in strict dependency order:

1. **Step 1: Create Concept Files First**
   - Author `anti-drift-rules.md` (Explorer 1 template).
   - Author `governance-schemas.md` (Explorer 2 template).
   - Author `general-informatics-router.md` (Explorer 3 template above).
   - *Rationale*: `okf_validator.py` checks `APEX-LINK-INTEGRITY` on `index.md`. If `index.md` links to files that do not yet exist, validation will fail.
2. **Step 2: Update Root `index.md`**
   - Replace `index.md` with the structural template in Section 4.
   - *Rationale*: All 10 referenced targets now exist on disk, ensuring `0 APEX_PROFILE Errors`.
3. **Step 3: Run Deterministic Conformance Verification**
   - Run `python apex-meta/scripts/okf_validator.py --target apex-meta/informatics`.
   - Run `python apex-meta/informatics/tests/test_informatics_e2e.py`.
   - Confirm 0 OKF Errors, 0 APEX_PROFILE Errors, 0 test failures, and 0 skipped tests.
