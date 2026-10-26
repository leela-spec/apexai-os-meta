# Original User Request

## 2026-10-19T16:12:11Z

Design, modularize, and formalize the next-generation, ultra-token-efficient Apex Informatics Architecture and Instruction System. Create a consolidated general router file (to be embedded directly into agent instruction surfaces) with conditional "IF-clauses" that route JIT into an extensible modular specification suite. Every file must enforce a **Significance & Ranking System** (P0–P3 tiers + raw 3-metric estimates: Impact, Evidence, Risk) so that the most established, battle-proven, and token-efficient rules appear first. All metrics and ceilings are pragmatic orientations with explicit rule-breaking authority when clarity requires it. Draw freely from the Universal AI Instruction System research (`module-deepening/`), `2Dos Ai Instructions.md`, and `Snippets.md` as empirical evidence repositories.

Working directory: `c:\GitDev\apexai-os-meta\apex-meta\informatics`
Integrity mode: development

## Reference Materials
- **Empirical Rule Deepening Corpus:** `c:\GitDev\apexai-os-meta\apex-meta\handoff\universal-ai-instruction-system\module-deepening\` (A01–A13, C01–C03)
- **Universal Architecture & Pilot Contract:** `c:\GitDev\apexai-os-meta\apex-meta\handoff\universal-ai-instruction-system\08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md`
- **Global Snippet Grammar:** `c:\GitDev\apexai-os-meta\apex-meta\handoff\universal-ai-instruction-system\02-GLOBAL-SNIPPET-GRAMMAR.md`
- **Operational Lore & Snippets:** `c:\GitDev\apexai-os-meta\apex-meta\AI-Snippets\Orga\2Dos Ai Instructions.md` & `c:\GitDev\apexai-os-meta\apex-meta\AI-Snippets\Snippets.md`
- **Empirical Context & Primacy Authority:** `apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__ai_handling_routing/2Do_context_file_authority_reference.md`

## Requirements

### R1. Significance Ranking Architecture (P0–P3 + 3-Metric Estimates)
Establish a clear ranking and ordering orientation across generated files:
- **Priority Tiers (P0–P3):**
  - **P0 (Critical Invariant / Non-negotiable):** Universal safety, target dominance, and non-negotiable boundaries.
  - **P1 (Core Method / High Impact):** Primary operational patterns, essential structural rules, and standard workflows.
  - **P2 (Standard Practice / Medium Impact):** Contextual conventions, formatting ergonomics, and secondary heuristics.
  - **P3 (Advisory / Contextual):** Optimization hints, stylistic polish, and edge-case exceptions.
- **Three-Metric Qualitative/Quantitative Estimates:** Every rule or option provides raw estimates (scale 1–100) for the 3 core dimensions without computing any mathematical formula:
  - **Impact (I):** Value, effectiveness, target orientation.
  - **Evidence (E):** Grounding, empirical support, battle-proven track record.
  - **Risk (R):** Misjudgment potential, operational complexity, downside aftermath.
  - Tagged using the standardized syntax: `[P<tier> | I<impact>/E<evidence>/R<risk>]` (e.g., `[P0 | I95/E95/R10]`).
- **Top-Loaded Primacy:** Rules in every file should generally be ordered descending by importance (P0 -> P1 -> P2 -> P3, prioritizing highest Impact/Evidence and lowest Risk). Aim to position critical invariants near the top (within the first ~500 tokens) where model attention is highest.

### R2. Approximate Ceilings, Token Economy & Exception Authority
Formulate numeric targets as operational orientations rather than rigid, fragile walls:
- **Target Router Size:** The consolidated general router should aim for an approximate ceiling of ~100 lines and ~400 tokens as a baseline efficiency guideline, placing primary IF-dispatch gates near the top.
- **Approximate Chunk & Sentence Targets:** Aim for ~150 words per prose block before breaking into a table or list; target ~20 words per procedural sentence and ~25 words per descriptive sentence; prefer active voice and single-command sentences.
- **Heading Depth Guideline:** Prefer <= 3 heading levels (`#`, `##`, `###`) for scannability, but allow deeper nesting if a complex technical structure genuinely requires it.
- **Directive Density Guidance:** Keep directive density proportional to model capacity (~50 directives for GPT-4o / Claude Standard, ~80 for Claude Reasoning, ~100 for Gemini / o3).
- **Rule-Breaking & Exception Authority (Substance Over Ceremony):** An agent or author is explicitly permitted to exceed an approximate ceiling or relax a stylistic constraint whenever strict adherence would harm technical accuracy, omit load-bearing context, create artificial distortions, or produce unnatural prose. Substantive realization of the target always overrides mechanical metric compliance.

### R3. Consolidated General Router (To Be Planted in Agents)
Create a compact, unified root router (`index.md` / `general-informatics-router.md`) designed to be embedded into `AGENTS.md` and agent role cards:
- Uses lean XML tags with clean Markdown bodies (`<informatics when="..." ref="..." deepen_when="...">`).
- Formulates clear conditional "IF-clauses": an agent reads only the top-level trigger, and *if and only if* that specific action is demanded, it loads the linked deeper file JIT.
- Eager `@path` imports are strictly prohibited; enforces tool-based JIT retrieval.

### R4. Extensible Modular Specification Suite (Foundational Triad + Extensions)
Decompose repository informatics into modular, single-responsibility files. The core triad serves as the foundation, but the team is explicitly empowered to identify and add further modular files:
1. **`writing-profile.md` (Writing & Prose Ergonomics):** Information Mapping, "One Chunk, One Job", approximate STE limits, visual block targets, durable IDs vs. ordinary labels.
2. **`file-architecture.md` (File Creation & Bundle Structure):** OKF v0.2 frontmatter schemas, Five-Plane Information Architecture, concept/index/changelog layout, strict current-truth separation (zero inline changelogs), and top-loaded primacy.
3. **`execution-modes.md` (Task Adapters & Execution If-Clauses):**
   - *If Q&A Game / Decision Matrix:* apply structured options, grounding, raw 3-metric estimates `(I<val>/E<val>/R<val>)`, recommendation, and one-line rejection notes. No mathematical formulas.
   - *If Comparison / Bake-Off:* multi-metric candidate matrix, common criteria, calibrated qualitative scoring.
   - *If File Mutation / Patch:* deterministic AST/regex exact-match patch intent discipline (`patch-intent-schema.json`) with automated git rollback.
   - *If Handover / Handoff:* intent/outcome focus, input/process/output definition, DoD, and anti-drift boundaries.
   - *If Iterative Execution (MMM):* complexity routing (Route 0 direct, Route 1 compact preflight, Route 2 full spec), top-down decomposition, and bottom-up verification.
4. **Additional Specialized Modules (As Justified by Domain Analysis):** The team may introduce further dedicated files (e.g., `governance-schemas.md`, `validation-profiles.md`, or specialized agent adapters) if analysis reveals distinct architectural boundaries.

### R5. Synthesis of Empirical Research & Operational Snippets
Distill the best elements of the `module-deepening/` corpus (A01–A13, C01–C03) and the operational lore from `2Dos Ai Instructions.md` and `Snippets.md`:
- **Anti-Drift Laws:** TARGET dominates everything; 2-strike rule on broken subsystems; no sunk-cost reasoning; product before ceremony; stop on drift.
- **Minimalism & Anti-Overcorrection:** Do only what satisfies the explicit task; no precautionary defensive guardrails for hypothetical risks; purge stale residual names.
- **Context Hygiene:** Step-by-step conscious context loading; eradication of residual confusing names; prevention of whole-file hallucinated rewrites.

## Acceptance Criteria

### Verification & Validation
- [ ] **Deterministic Conformance:** Running `python apex-meta/scripts/okf_validator.py` on all newly authored files reports `0 OKF Errors` and `0 APEX_PROFILE Errors`.
- [ ] **Significance Ranking Audit:** Rules in generated files are tagged with `[P<tier> | I<impact>/E<evidence>/R<risk>]` (no computed mathematical formulas) and ordered generally descending by priority tier (P0 -> P1 -> P2 -> P3).
- [ ] **Compactness & Pragmatic Sizing:** Verification confirms the general router file is reasonably compact (~100 lines / ~400 tokens) with critical routing logic top-loaded, without unnatural omissions or compromised technical clarity.
- [ ] **Context Isolation Simulation:** An agent executing a pure writing task loads only `writing-profile.md` without loading `file-architecture.md`, `execution-modes.md`, or other modules.
- [ ] **Traceability Audit:** A verification report proves that all critical operational snippets from `Snippets.md` and `2Dos Ai Instructions.md` and relevant insights from `module-deepening/` are formally codified and prioritized.


## 2026-10-21T16:45:38Z

Independently audit, stress-test, and validate the `v1.0` Finalization Dossier (`FinalizationDossier/00`–`06`), its architectural recommendations (`DEC-21`–`DEC-24`), and the finalized `v1.0` candidate, blueprint, and canonical library files against the 10-packet research corpus (`ResearchOfFile10/`). Verify whether every research critique, accepted/rejected claim, token count, cross-file provenance mapping, and surgical library patch is empirically sound, internally consistent, and free of hidden regressions or unaddressed gaps.

Working directory: `c:\GitDev\apexai-os-meta`
Integrity mode: development

## Reference Materials & Target Scope
- **Finalization Dossier Under Audit (Primary Target):**
  - `c:\GitDev\apexai-os-meta\apex-meta\informatics\Agent_Setup\NextIteration\v2-always-on-architecture\FinalizationDossier\index.md`
  - `00-research-critique-and-architecture-design.md` through `06-cross-dependency-and-verification-report.md`
- **Upstream Research Corpus (Ground Truth Input to Compare Against):**
  - `c:\GitDev\apexai-os-meta\apex-meta\informatics\Agent_Setup\NextIteration\v2-always-on-architecture\10-RESEARCH-EXECUTION-HANDOVER.md`
  - `c:\GitDev\apexai-os-meta\apex-meta\informatics\Agent_Setup\NextIteration\v2-always-on-architecture\ResearchOfFile10\RESULTS-01-xml-vs-markdown-gating.md` through `RESULTS-11-synthesis.md`
- **Finalized `v1.0` Candidate & Blueprint Suite Under Audit:**
  - `13-candidate-3A-xml.md`, `14-candidate-3B-hybrid.md`, `03-BLUEPRINT-agents.md`, `04-empirical-test-protocol.md`, `01-decision-register.md`, `09-contract-block-v0.5.md`, `11-instruction-surface-architecture.md`, `12-status-index.md`
- **Finalized Canonical Plane 4 Library Suite Under Audit:**
  - `c:\GitDev\apexai-os-meta\apex-meta\informatics\index.md`, `general-informatics-router.md`, `writing-profile.md`, `file-architecture.md`, `execution-modes.md`, `anti-drift-rules.md`, `governance-schemas.md`, `log.md`
- **Operational Lore & Security Redaction Targets:**
  - `c:\GitDev\apexai-os-meta\apex-meta\AI-Snippets\Orga\2Dos.md` and `2Dos Ai Instructions.md`

## Requirements

### R1. Independent Audit of Research Critique & Architectural Recommendations (`DEC-21`–`DEC-24`)
Independently evaluate the Dossier's critique of `ResearchOfFile10` (`RP-01`–`RP-10` and `RESULTS-11-synthesis.md`):
- Check whether any valid, high-leverage finding from `ResearchOfFile10` was unfairly dismissed, diluted, or omitted during the `v1.0` finalization pass.
- Challenge the four core architectural recommendations (`DEC-21` physical byte-identical `<apex_contract>` sync vs. `@AGENTS.md` import shims; `DEC-22` Two-Layer Carrier Architecture with `base_ref="apex-meta/informatics/"`; `DEC-23` paired `3A` Pure XML vs. `3B` Hybrid candidates with all 5 `deepen_when=` dropped; `DEC-24` selective integration of `RP-04`, `RP-05`, and `RP-07` wording) for any blind spots, edge-case failures across Claude Code / Codex / Gemini / Cursor / Copilot / Windsurf, or better alternatives.

### R2. Byte-Level & Token-Metric Verification of `v1.0` Contract Candidates & Blueprint
Independently verify `13-candidate-3A-xml.md`, `14-candidate-3B-hybrid.md`, and `03-BLUEPRINT-agents.md`:
- Recompute exact line, word, character, repo-estimator (`words * 1.3`), and `cl100k_base` BPE token counts from live file bytes to confirm or falsify the numbers reported in the Dossier.
- Compare `3A` and `3B` rule-for-rule to verify 100% behavioral equivalence between the XML and Hybrid serializations.
- Check `03-BLUEPRINT-agents.md` for any remaining duplication between Layer 1 (`<apex_contract>`) and Layer 2 (repo-specific sections) or any broken relative links.

### R3. Bidirectional Traceability & Cross-Dependency Audit Across the Plane 4 Library Suite
Audit every clause in `<apex_contract v="1.0">` against the canonical Plane 4 library files (`writing-profile.md`, `file-architecture.md`, `execution-modes.md`, `anti-drift-rules.md`, `governance-schemas.md`, `index.md`, `general-informatics-router.md`):
- Verify that every rule in `<apex_contract v="1.0">` is backed by its claimed canonical rule ID (`WP-xx`, `FA-xx`, `EM-xx`, `AD-xx`, `GS-xx`) without contradiction, stale `v0.3`/`v0.4` tag names, or single-owner violations (`WP-23`).
- Inspect `04-empirical-test-protocol.md`, `01-decision-register.md`, and `11-instruction-surface-architecture.md` for any lingering cross-file inconsistencies.

### R4. Deliverable: Independent Validation Report & Surgical Remediation (If Needed)
Write a comprehensive, evidence-grounded validation report to `c:\GitDev\apexai-os-meta\apex-meta\informatics\Agent_Setup\NextIteration\v2-always-on-architecture\FinalizationDossier\07-teamwork-independent-validation.md` using `[P<tier> | I<impact>/E<evidence>/R<risk>]` tags (no synthetic math formulas) and a structured Q&A Decision Matrix for any contested recommendation:
- State a clear `PASS`, `WARN`, or `FAIL` verdict per file and per architectural decision (`DEC-21`–`DEC-24`).
- If any factual discrepancy, broken link, stale reference, or unambiguous wording defect is discovered in the developed files (`v2-always-on-architecture/` or `apex-meta/informatics/`), apply the exact surgical fix and document it in `07-teamwork-independent-validation.md` and `FinalizationDossier/index.md`.
- **Strict Boundary:** Do NOT modify the live root `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md` files.

## Acceptance Criteria

### Independent Verification & Conformance Gates
- [ ] **Deterministic Validator Gate:** Running `python apex-meta/scripts/okf_validator.py --target apex-meta/informatics` exits with `0 OKF Errors` and `0 Apex Profile Errors`.
- [ ] **Full Adversarial & Ownership Test Suite:** Running `python -m pytest apex-meta/informatics/tests/ -q` passes 100% of tests (196/196 passed).
- [ ] **Independent Metric Reproduction:** Every token, word, and line count in `13-candidate-3A-xml.md`, `14-candidate-3B-hybrid.md`, and `03-BLUEPRINT-agents.md` is independently recomputed via script and verified in `07-teamwork-independent-validation.md`.
- [ ] **Zero Live Carrier Mutation:** `git diff AGENTS.md CLAUDE.md GEMINI.md` shows zero new changes introduced by the validation run.
- [ ] **Complete Dossier Artifact:** `FinalizationDossier/07-teamwork-independent-validation.md` is written and linked from `FinalizationDossier/index.md` with file-by-file verdicts (`PASS`/`WARN`/`FAIL`) and `[P<tier> | I/E/R]` rankings.


## 2026-10-22T11:10:20Z

# Teamwork Project Prompt — Layered Rule Knowledge Base & 3A-Ultra Compression

> Status: Launched
> Goal: Build Layered Rule KB (Rules 02–22), Plane 4 Module Audits, and Compile `16-candidate-3A-ultra.md`
> Requested team: [Informatics Architecture & High-Reasoning Token Optimization Team]

Systematically author the complete Layered Rule Knowledge Base for the Apex Informatics Instruction System in `apex-meta/informatics/final/research/06-layered-rule-kb/` (Rules 02 through 22, matching prototype `rule-01-target.md`), audit the 5 Plane 4 infrastructure modules for semantic block value and single-ownership discipline, and compile `16-candidate-3A-ultra.md` in `candidates/` (~950 BPE tokens) synthesizing all Option B surgical compressions.

Working directory: `c:\GitDev\apexai-os-meta`
Integrity mode: development

---

## Reference Materials & Target Scope

### Primary Canonical Sources & Prototypes
- **Master Essence Contract (Layer 0):** `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\candidates\13-candidate-3A-xml.md` (22 rules, 1,350 BPE tokens)
- **Sibling Formatting Projections:** `candidates\14-candidate-3B-hybrid.md` and `candidates\15-candidate-3C-bullet-hybrid.md`
- **Prototype Layered Rule KB File (Layer 1 Template):** `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb\rule-01-target.md`
- **Consolidated Final Directory & Index:** `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\index.md`
- **Long-List Ideas & Close Cuts:** `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\05-LONG-LIST-IDEAS-AND-CLOSE-CUTS.md`

### Upstream Research Corpora in `final/research/` (Zero Mutation, Cite & Link)
- `research/01-universal-instruction-research/` (`module-deepening/` A01–A13, C01–C03; `00`–`20` architecture specs)
- `research/02-deep-reasoning/` (`00`–`07` reasoning logs; `modules/M01`–`M06`)
- `research/03-research-of-file-10/` (`RESULTS-01` through `RESULTS-11-synthesis.md`, `Apex_Informatics_Research_Results_2026-10-21/`)
- `research/04-finalization-dossier/` (`00` through `08`, `07-teamwork-independent-validation.md`)
- `research/05-analysis-after-research/` (`AnalysisOfResearchIntegration.md`)

### Canonical Plane 4 Infrastructure Modules in `apex-meta/informatics/` (Layer 2)
- `writing-profile.md` (`WP-01`..`WP-25`)
- `file-architecture.md` (`FA-01`..`FA-13`)
- `execution-modes.md` (`EM-01`..`EM-12`)
- `anti-drift-rules.md` (`AD-01`..`AD-26`)
- `governance-schemas.md` (`GS-01`..`GS-17`)
- `general-informatics-router.md`
- `index.md`

### Operational Lore & Grounding Sources
- `c:\GitDev\apexai-os-meta\apex-meta\AI-Snippets\Orga\2Dos Ai Instructions.md` & `Snippets.md`

---

## Requirements

### R1. Complete Layered Rule Knowledge Base for All 22 Rules (`rule-02` through `rule-22`)
In `apex-meta/informatics/final/research/06-layered-rule-kb/`, create a dedicated deep-dive file for every remaining rule in `13-candidate-3A-xml.md`, following the structure and rigor of [`rule-01-target.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/final/research/06-layered-rule-kb/rule-01-target.md):
- `rule-02-product-first.md` (`<product_first>`)
- `rule-03-scope.md` (`<scope>`)
- `rule-04-communication.md` (`<communication>`)
- `rule-05-hold-position.md` (`<hold_position>`)
- `rule-06-ground.md` (`<ground>`)
- `rule-07-reuse.md` (`<reuse>`)
- `rule-08-context.md` (`<context>`)
- `rule-09-recovery.md` (`<recovery>`)
- `rule-10-stop-repairing.md` (`<stop_repairing>`)
- `rule-11-current-truth.md` (`<current_truth>`)
- `rule-12-surgical.md` (`<surgical>`)
- `rule-13-editing.md` (`<editing>`)
- `rule-14-new-machinery.md` (`<new_machinery>`)
- `rule-15-detour.md` (`<detour>`)
- `rule-16-authoring.md` (`<authoring>`)
- `rule-17-trade-off.md` (`<trade_off>`)
- `rule-18-handover.md` (`<handover>`)
- `rule-19-iterative.md` (`<iterative>`)
- `rule-20-schemas.md` (`<schemas>`)
- `rule-21-sync.md` (`<sync>`)
- `rule-22-pointers.md` (`<pointers>`)

**Every single rule deep-dive must provide:**
1. **OKF v0.2 Frontmatter:** `type: Reference`, unique durable `id: V2-LAYERED-KB-RULE-XX-...`, `title`, `description`, `status: current_truth`, `tags: [...]`.
2. **Layer Positioning:** Links to Layer 0 (`13-candidate-3A-xml.md`), Layer 1 (this file), and Layer 2 (canonical Plane 4 owner rules).
3. **§1 Original Rule & Atomic Semantic Block Inventory:**
   - Exact `v1.0-3A` text with token metrics (BPE `cl100k_base`, repo tokens, chars, words).
   - Numbered bullet list of atomic Semantic Blocks (`SB-XX.1` through `SB-XX.N`) with exact text, BPE token counts, and character lengths.
4. **§2 Chapter-by-Chapter Semantic Block Analysis & Alternatives:**
   - Dedicated subsection per semantic block (`SB-XX.k`).
   - What it means & specific failure mode addressed.
   - High-reasoning value critique tagged with `[P0-P3 | I/E/R]` (distinguishing default RLHF model behavior from high-leverage non-default discipline, identifying redundancies with sibling rules, and flagging token fat).
   - Three concrete formulation options:
     - **Option A (Baseline):** Current text as in `3A`.
     - **Option B (Recommended Surgical Compression):** Maximum information density, zero semantic loss, active voice, tightened phrasing.
     - **Option C (Aggressive / Cross-Rule Alternative):** Deeper structural compression, cross-rule deduplication, fusion, or alternative syntax.
5. **§3 Whole-Rule Recomposition Rollup Table:**
   - Side-by-side comparison of Baseline `3A`, Option B Surgical, and Option C Aggressive.
   - Measured BPE token count and percentage token savings.
6. **§4 Complete Bidirectional Research & Provenance Links:**
   - Links to internal research packets in `final/research/` (`RESULTS-01`..`11`, `A01`..`A13`, `C01`..`C03`, `FinalizationDossier/`).
   - Links to external literature/benchmarks (SpecBench, FixedBench, SWE-bench, Tao et al., Insights Discovery, etc.).
   - Canonical Plane 4 rule owners (`WP-xx`, `FA-xx`, `EM-xx`, `AD-xx`, `GS-xx`) and operational lore (`2Dos Ai Instructions.md`, `Snippets.md`).
7. **§5 Failure Modes & Not-To-Dos (`WP-25`):**
   - Precise boundaries: what must NEVER be cut, and what pitfalls to avoid when implementing this rule.

---

### R2. Plane 4 Infrastructure Module Audits
In `apex-meta/informatics/final/research/06-layered-rule-kb/`, create 5 module audit files:
- `audit-module-01-writing-profile.md` (auditing `writing-profile.md` `WP-01`..`WP-25`)
- `audit-module-02-file-architecture.md` (auditing `file-architecture.md` `FA-01`..`FA-13`)
- `audit-module-03-execution-modes.md` (auditing `execution-modes.md` `EM-01`..`EM-12`)
- `audit-module-04-anti-drift-rules.md` (auditing `anti-drift-rules.md` `AD-01`..`AD-26`)
- `audit-module-05-governance-schemas.md` (auditing `governance-schemas.md` `GS-01`..`GS-17`)

Each audit must examine:
- Rule-by-rule semantic block inventory.
- Verification of Single-Owner rule (`WP-23`): verify that each rule has one canonical definition module and other modules only reference it.
- Identification of stale terms, redundant phrasing, or candidate simplifications.
- Cross-traceability matrix to `<apex_contract v="1.0">` and `16-candidate-3A-ultra.md`.

---

### R3. Compile `16-candidate-3A-ultra.md` (~950 BPE Tokens)
In `apex-meta/informatics/final/candidates/16-candidate-3A-ultra.md`:
- Assemble the complete, ready-to-test contract block by concatenating all 22 recommended **Option B** surgical compressions from the Layered Rule KB.
- Maintain root tag `<apex_contract v="1.0-ultra" base_ref="apex-meta/informatics/">`.
- Keep the exact 22 semantic tags: `<target>`, `<product_first>`, `<scope>`, `<communication>`, `<hold_position>`, `<ground>`, `<reuse>`, `<context>`, `<recovery>`, `<stop_repairing>`, `<current_truth>`, `<surgical>`, `<editing>`, `<new_machinery>`, `<detour>`, `<authoring>`, `<trade_off>`, `<handover>`, `<iterative>`, `<schemas>`, `<sync>`, `<pointers>`.
- Recompute and record exact metrics: lines, words, chars, repo tokens (`chars // 4`), and `cl100k_base` BPE tokens. Target size: **~900–980 BPE tokens** (a ~30% reduction from `3A`'s 1,350 BPE tokens, preserving 100% of non-default invariants).
- Provide a rule-by-rule delta table against `13-candidate-3A-xml.md` showing BPE before, BPE after, and percentage savings.

---

### R4. Index & Directory Linking
- Create `apex-meta/informatics/final/research/06-layered-rule-kb/index.md` listing and linking all 22 rule deep-dives, 5 module audits, and the rollup.
- Update `apex-meta/informatics/final/index.md` to reference the completed Layered Rule KB and `16-candidate-3A-ultra.md`.

---

## Acceptance Criteria

- [ ] **22 Rule Files Complete:** All files `rule-01-target.md` through `rule-22-pointers.md` exist in `apex-meta/informatics/final/research/06-layered-rule-kb/` with all 5 mandatory sections.
- [ ] **5 Module Audit Files Complete:** `audit-module-01` through `audit-module-05` exist with full single-owner and semantic block audits.
- [ ] **`16-candidate-3A-ultra.md` Delivered:** Synthesizes Option B compressions, targets ~900–980 BPE tokens, and documents exact delta metrics.
- [ ] **Deterministic Conformance Gate:** `python apex-meta/scripts/okf_validator.py --target apex-meta/informatics` passes with `0 OKF Errors` and `0 Apex Profile Errors`.
- [ ] **Adversarial & Ownership Test Suite:** `python -m pytest apex-meta/informatics/tests/ -q` passes 100% (196/196 passed).
- [ ] **Zero Live Mutation:** `git status` confirms zero modification to root `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md`.
- [ ] **Research Bytes Preserved:** Zero modifications to existing research files in `final/research/01-universal-instruction-research/` and `final/research/03-research-of-file-10/`.
