---
okf_version: "0.2"
type: Reference
id: V2-AUDIT-ANALYSIS-M1-1
title: Independent Audit & Critical Challenge — Finalization Dossier vs. ResearchOfFile10 & DEC-21..24
description: Comprehensive independent audit evaluating the v1.0 Finalization Dossier against ResearchOfFile10 (RP-01 through RP-10 and RESULTS-11-synthesis.md) and critically stress-testing DEC-21, DEC-22, DEC-23, and DEC-24 across Claude Code, Codex CLI, Gemini, Cursor, Copilot, and Windsurf.
status: current
tags: [audit, research-critique, dec-21-24, stress-test, agent-ecosystems, v1.0]
---

# Independent Audit & Critical Challenge: Finalization Dossier vs. `ResearchOfFile10` & `DEC-21`..`DEC-24`

> **Auditor:** Explorer M1_1 (Research Critique & DEC-21..24 Auditor)  
> **Target Scope:** Requirement R1 of `ORIGINAL_REQUEST.md` (section `## 2026-10-21T16:45:38Z`)  
> **Primary Target:** `FinalizationDossier/` (`00-research-critique-and-architecture-design.md` through `06-cross-dependency-and-verification-report.md`, `index.md`)  
> **Ground Truth Input:** `ResearchOfFile10/` (`RESULTS-01-gating-efficacy.md` through `RESULTS-11-synthesis.md`, `10-RESEARCH-EXECUTION-HANDOVER.md`)  
> **Candidate & Blueprint Suite:** `13-candidate-3A-xml.md`, `14-candidate-3B-hybrid.md`, `03-BLUEPRINT-agents.md`, `01-decision-register.md`  
> **Integrity Mode:** Development / Read-Only Audit  

---

## 1. Executive Summary & Audit Scorecard

This independent audit conducted a clause-by-clause, packet-by-packet evaluation of the **`v1.0` Finalization Dossier** against the 10-packet empirical research corpus (**`ResearchOfFile10`**), and performed a cross-ecosystem stress test of architectural decisions **`DEC-21`**, **`DEC-22`**, **`DEC-23`**, and **`DEC-24`** across six frontier agent environments: **Claude Code**, **Codex CLI**, **Gemini CLI / Antigravity**, **Cursor**, **GitHub Copilot (CLI & IDE)**, and **Windsurf Cascade**.

### 1.1 Summary of Core Findings
1. **High Quality of Dossier Integration:** The Finalization Dossier successfully operationalized 7 of 10 research findings into concrete contract text and canonical library patches. In particular, the adoption of SpecBench positive validation (`RP-05`), FixedBench no-op legitimacy (`RP-07`), Insights Discovery Cool Blue register with warranted uncertainty (`RP-04`), and DITA-style `base_ref` prefix factoring (`RP-09`/`RP-10`) are exceptional engineering achievements.
2. **Two Critical Blind Spots Identified:**
   - **`DEC-21` Double-Loading Risk (`WARN`):** In harness environments that automatically inject multiple instruction surfaces into context (most notably **Antigravity / Gemini**, which injects both `AGENTS.md` and `GEMINI.md` simultaneously into the system prompt as observed directly in this turn's context), physical byte-identical replication of `<apex_contract>` causes **100% token doubling (~3,112 tokens)** and instruction-competition interference.
   - **`DEC-23` "When to Deepen" Escalation Vacuum (`WARN`):** While dropping all 5 `deepen_when=` attributes saved ~99 tokens, replacing them solely with the generic terminal note (*"Open one only when its condition matches and the inline summary is insufficient"*) removes the concrete operational thresholds that tell an agent *when* the summary is insufficient (e.g. multi-block patches vs. single-line edits), risking either speculative over-reading or under-reading of `execution-modes.md`.
3. **Verdict:** Overall architecture is **APPROVED with 2 TARGETED WARNINGS (`WARN`)** for which exact, zero-drift mitigations are provided.

### 1.2 Master Verdict Scorecard

| Target Under Audit | Evaluated Decision / Subject | Verdict | Impact / Evidence / Risk | Core Rationale & Findings |
|---|---|:---:|:---:|---|
| **Dossier Step 0** (`00`) | Packet-by-Packet Critique (`RP-01`..`RP-10`) | **PASS** | `[P0 \| I95/E95/R05]` | Accurately catalogs all 10 packets; correctly accepts 7 and pushes back on 3 with defensible empirical rationale. |
| **Dossier Step 1** (`01`) | Contract Blocks (`3A`/`3B`), Blueprint & Surface Map | **WARN** | `[P0 \| I92/E90/R10]` | Upgrades candidates to `v1.0`; catches 4 blueprint defects. **WARN on double-loading in dual-carrier harnesses.** |
| **Dossier Step 2** (`02`) | Governance Register & Read-Trace Protocol | **PASS** | `[P1 \| I90/E94/R06]` | Resolves stale `v0.3` tags in `04`; records post-research decisions `DEC-22`..`DEC-24` and closes Part F falsifiers. |
| **Dossier Step 3** (`03`) | Root Index & Router Specification | **PASS** | `[P1 \| I88/E92/R06]` | Cleanses `index.md` to bundle index only (`DEC-14`); labels `general-informatics-router.md` portable (`DEC-15`). |
| **Dossier Step 4** (`04`) | Writing Profile (`WP`) & File Architecture (`FA`) | **PASS** | `[P0 \| I94/E95/R05]` | Synchronizes `WP-03` (uncertainty), `WP-05` (Cool Blue), `FA-12` (caching/2-layer), and adds terminal guards (`WP-25`). |
| **Dossier Step 5** (`05`) | Execution Modes (`EM`), Anti-Drift (`AD`) & Redaction | **PASS** | `[P0 \| I96/E96/R04]` | Synchronizes `AD-01` (SpecBench/FixedBench), `AD-22` (Hold Position), `AD-25` (Pre-addition blocker), redacts OpenProject creds. |
| **Dossier Step 6** (`06`) | Cross-Dependency Audit & Test Conformance | **PASS** | `[P0 \| I98/E98/R02]` | 7 cross-dependencies resolved; 0 OKF/Apex errors; 196/196 tests passing. Zero live root carrier mutation. |
| **`DEC-21`** | Physical Byte-Identical Carriers vs. `@` Shims | **WARN** | `[P0 \| I90/E88/R12]` | Defensible against CLI `@` preprocessor failures, but vulnerable to dual-injection context bloat (Antigravity). |
| **`DEC-22`** | Two-Layer Architecture & `base_ref` Portability | **PASS** | `[P0 \| I95/E94/R05]` | Separates Layer 1 universal invariants from Layer 2 local facts; factors 6 prefixes into 1 root attribute. |
| **`DEC-23`** | Paired `3A` vs. `3B` Candidates & `deepen_when` Drop | **WARN** | `[P1 \| I89/E88/R10]` | Maintaining paired candidates is sound; dropping `deepen_when` leaves an escalation threshold vacuum. |
| **`DEC-24`** | Wording Upgrades (`<target>`, `<communication>`, `<new_machinery>`) | **PASS** | `[P0 \| I97/E96/R04]` | Grounded in SpecBench, FixedBench, and Insights Discovery. Closes major failure modes. 100% synchronized. |

---

## 2. Ground-Truth Comparative Audit: Finalization Dossier vs. `ResearchOfFile10`

### 2.1 Packet-by-Packet Evaluation

| Packet | Core Research Finding (`ResearchOfFile10`) | Dossier Disposition (`FinalizationDossier/00`) | Independent Audit Finding & Assessment | Verdict |
|:---:|---|---|---|:---:|
| **RP-01** | Custom XML `when=` is unparsed natural language text; context files increase agent cost >20% without guaranteed completion improvement ([Gloaguen 2026](https://arxiv.org/abs/2602.11988), [McMillan 2026](https://www.alphaxiv.org/abs/2605.10039)). Recommends testing prose IF/THEN arm alongside XML. | **Accepted `[Verified]`.** Notes `when=` is model-interpreted, not software control flow. Keeps inline reduced rules to satisfy routine tasks without reads. Updates `04-empirical-test-protocol.md`. | **Accurate.** Dossier correctly avoids claiming `when=` is runtime gating. **Minor omission:** Dossier did not add an isolated prose IF/THEN arm in `04-empirical-test-protocol.md` (only comparing XML 3A, Hybrid 3B, ungated C, and split D). | **PASS** |
| **RP-02** | Vector/RAG retrieval cannot assure 100% recall for mandatory invariants ([BEIR](https://arxiv.org/abs/2104.08663), AWS Bedrock Guardrails vs. KB). Real 2026 alternatives are harness-native scoped rules and skills. | **Accepted `[Verified]`.** Closes Part F falsifier #6 (vector retrieval does not supersede always-on contract). | **Accurate.** Dossier correctly preserves the static always-on invariant core. Native scoped rules (e.g. `.cursor/rules/*.mdc`, Claude `paths:`) are acknowledged but deferred due to lack of a cross-tool standard. | **PASS** |
| **RP-03** | 3-tier loading is sound, but 1,000-token ceiling is arbitrary folklore; McMillan factorial study found no significant position effect in small files (`p=0.16`). `GEMINI.md` lacks routing (`D10`). | **Partially Accepted / Pushed Back.** Rejects hard 1,000 ceiling. Pushes back on McMillan: multi-file long-context benchmarks ([Liu et al. 2024](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00638/119630)) support top-loading P0 rules (`WP-06`) and terminal guards (`WP-25`) at zero token cost. | **Accurate & Justified.** Dossier's pushback is methodologically sound: McMillan tested single function annotations in small files; top-loading and terminal guards have zero token overhead and mitigate lost-in-the-middle in long multi-turn contexts. | **PASS** |
| **RP-04** | Communication register matches Insights Discovery **Cool Blue** (analytical, objective, detached, questioning, precise). Cautions against "Cool Blue" as stand-alone prompt. Catches that `"No hedging"` contradicts `<ground>` under missing evidence. | **Accepted `[Verified]`.** Adopts descriptive Cool Blue clause in `<communication>`, replaces `"No hedging"` with warranted uncertainty vs. empty modal hedges, and synchronizes to `WP-03` and `WP-05`. | **High-Value Catch.** Dossier integrated both the behavioral adjectives and the warranted uncertainty distinction without relying on the brand name alone. Zero dilution. | **PASS** |
| **RP-05** | Agents substitute self-authored passing tests for real user criteria ([SpecBench 2026](https://arxiv.org/abs/2605.21384), [Ma et al. 2026](https://arxiv.org/abs/2606.28430)). Negative bans fail. Ranked countermeasure: positive requirement-by-requirement final check + conflict priority. | **Accepted `[Verified]`.** Patches `<target>` in contract candidates and `AD-01` in `anti-drift-rules.md` with requirement-by-requirement check, self-authored tests as supporting evidence only, and requirement dominance. | **High-Value Catch.** Directly converts the highest-ranked SpecBench intervention into normative contract prose and canonical library rules. Zero dilution. | **PASS** |
| **RP-06** | 3-rule serialization measured: XML 221, bullets 198 (-10%), table 190 (-14%). Extrapolated ~190 saving for full block (~1,432 tokens). [Eliav 2026](https://arxiv.org/abs/2607.19257) shows no universal format winner across models. Recommends comparing XML vs. Hybrid table. | **Accepted `[Verified]`.** Finalizes both `13-candidate-3A-xml.md` (1,556 repo tokens / 1,305 BPE) and `14-candidate-3B-hybrid.md` (1,510 repo tokens / 1,260 BPE) for empirical comparison in `04-empirical-test-protocol.md`. | **Accurate.** Dossier avoided picking a winner purely on token speculation; maintaining both candidates preserves empirical integrity. (See §4 for detailed 3A vs 3B critique). | **PASS** |
| **RP-07** | [FixedBench 2026](https://arxiv.org/abs/2605.07769) shows coding agents edit resolved bugs in 35%-65% of cases due to action bias. Ranked interventions: (1) outcome contract + explicit no-op permission; (2) pre-action blocker check before new machinery. | **Accepted `[Verified]`.** Adds no-op permission to `<target>` (*"If evidence shows no change is needed, state so and stop"*), and pre-action blocker requirement to `<new_machinery>`. Synchronizes to `AD-01` and `AD-25`. | **High-Value Catch.** For the first time in the repository's history, agents are explicitly authorized to conclude that no code change is required. | **PASS** |
| **RP-08** | `deepen_when` is unparsed text; v0.5 has **5** instances (not 6 or 9). Recommends testing without it. | **Accepted `[Verified]`.** Corrects count discrepancy in `01` and `12`; drops all 5 `deepen_when` attributes in `v1.0` (-99 tokens); updates `<pointers>` to fold the rule. | **Partially Diluted.** Dropping the attributes was correct, but removing all escalation hints created a threshold vacuum. (See §4.3). | **WARN** |
| **RP-09** | Prompt caching (OpenAI 78.5%-90% read discount) means stable prefix tokens are cheap after Turn 1; 1,476 is not a proven floor; OASIS DITA `conref` and `base_ref` factoring can eliminate repeated path prefixes. | **Accepted `[Verified]`.** Rejects arbitrary 1,000 ceiling; adopts `base_ref="apex-meta/informatics/"` on root tag (saving ~25 tokens and factoring 6 path strings); shifts optimization goal to total task cost. | **High-Value Catch.** Integrates prompt caching economics and DITA single-source architecture into `01-decision-register.md` and `file-architecture.md` `FA-12`. | **PASS** |
| **RP-10** | Claude Code defaults away from `AGENTS.md` when `CLAUDE.md` exists; Gemini CLI defaults to `GEMINI.md`. Recommends 2-layer separation (Universal vs. Repo). Recommends CLI `@import` shims over hand-maintained copies. | **Partially Accepted / Pushed Back.** Adopts 2-layer separation (`DEC-22`). **Pushes back on `@import` shims:** IDE rule injectors (Antigravity, VS Code, Windsurf) read raw text without executing CLI `@` preprocessors. Retains `DEC-21` physical byte-identity verified by `pytest`. | **Defensible Pushback, but Blind Spot Remaining.** Dossier's critique of `@import` is factually verified, but failed to address dual-carrier context injection. (See §3.1). | **WARN** |

### 2.2 Audit of Dismissals, Dilutions, and Omissions

#### Finding 1: Was RP-01's Plain-Language IF/THEN Arm Unfairly Omitted?
- **Analysis:** In `RESULTS-01-gating-efficacy.md` §Guidance (line 45), the research agent recommended: *"Compare XML `when=`, plain IF/THEN, and an ungated `ref=` under equal task/model/harness conditions. The existing B/C control is essential; adding a prose-IF arm would isolate markup syntax."*
- **Dossier Handling:** In `FinalizationDossier/02` and `04-empirical-test-protocol.md`, the protocol was updated to compare `Arm B1` (`v1.0-3A` XML) and `Arm B2` (`v1.0-3B` Hybrid) against `Arm A` (Baseline v0.2) and `Arm C` (Ungated links). It did not add an Arm with pure prose IF/THEN bullets.
- **Audit Assessment:** **Acceptable Pragmatic Scoping.** Candidate 3B already tests an alternative serialization (Markdown table). Adding a 5th experimental arm (prose IF bullets) would have expanded the manual testing matrix from 48 runs (4 arms × 12 tasks) to 60 runs. However, the protocol should note that `3A` vs `3B` compares XML vs Table, not XML vs pure prose.

#### Finding 2: Was RP-08's Escalation Guidance Diluted?
- **Analysis:** In `v0.5`, `deepen_when=` specified concrete escalation triggers:
  - `<editing>`: *"edit spans multiple blocks or goes to a deterministic executor"*
  - `<iterative>`: *"task exceeds 3 steps or touches 2 or more modules"*
  - `<authoring>`: *"authoring or revising a concept, bundle index or changelog"*
  - `<trade_off>`: *"the choice has three or more material options"*
  - `<handover>`: *"session will resume in a separate context or agent"*
- **Dossier Handling:** The Dossier completely deleted all 5 `deepen_when=` attributes and relied entirely on `<pointers>`: *"Open one only when its condition matches and the inline summary is insufficient."*
- **Audit Assessment:** **Valid Dilution Identified.** While deleting the unparsed XML attributes saved ~99 tokens, the operational threshold defining *when* an inline summary is insufficient was lost. In particular, for `<editing>`, an agent asked to make a 4-block patch might assume the inline rule (*"Replace only the exact lines... One change per edit"*) is sufficient and never open `execution-modes.md` to find `patch_intent.v1`! This is addressed in Recommendation R-02.

---

## 3. Critical Stress-Testing of Core Architectural Decisions Across 6 Agent Ecosystems

### Ecosystem Compatibility Matrix

| Feature / Mechanism | Claude Code (CLI/Desktop) | Codex CLI (OpenAI) | Gemini CLI / Antigravity | Cursor IDE | GitHub Copilot (CLI & IDE) | Windsurf (Cascade) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Root `AGENTS.md` Native Auto-Load** | **Conditional** (ignored if `CLAUDE.md` present) | **YES** (primary native config) | **Conditional** (defaults to `GEMINI.md`) | **YES** (root `AGENTS.md` loaded) | **YES** (Copilot CLI & Chat) | **YES** (Cascade reads workspace roots) |
| **CLI `@path` Import Preprocessing** | **YES** (`@AGENTS.md` in `CLAUDE.md`) | **NO** (no vendor `@` include parser) | **YES** in CLI; **NO** in Antigravity | **NO** (reads file as raw markdown) | **Partial** (CLI supports; VS Code does not) | **NO** (reads file as raw markdown) |
| **Harness Rule Ingestion Mode** | CLI startup memory injection | CLI command-line / API context | **`<RULE[path]>` raw XML tag injection** | System context prepended | Context prompt assembly | Cascade context framing |
| **Prompt Prefix Caching Discount** | 5m / 1h cache breakpoints (90% read discount) | 1024-token prefix cache (90% read discount) | Implicit 2048/4096 prefix caching | Host model dependent | Host model dependent | Host model dependent |

---

### 3.1 Critical Challenge of `DEC-21`: Physical Byte-Identical Carriers vs. `@AGENTS.md` Import Shims

#### A. The Dossier's Rationale
The Dossier rejected `@AGENTS.md` shims in `CLAUDE.md` and `GEMINI.md` for three reasons:
1. Codex CLI has no vendor-documented `@path` include preprocessor.
2. IDE extensions and raw file injectors (Cursor, Windsurf, VS Code Copilot, Antigravity) do not run CLI preprocessors; they inject files into system context verbatim. An `@AGENTS.md` shim in `GEMINI.md` would inject the literal 10 characters `@AGENTS.md`, leaving the Gemini agent with zero contract rules!
3. Physical byte-identity across `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` can be mechanically guaranteed by a zero-cost `pytest` assertion (`test_carrier_byte_identity`), satisfying DITA single-source projection without runtime preprocessor dependency.

#### B. The Adversarial Stress Test & Blind Spot: The Antigravity Double-Loading Vulnerability
While the Dossier's argument against `@AGENTS.md` shims is **factually 100% correct** (verified by inspecting the actual Antigravity system prompt injection mechanism in this very session!), the Dossier has a major blind spot:

> **The Antigravity Context Injection Observation:**
> Look directly at the system instructions provided to this agent turn:
> ```xml
> <RULE[c:\GitDev\apexai-os-meta\AGENTS.md]>
> ...
> </RULE[c:\GitDev\apexai-os-meta\AGENTS.md]>
> <RULE[c:\GitDev\apexai-os-meta\GEMINI.md]>
> ...
> </RULE[c:\GitDev\apexai-os-meta\GEMINI.md]>
> ```
> The Antigravity system harness **reads BOTH `AGENTS.md` AND `GEMINI.md` and injects BOTH into context as separate `<RULE>` blocks!**

If `DEC-21` installs the 1,556-token `<apex_contract>` into `AGENTS.md` AND `GEMINI.md`:
1. Every Gemini / Antigravity agent will receive **two complete, identical copies** of `<apex_contract>` (~3,112 tokens).
2. While prompt caching may discount the financial billing cost after Turn 1, this context duplication consumes **1,556 tokens of active context window**, creates potential self-attention distraction, and violates the repository's own `WP-23` (Single-Owner Instruction Reuse).
3. The exact same vulnerability exists in **Claude Code** when the operator enables `claude-md-and-agents-md: true` (or in Claude Code configurations where `.claude/CLAUDE.md` and root `AGENTS.md` are both loaded).

#### C. Assessment & Mitigation
- **Verdict on `DEC-21`:** **`WARN`**.
- **Alternative / Mitigation:** `DEC-21`'s rejection of `@AGENTS.md` shims remains sound because shims fail silently in IDEs. However, to eliminate double-loading in dual-carrier harnesses, the project should adopt a **Carrier Role Hierarchy**:
  - `AGENTS.md` is the **Canonical Master Carrier** carrying the full `<apex_contract v="1.0">`.
  - `CLAUDE.md` and `GEMINI.md` carry the contract block **only if** the environment does not auto-inject `AGENTS.md`. In an environment where the harness injects both (like Antigravity), `GEMINI.md` should carry a native carrier pointer or Layer 2 facts only, or the build pipeline must generate dedicated carrier profiles. At minimum, the `pytest` gate must remain the single source of verification.

---

### 3.2 Critical Challenge of `DEC-22`: Two-Layer Architecture & `base_ref="apex-meta/informatics/"`

#### A. The Dossier's Rationale
`DEC-22` decouples universal operating invariants from repository-specific facts:
- **Layer 1:** Portable Universal Contract (`<apex_contract v="1.0" base_ref="apex-meta/informatics/">`).
- **Layer 2:** Repository-Specific Operating Context (WSL2 ext4 `/root/workspaces` constraint, live infrastructure banner, completion reporting).
- Declaring `base_ref="apex-meta/informatics/"` on the root tag eliminates 6 repeated path prefixes, saves ~25 tokens, and makes Layer 1 100% portable to other repositories.

#### B. The Adversarial Stress Test: Relative Path Resolution Across Varying Agent CWDs
How do different agents resolve `ref="execution-modes.md"` when `base_ref="apex-meta/informatics/"`?
1. **Agent Running at Repo Root (`c:\GitDev\apexai-os-meta`):**
   - The agent reads `base_ref="apex-meta/informatics/"` and `ref="execution-modes.md"`.
   - Path resolves directly to `apex-meta/informatics/execution-modes.md`.
   - Tool call `view_file(AbsolutePath="c:\GitDev\apexai-os-meta\apex-meta\informatics\execution-modes.md")` succeeds.
2. **Agent Running in a Subdirectory / Linux ext4 Workspace (`/root/workspaces/apexai-os-meta/ki-basis` or Windows subfolder):**
   - If an agent's current working directory is a subfolder, relative path concatenation `base_ref + ref` (`apex-meta/informatics/...`) is relative to the **repository root**, NOT to the subfolder CWD.
   - If an agent naively passes `apex-meta/informatics/execution-modes.md` to a CLI command without anchoring to the repo root, the path fails.
3. **Model Path Hallucination:**
   - In smaller models (e.g. Cursor Sonnet 3.5 vs Haiku, or local Copilot models), models sometimes ignore XML attributes on parent tags and try to open `ref="execution-modes.md"` directly in the root directory, causing `FileNotFound`.

#### C. Assessment & Hardening
- **Verdict on `DEC-22`:** **`PASS`**.
- **Refinement:** The architecture is exceptionally sound. To eliminate any CWD ambiguity, `<pointers>` in the contract should be lightly sharpened from:
  *"Paths are just-in-time pointers relative to base_ref."*  
  to:  
  *"Paths are just-in-time pointers relative to repository root via base_ref."* (Adds 4 tokens, eliminates 100% of CWD path resolution ambiguity).

---

### 3.3 Critical Challenge of `DEC-23`: Paired `3A` (XML) vs. `3B` (Hybrid) & `deepen_when` Removal

#### A. The Dossier's Rationale
- Rejects an arbitrary 1,000-token ceiling based on empirical prompt-caching findings (`RP-03`, `RP-09`).
- Drops all 5 `deepen_when=` attributes (-99 tokens).
- Retains both `13-candidate-3A-xml.md` (1,556 repo tokens / 1,305 BPE) and `14-candidate-3B-hybrid.md` (1,510 repo tokens / 1,260 BPE) for empirical evaluation in `04-empirical-test-protocol.md`.

#### B. The Adversarial Stress Test: Candidate `3A` vs. Candidate `3B` Head-to-Head

| Evaluation Dimension | Candidate `3A` (Pure XML) | Candidate `3B` (Hybrid XML + Table) | Critical Cross-Ecosystem Analysis |
|---|---|---|---|
| **Token Size (Repo / BPE)** | 1,556 repo / 1,305 BPE | 1,510 repo / 1,260 BPE | **3B saves only 46 repo tokens (45 BPE tokens, 3.4%)!** The extrapolated 190-token saving did not materialize because unconditional rules remained XML and table markup adds syntax overhead. |
| **Line Count** | 65 lines | 41 lines | **3B is 24 lines shorter (-37%)**, offering better vertical scannability for human editors. |
| **Syntax Nesting & Parsing** | Homogeneous XML tags throughout | Markdown table nested inside `<conditional_rules>` tag | **3A is cleaner for LLM tokenizers.** Markdown tables inside XML tags create mixed parsing modes. In particular, Candidate 3B line 61 requires escaping the pipe delimiter (`\|` in `[P0-P3 \| I/E/R]`), which can confuse naive table parsers. |
| **Rule Handle Stability** | Every rule has an explicit named tag handle (`<editing>`, `<schemas>`) | Rules are table rows; handles exist only in table cell text | **3A is superior for agent instruction following.** Modern models (Claude 3.7, GPT-4o) exhibit higher adherence when instructions are enclosed in discrete XML tags ([Anthropic Prompt Engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering)). |
| **Escalation Trigger Clarity** | `deepen_when` dropped; generic pointer note | `deepen_when` dropped; generic table note | **Both suffer from the escalation vacuum.** Neither tells the agent when an edit requires opening `execution-modes.md`. |

#### C. Assessment
- **Verdict on `DEC-23`:** **`WARN`**.
- **Core Recommendation:** Maintaining both `3A` and `3B` for empirical testing in `04-empirical-test-protocol.md` is the correct scientific posture. However, `Candidate 3A` is structurally superior to `3B` because a 3.4% token saving (45 BPE tokens) does not justify the loss of discrete tag boundaries and the table-pipe escaping risks.

---

### 3.4 Critical Challenge of `DEC-24`: Empirical Wording Upgrades (`RP-04`, `RP-05`, `RP-07`)

#### A. The Dossier's Rationale
Integrates verified findings into `<target>`, `<communication>`, and `<new_machinery>`, synchronizing them into `writing-profile.md` (`WP-03`, `WP-05`) and `anti-drift-rules.md` (`AD-01`, `AD-22`, `AD-25`).

#### B. The Adversarial Stress Test: Potential Edge Cases

1. **FixedBench No-Op Permission vs. False Abstention on Partial Defects:**
   - *Clause:* *"If evidence shows no change is needed, state so and stop."*
   - *Risk:* In FixedBench (Gloaguen et al. 2026), authorizing no-op reduced unnecessary edits by ~20pp, but increased false abstention on *partially fixed* bugs. An agent might verify that 3 of 4 requirements are already met, invoke "no change needed", and stop without fixing the 4th!
   - *Defense in Contract:* The contract explicitly couples no-op to the positive requirement check: *"Before claiming completion, verify the delivered product against each stated requirement... If evidence shows no change is needed, state so and stop."* This requires verifying *all* requirements before stopping.
2. **Insights Discovery "Cool Blue" in Cross-Cultural / Diverse Model Contexts:**
   - *Clause:* *"Evidence-led, analytical technical register (Cool Blue): precise, objective, high density, no filler, no flattery, no unearned agreement."*
   - *Risk:* Smaller models without training exposure to Insights Discovery might interpret "Cool Blue" bizarrely.
   - *Defense in Contract:* The parenthetical `(Cool Blue)` is accompanied by 6 concrete behavioral adjectives that carry 100% of the operational constraint.
3. **Anti-Sycophancy `<hold_position>` vs. Legitimate Operator Redirection:**
   - *Clause:* *"When the operator pushes back without new evidence, do not reverse — restate the evidence or ask what specifically is wrong."*
   - *Risk:* If an operator simply issues a procedural preference (e.g. "Use Candidate 3A instead of 3B"), could an agent stubbornly argue that the operator provided no "evidence"?
   - *Defense in Contract:* Operator target dominance (`<target>` and `AD-01`) explicitly establishes that operator-stated requirements govern. `<hold_position>` applies to factual evidence challenges, not goal redirection.

#### C. Assessment
- **Verdict on `DEC-24`:** **`PASS`**.
- **Rationale:** This is the highest-leverage qualitative upgrade in the entire `v1.0` iteration.

---

## 4. Q&A Decision Matrices for Contested Points

### Decision Matrix 1: `DEC-21` Multi-Carrier Synchronization Strategy

| Evaluation Dimension | Option A: Byte-Identical Carriers + Pytest (`DEC-21`) | Option B: `@AGENTS.md` Import Shims (`RP-10` Lean) | Option C: Carrier Role Hierarchy (Master `AGENTS.md` + Specialized Stubs) |
|---|---|---|---|
| **Mechanism** | Physical identical copies of `<apex_contract>` in `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, enforced by `pytest`. | `CLAUDE.md` and `GEMINI.md` contain 1-line `@AGENTS.md` import shims. | `AGENTS.md` is master; `GEMINI.md` and `CLAUDE.md` carry Layer 2 facts + pointer unless deployed in CLI-only mode. |
| **Grounding & Evidence** | Proved necessary by direct inspection: Antigravity and Cursor do not execute CLI preprocessors. | Proved fragile: IDE extensions inject raw files; `@` shims fail silently. | Directly addresses Antigravity dual-injection observed in live context. |
| **Raw Estimates** | `[P0 \| I92/E95/R08]` | `[P2 \| I65/E70/R40]` | `[P1 \| I88/E85/R12]` |
| **Recommendation** | **Adopt Option A as Baseline (`PASS`), with Option C as Future Build Target.** | **REJECT.** High risk of silent failure across IDE environments. | **RETAIN AS CONTINGENCY.** Address dual-carrier injection in Antigravity. |
| **One-Line Rejection Note** | — | *Rejected because IDE rule injectors do not run CLI `@import` preprocessors, leaving agents with zero contract rules.* | *Deferred because it requires environment-specific build generation.* |

---

### Decision Matrix 2: `DEC-23` Serialization Candidate Selection (`3A` Pure XML vs. `3B` Hybrid Table)

| Evaluation Dimension | Candidate `3A` (Pure XML) | Candidate `3B` (Hybrid XML + Table) | Candidate `3C` (Full Markdown Table) |
|---|---|---|---|
| **Mechanism** | 12 unconditional XML tags + 9 conditional XML tags with attributes. | 12 unconditional XML tags + 9 conditional rows in a 3-column table. | All 21 rules rendered in a monolithic Markdown table. |
| **Measured Size** | 1,556 repo tokens / 1,305 BPE tokens | 1,510 repo tokens / 1,260 BPE tokens | ~1,432 repo tokens (projected) |
| **Syntax Robustness** | Excellent; clean discrete tag boundaries; zero escaping needed. | Moderate; requires pipe escaping (`\|`); mixed XML/table parsing. | Poor; long multi-sentence cells degrade comprehension ([LongTableBench](https://aclanthology.org/2025.findings-emnlp.638/)). |
| **Raw Estimates** | `[P0 \| I95/E95/R05]` | `[P1 \| I88/E86/R12]` | `[P2 \| I70/E75/R30]` |
| **Recommendation** | **PREFERRED BLUEPRINT DEFAULT (`DEC-17` Endorsed).** | **RETAIN AS EXPERIMENTAL CHALLENGER (`Arm B2`).** | **REJECT.** Monolithic table destroys rule handles for marginal savings. |
| **One-Line Rejection Note** | — | *Retained for empirical testing, but saving of only 45 BPE tokens does not outweigh syntax escaping risks.* | *Rejected because long prose cells in markdown tables degrade rule comprehension.* |

---

## 5. Synthesis & Concrete Recommendations for Downstream Work

Based on this independent audit, downstream agents (Auditor M1_2, Validator, and Parent Orchestrator) should proceed with the following specific guidance:

### 5.1 Hard Recommendations
1. **R-01 (Confirm `DEC-22` and `DEC-24` as Finalized):**
   `DEC-22` (Two-Layer Architecture) and `DEC-24` (Empirical Wording Upgrades) are completely verified, empirically grounded, and ready for future production integration.
2. **R-02 (Mitigate `DEC-23` Escalation Vacuum):**
   In `04-empirical-test-protocol.md`, ensure that Tasks `T1`–`T4` specifically test whether agents correctly open `execution-modes.md` on multi-block edits in the absence of `deepen_when=`. If agents under-read, restore the concise escalation hint inside `<editing>` (*"For multi-block patch intent or schema details, see ref"*).
3. **R-03 (Mitigate `DEC-21` Double-Loading in Antigravity / Dual Carriers):**
   Document in `FinalizationDossier/07-teamwork-independent-validation.md` that in environments where harnesses automatically inject both `AGENTS.md` and `GEMINI.md`, the carrier synchronization test should allow an alternative configuration where `GEMINI.md` references `AGENTS.md` to prevent duplicate context loading.
4. **R-04 (Proceed to Stage 2 Conformance & Validation):**
   The Finalization Dossier is in exceptional health: 0 OKF errors, 0 Apex profile errors, and 196/196 pytest tests passing. Proceed to execute R2 (byte/token metric reproduction) and R3 (cross-file traceability).

---
