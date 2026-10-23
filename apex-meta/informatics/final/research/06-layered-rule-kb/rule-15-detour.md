---
type: Reference
id: V2-LAYERED-KB-RULE-15-DETOUR
title: Rule 15 Deep-Dive — <detour> Semantic Block Decomposition, Value Audit & Compression Options
description: Decomposing <detour> (from 13-candidate-3A-xml.md) into atomic semantic blocks, evaluating token value against premature refactoring and speculative architectural detours, formulating tighter alternatives, and linking all internal and external research.
status: current_truth
tags: [layered-kb, rule-15, detour, semantic-blocks, token-compression, research-ledger]
---

# Rule 15 Deep-Dive: `<detour>` (`13-candidate-3A-xml.md`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (format siblings: [14-candidate-3B-hybrid.md](../../candidates/14-candidate-3B-hybrid.md), [15-candidate-3C-bullet-hybrid.md](../../candidates/15-candidate-3C-bullet-hybrid.md))
> - **Layer 1 (This File — Rule-Level Semantic Block Audit):** Decomposes `<detour>` into 2 atomic semantic blocks (`SB-15.1`..`SB-15.2`), audits token value against unrequested refactoring detours, and presents scored compression options.
> - **Layer 2 (Downstream Infrastructure Modules):** [anti-drift-rules.md](../../specs/anti-drift-rules.md) (`AD-05`, `AD-10`, `AD-12`), [writing-profile.md](../../specs/writing-profile.md) (`WP-01`).

---

## 1. Original Rule & Atomic Semantic Block Inventory

### 1.1 Current `v1.0-3A` Full Text (`44 BPE block` | `22 BPE inner` | `23 repo tokens` | `94 chars` | `19 words`)

```xml
<detour when="about to propose a refactor, redesign, migration or infrastructure addition">
Ask whether this must be fixed before the product can be tested. If not, defer it in one line.
</detour>
```

### 1.2 Atomic Semantic Block Inventory (Bullet List)

Every token in `<detour>` belongs to one of two distinct semantic blocks (`SB-15.1` and `SB-15.2`), plus the XML gating tag wrapper (`<detour when="...">...</detour>`, `22 BPE tokens`):

- **`SB-15.1` — Pre-Test Testability Filter (`13 BPE tokens` | `64 chars`):** *"Ask whether this must be fixed before the product can be tested."*
- **`SB-15.2` — One-Line Deferral Mandate (`9 BPE tokens` | `29 chars`):** *"If not, defer it in one line."*

---

## 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

### 2.1 Chapter `SB-15.1`: Pre-Test Testability Filter
> **Current Text (`13 BPE tokens`):** `"Ask whether this must be fixed before the product can be tested."`

- **What It Means & Failure Mode Addressed:** Imposes an immediate testability filter before any proposed refactoring, architectural redesign, or migration: if the product can be tested and verified without the refactor, the refactor must not be executed.
- **Value & Necessity Critique (`[P0 | I95/E95/R05]` — Anti-Detour Gate):**
  - **Honest High-Reasoning Critique:** Autonomous coding agents frequently stumble upon legacy code, non-optimal abstractions, or style inconsistencies and immediately launch into multi-turn refactoring sprees that derail the authorized assignment. Enforcing a direct testability threshold stops premature cleanup dead in its tracks.
  - **Where It Has Fat:** Phrasing can be converted from an indirect prompt (*"Ask whether this must be fixed..."*) into a direct, punchy rhetorical question (*"Must this be fixed before testing the product?"*), saving 4 BPE tokens.
- **Formulation Options:**
  - **Option A (Baseline — `13 BPE tokens`):** *"Ask whether this must be fixed before the product can be tested."* `(I95/E95/R05)`
  - **Option B (Recommended Surgical Compression — `9 BPE tokens`, `−4 BPE`):** *"Must this be fixed before testing the product?"* `(I96/E95/R04)`
  - **Option C (Aggressive Alternative — `9 BPE tokens`, `−4 BPE`):** *"Must this be fixed before testing the product?"* `(I96/E95/R04)`

---

### 2.2 Chapter `SB-15.2`: One-Line Deferral Mandate
> **Current Text (`9 BPE tokens`):** `"If not, defer it in one line."`

- **What It Means & Failure Mode Addressed:** Mandates that non-blocking improvements be acknowledged and deferred in exactly one line of communication rather than generating pages of architectural proposals or roadmap discussions.
- **Value & Necessity Critique (`[P0 | I94/E95/R05]` — Scope Focus Shield):**
  - **Why It Earns Its Tokens:** Prevents conversational drift and token inflation. Noting an adjacent discovery in a single line satisfies the agent's observation mandate without distracting from immediate execution.
  - **Where It Has Fat:** At 9 BPE tokens, this imperative is concise, clear, and unambiguous.
- **Formulation Options:**
  - **Option A (Baseline — `9 BPE tokens`):** *"If not, defer it in one line."* `(I94/E95/R05)`
  - **Option B (Recommended Surgical Compression — `9 BPE tokens`, `+0 BPE`):** *"If not, defer it in one line."* `(I94/E95/R05)`
  - **Option C (Aggressive Alternative — `9 BPE tokens`, `+0 BPE`):** *"If not, defer it in one line."* `(I94/E95/R05)`

---

## 3. Whole-Rule Recomposition Rollup for `<detour>`

| Rollup Option | Complete `<detour>` Text | BPE Tokens (`cl100k_base`) | Savings vs. Current `v1.0-3A` (`44 BPE`) |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<detour when="about to propose a refactor, redesign, migration or infrastructure addition"> Ask whether this must be fixed before the product can be tested. If not, defer it in one line. </detour>` | **`44`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<detour when="about to propose a refactor, redesign, migration or infrastructure addition"> Must this be fixed before testing the product? If not, defer it in one line. </detour>` | **`40`** | **`−4 BPE` (`−9.1%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<detour when="about to propose a refactor, redesign, migration or infrastructure addition"> Must this be fixed before testing the product? If not, defer it in one line. </detour>` | **`40`** | **`−4 BPE` (`−9.1%`)** |

---

## 4. Complete Bidirectional Research & Provenance Links for `<detour>`

### 4.1 Internal Project Research Corpus (`ResearchOfFile10` & `Universal AI Instruction System`)
- **Primary Research Packet (`RP-07` — Over-Building & Detour Prevention):** [RESULTS-07-over-building.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-07-over-building.md)
- **Universal Architecture Empirical Deepening:** [A02-scope-non-goals/README.md](../../research/01-universal-instruction-research/module-deepening/A02-scope-non-goals/README.md)
- **Efficiency & Default Behavior Analysis (`RP-09`):** [RESULTS-09-efficiency-audit.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md)
- **Historical Contract Lineage:** [02-informatics-contract-block.md](../../candidates/02-informatics-contract-block.md) (`v0.3`) $\rightarrow$ [07-contract-block-v0.4.md](../../candidates/07-contract-block-v0.4.md) (`v0.4`) $\rightarrow$ [09-contract-block-v0.5.md](../../candidates/09-contract-block-v0.5.md) (`v0.5`) $\rightarrow$ [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (`v1.0-3A`).

### 4.2 External Peer-Reviewed & Benchmark Sources
- **FixedBench (2026):** [Evaluating Over-Modification on Already-Fixed States](https://arxiv.org/abs/2605.07769) — Proves that autonomous coding agents wander into unprompted refactorings in 82% of unconstrained runs, increasing regression rates by 3.4x.

### 4.3 Canonical Plane 4 Infrastructure Modules & Operational Lore
- **Canonical Anti-Drift Owner (`AD-05`, `AD-10`, `AD-12`):** [anti-drift-rules.md](../../specs/anti-drift-rules.md)
- **Canonical Writing Profile Owner (`WP-01`):** [writing-profile.md](../../specs/writing-profile.md)
- **Operational Lore Grounding:** [2Dos Ai Instructions.md](../../../../AI-Snippets/Orga/2Dos%20Ai%20Instructions.md) (*"Operator Challenge Boundary"*), [Snippets.md](../../../../AI-Snippets/Snippets.md) (*"Product Advancement Invariant"*).

---

## 5. Failure Modes & Not-To-Dos (`WP-25`)

- **Never allow multi-paragraph architectural proposals for non-blocking refactors:** Defer speculative cleanups in exactly one line of output.
- **Never initiate a codebase refactoring or cleanup when assigned a targeted fix:** Focus strictly on the operational deliverable.
- **Never bypass the testability check:** If the product can be tested in its current structure, refactoring is not a blocker.
