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
- **GS-02 [P0 | I98/E96/R05] Prohibited Whole-File Patch Rewrites**: Never generate or apply full-file rewrites for existing files. Enforce surgical AST patch intents (`patch_intent.v1`) or exact-match search/replace blocks with unique surrounding context.
- **GS-03 [P0 | I96/E95/R05] Top-Loaded Attention Primacy**: Front-load critical P0 invariants near the beginning of every instruction and specification file (aiming for roughly the first ~500 tokens as a practical orientation) before attention density decays.
- **GS-04 [P0 | I95/E95/R06] Raw 3-Metric Significance Tagging**: Tag governed rules, options, and trade-offs with raw unaggregated 3-metric estimates `[P<tier> | I<impact>/E<evidence>/R<risk>]` on a 1–100 scale, keeping all three dimensions distinct.
- **GS-05 [P0 | I94/E96/R06] Flat YAML Frontmatter Serialization**: Write all YAML frontmatter headers as flat key-value pairs or inline bracketed lists. Never use multiline hyphenated lists (`- item`), as they cause zero-dependency parsers to fail.

---

## 2. Core Governance Schemas & Contracts

This section defines the formal structural schemas for repository metadata, patch mutations, and trade-off evaluations.

### 2.1 OKF v0.2 Frontmatter Governance Schema

- **GS-06 [P1 | I92/E95/R08] Root Index Schema (`index.md`)**: Define the root index of every knowledge bundle using the canonical OKF v0.2 frontmatter contract.
- **GS-07 [P1 | I92/E95/R08] Concept Document Schema (`*.md`)**: Mandate valid YAML frontmatter declaring `type`, `id`, `title`, and `description` on line 1 of every concept file.
- **GS-08 [P1 | I90/E94/R07] Bundle-Wide Durable ID Uniqueness**: Enforce unique, tier-agnostic durable identifiers across all documents within an OKF bundle. Duplicate IDs cause index collision and validator failure.

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

- **GS-09 [P1 | I96/E96/R05] Deterministic AST Patch Intent Specification**: Structure automated file mutations using the `patch_intent.v1` JSON Schema. Target edits by structural AST heading paths and context hints rather than volatile line numbers.
- **GS-10 [P1 | I95/E95/R05] AST Safety Threshold Invariants**: Enforce mandatory safety invariants on every patch intent: `require_unique_match: true`, `fail_on_ambiguity: true`, `allow_full_file_rewrite: false`, and `max_files_touched: 1`.
- **GS-11 [P1 | I93/E94/R06] Prohibited Brittle Identifiers**: Forbid `line_number`, `line_start`, `line_end`, `line_range`, `hunk`, and `unified_diff` within patch intents. Brittle line offsets cause silent patch corruption across concurrent edits.

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

- **GS-12 [P1 | I90/E92/R10] Structured Decision Matrix Protocol**: Format technical trade-offs using structured Q&A decision blocks. Include concrete technical descriptions, empirical grounding examples, raw 3-metric tags, and concise single-sentence rejection notes for non-selected options.
- **GS-13 [P1 | I88/E90/R12] 4-Phase Comparison Bake-Off Rubric**: Evaluate competing candidate technologies using four sequential phases: Gating Filters, Multi-Metric Evaluation Matrix, Ranked Verdicts, and Functional Prototypes with explicit decision triggers.

#### Q&A Decision Matrix Data Dictionary:
| Field | Type | Mandatory | Definition & Constraints |
|---|---|:---:|---|
| `Question` | String | Yes | Exact architectural trade-off or design decision requiring resolution. |
| `Options` | Array | Yes | Minimum 2 viable candidate options. Must provide description, grounding, and metrics. |
| `Grounding` | String | Yes | Concrete practical example, user story, or verifiable source citation. |
| `Metrics` | String | Yes | Raw unaggregated 3-metric estimate `(I<val>/E<val>/R<val>)` with integer values 1–100. |
| `Recommendation` | String | Yes | Identifier of the selected option matching one of the declared options. |
| `Reasoning` | String | Yes | Dense, evidence-grounded justification for the selection. |
| `Notes` | Array | Yes | One concise sentence per rejected option stating its decisive disqualifier. |

#### Bake-Off Evaluation Phases:
1. **Phase 1: Gating Hard Filters**: Eliminate non-viable candidates against hard constraints (e.g. license, runtime compatibility) prior to scoring.
2. **Phase 2: Multi-Metric Evaluation Matrix**: Score surviving candidates on a 1–5 scale across weighted criteria; must document a `Primary Failure Mode`.
3. **Phase 3: Ranked Verdicts**: Deliver a definitive rank-ordered placement list with a one-sentence placement verdict per candidate.
4. **Phase 4: Functional Prototypes & Decision Triggers**: Provide verified code boilerplate alongside explicit `"Select this if..."` and `"Avoid this if..."` conditional boundaries.

---

## 3. Universal Instruction Parsimony & Significance Ranking

This section establishes model-agnostic instruction sizing and sorting discipline to prevent attention dilution.

### 3.1 Universal Instruction Parsimony

- **GS-14 [P2 | I88/E92/R08] Universal Instruction Parsimony**: Keep active imperative directives per standalone file concise (aiming for roughly ~30–50 directives maximum per file) and offload domain-specific procedures into conditional JIT modules before a single file becomes an overloaded rule-wall.
- **GS-15 [P2 | I86/E90/R08] Directive Accounting Separation**: Count compliance directives (imperative DO / DO NOT statements) separately from declarative reference content, schemas, tables, and code snippets.
- **GS-16 [P2 | I84/E88/R08] No Default-Behavior Rules**: Codify only rules that prevent recurring failure modes or define non-obvious repository conventions; omit generic advice that models follow by default.

---

### 3.2 Significance Ranking Architecture (P0–P3)

- **GS-17 [P2 | I90/E94/R08] Priority Tier Classification**: Categorize governed rules into four standardized priority tiers: P0 (Critical Invariant), P1 (Core Method), P2 (Standard Practice), P3 (Advisory).
- **GS-18 [P2 | I92/E95/R06] Raw 3-Metric Tagging Syntax**: Tag governed rules with raw unaggregated metrics `[P<tier> | I<impact>/E<evidence>/R<risk>]` using integer values between 1 and 100.
- **GS-19 [P2 | I88/E92/R08] Descending Priority Sort Order**: Organize rules in descending order of significance (`P0 → P1 → P2 → P3`), prioritizing highest Impact/Evidence and lowest Risk within each functional section.

#### Priority Tiers Orientation:
| Tier | Classification | Compliance Orientation | Positional Placement | Operational Role |
|---|---|:---:|:---:|---|
| **P0** | **Critical Invariant** | Foundational (Substance Over Ceremony governs) | ~First 500 Tokens | Universal safety, target dominance, and core boundaries. |
| **P1** | **Core Method** | High | Early Body | Primary workflows, structural schemas, and standard engineering patterns. |
| **P2** | **Standard Practice** | Default | Mid Body | Contextual conventions, formatting ergonomics, and secondary heuristics. |
| **P3** | **Advisory** | Non-blocking | Concluding Sections | Optimization hints, stylistic polish, and edge-case orientations. |

#### Raw 3-Metric Dimensions:
- **Impact (I) [1–100]**: Operational value, leverage, and failure prevention (90–100: Decisive/Critical; 50–70: Substantial; 10–30: Cosmetic).
- **Evidence (E) [1–100]**: Empirical grounding and benchmark verification (90–100: Direct post-mortem/benchmark; 50–70: Established standard; 10–30: Heuristic).
- **Risk (R) [1–100]**: Downside aftermath and operational complexity (80–100: High corruption risk; 40–60: Process friction; 05–20: Low/reversible friction).

---

## 4. Conformance Diagnostics & Validation Mapping

This section defines the diagnostic categories enforced by automated validation tooling.

- **GS-20 [P3 | I80/E88/R10] Tri-Class Diagnostic Classification**: Classify validation findings into `OKF_ERROR` (format violation), `APEX_PROFILE_ERROR` (repository profile violation), or `ADVISORY_WARNING` (style orientation).
- **GS-21 [P3 | I82/E89/R08] Deterministic Conformance Gate**: Enforce zero `OKF_ERROR` and zero `APEX_PROFILE_ERROR` findings as the gate for bundle ratification. Advisory warnings do not block ratification.
- **GS-22 [P3 | I75/E82/R10] Sub-Bundle Boundary Pruning**: Isolate untracked subdirectories or staging folders using boundary `index.md` files to prevent validator leakage.

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
| **`ADVISORY_WARNING`** | `STE-SENTENCE-LENGTH` | Body prose | Prose sentence exceeds ~30 words (exempting tables, lists, and code). |

---

## 5. Traceability & Reference Grounding

- **Upstream Standard**: [Apex Informatics Standard](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/standard.md) (Sections 4, 10, 12, 14)
- **Patch Intent Source Schema**: [patch-intent-schema.json](file:///c:/GitDev/apexai-os-meta/.claude/skills/deterministic-markdown-patcher2/references/patch-intent-schema.json)
- **Operational Lore**: [Snippets.md](file:///c:/GitDev/apexai-os-meta/apex-meta/AI-Snippets/Snippets.md) & [2Dos Ai Instructions.md](file:///c:/GitDev/apexai-os-meta/apex-meta/AI-Snippets/Orga/2Dos%20Ai%20Instructions.md)
- **Deterministic Validation Engine**: [okf_validator.py](file:///c:/GitDev/apexai-os-meta/apex-meta/scripts/okf_validator.py)
