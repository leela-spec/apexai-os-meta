---
type: Standard
title: Apex Informatics Standard & Conformance Profile
description: The canonical Apex OS standard governing knowledge serialization, topic structuring, technical prose, agent instruction scoping, and deterministic validation.
tags: [informatics, standard, okf, information-architecture, progressive-disclosure]
generated: { by: gemini-3.7-flash, at: 2026-09-01T20:26:00Z }
status: current
---

# Apex Informatics Standard

## 1. Purpose, Scope, and Non-Scope

### Purpose
Establish a single, authoritative standard for structuring, authoring, and scoping knowledge and agent instructions across APEX OS. The architecture follows a strict progressive disclosure hierarchy:
```text
small always-on control
  → scoped instructions
    → task-triggered Skills
      → indexed OKF knowledge
        → evidence / raw / history (JIT only)
```

### Scope
- Normative knowledge bundles in declared repository directories.
- Agent instruction surfaces (`AGENTS.md`, `.claude/CLAUDE.md`, `.github/copilot-instructions.md`, `.claude/rules/**`, `.github/instructions/**`).
- Agent Skills procedure entrypoints and supporting reference files.

### Non-Scope
- Archival, generated, historical, and raw transcript corpora.
- Application code, database migrations, and runtime scripts outside declared knowledge bundles.
- External repositories (e.g. Leela) until specifically authorized.

---
## 1.2 Snippet/Summary

### Semantic XML Directive
<operating_rules standard="Apex-Informatics" activation="when_drafting_docs_or_procedures">
  <scope>Apply strictly to knowledge artifacts, technical documentation, and procedures. Adapt naturally for general queries.</scope>
  <rule name="okf_serialization">Add YAML frontmatter (type, title, description) to knowledge files; route via index without text duplication.</rule>
  <rule name="dita_mapping">Use single-purpose topics, visual block chunking, and tables/bullets over dense paragraphs.</rule>
  <rule name="ste_language">Active voice; one command per sentence; max 20 words for procedural steps (code/prose exempt).</rule>
  <rule name="progressive_disclosure">Smallest sufficient context: answer the immediate need before expanding into deep background.</rule>
  <rule name="current_truth">Document active reality only; exclude inline changelogs and superseded rationale.</rule>


## 2. Standards Precedence and Ownership


Authority for informatics is strictly layered:
1. **Upstream OKF v0.2 Specification**: Governs raw serialization format, parseable YAML frontmatter, and bundle root conventions.
2. **Apex Informatics Standard (This Document)**: Governs information architecture, topic boundaries, technical prose profile, agent instruction scoping, and durable IDs.
3. **Repository Deterministic Validator**: Checks conformance deterministically; separates official OKF errors from Apex Profile errors and advisory warnings.
4. **Agent Skills / Scoped Instructions**: Provide task-specific procedures and local adapters that point to, rather than duplicate, this standard.

---

## 3. Five-Plane Information Architecture

Knowledge within APEX OS is organized across five distinct planes:

| Plane | Purpose | Primary Artifacts | Loading Rule |
|---|---|---|---|
| **Control** | Universal invariants, security boundaries, repo routing | `AGENTS.md`, `.claude/CLAUDE.md` | Always-on / Session start |
| **Scoped Instructions** | Path-specific or domain-specific constraints | `.claude/rules/*.md`, `.github/instructions/*.md` | Path or domain trigger only |
| **Procedures (Skills)** | Reusable, repeatable operational workflows | `.claude/skills/*/SKILL.md` | Task-intent trigger only |
| **Knowledge Bundles** | Curated, distilled, verified conceptual truth | OKF bundles (`index.md` + concept files) | JIT reference via index |
| **Evidence & History** | Raw logs, transcripts, research benchmarks, audit trails | `_raw/`, `logs/`, `adoption-project/` | Deep audit/research only |

---

## 4. Knowledge Bundle Structure and OKF Conformance

A declared OKF knowledge bundle MUST conform to OKF v0.2:
1. **Root `index.md`**:
   - MUST begin with parseable YAML frontmatter containing `okf_version: "0.2"`.
   - MUST provide concise routing links to all bundle member concepts.
   - MUST NOT duplicate substantive body text from concept files.
2. **Concept Files**:
   - MUST begin with parseable YAML frontmatter containing `type`, `title`, and `description`.
   - MUST use recognized or locally documented `type` values (e.g. `Reference`, `Standard`, `Policy`, `Research`, `Plan`).
3. **Changelog `log.md`**:
   - MUST maintain chronological record of bundle changes without embedding discarded drafts.

---

## 5. Block and Topic Design

Knowledge files MUST apply Information Mapping and DITA topic principles:
- **Single-Purpose Topics**: Each concept file owns one clear subject or decision boundary.
- **Visual Block Discipline**: Content is partitioned into labeled blocks, tables, and lists rather than dense prose paragraphs.
- **Labeled Tables & Bulleted Contracts**: Structural requirements and input/output contracts MUST use explicit tables or bullet lists.
- **No Mixed-Purpose Blobs**: Instructions, background narratives, and reference facts MUST NOT be intermingled in a single paragraph.

---

## 6. Technical-Language Profile (STE-Derived)

Technical text MUST adhere to the following prose rules:
1. **Procedural Sentences**: SHOULD NOT exceed 20 words per sentence.
2. **Descriptive Sentences**: SHOULD NOT exceed 25 words per sentence.
3. **One Instruction per Sentence**: Multiple imperative commands MUST NOT be combined with commas or "and".
4. **Active Voice & Explicit Agents**: State clearly who or what performs each action.
5. **Normative Semantics**: RFC 2119 / 8174 keywords (`MUST`, `MUST NOT`, `SHOULD`, `MAY`) MUST be used only when defining strict requirements.
6. **Exemptions**: Code blocks, mathematical formulas, URLs, identifiers, literal quotations, and raw historical evidence are exempt from sentence-length checks.

---

## 7. Progressive Disclosure and Context Delivery

Agents MUST operate on the principle of **Smallest Sufficient Context**:
- Entrypoints (`AGENTS.md`, `CLAUDE.md`, `SKILL.md`) MUST remain concise navigation maps.
- Agents MUST read root indexes first, then load only the specific concept or reference section required for the active task.
- Massive reference corpora MUST NOT be loaded into context proactively.

---

## 8. Agent Instruction Scoping

- **Root Surfaces (`AGENTS.md`)**: Restricted to universal cross-agent invariants, critical safety boundaries, and top-level routing pointers.
- **Client Adapters (`.claude/CLAUDE.md`, `.github/copilot-instructions.md`)**: Bridge runtime-specific mechanisms to shared root contracts; MUST NOT maintain duplicate rulebooks.
- **Scoped Rules (`.claude/rules/*.md`)**: Activated only when modifying specific paths.

---

## 9. Procedure and Skill Boundaries

- **Skills Own Procedure, Not Knowledge**: A `SKILL.md` defines the step-by-step workflow for accomplishing a task.
- **Knowledge Lives in Bundles**: Theoretical explanations, domain schemas, and architecture references belong in OKF bundles, referenced by URL/path in `SKILL.md`.
- **Mirror Discipline**: Mirrored skills across `.agents/`, `.cursor/`, `.kiro/`, `.pi/`, and `.windsurf/` must preserve canonical contracts.

---

## 10. Identity: Durable IDs vs Ordinary Labels

- **Durable IDs**: Canonical identifiers (e.g. `Q01`, `A1.1`, `APEX-KB-001`) MUST be unique within their governed scope and remain immutable across revisions.
- **Ordinary Labels**: Informational headings and markdown links MAY evolve as long as durable IDs and explicit citations remain anchored.

---

## 11. Provenance, Current-Truth, and History Handling

- **Current-Truth Separation**: Live files represent current truth only.
- **No In-Line Changelogs**: Do not narrate superseded options, past errors, or "what changed" inside live instruction or standard documents.
- **Historical Allocation**: Past research, incident analysis, and migration notes live in dedicated research/evidence files (e.g. `adoption-project/`, `AI-Snippets/AIFailure/`).

---

## 12. Validation Classes

Deterministic tooling enforces three distinct diagnostic classes:

1. **`OKF`**: Upstream specification violations (missing frontmatter, missing `type`, invalid root `okf_version`).
2. **`APEX_PROFILE`**: Apex-specific profile violations (broken governed index links, duplicate durable IDs in scope, unfrontmattered `.okf.md` files in governed targets).
3. **`ADVISORY`**: Non-blocking stylistic suggestions (sentence length, prose chunk size).

---

## 13. Exceptions

- Unmanaged historical folders (`apex-meta/AI-Snippets/`, `SourceTranscriptionAnalysisPipeline_Research/`, `FEE/`) are exempt from strict OKF validation unless explicitly onboarded by an approved migration wave.
- Temporary scratch scripts and debug files in test fixtures are exempt from frontmatter validation.

---

## 14. Grounded References

- [OKF v0.2 Conformance Rules](../SmallSkills/OKF_Format/conformance-rules.md)
- [Informatics Design Formats Practice Guide](../kb/claude-code-orchestration-design/wiki/summaries/informatics-design-formats-practice-guide.md)
- [Token-Efficient Information Design](../kb/claude-code-orchestration-design/wiki/summaries/token-efficient-information-design.md)
- [Informatics Design Doctrine (Weekly Role)](../../.claude/skills/weekly-orchestrator/references/roles/informatics-design-doctrine.md)

