---
type: Reference
id: V2-LAYERED-KB-RULE-03-SCOPE
title: Rule 03 Deep-Dive — <scope> Semantic Block Decomposition, Value Audit & Compression Options
description: Decomposing <scope> (from 13-candidate-3A-xml.md) into atomic semantic blocks, evaluating token value, formulating tighter alternatives, and linking all internal and external research.
status: current_truth
tags: [layered-kb, rule-03, scope, semantic-blocks, token-compression, research-ledger]
---

# Rule 03 Deep-Dive: `<scope>` (`13-candidate-3A-xml.md`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (format siblings: [14-candidate-3B-hybrid.md](../../candidates/14-candidate-3B-hybrid.md), [15-candidate-3C-bullet-hybrid.md](../../candidates/15-candidate-3C-bullet-hybrid.md))
> - **Layer 1 (This File — Rule-Level Semantic Block Audit):** Decomposes `<scope>` into 3 atomic semantic blocks (`SB-03.1`..`SB-03.3`), audits token value against prompt expansion biases, and presents scored compression options.
> - **Layer 2 (Downstream Infrastructure Modules):** [anti-drift-rules.md](../../specs/anti-drift-rules.md) (`AD-18`, `AD-05`), [writing-profile.md](../../specs/writing-profile.md) (`WP-09`).

---

## 1. Original Rule & Atomic Semantic Block Inventory

### 1.1 Current `v1.0-3A` Full Text (`43 BPE block` | `38 BPE inner` | `57 repo tokens` | `230 chars` | `31 words`)

```xml
<scope>Do the authorized task and the work that materially enables it. Report adjacent improvements, cleanup, redesign and speculative capability instead of building them. Analyzing, reviewing or planning does not authorize implementing.</scope>
```

### 1.2 Atomic Semantic Block Inventory (Bullet List)

Every token in `<scope>` belongs to one of three distinct semantic blocks (`SB-03.1` through `SB-03.3`), plus the XML tag wrapper (`<scope>...</scope>`, `5 BPE tokens`):

- **`SB-03.1` — Authorized Task Boundary (`12 BPE tokens` | `63 chars`):** *"Do the authorized task and the work that materially enables it."*
- **`SB-03.2` — Report vs Build Prohibition (`15 BPE tokens` | `100 chars`):** *"Report adjacent improvements, cleanup, redesign and speculative capability instead of building them."*
- **`SB-03.3` — Read/Plan != Write Authority Gate (`11 BPE tokens` | `65 chars`):** *"Analyzing, reviewing or planning does not authorize implementing."*

---

## 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

### 2.1 Chapter `SB-03.1`: Authorized Task Boundary
> **Current Text (`12 BPE tokens`):** `"Do the authorized task and the work that materially enables it."`

- **What It Means & Failure Mode Addressed:** Confines execution strictly to the user's explicit objective plus whatever auxiliary actions are physically required to achieve it. It stops prompt-expansion drift where an agent takes a single feature request as an invitation to rewrite surrounding systems.
- **Value & Necessity Critique (`[P0 | I95/E95/R05]` — Core Anti-Drift Invariant):**
  - **Honest High-Reasoning Critique:** Frontier language models regularly interpret tasks expansively, inferring "helpful" tangential goals that were never authorized. Establishing that only the authorized task and its material enablers are in scope provides an unambiguous execution boundary.
  - **Where It Has Fat:** Phrasing can be tightened from 12 BPE tokens down to 10 BPE tokens while preserving full normative force.
- **Formulation Options:**
  - **Option A (Baseline — `12 BPE tokens`):** *"Do the authorized task and the work that materially enables it."* `(I95/E95/R05)`
  - **Option B (Recommended Surgical Compression — `10 BPE tokens`, `−2 BPE`):** *"Do only authorized work and material enablers."* `(I96/E95/R05)`
  - **Option C (Aggressive Imperative — `10 BPE tokens`, `−2 BPE`):** *"Execute only authorized work and material enablers;"* `(I94/E94/R08)`

---

### 2.2 Chapter `SB-03.2`: Report vs Build Prohibition
> **Current Text (`15 BPE tokens`):** `"Report adjacent improvements, cleanup, redesign and speculative capability instead of building them."`

- **What It Means & Failure Mode Addressed:** Mandates that when an agent identifies potential improvements outside the explicit assignment, it must capture them in text (e.g., in a handoff report or notes section) rather than altering codebase files.
- **Value & Necessity Critique (`[P0 | I94/E94/R06]` — Anti-Detour Safety Gate):**
  - **Why It Earns Its Tokens:** Prevents self-inflicted regressions. Autonomous agents frequently discover "dirty" legacy code or unoptimized routines while navigating a repository, attempt opportunistic cleanup, introduce breaking changes, and burn subsequent turns fixing bugs in code unrelated to the user's prompt.
  - **Where It Has Fat:** Enumerating four nouns (*"adjacent improvements, cleanup, redesign and speculative capability"*) spends 15 BPE tokens. This can be streamlined to capture the core failure categories.
- **Formulation Options:**
  - **Option A (Baseline — `15 BPE tokens`):** *"Report adjacent improvements, cleanup, redesign and speculative capability instead of building them."* `(I94/E94/R06)`
  - **Option B (Recommended Surgical Compression — `14 BPE tokens`, `−1 BPE`):** *"Report adjacent cleanup, redesign, and speculative features instead of building them."* `(I95/E95/R05)`
  - **Option C (Aggressive / Elliptical Alternative — `8 BPE tokens`, `−7 BPE`):** *"report adjacent cleanup instead of building it."* `(I88/E90/R15)`

---

### 2.3 Chapter `SB-03.3`: Read/Plan != Write Authority Gate
> **Current Text (`11 BPE tokens`):** `"Analyzing, reviewing or planning does not authorize implementing."`

- **What It Means & Failure Mode Addressed:** Explicitly specifies that prompts requesting analysis, architectural review, design options, or execution plans convey zero authorization to modify files or mutate system state.
- **Value & Necessity Critique (`[P0 | I96/E96/R04]` — Essential Apex Operational Invariant):**
  - **Why It Earns Its Tokens:** Frontier models frequently suffer from catastrophic action bias. When an operator asks "Can you analyze how to refactor this module?", default LLM behavior often jumps straight to modifying the files. This clause establishes an airtight boundary between inspection/planning and physical modification.
  - **Where It Has Fat:** The gerund triplet (*"Analyzing, reviewing or planning"*) can be reduced to two primary cognitive verbs without semantic erosion.
- **Formulation Options:**
  - **Option A (Baseline — `11 BPE tokens`):** *"Analyzing, reviewing or planning does not authorize implementing."* `(I96/E96/R04)`
  - **Option B (Recommended Surgical Compression — `9 BPE tokens`, `−2 BPE`):** *"Analyzing or planning never authorizes implementing."* `(I97/E96/R04)`
  - **Option C (Aggressive Alternative — `8 BPE tokens`, `−3 BPE`):** *"Analysis or planning never authorizes implementation."* `(I95/E95/R05)`

---

## 3. Whole-Rule Recomposition Rollup for `<scope>`

| Rollup Option | Complete `<scope>` Text | BPE Tokens (`cl100k_base`) | Savings vs. Current `v1.0-3A` (`43 BPE`) |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<scope>Do the authorized task and the work that materially enables it. Report adjacent improvements, cleanup, redesign and speculative capability instead of building them. Analyzing, reviewing or planning does not authorize implementing.</scope>` | **`43`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<scope>Do only authorized work and material enablers. Report adjacent cleanup, redesign, and speculative features instead of building them. Analyzing or planning never authorizes implementing.</scope>` | **`38`** | **`−5 BPE` (`−11.6%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<scope>Execute authorized work and material enablers; report adjacent cleanup instead of building it. Analysis or planning never authorizes implementation.</scope>` | **`30`** | **`−13 BPE` (`−30.2%`)** |

---

## 4. Complete Bidirectional Research & Provenance Links for `<scope>`

### 4.1 Internal Project Research Corpus (`ResearchOfFile10` & `Universal AI Instruction System`)
- **Primary Research Packet (`RP-07` — Over-Building & Action Bias):** [RESULTS-07-over-building.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-07-over-building.md)
- **Universal Architecture Empirical Deepening:** [A02-scope-non-goals/README.md](../../research/01-universal-instruction-research/module-deepening/A02-scope-non-goals/README.md)
- **Efficiency & Default Behavior Analysis (`RP-09`):** [RESULTS-09-efficiency-audit.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md)
- **Historical Contract Lineage:** [02-informatics-contract-block.md](../../candidates/02-informatics-contract-block.md) (`v0.3`) $\rightarrow$ [07-contract-block-v0.4.md](../../candidates/07-contract-block-v0.4.md) (`v0.4`) $\rightarrow$ [09-contract-block-v0.5.md](../../candidates/09-contract-block-v0.5.md) (`v0.5`) $\rightarrow$ [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (`v1.0-3A`).

### 4.2 External Peer-Reviewed & Benchmark Sources
- **FixedBench (2026):** [Evaluating Over-Modification on Already-Fixed States](https://arxiv.org/abs/2605.07769) — Demonstrates that coding agents suffer from severe action bias, performing unrequested refactorings in over 80% of test scenarios unless explicitly constrained to authorized boundaries.

### 4.3 Canonical Plane 4 Infrastructure Modules & Operational Lore
- **Canonical Anti-Drift Owner (`AD-18`, `AD-05`):** [anti-drift-rules.md](../../specs/anti-drift-rules.md)
- **Canonical Writing Profile Owner (`WP-09`):** [writing-profile.md](../../specs/writing-profile.md)
- **Operational Lore Grounding:** [2Dos Ai Instructions.md](../../../../AI-Snippets/Orga/2Dos%20Ai%20Instructions.md) (*"Zero-Speculation Scope Boundary"*), [Snippets.md](../../../../AI-Snippets/Snippets.md) (*"Scope boundary"*).

---

## 5. Failure Modes & Not-To-Dos (`WP-25`)

- **Never remove the Read/Plan != Write authority gate (`SB-03.3`):** Without this explicit barrier, agents will routinely convert diagnostic or exploratory questions into unwanted codebase edits.
- **Never prohibit reporting adjacent insights:** Reporting observations allows the operator to evaluate future work without bearing the immediate execution risk of unvetted changes.
- **Never allow "while I'm here" refactoring:** Touching code outside the direct path of the authorized task violates the single-responsibility principle of autonomous turns.
