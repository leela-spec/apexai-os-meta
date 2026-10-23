---
type: Reference
id: V2-LAYERED-KB-RULE-21-SYNC
title: Rule 21 Deep-Dive — <sync> Semantic Block Decomposition, Value Audit & Compression Options
description: Decomposing <sync> (from 13-candidate-3A-xml.md) into atomic semantic blocks, evaluating token value against repository over-analysis and accidental file loss, formulating tighter alternatives, and linking all internal and external research.
status: current_truth
tags: [layered-kb, rule-21, sync, semantic-blocks, token-compression, research-ledger]
---

# Rule 21 Deep-Dive: `<sync>` (`13-candidate-3A-xml.md`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (format siblings: [14-candidate-3B-hybrid.md](../../candidates/14-candidate-3B-hybrid.md), [15-candidate-3C-bullet-hybrid.md](../../candidates/15-candidate-3C-bullet-hybrid.md))
> - **Layer 1 (This File — Rule-Level Semantic Block Audit):** Decomposes `<sync>` into 3 atomic semantic blocks (`SB-21.1`..`SB-21.3`), audits token value against repository over-analysis, and presents scored compression options.
> - **Layer 2 (Downstream Infrastructure Modules):** [execution-modes.md](../../../execution-modes.md) (`EM-12`), [anti-drift-rules.md](../../../anti-drift-rules.md) (`AD-23`).

---

## 1. Original Rule & Atomic Semantic Block Inventory

### 1.1 Current `v1.0-3A` Full Text (`53 BPE block` | `36 BPE inner` | `63 repo tokens` | `253 chars` | `37 words`)

```xml
<sync when="the operator asks to sync, commit or push">
Run the git commands first, not repository analysis. Preserve every file: commit unrelated dirty files separately rather than dropping them. On non-fast-forward, pull with rebase and retry.
</sync>
```

### 1.2 Atomic Semantic Block Inventory (Bullet List)

Every token in `<sync>` belongs to one of three distinct semantic blocks (`SB-21.1` through `SB-21.3`), plus the XML gating tag wrapper (`<sync when="...">...</sync>`, `17 BPE tokens`):

- **`SB-21.1` — Git Command Primacy (`10 BPE tokens` | `52 chars`):** *"Run the git commands first, not repository analysis."*
- **`SB-21.2` — Asset Preservation Invariant (`15 BPE tokens` | `87 chars`):** *"Preserve every file: commit unrelated dirty files separately rather than dropping them."*
- **`SB-21.3` — Rebase Retry Protocol (`12 BPE tokens` | `48 chars`):** *"On non-fast-forward, pull with rebase and retry."*

---

## 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

### 2.1 Chapter `SB-21.1`: Git Command Primacy
> **Current Text (`10 BPE tokens`):** `"Run the git commands first, not repository analysis."`

- **What It Means & Failure Mode Addressed:** Directs the agent to execute git sync operations (`git add`, `git commit`, `git push`) immediately without initiating unprompted multi-file repository audits or git diff analyses.
- **Value & Necessity Critique (`[P0 | I96/E96/R05]` — Git Dispatch Primacy):**
  - **Honest High-Reasoning Critique:** Coding agents frequently procrastinate when instructed to push: they run recursive status scans, inspect untracked files, or analyze working tree history across 3–4 conversational turns instead of running the requested git command. Executing git commands first preserves operational tempo (`EM-12`).
  - **Where It Has Fat:** Phrasing can be tightened from *"Run the git commands first, not repository analysis"* to *"Execute git commands immediately, not repo analysis"*, saving 1 BPE token.
- **Formulation Options:**
  - **Option A (Baseline — `10 BPE tokens`):** *"Run the git commands first, not repository analysis."* `(I96/E96/R05)`
  - **Option B (Recommended Surgical Compression — `9 BPE tokens`, `−1 BPE`):** *"Execute git commands immediately, not repo analysis."* `(I97/E96/R04)`
  - **Option C (Aggressive Alternative — `8 BPE tokens`, `−2 BPE`):** *"Run git commands immediately without repo analysis."* `(I95/E95/R05)`

---

### 2.2 Chapter `SB-21.2`: Asset Preservation Invariant
> **Current Text (`15 BPE tokens`):** `"Preserve every file: commit unrelated dirty files separately rather than dropping them."`

- **What It Means & Failure Mode Addressed:** Strict data-safety boundary: forbids discarding, reverting, or stashing uncommitted files; unrelated changes must be committed separately or preserved intact.
- **Value & Necessity Critique (`[P0 | I98/E96/R04]` — Data Loss Prevention):**
  - **Why It Earns Its Tokens:** A notorious defect in autonomous coding tools is running `git checkout -- .` or `git clean -fd` to produce a clean working tree for a push, silently deleting hours of user work. Forcing absolute file preservation stops destructive tree resets (`EM-12`, `AD-23`).
  - **Where It Has Fat:** Phrasing is already compact; changing "every file" to "all files" maintains exact token count while reinforcing plural scope.
- **Formulation Options:**
  - **Option A (Baseline — `15 BPE tokens`):** *"Preserve every file: commit unrelated dirty files separately rather than dropping them."* `(I98/E96/R04)`
  - **Option B (Recommended Surgical Compression — `15 BPE tokens`, `+0 BPE`):** *"Preserve all files: commit unrelated dirty files separately rather than dropping them."* `(I98/E96/R04)`
  - **Option C (Aggressive Alternative — `15 BPE tokens`, `+0 BPE`):** *"Preserve all files: commit unrelated dirty files separately instead of dropping them."* `(I98/E96/R04)`

---

### 2.3 Chapter `SB-21.3`: Rebase Retry Protocol
> **Current Text (`12 BPE tokens`):** `"On non-fast-forward, pull with rebase and retry."`

- **What It Means & Failure Mode Addressed:** Standard conflict-recovery routine for rejected pushes: automatically run `git pull --rebase` and retry the push without manual operator escalation.
- **Value & Necessity Critique (`[P1 | I92/E94/R06]` — Autonomous Integration):**
  - **Why It Earns Its Tokens:** Prevents unnecessary agent halts when a remote repository moved ahead during the turn. Rebase retry integrates remote commits cleanly without generating messy merge bubbles.
  - **Where It Has Fat:** At 12 BPE tokens, this instruction is concise and operational.
- **Formulation Options:**
  - **Option A (Baseline — `12 BPE tokens`):** *"On non-fast-forward, pull with rebase and retry."* `(I92/E94/R06)`
  - **Option B (Recommended Surgical Compression — `12 BPE tokens`, `+0 BPE`):** *"On non-fast-forward, pull with rebase and retry."* `(I92/E94/R06)`
  - **Option C (Aggressive Alternative — `12 BPE tokens`, `+0 BPE`):** *"On non-fast-forward, pull --rebase and retry."* `(I92/E94/R06)`

---

## 3. Whole-Rule Recomposition Rollup for `<sync>`

| Rollup Option | Complete `<sync>` Text | BPE Tokens (`cl100k_base`) | Savings vs. Current `v1.0-3A` (`53 BPE`) |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<sync when="the operator asks to sync, commit or push"> Run the git commands first, not repository analysis. Preserve every file: commit unrelated dirty files separately rather than dropping them. On non-fast-forward, pull with rebase and retry. </sync>` | **`53`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<sync when="the operator asks to sync, commit or push"> Execute git commands immediately, not repo analysis. Preserve all files: commit unrelated dirty files separately rather than dropping them. On non-fast-forward, pull with rebase and retry. </sync>` | **`52`** | **`−1 BPE` (`−1.9%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<sync when="the operator asks to sync, commit or push"> Run git commands immediately without repo analysis. Preserve all files: commit unrelated dirty files separately instead of dropping them. On non-fast-forward, pull --rebase and retry. </sync>` | **`51`** | **`−2 BPE` (`−3.8%`)** |

---

## 4. Complete Bidirectional Research & Provenance Links for `<sync>`

### 4.1 Internal Project Research Corpus (`ResearchOfFile10` & `Universal AI Instruction System`)
- **Primary Research Packet (`RP-10` — Surface Layering & CLI Dispatch Deduplication):** [RESULTS-10-surface-layering.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-10-surface-layering.md)
- **Efficiency & Default Behavior Analysis (`RP-09`):** [RESULTS-09-efficiency-audit.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md)
- **Universal Architecture Empirical Deepening:** [A10-error-recovery-escalation/README.md](../../research/01-universal-instruction-research/module-deepening/A10-error-recovery-escalation/README.md)
- **Cross-Packet Synthesis:** [RESULTS-11-synthesis.md](../../research/03-research-of-file-10/RESULTS-11-synthesis.md)
- **Historical Contract Lineage:** [02-informatics-contract-block.md](../../candidates/02-informatics-contract-block.md) (`v0.3`) $\rightarrow$ [07-contract-block-v0.4.md](../../candidates/07-contract-block-v0.4.md) (`v0.4`) $\rightarrow$ [09-contract-block-v0.5.md](../../candidates/09-contract-block-v0.5.md) (`v0.5`) $\rightarrow$ [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (`v1.0-3A`).

### 4.2 External Peer-Reviewed & Benchmark Sources
- **Chacon, S., & Straub, B. (2014):** *Pro Git* (2nd Edition, Apress) — Non-fast-forward integration, linear rebase workflows, and working tree preservation.
- **SWE-bench (2024):** Evaluating coding agents on repository maintenance and git commit hygiene.

### 4.3 Canonical Plane 4 Infrastructure Modules & Operational Lore
- **Canonical Execution Modes Owner (`EM-12`):** [execution-modes.md](../../../execution-modes.md)
- **Canonical Anti-Drift Owner (`AD-23`):** [anti-drift-rules.md](../../../anti-drift-rules.md)
- **Operational Lore Grounding:** [2Dos.md](../../../../AI-Snippets/Orga/2Dos.md) (*"Git Dispatch Primacy"*), [Snippets.md](../../../../AI-Snippets/Snippets.md) (*"Asset Preservation & Deterministic Moves"*).

---

## 5. Failure Modes & Not-To-Dos (`WP-25`)

- **Never execute destructive git cleanup commands (`git checkout -- .`, `git clean -fd`, `git reset --hard`):** Preserve every file on disk.
- **Never enter multi-turn repository audits when the operator prompt is a simple sync or push request:** Execute the git command immediately.
- **Never drop or discard uncommitted changes belonging to adjacent tasks:** Commit them separately if a clean tree is required.
