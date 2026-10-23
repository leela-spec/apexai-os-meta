---
type: Reference
id: V2-LAYERED-KB-RULE-04-COMMUNICATION
title: Rule 04 Deep-Dive — <communication> Semantic Block Decomposition, Value Audit & Compression Options
description: Decomposing <communication> (from 13-candidate-3A-xml.md) into atomic semantic blocks, evaluating token value, formulating tighter alternatives, and linking all internal and external research.
status: current_truth
tags: [layered-kb, rule-04, communication, semantic-blocks, token-compression, research-ledger]
---

# Rule 04 Deep-Dive: `<communication>` (`13-candidate-3A-xml.md`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (format siblings: [14-candidate-3B-hybrid.md](../../candidates/14-candidate-3B-hybrid.md), [15-candidate-3C-bullet-hybrid.md](../../candidates/15-candidate-3C-bullet-hybrid.md))
> - **Layer 1 (This File — Rule-Level Semantic Block Audit):** Decomposes `<communication>` into 4 atomic semantic blocks (`SB-04.1`..`SB-04.4`), audits token value against RLHF sycophancy and narrative bloat, and presents scored compression options.
> - **Layer 2 (Downstream Infrastructure Modules):** [writing-profile.md](../../../writing-profile.md) (`WP-02`, `WP-03`, `WP-04`, `WP-05`, `WP-12`), [anti-drift-rules.md](../../../anti-drift-rules.md) (`AD-17`).

---

## 1. Original Rule & Atomic Semantic Block Inventory

### 1.1 Current `v1.0-3A` Full Text (`73 BPE block` | `68 BPE inner` | `89 repo tokens` | `358 chars` | `47 words`)

```xml
<communication>Active voice, explicit actor. One imperative per sentence. Conclusion first. Evidence-led, analytical technical register (Cool Blue): precise, objective, high density, no filler, no flattery, no unearned agreement. State uncertainty plainly when evidence is incomplete; avoid empty hedges. Report the result and exact blocker; compress routine tool activity.</communication>
```

### 1.2 Atomic Semantic Block Inventory (Bullet List)

Every token in `<communication>` belongs to one of four distinct semantic blocks (`SB-04.1` through `SB-04.4`), plus the XML tag wrapper (`<communication>...</communication>`, `5 BPE tokens`):

- **`SB-04.1` — Grammar & Primacy Foundations (`14 BPE tokens` | `76 chars`):** *"Active voice, explicit actor. One imperative per sentence. Conclusion first."*
- **`SB-04.2` — Cool Blue Analytical Register (`29 BPE tokens` | `137 chars`):** *"Evidence-led, analytical technical register (Cool Blue): precise, objective, high density, no filler, no flattery, no unearned agreement."*
- **`SB-04.3` — Warranted Uncertainty vs Empty Hedges (`13 BPE tokens` | `74 chars`):** *"State uncertainty plainly when evidence is incomplete; avoid empty hedges."*
- **`SB-04.4` — Actionable Output & Chatter Compression (`12 BPE tokens` | `68 chars`):** *"Report the result and exact blocker; compress routine tool activity."*

---

## 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

### 2.1 Chapter `SB-04.1`: Grammar & Primacy Foundations
> **Current Text (`14 BPE tokens`):** `"Active voice, explicit actor. One imperative per sentence. Conclusion first."`

- **What It Means & Failure Mode Addressed:** Dictates rigorous prose ergonomics: identifying who performs each action, restricting instructions to single unambiguous procedural imperatives per sentence (WP-02), and presenting findings bottom-line-up-front (BLUF / WP-12).
- **Value & Necessity Critique (`[P2 | I82/E88/R08]` — Stylistic & Structural Anchor):**
  - **Honest High-Reasoning Critique:** Frontier LLMs inherently default to passive voice, compound multi-clause sentences, and conversational preambles that delay the core answer. Enforcing active voice, single imperatives, and conclusion-first ordering directly improves instruction following and scanning speed.
  - **Where It Has Fat:** While concise, punctuation can be fused slightly to optimize token flow without diluting the commands.
- **Formulation Options:**
  - **Option A (Baseline — `14 BPE tokens`):** *"Active voice, explicit actor. One imperative per sentence. Conclusion first."* `(I82/E88/R08)`
  - **Option B (Recommended Surgical Compression — `14 BPE tokens`, `+0 BPE`):** *"Active voice, explicit actor, conclusion first. One imperative per sentence."* `(I84/E89/R07)`
  - **Option C (Aggressive / Unified Alternative — `11 BPE tokens`, `−3 BPE`):** *"Conclusion first in active voice; one imperative per sentence."* `(I80/E86/R10)`

---

### 2.2 Chapter `SB-04.2`: Cool Blue Analytical Register
> **Current Text (`29 BPE tokens`):** `"Evidence-led, analytical technical register (Cool Blue): precise, objective, high density, no filler, no flattery, no unearned agreement."`

- **What It Means & Failure Mode Addressed:** Prescribes an objective, detached, evidence-grounded technical register based on the Insights Discovery Cool Blue behavioral persona. It explicitly bans conversational filler, complimentary sycophancy ("Certainly!", "Great question!"), and agreeable acquiescence when data contradicts the user.
- **Value & Necessity Critique (`[P1 | I90/E92/R06]` — Anti-Sycophancy Register Anchor):**
  - **Why It Earns Its Tokens:** Grounding in Cool Blue (RP-04) replaced vague exhortations to "be professional" with a battle-tested behavioral archetype. Standard RLHF alignment produces obsequious, verbose assistants. Naming Cool Blue suppresses filler and enforces dense, fact-first reporting.
  - **Where It Has Fat:** Listing seven descriptive adjectives/phrases consumes 29 BPE tokens. Option B condenses the descriptor string to its core operational behaviors.
- **Formulation Options:**
  - **Option A (Baseline — `29 BPE tokens`):** *"Evidence-led, analytical technical register (Cool Blue): precise, objective, high density, no filler, no flattery, no unearned agreement."* `(I90/E92/R06)`
  - **Option B (Recommended Surgical Compression — `22 BPE tokens`, `−7 BPE`):** *"Analytical register (Cool Blue): objective, dense, zero filler, flattery, or unearned agreement."* `(I92/E93/R05)`
  - **Option C (Aggressive Alternative — `19 BPE tokens`, `−10 BPE`):** *"Analytical register (Cool Blue): objective, dense, zero flattery or unearned agreement."* `(I88/E90/R08)`

---

### 2.3 Chapter `SB-04.3`: Warranted Uncertainty vs Empty Hedges
> **Current Text (`13 BPE tokens`):** `"State uncertainty plainly when evidence is incomplete; avoid empty hedges."`

- **What It Means & Failure Mode Addressed:** Distinguishes genuine, warranted epistemic uncertainty (where data is physically missing) from rhetorical or sycophantic hedging ("I believe", "it seems", "perhaps").
- **Value & Necessity Critique (`[P0 | I95/E95/R05]` — Epistemic Honesty Invariant):**
  - **Why It Earns Its Tokens:** The earlier contract formulation ("No hedging") introduced a serious behavioral paradox: when an agent lacked conclusive evidence, it either had to lie with unearned certainty or violate the no-hedging rule. This refined clause (from RP-04) commands plain admission of unknowns while continuing to ban decorative filler hedges.
  - **Where It Has Fat:** The phrasing is already exceptionally lean.
- **Formulation Options:**
  - **Option A (Baseline — `13 BPE tokens`):** *"State uncertainty plainly when evidence is incomplete; avoid empty hedges."* `(I95/E95/R05)`
  - **Option B (Recommended Surgical Compression — `13 BPE tokens`, `+0 BPE`):** *"State uncertainty plainly when evidence is incomplete; avoid empty hedges."* `(I95/E95/R05)`
  - **Option C (Aggressive / Terse Alternative — `8 BPE tokens`, `−5 BPE`):** *"State uncertainty plainly without empty hedges."* `(I90/E91/R10)`

---

### 2.4 Chapter `SB-04.4`: Actionable Output & Chatter Compression
> **Current Text (`12 BPE tokens`):** `"Report the result and exact blocker; compress routine tool activity."`

- **What It Means & Failure Mode Addressed:** Instructs the agent to state the tangible outcome and the precise blocking condition, rather than dumping play-by-play narratives of every minor shell or filesystem invocation.
- **Value & Necessity Critique (`[P1 | I90/E92/R06]` — Context Conservation Invariant):**
  - **Why It Earns Its Tokens:** Routine command chatter bloats multi-turn chat context, accelerating context window exhaustion and inducing "lost in the middle" degradation. Compressing chatter keeps attention focused on core blockers and final deliverables.
  - **Where It Has Fat:** Two BPE tokens can be saved by replacing *"routine tool activity"* with *"tool chatter"*.
- **Formulation Options:**
  - **Option A (Baseline — `12 BPE tokens`):** *"Report the result and exact blocker; compress routine tool activity."* `(I90/E92/R06)`
  - **Option B (Recommended Surgical Compression — `10 BPE tokens`, `−2 BPE`):** *"Report results and exact blockers; compress tool chatter."* `(I91/E92/R05)`
  - **Option C (Aggressive Alternative — `11 BPE tokens`, `−1 BPE`):** *"Report results and exact blockers; compress routine tool activity."* `(I89/E91/R07)`

---

## 3. Whole-Rule Recomposition Rollup for `<communication>`

| Rollup Option | Complete `<communication>` Text | BPE Tokens (`cl100k_base`) | Savings vs. Current `v1.0-3A` (`73 BPE`) |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<communication>Active voice, explicit actor. One imperative per sentence. Conclusion first. Evidence-led, analytical technical register (Cool Blue): precise, objective, high density, no filler, no flattery, no unearned agreement. State uncertainty plainly when evidence is incomplete; avoid empty hedges. Report the result and exact blocker; compress routine tool activity.</communication>` | **`73`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<communication>Active voice, explicit actor, conclusion first. One imperative per sentence. Analytical register (Cool Blue): objective, dense, zero filler, flattery, or unearned agreement. State uncertainty plainly when evidence is incomplete; avoid empty hedges. Report results and exact blockers; compress tool chatter.</communication>` | **`64`** | **`−9 BPE` (`−12.3%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<communication>Conclusion first in active voice; one imperative per sentence. Analytical register (Cool Blue): objective, dense, zero flattery or unearned agreement. State uncertainty plainly without empty hedges. Report results and exact blockers; compress tool chatter.</communication>` | **`53`** | **`−20 BPE` (`−27.4%`)** |

---

## 4. Complete Bidirectional Research & Provenance Links for `<communication>`

### 4.1 Internal Project Research Corpus (`ResearchOfFile10` & `Universal AI Instruction System`)
- **Primary Research Packet (`RP-04` — Register Terminology & Epistemic Stance):** [RESULTS-04-register-terminology.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-04-register-terminology.md)
- **Secondary Research Packet (`RP-09` — Efficiency Audit & Default Behavior):** [RESULTS-09-efficiency-audit.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md)
- **Universal Architecture Empirical Deepening:** [A12-communication-economy-actionable-visibility/README.md](../../research/01-universal-instruction-research/module-deepening/A12-communication-economy-actionable-visibility/README.md)
- **Historical Contract Lineage:** [02-informatics-contract-block.md](../../candidates/02-informatics-contract-block.md) (`v0.3`) $\rightarrow$ [07-contract-block-v0.4.md](../../candidates/07-contract-block-v0.4.md) (`v0.4`) $\rightarrow$ [09-contract-block-v0.5.md](../../candidates/09-contract-block-v0.5.md) (`v0.5`) $\rightarrow$ [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (`v1.0-3A`).

### 4.2 External Peer-Reviewed & Benchmark Sources
- **Insights Discovery Model (Developers Insights 2026):** [The Cool Blue Register](https://developers.insights.com/discovery-model) — Demonstrates how persona and register anchors establish rigorous analytical detachment in automated agent interactions.
- **Minto Pyramid Principle (BLUF):** Classic information architecture pattern prioritizing actionable conclusions before supporting derivations.

### 4.3 Canonical Plane 4 Infrastructure Modules & Operational Lore
- **Canonical Writing Profile Owner (`WP-02`, `WP-03`, `WP-04`, `WP-05`, `WP-12`):** [writing-profile.md](../../../writing-profile.md)
- **Canonical Anti-Drift Owner (`AD-17`):** [anti-drift-rules.md](../../../anti-drift-rules.md)
- **Operational Lore Grounding:** [2Dos Ai Instructions.md](../../../../AI-Snippets/Orga/2Dos%20Ai%20Instructions.md) (*"Cool Blue Register"*), [Snippets.md](../../../../AI-Snippets/Snippets.md) (*"Directness & BLUF"*).

---

## 5. Failure Modes & Not-To-Dos (`WP-25`)

- **Never revert to a blunt "No hedging" command:** Banning all hedging when information is incomplete forces models to hallucinate false certainty or fabricate test results.
- **Never delete the anti-flattery or anti-unearned-agreement directives:** Without explicit suppression, RLHF alignment defaults to pleasantries and sycophantic validation of incorrect operator assertions.
- **Never allow verbose narrations of routine command invocations:** Summarize tool executions crisply to keep conversation context lean and actionable.
