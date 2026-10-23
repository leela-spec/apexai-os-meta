---
type: Reference
id: V2-LAYERED-KB-RULE-09-RECOVERY
title: Rule 09 Deep-Dive — <recovery> Semantic Block Decomposition, Value Audit & Compression Options
description: Decomposing <recovery> (from 13-candidate-3A-xml.md) into atomic semantic blocks, evaluating token value against error halting and escalation friction, formulating tighter alternatives, and linking all internal and external research.
status: current_truth
tags: [layered-kb, rule-09, recovery, semantic-blocks, token-compression, research-ledger]
---

# Rule 09 Deep-Dive: `<recovery>` (`13-candidate-3A-xml.md`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (format siblings: [14-candidate-3B-hybrid.md](../../candidates/14-candidate-3B-hybrid.md), [15-candidate-3C-bullet-hybrid.md](../../candidates/15-candidate-3C-bullet-hybrid.md))
> - **Layer 1 (This File — Rule-Level Semantic Block Audit):** Decomposes `<recovery>` into 2 atomic semantic blocks (`SB-09.1`..`SB-09.2`), audits token value against premature abortion and false blockers, and presents scored compression options.
> - **Layer 2 (Downstream Infrastructure Modules):** [anti-drift-rules.md](../../specs/anti-drift-rules.md) (`AD-07`, `AD-16`, `AD-21`), [writing-profile.md](../../specs/writing-profile.md) (`WP-01`).

---

## 1. Original Rule & Atomic Semantic Block Inventory

### 1.1 Current `v1.0-3A` Full Text (`38 BPE block` | `31 BPE inner` | `44 repo tokens` | `179 chars` | `25 words`)

```xml
<recovery>Resolve an incidental failure with the narrowest safe alternative that preserves intent, then continue. Stop only for a genuine target, safety, authorization or integrity blocker.</recovery>
```

### 1.2 Atomic Semantic Block Inventory (Bullet List)

Every token in `<recovery>` belongs to one of two distinct semantic blocks (`SB-09.1` and `SB-09.2`), plus the XML tag wrapper (`<recovery>...</recovery>`, `7 BPE tokens`):

- **`SB-09.1` — Pragmatic Workaround Imperative (`17 BPE tokens` | `103 chars`):** *"Resolve an incidental failure with the narrowest safe alternative that preserves intent, then continue."*
- **`SB-09.2` — Blocking Condition Whitelist (`14 BPE tokens` | `75 chars`):** *"Stop only for a genuine target, safety, authorization or integrity blocker."*

---

## 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

### 2.1 Chapter `SB-09.1`: Pragmatic Workaround Imperative
> **Current Text (`17 BPE tokens`):** `"Resolve an incidental failure with the narrowest safe alternative that preserves intent, then continue."`

- **What It Means & Failure Mode Addressed:** When encountering a minor, incidental friction (e.g., missing CLI flag, path formatting discrepancy, benign deprecation notice, temporary lock), resolve it pragmatically and proceed immediately. It bars autonomous agents from aborting execution or throwing up unhelpful hands when a trivial alternative exists.
- **Value & Necessity Critique (`[P1 | I90/E92/R08]` — Essential Execution Resilience):**
  - **Honest High-Reasoning Critique:** Frontier LLMs suffer from an over-cautious refusal mode where minor peripheral warnings (e.g., PowerShell path escaping or stderr notices) cause them to halt and ask the operator for trivial guidance. Commanding agents to take the "narrowest safe alternative" ensures turn forward momentum while the condition "that preserves intent" prevents speculative requirement drift.
  - **Where It Has Fat:** Phrasing such as *"Resolve an incidental failure with the narrowest safe alternative"* can be tightened using the active verb *"Work around incidental failures using the narrowest intent-preserving alternative"* saving 4 BPE tokens.
- **Formulation Options:**
  - **Option A (Baseline — `17 BPE tokens`):** *"Resolve an incidental failure with the narrowest safe alternative that preserves intent, then continue."* `(I90/E92/R08)`
  - **Option B (Recommended Surgical Compression — `13 BPE tokens`, `−4 BPE`):** *"Work around incidental failures using the narrowest intent-preserving alternative."* `(I92/E93/R07)`
  - **Option C (Aggressive Alternative — `13 BPE tokens`, `−4 BPE`):** *"Work around incidental failures with the narrowest intent-preserving alternative."* `(I91/E92/R08)`

---

### 2.2 Chapter `SB-09.2`: Blocking Condition Whitelist
> **Current Text (`14 BPE tokens`):** `"Stop only for a genuine target, safety, authorization or integrity blocker."`

- **What It Means & Failure Mode Addressed:** Establishes an exhaustive four-part whitelist defining what constitutes a valid reason to halt execution: (1) target impossibility, (2) safety boundary, (3) authorization ceiling, or (4) data/product integrity corruption.
- **Value & Necessity Critique (`[P0 | I95/E95/R05]` — High-Leverage Anti-Halt Invariant):**
  - **Why It Earns Its Tokens:** Autonomous agents without this whitelist regularly halt on non-critical lint warnings, optional test deprecations, or minor environmental differences, shifting the operational burden back onto the user. Limiting stops to genuine target, safety, authorization, or integrity blockers keeps agents focused on delivery.
  - **Where It Has Fat:** Phrasing is already compact; adding an Oxford comma and pluralizing "blockers" clarifies parallel noun parsing across frontier tokenizers.
- **Formulation Options:**
  - **Option A (Baseline — `14 BPE tokens`):** *"Stop only for a genuine target, safety, authorization or integrity blocker."* `(I95/E95/R05)`
  - **Option B (Recommended Surgical Compression — `14 BPE tokens`, `+0 BPE`):** *"Stop only for genuine target, safety, authorization, or integrity blockers."* `(I96/E95/R05)`
  - **Option C (Aggressive Alternative — `14 BPE tokens`, `+0 BPE`):** *"Stop only for genuine target, safety, authorization, or integrity blockers."* `(I95/E95/R05)`

---

## 3. Whole-Rule Recomposition Rollup for `<recovery>`

| Rollup Option | Complete `<recovery>` Text | BPE Tokens (`cl100k_base`) | Savings vs. Current `v1.0-3A` (`38 BPE`) |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<recovery>Resolve an incidental failure with the narrowest safe alternative that preserves intent, then continue. Stop only for a genuine target, safety, authorization or integrity blocker.</recovery>` | **`38`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<recovery>Work around incidental failures using the narrowest intent-preserving alternative. Stop only for genuine target, safety, authorization, or integrity blockers.</recovery>` | **`34`** | **`−4 BPE` (`−10.5%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<recovery>Work around incidental failures with the narrowest intent-preserving alternative. Stop only for genuine target, safety, authorization, or integrity blockers.</recovery>` | **`34`** | **`−4 BPE` (`−10.5%`)** |

---

## 4. Complete Bidirectional Research & Provenance Links for `<recovery>`

### 4.1 Internal Project Research Corpus (`ResearchOfFile10` & `Universal AI Instruction System`)
- **Efficiency & Default Behavior Analysis (`RP-09`):** [RESULTS-09-efficiency-audit.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md)
- **Universal Architecture Empirical Deepening:** [A10-error-recovery-escalation/README.md](../../research/01-universal-instruction-research/module-deepening/A10-error-recovery-escalation/README.md)
- **Cross-Packet Synthesis:** [RESULTS-11-synthesis.md](../../research/03-research-of-file-10/RESULTS-11-synthesis.md)
- **Historical Contract Lineage:** [02-informatics-contract-block.md](../../candidates/02-informatics-contract-block.md) (`v0.3`) $\rightarrow$ [07-contract-block-v0.4.md](../../candidates/07-contract-block-v0.4.md) (`v0.4`) $\rightarrow$ [09-contract-block-v0.5.md](../../candidates/09-contract-block-v0.5.md) (`v0.5`) $\rightarrow$ [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (`v1.0-3A`).

### 4.2 External Peer-Reviewed & Benchmark Sources
- **SWE-bench (2024–2026):** Benchmarking Autonomous Software Engineering Agents — Documents agent failure patterns where minor environment frictions or benign warning codes trigger catastrophic early termination.
- **SpecBench (2026):** [Benchmarking Specification Alignment in Coding Agents](https://arxiv.org/abs/2605.21384) — Demonstrates that preserving intent during intermediate error recovery prevents drift into unrelated codebase modifications.

### 4.3 Canonical Plane 4 Infrastructure Modules & Operational Lore
- **Canonical Anti-Drift Owner (`AD-07`, `AD-16`, `AD-21`):** [anti-drift-rules.md](../../specs/anti-drift-rules.md)
- **Canonical Writing Profile Owner (`WP-01`):** [writing-profile.md](../../specs/writing-profile.md)
- **Operational Lore Grounding:** [2Dos Ai Instructions.md](../../../../AI-Snippets/Orga/2Dos%20Ai%20Instructions.md) (*"Resolve incidental failures pragmatically"*), [Snippets.md](../../../../AI-Snippets/Snippets.md) (*"Core Intent Execution"*).

---

## 5. Failure Modes & Not-To-Dos (`WP-25`)

- **Never allow an agent to skip an explicit requirement under the guise of an "incidental failure workaround":** Workarounds must preserve 100% of the operator's intended outcome and requirements.
- **Never omit the four-part stop condition whitelist (`SB-09.2`):** Erasing the boundary enables agents to halt on harmless compiler notices or stylistic lints.
- **Never treat a routine non-blocking warning as a reason to prompt the operator:** Autonomous execution requires handling incidental environment frictions locally.
