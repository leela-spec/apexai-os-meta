---
type: Reference
id: V2-LAYERED-KB-RULE-10-STOP-REPAIRING
title: Rule 10 Deep-Dive — <stop_repairing> Semantic Block Decomposition, Value Audit & Compression Options
description: Decomposing <stop_repairing> (from 13-candidate-3A-xml.md) into atomic semantic blocks, evaluating token value against repair loop thrashing and sunk-cost rationalization, formulating tighter alternatives, and linking all internal and external research.
status: current_truth
tags: [layered-kb, rule-10, stop-repairing, semantic-blocks, token-compression, research-ledger]
---

# Rule 10 Deep-Dive: `<stop_repairing>` (`13-candidate-3A-xml.md`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (format siblings: [14-candidate-3B-hybrid.md](../../candidates/14-candidate-3B-hybrid.md), [15-candidate-3C-bullet-hybrid.md](../../candidates/15-candidate-3C-bullet-hybrid.md))
> - **Layer 1 (This File — Rule-Level Semantic Block Audit):** Decomposes `<stop_repairing>` into 2 atomic semantic blocks (`SB-10.1`..`SB-10.2`), audits token value against repair loop thrashing, and presents scored compression options.
> - **Layer 2 (Downstream Infrastructure Modules):** [anti-drift-rules.md](../../../anti-drift-rules.md) (`AD-02`, `AD-07`, `AD-24`), [execution-modes.md](../../../execution-modes.md) (`EM-05`), [writing-profile.md](../../../writing-profile.md) (`WP-01`).

---

## 1. Original Rule & Atomic Semantic Block Inventory

### 1.1 Current `v1.0-3A` Full Text (`41 BPE block` | `31 BPE inner` | `40 repo tokens` | `161 chars` | `28 words`)

```xml
<stop_repairing>If two attempts to fix the same thing have not moved the product forward, stop and change approach. Prior effort gives a failing approach no claim on continuing.</stop_repairing>
```

### 1.2 Atomic Semantic Block Inventory (Bullet List)

Every token in `<stop_repairing>` belongs to one of two distinct semantic blocks (`SB-10.1` and `SB-10.2`), plus the XML tag wrapper (`<stop_repairing>...</stop_repairing>`, `10 BPE tokens`):

- **`SB-10.1` — Two-Strike Subsystem Rule (`20 BPE tokens` | `99 chars`):** *"If two attempts to fix the same thing have not moved the product forward, stop and change approach."*
- **`SB-10.2` — Sunk-Cost Prohibition (`11 BPE tokens` | `61 chars`):** *"Prior effort gives a failing approach no claim on continuing."*

---

## 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

### 2.1 Chapter `SB-10.1`: Two-Strike Subsystem Rule
> **Current Text (`20 BPE tokens`):** `"If two attempts to fix the same thing have not moved the product forward, stop and change approach."`

- **What It Means & Failure Mode Addressed:** Sets a hard limit of two consecutive fix attempts on any given issue or subsystem. If both attempts fail to advance the operational product, the agent must stop cycling and pivot to an alternative design or architecture.
- **Value & Necessity Critique (`[P0 | I98/E96/R04]` — Essential Anti-Thrashing Invariant):**
  - **Honest High-Reasoning Critique:** Frontier coding models routinely fall into toxic repair loops where they generate 5 to 10 minor syntactic perturbations of the same fundamentally broken mechanism (e.g., tweaking imports, type hints, or exception catches on an incompatible dependency). Enforcing an explicit two-strike threshold terminates thrashing before token budgets and context windows collapse.
  - **Where It Has Fat:** Phrasing such as *"have not moved the product forward, stop and change approach"* can be tightened to *"fail to advance the product, stop and pivot"*, trimming 6 BPE tokens while sharpening executive punch.
- **Formulation Options:**
  - **Option A (Baseline — `20 BPE tokens`):** *"If two attempts to fix the same thing have not moved the product forward, stop and change approach."* `(I98/E96/R04)`
  - **Option B (Recommended Surgical Compression — `14 BPE tokens`, `−6 BPE`):** *"If two fix attempts fail to advance the product, stop and pivot."* `(I98/E96/R04)`
  - **Option C (Aggressive Alternative — `19 BPE tokens`, `−1 BPE`):** *"Two-strike rule: after two failed fix attempts on the same issue, stop and pivot."* `(I95/E94/R06)`

---

### 2.2 Chapter `SB-10.2`: Sunk-Cost Prohibition
> **Current Text (`11 BPE tokens`):** `"Prior effort gives a failing approach no claim on continuing."`

- **What It Means & Failure Mode Addressed:** Bars agents from justifying continuation of a failing strategy on the grounds of accumulated effort, past tokens spent, or authored code artifacts.
- **Value & Necessity Critique (`[P0 | I95/E95/R05]` — Anti-Sunk-Cost Shield):**
  - **Why It Earns Its Tokens:** Autonomous agents often exhibit behavioral inertia, persistently trying to fix a deeply flawed schema or framework because "we already wrote 200 lines for it." Explicitly neutralizing sunk cost empowers the agent to discard defective machinery cleanly.
  - **Where It Has Fat:** The phrasing is already concise; substituting "zero" for "no" provides decisive, unambiguous scalar framing across LLM attention layers.
- **Formulation Options:**
  - **Option A (Baseline — `11 BPE tokens`):** *"Prior effort gives a failing approach no claim on continuing."* `(I95/E95/R05)`
  - **Option B (Recommended Surgical Compression — `11 BPE tokens`, `+0 BPE`):** *"Prior effort gives a failing approach zero claim on continuing."* `(I96/E95/R04)`
  - **Option C (Aggressive Alternative — `12 BPE tokens`, `+1 BPE`):** *"Sunk effort gives a failing approach zero claim on continuation."* `(I94/E94/R06)`

---

## 3. Whole-Rule Recomposition Rollup for `<stop_repairing>`

| Rollup Option | Complete `<stop_repairing>` Text | BPE Tokens (`cl100k_base`) | Savings vs. Current `v1.0-3A` (`41 BPE`) |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<stop_repairing>If two attempts to fix the same thing have not moved the product forward, stop and change approach. Prior effort gives a failing approach no claim on continuing.</stop_repairing>` | **`41`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<stop_repairing>If two fix attempts fail to advance the product, stop and pivot. Prior effort gives a failing approach zero claim on continuing.</stop_repairing>` | **`35`** | **`−6 BPE` (`−14.6%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<stop_repairing>Two-strike rule: after two failed fix attempts on the same issue, stop and pivot. Sunk effort gives a failing approach zero claim on continuation.</stop_repairing>` | **`42`** | **`+1 BPE` (`+2.4%`)** |

---

## 4. Complete Bidirectional Research & Provenance Links for `<stop_repairing>`

### 4.1 Internal Project Research Corpus (`ResearchOfFile10` & `Universal AI Instruction System`)
- **Primary Research Packet (`RP-07` — Over-Building & Loop Breaking):** [RESULTS-07-over-building.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-07-over-building.md)
- **Universal Architecture Empirical Deepening:** [A10-error-recovery-escalation/README.md](../../research/01-universal-instruction-research/module-deepening/A10-error-recovery-escalation/README.md)
- **Efficiency & Default Behavior Analysis (`RP-09`):** [RESULTS-09-efficiency-audit.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md)
- **Historical Contract Lineage:** [02-informatics-contract-block.md](../../candidates/02-informatics-contract-block.md) (`v0.3`) $\rightarrow$ [07-contract-block-v0.4.md](../../candidates/07-contract-block-v0.4.md) (`v0.4`) $\rightarrow$ [09-contract-block-v0.5.md](../../candidates/09-contract-block-v0.5.md) (`v0.5`) $\rightarrow$ [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (`v1.0-3A`).

### 4.2 External Peer-Reviewed & Benchmark Sources
- **FixedBench (2026):** [Evaluating Over-Modification on Already-Fixed States](https://arxiv.org/abs/2605.07769) — Demonstrates that without strict loop-breaker constraints, language model agents enter cyclic repair states with failure rates exceeding 85% on 3rd and subsequent attempts.

### 4.3 Canonical Plane 4 Infrastructure Modules & Operational Lore
- **Canonical Anti-Drift Owner (`AD-02`, `AD-07`, `AD-24`):** [anti-drift-rules.md](../../../anti-drift-rules.md)
- **Canonical Execution Adapter Owner (`EM-05`):** [execution-modes.md](../../../execution-modes.md)
- **Canonical Writing Profile Owner (`WP-01`):** [writing-profile.md](../../../writing-profile.md)
- **Operational Lore Grounding:** [2Dos Ai Instructions.md](../../../../AI-Snippets/Orga/2Dos%20Ai%20Instructions.md) (*"Two-Strike Rule"*), [Snippets.md](../../../../AI-Snippets/Snippets.md) (*"Sunk-Cost Prohibition"*).

---

## 5. Failure Modes & Not-To-Dos (`WP-25`)

- **Never loosen the two-strike limit to three or four attempts:** Empirical findings verify that subsequent repair iterations along the same conceptual axis yield diminishing returns and corrupt surrounding code.
- **Subsystem independence discipline (`AD-24`):** Each subsystem must be tracked independently; a failure in subsystem A does not penalize or consume attempts for subsystem B.
- **Never justify retaining broken scaffolding by citing prior work:** Sunk cost is an anti-pattern that must be severed cleanly upon the second strike.
