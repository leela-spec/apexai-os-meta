---
type: Reference
id: V2-LAYERED-KB-RULE-13-EDITING
title: Rule 13 Deep-Dive — <editing> Semantic Block Decomposition, Value Audit & Compression Options
description: Decomposing <editing> (from 13-candidate-3A-xml.md) into atomic semantic blocks, evaluating token value for exact-match patching, file relocation, and JIT escalation, formulating tighter alternatives, and linking all internal and external research.
status: current_truth
tags: [layered-kb, rule-13, editing, semantic-blocks, token-compression, research-ledger]
---

# Rule 13 Deep-Dive: `<editing>` (`13-candidate-3A-xml.md`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (format siblings: [14-candidate-3B-hybrid.md](../../candidates/14-candidate-3B-hybrid.md), [15-candidate-3C-bullet-hybrid.md](../../candidates/15-candidate-3C-bullet-hybrid.md))
> - **Layer 1 (This File — Rule-Level Semantic Block Audit):** Decomposes `<editing>` into 4 atomic semantic blocks (`SB-13.1`..`SB-13.4`), audits token value across exact-match patch disciplines and JIT triggers, and presents scored compression options.
> - **Layer 2 (Downstream Infrastructure Modules):** [execution-modes.md](../../../execution-modes.md) (`EM-01`, `EM-08`), [anti-drift-rules.md](../../../anti-drift-rules.md) (`AD-23`), [governance-schemas.md](../../../governance-schemas.md) (`GS-09`..`GS-11`), [writing-profile.md](../../../writing-profile.md) (`WP-01`).

---

## 1. Original Rule & Atomic Semantic Block Inventory

### 1.1 Current `v1.0-3A` Full Text (`75 BPE block` | `50 BPE inner` | `59 repo tokens` | `239 chars` | `40 words`)

```xml
<editing when="changing, moving or deleting a file that already exists" ref="execution-modes.md">
Replace only the exact lines that must change, copied character-for-character from the file you just read. One change per edit. Move or copy with git mv or cp, never by rewriting contents. Open ref for AST patches or multi-block executors.
</editing>
```

### 1.2 Atomic Semantic Block Inventory (Bullet List)

Every token in `<editing>` belongs to one of four distinct semantic blocks (`SB-13.1` through `SB-13.4`), plus the XML gating tag wrapper (`<editing when="..." ref="...">...</editing>`, `25 BPE tokens`):

- **`SB-13.1` — Exact-Match Replacement Discipline (`20 BPE tokens` | `106 chars`):** *"Replace only the exact lines that must change, copied character-for-character from the file you just read."*
- **`SB-13.2` — Atomic Single-Operation Edit (`5 BPE tokens` | `20 chars`):** *"One change per edit."*
- **`SB-13.3` — Deterministic File Movement (`14 BPE tokens` | `60 chars`):** *"Move or copy with git mv or cp, never by rewriting contents."*
- **`SB-13.4` — Second-Threshold Escalation Trigger (`11 BPE tokens` | `50 chars`):** *"Open ref for AST patches or multi-block executors."*

---

## 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

### 2.1 Chapter `SB-13.1`: Exact-Match Replacement Discipline
> **Current Text (`20 BPE tokens`):** `"Replace only the exact lines that must change, copied character-for-character from the file you just read."`

- **What It Means & Failure Mode Addressed:** Requires that target modification chunks be copied verbatim from freshly inspected files rather than reconstructed from memory. It prevents patch matching failures caused by whitespace hallucination, quotation style mismatches, or line ending discrepancies.
- **Value & Necessity Critique (`[P0 | I98/E96/R05]` — Anti-Hallucination Tool Discipline):**
  - **Honest High-Reasoning Critique:** When coding agents execute patch tools (e.g., `replace_file_content`), they frequently fail because they guess indentation or minor punctuation from conversational memory. Commanding character-for-character reproduction from live text eliminates match failures.
  - **Where It Has Fat:** Phrasing can be tightened from *"the file you just read"* to *"live text"*, saving 8 BPE tokens while maintaining total invariant strength.
- **Formulation Options:**
  - **Option A (Baseline — `20 BPE tokens`):** *"Replace only the exact lines that must change, copied character-for-character from the file you just read."* `(I98/E96/R05)`
  - **Option B (Recommended Surgical Compression — `12 BPE tokens`, `−8 BPE`):** *"Replace only exact lines copied character-for-character from live text."* `(I98/E96/R04)`
  - **Option C (Aggressive Alternative — `12 BPE tokens`, `−8 BPE`):** *"Replace only exact lines copied character-for-character from live text;"* `(I96/E95/R05)`

---

### 2.2 Chapter `SB-13.2`: Atomic Single-Operation Edit
> **Current Text (`5 BPE tokens`):** `"One change per edit."`

- **What It Means & Failure Mode Addressed:** Forbids attempting multi-location edits in a single unverified call. Each edit must be atomic and verified independently.
- **Value & Necessity Critique (`[P1 | I92/E94/R06]` — Failure Isolation Discipline):**
  - **Why It Earns Its Tokens:** Multi-edit operations frequently fail midway through a file, leaving the file in an inconsistent state where subsequent line numbers are offset and rollback is complicated. Atomic editing isolates defects.
  - **Where It Has Fat:** At 5 BPE tokens, this directive is already optimal.
- **Formulation Options:**
  - **Option A (Baseline — `5 BPE tokens`):** *"One change per edit."* `(I92/E94/R06)`
  - **Option B (Recommended Surgical Compression — `5 BPE tokens`, `+0 BPE`):** *"One change per edit."* `(I92/E94/R06)`
  - **Option C (Aggressive Alternative — `5 BPE tokens`, `+0 BPE`):** *"one change per edit."* `(I90/E92/R08)`

---

### 2.3 Chapter `SB-13.3`: Deterministic File Movement
> **Current Text (`14 BPE tokens`):** `"Move or copy with git mv or cp, never by rewriting contents."`

- **What It Means & Failure Mode Addressed:** Mandates that file renames, directory moves, or duplications use native shell commands (`git mv`, `cp`) rather than reading the entire source file and writing it into a new target path.
- **Value & Necessity Critique (`[P1 | I92/E94/R06]` — History & Token Efficiency Guard):**
  - **Why It Earns Its Tokens:** Autonomous agents often move files by reading 500 lines into prompt memory and then invoking `write_to_file`. This destroys git rename tracking, bloats context, and risks truncation defects.
  - **Where It Has Fat:** Changing "with" to "via" maintains crisp precision.
- **Formulation Options:**
  - **Option A (Baseline — `14 BPE tokens`):** *"Move or copy with git mv or cp, never by rewriting contents."* `(I92/E94/R06)`
  - **Option B (Recommended Surgical Compression — `14 BPE tokens`, `+0 BPE`):** *"Move or copy via git mv or cp, never by rewriting contents."* `(I93/E94/R05)`
  - **Option C (Aggressive Alternative — `9 BPE tokens`, `−5 BPE`):** *"Move or copy via git mv or cp."* `(I88/E90/R12)`

---

### 2.4 Chapter `SB-13.4`: Second-Threshold Escalation Trigger
> **Current Text (`11 BPE tokens`):** `"Open ref for AST patches or multi-block executors."`

- **What It Means & Failure Mode Addressed:** Instructs the model that the referenced file (`execution-modes.md`) is only to be loaded when performing structured AST patches or complex multi-block operations, not for routine string replacements.
- **Value & Necessity Critique (`[P1 | I90/E92/R08]` — Context Gate Enforcement):**
  - **Why It Earns Its Tokens:** Following the removal of `deepen_when` in `DEC-23`, inline escalation triggers prevent agents from eagerly reading deep specification modules on every routine 1-line edit.
  - **Where It Has Fat:** Phrasing is already compact and clear.
- **Formulation Options:**
  - **Option A (Baseline — `11 BPE tokens`):** *"Open ref for AST patches or multi-block executors."* `(I90/E92/R08)`
  - **Option B (Recommended Surgical Compression — `11 BPE tokens`, `+0 BPE`):** *"Open ref for AST patches or multi-block executors."* `(I90/E92/R08)`
  - **Option C (Aggressive Alternative — `11 BPE tokens`, `+0 BPE`):** *"Open ref for AST patches or multi-block executors."* `(I90/E92/R08)`

---

## 3. Whole-Rule Recomposition Rollup for `<editing>`

| Rollup Option | Complete `<editing>` Text | BPE Tokens (`cl100k_base`) | Savings vs. Current `v1.0-3A` (`75 BPE`) |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<editing when="changing, moving or deleting a file that already exists" ref="execution-modes.md"> Replace only the exact lines that must change, copied character-for-character from the file you just read. One change per edit. Move or copy with git mv or cp, never by rewriting contents. Open ref for AST patches or multi-block executors. </editing>` | **`75`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<editing when="changing, moving or deleting a file that already exists" ref="execution-modes.md"> Replace only exact lines copied character-for-character from live text. One change per edit. Move or copy via git mv or cp, never by rewriting contents. Open ref for AST patches or multi-block executors. </editing>` | **`67`** | **`−8 BPE` (`−10.7%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<editing when="changing, moving or deleting a file that already exists" ref="execution-modes.md"> Replace only exact lines copied character-for-character from live text; one change per edit. Move or copy via git mv or cp. Open ref for AST patches or multi-block executors. </editing>` | **`62`** | **`−13 BPE` (`−17.3%`)** |

---

## 4. Complete Bidirectional Research & Provenance Links for `<editing>`

### 4.1 Internal Project Research Corpus (`ResearchOfFile10` & `Universal AI Instruction System`)
- **Primary Research Packet (`RP-01` — Gating Efficacy):** [RESULTS-01-gating-efficacy.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-01-gating-efficacy.md)
- **Deepening Removal & Escalation Architecture (`RP-08`):** [RESULTS-08-deepen-when-mechanics.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-08-deepen-when-mechanics.md)
- **Universal Architecture Empirical Deepening:** [A08-evidence-integrity-uncertainty-calibration/README.md](../../research/01-universal-instruction-research/module-deepening/A08-evidence-integrity-uncertainty-calibration/README.md)
- **Cross-Packet Synthesis:** [RESULTS-11-synthesis.md](../../research/03-research-of-file-10/RESULTS-11-synthesis.md) (`DEC-23`)
- **Historical Contract Lineage:** [02-informatics-contract-block.md](../../candidates/02-informatics-contract-block.md) (`v0.3`) $\rightarrow$ [07-contract-block-v0.4.md](../../candidates/07-contract-block-v0.4.md) (`v0.4`) $\rightarrow$ [09-contract-block-v0.5.md](../../candidates/09-contract-block-v0.5.md) (`v0.5`) $\rightarrow$ [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (`v1.0-3A`).

### 4.2 External Peer-Reviewed & Benchmark Sources
- **Gloaguen et al. (2026):** [Evaluation of Gated Agent Prompts](https://arxiv.org/abs/2602.11988) — Demonstrates that conditional prompt gating suppresses token overhead while second-threshold cues effectively prevent premature documentation loading.

### 4.3 Canonical Plane 4 Infrastructure Modules & Operational Lore
- **Canonical Execution Adapter Owner (`EM-01`, `EM-08`):** [execution-modes.md](../../../execution-modes.md)
- **Canonical Anti-Drift Owner (`AD-23`):** [anti-drift-rules.md](../../../anti-drift-rules.md)
- **Canonical Governance Owner (`GS-09`, `GS-10`, `GS-11`):** [governance-schemas.md](../../../governance-schemas.md)
- **Canonical Writing Profile Owner (`WP-01`):** [writing-profile.md](../../../writing-profile.md)
- **Operational Lore Grounding:** [2Dos Ai Instructions.md](../../../../AI-Snippets/Orga/2Dos%20Ai%20Instructions.md) (*"Deterministic file movement"*), [Snippets.md](../../../../AI-Snippets/Snippets.md) (*"Exact-match editing"*).

---

## 5. Failure Modes & Not-To-Dos (`WP-25`)

- **Never omit "copied character-for-character from live text":** Removing this constraint causes models to reconstruct target blocks from memory, producing whitespace mismatches and tool failures.
- **Never allow multi-block edits without individual verification:** If a patch fails in a multi-edit bundle, the entire file state becomes ungrounded.
- **Never open `execution-modes.md` for simple single-line replacements:** Only open the reference when authoring formal AST patch intents or complex scripts.
