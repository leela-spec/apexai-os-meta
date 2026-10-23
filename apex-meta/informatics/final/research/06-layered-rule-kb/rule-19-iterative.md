---
type: Reference
id: V2-LAYERED-KB-RULE-19-ITERATIVE
title: Rule 19 Deep-Dive — <iterative> Semantic Block Decomposition, Value Audit & Compression Options
description: Decomposing <iterative> (from 13-candidate-3A-xml.md) into atomic semantic blocks, evaluating token value against lost-in-context drift and execution complexity routing, formulating tighter alternatives, and linking all internal and external research.
status: current_truth
tags: [layered-kb, rule-19, iterative, semantic-blocks, token-compression, research-ledger]
---

# Rule 19 Deep-Dive: `<iterative>` (`13-candidate-3A-xml.md`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (format siblings: [14-candidate-3B-hybrid.md](../../candidates/14-candidate-3B-hybrid.md), [15-candidate-3C-bullet-hybrid.md](../../candidates/15-candidate-3C-bullet-hybrid.md))
> - **Layer 1 (This File — Rule-Level Semantic Block Audit):** Decomposes `<iterative>` into 4 atomic semantic blocks (`SB-19.1`..`SB-19.4`), audits token value against execution drift, and presents scored compression options.
> - **Layer 2 (Downstream Infrastructure Modules):** [execution-modes.md](../../specs/execution-modes.md) (`EM-10`, `EM-11`), [anti-drift-rules.md](../../specs/anti-drift-rules.md) (`AD-04`).

---

## 1. Original Rule & Atomic Semantic Block Inventory

### 1.1 Current `v1.0-3A` Full Text (`88 BPE block` | `56 BPE inner` | `99 repo tokens` | `398 chars` | `60 words`)

```xml
<iterative when="the task spans multiple modules, needs research, or cannot finish in one pass" ref="execution-modes.md">
Execute a clear single-step task directly. For multi-step work write a short preflight — target, inputs, scope, output, active step — then proceed step by step. For a multi-module project create a file per step. Open ref for the route ladder or MMM decomposition.
</iterative>
```

### 1.2 Atomic Semantic Block Inventory (Bullet List)

Every token in `<iterative>` belongs to one of four distinct semantic blocks (`SB-19.1` through `SB-19.4`), plus the XML gating tag wrapper (`<iterative when="..." ref="...">...</iterative>`, `32 BPE tokens`):

- **`SB-19.1` — Route 0 Direct Execution (`8 BPE tokens` | `42 chars`):** *"Execute a clear single-step task directly."*
- **`SB-19.2` — Route 1 Compact Preflight (`27 BPE tokens` | `117 chars`):** *"For multi-step work write a short preflight — target, inputs, scope, output, active step — then proceed step by step."*
- **`SB-19.3` — Route 2 / MMM File-Producing Loop (`11 BPE tokens` | `50 chars`):** *"For a multi-module project create a file per step."*
- **`SB-19.4` — MMM Route Ladder Escalation Pointer (`10 BPE tokens` | `51 chars`):** *"Open ref for the route ladder or MMM decomposition."*

---

## 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

### 2.1 Chapter `SB-19.1`: Route 0 Direct Execution
> **Current Text (`8 BPE tokens`):** `"Execute a clear single-step task directly."`

- **What It Means & Failure Mode Addressed:** Express bypass for simple assignments: when a task requires only a single clear step, the agent acts immediately without generating preflight documentation or ceremonial overhead.
- **Value & Necessity Critique (`[P1 | I90/E92/R08]` — Anti-Overengineering Invariant):**
  - **Honest High-Reasoning Critique:** Eliminates planning paralysis (`EM-10`). Frontier models frequently spend 300+ tokens generating multi-phase plans for one-line edits or single command invocations.
  - **Where It Has Fat:** Phrasing can be shortened to *"Execute single-step tasks directly"*, saving 2 BPE tokens.
- **Formulation Options:**
  - **Option A (Baseline — `8 BPE tokens`):** *"Execute a clear single-step task directly."* `(I90/E92/R08)`
  - **Option B (Recommended Surgical Compression — `6 BPE tokens`, `−2 BPE`):** *"Execute single-step tasks directly."* `(I92/E92/R07)`
  - **Option C (Aggressive Alternative — `6 BPE tokens`, `−2 BPE`):** *"Execute single-step tasks directly."* `(I92/E92/R07)`

---

### 2.2 Chapter `SB-19.2`: Route 1 Compact Preflight
> **Current Text (`27 BPE tokens`):** `"For multi-step work write a short preflight — target, inputs, scope, output, active step — then proceed step by step."`

- **What It Means & Failure Mode Addressed:** For intermediate multi-step workflows, mandates authoring an in-context preflight summary establishing five core anchors (target, inputs, scope, output, active step) before executing.
- **Value & Necessity Critique (`[P0 | I95/E95/R05]` — Anti-Drift Anchor):**
  - **Why It Earns Its Tokens:** Counteracts compounding multi-step hallucination. Explicitly anchoring the active step and target prevents the model from dropping secondary constraints across successive tool turns (`EM-10`, `AD-04`).
  - **Where It Has Fat:** Can be punctuated cleanly with parentheses instead of em-dashes and fused seamlessly with `SB-19.3`.
- **Formulation Options:**
  - **Option A (Baseline — `27 BPE tokens`):** *"For multi-step work write a short preflight — target, inputs, scope, output, active step — then proceed step by step."* `(I95/E95/R05)`
  - **Option B (Recommended Surgical Compression — `28 BPE tokens`, `+1 BPE`):** *"For multi-step work, write a compact preflight (target, inputs, scope, output, active step) and proceed step by step,"* `(I96/E95/R05)`
  - **Option C (Aggressive Alternative — `28 BPE tokens`, `+1 BPE`):** *"For multi-step work, draft a short preflight (target, inputs, scope, output, active step) and proceed step by step,"* `(I94/E94/R06)`

---

### 2.3 Chapter `SB-19.3`: Route 2 / MMM File-Producing Loop
> **Current Text (`11 BPE tokens`):** `"For a multi-module project create a file per step."`

- **What It Means & Failure Mode Addressed:** For complex multi-module engineering projects, intermediate state must be materialized into discrete files on disk (`step-xx.md`, `analysis.md`) rather than kept solely in volatile conversational context.
- **Value & Necessity Critique (`[P0 | I96/E96/R05]` — Disk-State Persistence):**
  - **Why It Earns Its Tokens:** The core mechanism of Macro-Meso-Micro (MMM) decomposition (`EM-10`). Context windows truncate or compress during long runs; disk files survive context loss and enable independent verification.
  - **Where It Has Fat:** Merges naturally with the preceding preflight sentence as a subordinate clause.
- **Formulation Options:**
  - **Option A (Baseline — `11 BPE tokens`):** *"For a multi-module project create a file per step."* `(I96/E96/R05)`
  - **Option B (Recommended Surgical Compression — `10 BPE tokens`, `−1 BPE`):** *"creating a file per step for multi-module projects."* `(I96/E96/R05)`
  - **Option C (Aggressive Alternative — `10 BPE tokens`, `−1 BPE`):** *"creating a file per step for multi-module projects."* `(I96/E96/R05)`

---

### 2.4 Chapter `SB-19.4`: MMM Route Ladder Escalation Pointer
> **Current Text (`10 BPE tokens`):** `"Open ref for the route ladder or MMM decomposition."`

- **What It Means & Failure Mode Addressed:** Directs the agent to `execution-modes.md` Adapter 5 (`EM-10` §6.3 Route Ladder: Route 0, Route 1, Route 2) when project complexity requires structured decomposition.
- **Value & Necessity Critique (`[P1 | I90/E92/R08]` — Escalation Cue):**
  - **Why It Earns Its Tokens:** Preserved from `RP-08`. Establishes the exact reference to the Macro-Meso-Micro framework without wasting tokens embedding the full ladder in the contract.
  - **Where It Has Fat:** Trimming the word "the" saves 1 BPE token.
- **Formulation Options:**
  - **Option A (Baseline — `10 BPE tokens`):** *"Open ref for the route ladder or MMM decomposition."* `(I90/E92/R08)`
  - **Option B (Recommended Surgical Compression — `9 BPE tokens`, `−1 BPE`):** *"Open ref for route ladder or MMM decomposition."* `(I91/E92/R07)`
  - **Option C (Aggressive Alternative — `9 BPE tokens`, `−1 BPE`):** *"Open ref for route ladder or MMM decomposition."* `(I91/E92/R07)`

---

## 3. Whole-Rule Recomposition Rollup for `<iterative>`

| Rollup Option | Complete `<iterative>` Text | BPE Tokens (`cl100k_base`) | Savings vs. Current `v1.0-3A` (`88 BPE`) |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<iterative when="the task spans multiple modules, needs research, or cannot finish in one pass" ref="execution-modes.md"> Execute a clear single-step task directly. For multi-step work write a short preflight — target, inputs, scope, output, active step — then proceed step by step. For a multi-module project create a file per step. Open ref for the route ladder or MMM decomposition. </iterative>` | **`88`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<iterative when="the task spans multiple modules, needs research, or cannot finish in one pass" ref="execution-modes.md"> Execute single-step tasks directly. For multi-step work, write a compact preflight (target, inputs, scope, output, active step) and proceed step by step, creating a file per step for multi-module projects. Open ref for route ladder or MMM decomposition. </iterative>` | **`85`** | **`−3 BPE` (`−3.4%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<iterative when="the task spans multiple modules, needs research, or cannot finish in one pass" ref="execution-modes.md"> Execute single-step tasks directly. For multi-step work, draft a short preflight (target, inputs, scope, output, active step) and proceed step by step, creating a file per step for multi-module projects. Open ref for route ladder or MMM decomposition. </iterative>` | **`85`** | **`−3 BPE` (`−3.4%`)** |

---

## 4. Complete Bidirectional Research & Provenance Links for `<iterative>`

### 4.1 Internal Project Research Corpus (`ResearchOfFile10` & `Universal AI Instruction System`)
- **Primary Research Packet (`RP-08` — Escalation Cue Recovery & Route Ladder):** [RESULTS-08-deepen-when-mechanics.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-08-deepen-when-mechanics.md)
- **Default Behavior & Complexity Auditing (`RP-09`):** [RESULTS-09-efficiency-audit.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md)
- **Universal Architecture Empirical Deepening:** [A04-complexity-adaptive-workflow/README.md](../../research/01-universal-instruction-research/module-deepening/A04-complexity-adaptive-workflow/README.md)
- **Cross-Packet Synthesis:** [RESULTS-11-synthesis.md](../../research/03-research-of-file-10/RESULTS-11-synthesis.md)
- **Historical Contract Lineage:** [02-informatics-contract-block.md](../../candidates/02-informatics-contract-block.md) (`v0.3`) $\rightarrow$ [07-contract-block-v0.4.md](../../candidates/07-contract-block-v0.4.md) (`v0.4`) $\rightarrow$ [09-contract-block-v0.5.md](../../candidates/09-contract-block-v0.5.md) (`v0.5`) $\rightarrow$ [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (`v1.0-3A`).

### 4.2 External Peer-Reviewed & Benchmark Sources
- **Simon, H. A. (1962):** *The Architecture of Complexity* — Foundational principles of hierarchical decomposition and bounded rationality in multi-stage systems.
- **SpecBench (2026):** Multi-turn agent drift and the demonstrable effectiveness of disk-persisted state tracking.

### 4.3 Canonical Plane 4 Infrastructure Modules & Operational Lore
- **Canonical Execution Modes Owner (`EM-10`, `EM-11`):** [execution-modes.md](../../specs/execution-modes.md)
- **Canonical Anti-Drift Owner (`AD-04`):** [anti-drift-rules.md](../../specs/anti-drift-rules.md)
- **Operational Lore Grounding:** [2Dos Ai Instructions.md](../../../../AI-Snippets/Orga/2Dos%20Ai%20Instructions.md) (*"MMM Execution Loop"*), [Snippets.md](../../../../AI-Snippets/Snippets.md) (*"Route Ladder"*).

---

## 5. Failure Modes & Not-To-Dos (`WP-25`)

- **Never allow complex multi-module tasks to execute purely in conversational memory without writing step files to disk:** Volatile context degrades and causes drift.
- **Never impose multi-step preflight overhead on simple, unambiguous single-step tasks:** Route 0 tasks must be executed directly.
- **Never violate the Upward Invalidation Rule (`EM-11`):** Do not mutate macro architecture or overarching scope simply because low-level micro implementation details shifted.
