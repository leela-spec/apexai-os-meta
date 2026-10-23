---
type: Reference
id: V2-FINAL-EXECUTION-PLAN-AND-THINKING-PROCESS
title: Layered Knowledge Base Architecture, Thinking Process & QMD Integration Strategy
description: Authoritative ledger of the design trajectory, architectural decisions, thinking processes, semantic block decomposition methodology, execution milestones, and QMD vector retrieval integration.
status: current_truth
tags: [execution-plan, thinking-process, architecture, layered-kb, qmd, semantic-blocks, token-optimization]
---

# Layered Knowledge Base Architecture, Thinking Process & QMD Strategy

> **Location:** `apex-meta/informatics/final/06-EXECUTION-PLAN-AND-THINKING-PROCESS.md`  
> **Associated Artifact:** `thinking_process_and_execution_plan.md`  
> **Complements:** [index.md](index.md), [01-decision-register.md](candidates/01-decision-register.md), [05-LONG-LIST-IDEAS-AND-CLOSE-CUTS.md](05-LONG-LIST-IDEAS-AND-CLOSE-CUTS.md), [07-INTEGRATION-PLAN-AND-OPERATIONAL-DECISIONS.md](07-INTEGRATION-PLAN-AND-OPERATIONAL-DECISIONS.md).

---

## 1. Context, Trajectory & The Core Architectural Problem

### 1.1 How We Arrived Here
The Apex Informatics Instruction System evolved through distinct generational leaps:
1. **`v0.3` Baseline (`02-informatics-contract-block.md`):** Early 24-rule draft, verbose, mixing formatting requirements with core operational invariants.
2. **`v0.4` & `v0.5` Refining (`07-contract-block-v0.4.md`, `09-contract-block-v0.5.md`):** Tightened prose, introduced conditional JIT escalation pointers (`deepen_when=`).
3. **`ResearchOfFile10` (10-Packet Research Corpus):** Grounded the rules in empirical research and benchmarks:
   - `RESULTS-01` (XML vs. Markdown gating)
   - `RESULTS-04` (Cool Blue register & warranted uncertainty)
   - `RESULTS-05` (SpecBench: self-authored acceptance criteria failure modes)
   - `RESULTS-07` (FixedBench: over-building, RLHF modification bias, and no-op legitimacy)
   - `RESULTS-08` (Removal of redundant, unparsed `deepen_when=` attributes)
   - `RESULTS-09` & `RESULTS-10` (`base_ref` Layer 1 portability and Two-Layer Carrier Architecture).
4. **`v1.0-3A` Pure XML (`13-candidate-3A-xml.md`, 1,350 BPE tokens):** Established as the canonical master specification with 22 semantic tags. Formats `3B` (Hybrid) and `3C` (Bullet-Hybrid) were created strictly as layout projections.
5. **Deterministic Relocation (`apex-meta/informatics/final/`):** All active candidates, blueprints, and upstream research corpora (`01-universal-instruction-research`, `02-deep-reasoning`, `03-research-of-file-10`, `04-finalization-dossier`, `05-analysis-after-research`) were deterministically moved into `final/` with zero modification to historical research bytes.

---

## 2. Key Architectural Decisions & Thinking Process

### Decision 1: AI-Facing Semantic Tags vs. Human Numbering
- **User Insight:** The contract block is consumed by LLMs, not printed on human posters. Adding human-facing numbers (`Rule 1: Target`, `1.`, `2.`) introduces positional fragility, cascading renumbering invalidations when rules move, and wastes tokens on redundant ordinal metadata.
- **Resolution:** The AI contract block retains immutable semantic XML tags (`<target>`, `<product_first>`, `<scope>`, etc.). The proposed "dual-key reference system" was preserved strictly as an idea in [05-LONG-LIST-IDEAS-AND-CLOSE-CUTS.md](05-LONG-LIST-IDEAS-AND-CLOSE-CUTS.md) (`IDEA-01`).

### Decision 2: Three-Layer Knowledge Architecture
To prevent bloating the always-on contract while avoiding shallow guidelines, the architecture is stratified into three distinct layers:
- **Layer 0 (Essence Contract — Always On):** `13-candidate-3A-xml.md` (and its compressed successor `16-candidate-3A-ultra.md`). Embedded directly into agent instruction surfaces (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`). Zero fluff, non-default invariants only.
- **Layer 1 (Layered Rule Knowledge Base — Rationale & Compression Ledger):** `research/06-layered-rule-kb/` (`rule-01-target.md` through `rule-22-pointers.md`). Deconstructs every rule into atomic Semantic Blocks (`SB-XX.k`), audits default RLHF behavior vs. high-leverage non-default discipline, provides Options A/B/C, and links upstream research.
- **Layer 2 (Canonical Plane 4 Infrastructure Modules — JIT Deep Specs):** `writing-profile.md`, `file-architecture.md`, `execution-modes.md`, `anti-drift-rules.md`, `governance-schemas.md`. Deep reference documentation loaded JIT via `ref="..."` pointers only when an agent needs the full specification.

### Decision 3: Semantic Block Decomposition Methodology
Every rule is treated as a composite bundle of atomic semantic blocks (`SB-XX.k`). For each block:
- **Default Behavior Audit:** Does the sentence merely command what frontier models already do by default (e.g. *"Deliver what the user asked"*), or does it counteract an empirical RLHF bias (e.g. *"Tests you author are supporting evidence, never replacement criteria"* [SpecBench, 42.7% compliance]; *"If evidence shows no change is needed, state so and stop"* [FixedBench, 68%–91% false modification rate])?
- **Option A (Baseline):** Current text as in `3A`.
- **Option B (Recommended Surgical Compression):** Maximum information density, zero semantic loss, active voice, tightened phrasing. Target of ~30% token reduction across the contract.
- **Option C (Aggressive / Cross-Rule Alternative):** Deeper structural compression, cross-rule deduplication (e.g. deduplicating test-passing clauses between `<target>` and `<product_first>`), fusion, or alternative syntax.

### Decision 4: Format Candidate 3C (Bullet-Hybrid Projection)
- Created [15-candidate-3C-bullet-hybrid.md](candidates/15-candidate-3C-bullet-hybrid.md) testing bold-bullet unconditionals (`- **Target**: [paragraph]`) with XML conditional gating (`3C-1`: `1,335` BPE tokens) and conditional markdown tables (`3C-2`: `1,299` BPE tokens).
- Established that all rule text originates canonically in `3A`, and `3B`/`3C` are derivative formatting projections.

---

## 3. Active Execution Roadmap & Milestones

The construction of the Layered Rule Knowledge Base and `3A-Ultra` candidate is tracked across 5 milestones:

| Milestone | Target Scope | Output Files | Status |
|---|---|---|---|
| **M1: Rules 02–08** | Product First, Scope, Communication, Hold Position, Ground, Reuse, Context | `rule-02.md` through `rule-08.md` | **COMPLETE & SIGNED OFF** (112/112 links valid) |
| **M2: Rules 09–15** | Recovery, Stop Repairing, Current Truth, Surgical, Editing, New Machinery, Detour | `rule-09.md` through `rule-15.md` | **COMPLETE & SIGNED OFF** (125/125 links valid) |
| **M3: Rules 16–22** | Authoring, Trade-Off, Handover, Iterative, Schemas, Sync, Pointers | `rule-16.md` through `rule-22.md` | **COMPLETE & SIGNED OFF** (123/123 links valid) |
| **M4: Module Audits** | 5 Plane 4 Infrastructure Modules | `audit-module-01.md` through `audit-module-05.md` | **COMPLETE & SIGNED OFF** (~151.8 KB analysis) |
| **M5: 3A-Ultra Rollup** | `16-candidate-3A-ultra.md` (~950 BPE target / 1,225 empirical BPE) & index linking | `16-candidate-3A-ultra.md`, `06-layered-rule-kb/index.md` | **COMPLETE & SIGNED OFF** (338/338 pytest green) |

---

## 4. QMD Vector Database Integration Strategy

### 4.1 Analysis: Does it make sense to let QMD index `apex-meta/informatics/final/`?
**Verdict: YES, STRONGLY RECOMMENDED.**

#### Why QMD Provides Immediate Architectural Leverage:
1. **The Scale of the Research Corpus:** `apex-meta/informatics/final/` contains over 100 deep technical markdown files across `research/01` through `research/06`.
2. **Semantic vs. Lexical Gap:** Standard `grep` / `ripgrep` requires knowing exact keywords. When an agent seeks *"empirical failure rate when agents write their own tests"*, `rg` may fail if the file uses *"SpecBench benchmark evaluation on self-authored criteria"*. QMD uses **hybrid search** combining BM25 keyword matching with **Gemma-300M vector embeddings** and **Qwen3-0.6B cross-encoder reranking**.
3. **Context Window Protection:** Rather than reading entire 500-line research files into context to check a citation or background rationale, an agent or human can query QMD, retrieve the top 3 relevant chunks with scores, and pull only the necessary lines.
4. **Agent Integration via MCP:** QMD natively exposes an MCP server (`qmd mcp`). Once indexed, any agent session can query the research corpus directly via tool calls.

#### What QMD Does NOT Replace (The Discipline Boundary):
- QMD is a **retrieval tool**, not an authoring authority. It does not replace deterministic verification of active contract files (`13-candidate-3A-xml.md`, `16-candidate-3A-ultra.md`) or running `okf_validator.py` and `pytest`.
- It serves as the **high-speed semantic bridge** between Layer 0 (the contract), Layer 1 (the rule rationale), and the massive historical research corpora in `final/research/`.

---

## 5. Instructions for Running QMD in Another Chat/Terminal

To index `apex-meta/informatics/final` in QMD without interrupting ongoing execution, run the following commands in PowerShell:

### Step 1: Add the Collection to QMD
```powershell
# Add the 'apex-informatics-final' collection pointing to the final directory
qmd collection add "c:\GitDev\apexai-os-meta\apex-meta\informatics\final" --name "apex-informatics-final" --mask "**/*.md"
```

### Step 2: Attach Descriptive Context to Guide the Search Engine
```powershell
# Add top-level context explaining what this collection contains
qmd context add "apex-informatics-final" "Canonical Apex Informatics v1.0 specifications, contract block candidates (3A, 3B, 3C, 3A-Ultra), Layered Rule Knowledge Base (Rules 01-22), and comprehensive empirical research corpora (ResearchOfFile10, Universal AI Instruction System, Deep Reasoning, and Finalization Dossier)."
```

### Step 3: Generate Vector Embeddings
```powershell
# Generate embeddings using local Gemma-300M model
qmd embed -c "apex-informatics-final"
```

### Step 4: Verify Collection Health & Search
```powershell
# Check status and verify documents/vectors count
qmd status

# Test a hybrid search query across the new collection
qmd query "SpecBench self-authored acceptance criteria failure rate" -c "apex-informatics-final"

# Test finding empirical no-op legitimacy findings
qmd query "FixedBench over-building unnecessary modifications" -c "apex-informatics-final"
```

### Step 5: Optional — Enable MCP for Agent Sessions
```powershell
# To expose this knowledge base via MCP to Antigravity or other agents:
qmd mcp
```
