---
type: Reference
id: V2-LAYERED-KB-RULE-22-POINTERS
title: Rule 22 Deep-Dive — <pointers> Semantic Block Decomposition, Value Audit & Compression Options
description: Decomposing <pointers> (from 13-candidate-3A-xml.md) into atomic semantic blocks, evaluating token value as the terminal guard and JIT path resolver, formulating tighter alternatives, and linking all internal and external research.
status: current_truth
tags: [layered-kb, rule-22, pointers, semantic-blocks, token-compression, research-ledger]
---

# Rule 22 Deep-Dive: `<pointers>` (`13-candidate-3A-xml.md`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (format siblings: [14-candidate-3B-hybrid.md](../../candidates/14-candidate-3B-hybrid.md), [15-candidate-3C-bullet-hybrid.md](../../candidates/15-candidate-3C-bullet-hybrid.md))
> - **Layer 1 (This File — Rule-Level Semantic Block Audit):** Decomposes `<pointers>` into 2 atomic semantic blocks (`SB-22.1`..`SB-22.2`), audits token value as the terminal guard, and presents scored compression options.
> - **Layer 2 (Downstream Infrastructure Modules):** [general-informatics-router.md](../../specs/general-informatics-router.md), [writing-profile.md](../../specs/writing-profile.md) (`WP-25`, `WP-18`), [anti-drift-rules.md](../../specs/anti-drift-rules.md) (`AD-26`).

---

## 1. Original Rule & Atomic Semantic Block Inventory

### 1.1 Current `v1.0-3A` Full Text (`32 BPE block` | `25 BPE inner` | `38 repo tokens` | `155 chars` | `20 words`)

```xml
<pointers>Paths are just-in-time pointers relative to base_ref. Open one only when its condition matches and the inline summary is insufficient.</pointers>
```

### 1.2 Atomic Semantic Block Inventory (Bullet List)

Every token in `<pointers>` belongs to one of two distinct semantic blocks (`SB-22.1` and `SB-22.2`), plus the XML tag wrapper (`<pointers>...</pointers>`, `7 BPE tokens`):

- **`SB-22.1` — Base Ref Path Factoring (`11 BPE tokens` | `53 chars`):** *"Paths are just-in-time pointers relative to base_ref."*
- **`SB-22.2` — Two-Threshold Escalation Invariant (`14 BPE tokens` | `80 chars`):** *"Open one only when its condition matches and the inline summary is insufficient."*

---

## 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

### 2.1 Chapter `SB-22.1`: Base Ref Path Factoring
> **Current Text (`11 BPE tokens`):** `"Paths are just-in-time pointers relative to base_ref."`

- **What It Means & Failure Mode Addressed:** Establishes the scoping convention for all reference attributes: any `ref="..."` attribute inside `<apex_contract>` resolves relative to `base_ref="apex-meta/informatics/"` declared on the root tag.
- **Value & Necessity Critique (`[P1 | I92/E90/R08]` — Prefix Factoring):**
  - **Honest High-Reasoning Critique:** Eliminates repetitive directory prefix tokens (e.g. `apex-meta/informatics/`) across all individual gating tags (`RP-09`, `RP-10`). Factoring the base path once saves ~25 tokens across the contract block and enables portable file relocation.
  - **Where It Has Fat:** At 11 BPE tokens, this definition is clear, precise, and introduces the `base_ref` contract mechanism.
- **Formulation Options:**
  - **Option A (Baseline — `11 BPE tokens`):** *"Paths are just-in-time pointers relative to base_ref."* `(I92/E90/R08)`
  - **Option B (Recommended Surgical Compression — `11 BPE tokens`, `+0 BPE`):** *"Paths are just-in-time pointers relative to base_ref."* `(I92/E90/R08)`
  - **Option C (Aggressive Alternative — `9 BPE tokens`, `−2 BPE`):** *"Paths are JIT pointers relative to base_ref."* `(I90/E88/R10)`

---

### 2.2 Chapter `SB-22.2`: Two-Threshold Escalation Invariant
> **Current Text (`14 BPE tokens`):** `"Open one only when its condition matches and the inline summary is insufficient."`

- **What It Means & Failure Mode Addressed:** Imposes a strict dual-gate threshold before opening any referenced Plane 4 specification module: (1) the active task must trigger the `when="..."` condition, AND (2) the inline rule summary must prove genuinely insufficient for execution.
- **Value & Necessity Critique (`[P0 | I96/E96/R05]` — Terminal Guard Invariant):**
  - **Why It Earns Its Tokens:** Positioned at the very end of the contract block to leverage the recency effect (`WP-25`, `AD-26`). Without this explicit double-lock threshold, agents eagerly read 300-line reference files on turn 1, bloating the context window and diluting focus.
  - **Where It Has Fat:** Replacing "one" with "a reference" adds 1 BPE token but improves grammatical clarity, preventing ambiguity in prompt interpretation.
- **Formulation Options:**
  - **Option A (Baseline — `14 BPE tokens`):** *"Open one only when its condition matches and the inline summary is insufficient."* `(I96/E96/R05)`
  - **Option B (Recommended Surgical Compression — `15 BPE tokens`, `+1 BPE`):** *"Open a reference only when its condition matches and the inline summary is insufficient."* `(I97/E96/R04)`
  - **Option C (Aggressive Alternative — `15 BPE tokens`, `+1 BPE`):** *"Open a reference only when its condition triggers and the inline summary is insufficient."* `(I95/E95/R05)`

---

## 3. Whole-Rule Recomposition Rollup for `<pointers>`

| Rollup Option | Complete `<pointers>` Text | BPE Tokens (`cl100k_base`) | Savings vs. Current `v1.0-3A` (`32 BPE`) |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<pointers>Paths are just-in-time pointers relative to base_ref. Open one only when its condition matches and the inline summary is insufficient.</pointers>` | **`32`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<pointers>Paths are just-in-time pointers relative to base_ref. Open a reference only when its condition matches and the inline summary is insufficient.</pointers>` | **`33`** | **`+1 BPE` (`+3.1%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<pointers>Paths are JIT pointers relative to base_ref. Open a reference only when its condition triggers and the inline summary is insufficient.</pointers>` | **`31`** | **`−1 BPE` (`−3.1%`)** |

---

## 4. Complete Bidirectional Research & Provenance Links for `<pointers>`

### 4.1 Internal Project Research Corpus (`ResearchOfFile10` & `Universal AI Instruction System`)
- **Primary Research Packet (`RP-08` — Deepen-When Removal & Terminal Folding):** [RESULTS-08-deepen-when-mechanics.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-08-deepen-when-mechanics.md)
- **Base Ref Path Factoring & Architecture (`RP-09`):** [RESULTS-09-efficiency-audit.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md)
- **Surface Layering & Terminal Position Invariants (`RP-10`):** [RESULTS-10-surface-layering.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-10-surface-layering.md)
- **Cross-Packet Synthesis:** [RESULTS-11-synthesis.md](../../research/03-research-of-file-10/RESULTS-11-synthesis.md)
- **Historical Contract Lineage:** [02-informatics-contract-block.md](../../candidates/02-informatics-contract-block.md) (`v0.3`) $\rightarrow$ [07-contract-block-v0.4.md](../../candidates/07-contract-block-v0.4.md) (`v0.4`) $\rightarrow$ [09-contract-block-v0.5.md](../../candidates/09-contract-block-v0.5.md) (`v0.5`) $\rightarrow$ [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (`v1.0-3A`).

### 4.2 External Peer-Reviewed & Benchmark Sources
- **OASIS DITA Content Reference (`conref`) Model:** Scalable JIT indirect referencing architecture separating root routing from deep modular specifications.
- **SpecBench (2026):** Progressive context retrieval and the quantitative hazards of premature, eager reference loading in coding agents.

### 4.3 Canonical Plane 4 Infrastructure Modules & Operational Lore
- **Canonical General Router Owner:** [general-informatics-router.md](../../specs/general-informatics-router.md)
- **Canonical Writing Profile Owner (`WP-25`, `WP-18`):** [writing-profile.md](../../specs/writing-profile.md)
- **Canonical Anti-Drift Owner (`AD-26`):** [anti-drift-rules.md](../../specs/anti-drift-rules.md)
- **Operational Lore Grounding:** [2Dos Ai Instructions.md](../../../../AI-Snippets/Orga/2Dos%20Ai%20Instructions.md) (*"Two-threshold JIT routing"*), [Snippets.md](../../../../AI-Snippets/Snippets.md) (*"Terminal Guard"*).

---

## 5. Failure Modes & Not-To-Dos (`WP-25`)

- **Never move `<pointers>` away from the terminal position of the contract block (`WP-25`):** Terminal position maximizes adherence via the recency effect.
- **Never open a referenced specification file unless BOTH thresholds are satisfied:** The task trigger must match AND the inline summary must be inadequate to proceed.
- **Never resolve relative `ref="..."` paths against arbitrary parent directories:** Always anchor resolution to `base_ref`.
