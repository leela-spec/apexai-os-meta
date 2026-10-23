---
type: Reference
id: V2-LAYERED-KB-RULE-05-HOLD-POSITION
title: Rule 05 Deep-Dive — <hold_position> Semantic Block Decomposition, Value Audit & Compression Options
description: Decomposing <hold_position> (from 13-candidate-3A-xml.md) into atomic semantic blocks, evaluating token value, formulating tighter alternatives, and linking all internal and external research.
status: current_truth
tags: [layered-kb, rule-05, hold-position, semantic-blocks, token-compression, research-ledger]
---

# Rule 05 Deep-Dive: `<hold_position>` (`13-candidate-3A-xml.md`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (format siblings: [14-candidate-3B-hybrid.md](../../candidates/14-candidate-3B-hybrid.md), [15-candidate-3C-bullet-hybrid.md](../../candidates/15-candidate-3C-bullet-hybrid.md))
> - **Layer 1 (This File — Rule-Level Semantic Block Audit):** Decomposes `<hold_position>` into 3 atomic semantic blocks (`SB-05.1`..`SB-05.3`), audits token value against RLHF sycophancy and over-correction, and presents scored compression options.
> - **Layer 2 (Downstream Infrastructure Modules):** [anti-drift-rules.md](../../../anti-drift-rules.md) (`AD-22`).

---

## 1. Original Rule & Atomic Semantic Block Inventory

### 1.1 Current `v1.0-3A` Full Text (`55 BPE block` | `48 BPE inner` | `64 repo tokens` | `259 chars` | `41 words`)

```xml
<hold_position>When the operator pushes back without new evidence, do not reverse — restate the evidence or ask what specifically is wrong. Treat a narrow correction as narrow: change what was challenged, leave the rest. State disagreement plainly when evidence supports it.</hold_position>
```

### 1.2 Atomic Semantic Block Inventory (Bullet List)

Every token in `<hold_position>` belongs to one of three distinct semantic blocks (`SB-05.1` through `SB-05.3`), plus the XML tag wrapper (`<hold_position>...</hold_position>`, `7 BPE tokens`):

- **`SB-05.1` — Anti-Sycophancy Pushback Guard (`24 BPE tokens` | `124 chars`):** *"When the operator pushes back without new evidence, do not reverse — restate the evidence or ask what specifically is wrong."*
- **`SB-05.2` — Narrow Correction Containment (`17 BPE tokens` | `80 chars`):** *"Treat a narrow correction as narrow: change what was challenged, leave the rest."*
- **`SB-05.3` — Principled Dissent Invariant (`8 BPE tokens` | `53 chars`):** *"State disagreement plainly when evidence supports it."*

---

## 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

### 2.1 Chapter `SB-05.1`: Anti-Sycophancy Pushback Guard
> **Current Text (`24 BPE tokens`):** `"When the operator pushes back without new evidence, do not reverse — restate the evidence or ask what specifically is wrong."`

- **What It Means & Failure Mode Addressed:** Forbids reflexively capitulating or reversing a correct, verified finding when the operator offers an unevidenced challenge (such as "Are you sure?", "That looks wrong", or a skeptical query). It directs the agent to restate the underlying evidence or ask for specific counter-evidence.
- **Value & Necessity Critique (`[P0 | I98/E96/R04]` — Essential Non-Default Invariant):**
  - **Honest High-Reasoning Critique:** Default RLHF alignment penalizes perceived disagreement, instilling deep sycophancy across frontier models. Research shows LLMs flip from correct to incorrect answers over 60% of the time upon receiving bare pushback. Forcing the agent to anchor in evidence directly preserves technical truth.
  - **Where It Has Fat:** Phrasing can be tightened from 24 down to 18 BPE tokens by condensing the conditional structure into an active command.
- **Formulation Options:**
  - **Option A (Baseline — `24 BPE tokens`):** *"When the operator pushes back without new evidence, do not reverse — restate the evidence or ask what specifically is wrong."* `(I98/E96/R04)`
  - **Option B (Recommended Surgical Compression — `18 BPE tokens`, `−6 BPE`):** *"Do not reverse on pushback without new evidence; restate evidence or clarify the flaw."* `(I98/E96/R04)`
  - **Option C (Aggressive Imperative — `14 BPE tokens`, `−10 BPE`):** *"Never reverse without new evidence; restate evidence or clarify the flaw."* `(I95/E94/R08)`

---

### 2.2 Chapter `SB-05.2`: Narrow Correction Containment
> **Current Text (`17 BPE tokens`):** `"Treat a narrow correction as narrow: change what was challenged, leave the rest."`

- **What It Means & Failure Mode Addressed:** When an operator provides a legitimate but localized correction (e.g., updating a port number, renaming a variable, or tuning a parameter), the agent must confine its change strictly to the challenged element, preserving all surrounding verified work.
- **Value & Necessity Critique (`[P0 | I95/E94/R06]` — Anti-Overcorrection Boundary):**
  - **Why It Earns Its Tokens:** Autonomous agents often exhibit destructive over-reaction: receiving a 1-line feedback item, they discard an entire working 200-line implementation and regenerate it from scratch, frequently re-introducing previously resolved bugs or regressions.
  - **Where It Has Fat:** The tautological phrase *"Treat a narrow correction as narrow"* can be tightened into a direct procedural imperative.
- **Formulation Options:**
  - **Option A (Baseline — `17 BPE tokens`):** *"Treat a narrow correction as narrow: change what was challenged, leave the rest."* `(I95/E94/R06)`
  - **Option B (Recommended Surgical Compression — `15 BPE tokens`, `−2 BPE`):** *"Treat narrow corrections narrowly: update what was challenged and keep the rest."* `(I96/E95/R05)`
  - **Option C (Aggressive Alternative — `9 BPE tokens`, `−8 BPE`):** *"Confine corrections strictly to what was challenged."* `(I92/E92/R10)`

---

### 2.3 Chapter `SB-05.3`: Principled Dissent Invariant
> **Current Text (`8 BPE tokens`):** `"State disagreement plainly when evidence supports it."`

- **What It Means & Failure Mode Addressed:** Grants explicit permission and procedural command to express professional, evidence-backed disagreement rather than feigning consensus or masking discrepancies.
- **Value & Necessity Critique (`[P1 | I90/E92/R06]` — Behavioral Permission Anchor):**
  - **Why It Earns Its Tokens:** Frontier models frequently soften, disguise, or omit their disagreement, producing passive-aggressive text or agreeing verbally while doing the opposite. Stating disagreement plainly when evidence supports it maintains transparent collaboration.
  - **Where It Has Fat:** The sentence is already maximally compact (8 BPE tokens).
- **Formulation Options:**
  - **Option A (Baseline — `8 BPE tokens`):** *"State disagreement plainly when evidence supports it."* `(I90/E92/R06)`
  - **Option B (Recommended Surgical Compression — `8 BPE tokens`, `+0 BPE`):** *"State disagreement plainly when evidence supports it."* `(I90/E92/R06)`
  - **Option C (Aggressive Alternative — `8 BPE tokens`, `+0 BPE`):** *"State disagreement plainly when evidence supports it."* `(I90/E92/R06)`

---

## 3. Whole-Rule Recomposition Rollup for `<hold_position>`

| Rollup Option | Complete `<hold_position>` Text | BPE Tokens (`cl100k_base`) | Savings vs. Current `v1.0-3A` (`55 BPE`) |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<hold_position>When the operator pushes back without new evidence, do not reverse — restate the evidence or ask what specifically is wrong. Treat a narrow correction as narrow: change what was challenged, leave the rest. State disagreement plainly when evidence supports it.</hold_position>` | **`55`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<hold_position>Do not reverse on pushback without new evidence; restate evidence or clarify the flaw. Treat narrow corrections narrowly: update what was challenged and keep the rest. State disagreement plainly when evidence supports it.</hold_position>` | **`47`** | **`−8 BPE` (`−14.5%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<hold_position>Never reverse without new evidence; restate evidence or clarify the flaw. Confine corrections strictly to what was challenged. State disagreement plainly when evidence supports it.</hold_position>` | **`38`** | **`−17 BPE` (`−30.9%`)** |

---

## 4. Complete Bidirectional Research & Provenance Links for `<hold_position>`

### 4.1 Internal Project Research Corpus (`ResearchOfFile10` & `Universal AI Instruction System`)
- **Primary Research Packet (`RP-04` — Pushback Resilience & Sycophancy Suppression):** [RESULTS-04-register-terminology.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-04-register-terminology.md)
- **Secondary Research Packet (`RP-09` — Efficiency Audit & Non-Default Invariants):** [RESULTS-09-efficiency-audit.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md)
- **Universal Architecture Empirical Deepening:** [A05-intent-alignment-clarification-threshold/README.md](../../research/01-universal-instruction-research/module-deepening/A05-intent-alignment-clarification-threshold/README.md)
- **Historical Contract Lineage:** [02-informatics-contract-block.md](../../candidates/02-informatics-contract-block.md) (`v0.3`) $\rightarrow$ [07-contract-block-v0.4.md](../../candidates/07-contract-block-v0.4.md) (`v0.4`) $\rightarrow$ [09-contract-block-v0.5.md](../../candidates/09-contract-block-v0.5.md) (`v0.5`) $\rightarrow$ [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (`v1.0-3A`).

### 4.2 External Peer-Reviewed & Benchmark Sources
- **Wei et al. (2024):** [Simple Synthetic Data Reduces Sycophancy in Large Language Models](https://arxiv.org/abs/2308.03958) — Documents the systematic vulnerability of RLHF models to user agreement biases.
- **Perez et al. (2023):** [Discovering Language Model Behaviors with Model-Written Evaluations](https://arxiv.org/abs/2212.09251) — Quantifies that models prioritize sycophantic alignment over factual correctness when confronted with operator doubt.

### 4.3 Canonical Plane 4 Infrastructure Modules & Operational Lore
- **Canonical Anti-Drift Owner (`AD-22`):** [anti-drift-rules.md](../../../anti-drift-rules.md)
- **Operational Lore Grounding:** [2Dos Ai Instructions.md](../../../../AI-Snippets/Orga/2Dos%20Ai%20Instructions.md) (*"Hold position on unevidenced pushback"*), [Snippets.md](../../../../AI-Snippets/Snippets.md) (*"Anti-Overcorrection"*).

---

## 5. Failure Modes & Not-To-Dos (`WP-25`)

- **Never omit "without new evidence" (`SB-05.1`):** An agent must immediately adapt when the operator supplies new data, error logs, or revised constraints; stubborness without evidence violates basic task alignment.
- **Never discard narrow correction containment (`SB-05.2`):** Treating a minor adjustment as permission to refactor or rewrite the entire codebase is among the most catastrophic failure modes of autonomous coding agents.
- **Never apologize obsequiously before defending a verified position:** State the supporting command or file coordinates directly rather than issuing self-abasing apologies.
