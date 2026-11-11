---
type: Reference
id: V2-LAYERED-KB-RULE-23-ALIGN
title: Rule 23 Deep-Dive — <align> Semantic Block Decomposition, Value Audit & Optimization
description: Complete 5-section semantic block decomposition (SB-23.1..SB-23.8) for <align>, empirical critique of verbatim prompt echo, Goal/Tasks/Subtasks decomposition, flowing Input, L0-L3 Redraft scaling, resolved TODO-EM-13-A reasoning frameworks, and BPE metrics.
status: current_truth
tags: [layered-kb, rule-23, align, em-13, semantic-blocks, token-compression, research-ledger]
---

# Rule 23 Deep-Dive: `<align>` (`apex_contract_v1.0_ultra.xml`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Live Master Contract):** [`specs/apex_contract_v1.0_ultra.xml`](../../specs/apex_contract_v1.0_ultra.xml) (`<align>` added after the initial 22-rule `3A` freeze; baseline trigger refined in [`C1`](../../operations/20-CHANGE-RECORD-2026-11-06-07.md)).
> - **Layer 1 (This File — Rule-Level Semantic Block Audit):** Decomposes `<align>` into 8 atomic semantic blocks (`SB-23.1`..`SB-23.8`), audits field design and token efficiency (`cl100k_base` & `o200k_base`), resolves `TODO-EM-13-A`, and documents the 2026-11-11 upgrade (`Goal` + `Tasks -> Subtasks`, flowing `Input`, two-phase `ref` pre-read, and `EM-06a`-scaled `Redraft`).
> - **Layer 2 (Downstream Canonical Owner):** [`specs/execution-modes/task-specification.md`](../../specs/execution-modes/task-specification.md) (`EM-13`), paired with [`iterative-execution.md`](../../specs/execution-modes/iterative-execution.md) (`EM-10`), [`qa-decision-matrix.md`](../../specs/execution-modes/qa-decision-matrix.md) (`EM-06a`), and [`execution-modes.md`](../../specs/execution-modes.md).

---

## 1. Baseline Rule & Atomic Semantic Block Inventory

### 1.1 Pre-Upgrade `2026-11-07` Master Text (`179 BPE block` `cl100k_base` | `187 BPE` `o200k_base` | `139 BPE inner` | `198 repo tokens` | `794 chars` | `126 words`)

```xml
<align when="the task is non-trivial, not a direct question, and not already defined by a previous step" ref="specs/execution-modes/task-specification.md">
Before acting, restate the task once and wait for confirmation. Six fields, no preamble:
- **Input**: the literal ask, verbatim.
- **Sources**: the artifacts you will open.
- **Process**: how you will get and verify the facts, and the reasoning framework if you use one.
- **Skills**: the tools or skills you will invoke, or none.
- **Output**: what you will change, and what the deliverable is.
- **Redraft**: the shape of the future output - its headers with what each will contain and the value it carries; or concrete examples where specific detail was asked for.
Open ref for definitions and the failure each field prevents.
</align>
```

### 1.2 Atomic Semantic Block Inventory (`SB-23.1`..`SB-23.8`)

Every token in the `2026-11-07` `<align>` baseline belongs to one of 8 semantic blocks plus the XML wrapper (`40 BPE cl100k` / `41 BPE o200k`, `164 chars`):

- **`SB-23.1` — Pre-Action Approval Gate (`19 BPE cl100k` / `20 o200k` | `88 chars`):** *"Before acting, restate the task once and wait for confirmation. Six fields, no preamble:"*
- **`SB-23.2` — Field 1 Literal Input (`11 BPE cl100k` / `12 o200k` | `39 chars`):** *"- **Input**: the literal ask, verbatim."*
- **`SB-23.3` — Field 2 Planned Sources (`10 BPE cl100k` / `11 o200k` | `43 chars`):** *"- **Sources**: the artifacts you will open."*
- **`SB-23.4` — Field 3 Verification & Framework (`22 BPE cl100k` / `23 o200k` | `97 chars`):** *"- **Process**: how you will get and verify the facts, and the reasoning framework if you use one."*
- **`SB-23.5` — Field 4 Tooling & Skills (`15 BPE cl100k` / `16 o200k` | `59 chars`):** *"- **Skills**: the tools or skills you will invoke, or none."*
- **`SB-23.6` — Field 5 Deliverable Scope (`16 BPE cl100k` / `17 o200k` | `64 chars`):** *"- **Output**: what you will change, and what the deliverable is."*
- **`SB-23.7` — Field 6 Disposable Preview (`35 BPE cl100k` / `36 o200k` | `171 chars`):** *"- **Redraft**: the shape of the future output - its headers with what each will contain and the value it carries; or concrete examples where specific detail was asked for."*
- **`SB-23.8` — Field Mechanics Pointer (`11 BPE cl100k` / `11 o200k` | `61 chars`):** *"Open ref for definitions and the failure each field prevents."*

---

## 2. Chapter-by-Chapter Semantic Block Audit & Alternatives

### 2.1 Chapter `SB-23.1` & Wrapper: Trigger Ambiguity and Pre-Read Dispatch
> **Baseline (`40 + 19 BPE cl100k`):** `when="... and not already defined by a previous step"` + *"Before acting, restate the task once and wait for confirmation. Six fields, no preamble:"*

- **Failure Mode Addressed:** Frontier coding agents burn turns executing the wrong design under unprompted action bias (`FixedBench 2026`, `68%–91%` over-modification rate). Conversely, restating every already-approved step stalls multi-step loops (`C1` trigger refinement `2026-11-06`).
- **Two Defects Identified (`2026-11-11`):**
  1. `"already defined by a previous step"` was undefined (`rule-23-align.md` archival backlog): agents could treat their own prior analysis as authorization to skip alignment (`<scope>`: analyzing never authorizes implementing). Changing the trigger to *"not already defined by an approved step"* and defining approved steps in `task-specification.md` closes self-authorization.
  2. In [`operations/17`](../../operations/17-READ-TRACE-PILOT-AND-BASE-REF-FRAGILITY-FINDINGS.md) (`0/2` `<handover>`/`<trade_off>`) and [`01-findings-and-protocol.md`](../08-read-trace-routing-experiments/01-findings-and-protocol.md) Stage 1 (`1/36` `<authoring>`, `0/9` `<editing>`/`<trade_off>`), post-hoc `Stop` hooks and `.claude/rules/` `paths:` globs apply only to Claude Code ([`operations/15`](../../operations/15-PROSE-TO-DETERMINISTIC-TRANSLATION-FINDINGS.md)). Cross-agent execution across Codex (`AGENTS.md` hierarchy) and Gemini (`GEMINI.md` + `@path`) requires pairing `<align>` with `<pointers>` in a **two-phase plan-then-execute gate**: list matched conditional `ref`s and open them *before* acting or delivering final output.
- **Formulation Options:**
  - **Option A (Baseline — `19 BPE inner`):** *"Before acting, restate the task once and wait for confirmation. Six fields, no preamble:"* `(I84/E80/R15)`
  - **Option B (Recommended — `20 BPE inner`, `+1 BPE`):** *"Before acting, open matched conditional refs, state six fields (no preamble), and wait for confirmation:"* `(I95/E88/R08)`
  - **Option C (Aggressive — `19 BPE inner`, `+0 BPE`):** *"Before acting, open matched refs, align in six fields (no preamble), wait for confirmation:"* `(I90/E84/R14)`

---

### 2.2 Chapters `SB-23.2` & `SB-23.3`: Replacing Prompt Echo with `Goal` (`Tasks -> Subtasks`) & Flowing `Input`
> **Baseline (`11 + 10 = 21 BPE cl100k`):** *"- **Input**: the literal ask, verbatim."* + *"- **Sources**: the artifacts you will open."*

- **Why `SB-23.2` ("the literal ask, verbatim") Failed in Practice `[P0 | I94/E90/R06]`:**
  - Echoing the user's prompt verbatim duplicates text already in the conversation turn, adds token overhead (>20% cost inflation per Gloaguen et al. 2026 without improving success), and captures conversational wording instead of **flowing context** (opened `ref` specs, assumptions, and exclusions).
  - Omitting explicit **Goal** decomposition hides `Tasks` and `Subtasks` relationships, violating Story Mapping hierarchies ([Jeff Patton](https://www.jpattonassociates.com/)) and aggravating constraint omissions ([`SpecBench 2026`](https://arxiv.org/abs/2605.21384), `42.7%` full-spec alignment).
  - Elevating **`Goal`** (`outcome + constraints, decomposed into Tasks -> Subtasks when multi-step`) to Field 1 and folding **`Sources`** into flowing **`Input`** keeps **exactly six fields** and aligns `<align>` 1-to-1 with `<iterative>` (`EM-10`).
- **Formulation Options (`Field 1 + Field 2` combined):**
  - **Option A (Baseline — `21 BPE cl100k`):** Literal `Input` + `Sources` (no `Goal` decomposition). `(I72/E85/R25)`
  - **Option B (Recommended — `47 BPE cl100k`, `+26 BPE`):** `Goal` (`Tasks -> Subtasks`) + flowing `Input` (`sources, opened ref specs, assumptions, exclusions; never copy-paste the prompt`). `(I96/E92/R06)`
  - **Option C (Aggressive — `32 BPE cl100k`, `+11 BPE`):** Compressed `Goal` (`nested Tasks -> Subtasks`) + `Input` (`flowing sources, opened refs, assumptions, exclusions`). `(I91/E88/R12)`

---

### 2.3 Chapters `SB-23.4`, `SB-23.5`, `SB-23.6`: `Process` (+ Resolved `TODO-EM-13-A`), `Skills`, `Output`
> **Baseline (`22 + 15 + 16 = 53 BPE cl100k`):** `Process`, `Skills`, `Output`.

- **`Process` & Empirical Resolution of `TODO-EM-13-A` (`2026-11-11`):**
  - `task-specification.md:45` previously claimed *"the ranked set of highest-impact reasoning frameworks is already researched in this corpus"*.
  - Exhaustive live check (`git grep -n -i -E "framework|critical path|..."` across `apex-meta/informatics/` and `apex-meta/AI-Snippets/` plus `qmd search` across all 45 collections) proved **no internal ranked reasoning-framework study exists** (written ungrounded at initial commit `1a7f1e82`, `2026-11-02`).
  - Rather than inventing synthetic weights (`WP-07`), `task-specification.md` §8.3 now provides a curated, practical named-framework guide linked to existing Apex modes: First Principles / 5-Whys root-cause, Dependency / Critical Path sequencing, SCQA / Minto Pyramid (`WP-12`), Divergence-Convergence, Premortem / Inversion, Q&A Decision Matrix (`EM-06`), and Comparison Bake-Off (`EM-07`).
  - Tightening `Process` to verification commands, matched modes, and named framework saves `-5 BPE` (`22 -> 17 BPE cl100k`).
- **`Output` Per-Subtask Mapping (`16 -> 18 BPE cl100k`):** Mapping target changes and deliverables per subtask keeps nested `Goal -> Output -> Redraft` symmetry across multi-step plans.
- **Formulation Options (`SB-23.4 + 23.5 + 23.6`):**
  - **Option A (Baseline — `53 BPE cl100k`):** Wordy phrasing, unmapped subtasks. `(I86/E84/R12)`
  - **Option B (Recommended — `49 BPE cl100k`, `−4 BPE`):** Compact `Process` (`17`), `Skills` (`14`), and subtask-mapped `Output` (`18`). `(I94/E90/R06)`
  - **Option C (Aggressive — `35 BPE cl100k`, `−18 BPE`):** Telegraphic bullets (`12 + 11 + 12`). `(I88/E85/R12)`

---

### 2.4 Chapters `SB-23.7` & `SB-23.8`: `EM-06a`-Scaled `Redraft` & Escalation Pointer
> **Baseline (`35 + 11 = 46 BPE cl100k`):** 30-word `Redraft` description + generic pointer.

- **Critique (`[P0 | I93/E90/R08]`):** `SB-23.7` consumed 35 tokens yet lacked intensity scaling and per-subtask user-story framing (Jeff Patton Story Mapping + Specification by Example `Given-When-Then`). Meanwhile, full multi-persona simulations on low-risk edits waste finite attention budget (Anthropic *Effective Context Engineering for AI Agents*). Scaling `Redraft` dynamically by `EM-06a` (`L0` skip -> `L1` outline/story -> `L2` worked example per subtask -> `L3` edge-case scenarios) trims `-10 BPE` (`35 -> 25 BPE`) while matching effort to stakes.
- **`SB-23.8`:** Pointing directly at field boundaries and approved-step criteria (`11 -> 10 BPE cl100k`, `−1 BPE`) directs agents to the updated §8 rules.
- **Formulation Options (`SB-23.7 + 23.8`):**
  - **Option A (Baseline — `46 BPE cl100k`):** 30-word `Redraft` prose + generic pointer. `(I85/E85/R14)`
  - **Option B (Recommended — `35 BPE cl100k`, `−11 BPE`):** Scaled `Redraft` (`25 BPE`) + crisp approved-step pointer (`10 BPE`). `(I94/E90/R07)`
  - **Option C (Aggressive — `24 BPE cl100k`, `−22 BPE`):** Minimal shorthand (`18 + 6 BPE`). `(I87/E82/R15)`

---

## 3. Whole-Rule Recomposition Rollup for `<align>`

| Rollup Option | Summary Shape | `cl100k_base` | `o200k_base` | Delta vs. `2026-11-07` (`179 cl` / `187 o2`) |
|---|---|---:|---:|---|
| **1. `2026-11-07` Baseline (Option A)** | `Input` (literal prompt), `Sources`, `Process`, `Skills`, `Output`, `Redraft` (unscaled) | **`179`** | **`187`** | `0` (`0.0%`) |
| **2. Recommended Upgrade (Option B)** | Two-phase `ref` pre-read + `Goal` (`Tasks->Subtasks`), flowing `Input`, `Process`, `Skills`, `Output`, `L0-L3` `Redraft` | **`191`** | **`198`** | **`+12 cl` (`+6.7%`)** / **`+11 o2`**, `-12` words (`126 -> 114`) |
| **3. Aggressive Compact (Option C)** | Telegraphic headers with `Tasks -> Subtasks` and `L0-L3` | **`149`** | **`156`** | **`−30 cl` (`−16.8%`)** / **`−31 o2`** |

---

## 4. Complete Bidirectional Research & Provenance Links for `<align>`

### 4.1 Internal Corpus Evidence & Specs
- **Canonical Spec Owner (`EM-13`):** [`task-specification.md`](../../specs/execution-modes/task-specification.md) (§8–§8.4)
- **Scaling & Preflight Siblings:** [`qa-decision-matrix.md`](../../specs/execution-modes/qa-decision-matrix.md) (`EM-06a`), [`iterative-execution.md`](../../specs/execution-modes/iterative-execution.md) (`EM-10`), [`handover.md`](../../specs/execution-modes/handover.md) (`EM-14`)
- **Empirical Failure & Harness Traces:** [`operations/15`](../../operations/15-PROSE-TO-DETERMINISTIC-TRANSLATION-FINDINGS.md), [`operations/17`](../../operations/17-READ-TRACE-PILOT-AND-BASE-REF-FRAGILITY-FINDINGS.md), [`operations/20`](../../operations/20-CHANGE-RECORD-2026-11-06-07.md) (`C1`, `M6`), [`01-findings-and-protocol.md`](../08-read-trace-routing-experiments/01-findings-and-protocol.md), [`19-MAUSBOT-INSTALLATION-RECORD.md`](../../operations/19-MAUSBOT-INSTALLATION-RECORD.md)

### 4.2 External Research & Engineering Literature (Verified `2026-11-11`)
- **Anthropic Engineering:** *Effective Context Engineering for AI Agents* — Context rot, high-signal minimal tokens, JIT retrieval over eager pre-loading, plan-execute isolation.
- **Gloaguen et al. (ETH Zurich / ICLR 2026 Workshop):** *Evaluating AGENTS.md* — Unnecessary context bloat inflates inference cost >20% without improving task success.
- **[SpecBench (2026)](https://arxiv.org/abs/2605.21384) & [FixedBench (2026)](https://arxiv.org/abs/2605.07769):** Multi-constraint omission (`42.7%` compliance) and unprompted edit bias (`68%–91%`) motivating pre-action alignment.
- **[Jeff Patton User Story Mapping](https://www.jpattonassociates.com/) & Specification by Example (`Given-When-Then`):** Horizontal `Goal -> Tasks -> Subtasks` backbone paired with concrete worked examples.
- **Living SSOT Specs vs. Snapshots (`Fission-AI/OpenSpec` vs. GitHub Spec Kit):** Updating one living spec via explicit deltas instead of accumulating stale one-off snapshots.

---

## 5. Failure Modes & Not-To-Dos (`WP-25`)

- **Never copy-paste the user's raw prompt into `Input`:** Synthesize flowing sources, opened `ref` specs, assumptions, and exclusions (`Goal` holds the required outcome).
- **Never treat `<align>`'s "already defined by an approved step" exception as self-authorized by prior analysis:** Only explicit operator approval, an approved plan step, or trivial `Route 0` typos/lookups bypass `<align>`.
- **Never skip opening matched conditional `ref` files when `<align>` or a conditional `when=` triggers:** Two-phase planning requires reading matched `ref`s *before* editing or writing final output across all agent harnesses.
- **Never emit heavyweight `L3` persona simulations for routine `L1` edits:** Scale `Redraft` granularity dynamically to decision risk and reversibility (`EM-06a`).
