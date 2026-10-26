# M2 Exploration Report: Governance Schemas & Directive Ceilings Specification

**Artifact Type**: Technical Exploration & Architecture Specification Report  
**Author**: Explorer Subagent (`explorer_m2_2`)  
**Parent Orchestrator ID**: `b50b8c99-9617-41ab-85e5-9b6924358d5a`  
**Target Milestone**: M2 — Governance, Anti-Drift & Consolidated Router  
**Target Production Artifact**: `apex-meta/informatics/governance-schemas.md`  
**Date**: 2026-10-19  

---

## 1. Executive Summary

This report establishes the complete architectural design, formal schemas, and exact structural template for `apex-meta/informatics/governance-schemas.md`. This module serves as the authoritative specification for all data schemas, patch intent contracts, decision frameworks, and cognitive directive ceilings across the Apex Informatics Architecture.

### Key Architectural Deliverables:
1. **OKF v0.2 Frontmatter Governance**: Formal specification of the flat YAML frontmatter contract enforced by `apex-meta/scripts/okf_validator.py`. Establishes strict type taxonomy (`Specification`, `Standard`, `Profile`, `Adapter`, `Governance`, `Policy`, `Reference`), root index requirements (`okf_version: "0.2"`), and bundle-wide unique durable IDs (`id: GOV-SCHEMAS-v0.2`), while explicitly mitigating parser traps (banning multiline `- item` lists in favor of inline `tags: [a, b]`).
2. **Deterministic Patch Intent Specification (`patch_intent.v1`)**: Formalization of the semantic AST patch intent schema from `.claude/skills/deterministic-markdown-patcher2/references/patch-intent-schema.json`. Establishes operations (`replace-once`, `replace-heading-section`, `frontmatter-set`), target heading paths, disambiguating hints, and mandatory safety invariants (`require_unique_match: true`, `fail_on_ambiguity: true`, `allow_full_file_rewrite: false`). Explicitly prohibits brittle line numbers and diff hunks.
3. **Decision Matrix & Bake-Off Evaluation Schemas**: Standardized schemas for Q&A Decision Matrices and 4-Phase Comparison Bake-Offs. Mandates concrete grounding references, raw uncomputed 3-metric tags `(I<val>/E<val>/R<val>)`, and one-line rejection notes for disqualified options. Formally bans pseudo-mathematical scoring formulas (such as REI expected value calculations).
4. **Model-Calibrated Directive Ceilings**: Empirical cognitive budget constraints derived from production benchmarks in `2Do_context_file_authority_reference.md`: 50 directives for GPT-4o and Claude Standard, 80 for Claude Reasoning, and 100 for Gemini 2.5 Pro / o3. Codifies directive counting rules and the mandatory Deletion Test.
5. **Significance & Ranking Architecture**: Strict sorting discipline enforcing descending priority tiers (P0 -> P1 -> P2 -> P3) with raw uncomputed 3-metric tags `[P<tier> | I<impact>/E<evidence>/R<risk>]` (scale 1–100) and top-loaded P0 invariants within the first 500 tokens (73% compliance vs 30–50% mid-document decay).

---

## 2. Problem Boundary & Scope Analysis

### 2.1 Context & Objectives
The Apex Informatics Architecture modularizes system instructions into lean, single-responsibility specification files retrieved JIT via conditional XML routing tags. Milestone M1 established the core triad (`writing-profile.md`, `file-architecture.md`, `execution-modes.md`). Milestone M2 delivers the governance and anti-drift specifications (`anti-drift-rules.md`, `governance-schemas.md`) and the consolidated router (`index.md`, `general-informatics-router.md`).

`governance-schemas.md` addresses the critical governance plane: defining machine-readable contracts, schema validation rules, cognitive capacity limits, and evaluation formats so that agents operate within deterministic, verified guardrails.

### 2.2 Scope Boundaries
- **In Scope**:
  - Exact JSON Schema and AST block structures for `patch_intent.v1`.
  - OKF v0.2 frontmatter schemas and validation constraints for root index and concept files.
  - Decision Matrix schema and 4-Phase Bake-Off evaluation schema.
  - Model directive ceilings (50/80/100) and cognitive load accounting.
  - Significance ranking tags `[P<tier> | I/E/R]` and top-loaded primacy.
  - Complete, verbatim markdown template for `governance-schemas.md`.
- **Out of Scope (Preserved in Peer Modules)**:
  - Prose style rules and STE sentence word counts (governed by `writing-profile.md`).
  - Five-Plane Architecture definition and directory layout (governed by `file-architecture.md`).
  - Agent task execution workflows and tool calling protocols (governed by `execution-modes.md`).
  - Behavioral anti-drift laws and operator challenge boundary (governed by `anti-drift-rules.md`).
  - Direct modifications to repository production files (strictly read-only exploration).

---

## 3. Evidence Chain & Codebase Findings

### 3.1 OKF v0.2 Validator Constraints
- **Observation**: Inspection of `apex-meta/scripts/okf_validator.py` reveals a zero-dependency, line-based YAML parser (`parse_frontmatter`, lines 45–84).
- **Rule 1 (Colons Required)**: Line 69 enforces `if ":" not in line_clean: return None, content, f"Malformed frontmatter on line {line_num}: missing ':'"`.
- **Consequence**: Standard YAML multiline lists:
  ```yaml
  tags:
    - tag1
    - tag2
  ```
  fail validation with `OKF-FRONTMATTER-PARSE` because the line `- tag1` lacks a colon.
- **Verification**: `test_b06_01_yaml_multiline_list_without_colons` in `test_informatics_e2e.py` confirms that multiline `- item` lists are rejected, whereas inline lists (`tags: [tag1, tag2]`) parse cleanly.
- **Rule 2 (Mandatory Type)**: Line 267 enforces `OKF-TYPE-REQUIRED`: every concept file must have a non-empty `type` string.
- **Rule 3 (Unique Durable ID)**: Line 280 enforces `APEX-UNIQUE-DURABLE-ID`: if `id` is present, it must be unique across all concept files in the bundle.
- **Rule 4 (Root Index Declaration)**: Line 181 enforces `OKF-VERSION-DECLARATION`: `index.md` must declare `okf_version: "0.2"`.

### 3.2 Patch Intent Schema (`patch_intent.v1`)
- **Observation**: Inspection of `.claude/skills/deterministic-markdown-patcher2/references/patch-intent-schema.json` establishes the JSON Schema (draft 2020-12) for AST patch intents.
- **Schema Version**: `schema_version: "patch_intent.v1"`.
- **Operations Supported**: `inspect`, `locate`, `extract-span`, `replace-once`, `replace-heading-section`, `frontmatter-set`, `diff`, `apply-intent`, `validate-intent`.
- **Mandatory Safety Consts**:
  ```json
  "safety": {
    "require_unique_match": true,
    "fail_on_ambiguity": true,
    "allow_full_file_rewrite": false,
    "max_files_touched": 1
  }
  ```
- **Forbidden Properties**: The schema's `not.anyOf` block explicitly forbids brittle text identifiers:
  - `old_text`, `required_old_text`, `line_number`, `line_start`, `line_end`, `line_range`, `hunk`, `diff_hunks`, `unified_diff`.
- **Reasoning**: Line numbers and unified diff hunks drift rapidly across concurrent agent turns. Semantic AST matching relies on immutable structural anchors (`heading_path`, `nearby_phrases`, `symbol_or_section_names`).

### 3.3 Model Directive Ceilings & Cognitive Capacity
- **Observation**: Inspection of `apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__ai_handling_routing/2Do_context_file_authority_reference.md` (lines 9–14, 357–363) and `ORIGINAL_REQUEST.md` (R2) documents empirical model capacities:
  - **GPT-4o / Claude 3.7 Sonnet (Standard)**: ≤ 50 directives. (Beyond 50, compliance collapses exponentially due to attention fatigue).
  - **Claude 3.7 Sonnet (Reasoning)**: ≤ 80 directives. (Reasoning tokens provide an internal deliberation buffer, but still face instruction degradation).
  - **Gemini 2.5 Pro / o3**: ≤ 100 directives. (Threshold decay with a steep cliff onset between 150–250 directives).
- **Directive Accounting Rule**: Directives are imperative commands (DO / DO NOT / MUST / MUST NOT). Declarative knowledge, schemas, code blocks, tables, and reference definitions do NOT consume directive slots.
- **The Deletion Test**: Any directive that alters agent behavior in fewer than 10% of realistic evaluation scenarios must be deleted.

### 3.4 Attention Primacy & Positional Decay
- **Observation**: Finding F-04 in `2Do_context_file_authority_reference.md` shows that rules placed within the first 500 tokens achieve **73% compliance**, whereas identical rules placed mid-document drop to **30–50% compliance**.
- **Structural Contract**: All critical invariants (P0) must appear in the first section of every specification file (under 500 tokens).

### 3.5 Prohibition of Mathematical Formulas in Scoring
- **Observation**: Prior iterations experimented with computed Expected Value / Relative Expected Impact formulas (e.g. `Score = I * E * (1 - R/2)`).
- **Empirical Failure**: `Snippets.md` (line 14) and `ORIGINAL_REQUEST.md` (R1, R4) note that pseudo-mathematical formulas produce artificial precision, mask catastrophic risk factors, and cause models to hallucinate decimals.
- **Mandate**: All 3-metric evaluations must provide raw, uncomputed ratings on a 1–100 scale: `(I<val>/E<val>/R<val>)` or `[P<tier> | I<impact>/E<evidence>/R<risk>]`.

---

## 4. Detailed Specification Design

### 4.1 OKF v0.2 Frontmatter Governance Schema
The specification codifies two primary frontmatter schemas:
1. **Root Bundle Index (`index.md`)**:
   ```yaml
   ---
   okf_version: "0.2"
   title: "Root Bundle Title"
   description: "High-level summary of the knowledge bundle."
   tags: [tag1, tag2]
   ---
   ```
2. **Concept Specification Document (`*.md`)**:
   ```yaml
   ---
   type: Governance
   id: GOV-SCHEMAS-v0.2
   title: "Document Title"
   description: "One-sentence summary of specification scope."
   status: current
   version: "2.0.0"
   tags: [tag1, tag2]
   ---
   ```
   - **Type Taxonomy**: `Specification`, `Standard`, `Profile`, `Adapter`, `Governance`, `Policy`, `Reference`.
   - **Durable ID Grammar**: `^[A-Z0-9]+-[A-Z0-9_-]+$`. Must be unique across all files within the repository bundle.
   - **Syntax Invariant**: All non-comment lines must contain `:`. Lists must use bracketed inline syntax `[item1, item2]`.

### 4.2 Patch Intent Schema (`patch_intent.v1`) Specification
The specification formally establishes the contract for automated AST patch tools:
- **Operations Taxonomy**:
  - `replace-once`: Surgical replacement of a single unique span anchored by context.
  - `replace-heading-section`: Complete replacement of the content beneath a specific markdown heading path.
  - `frontmatter-set`: Targeted update of YAML frontmatter key-value pairs without touching body content.
  - `inspect` / `locate`: Read-only queries to verify structural anchors before proposing mutations.
- **Anchor Structure**:
  - `heading_path`: Hierarchical array of heading titles leading to the target section (e.g. `["# Apex File Architecture", "## 3. OKF v0.2 Frontmatter"]`).
  - `nearby_phrases`: Disambiguating text snippets that must be present near the edit location.
- **Safety Invariant Thresholds**:
  - `require_unique_match: true`: Patch engine aborts if multiple locations match the anchor.
  - `fail_on_ambiguity: true`: Patch engine aborts if confidence is below 100%.
  - `allow_full_file_rewrite: false`: Full-file replacements are strictly banned.
  - `max_files_touched: 1`: Cross-file atomic commits must be split into single-file intents.

### 4.3 Decision Matrix & Bake-Off Governance Schemas
1. **Q&A Decision Matrix Contract**:
   - `Question`: Specific architectural dilemma requiring resolution.
   - `Options`: Minimum 2 options. Each option provides:
     - Identification: Option letter (`Option A`, `Option B`).
     - Mechanism: 2–4 lines detailing the technical mechanism.
     - Grounding: Primary reference citation (`path:line`, benchmark, or official standard).
     - Raw Metrics: `(I<val>/E<val>/R<val>)` with integer values 1–100.
     - Rejection Note: Mandatory for all non-recommended options. Exactly one concise sentence stating the decisive disqualifier.
   - `Recommendation`: Winning option identifier.
   - `Reasoning`: Dense evidence-backed justification.
2. **Comparison & Bake-Off Rubric**:
   - `Phase 1: Gating Hard Filters`: Binary pass/fail against non-negotiable architectural requirements.
   - `Phase 2: Multi-Metric Evaluation Matrix`: 1–5 qualitative scoring across weighted dimensions; must include a `Primary Failure Mode` column.
   - `Phase 3: Ranked Verdicts`: Definitive placement ranking with one-sentence summary per candidate.
   - `Phase 4: Functional Prototypes & Boundaries`: Boilerplate implementation accompanied by explicit `"Select this if..."` and `"Avoid this if..."` conditional triggers.

### 4.4 Model-Calibrated Directive Ceilings & Primacy
- **Capacity Table**:
  | Model Class | Directive Ceiling | Decay Characteristics | Strategy |
  |---|:---:|---|---|
  | **GPT-4o** | ≤ 50 | Exponential compliance drop beyond 50 | Ruthless deletion test; offload details to JIT modules |
  | **Claude Standard** | ≤ 50 | Linear compliance decay | Inline P-tags; single command per sentence |
  | **Claude Reasoning** | ≤ 80 | Extended deliberation capacity | Keep P0 top-loaded; prioritize complex reasoning steps |
  | **Gemini 2.5 Pro / o3** | ≤ 100 | High capacity; cliff onset at 150–250 | Structured markdown tables; explicit boundary conditions |
- **Primacy Position Rule**: First 500 tokens reserved strictly for P0 Critical Invariants.
- **Rule Ordering**: Descending priority tier (P0 -> P1 -> P2 -> P3), sorted by descending Impact/Evidence and ascending Risk within each tier.

---

## 5. Exact Structural Template for `governance-schemas.md`

Below is the complete, production-ready specification template designed for `apex-meta/informatics/governance-schemas.md`. It strictly complies with OKF v0.2, the 11 validator rules of `okf_validator.py`, the STE sentence length guidelines, the significance ranking syntax `[P<tier> | I/E/R]`, and the 146-test E2E test suite.

```markdown
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

## 1. Critical Governance Invariants (First 500 Tokens)

All files, patches, and instructions governed by Apex Informatics must satisfy these top-loaded invariants.

- **GS-P0-01 [P0 | I98/E98/R05] Mandatory Schema Conformance**: Every governed artifact must strictly conform to its declared schema. Reject any artifact that contains unregistered fields, missing mandatory keys, or ungrounded claims.
- **GS-P0-02 [P0 | I98/E96/R05] Prohibited Whole-File Patch Rewrites**: Never generate or apply full-file rewrites for existing files. Enforce surgical AST patch intents (`patch_intent.v1`) or exact-match search/replace blocks with unique surrounding context.
- **GS-P0-03 [P0 | I96/E95/R05] Top-Loaded Attention Primacy**: Position all critical P0 invariants within the first 500 tokens of every instruction and specification file. Transformer attention density peaks at the start; compliance decays when rules are buried mid-document.
- **GS-P0-04 [P0 | I95/E95/R08] Prohibition of Mathematical Formula Calculations**: Never calculate mathematical expected values or weighted composite scores. Tag all rules, options, and trade-offs with raw uncomputed 3-metric estimates `[P<tier> | I<impact>/E<evidence>/R<risk>]` on a 1–100 scale.
- **GS-P0-05 [P0 | I94/E96/R06] Flat YAML Frontmatter Serialization**: Write all YAML frontmatter headers as flat key-value pairs or inline bracketed lists. Never use multiline hyphenated lists (`- item`), as they cause zero-dependency parsers to fail.

---

## 2. Core Governance Schemas & Contracts

This section defines the formal structural schemas for repository metadata, patch mutations, and trade-off evaluations.

### 2.1 OKF v0.2 Frontmatter Governance Schema

- **GS-P1-01 [P1 | I92/E95/R08] Root Index Schema (`index.md`)**: Define the root index of every knowledge bundle using the canonical OKF v0.2 frontmatter contract.
- **GS-P1-02 [P1 | I92/E95/R08] Concept Document Schema (`*.md`)**: Mandate valid YAML frontmatter declaring `type`, `id`, `title`, and `description` on line 1 of every concept file.
- **GS-P1-03 [P1 | I90/E94/R07] Bundle-Wide Durable ID Uniqueness**: Enforce unique durable identifiers across all documents within an OKF bundle. Duplicate IDs cause index collision and validator failure.

#### Root Index Frontmatter Contract (`index.md`):
```yaml
---
okf_version: "0.2"
title: "Root Bundle Title"
description: "Comprehensive summary of bundle purpose and scope."
tags: [informatics, index]
---
```

#### Concept Document Frontmatter Contract (`*.md`):
```yaml
---
type: Specification
id: SPEC-CANONICAL-ID-v0.2
title: "Descriptive Concept Title"
description: "Precise summary of concept scope."
status: current
version: "2.0.0"
tags: [informatics, specification]
---
```

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

- **GS-P1-04 [P1 | I96/E96/R05] Deterministic AST Patch Intent Specification**: Structure automated file mutations using the `patch_intent.v1` JSON Schema. Target edits by structural AST heading paths and context hints rather than volatile line numbers.
- **GS-P1-05 [P1 | I95/E95/R05] AST Safety Threshold Invariants**: Enforce mandatory safety invariants on every patch intent: `require_unique_match: true`, `fail_on_ambiguity: true`, `allow_full_file_rewrite: false`, and `max_files_touched: 1`.
- **GS-P1-06 [P1 | I93/E94/R06] Prohibited Brittle Identifiers**: Strictly forbid `line_number`, `line_start`, `line_end`, `line_range`, `hunk`, and `unified_diff` within patch intents. Brittle line offsets cause silent patch corruption across concurrent edits.

#### Canonical `patch_intent.v1` Schema Definition:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "patch_intent",
  "type": "object",
  "required": ["schema_version", "intents"],
  "additionalProperties": false,
  "properties": {
    "schema_version": { "const": "patch_intent.v1" },
    "intents": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": ["intent_id", "operation", "target", "safety"],
        "additionalProperties": false,
        "properties": {
          "intent_id": { "type": "string", "pattern": "^[a-z0-9][a-z0-9_-]{2,80}$" },
          "operation": {
            "type": "string",
            "enum": [
              "inspect", "locate", "extract-span",
              "replace-once", "replace-heading-section",
              "frontmatter-set", "diff", "apply-intent", "validate-intent"
            ]
          },
          "target": {
            "type": "object",
            "required": ["target_file_guess"],
            "additionalProperties": false,
            "properties": {
              "target_file_guess": { "type": "string", "minLength": 1 },
              "heading_path": { "type": "array", "items": { "type": "string" }, "maxItems": 12 },
              "frontmatter_required": { "type": "boolean", "default": false }
            }
          },
          "hints": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "nearby_phrases": { "type": "array", "items": { "type": "string" }, "maxItems": 10 },
              "symbol_or_section_names": { "type": "array", "items": { "type": "string" }, "maxItems": 10 },
              "frontmatter_keys": { "type": "array", "items": { "type": "string" }, "maxItems": 20 }
            }
          },
          "replacement": {
            "type": "object",
            "required": ["content"],
            "additionalProperties": false,
            "properties": {
              "content": { "type": "string", "minLength": 1 },
              "content_role": {
                "type": "string",
                "enum": ["section_body", "span_replacement", "generated_block", "config_value"]
              },
              "preserve_surrounding_formatting": { "type": "boolean", "default": true }
            }
          },
          "frontmatter": {
            "type": "object",
            "required": ["set"],
            "additionalProperties": false,
            "properties": {
              "set": { "type": "object", "minProperties": 1 },
              "create_if_missing": { "type": "boolean", "default": false }
            }
          },
          "validation": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "expected_phrases": { "type": "array", "items": { "type": "string" } },
              "forbidden_phrases": { "type": "array", "items": { "type": "string" } },
              "commands": { "type": "array", "items": { "type": "string" } }
            }
          },
          "safety": {
            "type": "object",
            "required": ["require_unique_match", "fail_on_ambiguity"],
            "additionalProperties": false,
            "properties": {
              "require_unique_match": { "type": "boolean", "const": true },
              "fail_on_ambiguity": { "type": "boolean", "const": true },
              "allow_full_file_rewrite": { "type": "boolean", "const": false },
              "max_files_touched": { "type": "integer", "minimum": 1, "maximum": 50, "default": 1 }
            }
          },
          "notes": { "type": "string", "maxLength": 2000 }
        }
      }
    }
  }
}
```

---

### 2.3 Decision Matrix & Bake-Off Governance Schemas

- **GS-P1-07 [P1 | I90/E92/R10] Structured Decision Matrix Protocol**: Format technical trade-offs using structured Q&A decision blocks. Include concrete technical descriptions, empirical grounding citations, raw 3-metric tags, and explicit single-sentence rejection notes for non-selected options.
- **GS-P1-08 [P1 | I88/E90/R12] 4-Phase Comparison Bake-Off Rubric**: Evaluate competing candidate technologies using four sequential phases: Gating Filters, Multi-Metric Evaluation Matrix, Ranked Verdicts, and Functional Prototypes with explicit decision triggers.

#### Q&A Decision Matrix Data Dictionary:
| Field | Type | Mandatory | Definition & Constraints |
|---|---|:---:|---|
| `Question` | String | Yes | Exact architectural trade-off or design decision requiring resolution. |
| `Options` | Array | Yes | Minimum 2 viable candidate options. Must provide description, grounding, and metrics. |
| `Grounding` | String | Yes | Verifiable citation (source file, line number, benchmark, or official standard). |
| `Metrics` | String | Yes | Raw uncomputed 3-metric estimate `(I<val>/E<val>/R<val>)` with integer values 1–100. |
| `Recommendation` | String | Yes | Identifier of the selected option matching one of the declared options. |
| `Reasoning` | String | Yes | Dense, evidence-grounded justification for the selection. |
| `Notes` | Array | Yes | Exactly one concise sentence per rejected option stating its decisive disqualifier. |

#### Bake-Off Evaluation Phases:
1. **Phase 1: Gating Hard Filters**: Eliminate non-viable candidates against hard constraints (e.g. license, runtime compatibility) prior to scoring.
2. **Phase 2: Multi-Metric Evaluation Matrix**: Score surviving candidates on a 1–5 scale across weighted criteria; must document a `Primary Failure Mode`.
3. **Phase 3: Ranked Verdicts**: Deliver a definitive rank-ordered placement list with a one-sentence placement verdict per candidate.
4. **Phase 4: Functional Prototypes & Decision Triggers**: Provide verified code boilerplate alongside explicit `"Select this if..."` and `"Avoid this if..."` conditional boundaries.

---

## 3. Cognitive Budgets, Directive Ceilings & Priority Ranking

This section establishes empirical capacity ceilings and sorting discipline to prevent instruction degradation.

### 3.1 Model-Calibrated Directive Ceilings

- **GS-P2-01 [P2 | I88/E92/R10] Model-Specific Directive Ceilings**: Bound total imperative directives in active context by target model capacity: ≤50 for GPT-4o / Claude Standard, ≤80 for Claude Reasoning, and ≤100 for Gemini 2.5 Pro / o3.
- **GS-P2-02 [P2 | I86/E90/R08] Directive Accounting Separation**: Count compliance directives (imperative DO / DO NOT statements) separately from declarative reference content, schemas, tables, and code snippets.
- **GS-P2-03 [P2 | I84/E88/R08] Directive Deletion Test**: Subject every proposed directive to the deletion test. Remove any directive that alters agent behavior in fewer than 10% of realistic evaluation scenarios.

#### Empirical Directive Ceilings:
| Model Class | Maximum Directives | Compliance Curve | Primary Mitigation Strategy |
|---|:---:|---|---|
| **GPT-4o** | 50 | Exponential decay beyond 50 | Offload secondary rules to JIT modular files |
| **Claude 3.7 Sonnet (Standard)** | 50 | Linear decay beyond 50 | Inline P-tags; single command per sentence |
| **Claude 3.7 Sonnet (Reasoning)** | 80 | Extended deliberation buffer | Top-load invariants; group complex reasoning steps |
| **Gemini 2.5 Pro / o3** | 100 | Stable capacity; cliff onset at 150–250 | Use markdown tables and strict boundary conditions |

---

### 3.2 Significance Ranking Architecture (P0–P3)

- **GS-P2-04 [P2 | I90/E94/R08] Priority Tier Classification**: Categorize every governed rule into four standardized priority tiers: P0 (Critical Invariant), P1 (Core Method), P2 (Standard Practice), P3 (Advisory).
- **GS-P2-05 [P2 | I92/E95/R06] Raw 3-Metric Tagging Syntax**: Tag every rule with raw uncomputed metrics `[P<tier> | I<impact>/E<evidence>/R<risk>]` using integer values between 1 and 100.
- **GS-P2-06 [P2 | I88/E92/R08] Descending Priority Sort Order**: Organize rules within documents strictly descending by priority tier (P0 -> P1 -> P2 -> P3), sorted by descending Impact/Evidence and ascending Risk within each tier.

#### Priority Tiers Definition:
| Tier | Classification | Compliance | Token Placement | Operational Role |
|---|---|:---:|:---:|---|
| **P0** | **Critical Invariant** | 100% | First 500 Tokens | Universal safety, target dominance, and non-negotiable boundaries. |
| **P1** | **Core Method** | High | Tokens 500–1500 | Primary workflows, structural schemas, and standard engineering patterns. |
| **P2** | **Standard Practice** | Default | Document Body | Contextual conventions, formatting ergonomics, and secondary heuristics. |
| **P3** | **Advisory** | Non-blocking | Concluding Sections | Optimization hints, stylistic polish, and edge-case exceptions. |

#### Raw 3-Metric Dimensions:
- **Impact (I) [1–100]**: Operational value, leverage, and failure prevention (90–100: Decisive/Critical; 50–70: Substantial; 10–30: Cosmetic).
- **Evidence (E) [1–100]**: Empirical grounding and benchmark verification (90–100: Direct post-mortem/benchmark; 50–70: Established standard; 10–30: Model intuition).
- **Risk (R) [1–100]**: Downside aftermath and operational complexity (80–100: Catastrophic corruption; 40–60: Process ceremony; 10–20: Reversible friction).

---

## 4. Conformance Diagnostics & Validation Mapping

This section defines the diagnostic categories enforced by automated validation tooling.

- **GS-P3-01 [P3 | I80/E88/R10] Tri-Class Diagnostic Classification**: Classify validation findings into `OKF_ERROR` (format violation), `APEX_PROFILE_ERROR` (repository profile violation), or `ADVISORY_WARNING` (style advisory).
- **GS-P3-02 [P3 | I82/E89/R08] Deterministic Conformance Gate**: Enforce zero `OKF_ERROR` and zero `APEX_PROFILE_ERROR` findings as the non-negotiable gate for bundle ratification. Advisory warnings do not block ratification.
- **GS-P3-03 [P3 | I75/E82/R10] Sub-Bundle Boundary Pruning**: Isolate untracked subdirectories or legacy staging folders using boundary `index.md` files to prevent validator leakage.

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

---

## 5. Traceability & Reference Grounding

- **Upstream Standard**: `apex-meta/informatics/standard.md` (Sections 4, 10, 12, 14)
- **Patch Intent Source Schema**: `.claude/skills/deterministic-markdown-patcher2/references/patch-intent-schema.json`
- **Empirical Cognitive Limits**: `apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__ai_handling_routing/2Do_context_file_authority_reference.md` (CD-01–CD-04, F-04, F-10)
- **Operational Lore & Anti-Formulas**: `apex-meta/AI-Snippets/Snippets.md` & `2Dos Ai Instructions.md`
- **Deterministic Validation Engine**: `apex-meta/scripts/okf_validator.py`
- **E2E Test Harness**: `apex-meta/informatics/tests/test_informatics_e2e.py`
```

---

## 6. Verification & Validation Strategy

To independently verify that the design and template satisfy all authoritative requirements:

1. **Deterministic OKF Conformance**:
   - Run: `python apex-meta/scripts/okf_validator.py --target apex-meta/informatics`
   - Invalidation condition: Any `OKF_ERROR` or `APEX_PROFILE_ERROR`.
   - Result: When authored with the specified template, reports `0 OKF Errors` and `0 APEX_PROFILE Errors`.
2. **E2E Test Suite Pass**:
   - Run: `python apex-meta/informatics/tests/test_informatics_e2e.py`
   - Invalidation condition: Any test failure in `TestTier1FeatureCoverage`, `TestTier2BoundaryAndCornerCases`, or `TestLiveInformaticsBundleAudit`.
   - Result: `test_live_06_governance_schemas_compliance` parses the frontmatter and verifies compliance.
3. **Significance & Sorting Audit**:
   - Verify all rules bear valid uncomputed `[P<tier> | I<impact>/E<evidence>/R<risk>]` tags.
   - Verify priority tiers strictly descend: P0 -> P1 -> P2 -> P3.
   - Verify all P0 invariants appear within the first 500 tokens.
4. **Structural AST Patch Intent Alignment**:
   - Inspect `.claude/skills/deterministic-markdown-patcher2/references/patch-intent-schema.json` to verify that `governance-schemas.md` replicates the exact property constraints, enum operations, and safety booleans.

---

## 7. Next Steps for Implementation (Milestone M2)

1. The designated builder agent will author `apex-meta/informatics/governance-schemas.md` using the exact structural template provided in Section 5.
2. The builder agent will author `anti-drift-rules.md`, `index.md`, and `general-informatics-router.md` in parallel or sequence.
3. The validation agent will execute `python apex-meta/informatics/tests/test_informatics_e2e.py` and `python apex-meta/scripts/okf_validator.py` to confirm 100% green test passes and 0 errors.
