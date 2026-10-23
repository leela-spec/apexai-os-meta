---
type: Reference
id: V2-LAYERED-KB-RULE-14-NEW-MACHINERY
title: Rule 14 Deep-Dive — <new_machinery> Semantic Block Decomposition, Value Audit & Compression Options
description: Decomposing <new_machinery> (from 13-candidate-3A-xml.md) into atomic semantic blocks, evaluating token value against speculative scaffolding and over-building biases, formulating tighter alternatives, and linking all internal and external research.
status: current_truth
tags: [layered-kb, rule-14, new-machinery, semantic-blocks, token-compression, research-ledger]
---

# Rule 14 Deep-Dive: `<new_machinery>` (`13-candidate-3A-xml.md`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (format siblings: [14-candidate-3B-hybrid.md](../../candidates/14-candidate-3B-hybrid.md), [15-candidate-3C-bullet-hybrid.md](../../candidates/15-candidate-3C-bullet-hybrid.md))
> - **Layer 1 (This File — Rule-Level Semantic Block Audit):** Decomposes `<new_machinery>` into 3 atomic semantic blocks (`SB-14.1`..`SB-14.3`), audits token value against speculative scaffolding, and presents scored compression options.
> - **Layer 2 (Downstream Infrastructure Modules):** [anti-drift-rules.md](../../../anti-drift-rules.md) (`AD-25`, `AD-10`, `AD-13`), [writing-profile.md](../../../writing-profile.md) (`WP-01`).

---

## 1. Original Rule & Atomic Semantic Block Inventory

### 1.1 Current `v1.0-3A` Full Text (`70 BPE block` | `43 BPE inner` | `54 repo tokens` | `216 chars` | `36 words`)

```xml
<new_machinery when="about to add a script, test, gate, schema, wrapper or abstraction">
Name the exact requirement, blocker or material risk it serves first; if ordinary use surfaces the problem in ~2 steps, fix the data or logic instead. Do not build more verification machinery than the risk justifies.
</new_machinery>
```

### 1.2 Atomic Semantic Block Inventory (Bullet List)

Every token in `<new_machinery>` belongs to one of three distinct semantic blocks (`SB-14.1` through `SB-14.3`), plus the XML gating tag wrapper (`<new_machinery when="...">...</new_machinery>`, `27 BPE tokens`):

- **`SB-14.1` — Pre-Addition Blocker Mandate (`13 BPE tokens` | `69 chars`):** *"Name the exact requirement, blocker or material risk it serves first;"*
- **`SB-14.2` — 2-Step Visibility Threshold (`18 BPE tokens` | `80 chars`):** *"if ordinary use surfaces the problem in ~2 steps, fix the data or logic instead."*
- **`SB-14.3` — Machinery Proportionality Invariant (`12 BPE tokens` | `65 chars`):** *"Do not build more verification machinery than the risk justifies."*

---

## 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

### 2.1 Chapter `SB-14.1`: Pre-Addition Blocker Mandate
> **Current Text (`13 BPE tokens`):** `"Name the exact requirement, blocker or material risk it serves first;"`

- **What It Means & Failure Mode Addressed:** Requires the agent to explicitly state the requirement, blocker, or material risk being addressed before creating any new script, test suite, gate, schema, or wrapper.
- **Value & Necessity Critique (`[P0 | I95/E95/R06]` — Anti-Action-Bias Gate):**
  - **Honest High-Reasoning Critique:** Frontier coding agents possess an intense action bias toward constructing helper scripts, abstraction classes, and test harnesses for hypothetical needs. Mandating an explicit pre-action justification eliminates speculative scaffolding.
  - **Where It Has Fat:** Phrasing can be sharpened by replacing "serves" with "resolves" and capitalizing the clause for sentence independence.
- **Formulation Options:**
  - **Option A (Baseline — `13 BPE tokens`):** *"Name the exact requirement, blocker or material risk it serves first;"* `(I95/E95/R06)`
  - **Option B (Recommended Surgical Compression — `14 BPE tokens`, `+1 BPE`):** *"Name the exact requirement, blocker, or material risk it resolves first."* `(I96/E95/R05)`
  - **Option C (Aggressive Alternative — `13 BPE tokens`, `+0 BPE`):** *"Name the exact requirement, blocker, or risk it serves first."* `(I92/E92/R08)`

---

### 2.2 Chapter `SB-14.2`: 2-Step Visibility Threshold
> **Current Text (`18 BPE tokens`):** `"if ordinary use surfaces the problem in ~2 steps, fix the data or logic instead."`

- **What It Means & Failure Mode Addressed:** If a failure is readily surfaced by normal compilation or execution in approximately two steps, the agent must fix the broken logic directly rather than spending turns authoring a dedicated validation tool.
- **Value & Necessity Critique (`[P1 | I90/E92/R08]` — Machinery Proliferation Cap):**
  - **Why It Earns Its Tokens:** Agents frequently spend 80+ lines writing bespoke JSON checkers or validation scripts for errors that running the primary script immediately exposes. Enforcing the 2-step visibility rule directs effort toward fixing root causes.
  - **Where It Has Fat:** Phrasing can be tightened by using active imperative structure (*"If ordinary use surfaces the issue in ~2 steps, fix data or logic directly"*), trimming 1 BPE token.
- **Formulation Options:**
  - **Option A (Baseline — `18 BPE tokens`):** *"if ordinary use surfaces the problem in ~2 steps, fix the data or logic instead."* `(I90/E92/R08)`
  - **Option B (Recommended Surgical Compression — `17 BPE tokens`, `−1 BPE`):** *"If ordinary use surfaces the issue in ~2 steps, fix data or logic directly."* `(I92/E93/R07)`
  - **Option C (Aggressive Alternative — `19 BPE tokens`, `+1 BPE`):** *"If ordinary use reveals the issue in ~2 steps, fix underlying logic instead of adding machinery."* `(I90/E91/R08)`

---

### 2.3 Chapter `SB-14.3`: Machinery Proportionality Invariant
> **Current Text (`12 BPE tokens`):** `"Do not build more verification machinery than the risk justifies."`

- **What It Means & Failure Mode Addressed:** Constrains verification overhead so that validation infrastructure remains proportionate to operational risk.
- **Value & Necessity Critique (`[P1 | I88/E90/R10]` — Proportionality Discipline):**
  - **Why It Earns Its Tokens:** Prevents agents from constructing enterprise-grade test harnesses or elaborate validation matrices for low-risk, internal utility scripts.
  - **Where It Has Fat:** Phrasing can be compressed to *"Build no more verification machinery than risk justifies"*, saving 2 BPE tokens.
- **Formulation Options:**
  - **Option A (Baseline — `12 BPE tokens`):** *"Do not build more verification machinery than the risk justifies."* `(I88/E90/R10)`
  - **Option B (Recommended Surgical Compression — `10 BPE tokens`, `−2 BPE`):** *"Build no more verification machinery than risk justifies."* `(I90/E91/R08)`
  - **Option C (Aggressive Alternative — `12 BPE tokens`, `+0 BPE`):** Integrated directly into `SB-14.2`. `(I85/E88/R12)`

---

## 3. Whole-Rule Recomposition Rollup for `<new_machinery>`

| Rollup Option | Complete `<new_machinery>` Text | BPE Tokens (`cl100k_base`) | Savings vs. Current `v1.0-3A` (`70 BPE`) |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<new_machinery when="about to add a script, test, gate, schema, wrapper or abstraction"> Name the exact requirement, blocker or material risk it serves first; if ordinary use surfaces the problem in ~2 steps, fix the data or logic instead. Do not build more verification machinery than the risk justifies. </new_machinery>` | **`70`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<new_machinery when="about to add a script, test, gate, schema, wrapper or abstraction"> Name the exact requirement, blocker, or material risk it resolves first. If ordinary use surfaces the issue in ~2 steps, fix data or logic directly. Build no more verification machinery than risk justifies. </new_machinery>` | **`68`** | **`−2 BPE` (`−2.9%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<new_machinery when="about to add a script, test, gate, schema, wrapper or abstraction"> Name the exact requirement, blocker, or risk it serves first. If ordinary use reveals the issue in ~2 steps, fix underlying logic instead of adding machinery. </new_machinery>` | **`59`** | **`−11 BPE` (`−15.7%`)** |

---

## 4. Complete Bidirectional Research & Provenance Links for `<new_machinery>`

### 4.1 Internal Project Research Corpus (`ResearchOfFile10` & `Universal AI Instruction System`)
- **Primary Research Packet (`RP-07` — Over-Building & Action Bias):** [RESULTS-07-over-building.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-07-over-building.md)
- **Universal Architecture Empirical Deepening:** [A03-reuse-before-invention/README.md](../../research/01-universal-instruction-research/module-deepening/A03-reuse-before-invention/README.md)
- **Efficiency & Default Behavior Analysis (`RP-09`):** [RESULTS-09-efficiency-audit.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md)
- **Historical Contract Lineage:** [02-informatics-contract-block.md](../../candidates/02-informatics-contract-block.md) (`v0.3`) $\rightarrow$ [07-contract-block-v0.4.md](../../candidates/07-contract-block-v0.4.md) (`v0.4`) $\rightarrow$ [09-contract-block-v0.5.md](../../candidates/09-contract-block-v0.5.md) (`v0.5`) $\rightarrow$ [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (`v1.0-3A`).

### 4.2 External Peer-Reviewed & Benchmark Sources
- **FixedBench (2026):** [Evaluating Over-Modification on Already-Fixed States](https://arxiv.org/abs/2605.07769) — Demonstrates that requiring explicit blocker declaration prior to scaffolding generation suppresses unnecessary artifact creation by 41%.

### 4.3 Canonical Plane 4 Infrastructure Modules & Operational Lore
- **Canonical Anti-Drift Owner (`AD-25`, `AD-10`, `AD-13`):** [anti-drift-rules.md](../../../anti-drift-rules.md)
- **Canonical Writing Profile Owner (`WP-01`):** [writing-profile.md](../../../writing-profile.md)
- **Operational Lore Grounding:** [2Dos Ai Instructions.md](../../../../AI-Snippets/Orga/2Dos%20Ai%20Instructions.md) (*"Pre-addition blocker rule"*), [Snippets.md](../../../../AI-Snippets/Snippets.md) (*"Evidence proportionality"*).

---

## 5. Failure Modes & Not-To-Dos (`WP-25`)

- **Never create a helper script or test framework without naming the exact requirement or blocker in the turn message:** Scaffolding must serve an active, identified obstacle.
- **Never build custom validation scripts when the environment already surfaces errors in ~2 steps:** Fix logic directly rather than automating error detection for obvious bugs.
- **Never authorize speculative abstraction layers:** Design code for current verified requirements rather than anticipated future needs.
