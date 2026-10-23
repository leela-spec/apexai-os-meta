---
type: Reference
id: V2-LAYERED-KB-RULE-16-AUTHORING
title: Rule 16 Deep-Dive — <authoring> Semantic Block Decomposition, Value Audit & Compression Options
description: Decomposing <authoring> (from 13-candidate-3A-xml.md) into atomic semantic blocks, evaluating token value against frontmatter syntax errors and significance tagging discipline, formulating tighter alternatives, and linking all internal and external research.
status: current_truth
tags: [layered-kb, rule-16, authoring, semantic-blocks, token-compression, research-ledger]
---

# Rule 16 Deep-Dive: `<authoring>` (`13-candidate-3A-xml.md`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (format siblings: [14-candidate-3B-hybrid.md](../../candidates/14-candidate-3B-hybrid.md), [15-candidate-3C-bullet-hybrid.md](../../candidates/15-candidate-3C-bullet-hybrid.md))
> - **Layer 1 (This File — Rule-Level Semantic Block Audit):** Decomposes `<authoring>` into 6 atomic semantic blocks (`SB-16.1`..`SB-16.6`), audits token value, and presents scored compression options.
> - **Layer 2 (Downstream Infrastructure Modules):** [file-architecture.md](../../specs/file-architecture.md) (`FA-13`, `FA-06`, `FA-02`, `FA-10`), [writing-profile.md](../../specs/writing-profile.md) (`WP-06`, `WP-07`, `WP-10`, `WP-19`, `WP-24`, `WP-25`), [governance-schemas.md](../../specs/governance-schemas.md) (`GS-03`, `GS-04`, `GS-14`..`GS-17`), [index.md](../../index.md).

---

## 1. Original Rule & Atomic Semantic Block Inventory

### 1.1 Current `v1.0-3A` Full Text (`123 BPE block` | `97 BPE inner` | `135 repo tokens` | `542 chars` | `79 words`)

```xml
<authoring when="creating, editing or validating a governed knowledge or specification file" ref="index.md">
Flat YAML frontmatter: every line has a colon, lists use inline brackets, never multiline dashes. Concept files declare type, id, title, description, status. Front-load critical rules; close on the failure-mode guard. Tag governed rules [P0-P3 | I/E/R] 1-100, never combined. One responsibility per file. Link every file you list. Do not impose this on chat, code or logs. Open ref for tier definitions or bundle layout.
</authoring>
```

### 1.2 Atomic Semantic Block Inventory (Bullet List)

Every token in `<authoring>` belongs to one of six distinct semantic blocks (`SB-16.1` through `SB-16.6`), plus the XML gating tag wrapper (`<authoring when="..." ref="...">...</authoring>`, `26 BPE tokens`):

- **`SB-16.1` — Flat YAML Frontmatter Syntax (`20 BPE tokens` | `97 chars`):** *"Flat YAML frontmatter: every line has a colon, lists use inline brackets, never multiline dashes."*
- **`SB-16.2` — Mandatory OKF Concept Fields (`13 BPE tokens` | `59 chars`):** *"Concept files declare type, id, title, description, status."*
- **`SB-16.3` — Primacy & Recency Ordering (`12 BPE tokens` | `59 chars`):** *"Front-load critical rules; close on the failure-mode guard."*
- **`SB-16.4` — Raw 3-Metric Significance Tagging (`21 BPE tokens` | `57 chars`):** *"Tag governed rules [P0-P3 | I/E/R] 1-100, never combined."*
- **`SB-16.5` — Information Mapping & Link Integrity (`11 BPE tokens` | `54 chars`):** *"One responsibility per file. Link every file you list."*
- **`SB-16.6` — Governance Scope Pin & Escalation Cue (`20 BPE tokens` | `89 chars`):** *"Do not impose this on chat, code or logs. Open ref for tier definitions or bundle layout."*

---

## 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

### 2.1 Chapter `SB-16.1`: Flat YAML Frontmatter Syntax
> **Current Text (`20 BPE tokens`):** `"Flat YAML frontmatter: every line has a colon, lists use inline brackets, never multiline dashes."`

- **What It Means & Failure Mode Addressed:** Strict syntax constraint for metadata: forbids multiline `- item` lists; requires inline bracket sequences (e.g. `tags: [a, b]`).
- **Value & Necessity Critique (`[P0 | I96/E98/R04]` — Non-Default Parser Gate):**
  - **Honest High-Reasoning Critique:** Frontier LLMs naturally default to standard YAML with indented multiline dash lists. However, zero-dependency lightweight validation tooling (`okf_validator.py`) relies on deterministic single-line regex parsing. Multiline lists break regex key extractors and crash downstream automated ingest.
  - **Where It Has Fat:** Phrasing can be tightened from *"every line has a colon, lists use inline brackets, never multiline dashes"* to *"colons on every line, inline bracket lists, no multiline dashes"*, saving 1 BPE token without losing syntactic precision.
- **Formulation Options:**
  - **Option A (Baseline — `20 BPE tokens`):** *"Flat YAML frontmatter: every line has a colon, lists use inline brackets, never multiline dashes."* `(I96/E98/R04)`
  - **Option B (Recommended Surgical Compression — `19 BPE tokens`, `−1 BPE`):** *"Flat YAML frontmatter: colons on every line, inline bracket lists, no multiline dashes."* `(I96/E98/R04)`
  - **Option C (Aggressive Alternative — `14 BPE tokens`, `−6 BPE`):** *"Flat YAML frontmatter: inline brackets for lists, no multiline dashes."* `(I92/E94/R08)`

---

### 2.2 Chapter `SB-16.2`: Mandatory OKF Concept Fields
> **Current Text (`13 BPE tokens`):** `"Concept files declare type, id, title, description, status."`

- **What It Means & Failure Mode Addressed:** Dictates the five mandatory frontmatter fields required for every governed concept document under Open Knowledge Format (OKF v0.2).
- **Value & Necessity Critique (`[P0 | I95/E98/R04]` — Schema Integrity):**
  - **Why It Earns Its Tokens:** Knowledge bundles require stable machine indexing. Omission of `id` or `type` causes validation failures in `okf_validator.py` and breaks graph cross-referencing.
  - **Where It Has Fat:** At 13 BPE tokens, this clause is already compact and lists all five necessary schema attributes.
- **Formulation Options:**
  - **Option A (Baseline — `13 BPE tokens`):** *"Concept files declare type, id, title, description, status."* `(I95/E98/R04)`
  - **Option B (Recommended Surgical Compression — `13 BPE tokens`, `+0 BPE`):** *"Concept files declare type, id, title, description, status."* `(I95/E98/R04)`
  - **Option C (Aggressive Alternative — `11 BPE tokens`, `−2 BPE`):** *"Declare type, id, title, description, status."* `(I92/E95/R06)`

---

### 2.3 Chapter `SB-16.3`: Primacy & Recency Ordering
> **Current Text (`12 BPE tokens`):** `"Front-load critical rules; close on the failure-mode guard."`

- **What It Means & Failure Mode Addressed:** Structures documents so that P0 invariants appear within the first ~500 tokens (primacy) and negative constraints terminate the file (recency).
- **Value & Necessity Critique (`[P1 | I90/E92/R08]` — Attention Ergonomics):**
  - **Why It Earns Its Tokens:** Counteracts transformer "lost-in-the-middle" degradation. Models process constraints placed at the top and bottom of instruction blocks with significantly higher adherence.
  - **Where It Has Fat:** Phrasing can be sharpened by replacing "critical rules" with "invariants" and "failure-mode guard" with "failure guards", saving 2 BPE tokens.
- **Formulation Options:**
  - **Option A (Baseline — `12 BPE tokens`):** *"Front-load critical rules; close on the failure-mode guard."* `(I90/E92/R08)`
  - **Option B (Recommended Surgical Compression — `10 BPE tokens`, `−2 BPE`):** *"Front-load invariants; close on failure guards."* `(I92/E93/R07)`
  - **Option C (Aggressive Alternative — `10 BPE tokens`, `−2 BPE`):** *"Front-load invariants; close on failure guards."* `(I92/E93/R07)`

---

### 2.4 Chapter `SB-16.4`: Raw 3-Metric Significance Tagging
> **Current Text (`21 BPE tokens`):** `"Tag governed rules [P0-P3 | I/E/R] 1-100, never combined."`

- **What It Means & Failure Mode Addressed:** Mandates tagging every governed rule with a priority tier (`P0`–`P3`) and uncombined raw estimates (1–100) for Impact, Evidence, and Risk.
- **Value & Necessity Critique (`[P0 | I96/E96/R05]` — Ranking Standard):**
  - **Why It Earns Its Tokens:** Banishes synthetic mathematical scoring formulas. Models frequently invent arbitrary weighted-average calculations that convey false precision; requiring raw triplets preserves transparent, empirical judgment.
  - **Where It Has Fat:** Phrasing can be streamlined from *"Tag governed rules [P0-P3 | I/E/R] 1-100, never combined"* to *"Tag rules [P0-P3 | I/E/R] 1-100 uncombined"*, saving 2 BPE tokens.
- **Formulation Options:**
  - **Option A (Baseline — `21 BPE tokens`):** *"Tag governed rules [P0-P3 | I/E/R] 1-100, never combined."* `(I96/E96/R05)`
  - **Option B (Recommended Surgical Compression — `19 BPE tokens`, `−2 BPE`):** *"Tag rules [P0-P3 | I/E/R] 1-100 uncombined."* `(I96/E96/R05)`
  - **Option C (Aggressive Alternative — `19 BPE tokens`, `−2 BPE`):** *"Tag rules [P0-P3 | I/E/R] 1-100 uncombined."* `(I96/E96/R05)`

---

### 2.5 Chapter `SB-16.5`: Information Mapping & Link Integrity
> **Current Text (`11 BPE tokens`):** `"One responsibility per file. Link every file you list."`

- **What It Means & Failure Mode Addressed:** Enforces modular, single-responsibility files (`WP-10`) and demands that every mentioned file path has an active, clickable Markdown hyperlink (`WP-24`).
- **Value & Necessity Critique (`[P1 | I90/E92/R08]` — Navigation Integrity):**
  - **Why It Earns Its Tokens:** Agents frequently list filenames without links or lump multiple divergent topics into sprawling monolithic files. Enforcing both constraints guarantees scannable, connected documentation.
  - **Where It Has Fat:** Phrasing can be tightened to *"One purpose per file; link listed files"*, saving 2 BPE tokens.
- **Formulation Options:**
  - **Option A (Baseline — `11 BPE tokens`):** *"One responsibility per file. Link every file you list."* `(I90/E92/R08)`
  - **Option B (Recommended Surgical Compression — `9 BPE tokens`, `−2 BPE`):** *"One purpose per file; link listed files."* `(I90/E92/R08)`
  - **Option C (Aggressive Alternative — `9 BPE tokens`, `−2 BPE`):** *"One purpose per file; link listed files."* `(I90/E92/R08)`

---

### 2.6 Chapter `SB-16.6`: Governance Scope Pin & Escalation Cue
> **Current Text (`20 BPE tokens`):** `"Do not impose this on chat, code or logs. Open ref for tier definitions or bundle layout."`

- **What It Means & Failure Mode Addressed:** Explicitly restricts authoring constraints to formal documentation (excluding code and chat), and points to `index.md` for tier schemas.
- **Value & Necessity Critique (`[P1 | I92/E94/R06]` — Scope Fence & Pointer):**
  - **Why It Earns Its Tokens:** Prevents agents from over-governing casual chat or adding frontmatter blocks to application source code. The escalation pointer ensures full definitions remain accessible JIT without cluttering the contract block.
  - **Where It Has Fat:** Phrasing can be tightened from *"Do not impose this on chat, code or logs"* to *"Exclude chat, code, and logs"*, saving 3 BPE tokens.
- **Formulation Options:**
  - **Option A (Baseline — `20 BPE tokens`):** *"Do not impose this on chat, code or logs. Open ref for tier definitions or bundle layout."* `(I92/E94/R06)`
  - **Option B (Recommended Surgical Compression — `17 BPE tokens`, `−3 BPE`):** *"Exclude chat, code, and logs. Open ref for tier definitions or bundle layout."* `(I93/E94/R05)`
  - **Option C (Aggressive Alternative — `16 BPE tokens`, `−4 BPE`):** *"Exclude chat, code, and logs. Open ref for tier/bundle specs."* `(I90/E92/R08)`

---

## 3. Whole-Rule Recomposition Rollup for `<authoring>`

| Rollup Option | Complete `<authoring>` Text | BPE Tokens (`cl100k_base`) | Savings vs. Current `v1.0-3A` (`123 BPE`) |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<authoring when="creating, editing or validating a governed knowledge or specification file" ref="index.md"> Flat YAML frontmatter: every line has a colon, lists use inline brackets, never multiline dashes. Concept files declare type, id, title, description, status. Front-load critical rules; close on the failure-mode guard. Tag governed rules [P0-P3 | I/E/R] 1-100, never combined. One responsibility per file. Link every file you list. Do not impose this on chat, code or logs. Open ref for tier definitions or bundle layout. </authoring>` | **`123`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<authoring when="creating, editing or validating a governed knowledge or specification file" ref="index.md"> Flat YAML frontmatter: colons on every line, inline bracket lists, no multiline dashes. Concept files declare type, id, title, description, status. Front-load invariants; close on failure guards. Tag rules [P0-P3 | I/E/R] 1-100 uncombined. One purpose per file; link listed files. Exclude chat, code, and logs. Open ref for tier definitions or bundle layout. </authoring>` | **`113`** | **`−10 BPE` (`−8.1%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<authoring when="creating, editing or validating a governed knowledge or specification file" ref="index.md"> Flat YAML frontmatter: inline brackets for lists, no multiline dashes. Declare type, id, title, description, status. Front-load invariants; close on failure guards. Tag rules [P0-P3 | I/E/R] 1-100 uncombined. One purpose per file; link listed files. Exclude chat, code, and logs. Open ref for tier/bundle specs. </authoring>` | **`105`** | **`−18 BPE` (`−14.6%`)** |

---

## 4. Complete Bidirectional Research & Provenance Links for `<authoring>`

### 4.1 Internal Project Research Corpus (`ResearchOfFile10` & `Universal AI Instruction System`)
- **Primary Research Packet (`RP-08` — Gating Attribute Cleanup & Escalation Retention):** [RESULTS-08-deepen-when-mechanics.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-08-deepen-when-mechanics.md)
- **Frontmatter Parsing & Regex Robustness (`RP-09`):** [RESULTS-09-efficiency-audit.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md)
- **Universal Architecture Empirical Deepening:** [C03-conditional-informatics-formal-authoring/README.md](../../research/01-universal-instruction-research/module-deepening/C03-conditional-informatics-formal-authoring/README.md)
- **Cross-Packet Synthesis:** [RESULTS-11-synthesis.md](../../research/03-research-of-file-10/RESULTS-11-synthesis.md)
- **Historical Contract Lineage:** [02-informatics-contract-block.md](../../candidates/02-informatics-contract-block.md) (`v0.3`) $\rightarrow$ [07-contract-block-v0.4.md](../../candidates/07-contract-block-v0.4.md) (`v0.4`) $\rightarrow$ [09-contract-block-v0.5.md](../../candidates/09-contract-block-v0.5.md) (`v0.5`) $\rightarrow$ [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (`v1.0-3A`).

### 4.2 External Peer-Reviewed & Benchmark Sources
- **OASIS DITA Standard Architecture:** Structured technical documentation authoring constraints, information typing, and single-responsibility topics.
- **Horn, R. E. (1998):** *Information Mapping Methodology* — Structured writing principles, visual chunking, and strict modularity.
- **SpecBench (2026):** Specification alignment in coding agents and the necessity of front-loaded invariants in long contexts.

### 4.3 Canonical Plane 4 Infrastructure Modules & Operational Lore
- **Canonical File Architecture Owner (`FA-13`, `FA-06`, `FA-02`, `FA-10`):** [file-architecture.md](../../specs/file-architecture.md)
- **Canonical Writing Profile Owner (`WP-06`, `WP-07`, `WP-10`, `WP-19`, `WP-24`, `WP-25`):** [writing-profile.md](../../specs/writing-profile.md)
- **Canonical Governance Schemas Owner (`GS-03`, `GS-04`, `GS-14`..`GS-17`):** [governance-schemas.md](../../specs/governance-schemas.md)
- **Canonical Root Router:** [index.md](../../index.md)
- **Operational Lore Grounding:** [2Dos Ai Instructions.md](../../../../AI-Snippets/Orga/2Dos%20Ai%20Instructions.md) (*"Flat YAML Serialization"*), [Snippets.md](../../../../AI-Snippets/Snippets.md) (*"Significance Ranking Architecture"*).

---

## 5. Failure Modes & Not-To-Dos (`WP-25`)

- **Never use multiline YAML list syntax (`- item`) in frontmatter:** Breaks zero-dependency single-line regex parsers (`okf_validator.py`).
- **Never compute a composite mathematical formula from raw (I/E/R) estimates:** Retain uncombined triplets to prevent hallucinated pseudo-precision.
- **Never impose OKF frontmatter or governance rules on chat messages, source code, or execution logs:** Keep governance confined to documentation.
- **Never omit the markdown link for any file listed in documentation (`WP-24`):** Ensure all referenced paths resolve to valid files.
