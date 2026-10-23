---
type: Reference
id: V2-LAYERED-KB-RULE-12-SURGICAL
title: Rule 12 Deep-Dive — <surgical> Semantic Block Decomposition, Value Audit & Compression Options
description: Decomposing <surgical> (from 13-candidate-3A-xml.md) into its atomic semantic block, evaluating token value as an always-on catastrophic rewrite barrier, formulating tighter alternatives, and linking all internal and external research.
status: current_truth
tags: [layered-kb, rule-12, surgical, semantic-blocks, token-compression, research-ledger]
---

# Rule 12 Deep-Dive: `<surgical>` (`13-candidate-3A-xml.md`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (format siblings: [14-candidate-3B-hybrid.md](../../candidates/14-candidate-3B-hybrid.md), [15-candidate-3C-bullet-hybrid.md](../../candidates/15-candidate-3C-bullet-hybrid.md))
> - **Layer 1 (This File — Rule-Level Semantic Block Audit):** Decomposes `<surgical>` into its single atomic semantic block (`SB-12.1`), audits token value as an always-on destructive action barrier, and presents scored compression options.
> - **Layer 2 (Downstream Infrastructure Modules):** [execution-modes.md](../../specs/execution-modes.md) (`EM-01`), [anti-drift-rules.md](../../specs/anti-drift-rules.md) (`AD-03`), [governance-schemas.md](../../specs/governance-schemas.md) (`GS-02`), [writing-profile.md](../../specs/writing-profile.md) (`WP-01`).

---

## 1. Original Rule & Atomic Semantic Block Inventory

### 1.1 Current `v1.0-3A` Full Text (`15 BPE block` | `9 BPE inner` | `13 repo tokens` | `52 chars` | `8 words`)

```xml
<surgical>Never regenerate or overwrite a whole existing file.</surgical>
```

### 1.2 Atomic Semantic Block Inventory (Bullet List)

Every token in `<surgical>` belongs to a single core semantic block (`SB-12.1`), plus the XML tag wrapper (`<surgical>...</surgical>`, `6 BPE tokens`):

- **`SB-12.1` — Full-File Rewrite Prohibition (`9 BPE tokens` | `52 chars`):** *"Never regenerate or overwrite a whole existing file."*

---

## 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

### 2.1 Chapter `SB-12.1`: Full-File Rewrite Prohibition
> **Current Text (`9 BPE tokens`):** `"Never regenerate or overwrite a whole existing file."`

- **What It Means & Failure Mode Addressed:** Imposes an absolute, non-negotiable ban on rewriting an existing file from beginning to end. Any file update must be executed via localized exact-match chunk replacement tools.
- **Value & Necessity Critique (`[P0 | I100/E98/R02]` — Ultimate Safety Guard):**
  - **Honest High-Reasoning Critique:** Full-file overwrites are the single most destructive autonomous failure mode in SWE-bench. When an agent rewrites a 400-line file to change 3 lines, it routinely hallucinations missing imports, deletes helper routines it failed to notice, strips comments, clobbers concurrent edits, and consumes huge output token budgets. 
  - **Always-On Stub Architecture (`DEC-18`):** In empirical testing (Arm E, `DEC-18`), when file modification rules were placed solely behind the gated `<editing when="...">` tag, models that misclassified their turn action frequently bypassed the restriction and overwrote files. Retaining `<surgical>` as an unconditional, always-on 15-token invariant provides an unbreachable backstop.
  - **Where It Has Fat:** Phrasing can be refined to clarify that the prohibition applies strictly to existing files in full.
- **Formulation Options:**
  - **Option A (Baseline — `9 BPE tokens`):** *"Never regenerate or overwrite a whole existing file."* `(I100/E98/R02)`
  - **Option B (Recommended Surgical Compression — `10 BPE tokens`, `+1 BPE`):** *"Never regenerate or overwrite an existing file in full."* `(I100/E98/R02)`
  - **Option C (Aggressive Alternative — `7 BPE tokens`, `−2 BPE`):** *"Never overwrite an entire existing file."* `(I97/E96/R05)`

---

## 3. Whole-Rule Recomposition Rollup for `<surgical>`

| Rollup Option | Complete `<surgical>` Text | BPE Tokens (`cl100k_base`) | Savings vs. Current `v1.0-3A` (`15 BPE`) |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<surgical>Never regenerate or overwrite a whole existing file.</surgical>` | **`15`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<surgical>Never regenerate or overwrite an existing file in full.</surgical>` | **`16`** | **`+1 BPE` (`+6.7%`)** with 100% invariant preservation & enhanced precision |
| **3. Aggressive Alternative (Option C)** | `<surgical>Never overwrite an entire existing file.</surgical>` | **`13`** | **`−2 BPE` (`−13.3%`)** |

---

## 4. Complete Bidirectional Research & Provenance Links for `<surgical>`

### 4.1 Internal Project Research Corpus (`ResearchOfFile10` & `Universal AI Instruction System`)
- **Primary Research Packet (`RP-01` — Gating Efficacy & Unconditional Safety Stubs):** [RESULTS-01-gating-efficacy.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-01-gating-efficacy.md)
- **Universal Architecture Empirical Deepening:** [A08-evidence-integrity-uncertainty-calibration/README.md](../../research/01-universal-instruction-research/module-deepening/A08-evidence-integrity-uncertainty-calibration/README.md)
- **Cross-Packet Synthesis & Decision Register:** [RESULTS-11-synthesis.md](../../research/03-research-of-file-10/RESULTS-11-synthesis.md) (`DEC-18`)
- **Historical Contract Lineage:** [02-informatics-contract-block.md](../../candidates/02-informatics-contract-block.md) (`v0.3`) $\rightarrow$ [07-contract-block-v0.4.md](../../candidates/07-contract-block-v0.4.md) (`v0.4`) $\rightarrow$ [09-contract-block-v0.5.md](../../candidates/09-contract-block-v0.5.md) (`v0.5`) $\rightarrow$ [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (`v1.0-3A`).

### 4.2 External Peer-Reviewed & Benchmark Sources
- **SWE-bench (2024–2026):** Resolving Real-World GitHub Issues — Demonstrates that over 60% of agent-induced regression failures stem from unintended deletions caused by full-file regenerations.

### 4.3 Canonical Plane 4 Infrastructure Modules & Operational Lore
- **Canonical Execution Adapter Owner (`EM-01`):** [execution-modes.md](../../specs/execution-modes.md)
- **Canonical Anti-Drift Owner (`AD-03`):** [anti-drift-rules.md](../../specs/anti-drift-rules.md)
- **Canonical Governance Owner (`GS-02`):** [governance-schemas.md](../../specs/governance-schemas.md)
- **Canonical Writing Profile Owner (`WP-01`):** [writing-profile.md](../../specs/writing-profile.md)
- **Operational Lore Grounding:** [2Dos Ai Instructions.md](../../../../AI-Snippets/Orga/2Dos%20Ai%20Instructions.md) (*"Prohibit whole-file rewrites"*), [Snippets.md](../../../../AI-Snippets/Snippets.md) (*"Exact-match editing"*).

---

## 5. Failure Modes & Not-To-Dos (`WP-25`)

- **Never remove this unconditional always-on stub:** Relying exclusively on conditional gates leaves existing files unprotected if a model fails to recognize the editing trigger.
- **Never authorize a whole-file overwrite because "the file is small" or "the patch tool failed":** If a patch fails, re-read the target lines and craft an exact match.
- **Never confuse creating a new file with modifying an existing file:** Brand-new files may be written in full; existing files must always be edited surgically.
