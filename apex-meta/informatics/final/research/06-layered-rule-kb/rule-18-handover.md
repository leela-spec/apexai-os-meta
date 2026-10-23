---
type: Reference
id: V2-LAYERED-KB-RULE-18-HANDOVER
title: Rule 18 Deep-Dive — <handover> Semantic Block Decomposition, Value Audit & Compression Options
description: Decomposing <handover> (from 13-candidate-3A-xml.md) into atomic semantic blocks, evaluating token value against premature handoffs and forensic session transfers, formulating tighter alternatives, and linking all internal and external research.
status: current_truth
tags: [layered-kb, rule-18, handover, semantic-blocks, token-compression, research-ledger]
---

# Rule 18 Deep-Dive: `<handover>` (`13-candidate-3A-xml.md`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (format siblings: [14-candidate-3B-hybrid.md](../../candidates/14-candidate-3B-hybrid.md), [15-candidate-3C-bullet-hybrid.md](../../candidates/15-candidate-3C-bullet-hybrid.md))
> - **Layer 1 (This File — Rule-Level Semantic Block Audit):** Decomposes `<handover>` into 3 atomic semantic blocks (`SB-18.1`..`SB-18.3`), audits token value against premature handoffs, and presents scored compression options.
> - **Layer 2 (Downstream Infrastructure Modules):** [execution-modes.md](../../specs/execution-modes.md) (`EM-09`, `EM-02`), [anti-drift-rules.md](../../specs/anti-drift-rules.md) (`AD-06`).

---

## 1. Original Rule & Atomic Semantic Block Inventory

### 1.1 Current `v1.0-3A` Full Text (`85 BPE block` | `52 BPE inner` | `92 repo tokens` | `368 chars` | `51 words`)

```xml
<handover when="ending a session, delegating to a subagent, or writing any handoff" ref="execution-modes.md">
Never write a handover to defer what you can resolve now. When genuinely needed: what was observed, the reasoning chain, caveats, conclusion, and exact commands to reproduce. Open ref for delegation contracts (input ledger, process, output, DoD).
</handover>
```

### 1.2 Atomic Semantic Block Inventory (Bullet List)

Every token in `<handover>` belongs to one of three distinct semantic blocks (`SB-18.1` through `SB-18.3`), plus the XML gating tag wrapper (`<handover when="..." ref="...">...</handover>`, `33 BPE tokens`):

- **`SB-18.1` — Handover Non-Paralysis Invariant (`13 BPE tokens` | `57 chars`):** *"Never write a handover to defer what you can resolve now."*
- **`SB-18.2` — 5-Component Forensic Report (`23 BPE tokens` | `116 chars`):** *"When genuinely needed: what was observed, the reasoning chain, caveats, conclusion, and exact commands to reproduce."*
- **`SB-18.3` — Delegation Contract Escalation Pointer (`16 BPE tokens` | `71 chars`):** *"Open ref for delegation contracts (input ledger, process, output, DoD)."*

---

## 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

### 2.1 Chapter `SB-18.1`: Handover Non-Paralysis Invariant
> **Current Text (`13 BPE tokens`):** `"Never write a handover to defer what you can resolve now."`

- **What It Means & Failure Mode Addressed:** Strict prohibition on creating a handover report or deferring execution when the active turn's tools can resolve the remaining questions immediately.
- **Value & Necessity Critique (`[P0 | I98/E96/R04]` — Anti-Sloth Gate):**
  - **Honest High-Reasoning Critique:** A major failure mode of autonomous agents is "handover dodging": encountering an error or minor verification task, writing a polite handover saying "the next agent should run the tests", and exiting. If tools can verify it now, the agent must execute it now (`EM-02`, `EM-09`).
  - **Where It Has Fat:** Phrasing can be compressed from *"what you can resolve now"* to *"resolvable work"*, saving 2 BPE tokens.
- **Formulation Options:**
  - **Option A (Baseline — `13 BPE tokens`):** *"Never write a handover to defer what you can resolve now."* `(I98/E96/R04)`
  - **Option B (Recommended Surgical Compression — `11 BPE tokens`, `−2 BPE`):** *"Never write a handover to defer resolvable work."* `(I98/E96/R04)`
  - **Option C (Aggressive Alternative — `11 BPE tokens`, `−2 BPE`):** *"Never write a handover to defer resolvable work."* `(I98/E96/R04)`

---

### 2.2 Chapter `SB-18.2`: 5-Component Forensic Report
> **Current Text (`23 BPE tokens`):** `"When genuinely needed: what was observed, the reasoning chain, caveats, conclusion, and exact commands to reproduce."`

- **What It Means & Failure Mode Addressed:** Codifies the mandatory 5-element forensic structure for every handoff: Observation, Logic Chain, Caveats, Conclusion, and Verification Method.
- **Value & Necessity Critique (`[P0 | I96/E96/R05]` — Forensic Transfer Standard):**
  - **Why It Earns Its Tokens:** Transferred tasks fail when receiving agents must guess why decisions were made or lack the exact commands to verify state. Structuring all handoffs across these five components ensures complete self-containment without interactive overhead (`EM-09`).
  - **Where It Has Fat:** Phrasing can be tightened from *"When genuinely needed: what was observed, the reasoning chain..."* to *"When needed: state observations, reasoning chain..."*, saving 5 BPE tokens.
- **Formulation Options:**
  - **Option A (Baseline — `23 BPE tokens`):** *"When genuinely needed: what was observed, the reasoning chain, caveats, conclusion, and exact commands to reproduce."* `(I96/E96/R05)`
  - **Option B (Recommended Surgical Compression — `18 BPE tokens`, `−5 BPE`):** *"When needed: state observations, reasoning chain, caveats, conclusion, and reproduction commands."* `(I97/E96/R04)`
  - **Option C (Aggressive Alternative — `18 BPE tokens`, `−5 BPE`):** *"When needed: include observation, reasoning chain, caveats, conclusion, and reproduction commands."* `(I95/E95/R05)`

---

### 2.3 Chapter `SB-18.3`: Delegation Contract Escalation Pointer
> **Current Text (`16 BPE tokens`):** `"Open ref for delegation contracts (input ledger, process, output, DoD)."`

- **What It Means & Failure Mode Addressed:** Directs the agent to `execution-modes.md` Adapter 4 (§5.1 4-Dimensional Delegation Contract) when dispatching subagents or delegating work units.
- **Value & Necessity Critique (`[P1 | I92/E94/R06]` — Delegation Integrity):**
  - **Why It Earns Its Tokens:** Preserved from `RP-08`. Subagent delegation without bounded input ledgers and explicit Definition of Done leads to runaway hallucination or task drift.
  - **Where It Has Fat:** At 16 BPE tokens, this pointer names the 4 essential dimensions of delegation contracts.
- **Formulation Options:**
  - **Option A (Baseline — `16 BPE tokens`):** *"Open ref for delegation contracts (input ledger, process, output, DoD)."* `(I92/E94/R06)`
  - **Option B (Recommended Surgical Compression — `16 BPE tokens`, `+0 BPE`):** *"Open ref for delegation contracts (input ledger, process, output, DoD)."* `(I92/E94/R06)`
  - **Option C (Aggressive Alternative — `16 BPE tokens`, `+0 BPE`):** *"Open ref for delegation contracts (input ledger, process, output, DoD)."* `(I92/E94/R06)`

---

## 3. Whole-Rule Recomposition Rollup for `<handover>`

| Rollup Option | Complete `<handover>` Text | BPE Tokens (`cl100k_base`) | Savings vs. Current `v1.0-3A` (`85 BPE`) |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<handover when="ending a session, delegating to a subagent, or writing any handoff" ref="execution-modes.md"> Never write a handover to defer what you can resolve now. When genuinely needed: what was observed, the reasoning chain, caveats, conclusion, and exact commands to reproduce. Open ref for delegation contracts (input ledger, process, output, DoD). </handover>` | **`85`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<handover when="ending a session, delegating to a subagent, or writing any handoff" ref="execution-modes.md"> Never write a handover to defer resolvable work. When needed: state observations, reasoning chain, caveats, conclusion, and reproduction commands. Open ref for delegation contracts (input ledger, process, output, DoD). </handover>` | **`78`** | **`−7 BPE` (`−8.2%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<handover when="ending a session, delegating to a subagent, or writing any handoff" ref="execution-modes.md"> Never write a handover to defer resolvable work. When needed: include observation, reasoning chain, caveats, conclusion, and reproduction commands. Open ref for delegation contracts (input ledger, process, output, DoD). </handover>` | **`78`** | **`−7 BPE` (`−8.2%`)** |

---

## 4. Complete Bidirectional Research & Provenance Links for `<handover>`

### 4.1 Internal Project Research Corpus (`ResearchOfFile10` & `Universal AI Instruction System`)
- **Primary Research Packet (`RP-08` — Escalation Cue Recovery & Delegation Schemas):** [RESULTS-08-deepen-when-mechanics.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-08-deepen-when-mechanics.md)
- **Empirical Deepening on Evidence Integrity:** [A08-evidence-integrity-uncertainty-calibration/README.md](../../research/01-universal-instruction-research/module-deepening/A08-evidence-integrity-uncertainty-calibration/README.md)
- **Error Recovery & Delegation Protocols:** [A10-error-recovery-escalation/README.md](../../research/01-universal-instruction-research/module-deepening/A10-error-recovery-escalation/README.md)
- **Cross-Packet Synthesis:** [RESULTS-11-synthesis.md](../../research/03-research-of-file-10/RESULTS-11-synthesis.md)
- **Historical Contract Lineage:** [02-informatics-contract-block.md](../../candidates/02-informatics-contract-block.md) (`v0.3`) $\rightarrow$ [07-contract-block-v0.4.md](../../candidates/07-contract-block-v0.4.md) (`v0.4`) $\rightarrow$ [09-contract-block-v0.5.md](../../candidates/09-contract-block-v0.5.md) (`v0.5`) $\rightarrow$ [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (`v1.0-3A`).

### 4.2 External Peer-Reviewed & Benchmark Sources
- **Teamwork Communication & Handoff Protocols (Antigravity 2026):** 5-Component forensic report structure (Observation, Logic Chain, Caveats, Conclusion, Verification Method).
- **Patterson, E. S., et al. (2004):** *Handoff strategies in high-risk domains* — Systematic communication transfer minimizing loss of critical situational awareness.

### 4.3 Canonical Plane 4 Infrastructure Modules & Operational Lore
- **Canonical Execution Modes Owner (`EM-09`, `EM-02`):** [execution-modes.md](../../specs/execution-modes.md)
- **Canonical Anti-Drift Owner (`AD-06`):** [anti-drift-rules.md](../../specs/anti-drift-rules.md)
- **Operational Lore Grounding:** [2Dos Ai Instructions.md](../../../../AI-Snippets/Orga/2Dos%20Ai%20Instructions.md) (*"5-Component Handoff Report"*), [Snippets.md](../../../../AI-Snippets/Snippets.md) (*"Handover Non-Paralysis"*).

---

## 5. Failure Modes & Not-To-Dos (`WP-25`)

- **Never write a handover report to defer questions or tasks that active tools in the current turn can directly answer:** Verify and complete resolvable work immediately.
- **Never omit reproduction and verification commands from Section 5 of the handover report:** Handoffs must provide deterministic, independently executable verification commands.
- **Never delegate to a subagent without an explicit 4-dimensional contract (Input Priority Ledger, Process Constraints, Output Contract, DoD):** Prevent unstructured subagent drift.
