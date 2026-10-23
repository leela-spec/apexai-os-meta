---
type: Reference
id: V2-LAYERED-KB-RULE-20-SCHEMAS
title: Rule 20 Deep-Dive — <schemas> Semantic Block Decomposition, Value Audit & Compression Options
description: Decomposing <schemas> (from 13-candidate-3A-xml.md) into atomic semantic blocks, evaluating token value against volatile line numbers and schema drift, formulating tighter alternatives, and linking all internal and external research.
status: current_truth
tags: [layered-kb, rule-20, schemas, semantic-blocks, token-compression, research-ledger]
---

# Rule 20 Deep-Dive: `<schemas>` (`13-candidate-3A-xml.md`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (format siblings: [14-candidate-3B-hybrid.md](../../candidates/14-candidate-3B-hybrid.md), [15-candidate-3C-bullet-hybrid.md](../../candidates/15-candidate-3C-bullet-hybrid.md))
> - **Layer 1 (This File — Rule-Level Semantic Block Audit):** Decomposes `<schemas>` into 4 atomic semantic blocks (`SB-20.1`..`SB-20.4`), audits token value against schema drift and brittle patch targeting, and presents scored compression options.
> - **Layer 2 (Downstream Infrastructure Modules):** [governance-schemas.md](../../../governance-schemas.md) (`GS-01`, `GS-09`, `GS-10`, `GS-11`).

---

## 1. Original Rule & Atomic Semantic Block Inventory

### 1.1 Current `v1.0-3A` Full Text (`64 BPE block` | `34 BPE inner` | `73 repo tokens` | `292 chars` | `40 words`)

```xml
<schemas when="emitting a patch intent, or validating bundle or schema conformance" ref="governance-schemas.md">
Satisfy the declared schema exactly. Never invent fields. Target edits by heading path and surrounding text, never line number. Open ref for exact JSON or YAML schemas.
</schemas>
```

### 1.2 Atomic Semantic Block Inventory (Bullet List)

Every token in `<schemas>` belongs to one of four distinct semantic blocks (`SB-20.1` through `SB-20.4`), plus the XML gating tag wrapper (`<schemas when="..." ref="...">...</schemas>`, `30 BPE tokens`):

- **`SB-20.1` — Mandatory Schema Conformance (`8 BPE tokens` | `36 chars`):** *"Satisfy the declared schema exactly."*
- **`SB-20.2` — Closed Object Invariant (`4 BPE tokens` | `20 chars`):** *"Never invent fields."*
- **`SB-20.3` — Prohibited Line-Number Target Locators (`13 BPE tokens` | `69 chars`):** *"Target edits by heading path and surrounding text, never line number."*
- **`SB-20.4` — Schema Escalation Pointer (`9 BPE tokens` | `40 chars`):** *"Open ref for exact JSON or YAML schemas."*

---

## 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

### 2.1 Chapter `SB-20.1`: Mandatory Schema Conformance
> **Current Text (`8 BPE tokens`):** `"Satisfy the declared schema exactly."`

- **What It Means & Failure Mode Addressed:** Demands strict, literal conformance to declared data schemas (`GS-01`). JSON, YAML, and patch payloads must satisfy all required type signatures and validation rules.
- **Value & Necessity Critique (`[P0 | I98/E98/R04]` — Data Integrity Core):**
  - **Honest High-Reasoning Critique:** Without strict schema adherence, autonomous agents frequently emit approximate JSON payloads that fail automated downstream parsers, causing pipeline crashes.
  - **Where It Has Fat:** Phrasing can be converted to an active verb clause (*"Conform to declared schemas exactly;"*) to link smoothly with `SB-20.2`.
- **Formulation Options:**
  - **Option A (Baseline — `8 BPE tokens`):** *"Satisfy the declared schema exactly."* `(I98/E98/R04)`
  - **Option B (Recommended Surgical Compression — `7 BPE tokens`, `−1 BPE`):** *"Conform to declared schemas exactly;"* `(I98/E98/R04)`
  - **Option C (Aggressive Alternative — `6 BPE tokens`, `−2 BPE`):** *"Satisfy declared schemas exactly"* `(I96/E96/R05)`

---

### 2.2 Chapter `SB-20.2`: Closed Object Invariant
> **Current Text (`4 BPE tokens`):** `"Never invent fields."`

- **What It Means & Failure Mode Addressed:** Explicitly bans hallucinating or inventing undeclared fields in structured payloads (`additionalProperties: false` semantics in `GS-01`, `GS-10`).
- **Value & Necessity Critique (`[P0 | I98/E98/R04]` — Schema Pollution Shield):**
  - **Why It Earns Its Tokens:** Frontier models love adding speculative fields (e.g. `"comment"`, `"notes"`, `"metadata"`, `"author"`) that are not defined in the specification, causing strict schema validators to reject the payload.
  - **Where It Has Fat:** At 4 BPE tokens, this imperative is maximally dense and unequivocal.
- **Formulation Options:**
  - **Option A (Baseline — `4 BPE tokens`):** *"Never invent fields."* `(I98/E98/R04)`
  - **Option B (Recommended Surgical Compression — `4 BPE tokens`, `+0 BPE`):** *"never invent fields."* `(I98/E98/R04)`
  - **Option C (Aggressive Alternative — `5 BPE tokens`, `+1 BPE`):** *"with zero invented fields."* `(I96/E96/R05)`

---

### 2.3 Chapter `SB-20.3`: Prohibited Line-Number Target Locators
> **Current Text (`13 BPE tokens`):** `"Target edits by heading path and surrounding text, never line number."`

- **What It Means & Failure Mode Addressed:** Prohibits using volatile line numbers as anchors in patch intents; mandates identifying target locations by semantic heading hierarchy and surrounding context lines (`GS-09`, `GS-11`).
- **Value & Necessity Critique (`[P0 | I98/E96/R04]` — Mutation Stability Invariant):**
  - **Why It Earns Its Tokens:** Line numbers drift the instant any preceding edit occurs in a file. Patching by line number leads to catastrophic misapplication where edits corrupt neighboring functions. Semantic heading and context matching guarantees idempotent, drift-resistant application.
  - **Where It Has Fat:** Phrasing can be clarified with *"Locate patch targets by heading path and surrounding context, never line numbers"* (+2 BPE for enhanced operational precision).
- **Formulation Options:**
  - **Option A (Baseline — `13 BPE tokens`):** *"Target edits by heading path and surrounding text, never line number."* `(I98/E96/R04)`
  - **Option B (Recommended Surgical Compression — `15 BPE tokens`, `+2 BPE`):** *"Locate patch targets by heading path and surrounding context, never line numbers."* `(I98/E97/R03)`
  - **Option C (Aggressive Alternative — `12 BPE tokens`, `−1 BPE`):** *"Target edits via heading path and context, never line numbers."* `(I95/E95/R06)`

---

### 2.4 Chapter `SB-20.4`: Schema Escalation Pointer
> **Current Text (`9 BPE tokens`):** `"Open ref for exact JSON or YAML schemas."`

- **What It Means & Failure Mode Addressed:** Escalation pointer instructing the agent to consult `governance-schemas.md` when exact schema definitions, patch intent specifications, or validation formats are needed.
- **Value & Necessity Critique (`[P1 | I90/E92/R08]` — Escalation Cue):**
  - **Why It Earns Its Tokens:** Preserved from `RP-08`. Keeps the contract lean while providing direct access to formal JSON/YAML schemas JIT.
  - **Where It Has Fat:** At 9 BPE tokens, this cue is concise and functional.
- **Formulation Options:**
  - **Option A (Baseline — `9 BPE tokens`):** *"Open ref for exact JSON or YAML schemas."* `(I90/E92/R08)`
  - **Option B (Recommended Surgical Compression — `9 BPE tokens`, `+0 BPE`):** *"Open ref for exact JSON or YAML schemas."* `(I90/E92/R08)`
  - **Option C (Aggressive Alternative — `9 BPE tokens`, `+0 BPE`):** *"Open ref for exact JSON or YAML schemas."* `(I90/E92/R08)`

---

## 3. Whole-Rule Recomposition Rollup for `<schemas>`

| Rollup Option | Complete `<schemas>` Text | BPE Tokens (`cl100k_base`) | Savings vs. Current `v1.0-3A` (`64 BPE`) |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<schemas when="emitting a patch intent, or validating bundle or schema conformance" ref="governance-schemas.md"> Satisfy the declared schema exactly. Never invent fields. Target edits by heading path and surrounding text, never line number. Open ref for exact JSON or YAML schemas. </schemas>` | **`64`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<schemas when="emitting a patch intent, or validating bundle or schema conformance" ref="governance-schemas.md"> Conform to declared schemas exactly; never invent fields. Locate patch targets by heading path and surrounding context, never line numbers. Open ref for exact JSON or YAML schemas. </schemas>` | **`64`** | **`+0 BPE` (`0.0%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<schemas when="emitting a patch intent, or validating bundle or schema conformance" ref="governance-schemas.md"> Satisfy declared schemas exactly with zero invented fields. Target edits via heading path and context, never line numbers. Open ref for exact JSON or YAML schemas. </schemas>` | **`62`** | **`−2 BPE` (`−3.1%`)** |

---

## 4. Complete Bidirectional Research & Provenance Links for `<schemas>`

### 4.1 Internal Project Research Corpus (`ResearchOfFile10` & `Universal AI Instruction System`)
- **Primary Research Packet (`RP-08` — Escalation Cue Recovery & Schema Pointers):** [RESULTS-08-deepen-when-mechanics.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-08-deepen-when-mechanics.md)
- **Schema Efficiency & Closed Properties (`RP-09`):** [RESULTS-09-efficiency-audit.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md)
- **Universal Architecture Empirical Deepening:** [A08-evidence-integrity-uncertainty-calibration/README.md](../../research/01-universal-instruction-research/module-deepening/A08-evidence-integrity-uncertainty-calibration/README.md)
- **Cross-Packet Synthesis:** [RESULTS-11-synthesis.md](../../research/03-research-of-file-10/RESULTS-11-synthesis.md)
- **Historical Contract Lineage:** [02-informatics-contract-block.md](../../candidates/02-informatics-contract-block.md) (`v0.3`) $\rightarrow$ [07-contract-block-v0.4.md](../../candidates/07-contract-block-v0.4.md) (`v0.4`) $\rightarrow$ [09-contract-block-v0.5.md](../../candidates/09-contract-block-v0.5.md) (`v0.5`) $\rightarrow$ [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (`v1.0-3A`).

### 4.2 External Peer-Reviewed & Benchmark Sources
- **JSON Schema Draft 2020-12:** Strict specification conformance, closed schemas (`unevaluatedProperties: false`), and rigorous typing constraints.
- **AST-Based Source Transformation Benchmarks:** Demonstrating that line-number targeted patches experience high failure rates in automated pipelines due to offset shifts.

### 4.3 Canonical Plane 4 Infrastructure Modules & Operational Lore
- **Canonical Governance Schemas Owner (`GS-01`, `GS-09`, `GS-10`, `GS-11`):** [governance-schemas.md](../../../governance-schemas.md)
- **Operational Lore Grounding:** [2Dos Ai Instructions.md](../../../../AI-Snippets/Orga/2Dos%20Ai%20Instructions.md) (*"Prohibit line numbers in patch intents"*), [Snippets.md](../../../../AI-Snippets/Snippets.md) (*"Mandatory Schema Conformance"*).

---

## 5. Failure Modes & Not-To-Dos (`WP-25`)

- **Never allow line numbers (`line_number`, `line_start`, `line_end`) in patch intents:** Always target edits by heading path and surrounding context.
- **Never emit JSON or YAML payloads with undeclared, hallucinated fields:** Strictly enforce closed object schemas.
- **Never bypass schema validation when generating machine-readable governance artifacts:** Maintain 100% syntactic conformance.
