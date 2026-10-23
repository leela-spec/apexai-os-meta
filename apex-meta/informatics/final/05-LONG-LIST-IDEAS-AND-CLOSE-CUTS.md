---
type: Reference
id: V2-FINAL-LONG-LIST-IDEAS
title: Long List — Unimplemented Ideas, Close Cuts, Discarded Options & Architectural Backlog
description: Permanent documentation system capturing all architectural ideas, close-cut formulations, discarded format models, and future optimization concepts discussed during the informatics design cycle.
status: current
tags: [informatics, final, long-list, close-cuts, ideas-backlog, architectural-incubator]
---

# Long List: Unimplemented Ideas, Close Cuts & Architectural Backlog

> **Purpose:** This file acts as the permanent repository for ideas, alternative formats, close-cut formulations, and rejected paths discussed during the informatics optimization process. No insight or debate is lost. While the **Shortlist** ([candidates/13-candidate-3A-xml.md](candidates/13-candidate-3A-xml.md)) contains only the active, battle-tested operative contracts, this **Long List** preserves the full design space for future reference and experimentation.

---

## 1. Architectural & Referencing Ideas

### IDEA-01: Layered Dual-Key Reference Protocol (Saved per Operator Directive)
- **Concept:** Pair an immutable semantic XML handle (e.g., `<target>`) with an ordinal human catalog number (e.g., `Rule 01`) and sub-rule semantic block IDs (`SB-01.1`..`SB-01.4`).
- **Why Discussed:** Aimed to provide conversational convenience ("check Rule 1") while protecting against off-by-one renumbering breakage when rules are added or re-ordered.
- **Why Deferred from Shortlist:** The operator correctly identified that the contract is consumed **by AI agents**, not humans. Adding ordinal numbers into the prompt introduces unnecessary token overhead and risks positional rigidity. Pure semantic XML tags (`<target>`) are already 100% position-independent, parse cleanly, and carry zero ordinal baggage.
- **Future Application:** Reserved for human-facing documentation portals, interactive HTML dashboards, or visual inspection tools.

### IDEA-02: Micro-Split File Architecture for `execution-modes.md` (`DEC-16`)
- **Concept:** Physically split `execution-modes.md` (4,208 tokens) into 6 per-adapter standalone files (`adapter-1-qa-matrix.md`, `adapter-2-bakeoff.md`, etc.).
- **Close-Cut Debate:** In-file conditional branches save 0 tokens once loaded. Splitting would theoretically cut patch-task loading from 4,208 down to 713 tokens (−83%).
- **Why Deferred:** [McMillan (2026)](https://www.alphaxiv.org/abs/2605.10039) demonstrated that over-fragmenting files can increase exploratory tool calls by 40% if agents fail to honor gates.
- **Disposition:** Gated on empirical testing in [candidates/04-empirical-test-protocol.md](candidates/04-empirical-test-protocol.md) (`Arm B1` vs. `Arm C`).

### IDEA-03: DITA Topic Projection Compiler (Build-Time Single-Sourcing)
- **Concept:** Store instructions in one master DITA/OKF XML file and auto-compile them at build time into `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md`.
- **Disposition:** Recommended for future multi-repo scaling. For now, `Option A` (physical byte-identical copies verified by `pytest`) provides a zero-dependency baseline.

---

## 2. Close-Cut Rule Formulations & Discarded Variations

### CUT-01: Format Candidate 3B (Conditional Table Inside `<conditional_rules>`)
- **Text:** [candidates/14-candidate-3B-hybrid.md](candidates/14-candidate-3B-hybrid.md)
- **Close-Cut Trade-Off:** Replaced 9 XML gated tags with a 3-column Markdown table (`When | Operative Rule | Ref`). Saves 36 BPE tokens.
- **Why Relegated:** The 36-token saving is negligible (<3% of total block) and creates zero prompt cache block savings, while introducing pipe-escaping (`\|`) fragility and cell collapse under 80-column line wrapping.

### CUT-02: Format Candidate 3C (Bold-Bullet Unconditionals `- **Label**: ...`)
- **Text:** [candidates/15-candidate-3C-bullet-hybrid.md](candidates/15-candidate-3C-bullet-hybrid.md)
- **Close-Cut Trade-Off:** Replaced 12 unconditional XML tags with `- **Target**: ...`. Saves 15 BPE tokens (`3C-1`) or 51 BPE tokens (`3C-2`).
- **Why Relegated:** XML tags provide distinct opening and closing semantic boundaries (`<target>...</target>`) that LLM attention mechanisms parse with higher boundary fidelity than bold markdown spans. Preserved in `candidates/` as an experimental challenger.

### CUT-03: The 5 Dropped `deepen_when=` Attributes
- **Baseline:** `v0.5` had `deepen_when=` on `<editing>`, `<authoring>`, `<trade_off>`, `<handover>`, and `<iterative>`.
- **Research Finding (`RP-08`):** `deepen_when=` has no native runtime parser in any CLI and cost 99 tokens.
- **Resolution:** Pruned from the XML attribute list, but their operative escalation triggers (`AST patches`, `tier definitions`, `bake-offs`, `delegation contracts`, `route ladder/MMM`) were preserved as concise inline `Open ref for ...` cues in both `3A` and `3B`.

---

## 3. RLHF Default-Behavior Ablation Queue (`Arm I`)

[RESULTS-09-efficiency-audit.md](research/03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md) identified five clauses in `v1.0-3A` that may represent default frontier-model behavior:

1. **`<reuse>` General Tool Check:** Does Claude 4.x / GPT-5 already check installed tools before writing custom scripts without being instructed?
2. **`<context>` JIT Loading Opening Clause:** Does *"Load just-in-time. Never bulk-read directories at start"* add value over the specific per-step file persistence clause?
3. **`<recovery>` Incidental Failure Retry:** Do modern coding CLIs already retry transient errors?
4. **`<communication>` Active Voice / One Imperative:** Does explicit command styling change model output quality versus concise technical prose alone?
5. **`<iterative>` Single-Step Direct Execution:** Do models need to be told to execute single-step tasks directly?

**Testing Strategy:** These 5 candidates are pre-registered in [candidates/04-empirical-test-protocol.md](candidates/04-empirical-test-protocol.md) (`Arm I`, Tasks `T1`–`T16`) to measure regression rates if trimmed.

---

## 4. Failure Modes & Idea Lifecycle Protocol (`WP-25`)

- **Never re-introduce a dropped idea without empirical evidence:** Items in this Long List must demonstrate a measurable benchmark advantage before being promoted to the Shortlist.
- **Never delete discarded history:** When an option is rejected during architecture bake-offs, record its mechanism, grounding, and one-line rejection reason in this document.
