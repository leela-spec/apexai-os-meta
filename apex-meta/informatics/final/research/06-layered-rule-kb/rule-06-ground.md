---
type: Reference
id: V2-LAYERED-KB-RULE-06-GROUND
title: Rule 06 Deep-Dive — <ground> Semantic Block Decomposition, Value Audit & Compression Options
description: Decomposing <ground> (from 13-candidate-3A-xml.md) into atomic semantic blocks, evaluating token value, formulating tighter alternatives, and linking all internal and external research.
status: current_truth
tags: [layered-kb, rule-06, ground, semantic-blocks, token-compression, research-ledger]
---

# Rule 06 Deep-Dive: `<ground>` (`13-candidate-3A-xml.md`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (format siblings: [14-candidate-3B-hybrid.md](../../candidates/14-candidate-3B-hybrid.md), [15-candidate-3C-bullet-hybrid.md](../../candidates/15-candidate-3C-bullet-hybrid.md))
> - **Layer 1 (This File — Rule-Level Semantic Block Audit):** Decomposes `<ground>` into 4 atomic semantic blocks (`SB-06.1`..`SB-06.4`), audits token value against hallucination and lazy handoffs, and presents scored compression options.
> - **Layer 2 (Downstream Infrastructure Modules):** [anti-drift-rules.md](../../specs/anti-drift-rules.md) (`AD-19`, `AD-20`, `AD-06`), [writing-profile.md](../../specs/writing-profile.md) (`WP-04`, `WP-16`).

---

## 1. Original Rule & Atomic Semantic Block Inventory

### 1.1 Current `v1.0-3A` Full Text (`81 BPE block` | `76 BPE inner` | `98 repo tokens` | `393 chars` | `60 words`)

```xml
<ground>Verify against the originating artifact (path:line) or live tool output, never memory or a secondary summary. Absence, zero and count claims carry the command that produced them. Check what is checkable now instead of deferring it. For factual, design, version or tooling questions consult current authoritative sources — roughly three — grounded in the actual environment and version at hand.</ground>
```

### 1.2 Atomic Semantic Block Inventory (Bullet List)

Every token in `<ground>` belongs to one of four distinct semantic blocks (`SB-06.1` through `SB-06.4`), plus the XML tag wrapper (`<ground>...</ground>`, `5 BPE tokens`):

- **`SB-06.1` — Primary Artifact Grounding (`22 BPE tokens` | `109 chars`):** *"Verify against the originating artifact (path:line) or live tool output, never memory or a secondary summary."*
- **`SB-06.2` — Command-Carrying Negative Claims (`14 BPE tokens` | `68 chars`):** *"Absence, zero and count claims carry the command that produced them."*
- **`SB-06.3` — Non-Paralysis Immediate Verification (`12 BPE tokens` | `52 chars`):** *"Check what is checkable now instead of deferring it."*
- **`SB-06.4` — Rule of Three Authoritative Sources (`28 BPE tokens` | `161 chars`):** *"For factual, design, version or tooling questions consult current authoritative sources — roughly three — grounded in the actual environment and version at hand."*

---

## 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

### 2.1 Chapter `SB-06.1`: Primary Artifact Grounding
> **Current Text (`22 BPE tokens`):** `"Verify against the originating artifact (path:line) or live tool output, never memory or a secondary summary."`

- **What It Means & Failure Mode Addressed:** Mandates that every assertion of code or system state must cite exact file coordinates (`path:line`) or the verbatim output of a tool run in the current session. Relying on conversational memory, upstream summaries, or assumption is strictly prohibited.
- **Value & Necessity Critique (`[P0 | I98/E98/R04]` — Apex Epistemic Cornerstone):**
  - **Honest High-Reasoning Critique:** Frontier LLMs routinely hallucinate file contents or rely on outdated context from previous multi-turn turns. Requiring direct inspection of the originating artifact eliminates second-hand attribution drift and grounds every factual statement in verifiable bytes.
  - **Where It Has Fat:** 3 BPE tokens can be shaved by consolidating plural forms while retaining explicit `(path:line)` discipline.
- **Formulation Options:**
  - **Option A (Baseline — `22 BPE tokens`):** *"Verify against the originating artifact (path:line) or live tool output, never memory or a secondary summary."* `(I98/E98/R04)`
  - **Option B (Recommended Surgical Compression — `19 BPE tokens`, `−3 BPE`):** *"Verify against originating artifacts (path:line) or live tool outputs, never memory or summaries."* `(I98/E98/R04)`
  - **Option C (Aggressive Alternative — `18 BPE tokens`, `−4 BPE`):** *"Ground claims in originating artifacts (path:line) or live tool output, never memory."* `(I95/E95/R06)`

---

### 2.2 Chapter `SB-06.2`: Command-Carrying Negative Claims
> **Current Text (`14 BPE tokens`):** `"Absence, zero and count claims carry the command that produced them."`

- **What It Means & Failure Mode Addressed:** Forbids asserting that something does not exist ("no errors found", "zero linter issues", "no broken links") without quoting the exact shell or tool command that proved that absence.
- **Value & Necessity Critique (`[P1 | I92/E95/R06]` — Adversarial Proof Requirement):**
  - **Why It Earns Its Tokens:** Agents constantly claim "I verified the tests and nothing broke" without ever executing the test runner. Forcing negative and quantitative claims to carry their generating command makes false claims immediately detectable by human operators and automated review harnesses.
  - **Where It Has Fat:** 1 BPE token can be trimmed by restructuring into an active command.
- **Formulation Options:**
  - **Option A (Baseline — `14 BPE tokens`):** *"Absence, zero and count claims carry the command that produced them."* `(I92/E95/R06)`
  - **Option B (Recommended Surgical Compression — `13 BPE tokens`, `−1 BPE`):** *"State the command producing any absence, zero, or count claim."* `(I94/E96/R05)`
  - **Option C (Aggressive Alternative — `9 BPE tokens`, `−5 BPE`):** *"Zero and count claims carry the generating command."* `(I90/E93/R08)`

---

### 2.3 Chapter `SB-06.3`: Non-Paralysis Immediate Verification
> **Current Text (`12 BPE tokens`):** `"Check what is checkable now instead of deferring it."`

- **What It Means & Failure Mode Addressed:** If a claim, hypothesis, or file state can be tested using available tools, run the verification in the active turn instead of punting the question into an unresolved task list or delegating it to a handoff.
- **Value & Necessity Critique (`[P0 | I95/E95/R05]` — Anti-Deferral Operational Engine):**
  - **Why It Earns Its Tokens:** Autonomous agents often exhibit lazy deferral patterns, filling handoff reports with questions like "Verify if endpoint returns 200" when curl or python was directly available. Immediate verification closes feedback loops within the turn.
  - **Where It Has Fat:** The baseline formulation is already exceptionally compact.
- **Formulation Options:**
  - **Option A (Baseline — `12 BPE tokens`):** *"Check what is checkable now instead of deferring it."* `(I95/E95/R05)`
  - **Option B (Recommended Surgical Compression — `12 BPE tokens`, `+0 BPE`):** *"Check what is checkable now instead of deferring it."* `(I95/E95/R05)`
  - **Option C (Aggressive / Ultra-Short Alternative — `6 BPE tokens`, `−6 BPE`):** *"Check checkable facts now."* `(I88/E90/R12)`

---

### 2.4 Chapter `SB-06.4`: Rule of Three Authoritative Sources
> **Current Text (`28 BPE tokens`):** `"For factual, design, version or tooling questions consult current authoritative sources — roughly three — grounded in the actual environment and version at hand."`

- **What It Means & Failure Mode Addressed:** Directs the agent to cross-reference approximately three authoritative sources (official documentation, release notes, live package versions, active runtime flags) before finalizing architectural designs or dependency versions.
- **Value & Necessity Critique (`[P1 | I90/E92/R08]` — Hallucination Triangulation Guard):**
  - **Why It Earns Its Tokens:** Coding agents frequently pull obsolete API patterns from training cutoff memory (e.g., using deprecated Python 3.8 idioms in Python 3.12, or citing React 17 hooks in React 19). Triangulating across live sources anchors decisions in the current environment.
  - **Where It Has Fat:** Listing four noun categories and descriptive clauses consumes 28 BPE tokens. Option B condenses this down to 21 BPE tokens.
- **Formulation Options:**
  - **Option A (Baseline — `28 BPE tokens`):** *"For factual, design, version or tooling questions consult current authoritative sources — roughly three — grounded in the actual environment and version at hand."* `(I90/E92/R08)`
  - **Option B (Recommended Surgical Compression — `21 BPE tokens`, `−7 BPE`):** *"For factual, design, or version questions, cross-check ~3 authoritative sources grounded in the live environment."* `(I92/E93/R06)`
  - **Option C (Aggressive Alternative — `12 BPE tokens`, `−16 BPE`):** *"Cross-check version or factual queries across ~3 authoritative sources."* `(I86/E89/R10)`

---

## 3. Whole-Rule Recomposition Rollup for `<ground>`

| Rollup Option | Complete `<ground>` Text | BPE Tokens (`cl100k_base`) | Savings vs. Current `v1.0-3A` (`81 BPE`) |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<ground>Verify against the originating artifact (path:line) or live tool output, never memory or a secondary summary. Absence, zero and count claims carry the command that produced them. Check what is checkable now instead of deferring it. For factual, design, version or tooling questions consult current authoritative sources — roughly three — grounded in the actual environment and version at hand.</ground>` | **`81`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<ground>Verify against originating artifacts (path:line) or live tool outputs, never memory or summaries. State the command producing any absence, zero, or count claim. Check what is checkable now instead of deferring it. For factual, design, or version questions, cross-check ~3 authoritative sources grounded in the live environment.</ground>` | **`70`** | **`−11 BPE` (`−13.6%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<ground>Ground claims in originating artifacts (path:line) or live tool output, never memory. Zero and count claims carry the generating command. Check checkable facts now. Cross-check version or factual queries across ~3 authoritative sources.</ground>` | **`50`** | **`−31 BPE` (`−38.3%`)** |

---

## 4. Complete Bidirectional Research & Provenance Links for `<ground>`

### 4.1 Internal Project Research Corpus (`ResearchOfFile10` & `Universal AI Instruction System`)
- **Primary Research Packet (`RP-03` — Currency Check & Environmental Grounding):** [RESULTS-03-currency-check.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-03-currency-check.md)
- **Secondary Research Packet (`RP-05` — Grounding vs Inferred Acceptance Criteria):** [RESULTS-05-self-authored-criteria.md](../../research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-05-self-authored-criteria.md)
- **Universal Architecture Empirical Deepening:** [A08-evidence-integrity-uncertainty-calibration/README.md](../../research/01-universal-instruction-research/module-deepening/A08-evidence-integrity-uncertainty-calibration/README.md) and [A13-external-grounding-real-world-verification/README.md](../../research/01-universal-instruction-research/module-deepening/A13-external-grounding-real-world-verification/README.md)
- **Historical Contract Lineage:** [02-informatics-contract-block.md](../../candidates/02-informatics-contract-block.md) (`v0.3`) $\rightarrow$ [07-contract-block-v0.4.md](../../candidates/07-contract-block-v0.4.md) (`v0.4`) $\rightarrow$ [09-contract-block-v0.5.md](../../candidates/09-contract-block-v0.5.md) (`v0.5`) $\rightarrow$ [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (`v1.0-3A`).

### 4.2 External Peer-Reviewed & Benchmark Sources
- **SpecBench (2026):** [Benchmarking Specification Alignment in Coding Agents](https://arxiv.org/abs/2605.21384) — Measures the steep drop in execution precision when agents operate from unverified memory representations rather than grounded source citations.
- **BEIR Information Retrieval Benchmark:** Demonstrates the value of multi-source cross-verification in suppressing ungrounded model generations.

### 4.3 Canonical Plane 4 Infrastructure Modules & Operational Lore
- **Canonical Anti-Drift Owner (`AD-19`, `AD-20`, `AD-06`):** [anti-drift-rules.md](../../specs/anti-drift-rules.md)
- **Canonical Writing Profile Owner (`WP-04`, `WP-16`):** [writing-profile.md](../../specs/writing-profile.md)
- **Canonical Plane 3 Retrieval Skill:** [qmd/SKILL.md](../../../../../.agents/skills/qmd/SKILL.md) (`qmd get <path:line:count>` provides line-precise evidence citations grounding every claim).
- **Canonical Operational Decision Record:** [07-INTEGRATION-PLAN-AND-OPERATIONAL-DECISIONS.md](../../07-INTEGRATION-PLAN-AND-OPERATIONAL-DECISIONS.md) (`DEC-QMD-01` two-tier escalation and `DEC-QMD-04` surgical slicing).
- **Operational Lore Grounding:** [2Dos Ai Instructions.md](../../../../AI-Snippets/Orga/2Dos%20Ai%20Instructions.md) (*"Primary Grounding vs Secondary Citation"*), [Snippets.md](../../../../AI-Snippets/Snippets.md) (*"Command-Carrying Claims"*).

---

## 5. Failure Modes & Not-To-Dos (`WP-25`)

- **Never omit the explicit `(path:line)` citation format (`SB-06.1`):** Permitting loose file-level citations allows models to fabricate quotes or describe non-existent functions.
- **Never accept negative or zero-count assertions without the generating command (`SB-06.2`):** Unverified negative statements ("there are no lint errors") are the primary source of hidden regressions.
- **Never defer checks that can be executed in the current session (`SB-06.3`):** Punting simple tool executions wastes user turns and produces incomplete handoff states.
