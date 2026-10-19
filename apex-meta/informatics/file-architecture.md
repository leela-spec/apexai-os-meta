---
type: Specification
id: SPEC-FILE-ARCH-v0.2
title: Apex File Architecture & Bundle Specification
description: The canonical Apex OS specification governing Five-Plane Information Architecture, OKF v0.2 bundle layouts, flat YAML serialization, current-truth separation, and attention primacy.
tags: [informatics, file-architecture, five-planes, okf-v0.2, current-truth, primacy]
status: current
version: "2.0.0"
---

# Apex File Architecture & Bundle Specification

This specification governs file organization, frontmatter schemas, directory layouts, and information isolation across APEX OS.

## 1. Critical Architecture Invariants

All files authored under Apex Informatics must satisfy these top-loaded invariants.

### FA-01: Strict Current-Truth Separation
[P0 | I95/E95/R08] Live specification and instruction files state active current truth only. Never embed inline changelogs, superseded alternatives, or historical narratives inside live documents. Record historical changes, deprecated options, and audit notes in dedicated external changelogs (`log.md`) or archive directories.

### FA-02: Top-Loaded Attention Primacy
[P0 | I95/E92/R08] Front-load critical P0 invariants near the beginning of every specification and instruction file (aiming for roughly the first ~500 tokens as a practical orientation). Organize subsequent rules in generally descending priority order (P0, then P1, P2, and P3) so primary constraints are read before attention decays, without truncating load-bearing context.

### FA-03: Five-Plane Information Separation
[P0 | I92/E90/R12] Maintain strict separation across the five architecture planes. Never combine system prompts, scoped rules, procedural skills, knowledge bundles, and raw evidence in a single file. Mixed-type monoliths cause severe context clash and prevent targeted just-in-time reloading.

### FA-04: Substance Over Ceremony Exception Authority
[P0 | I98/E98/R05] Substantive realization of the target strictly overrides mechanical metric compliance. Authors and agents possess explicit authority to exceed approximate line, word, or token orientations whenever strict adherence would omit load-bearing context, harm technical accuracy, or compromise system safety.

---

## 2. Five-Plane Information Architecture

Knowledge and instructions across APEX OS decompose into five distinct planes. Each plane serves a dedicated purpose and follows an explicit loading lifecycle.

| Plane | Name | Purpose | Primary Artifacts | Loading Rule | Token Orientation |
|---|---|---|---|---|:---:|
| **1** | **Control Plane** | Universal invariants, security boundaries, and root routing | `AGENTS.md`, `.claude/CLAUDE.md`, root router | Always-on at session start | ~2,000 |
| **2** | **Scoped Instructions Plane** | Path-specific and subsystem-specific constraints | `.claude/rules/*.md`, `.github/instructions/*.md` | Activated on path match | ~1,500 |
| **3** | **Procedures Plane (Skills)** | Reusable, repeatable operational workflows | `.claude/skills/*/SKILL.md` | Task-intent trigger only | ~4,000 |
| **4** | **Knowledge Bundles Plane** | Curated, verified, conceptual system truth | OKF bundles (`index.md` + concept files) | JIT retrieval via index pointer | Scoped |
| **5** | **Evidence & History Plane** | Raw transcripts, audit trails, benchmarks, and logs | `_raw/`, `logs/`, `archive/`, `postmortems/` | Deep forensics and research only | Unbounded |

### Plane Loading Lifecycle
Agents must load context progressively following the plane hierarchy:
1. The agent reads the Control Plane at session initialization.
2. When touching governed file paths, the runtime loads matching Scoped Instructions.
3. When executing specialized operations, the agent triggers task-specific Procedures (Skills).
4. Skills retrieve targeted Knowledge Bundles just in time using relative index links.
5. The agent accesses Evidence & History only during explicit post-mortems or forensic audits.

---

## 3. OKF v0.2 Frontmatter Schemas

Every governed markdown document in an OKF bundle must begin with valid YAML frontmatter enclosed by `---` delimiters.

### FA-04: Flat/Inline YAML Frontmatter Serialization
[P1 | I90/E95/R10] Use flat key-value pairs or inline bracket lists in all frontmatter headers. Every non-comment line must contain a colon separator (`:`). Never use multiline YAML list syntax (`- item`), as it causes custom zero-dependency parsers to fail.

#### Frontmatter Syntax Rules:
- The opening `---` delimiter must appear on line 1.
- Scalar mappings must follow the pattern `key: value` or `key: "quoted value"`.
- Sequence lists must use inline bracket syntax: `tags: [item1, item2]`.
- Mappings must use inline braces: `meta: { key: value }`.

### FA-05: Root Index Specification (`index.md`)
[P1 | I88/E92/R12] Every knowledge bundle must provide a root `index.md`. The root index establishes bundle identity and governs navigation across concept files.

#### Root Index Frontmatter Schema:
```yaml
---
okf_version: "0.2"
title: "Descriptive Bundle Title"
description: "Comprehensive summary of bundle purpose and scope."
---
```

#### Root Index Content Rules:
- Must declare `okf_version: "0.2"`.
- Must provide relative markdown links to all member concept files.
- Must not duplicate substantive body text from concept documents.
- Every relative link `[Text](path.md)` must resolve to an existing file in the bundle directory.

### FA-06: Concept Document Specification (`*.md`)
[P1 | I88/E92/R12] Concept files store curated domain knowledge, specifications, standards, and adapters.

#### Concept Frontmatter Schema:
```yaml
---
type: Specification
id: SPEC-EXAMPLE-001
title: "Concept Document Title"
description: "Precise summary of concept scope."
tags: [informatics, example]
status: current
---
```

#### Concept Field Requirements:
- `type`: Mandatory non-empty string defining document classification (e.g. `Specification`, `Standard`, `Profile`, `Adapter`, `Policy`).
- `id`: Unique durable identifier across the repository bundle.
- `title`: Human-readable document title.
- `description`: Single-sentence summary of document contents.
- `tags`: Inline bracket list of taxonomy tags.
- `status`: Lifecycle state (`current`, `draft`, `deprecated`).

### FA-07: Unique Durable Identifiers
[P1 | I85/E88/R15] Assign an immutable durable ID (`id: ...`) to every governed concept file. Durable IDs provide stable cross-referencing targets even when file names, headings, or section titles change. The validator checks and enforces ID uniqueness across the entire bundle.

---

## 4. Bundle Layout & Directory Topology

An OKF v0.2 knowledge bundle organizes files under a dedicated directory structure.

```text
apex-meta/informatics/
├── index.md                 # Root bundle index and router
├── log.md                   # Dedicated bundle change log
├── standard.md              # Apex Informatics Standard
├── writing-profile.md       # Writing & prose ergonomics
├── file-architecture.md     # File creation & bundle structure
├── execution-modes.md       # Operational task adapters
└── Agent_Setup/             # Isolated sub-bundle
    ├── index.md             # Sub-bundle boundary index
    └── 00-README.md         # Local research package
```

### FA-08: Sub-Bundle Isolation Boundary
[P1 | I85/E90/R15] Subdirectories containing their own `index.md` file form independent sub-bundles. The repository validator automatically stops recursion at sub-bundle boundaries. This pruning isolates legacy onboarding files, experimental prototypes, and untracked drafts from root bundle verification.

### FA-09: Residual Name Eradication
[P1 | I82/E85/R18] When refactoring or deleting system components, eradicate all residual mentions of obsolete names from live specification documents. Lingering references to retired components cause models to hallucinate legacy behaviors and resurrect deleted workflows.

### FA-10: Single-Purpose Topic Files
[P2 | I78/E82/R20] Structure every concept document around a single responsibility. Apply Information Mapping principles: partition content into clearly labeled sections, tables, and bulleted lists. Avoid dense narrative paragraphs that bury actionable rules.

### FA-11: Dedicated Changelog Allocation
[P2 | I75/E80/R18] Record version history and modification milestones exclusively in `log.md`. The validator exempts `log.md` from mandatory concept frontmatter checks. Keeping changelogs in a dedicated file prevents historical clutter from diluting model attention.

---

## 5. Significance & Ranking Architecture

Every governed rule, adapter, and operational constraint carries an explicit priority tier and raw 3-metric tag.

### Priority Tier Hierarchy (P0–P3)
- **P0 — Critical Invariant**: Universal safety boundaries, target dominance, and foundational system rules.
- **P1 — Core Method**: Primary operational patterns, essential structural rules, and standard engineering workflows.
- **P2 — Standard Practice**: Contextual conventions, formatting ergonomics, and secondary heuristics.
- **P3 — Advisory**: Optimization hints, stylistic polish, and edge-case orientations.

### Raw 3-Metric Estimates: `[P<tier> | I<impact>/E<evidence>/R<risk>]`
Rules provide raw uncomputed estimates on a 1–100 scale across three independent dimensions:
- **Impact (I)**: Operational leverage, effectiveness, and prevention of material failure.
- **Evidence (E)**: Empirical grounding, production track record, and multi-source verification.
- **Risk (R)**: Operational complexity, misjudgment potential, and downside aftermath.

---

## 6. Token Orientations & Universal Instruction Parsimony

### FA-12: Plane Token Orientations & Universal Instruction Parsimony
[P2 | I82/E88/R10] Keep persistent instruction surfaces concise to prevent attention dilution:
- **Control Plane**: roughly ~2,000 tokens.
- **Scoped Instructions**: roughly ~1,500 tokens per rule file.
- **Procedures (Skills)**: roughly ~4,000 tokens per skill.
- **Universal Instruction Parsimony**: Aim for roughly ~30–50 active imperative directives maximum per standalone file; decompose larger domains into JIT sub-modules rather than overloading a single file.
