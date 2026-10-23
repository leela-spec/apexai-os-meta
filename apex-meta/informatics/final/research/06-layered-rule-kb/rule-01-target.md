---
type: Reference
id: V2-LAYERED-KB-RULE-01-TARGET
title: Rule 01 Deep-Dive — <target> Semantic Block Decomposition, Value Audit & Compression Options
description: Prototype file for the Layered Rule Knowledge Base decomposing <target> (from 13-candidate-3A-xml.md) into atomic semantic blocks, evaluating token value, formulating tighter alternatives, and linking all internal and external research.
status: prototype_for_review
tags: [layered-kb, rule-01, target, semantic-blocks, token-compression, research-ledger]
---

# Rule 01 Deep-Dive: `<target>` (`13-candidate-3A-xml.md`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (format siblings: [14-candidate-3B-hybrid.md](../../candidates/14-candidate-3B-hybrid.md), [15-candidate-3C-bullet-hybrid.md](../../candidates/15-candidate-3C-bullet-hybrid.md))
> - **Layer 1 (This File — Rule-Level Semantic Block Audit):** Decomposes `<target>` into 4 atomic semantic blocks (`SB-01.1`..`SB-01.4`), audits whether each token bundle earns its place, and presents scored compression options.
> - **Layer 2 (Downstream Infrastructure Modules):** [anti-drift-rules.md](../../specs/anti-drift-rules.md) (`AD-01`, `AD-09`, `AD-12`), [execution-modes.md](../../specs/execution-modes.md) (`EM-04`), [writing-profile.md](../../specs/writing-profile.md) (`WP-01`).

---

## 1. Original Rule & Atomic Semantic Block List

### 1.1 Current `v1.0-3A` Full Text (`56 BPE tokens` | `71 repo tokens` | `285 chars` | `42 words`)

```xml
<target>Deliver the result the operator specified. Before claiming completion, verify the delivered product against each stated requirement (which outranks any inferred criteria). Tests, schemas and checklists you author are supporting evidence, never replacement criteria; on conflict, the requirement wins. If evidence shows no change is needed, state so and stop.</target>
```

### 1.2 Atomic Semantic Block Inventory (Bullet List)

Every token in `<target>` belongs to one of four distinct semantic blocks (`SB-01.1` through `SB-01.4`), plus the XML tag wrapper (`<target>...</target>`, `4 BPE tokens`):

- **`SB-01.1` — Core Outcome Imperative (`7 BPE tokens` | `42 chars`):** *"Deliver the result the operator specified."*
- **`SB-01.2` — Pre-Completion Verification & Requirement Precedence (`18 BPE tokens` | `107 chars`):** *"Before claiming completion, verify the delivered product against each stated requirement (which outranks any inferred criteria)."*
- **`SB-01.3` — Anti-Self-Authored-Criteria Guard (`17 BPE tokens` | `93 chars`):** *"Tests, schemas and checklists you author are supporting evidence, never replacement criteria; on conflict, the requirement wins."*
- **`SB-01.4` — No-Op Legitimacy Clause (`10 BPE tokens` | `40 chars`):** *"If evidence shows no change is needed, state so and stop."*

---

## 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

### 2.1 Chapter `SB-01.1`: Core Outcome Imperative
> **Current Text (`7 BPE tokens`):** `"Deliver the result the operator specified."`

- **What It Means & Failure Mode Addressed:** Establishes that the operator's stated target is the primary objective.
- **Value & Necessity Critique (`[P2 | I65/E85/R10]` — Partially Redundant with `SB-01.2`):**
  - **Honest High-Reasoning Critique:** On its own, *"Deliver the result the operator specified"* is **default RLHF assistant behavior** ([RESULTS-09](../ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md) §2). Every frontier model already tries to deliver what the user asked. Furthermore, `SB-01.2` (*"verify the delivered product against each stated requirement"*) already presupposes delivering the stated requirement! Keeping `SB-01.1` as a separate opening sentence spends `7 BPE tokens` stating a truism that can be fused directly into `SB-01.2`.
- **Formulation Options:**
  - **Option A (Keep Current — `7 BPE tokens`):** *"Deliver the result the operator specified."* `(I65/E85/R05)`
  - **Option B (Compress — `5 BPE tokens`, `−2 BPE`):** *"Deliver the stated target."* `(I65/E85/R05)`
  - **Option C (Recommended — Fuse into `SB-01.2`, `0 standalone tokens`, `−7 BPE`):** Merge the outcome obligation into `SB-01.2` so the rule opens immediately with the actionable check. `(I90/E92/R08)`

---

### 2.2 Chapter `SB-01.2`: Pre-Completion Verification & Requirement Precedence
> **Current Text (`18 BPE tokens`):** `"Before claiming completion, verify the delivered product against each stated requirement (which outranks any inferred criteria)."`

- **What It Means & Failure Mode Addressed:** Forces the agent to execute an explicit requirement-by-requirement check before stopping, and forbids letting codebase conventions or inferred habits override an explicit operator instruction.
- **Value & Necessity Critique (`[P0 | I96/E95/R05]` — High-Leverage Non-Default Behavior):**
  - **Why It Earns Its Tokens:** [RESULTS-05](../ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-05-self-authored-criteria.md) ([SpecBench, 2026](https://arxiv.org/abs/2605.21384)) showed frontier coding agents achieve only **42.7% full specification alignment** because they satisfy 2–3 prominent requirements and silently drop secondary constraints. Forcing a positive check against *each stated requirement* before completion directly targets that failure mode.
  - **Where It Has Fat:** The parenthetical `"(which outranks any inferred criteria)"` overlaps heavily with `SB-01.3`'s `"; on conflict, the requirement wins"`. Stated twice in two consecutive sentences, "the requirement outranks/wins" wastes ~6–8 tokens.
- **Formulation Options:**
  - **Option A (Keep Current — `18 BPE tokens`):** *"Before claiming completion, verify the delivered product against each stated requirement (which outranks any inferred criteria)."* `(I94/E95/R05)`
  - **Option B (Recommended — Fused with `SB-01.1` & Deduplicated against `SB-01.3` — `13 BPE tokens`, `−12 BPE` vs. `SB-01.1+01.2`):** *"Verify the delivered result against each stated requirement before claiming completion."* `(I96/E95/R06)`
  - **Option C (Ultra-Dense Imperative — `10 BPE tokens`, `−15 BPE` vs. `SB-01.1+01.2`):** *"Before finishing, verify the result against every stated requirement."* `(I93/E92/R10)`

---

### 2.3 Chapter `SB-01.3`: Anti-Self-Authored-Criteria Guard
> **Current Text (`17 BPE tokens`):** `"Tests, schemas and checklists you author are supporting evidence, never replacement criteria; on conflict, the requirement wins."`

- **What It Means & Failure Mode Addressed:** Prevents "self-grading theater" where an agent writes a weak unit test or checklist, sees it turn green, and declares a broken or incomplete deliverable "done".
- **Value & Necessity Critique (`[P0 | I98/E96/R05]` — Essential Apex Invariant):**
  - **Why It Earns Its Tokens:** Both operational lore ([2Dos Ai Instructions.md](../../../../AI-Snippets/Orga/2Dos%20Ai%20Instructions.md)) and [Ma et al. (2026)](https://arxiv.org/abs/2606.28430) (`RP-05`) show that when agents author both the code and the test, they systematically encode their own misunderstanding into the test.
  - **Where It Has Fat:** Compare `<target>` (`SB-01.3`) with the last sentence of `<product_first>` right below it in `3A`: *"Never let a verification script's passing become the definition of done."* Those two sentences are **80% overlapping**! In addition, *"Tests, schemas and checklists you author"* (`7 BPE tokens`) can be compressed to *"Self-authored tests or checklists"* (`5 BPE tokens`).
- **Formulation Options:**
  - **Option A (Keep Current — `17 BPE tokens`):** *"Tests, schemas and checklists you author are supporting evidence, never replacement criteria; on conflict, the requirement wins."* `(I96/E95/R05)`
  - **Option B (Recommended — Tightened & Unified Precedence — `14 BPE tokens`, `−3 BPE`):** *"Self-authored tests or checklists are evidence, never replacement criteria; stated requirements outrank inferred ones."* `(I98/E96/R06)`
  - **Option C (Cross-Rule Deduplication with `<product_first>` — `11 BPE tokens` + deletes `13 BPE` from `<product_first>` = `−19 BPE` net):** *"Self-authored tests, scripts or checklists never replace or define the stated requirement."* (And delete the duplicate final sentence of `<product_first>`!). `(I95/E94/R12)`

---

### 2.4 Chapter `SB-01.4`: No-Op Legitimacy Clause
> **Current Text (`10 BPE tokens`):** `"If evidence shows no change is needed, state so and stop."`

- **What It Means & Failure Mode Addressed:** Authorizes the agent to conclude that a file, rule, or module is already correct and requires **zero edits**, instead of inventing cosmetic churn to justify its turn.
- **Value & Necessity Critique (`[P0 | I95/E96/R05]` — Highest-Evidence Addition from `RP-07`):**
  - **Why It Earns Every Token:** [FixedBench (2026)](https://arxiv.org/abs/2605.07769) ([RESULTS-07](../ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-07-over-building.md)) demonstrated that frontier models fail on **68%–91% of already-resolved states** because RLHF action bias makes them assume every prompt demands a diff. Explicitly legitimizing *"no change is needed"* is the single highest-leverage countermeasure.
- **Formulation Options:**
  - **Option A (Keep Current — `10 BPE tokens`):** *"If evidence shows no change is needed, state so and stop."* `(I95/E96/R05)`
  - **Option B (Recommended — Slightly Tighter — `9 BPE tokens`, `−1 BPE`):** *"If evidence shows no change is needed, say so and stop."* `(I95/E96/R05)`
  - **Option C (Move to `<scope>` — `0 tokens in <target>`):** Move to `<scope>` (*"If nothing needs changing, say so and stop."*). `(I88/E90/R15 — slightly weaker because `<target>` is position #1 in the contract)`.

---

## 3. Whole-Rule Recomposition Rollup for `<target>`

| Rollup Option | Complete `<target>` Text | BPE Tokens (`cl100k_base`) | Savings vs. Current `v1.0-3A` (`56 BPE`) |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<target>Deliver the result the operator specified. Before claiming completion, verify the delivered product against each stated requirement (which outranks any inferred criteria). Tests, schemas and checklists you author are supporting evidence, never replacement criteria; on conflict, the requirement wins. If evidence shows no change is needed, state so and stop.</target>` | **`56`** | `0` (`0%`) |
| **2. Recommended Surgical Compression (`SB-01.1C + 01.2B + 01.3B + 01.4B`)** | `<target>Verify the delivered result against each stated requirement before claiming completion. Self-authored tests or checklists are evidence, never replacement criteria; stated requirements outrank inferred ones. If evidence shows no change is needed, say so and stop.</target>` | **`40`** | **`−16 BPE` (`−28.6%`)** with **zero semantic loss** |
| **3. Aggressive Cross-Rule Compression (`+ deduplicate <product_first>` final sentence)** | `<target>Before finishing, verify the result against every stated requirement. Self-authored tests, scripts or checklists never replace or define the requirement. If evidence shows no change is needed, say so and stop.</target>` | **`36`** *(plus `−13 BPE` in `<product_first>`)* | **`−20 BPE` in `<target>` / `−33 BPE` net (`−35.7%`)** |

---

## 4. Complete Bidirectional Research & Provenance Links for `<target>`

### 4.1 Internal Project Research Corpus (`ResearchOfFile10` & `Universal AI Instruction System`)
- **Primary Research Packet (`RP-05` — Self-Authored Acceptance Criteria):** [RESULTS-05-self-authored-criteria.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-05-self-authored-criteria.md)
- **Secondary Research Packet (`RP-07` — Over-Building & No-Op Legitimacy):** [RESULTS-07-over-building.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-07-over-building.md)
- **Efficiency & Default-Behavior Audit (`RP-09`):** [RESULTS-09-efficiency-audit.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md)
- **Cross-Packet Synthesis:** [RESULTS-11-synthesis.md](../../research/03-research-of-file-10/RESULTS-11-synthesis.md) (§4 Rank 4 & Rank 5)
- **Historical Contract Lineage:** [02-informatics-contract-block.md](../../candidates/02-informatics-contract-block.md) (`v0.3`) $\rightarrow$ [07-contract-block-v0.4.md](../../candidates/07-contract-block-v0.4.md) (`v0.4`) $\rightarrow$ [09-contract-block-v0.5.md](../../candidates/09-contract-block-v0.5.md) (`v0.5`) $\rightarrow$ [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (`v1.0-3A`).

### 4.2 External Peer-Reviewed & Benchmark Sources
- **SpecBench (2026):** [Benchmarking Specification Alignment in Coding Agents](https://arxiv.org/abs/2605.21384) — Establishes the 42.7% full-spec compliance baseline and the necessity of item-by-item requirement verification (`SB-01.2`).
- **Ma et al. (2026):** [Spec-Driven Software Engineering Benchmark](https://arxiv.org/abs/2606.28430) — Demonstrates failure modes when agents author both implementation and acceptance tests (`SB-01.3`).
- **FixedBench (2026):** [Evaluating Over-Modification on Already-Fixed States](https://arxiv.org/abs/2605.07769) — Proves 68%–91% unnecessary modification rate without explicit no-op legitimacy (`SB-01.4`).

### 4.3 Canonical Plane 4 Infrastructure Modules & Operational Lore
- **Canonical Anti-Drift Owner (`AD-01`, `AD-09`, `AD-12`):** [anti-drift-rules.md](../../specs/anti-drift-rules.md)
- **Canonical Execution Adapter Owner (`EM-04`):** [execution-modes.md](../../specs/execution-modes.md)
- **Canonical Writing Profile Owner (`WP-01`):** [writing-profile.md](../../specs/writing-profile.md)
- **Upstream Operational Lore:** [2Dos Ai Instructions.md](../../../../AI-Snippets/Orga/2Dos%20Ai%20Instructions.md), [Snippets.md](../../../../AI-Snippets/Snippets.md), and [A01-target-outcome-alignment/README.md](../../research/01-universal-instruction-research/module-deepening/A01-target-outcome-alignment/README.md).

---

## 5. Failure Modes & Not-To-Dos (`WP-25`)
- **Never cut `SB-01.3` (anti-self-authored criteria) or `SB-01.4` (no-op legitimacy):** Both counteract documented frontier-model RLHF biases that are **not** default model behavior.
- **Never state requirement precedence twice in the same tag:** Keep the precedence clause in one place (`SB-01.3B`) rather than repeating it in both `SB-01.2` and `SB-01.3`.
