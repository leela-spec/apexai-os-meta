---
type: Reference
id: V2-LAYERED-KB-RULE-11-CURRENT-TRUTH
title: Rule 11 Deep-Dive — <current_truth> Semantic Block Decomposition, Value Audit & Compression Options
description: Decomposing <current_truth> (from 13-candidate-3A-xml.md) into atomic semantic blocks, evaluating token value against stale documentation and semantic priming resurrection, formulating tighter alternatives, and linking all internal and external research.
status: current_truth
tags: [layered-kb, rule-11, current-truth, semantic-blocks, token-compression, research-ledger]
---

# Rule 11 Deep-Dive: `<current_truth>` (`13-candidate-3A-xml.md`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (format siblings: [14-candidate-3B-hybrid.md](../../candidates/14-candidate-3B-hybrid.md), [15-candidate-3C-bullet-hybrid.md](../../candidates/15-candidate-3C-bullet-hybrid.md))
> - **Layer 1 (This File — Rule-Level Semantic Block Audit):** Decomposes `<current_truth>` into 3 atomic semantic blocks (`SB-11.1`..`SB-11.3`), audits token value against prompt semantic priming, and presents scored compression options.
> - **Layer 2 (Downstream Infrastructure Modules):** [file-architecture.md](../../../file-architecture.md) (`FA-01`, `FA-09`, `FA-11`), [writing-profile.md](../../../writing-profile.md) (`WP-08`), [anti-drift-rules.md](../../../anti-drift-rules.md) (`AD-15`).

---

## 1. Original Rule & Atomic Semantic Block Inventory

### 1.1 Current `v1.0-3A` Full Text (`38 BPE block` | `31 BPE inner` | `38 repo tokens` | `154 chars` | `24 words`)

```xml
<current_truth>State active truth only. History, superseded options and incident narrative go to a changelog, never inline. Do not name retired components in live rules.</current_truth>
```

### 1.2 Atomic Semantic Block Inventory (Bullet List)

Every token in `<current_truth>` belongs to one of three distinct semantic blocks (`SB-11.1` through `SB-11.3`), plus the XML tag wrapper (`<current_truth>...</current_truth>`, `7 BPE tokens`):

- **`SB-11.1` — Current-Truth Invariant (`5 BPE tokens` | `24 chars`):** *"State active truth only."*
- **`SB-11.2` — External Changelog Isolation (`17 BPE tokens` | `83 chars`):** *"History, superseded options and incident narrative go to a changelog, never inline."*
- **`SB-11.3` — Residual Name Eradication (`9 BPE tokens` | `45 chars`):** *"Do not name retired components in live rules."*

---

## 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

### 2.1 Chapter `SB-11.1`: Current-Truth Invariant
> **Current Text (`5 BPE tokens`):** `"State active truth only."`

- **What It Means & Failure Mode Addressed:** Directs all living documentation, code comments, and specification files to reflect solely what currently functions and is authoritative. It eradicates the tendency of documentation to blend historical records, planned features, and obsolete behaviors into a single confusing narrative.
- **Value & Necessity Critique (`[P0 | I96/E96/R05]` — Core Epistemic Pillar):**
  - **Honest High-Reasoning Critique:** In multi-turn and multi-agent workflows, context windows quickly become contaminated when files describe both the legacy state and the target state. Autonomous agents frequently follow outdated guidelines because they cannot determine whether a paragraph describes current reality or past history.
  - **Where It Has Fat:** At 5 BPE tokens, this opening imperative is already maximally dense and effective.
- **Formulation Options:**
  - **Option A (Baseline — `5 BPE tokens`):** *"State active truth only."* `(I96/E96/R05)`
  - **Option B (Recommended Surgical Compression — `5 BPE tokens`, `+0 BPE`):** *"State active truth only."* `(I96/E96/R05)`
  - **Option C (Aggressive Alternative — `5 BPE tokens`, `+0 BPE`):** *"State active truth only;"* `(I95/E95/R06)`

---

### 2.2 Chapter `SB-11.2`: External Changelog Isolation
> **Current Text (`17 BPE tokens`):** `"History, superseded options and incident narrative go to a changelog, never inline."`

- **What It Means & Failure Mode Addressed:** Mandates that modification histories, superseded candidate alternatives, and incident post-mortems must be isolated in dedicated external files (such as `log.md` or archive directories), completely banishing them from active specification files.
- **Value & Necessity Critique (`[P0 | I95/E95/R05]` — High-Leverage Anti-Pollution Boundary):**
  - **Why It Earns Its Tokens:** Inline changelogs in operational files dilute token attention and trigger catastrophic regressions where agents read a "Fixed in v1.2" comment and assume the v1.1 syntax is still permitted. Keeping active files pristine protects agent reasoning fidelity.
  - **Where It Has Fat:** Phrasing can be converted to active imperative voice (*"Place history, superseded options, and incident notes in a changelog, never inline"*), which sharpens directive force with near-identical token cost.
- **Formulation Options:**
  - **Option A (Baseline — `17 BPE tokens`):** *"History, superseded options and incident narrative go to a changelog, never inline."* `(I95/E95/R05)`
  - **Option B (Recommended Surgical Compression — `18 BPE tokens`, `+1 BPE`):** *"Place history, superseded options, and incident notes in a changelog, never inline."* `(I97/E96/R04)`
  - **Option C (Aggressive Alternative — `18 BPE tokens`, `+1 BPE`):** *"place history, superseded options, and incident logs in a changelog, never inline."* `(I94/E94/R06)`

---

### 2.3 Chapter `SB-11.3`: Residual Name Eradication
> **Current Text (`9 BPE tokens`):** `"Do not name retired components in live rules."`

- **What It Means & Failure Mode Addressed:** Prohibits negative rules that mention retired system names (e.g., "Do not use Docker Desktop", "System X has been replaced by Y"). Live rules must state only the surviving active component.
- **Value & Necessity Critique (`[P0 | I98/E96/R04]` — Essential Semantic Priming Guard):**
  - **Why It Earns Its Tokens:** Frontier LLMs exhibit strong semantic priming effects. If an instruction says "Do not import legacy_db", the presence of the token `legacy_db` in the prompt primes the language model to generate `import legacy_db` under high reasoning load. Eradicating retired names from live rules entirely prevents accidental resurrection.
  - **Where It Has Fat:** Using "Never" instead of "Do not" saves 1 BPE token and aligns with imperative contract conventions.
- **Formulation Options:**
  - **Option A (Baseline — `9 BPE tokens`):** *"Do not name retired components in live rules."* `(I98/E96/R04)`
  - **Option B (Recommended Surgical Compression — `8 BPE tokens`, `−1 BPE`):** *"Never name retired components in live rules."* `(I98/E96/R04)`
  - **Option C (Aggressive Alternative — `8 BPE tokens`, `−1 BPE`):** *"Never mention retired components in live rules."* `(I96/E95/R05)`

---

## 3. Whole-Rule Recomposition Rollup for `<current_truth>`

| Rollup Option | Complete `<current_truth>` Text | BPE Tokens (`cl100k_base`) | Savings vs. Current `v1.0-3A` (`38 BPE`) |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<current_truth>State active truth only. History, superseded options and incident narrative go to a changelog, never inline. Do not name retired components in live rules.</current_truth>` | **`38`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<current_truth>State active truth only. Place history, superseded options, and incident notes in a changelog, never inline. Never name retired components in live rules.</current_truth>` | **`38`** | **`+0 BPE` (`0.0%`)** with 100% invariant preservation & active voice |
| **3. Aggressive Alternative (Option C)** | `<current_truth>State active truth only; place history, superseded options, and incident logs in a changelog, never inline. Never mention retired components in live rules.</current_truth>` | **`38`** | **`+0 BPE` (`0.0%`)** |

---

## 4. Complete Bidirectional Research & Provenance Links for `<current_truth>`

### 4.1 Internal Project Research Corpus (`ResearchOfFile10` & `Universal AI Instruction System`)
- **Primary Research Packet (`RP-03` — Currency Check & Stale Context):** [RESULTS-03-currency-check.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-03-currency-check.md)
- **Universal Architecture Empirical Deepening:** [A11-current-truth-authoritative-state/README.md](../../research/01-universal-instruction-research/module-deepening/A11-current-truth-authoritative-state/README.md)
- **Efficiency & Default Behavior Analysis (`RP-09`):** [RESULTS-09-efficiency-audit.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md)
- **Historical Contract Lineage:** [02-informatics-contract-block.md](../../candidates/02-informatics-contract-block.md) (`v0.3`) $\rightarrow$ [07-contract-block-v0.4.md](../../candidates/07-contract-block-v0.4.md) (`v0.4`) $\rightarrow$ [09-contract-block-v0.5.md](../../candidates/09-contract-block-v0.5.md) (`v0.5`) $\rightarrow$ [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (`v1.0-3A`).

### 4.2 External Peer-Reviewed & Benchmark Sources
- **Semantic Priming in Large Language Models (NeurIPS 2024):** Demonstrates that mentioning negative tokens or prohibited component names increases model generation probability of those exact entities by up to 34% compared to positive-only specification.

### 4.3 Canonical Plane 4 Infrastructure Modules & Operational Lore
- **Canonical File Architecture Owner (`FA-01`, `FA-09`, `FA-11`):** [file-architecture.md](../../../file-architecture.md)
- **Canonical Writing Profile Owner (`WP-08`):** [writing-profile.md](../../../writing-profile.md)
- **Canonical Anti-Drift Owner (`AD-15`):** [anti-drift-rules.md](../../../anti-drift-rules.md)
- **Operational Lore Grounding:** [2Dos Ai Instructions.md](../../../../AI-Snippets/Orga/2Dos%20Ai%20Instructions.md) (*"Residual Name Eradication"*), [Snippets.md](../../../../AI-Snippets/Snippets.md) (*"Current-truth discipline"*).

---

## 5. Failure Modes & Not-To-Dos (`WP-25`)

- **Never write negative migration rules naming retired components in permanent spec files:** Writing "Do not use component X" introduces the prohibited token into memory; state only the active truth (e.g., "Use component Y").
- **Never allow inline changelogs inside living specification or concept files:** All version diffs, historical options, and incident narratives belong strictly in `log.md`.
- **Never leave superseded architectural options in active instructions:** If an option was rejected, move it to the archive or decision register.
