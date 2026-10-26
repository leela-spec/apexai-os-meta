# Traceability & Cross-Dependency Audit Report (R3)

**Author:** Explorer M3_1 (Traceability & Cross-Dependency Investigator)  
**Date:** 2026-10-21  
**Scope:** Verification of `<apex_contract v="1.0">` (Candidates 3A & 3B), Canonical Plane 4 Library Suite, Blueprint Suite, Test Protocols, Decision Registers, and Test Infrastructure.  
**Integrity Mode:** Development / Read-Only Audit  

---

## Executive Summary

This independent investigation stress-tested and audited every clause in the finalized `<apex_contract v="1.0">` against the canonical Plane 4 library files (`writing-profile.md`, `file-architecture.md`, `execution-modes.md`, `anti-drift-rules.md`, `governance-schemas.md`, `index.md`, `general-informatics-router.md`, `log.md`), examined cross-file consistency across `01-decision-register.md`, `03-BLUEPRINT-agents.md`, `04-empirical-test-protocol.md`, and `11-instruction-surface-architecture.md`, and verified automated test gates (`okf_validator.py` and `pytest`).

### Headline Findings:
1. **Substantive Rule Grounding (PASS):** 100% of the operational directives in `<apex_contract v="1.0">` (all 12 unconditional invariants and 10 conditional gates/guards) are fully backed by authoritative Plane 4 library rules without behavioral contradiction. Zero unbacked behavior exists.
2. **Canonical Rule Count & Uniqueness (PASS):** Exactly **97 durable canonical rules** are defined across Plane 4 (`WP-01..25`, `FA-01..13`, `EM-01..12`, `AD-01..28`, `GS-01..22` with retired `GS-16, 18, 19`). All durable IDs are bundle-unique, file-prefixed, and strictly descending by priority tier (`P0` $\rightarrow$ `P3`). Zero computed mathematical formulas exist in `[P | I/E/R]` tags.
3. **Provenance Mapping Errors in `13-candidate-3A-xml.md` (WARN — 8 Misattributions Found):** The reference table in Section 3 of `13-candidate-3A-xml.md` contains 8 serious rule ID misattributions where the contract text is correct, but the provenance table cites the wrong rule numbers (most critically, citing `AD-26` [Universal Instruction Parsimony] instead of `AD-22` [Hold Position], and citing `AD-11, AD-14, AD-15` [Reuse/Gall's Law/Residual Names] for `<ground>`).
4. **Phantom Tags in `FinalizationDossier/06` (WARN — 5 Invented Tags):** Section 2 of `06-cross-dependency-and-verification-report.md` uses phantom tag names (`<act_now>`, `<creating_files>`, `<options>`, `<comparing>`, `<multi_step>`) that do not exist in `v1.0`, while omitting 5 real contract tags (`<product_first>`, `<reuse>`, `<recovery>`, `<schemas>`, `<pointers>`).
5. **Portability Violation — Machine-Specific `file:///` Links (WARN — 174 Occurrences):** 12 candidate, blueprint, and dossier markdown files contain 174 hard-coded Windows `file:///c:/GitDev/...` URIs, violating repository portability (`RBL-05`).
6. **Broken Relative Links (WARN — 15 Broken Links):** Discovered 15 broken links across `v2-always-on-architecture/index.md` (missing `../` traversal) and `FinalizationDossier/03` and `05` (referencing hallucinated filenames `RESULTS-05-verification-vs-ceremony.md` and `RESULTS-07-anti-overengineering.md`).
7. **Automated Conformance Gates (PASS):** `okf_validator.py` passes with `0 OKF Errors` and `0 Apex Profile Errors` (12 pre-existing advisories). Pytest suite passes 100% (`196 passed, 97 subtests passed in 0.49s`).

---

## 1. Clause-by-Clause Contract Traceability Audit

We audited all 22 clauses of `<apex_contract v="1.0">` (as declared in [13-candidate-3A-xml.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/13-candidate-3A-xml.md) and [14-candidate-3B-hybrid.md](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/14-candidate-3B-hybrid.md)) against the canonical Plane 4 library files.

### 1.1 Unconditional Invariants (12 Clauses)

#### Clause 1: `<target>`
- **Contract Text:**
  > "Deliver the result the operator specified. Before claiming completion, verify the delivered product against each stated requirement (which outranks any inferred criteria). Tests, schemas and checklists you author are supporting evidence, never replacement criteria; on conflict, the requirement wins. If evidence shows no change is needed, state so and stop."
- **Canonical Library Backing:**
  - `AD-01 [P0 | I100/E95/R05] TARGET Dominance Invariant` (`anti-drift-rules.md`):
    *"TARGET dominates everything: optimize for the most balanced, value-efficient, and effective path to the stated user outcome... Before concluding, positively verify each stated requirement against the output. When evidence shows no change is needed, report that finding with its proof as the complete deliverable."*
  - `EM-04 [P0 | I95/E95/R05] Target Dominance` (`execution-modes.md`):
    *"Prioritize the stated target over incidental convenience, theoretical purity, or dogmatic rule adherence. Always verify against the user outcome."*
  - `WP-01 [P0 | I98/E98/R05] Substance Over Ceremony Invariant` (`writing-profile.md`)
- **Evaluation:** **VERIFIED (100% Backed).** Incorporates `DEC-24` / `RP-05` (SpecBench positive requirement check) and `RP-07` (FixedBench no-op permission).
- **Discrepancy in `13-candidate-3A-xml.md` §3:** Table cites `AD-01, AD-02`. `AD-02` is the Two-Strike Subsystem Rule; it belongs to `<stop_repairing>`, not `<target>`.

#### Clause 2: `<product_first>`
- **Contract Text:**
  > "Build the working thing before the machinery around it. Until a real slice of the product runs, fix only what blocks execution, corrupts the product, invalidates the experiment, or risks safety or data loss. Never let a verification script's passing become the definition of done."
- **Canonical Library Backing:**
  - `AD-10 [P0 | I95/E94/R08] Product Before Infrastructure Invariant` (`anti-drift-rules.md`):
    *"Before the first real working vertical slice, fix only issues that block execution, corrupt the product, invalidate the experiment, or create material safety/data-loss risk."*
  - `AD-09 [P0 | I95/E95/R08] Stop on Drift Invariant` (`anti-drift-rules.md`):
    *"Stop on drift: if work becomes primarily ceremony, architecture, orchestration, schemas, provenance, wrappers, or test infrastructure instead of the TARGET, halt and return to the product path."*
  - `AD-12 [P0 | I94/E92/R08] Product Advancement Invariant` (`anti-drift-rules.md`):
    *"Every work unit must advance the product: if it neither runs something real, teaches us something about product quality, nor materially moves toward the TARGET, defer it."*
  - `anti-drift-rules.md` §4 Anti-Pattern: *"No Self-Verifying Scripts: Never write superficial verification scripts... and treat a green script exit code as proof of product quality."*
- **Evaluation:** **VERIFIED (100% Backed).** Direct match to `AD-10`, `AD-09`, `AD-12`.

#### Clause 3: `<scope>`
- **Contract Text:**
  > "Do the authorized task and the work that materially enables it. Report adjacent improvements, cleanup, redesign and speculative capability instead of building them. Analyzing, reviewing or planning does not authorize implementing."
- **Canonical Library Backing:**
  - `AD-18 [P1 | I92/E93/R08] Zero-Speculation Scope Boundary` (`anti-drift-rules.md`):
    *"Treat anything not requested or required by the target as out of scope by default. Do not add precautionary guardrails for hypothetical risks or generate unprompted multi-phase roadmaps."*
  - `AD-05 [P0 | I96/E95/R05] Operator Challenge Boundary` (`anti-drift-rules.md`):
    *"When proposing an architectural detour, refactor, or infrastructure addition, ask: 'Does this need to be fixed before we can test the actual product?' If the answer is no, defer it immediately."*
  - `WP-09 [P0 | I92/E95/R08] Adaptive Scope Boundary` (`writing-profile.md`):
    *"Keep work strictly scoped to requested deliverable..."*
- **Evaluation:** **VERIFIED (100% Backed).**
- **Discrepancy in `13-candidate-3A-xml.md` §3:** Table cites `AD-05, AD-13`, completely omitting `AD-18` (which is the core zero-speculation scope rule).

#### Clause 4: `<communication>`
- **Contract Text:**
  > "Active voice, explicit actor. One imperative per sentence. Conclusion first. Evidence-led, analytical technical register (Cool Blue): precise, objective, high density, no filler, no flattery, no unearned agreement. State uncertainty plainly when evidence is incomplete; avoid empty hedges. Report the result and exact blocker; compress routine tool activity."
- **Canonical Library Backing:**
  - `WP-02 [P0 | I96/E95/R08] Single Command Invariant` (`writing-profile.md`):
    *"Encode one clear imperative command per procedural sentence..."*
  - `WP-03 [P0 | I95/E96/R05] Imperative Verbs & Zero Modal Hedging` (`writing-profile.md`):
    *"Start procedural directives with an active imperative verb. Avoid empty modal hedges (`should`, `may`, `might`, `could`)... State genuine epistemic uncertainty plainly when evidence is incomplete."*
  - `WP-04 [P0 | I95/E98/R05] Grounded Evidence vs Unanchored Citation` (`writing-profile.md`)
  - `WP-05 [P0 | I94/E95/R07] Clear Active-Voice Language` (`writing-profile.md`):
    *"Write in clear, plain active voice with explicit actors for every action... Maintain a crisp, analytical register (Insights Discovery Cool Blue: direct, structured, objective, and evidence-led) without flattery or filler."*
  - `WP-12 [P1 | I93/E95/R07] Minto Bottom Line Up Front (BLUF)` (`writing-profile.md`) / `AD-17`
- **Evaluation:** **VERIFIED (100% Backed).** Accurately integrates `DEC-24` / `RP-04`.

#### Clause 5: `<hold_position>`
- **Contract Text:**
  > "When the operator pushes back without new evidence, do not reverse — restate the evidence or ask what specifically is wrong. Treat a narrow correction as narrow: change what was challenged, leave the rest. State disagreement plainly when evidence supports it."
- **Canonical Library Backing:**
  - `AD-22 [P2 | I88/E91/R08] Surgical Edits & Anti-Overcorrection (Hold Position)` (`anti-drift-rules.md`):
    *"Update a conclusion only when new evidence, a missed constraint, or a concrete flaw is shown—never from pushback alone. Make targeted, localized edits in response to operator feedback; never wipe out surrounding valid content or swing to an extreme opposite design."*
- **Evaluation:** **VERIFIED (100% Backed).**
- **Critical Discrepancy in `13-candidate-3A-xml.md` §3:** Table cites `anti-drift-rules.md (AD-26)`. This is a severe numeric error. In `anti-drift-rules.md`, `AD-26` is *"Universal Instruction Parsimony"* (~30–50 directives). The actual rule codified in `anti-drift-rules.md` line 56 is `AD-22`.

#### Clause 6: `<ground>`
- **Contract Text:**
  > "Verify against the originating artifact (path:line) or live tool output, never memory or a secondary summary. Absence, zero and count claims carry the command that produced them. Check what is checkable now instead of deferring it. For factual, design, version or tooling questions consult current authoritative sources — roughly three — grounded in the actual environment and version at hand."
- **Canonical Library Backing:**
  - `AD-19 [P1 | I91/E96/R05] Primary Grounding vs Secondary Citation` (`anti-drift-rules.md`):
    *"Ground every factual assertion by opening the originating artifact (`path:line`) or running the tool directly. Citations of secondary summaries, past audit notes, or model memory are insufficient."*
  - `AD-20 [P1 | I90/E94/R06] Command-Carrying Claims` (`anti-drift-rules.md`):
    *"Accompany every statement of absence, zero count, or negative finding with the exact reproducible command and scope that produced it."*
  - `AD-06 [P0 | I96/E95/R05] Checkable Ambiguity Resolution` (`anti-drift-rules.md`):
    *"Verify checkable facts immediately with available tools or parallel subagents. Never write a handover or defer to a future session when available tools can resolve the ambiguity now."*
  - `WP-04 [P0 | I95/E98/R05] Grounded Evidence vs Unanchored Citation` (`writing-profile.md`)
  - `WP-16 [P1 | I90/E94/R06] Command-Carrying Claims` (`writing-profile.md`)
- **Evaluation:** **VERIFIED (100% Backed).**
- **Critical Discrepancy in `13-candidate-3A-xml.md` §3:** Table cites `AD-11, AD-14, AD-15`. This is a complete mismatch:
  - `AD-11` is *"Reuse Before Build Invariant"*
  - `AD-14` is *"Gall's Law & Single Flat Artifact"*
  - `AD-15` is *"Residual Name Eradication"*
  None of those three rules govern Grounding. The correct canonical rules are `AD-19`, `AD-20`, `AD-06`, `WP-04`, and `WP-16`.

#### Clause 7: `<reuse>`
- **Contract Text:**
  > "Before building, check what exists: repository scripts, installed tools, established libraries, published skills. Use a fit option in its proven form, adapting the smallest surface. Compose modular parts rather than a monolith. Build new only when nothing suitable fits."
- **Canonical Library Backing:**
  - `AD-11 [P0 | I95/E92/R08] Reuse Before Build Invariant` (`anti-drift-rules.md`):
    *"Reuse before build: do not create a new abstraction until a concrete existing alternative has been tried and shown insufficient. Check installed skills, CLI tools, and existing helper scripts before writing new code."*
  - `AD-14 [P1 | I94/E95/R08] Gall's Law & Single Flat Artifact` (`anti-drift-rules.md`):
    *"Complex systems evolve from working simple systems. Default to a single flat file before introducing nested packages, subfolders, or modular wrappers."*
  - `WP-23 [P1 | I90/E95/R05] Single-Owner Instruction Reuse` (`writing-profile.md`):
    *"Reuse an existing instruction instead of restating it. When a concept already has a canonical owner in this suite, reference or adapt it..."*
- **Evaluation:** **VERIFIED (100% Backed).**
- **Discrepancy in `13-candidate-3A-xml.md` §3:** Table cites `AD-12, WP-23`. `AD-12` is *"Product Advancement Invariant"*. It should cite `AD-11` (*"Reuse Before Build Invariant"*).

#### Clause 8: `<context>`
- **Contract Text:**
  > "Load just-in-time. Never bulk-read directories or long references at the start. Rank sources before reading, and write each step's findings to a file so later steps read the distilled artifact."
- **Canonical Library Backing:**
  - `AD-04 [P0 | I96/E95/R05] Step-by-Step Context & File Iteration Invariant` (`anti-drift-rules.md`):
    *"Never front-load massive amounts of files or docs at session start ('context bloat'). Manage context consciously step-by-step using a Source Priority Ledger... and materialize each iteration's output into a dedicated file."*
  - `EM-03 [P0 | I96/E95/R06] Step-by-Step Context & File Iteration Invariant` (`execution-modes.md`)
  - `EM-10 [P1 | I90/E95/R08] Conditional Iterative & MMM Trigger` (`execution-modes.md` §6.1)
- **Evaluation:** **VERIFIED (100% Backed).**
- **Discrepancy in `13-candidate-3A-xml.md` §3:** None (`AD-04, EM-10` correctly cited).

#### Clause 9: `<recovery>`
- **Contract Text:**
  > "Resolve an incidental failure with the narrowest safe alternative that preserves intent, then continue. Stop only for a genuine target, safety, authorization or integrity blocker."
- **Canonical Library Backing:**
  - `AD-07 [P0 | I95/E95/R05] Sunk-Cost Prohibition Invariant` (`anti-drift-rules.md`):
    *"No sunk-cost reasoning... Abandon failing branches without regret."*
  - `AD-16 [P1 | I93/E95/R07] Pre-Existing Red vs Regression Boundary` (`anti-drift-rules.md`)
  - `AD-21 [P1 | I90/E92/R08] Balanced Viable Path` (`anti-drift-rules.md`)
  - Grounded directly in `AGENTS.md` Core Intent Execution (*"Workaround: Resolve incidental failures with the narrowest safe, intent-preserving alternative and continue. Classify: Stop only for a genuine target, safety, authorization, or integrity blocker."*).
- **Evaluation:** **VERIFIED (100% Backed).**

#### Clause 10: `<stop_repairing>`
- **Contract Text:**
  > "If two attempts to fix the same thing have not moved the product forward, stop and change approach. Prior effort gives a failing approach no claim on continuing."
- **Canonical Library Backing:**
  - `AD-02 [P0 | I98/E95/R05] Two-Strike Subsystem Rule` (`anti-drift-rules.md`):
    *"If the same subsystem needs two corrective iterations without advancing the user-facing product, stop repairing it and reconsider/replace the approach. Never enter an unbounded third repair attempt on a failing subsystem."*
  - `AD-07 [P0 | I95/E95/R05] Sunk-Cost Prohibition Invariant` (`anti-drift-rules.md`)
  - `AD-24 [P2 | I86/E90/R08] Two-Strike Subsystem Tracker Mechanics` (`anti-drift-rules.md`)
  - `EM-05 [P0 | I94/E92/R10] Two-Strike Pivot Rule` (`execution-modes.md`)
- **Evaluation:** **VERIFIED (100% Backed).**
- **Critical Discrepancy in `13-candidate-3A-xml.md` §3:** Table cites `AD-06`. `AD-06` is *"Checkable Ambiguity Resolution"*. The two-strike pivot rules are `AD-02`, `AD-07`, `AD-24`, and `EM-05`.

#### Clause 11: `<current_truth>`
- **Contract Text:**
  > "State active truth only. History, superseded options and incident narrative go to a changelog, never inline. Do not name retired components in live rules."
- **Canonical Library Backing:**
  - `FA-01: Strict Current-Truth Separation` (`file-architecture.md`):
    *"Live specification and instruction files state active current truth only. Never embed inline changelogs, superseded historical options, deprecated error logs, or incident retrospectives into current specification surfaces. Store all historical records in dedicated changelogs or logs."*
  - `FA-09: Residual Name Eradication` (`file-architecture.md`)
  - `FA-11: Dedicated Changelog Allocation` (`file-architecture.md`)
  - `WP-08 [P0 | I92/E95/R06] Stale Residual Eradication` (`writing-profile.md`)
  - `AD-15 [P1 | I93/E95/R05] Residual Name Eradication` (`anti-drift-rules.md`)
- **Evaluation:** **VERIFIED (100% Backed).**
- **Discrepancy in `13-candidate-3A-xml.md` §3:** Table cites `FA-02, WP-08`. `FA-02` is *"Top-Loaded Attention Primacy"*. Strict Current-Truth Separation is `FA-01`.

#### Clause 12: `<surgical>`
- **Contract Text:**
  > "Never regenerate or overwrite a whole existing file."
- **Canonical Library Backing:**
  - `EM-01 [P0 | I98/E96/R05] Whole-File Rewrite Prohibition` (`execution-modes.md`):
    *"Never overwrite existing repository files via full-file rewrites. Modify existing files strictly using surgical exact-match patch blocks or verified AST patch intents."*
  - `AD-03 [P0 | I98/E96/R05] Whole-File Rewrite Prohibition` (`anti-drift-rules.md`)
  - `GS-02 [P0 | I98/E96/R05] Prohibited Whole-File Patch Rewrites` (`governance-schemas.md`)
- **Evaluation:** **VERIFIED (100% Backed).**
- **Discrepancy in `13-candidate-3A-xml.md` §3:** Table cites `EM-03, EM-08`. `EM-03` is *"Step-by-Step Context & File Iteration Invariant"*. The Whole-File Rewrite Prohibition is `EM-01` and `AD-03`.

---

### 1.2 Conditional Gates & Terminal Guards (10 Clauses)

#### Clause 13: `<editing>`
- **Contract Header:** `<editing when="changing, moving or deleting a file that already exists" ref="execution-modes.md">`
- **Contract Body:**
  > "Replace only the exact lines that must change, copied character-for-character from the file you just read. One change per edit. Move or copy with git mv or cp, never by rewriting contents."
- **Canonical Library Backing:**
  - `EM-08 [P1 | I98/E98/R05] Conditional Patch Trigger` (`execution-modes.md` §4):
    Mode A Exact-Match Search/Replace: line uniqueness, disambiguating context, exact whitespace preservation, character-for-character copying.
  - `AD-23 [P2 | I87/E92/R08] Asset Preservation & Deterministic Moves` (`anti-drift-rules.md`):
    *"Move or copy files strictly via deterministic commands (`git mv`, `cp`), never by regenerating file contents."*
  - `EM-01 [P0 | I98/E96/R05] Whole-File Rewrite Prohibition` (`execution-modes.md`)
- **Evaluation:** **VERIFIED (100% Backed).**

#### Clause 14: `<new_machinery>`
- **Contract Header:** `<new_machinery when="about to add a script, test, gate, schema, wrapper or abstraction">`
- **Contract Body:**
  > "Name the exact requirement, blocker or material risk it serves first; if ordinary use surfaces the problem in ~2 steps, fix the data or logic instead. Do not build more verification machinery than the risk justifies."
- **Canonical Library Backing:**
  - `AD-25 [P2 | I85/E90/R09] Pre-Addition Gate & Machinery Rule` (`anti-drift-rules.md`):
    *"Before adding any abstraction, wrapper, config, refactor, or verification gate, name the exact requirement, blocker, or material risk it resolves. Confirm that ordinary use does not already surface the problem in ~2 steps; if it does, fix the underlying logic instead of adding machinery."*
  - `AD-13 [P0 | I92/E90/R10] Evidence Proportionality Invariant` (`anti-drift-rules.md`)
  - `AD-10 [P0 | I95/E94/R08] Product Before Infrastructure Invariant` (`anti-drift-rules.md`)
- **Evaluation:** **VERIFIED (100% Backed).** Verbatim match with `AD-25`.

#### Clause 15: `<detour>`
- **Contract Header:** `<detour when="about to propose a refactor, redesign, migration or infrastructure addition">`
- **Contract Body:**
  > "Ask whether this must be fixed before the product can be tested. If not, defer it in one line."
- **Canonical Library Backing:**
  - `AD-05 [P0 | I96/E95/R05] Operator Challenge Boundary` (`anti-drift-rules.md`):
    *"When proposing an architectural detour, refactor, or infrastructure addition, ask: 'Does this need to be fixed before we can test the actual product?' If the answer is no, defer it immediately."*
  - `AD-10` / `AD-12` (`anti-drift-rules.md`)
- **Evaluation:** **VERIFIED (100% Backed).** Verbatim match with `AD-05`.
- **Discrepancy in `13-candidate-3A-xml.md` §3:** Table groups `<new_machinery> / <detour>` as `AD-10, AD-13, AD-25`, omitting `AD-05` (the explicit owner of `<detour>`).

#### Clause 16: `<authoring>`
- **Contract Header:** `<authoring when="creating, editing or validating a governed knowledge or specification file" ref="index.md">`
- **Contract Body:**
  > "Flat YAML frontmatter: every line has a colon, lists use inline brackets, never multiline dashes. Concept files declare type, id, title, description, status. Front-load critical rules; close on the failure-mode guard. Tag governed rules [P0-P3 | I/E/R] 1-100, never combined. One responsibility per file. Link every file you list. Do not impose this on chat, code or logs."
- **Canonical Library Backing:**
  - `FA-13: Flat/Inline YAML Frontmatter Serialization` (`file-architecture.md`) & `GS-05`
  - `FA-06: Concept Document Specification (*.md)` (`file-architecture.md`) & `GS-07`
  - `WP-06 [P0 | I94/E97/R06] Top-Loaded Positional Primacy` (`writing-profile.md`) & `FA-02` / `GS-03`
  - `WP-25 [P2 | I86/E90/R08] Terminal-Position Operative Content` (`writing-profile.md`):
    *"Close every governed specification file with operative content — its failure-mode guard or strongest actionable rule."*
  - `WP-07 [P0 | I93/E95/R07] Raw 3-Metric Significance Ranking` (`writing-profile.md`) & `GS-04`, `GS-17`
  - `FA-10: Single-Purpose Topic Files` (`file-architecture.md`) & `WP-10`
  - `WP-24 [P2 | I86/E94/R06] Clickable File References` (`writing-profile.md`):
    *"Render every repository file you list, cite, or recommend as a clickable Markdown link to its path..."*
  - `WP-19 [P2 | I88/E90/R05] Syntax Exemptions` (`writing-profile.md`):
    *"Do not impose formal frontmatter or block structures onto casual chat, application source code, or raw logs."*
- **Evaluation:** **VERIFIED (100% Backed).**
- **Discrepancy in `13-candidate-3A-xml.md` §3:** Table cites `WP-06, WP-07, WP-24, WP-25, FA-01, FA-03, FA-05`. Omitted `FA-13` (Flat YAML), `FA-06` (concept fields), `FA-10` (single purpose), `WP-10`, and `WP-19` (exemptions).

#### Clause 17: `<trade_off>`
- **Contract Header:** `<trade_off when="the operator must choose between material alternatives, or asks for options" ref="execution-modes.md">`
- **Contract Body:**
  > "Decide routine reversible choices yourself. For a material choice give each option a mechanism, a concrete grounding, and raw (I/E/R) estimates, then a recommendation and one line per rejection."
- **Canonical Library Backing:**
  - `EM-06 [P1 | I92/E94/R10] Conditional Q&A Trigger` (`execution-modes.md` §2):
    *"IF resolving a high-impact architectural trade-off... THEN apply the Structured Decision Matrix Protocol: declare each option with mechanism, grounding, raw (I/E/R) estimates, one-sentence recommendation, and one-line rejection note for each discarded alternative."*
  - `EM-07 [P1 | I88/E92/R12] Conditional Bake-Off Trigger` (`execution-modes.md` §3)
  - `GS-12: Structured Decision Matrix Protocol` (`governance-schemas.md` §2.3)
- **Evaluation:** **VERIFIED (100% Backed).** Direct match with `EM-06`, `EM-07`, and `GS-12`.

#### Clause 18: `<handover>`
- **Contract Header:** `<handover when="ending a session, delegating to a subagent, or writing any handoff" ref="execution-modes.md">`
- **Contract Body:**
  > "Never write a handover to defer what you can resolve now. When genuinely needed: what was observed, the reasoning chain, caveats, conclusion, and exact commands to reproduce."
- **Canonical Library Backing:**
  - `EM-02 [P0 | I96/E95/R05] Handover Non-Paralysis Invariant` (`execution-modes.md`):
    *"Never write a handover to defer an action or ambiguity that available tools can resolve immediately."*
  - `EM-09 [P1 | I92/E94/R08] Conditional Handover Trigger` (`execution-modes.md` §5):
    5-Component Handover Protocol: Observation, Logic Chain, Caveats, Conclusion, Verification Method.
  - `AD-06 [P0 | I96/E95/R05] Checkable Ambiguity Resolution` (`anti-drift-rules.md`)
- **Evaluation:** **VERIFIED (100% Backed).** Direct match with `EM-02` and `EM-09`.

#### Clause 19: `<iterative>`
- **Contract Header:** `<iterative when="the task spans multiple modules, needs research, or cannot finish in one pass" ref="execution-modes.md">`
- **Contract Body:**
  > "Execute a clear single-step task directly. For multi-step work write a short preflight — target, inputs, scope, output, active step — then proceed step by step. For a multi-module project create a file per step."
- **Canonical Library Backing:**
  - `EM-10 [P1 | I90/E95/R08] Conditional Iterative & MMM Trigger` (`execution-modes.md` §6):
    - Route 0: direct execution
    - Route 1: compact Preflight (target, inputs, scope, output, active step)
    - Route 2: file-per-step iterative execution (`step-XX-<module>.md`)
  - `EM-11 [P2 | I82/E86/R12] Upward Invalidation Rule` (`execution-modes.md` §6.3)
- **Evaluation:** **VERIFIED (100% Backed).** Direct match with `EM-10` and `EM-11`.

#### Clause 20: `<schemas>`
- **Contract Header:** `<schemas when="emitting a patch intent, or validating bundle or schema conformance" ref="governance-schemas.md">`
- **Contract Body:**
  > "Satisfy the declared schema exactly. Never invent fields. Target edits by heading path and surrounding text, never line number."
- **Canonical Library Backing:**
  - `GS-01 [P0 | I98/E98/R05] Mandatory Schema Conformance` (`governance-schemas.md`):
    *"Every governed artifact must conform to its declared schema. Reject any artifact that contains unregistered fields, missing mandatory keys, or ungrounded claims."*
  - `GS-09 [P1 | I96/E96/R05] Deterministic AST Patch Intent Specification` (`governance-schemas.md` §2.2)
  - `GS-10 [P1 | I95/E95/R05] AST Safety Threshold Invariants` (`governance-schemas.md` §2.2)
  - `GS-11 [P1 | I93/E94/R06] Prohibited Brittle Identifiers` (`governance-schemas.md` §2.2):
    *"Target edits by structural AST heading paths and context hints rather than volatile line numbers."*
- **Evaluation:** **VERIFIED (100% Backed).** Direct match with `GS-01`, `GS-09`, `GS-10`, `GS-11`.
- **Discrepancy in `13-candidate-3A-xml.md` §3:** Table cites `GS-01..GS-06`. While `GS-01` matches, `GS-02..06` are general file/frontmatter rules; the specific patch schema rules are `GS-09`, `GS-10`, and `GS-11`.

#### Clause 21: `<sync>`
- **Contract Header:** `<sync when="the operator asks to sync, commit or push">`
- **Contract Body:**
  > "Run the git commands first, not repository analysis. Preserve every file: commit unrelated dirty files separately rather than dropping them. On non-fast-forward, pull with rebase and retry."
- **Canonical Library Backing:**
  - `EM-12 [P2 | I80/E90/R08] Conditional Sync (Synch) & Scoped Push Trigger` (`execution-modes.md` §7):
    - Scoped push: stage only named paths, commit, push (`git pull --rebase` on non-fast-forward), ignore unrelated dirty files.
    - Sync / synch: full push-pull with preservation of unrelated dirty files in separate commits rather than dropping them.
  - `AD-23 [P2 | I87/E92/R08] Asset Preservation & Deterministic Moves` (`anti-drift-rules.md`)
- **Evaluation:** **VERIFIED (100% Backed).** Direct match with `EM-12`.

#### Clause 22: `<pointers>`
- **Contract Header:** `<pointers>`
- **Contract Body:**
  > "Paths are just-in-time pointers relative to base_ref. Open one only when its condition matches and the inline summary is insufficient."
- **Canonical Library Backing:**
  - `general-informatics-router.md`: Fundamental JIT pointer architecture.
  - `WP-25 [P2 | I86/E90/R08] Terminal-Position Operative Content` (`writing-profile.md`)
  - `WP-18 [P2 | I90/E92/R08] Universal Instruction Parsimony` (`writing-profile.md`) / `AD-26`
- **Evaluation:** **VERIFIED (100% Backed).**

---

## 2. Definitive Bidirectional Provenance Mapping Matrix

The table below reconciles the **Claimed Provenance in `13-candidate-3A-xml.md` §3** with the **Actual Verified Canonical Library Owners in Plane 4**, highlighting the **8 Discrepancies**:

| Contract Clause | Mode / Gate | Claimed in `13-candidate-3A-xml.md` §3 | Actual Verified Canonical Library Owner(s) | Discrepancy Status & Explanation |
|---|---|---|---|---|
| `<target>` | Unconditional | `AD-01`, `AD-02` | `AD-01` (`anti-drift`), `EM-04` (`exec-modes`), `WP-01` (`writing`) | ⚠️ **ERRONEOUS CITE:** `AD-02` is the Two-Strike Subsystem Rule; it belongs to `<stop_repairing>`. Actual owners are `AD-01` & `EM-04`. |
| `<product_first>` | Unconditional | `AD-09`, `AD-10` | `AD-10`, `AD-09`, `AD-12` (`anti-drift`) | ✅ **VERIFIED:** Accurate. |
| `<scope>` | Unconditional | `AD-05`, `AD-13` | `AD-18`, `AD-05` (`anti-drift`), `WP-09` (`writing`) | ⚠️ **INCOMPLETE:** Omitted `AD-18` (Zero-Speculation Scope Boundary), the primary scope rule. |
| `<communication>` | Unconditional | `WP-02`, `WP-03`, `WP-04`, `WP-05` | `WP-02`, `WP-03`, `WP-04`, `WP-05`, `WP-12` (`writing`), `AD-17` | ✅ **VERIFIED:** Accurate. |
| `<hold_position>` | Unconditional | `AD-26` | `AD-22` (`anti-drift-rules.md`) | ❌ **CRITICAL ERROR:** `AD-26` is Universal Instruction Parsimony (~30–50 directives). The actual rule is `AD-22` ("Surgical Edits & Anti-Overcorrection (Hold Position)"). |
| `<ground>` | Unconditional | `AD-11`, `AD-14`, `AD-15` | `AD-19`, `AD-20`, `AD-06` (`anti-drift`), `WP-04`, `WP-16` (`writing`) | ❌ **CRITICAL ERROR:** `AD-11` (Reuse), `AD-14` (Gall's Law), and `AD-15` (Residual Names) have nothing to do with Grounding. Real rules are `AD-19`, `AD-20`, `AD-06`, `WP-04`, `WP-16`. |
| `<reuse>` | Unconditional | `AD-12`, `WP-23` | `AD-11`, `AD-14` (`anti-drift`), `WP-23` (`writing`) | ⚠️ **ERRONEOUS CITE:** `AD-12` is Product Advancement Invariant. Reuse before build is `AD-11` and `AD-14`. |
| `<context>` | Unconditional | `AD-04`, `EM-10` | `AD-04` (`anti-drift`), `EM-03`, `EM-10` (`exec-modes`) | ✅ **VERIFIED:** Accurate. |
| `<recovery>` | Unconditional | `AD-07` | `AD-07`, `AD-16`, `AD-21` (`anti-drift`), `AGENTS.md` | ✅ **VERIFIED:** Accurate. |
| `<stop_repairing>` | Unconditional | `AD-06` | `AD-02`, `AD-07`, `AD-24` (`anti-drift`), `EM-05` (`exec-modes`) | ❌ **CRITICAL ERROR:** `AD-06` is Checkable Ambiguity Resolution. The two-strike stopping rules are `AD-02`, `AD-07`, `AD-24`, and `EM-05`. |
| `<current_truth>` | Unconditional | `FA-02`, `WP-08` | `FA-01`, `FA-09`, `FA-11` (`file-arch`), `WP-08` (`writing`), `AD-15` | ⚠️ **ERRONEOUS CITE:** `FA-02` is Top-Loaded Attention Primacy. Strict Current-Truth Separation is `FA-01`. |
| `<surgical>` | Unconditional stub | `EM-03`, `EM-08` | `EM-01` (`exec-modes`), `AD-03` (`anti-drift`), `GS-02` (`schemas`) | ⚠️ **ERRONEOUS CITE:** `EM-03` is Step-by-Step Context. Whole-file rewrite ban is `EM-01` and `AD-03`. |
| `<editing>` | Gated (`execution-modes.md`) | `EM-03`, `EM-08` | `EM-01`, `EM-08` (`exec-modes`), `AD-23` (`anti-drift`), `GS-09`..`GS-11` | ⚠️ **ERRONEOUS CITE:** `EM-03` is Step-by-Step Context. Patch discipline is `EM-01`, `EM-08`, and `AD-23`. |
| `<new_machinery>` | Gated | `AD-10`, `AD-13`, `AD-25` | `AD-25`, `AD-10`, `AD-13` (`anti-drift`) | ✅ **VERIFIED:** Accurate. |
| `<detour>` | Gated | `AD-10`, `AD-13`, `AD-25` | `AD-05`, `AD-10`, `AD-12` (`anti-drift`) | ⚠️ **INCOMPLETE:** Omitted `AD-05` (Operator Challenge Boundary), the verbatim source of `<detour>`. |
| `<authoring>` | Gated (`index.md`) | `WP-06, 07, 24, 25`, `FA-01, 03, 05` | `FA-13`, `FA-06`, `FA-02`, `FA-10` (`file-arch`), `WP-06, 07, 10, 19, 24, 25` | ⚠️ **INCOMPLETE:** Omitted `FA-13` (Flat YAML), `FA-06` (concept schema), `WP-10` (one chunk), and `WP-19` (exemptions). |
| `<trade_off>` | Gated (`execution-modes.md`) | `EM-06`, `EM-07` | `EM-06`, `EM-07` (`exec-modes`), `GS-12`, `GS-13` (`schemas`) | ✅ **VERIFIED:** Accurate. |
| `<handover>` | Gated (`execution-modes.md`) | `EM-09` | `EM-09`, `EM-02` (`exec-modes`), `AD-06` (`anti-drift`) | ✅ **VERIFIED:** Accurate. |
| `<iterative>` | Gated (`execution-modes.md`) | `EM-10`, `EM-11` | `EM-10`, `EM-11` (`exec-modes`), `AD-04` (`anti-drift`) | ✅ **VERIFIED:** Accurate. |
| `<schemas>` | Gated (`governance-schemas.md`) | `GS-01`..`GS-06` | `GS-01`, `GS-09`, `GS-10`, `GS-11` (`governance-schemas.md`) | ⚠️ **INEXACT:** `GS-01..06` are general/frontmatter rules. Exact patch schema rules are `GS-09`, `GS-10`, and `GS-11`. |
| `<sync>` | Gated | `EM-12` | `EM-12` (`exec-modes`), `AD-23` (`anti-drift`) | ✅ **VERIFIED:** Accurate. |
| `<pointers>` | Terminal Guard | `general-informatics-router.md`, `WP-25` | `general-informatics-router.md`, `WP-25`, `WP-18` (`writing`), `AD-26` | ✅ **VERIFIED:** Accurate. |

---

## 3. Cross-File & Dossier Inconsistencies Discovered

### 3.1 Propagation of the Erroneous `AD-26` Reference
Because `AD-26` was mistakenly recorded as `<hold_position>` during early dossier drafting, the error spread into three separate artifacts:
1. `13-candidate-3A-xml.md` line 110: `| <hold_position> | Unconditional | anti-drift-rules.md (AD-26) |`
2. `12-status-index.md` line 52: `AD-26 added to codify <hold_position> (anti-sycophancy and narrow-correction discipline) in the canonical library (08-discussion-and-open-threads.md §5)`
3. `FinalizationDossier/00-research-critique-and-architecture-design.md` line 60: `+ Anti-Sycophancy Hold Position (AD-26)`

**Reality:** In `anti-drift-rules.md`, line 56 explicitly codifies Hold Position as `AD-22 [P2 | I88/E91/R08] Surgical Edits & Anti-Overcorrection (Hold Position)`. `AD-26` is `Universal Instruction Parsimony`. `FinalizationDossier/05-execution-antidrift-governance-audit.md` (lines 50–52) and `log.md` (line 8) both confirm `AD-22` was the patched rule.

### 3.2 Phantom Tag Names in `FinalizationDossier/06-cross-dependency-and-verification-report.md`
Section 2 (lines 28–49) of `06-cross-dependency-and-verification-report.md` carries a provenance table with 5 phantom tag names:
- `<act_now>` (non-existent in `v1.0`)
- `<creating_files>` (non-existent in `v1.0`)
- `<options>` (in `v1.0` this is `<trade_off>`)
- `<comparing>` (in `v1.0` this is inside `<trade_off>`)
- `<multi_step>` (in `v1.0` this is `<iterative>`)

And Section 2 omits 5 legitimate `v1.0` contract tags:
- `<product_first>`
- `<reuse>`
- `<recovery>`
- `<schemas>`
- `<pointers>`

Furthermore, Table CD-02 (line 15) states:
`Renamed v0.3 tags (<always>, <writing>, <files>, <dispatch>) to v1.0 tags (<target>..<sync>, <authoring>, <creating_files>, etc.)`
This proves that Section 2 of Dossier `06` was based on an outdated intermediate draft and never synchronized with the finalized Candidate `3A`/`3B` blocks.

### 3.3 Audit of `04-empirical-test-protocol.md`
- **Gating Alignment:** Task matrix `T1`–`T12` in §3 is 100% aligned with the finalized `v1.0` contract tags (`<stop_repairing>`, `<authoring>`, `<editing>`, `<trade_off>`, `<handover>`, `<schemas>`, `<new_machinery>`, `<detour>`, `<product_first>`, `<scope>`).
- **Minor Count Inconsistency in §8b (line 183):** States *"11 unconditional rules as bullets inside one `<always>` wrapper"*, whereas the finalized contract has **12 unconditional rules** (`<target>` through `<surgical>`).

### 3.4 Audit of `01-decision-register.md`
- **Settled & Post-Research Decisions:** Thoroughly documents `DEC-01` through `DEC-24`.
- **Carrier Consensus:** Correctly records `DEC-21` (physical byte-identical carrier synchronization across `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md`) and `DEC-22` (Two-Layer separation with `base_ref`).
- **Note:** `hold_position` is not indexed in Part H table, although covered under `DEC-24` in `FinalizationDossier/00`.

### 3.5 Audit of `11-instruction-surface-architecture.md`
- **Surface Precedence Matrix:** Accurately reflects 2026 vendor CLI and IDE behaviors (Codex, Claude Code, Gemini CLI, Copilot, Cursor).
- **Two-Layer Architecture:** Correctly specifies Layer 1 (Universal Contract, ~1,510–1,556 tokens) and Layer 2 (Repo-Specific Context, ~295 tokens).
- **Questions Q1–Q5:** Fully answered and consistent with `DEC-21`..`DEC-24`.

---

## 4. Portability & Link Integrity Audit

### 4.1 Machine-Specific `file:///` Absolute Links (`RBL-05`)
An exhaustive scan revealed **174 occurrences** of machine-specific `file:///c:/GitDev/apexai-os-meta/...` URIs across 12 files:
- `03-BLUEPRINT-agents.md`: 12 links
- `11-instruction-surface-architecture.md`: 4 links
- `13-candidate-3A-xml.md`: 33 links
- `14-candidate-3B-hybrid.md`: 4 links
- `FinalizationDossier/00-research-critique-and-architecture-design.md`: 28 links
- `FinalizationDossier/01-contract-and-blueprint-suite-audit.md`: 26 links
- `FinalizationDossier/02-governance-register-and-test-protocol-audit.md`: 16 links
- `FinalizationDossier/03-root-index-and-router-audit.md`: 13 links
- `FinalizationDossier/04-writing-and-file-architecture-audit.md`: 13 links
- `FinalizationDossier/05-execution-antidrift-governance-audit.md`: 15 links
- `FinalizationDossier/06-cross-dependency-and-verification-report.md`: 15 links
- `FinalizationDossier/index.md`: 25 links

**Impact:** These links break on Linux workspaces (`/root/workspaces/<repo>`), in WSL2, in CI pipelines, and on any other developer machine. They must be converted to portable relative paths.

### 4.2 Broken Relative Links (15 Broken Links Found)
1. **`v2-always-on-architecture/index.md` (lines 12–17):**
   - `../../general-informatics-router.md`
   - `../../writing-profile.md`
   - `../../file-architecture.md`
   - `../../execution-modes.md`
   - `../../anti-drift-rules.md`
   - `../../governance-schemas.md`  
   *Root Cause:* Path from `v2-always-on-architecture/` to `apex-meta/informatics/` requires three levels (`../../../`), not two (`../../`).
2. **`FinalizationDossier/03-root-index-and-router-audit.md` (lines 29, 34):**
   - `Agent_Setup/index.md` and `MMM/index.md` referenced without path traversal from `FinalizationDossier/` (`../../../`).
3. **`FinalizationDossier/05-execution-antidrift-governance-audit.md` (lines 8–9):**
   - `ResearchOfFile10/RESULTS-05-verification-vs-ceremony.md` (does not exist; real file is `ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-05-self-authored-criteria.md`)
   - `ResearchOfFile10/RESULTS-07-anti-overengineering.md` (does not exist; real file is `ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-07-over-building.md`)
4. **`FinalizationDossier/06-cross-dependency-and-verification-report.md` (line 19):**
   - `MMM/index.md` missing path traversal (`../../../MMM/index.md`).

---

## 5. Automated Conformance & Adversarial Test Gate Audit

### 5.1 Deterministic OKF & Apex Profile Validator
Command executed:
```powershell
python apex-meta/scripts/okf_validator.py --target apex-meta/informatics
```
**Output:**
```
============================================================
OKF Validator Report for: apex-meta/informatics
============================================================
Summary: OKF Errors: 0 | Apex Profile Errors: 0 | Advisories: 12
```
- **OKF Errors:** `0` (100% compliant)
- **Apex Profile Errors:** `0` (100% compliant)
- **Advisories:** `12` (all 12 are pre-existing STE-SENTENCE-LENGTH warnings permitted under `WP-01` and `GS-21`).

### 5.2 Pytest Adversarial & Canonical Ownership Suite
Command executed:
```powershell
python -m pytest apex-meta/informatics/tests/ -q
```
**Output:**
```
196 passed, 97 subtests passed in 0.49s (100%)
```
- `test_canonical_ownership.py`: 10/10 passed (zero duplicate IDs, all canonical pointers resolve, zero cross-file owner collisions, authoritative schema separation).
- `stress_test_m2_challenger.py`: Passed (router ceilings, XML tags, frontmatter, ranking syntax, primacy).
- `test_informatics_e2e.py`: Passed (end-to-end task workflows, mode dispatch).
- `test_tier5_adversarial.py`: Passed (context isolation simulation, operational lore codification, exact patch semantics, Minto BLUF, anti-overcorrection title assertion).

---

## 6. Proposed Surgical Remediation Plan

The following surgical edits are recommended to bring all dossier and candidate artifacts to 100% flawless consistency:

### 1. Fix Section 3 Provenance Table in `13-candidate-3A-xml.md`
Replace lines 104–125 with the verified Canonical Provenance Table from Section 2 of this report, correcting `AD-26` $\rightarrow$ `AD-22`, `AD-11/14/15` $\rightarrow$ `AD-19/20/06`, `AD-06` $\rightarrow$ `AD-02/07`, `AD-12` $\rightarrow$ `AD-11`, `FA-02` $\rightarrow$ `FA-01`, `EM-03` $\rightarrow$ `EM-01`, and adding `AD-18`.

### 2. Synchronize Provenance Table in `FinalizationDossier/06`
Replace Section 2 (lines 28–49) of `06-cross-dependency-and-verification-report.md` with the exact 22-clause contract tag list, eliminating phantom tags (`<act_now>`, `<creating_files>`, `<options>`, `<comparing>`, `<multi_step>`) and restoring the missing clauses (`<product_first>`, `<reuse>`, `<recovery>`, `<schemas>`, `<pointers>`).

### 3. Correct `AD-26` Typo in Meta-Indexes
In `12-status-index.md` line 52 and `FinalizationDossier/00` line 60, change `AD-26` to `AD-22` when referring to `<hold_position>`.

### 4. Convert Absolute `file:///` Links to Relative Paths
Batch-convert all 174 `file:///c:/GitDev/apexai-os-meta/...` URIs in `v2-always-on-architecture/` and `FinalizationDossier/` to repository-relative markdown links (`../../...`).

### 5. Fix Broken Relative Links
- Fix 6 links in `v2-always-on-architecture/index.md` from `../../` to `../../../`.
- Fix 2 research packet links in `FinalizationDossier/05` to point to `ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-05-self-authored-criteria.md` and `RESULTS-07-over-building.md`.
- Fix sub-bundle links in `FinalizationDossier/03` and `06` to include proper relative traversal.
