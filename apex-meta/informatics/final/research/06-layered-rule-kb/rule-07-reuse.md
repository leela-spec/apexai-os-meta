---
type: Reference
id: V2-LAYERED-KB-RULE-07-REUSE
title: Rule 07 Deep-Dive — <reuse> Semantic Block Decomposition, Value Audit & Compression Options
description: Decomposing <reuse> (from 13-candidate-3A-xml.md) into atomic semantic blocks, evaluating token value, formulating tighter alternatives, and linking all internal and external research.
status: current_truth
tags: [layered-kb, rule-07, reuse, semantic-blocks, token-compression, research-ledger]
---

# Rule 07 Deep-Dive: `<reuse>` (`13-candidate-3A-xml.md`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (format siblings: [14-candidate-3B-hybrid.md](../../candidates/14-candidate-3B-hybrid.md), [15-candidate-3C-bullet-hybrid.md](../../candidates/15-candidate-3C-bullet-hybrid.md))
> - **Layer 1 (This File — Rule-Level Semantic Block Audit):** Decomposes `<reuse>` into 4 atomic semantic blocks (`SB-07.1`..`SB-07.4`), audits token value against NIH (Not-Invented-Here) syndrome and over-abstraction, and presents scored compression options.
> - **Layer 2 (Downstream Infrastructure Modules):** [anti-drift-rules.md](../../specs/anti-drift-rules.md) (`AD-11`, `AD-14`), [writing-profile.md](../../specs/writing-profile.md) (`WP-23`).

---

## 1. Original Rule & Atomic Semantic Block Inventory

### 1.1 Current `v1.0-3A` Full Text (`56 BPE block` | `51 BPE inner` | `67 repo tokens` | `270 chars` | `39 words`)

```xml
<reuse>Before building, check what exists: repository scripts, installed tools, established libraries, published skills. Use a fit option in its proven form, adapting the smallest surface. Compose modular parts rather than a monolith. Build new only when nothing suitable fits.</reuse>
```

### 1.2 Atomic Semantic Block Inventory (Bullet List)

Every token in `<reuse>` belongs to one of four distinct semantic blocks (`SB-07.1` through `SB-07.4`), plus the XML tag wrapper (`<reuse>...</reuse>`, `5 BPE tokens`):

- **`SB-07.1` — Asset Inventory Imperative (`19 BPE tokens` | `113 chars`):** *"Before building, check what exists: repository scripts, installed tools, established libraries, published skills."*
- **`SB-07.2` — Minimal Adaptation Surface (`14 BPE tokens` | `67 chars`):** *"Use a fit option in its proven form, adapting the smallest surface."*
- **`SB-07.3` — Modular Composition (`9 BPE tokens` | `45 chars`):** *"Compose modular parts rather than a monolith."*
- **`SB-07.4` — Build as Last Resort (`8 BPE tokens` | `42 chars`):** *"Build new only when nothing suitable fits."*

---

## 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

### 2.1 Chapter `SB-07.1`: Asset Inventory Imperative
> **Current Text (`19 BPE tokens`):** `"Before building, check what exists: repository scripts, installed tools, established libraries, published skills."`

- **What It Means & Failure Mode Addressed:** Requires the agent to inspect the local filesystem, environment tools, package registries, and agent skills before writing bespoke utility code.
- **Value & Necessity Critique (`[P1 | I90/E92/R08]` — Anti-NIH Discipline):**
  - **Honest High-Reasoning Critique:** Frontier coding agents display strong Not-Invented-Here (NIH) tendencies, writing 50 lines of custom Python or shell scripting for operations already solved by native CLI tools (`ripgrep`, `jq`, `git`, `curl`) or pre-installed repository utilities. Enumerating the specific asset categories prompts active tool discovery.
  - **Where It Has Fat:** Phrasing can be tightened from 19 down to 15 BPE tokens by consolidating verbs and descriptors.
- **Formulation Options:**
  - **Option A (Baseline — `19 BPE tokens`):** *"Before building, check what exists: repository scripts, installed tools, established libraries, published skills."* `(I90/E92/R08)`
  - **Option B (Recommended Surgical Compression — `15 BPE tokens`, `−4 BPE`):** *"Before building, inspect repository scripts, installed tools, libraries, and skills."* `(I92/E93/R07)`
  - **Option C (Aggressive Alternative — `11 BPE tokens`, `−8 BPE`):** *"Inspect repo scripts, tools, and skills before building."* `(I88/E90/R10)`

---

### 2.2 Chapter `SB-07.2`: Minimal Adaptation Surface
> **Current Text (`14 BPE tokens`):** `"Use a fit option in its proven form, adapting the smallest surface."`

- **What It Means & Failure Mode Addressed:** When adopting an existing tool, library, or script, use it in its canonical interface and modify only the minimum necessary surface area to solve the task.
- **Value & Necessity Critique (`[P1 | I92/E93/R07]` — Anti-Over-Wrapping Invariant):**
  - **Why It Earns Its Tokens:** Agents love authoring elaborate 150-line adapter classes, abstract factories, and wrapper interfaces around simple 3-line standard library function calls. This rule demands minimal adaptation surface, suppressing wrapper churn.
  - **Where It Has Fat:** 5 BPE tokens can be saved by replacing passive phrasing with an active verb phrase.
- **Formulation Options:**
  - **Option A (Baseline — `14 BPE tokens`):** *"Use a fit option in its proven form, adapting the smallest surface."* `(I92/E93/R07)`
  - **Option B (Recommended Surgical Compression — `9 BPE tokens`, `−5 BPE`):** *"Adapt proven options over the smallest surface;"* `(I93/E94/R06)`
  - **Option C (Aggressive Alternative — `9 BPE tokens`, `−5 BPE`):** *"Adapt proven tools over the smallest surface;"* `(I91/E92/R08)`

---

### 2.3 Chapter `SB-07.3`: Modular Composition
> **Current Text (`9 BPE tokens`):** `"Compose modular parts rather than a monolith."`

- **What It Means & Failure Mode Addressed:** Enforces Gall's Law and Unix philosophy: combine focused, single-purpose components rather than architecting large, tightly coupled monolithic scripts.
- **Value & Necessity Critique (`[P2 | I80/E85/R10]` — Structural Architectural Guideline):**
  - **Why It Earns Its Tokens:** Monolithic implementations are brittle and difficult to debug across multi-agent workflows. Decomposing complex logic into small, independently testable units dramatically improves agent recovery.
  - **Where It Has Fat:** In Option B, it seamlessly fuses with `SB-07.2` as a compound clause, saving 5 BPE tokens.
- **Formulation Options:**
  - **Option A (Baseline — `9 BPE tokens`):** *"Compose modular parts rather than a monolith."* `(I80/E85/R10)`
  - **Option B (Recommended Surgical Compression — `4 BPE tokens`, `−5 BPE`):** *"compose modular parts."* `(I85/E88/R08)`
  - **Option C (Aggressive Alternative — `4 BPE tokens`, `−5 BPE`):** *"compose modular parts."* `(I85/E88/R08)`

---

### 2.4 Chapter `SB-07.4`: Build as Last Resort
> **Current Text (`8 BPE tokens`):** `"Build new only when nothing suitable fits."`

- **What It Means & Failure Mode Addressed:** Authoring net-new code, tools, or abstractions is permitted only after verifying that no existing component or tool meets the requirement.
- **Value & Necessity Critique (`[P1 | I92/E92/R08]` — Definitive Closure Gate):**
  - **Why It Earns Its Tokens:** Acts as the terminal condition of the `<reuse>` lifecycle, preventing unjustified wheel-reinvention.
  - **Where It Has Fat:** Already exceptionally lean (8 BPE tokens).
- **Formulation Options:**
  - **Option A (Baseline — `8 BPE tokens`):** *"Build new only when nothing suitable fits."* `(I92/E92/R08)`
  - **Option B (Recommended Surgical Compression — `8 BPE tokens`, `+0 BPE`):** *"Build new only when nothing suitable fits."* `(I92/E92/R08)`
  - **Option C (Aggressive Alternative — `8 BPE tokens`, `+0 BPE`):** *"Build new only when nothing suitable exists."* `(I91/E91/R09)`

---

## 3. Whole-Rule Recomposition Rollup for `<reuse>`

| Rollup Option | Complete `<reuse>` Text | BPE Tokens (`cl100k_base`) | Savings vs. Current `v1.0-3A` (`56 BPE`) |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<reuse>Before building, check what exists: repository scripts, installed tools, established libraries, published skills. Use a fit option in its proven form, adapting the smallest surface. Compose modular parts rather than a monolith. Build new only when nothing suitable fits.</reuse>` | **`56`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<reuse>Before building, inspect repository scripts, installed tools, libraries, and skills. Adapt proven options over the smallest surface; compose modular parts. Build new only when nothing suitable fits.</reuse>` | **`40`** | **`−16 BPE` (`−28.6%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<reuse>Inspect repo scripts, tools, and skills before building. Adapt proven tools over the smallest surface; compose modular parts. Build new only when nothing suitable exists.</reuse>` | **`36`** | **`−20 BPE` (`−35.7%`)** |

---

## 4. Complete Bidirectional Research & Provenance Links for `<reuse>`

### 4.1 Internal Project Research Corpus (`ResearchOfFile10` & `Universal AI Instruction System`)
- **Primary Research Packet (`RP-09` — Efficiency Audit & Non-Default Invariants):** [RESULTS-09-efficiency-audit.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md)
- **Universal Architecture Empirical Deepening:** [A03-reuse-before-invention/README.md](../../research/01-universal-instruction-research/module-deepening/A03-reuse-before-invention/README.md)
- **Historical Contract Lineage:** [02-informatics-contract-block.md](../../candidates/02-informatics-contract-block.md) (`v0.3`) $\rightarrow$ [07-contract-block-v0.4.md](../../candidates/07-contract-block-v0.4.md) (`v0.4`) $\rightarrow$ [09-contract-block-v0.5.md](../../candidates/09-contract-block-v0.5.md) (`v0.5`) $\rightarrow$ [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (`v1.0-3A`).

### 4.2 External Peer-Reviewed & Benchmark Sources
- **Gall's Law (General Systems Thinking):** *"A complex system that works is invariably found to have evolved from a simple system that worked. A complex system designed from scratch never works and cannot be patched up to make it work."*
- **DITA Single-Source Architecture:** Canonical documentation standard demonstrating reuse of atomic semantic components over custom page generation.

### 4.3 Canonical Plane 4 Infrastructure Modules & Operational Lore
- **Canonical Anti-Drift Owner (`AD-11`, `AD-14`):** [anti-drift-rules.md](../../specs/anti-drift-rules.md)
- **Canonical Writing Profile Owner (`WP-23`):** [writing-profile.md](../../specs/writing-profile.md)
- **Operational Lore Grounding:** [2Dos Ai Instructions.md](../../../../AI-Snippets/Orga/2Dos%20Ai%20Instructions.md) (*"Reuse before invention"*), [Snippets.md](../../../../AI-Snippets/Snippets.md) (*"Asset Preservation"*).

---

## 5. Failure Modes & Not-To-Dos (`WP-25`)

- **Never omit the explicit resource list (`SB-07.1`):** General admonitions to "reuse" fail to trigger active CLI checks; explicitly naming repository scripts, tools, and skills prompts tangible search behavior.
- **Never authorize writing custom script wrappers when built-in tool flags suffice:** Direct tool invocation is always superior to intermediate helper scripts.
- **Never treat code authoring as the default response to a problem:** Code is a liability; reuse minimizes maintenance burden and attack surface.
