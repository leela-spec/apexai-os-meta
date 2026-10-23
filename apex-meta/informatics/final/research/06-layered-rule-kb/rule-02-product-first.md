---
type: Reference
id: V2-LAYERED-KB-RULE-02-PRODUCT-FIRST
title: Rule 02 Deep-Dive — <product_first> Semantic Block Decomposition, Value Audit & Compression Options
description: Decomposing <product_first> (from 13-candidate-3A-xml.md) into atomic semantic blocks, evaluating token value, formulating tighter alternatives, and linking all internal and external research.
status: current_truth
tags: [layered-kb, rule-02, product-first, semantic-blocks, token-compression, research-ledger]
---

# Rule 02 Deep-Dive: `<product_first>` (`13-candidate-3A-xml.md`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (format siblings: [14-candidate-3B-hybrid.md](../../candidates/14-candidate-3B-hybrid.md), [15-candidate-3C-bullet-hybrid.md](../../candidates/15-candidate-3C-bullet-hybrid.md))
> - **Layer 1 (This File — Rule-Level Semantic Block Audit):** Decomposes `<product_first>` into 3 atomic semantic blocks (`SB-02.1`..`SB-02.3`), audits token value against RLHF biases, and presents scored compression options.
> - **Layer 2 (Downstream Infrastructure Modules):** [anti-drift-rules.md](../../specs/anti-drift-rules.md) (`AD-10`, `AD-09`, `AD-12`), [writing-profile.md](../../specs/writing-profile.md) (`WP-01`).

---

## 1. Original Rule & Atomic Semantic Block Inventory

### 1.1 Current `v1.0-3A` Full Text (`62 BPE block` | `55 BPE inner` | `70 repo tokens` | `280 chars` | `45 words`)

```xml
<product_first>Build the working thing before the machinery around it. Until a real slice of the product runs, fix only what blocks execution, corrupts the product, invalidates the experiment, or risks safety or data loss. Never let a verification script's passing become the definition of done.</product_first>
```

### 1.2 Atomic Semantic Block Inventory (Bullet List)

Every token in `<product_first>` belongs to one of three distinct semantic blocks (`SB-02.1` through `SB-02.3`), plus the XML tag wrapper (`<product_first>...</product_first>`, `7 BPE tokens`):

- **`SB-02.1` — Core Product Invariant (`10 BPE tokens` | `55 chars`):** *"Build the working thing before the machinery around it."*
- **`SB-02.2` — Pre-Execution Blocker Whitelist (`32 BPE tokens` | `151 chars`):** *"Until a real slice of the product runs, fix only what blocks execution, corrupts the product, invalidates the experiment, or risks safety or data loss."*
- **`SB-02.3` — Verification Script != DoD Guard (`13 BPE tokens` | `72 chars`):** *"Never let a verification script's passing become the definition of done."*

---

## 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

### 2.1 Chapter `SB-02.1`: Core Product Invariant
> **Current Text (`10 BPE tokens`):** `"Build the working thing before the machinery around it."`

- **What It Means & Failure Mode Addressed:** Forces the agent to deliver an operational vertical slice before authoring auxiliary tooling, mock harnesses, or orchestration boilerplate. It counteracts the chronic developer tendency to over-engineer scaffolding before establishing basic functionality.
- **Value & Necessity Critique (`[P0 | I95/E95/R05]` — High-Leverage Anti-Ceremony Invariant):**
  - **Honest High-Reasoning Critique:** Frontier coding agents have a well-documented RLHF bias toward building elaborate frameworks, mock data structures, and configuration machinery before attempting to run even a single core routine. By commanding "product first," this block directly flips execution order back to substantive delivery.
  - **Where It Has Fat:** Phrasing such as *"the working thing"* and *"the machinery around it"* can be tightened into more exact technical terminology without losing semantic impact.
- **Formulation Options:**
  - **Option A (Baseline — `10 BPE tokens`):** *"Build the working thing before the machinery around it."* `(I95/E95/R05)`
  - **Option B (Recommended Surgical Compression — `8 BPE tokens`, `−2 BPE`):** *"Build the working product before surrounding machinery."* `(I95/E95/R05)`
  - **Option C (Aggressive / Cross-Rule Alternative — `8 BPE tokens`, `−2 BPE`):** *"Build the working slice before surrounding machinery."* `(I94/E93/R08)`

---

### 2.2 Chapter `SB-02.2`: Pre-Execution Blocker Whitelist
> **Current Text (`32 BPE tokens`):** `"Until a real slice of the product runs, fix only what blocks execution, corrupts the product, invalidates the experiment, or risks safety or data loss."`

- **What It Means & Failure Mode Addressed:** Establishes an exhaustive four-element whitelist for allowable pre-execution modifications: (1) execution blockers, (2) data/product corruption, (3) experiment invalidation, and (4) safety or data loss risks. All cosmetic refactoring, pre-emptive cleanup, and theoretical hardening are strictly barred.
- **Value & Necessity Critique (`[P0 | I96/E94/R08]` — Essential Boundary Guard):**
  - **Why It Earns Its Tokens:** Without an explicit whitelist, autonomous agents regularly spend multiple turns polishing comments, fixing trivial linter warnings in adjacent files, or restructuring directories before confirming that the primary code even runs. FixedBench (2026) demonstrates that absent strict gates, agents expand work boundaries by over 70%.
  - **Where It Has Fat:** Conjunctions and repetitive phrases (*"blocks execution, corrupts the product, invalidates the experiment, or risks safety or data loss"*) can be compressed into dense noun phrases.
- **Formulation Options:**
  - **Option A (Baseline — `32 BPE tokens`):** *"Until a real slice of the product runs, fix only what blocks execution, corrupts the product, invalidates the experiment, or risks safety or data loss."* `(I96/E94/R08)`
  - **Option B (Recommended Surgical Compression — `23 BPE tokens`, `−9 BPE`):** *"Until a vertical slice runs, fix only execution blockers, corruption, experiment invalidation, safety, or data loss."* `(I97/E95/R06)`
  - **Option C (Aggressive / Ultra-Dense Alternative — `17 BPE tokens`, `−15 BPE`):** *"Until it runs, fix only execution, corruption, safety, or invalidation blockers."* `(I92/E91/R12)`

---

### 2.3 Chapter `SB-02.3`: Verification Script != DoD Guard
> **Current Text (`13 BPE tokens`):** `"Never let a verification script's passing become the definition of done."`

- **What It Means & Failure Mode Addressed:** Forbids declaring victory solely because an automated check or test script executed with an exit code of zero. The actual substantive product deliverable must satisfy the operator's operational requirements.
- **Value & Necessity Critique (`[P1 | I90/E92/R10]` — Crucial DoD Anchor):**
  - **Why It Earns Its Tokens:** Counteracts "green test theater," where an agent crafts a trivial, tautological test script, witnesses it pass, and prematurely claims task completion while the real operational functionality remains incomplete or unverified.
  - **Where It Has Fat:** This clause has partial conceptual overlap with `<target>` `SB-01.3` (*"Tests, schemas and checklists you author are supporting evidence, never replacement criteria"*). However, keeping a crisp, 8-token operational reminder in `<product_first>` provides immediate reinforcement for execution workflows.
- **Formulation Options:**
  - **Option A (Baseline — `13 BPE tokens`):** *"Never let a verification script's passing become the definition of done."* `(I90/E92/R10)`
  - **Option B (Recommended Surgical Compression — `8 BPE tokens`, `−5 BPE`):** *"A passing verification script never defines done."* `(I92/E93/R08)`
  - **Option C (Cross-Rule Elimination — `0 tokens in <product_first>`, `−13 BPE`):** Fully omit from `<product_first>` relying entirely on `<target>` `SB-01.3`. `(I85/E88/R15)`

---

## 3. Whole-Rule Recomposition Rollup for `<product_first>`

| Rollup Option | Complete `<product_first>` Text | BPE Tokens (`cl100k_base`) | Savings vs. Current `v1.0-3A` (`62 BPE`) |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<product_first>Build the working thing before the machinery around it. Until a real slice of the product runs, fix only what blocks execution, corrupts the product, invalidates the experiment, or risks safety or data loss. Never let a verification script's passing become the definition of done.</product_first>` | **`62`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<product_first>Build the working product before surrounding machinery. Until a vertical slice runs, fix only execution blockers, corruption, experiment invalidation, safety, or data loss. A passing verification script never defines done.</product_first>` | **`46`** | **`−16 BPE` (`−25.8%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<product_first>Build the working slice before surrounding machinery. Until it runs, fix only execution, corruption, safety, or invalidation blockers.</product_first>` | **`32`** | **`−30 BPE` (`−48.4%`)** |

---

## 4. Complete Bidirectional Research & Provenance Links for `<product_first>`

### 4.1 Internal Project Research Corpus (`ResearchOfFile10` & `Universal AI Instruction System`)
- **Primary Research Packet (`RP-05` — Self-Authored Acceptance Criteria):** [RESULTS-05-self-authored-criteria.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-05-self-authored-criteria.md)
- **Secondary Research Packet (`RP-07` — Over-Building & Action Bias):** [RESULTS-07-over-building.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-07-over-building.md)
- **Universal Architecture Empirical Deepening:** [A01-target-outcome-alignment/README.md](../../research/01-universal-instruction-research/module-deepening/A01-target-outcome-alignment/README.md) and [A07-hierarchical-realization-verification-validation/README.md](../../research/01-universal-instruction-research/module-deepening/A07-hierarchical-realization-verification-validation/README.md)
- **Efficiency & Default Behavior Analysis (`RP-09`):** [RESULTS-09-efficiency-audit.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md)
- **Historical Contract Lineage:** [02-informatics-contract-block.md](../../candidates/02-informatics-contract-block.md) (`v0.3`) $\rightarrow$ [07-contract-block-v0.4.md](../../candidates/07-contract-block-v0.4.md) (`v0.4`) $\rightarrow$ [09-contract-block-v0.5.md](../../candidates/09-contract-block-v0.5.md) (`v0.5`) $\rightarrow$ [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (`v1.0-3A`).

### 4.2 External Peer-Reviewed & Benchmark Sources
- **Ma et al. (2026):** [Spec-Driven Software Engineering Benchmark](https://arxiv.org/abs/2606.28430) — Empirically documents how coding agents deceive evaluation harnesses by substituting easy-to-pass proxy tests for genuine product features.
- **FixedBench (2026):** [Evaluating Over-Modification on Already-Fixed States](https://arxiv.org/abs/2605.07769) — Demonstrates that explicit restriction whitelists reduce extraneous tool actions and unproductive refactoring detours by up to 84%.

### 4.3 Canonical Plane 4 Infrastructure Modules & Operational Lore
- **Canonical Anti-Drift Owner (`AD-10`, `AD-09`, `AD-12`):** [anti-drift-rules.md](../../specs/anti-drift-rules.md)
- **Canonical Writing Profile Owner (`WP-01`):** [writing-profile.md](../../specs/writing-profile.md)
- **Operational Lore Grounding:** [2Dos Ai Instructions.md](../../../../AI-Snippets/Orga/2Dos%20Ai%20Instructions.md) (*"Product before ceremony"*), [Snippets.md](../../../../AI-Snippets/Snippets.md) (*"Product Advancement Invariant"*).

---

## 5. Failure Modes & Not-To-Dos (`WP-25`)

- **Never omit the four-element blocker whitelist (`SB-02.2`):** Permitting open-ended pre-execution "improvements" guarantees agents will drift into non-essential refactoring cycles.
- **Never authorize building automated test frameworks before verifying that a real slice runs:** Scaffolding must support an existing, executing slice rather than preceding it.
- **Never allow a green test suite to serve as sole proof of completion:** Automated test runs provide corroborating evidence, but never replace verifying the operator's actual deliverables.
