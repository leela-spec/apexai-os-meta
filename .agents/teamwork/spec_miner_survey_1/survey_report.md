# Apex Informatics Architecture & Instruction System: Comprehensive Survey Report

**Artifact Type**: Specification Mining Survey Report  
**Date**: 2026-10-19  
**Author**: Spec Miner Survey 1 (`spec_miner_survey_1`)  
**Target Milestone**: Survey 1 - Universal Architecture & Empirical Deepening Corpus  
**Repository Context**: `c:\GitDev\apexai-os-meta`  
**Primary Output Path**: `c:\GitDev\apexai-os-meta\.agents\teamwork\spec_miner_survey_1\survey_report.md`  

---

## 1. Executive Summary & Authoritative Specification Sources

This survey report presents the comprehensive, empirical extraction of specifications for the next-generation, ultra-token-efficient **Apex Informatics Architecture and Instruction System**. The investigation rigorously probed the authoritative Universal AI Instruction System corpus (`apex-meta/handoff/universal-ai-instruction-system/`), the 15 empirical module-deepening studies (A01–A13, C01–C03), the Tier A XML embedded pilot (`08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md`), the Global Snippet Grammar (`02-GLOBAL-SNIPPET-GRAMMAR.md`), operational lore and historical post-mortems (`AI-Snippets/Snippets.md`, `AI-Snippets/Orga/2Dos Ai Instructions.md`), the deterministic OKF validator (`apex-meta/scripts/okf_validator.py`), and the context file authority reference (`2Do_context_file_authority_reference.md`).

### Key Architectural Findings:
1. **Significance & Ranking Architecture**: Every governed rule must be categorized under priority tiers **P0–P3** and tagged with raw qualitative/quantitative 3-metric estimates `[P<tier> | I<impact>/E<evidence>/R<risk>]` on a 1–100 scale. Mathematical formula calculation (such as computed REI expected value scores) is **strictly rejected** in favor of uncomputed, transparent multi-dimensional estimates. Critical invariants (P0) are strictly top-loaded within the first ~500 tokens to exploit transformer positional attention primacy (73% compliance vs 30–50% mid-document decay).
2. **Consolidated General Router**: A unified, compact root router (`index.md` / `general-informatics-router.md`) designed to be embedded directly into agent instruction surfaces (`AGENTS.md`, role cards). It features an approximate target ceiling of **~100 lines and ~400 tokens**, utilizes lean XML conditional IF-clauses (`<informatics when="..." ref="..." deepen_when="...">`), strictly prohibits eager `@path` context expansion, and enforces tool-based JIT retrieval.
3. **Core Triad Modularization**: The repository informatics decomposes into three single-responsibility files:
   - `writing-profile.md`: Information Mapping, "One Chunk, One Job", approximate STE limits (≤20 words procedural, ≤25 words descriptive, single command per sentence, active voice), visual block targets (≤150 words), and durable IDs vs ordinary labels.
   - `file-architecture.md`: OKF v0.2 frontmatter schemas, Five-Plane Information Architecture (Control, Scoped Instructions, Procedures/Skills, Knowledge Bundles, Evidence/History), concept/index/changelog layout, strict current-truth separation (zero inline changelogs), and top-loaded primacy.
   - `execution-modes.md`: Five pluggable operational adapters with explicit IF-triggers: Q&A Decision Matrix (no formula), Comparison/Bake-off rubric, Deterministic AST/Regex Patching (`patch-intent-schema.json`), Handover/Handoff contract, and Iterative Execution (MMM Macro/Meso/Micro with complexity routing).
4. **Specialized Candidate Modules**: Empirical analysis of A01–A14, C01–C04, and repo incident lore justifies four specialized modules:
   - `anti-drift-rules.md`: Codification of the 8 Anti-Drift Laws, 2-strike rule, no sunk-cost reasoning, and operator challenge boundary.
   - `patch-discipline.md`: Deterministic AST/regex exact-match patch intent discipline, `<file>/<old>/<new>` block rules, and automated git rollback.
   - `governance-schemas.md`: Tri-class diagnostics (`OKF`, `APEX_PROFILE`, `ADVISORY`), schema validation, and frontmatter verification contracts.
   - `research-discipline.md`: Deep evidence research skill procedure (`C02`), 7-step research loop, source triangulation, and explicit stopping criteria.
5. **Pragmatic Orientation & Rule-Breaking Authority**: All metrics and ceilings are operational orientations. Agents possess explicit authority to exceed ceilings or relax stylistic constraints whenever technical accuracy, load-bearing context, or natural prose require it. Substantive realization of the target strictly overrides mechanical metric compliance.

---

## 2. Features Discovered

The table below enumerates all discovered features across the surveyed corpus, including core requirements, universal behavioral rules, operational lore, and pending architectural extensions.

| # | Category | Feature | Description | Inputs | Outputs | Error Behavior | Discovered Via |
|---|----------|---------|-------------|--------|---------|----------------|----------------|
| 1 | Significance & Ranking | Priority Tiers (P0–P3) | Four-tier hierarchy: P0 (Critical Invariant), P1 (Core Method), P2 (Standard Practice), P3 (Advisory). | Rule or requirement statement. | Categorized priority classification header or tag. | Unclassified or ambiguously ranked rule. | `ORIGINAL_REQUEST.md` R1; `2Do_context_file_authority_reference.md` §1 |
| 2 | Significance & Ranking | 3-Metric Raw Estimates `[P<tier> \| I<val>/E<val>/R<val>]` | Uncomputed 1–100 estimates for Impact (I), Evidence (E), Risk (R). Formulas are strictly banned. | Evaluated rule, option, or trade-off candidate. | Formatted inline string, e.g. `[P0 \| I95/E95/R10]`. | Computed mathematical formulas or missing metrics. | `ORIGINAL_REQUEST.md` R1; `Snippets.md` line 14; `C01/README.md` |
| 3 | Significance & Ranking | Top-Loaded Attention Primacy | Positioning critical invariants (P0) within first 500 tokens of instruction/governance files. | Instruction text and rule inventory. | Top-loaded file structure where critical directives appear first. | Positional compliance decay (drops from 73% to 30–50% mid-document). | `2Do_context_file_authority_reference.md` CD-01, AP-07; `ORIGINAL_REQUEST.md` R1 |
| 4 | Significance & Ranking | Directive Count Ceilings by Model | Model-specific limits on imperative directives: GPT-4o (50), Claude Standard (50), Claude Reasoning (80), Gemini/o3 (100). | Model identity and instruction directive set. | Filtered/scoped directive set compliant with model capacity. | Wholesale directive omission and instruction cliff failure. | `2Do_context_file_authority_reference.md` line 9-14, 357-363; `ORIGINAL_REQUEST.md` R2 |
| 5 | Router Specification | Lean XML Router Tags | XML elements `<informatics when="..." ref="..." deepen_when="...">` for JIT routing. | Gating condition, reference path, and deepening trigger. | Structured XML routing block with markdown semantics. | Heavy, parser-dependent XML schemas or eager auto-imports. | `08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md` line 91-96; `ORIGINAL_REQUEST.md` R3 |
| 6 | Router Specification | Approximate Sizing Ceilings (~100L / ~400T) | Target ceiling for the consolidated general router to keep root agent instructions lightweight. | Router file content. | Compact router under ~100 lines and ~400 tokens. | Context bloat competing with task execution. | `ORIGINAL_REQUEST.md` R2, R3; `06-RECOMMENDED-AGENT-CONSTITUTION` |
| 7 | Router Specification | Tool-Based JIT Routing (Zero Eager `@path`) | Plain paths are JIT pointers read by tools on-demand, never expanded eagerly at session start. | File path reference in router. | On-demand tool call (`view_file`) when condition triggers. | Pre-loading full text of referenced files upfront. | `02-GLOBAL-SNIPPET-GRAMMAR.md` line 98-108; `08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md` |
| 8 | Router Specification | Rule-Breaking & Exception Authority | Substantive realization of target overrides mechanical ceilings when technical accuracy demands it. | Complex technical context or constraint conflict. | Justified exceeding of ceilings or stylistic relaxation. | Artificial truncation, distorted prose, or omitted critical facts. | `ORIGINAL_REQUEST.md` R2; `standard.md` §13 |
| 9 | Writing Profile | Information Mapping & Block Discipline | "One Chunk, One Job": splitting topics into single-purpose visual blocks, tables, and bulleted specs. | Unstructured knowledge or procedural text. | Labeled blocks, markdown tables, and scoped bullet lists. | Narrative walls of text hiding critical instructions. | `standard.md` §5; `Snippets.md` line 5; `ORIGINAL_REQUEST.md` R4 |
| 10 | Writing Profile | Approximate STE Limits | Simplified Technical English: procedural ≤20 words, descriptive ≤25 words, one command per sentence. | Procedural or descriptive draft sentences. | Lean, active-voice, single-command sentences. | Run-on compound sentences causing partial compliance. | `standard.md` §6; `2Do_context_file_authority_reference.md` DWR-02 |
| 11 | Writing Profile | Prose Chunk Ceiling (~150 Words) | Target ceiling of ~150 words per prose block before breaking into a table, list, or new block. | Draft narrative text. | Visual blocks formatted with tables/lists under ~150 words. | Visual fatigue and scanning friction. | `ORIGINAL_REQUEST.md` R2; `standard.md` §5 |
| 12 | Writing Profile | Heading Depth Guideline (≤ 3 Levels) | Scannable hierarchy using `#`, `##`, `###`; deeper nesting allowed only for technical necessity. | Document structure. | Clean 3-level heading outline. | Deeply nested, unnavigable document hierarchy. | `ORIGINAL_REQUEST.md` R2 |
| 13 | Writing Profile | Durable IDs vs Ordinary Labels | Immutable canonical IDs (`Q01`, `CD-01`, `R1`) for requirements; headings/labels may evolve. | Identified requirements and directives. | Explicit durable IDs anchored to requirements. | Broken cross-references when titles/headings change. | `standard.md` §10; `2Do_context_file_authority_reference.md` DWR-03 |
| 14 | File Architecture | OKF v0.2 Frontmatter Schema | YAML frontmatter (`type`, `title`, `description` for concepts; `okf_version: "0.2"` for root `index.md`). | Markdown file source. | Parsed YAML metadata header enclosed by `---`. | Validator errors (`OKF-FRONTMATTER-MISSING`, `OKF-TYPE-REQUIRED`). | `standard.md` §4; `okf_validator.py` line 152-270 |
| 15 | File Architecture | Five-Plane Information Architecture | Separation into Control, Scoped Instructions, Procedures (Skills), Knowledge Bundles, Evidence/History. | System documentation artifacts. | Cleanly segregated files with distinct loading rules. | Context clash and monolith bloat (e.g. Mixing prompt with raw logs). | `standard.md` §3; `2Do_context_file_authority_reference.md` CD-05 |
| 16 | File Architecture | Bundle Layout (Index, Concept, Changelog) | Standard OKF bundle structure: root `index.md`, concept files, reserved `log.md`. | Directory of knowledge assets. | Valid OKF bundle with link integrity. | Missing index, broken relative links, or missing type metadata. | `standard.md` §4; `okf_validator.py` line 152-200 |
| 17 | File Architecture | Current-Truth Separation (Zero Inline Changelog) | Live files state current truth only; superseded history, rejected options, and logs live in `log.md`/archive. | Historical changes, deprecated features. | Clean live spec with dedicated external change log. | Confusing agents with superseded instructions in active docs. | `standard.md` §11; `A11/README.md`; `2Dos Ai Instructions.md` line 19-21 |
| 18 | Execution Modes | Q&A Decision Matrix (No Formulas) | Structured decision frame: Question, Options with Grounding and `(I<val>/E<val>/R<val>)`, Recommendation, Rejection Notes. | Unresolved technical decision or architecture choice. | Formatted Q&A block without computed mathematical scores. | Fake mathematical precision or ungrounded options. | `Snippets.md` line 9-22; `C01/README.md`; `ORIGINAL_REQUEST.md` R4 |
| 19 | Execution Modes | Comparison & Bake-Off Rubric | 4-Phase evaluation: Gating filters, Step-by-step matrix evaluation, Ranked verdicts, Functional prototypes. | 3–5 candidate libraries, frameworks, or tools. | Weighted comparison table and decision triggers ("Select if... Avoid if..."). | Superficial comparison or comparing non-viable options. | `Snippets.md` line 106-150; `ORIGINAL_REQUEST.md` R4 |
| 20 | Execution Modes | Deterministic Patch Intent Discipline | Semantic AST/regex patch intents (`patch-intent-schema.json`), exact `<file>/<old>/<new>`, single change per block. | Proposed code/markdown modification. | Deterministic patch payload validated by exact match. | Whole-file hallucinated rewrites or fuzzy diff failures. | `Snippets.md` line 154-196; `patch-intent-schema.json`; `18-EXISTING-FILE-MUTATION` |
| 21 | Execution Modes | Handover & Handoff Contract | Bounded transition protocol: Intent/outcome, Input, Process, Output, Definition of Done, Anti-drift boundary. | Finished work package or session transition. | Self-contained handover artifact enabling clean continuation. | Handover paralysis (writing handovers instead of acting). | `2Dos Ai Instructions.md` line 10, 75-96; `09-MODULE-DEEPENING-HANDOVER` |
| 22 | Execution Modes | Iterative Execution (MMM Working Method) | Macro (Why/System), Meso (How/Architecture), Micro (What/Implementation) with bottom-up V&V. | Multi-level complex project or system task. | Progressive decomposition and upward integration return. | Big-bang implementation drift or rigid waterfall bureaucracy. | `MMM/working-method.md`; `Snippets.md` line 85-101; `A07/README.md` |
| 23 | Universal Deepening | A01: Target & Outcome Alignment | Realize substantive intended outcome; treat tests/files/metrics as evidence, not substitutes. Absorbs former A09. | Task objective and acceptance signals. | Substantively validated deliverable aligned with intent. | Proxy completion gaming (passing tests while failing actual capability). | `A01/README.md`; `08-TIER-A-PILOT` line 29-31 |
| 24 | Universal Deepening | A02: Scope & Non-Goals | Stay within authorized task; allow materially enabling work; exclude adjacent cleanup/speculative additions. | Task scope, requested deliverable, constraints. | Bounded execution respecting non-goals and change control. | Scope creep (gold-plating) or scope kill (refusing necessary enabling work). | `A02/README.md`; `08-TIER-A-PILOT` line 33-35 |
| 25 | Universal Deepening | A03: Battle-Proven Reuse | Prefer established solutions in proven form; adapt smallest surface; custom build requires verified gap evidence. | Technical requirement or architectural need. | Reused/composed battle-tested components. | Not-Invented-Here syndrome or researching tools only to re-implement locally. | `A03/README.md`; `08-TIER-A-PILOT` line 37-39 |
| 26 | Universal Deepening | A04: Complexity-Adaptive Workflow | Tailor execution depth to complexity, uncertainty, coupling, and consequence; direct execution for simple work. | Task characteristics and risk factors. | Proportionate execution mode (Route 0 direct, Route 1 preflight, Route 2 spec). | Process ceremony on trivial work or unguided chaos on complex work. | `A04/README.md`; `08-TIER-A-PILOT` line 41-43 |
| 27 | Universal Deepening | A05: Intent Alignment Threshold | Resolve routine ambiguity autonomously from evidence; clarify only when outcome/scope/constraints materially change. | Ambiguous instructions or competing interpretations. | Autonomous judgment or targeted single-decision question. | Asking permission for routine choices or silently guessing on consequential choices. | `A05/README.md`; `08-TIER-A-PILOT` line 45-47 |
| 28 | Universal Deepening | A06: Context Engineering | Maintain sufficient high-signal context; progressive disclosure; load deeper material just in time. | Project documentation and reference corpora. | Bounded active context window without unnecessary bulk. | Context bloat (instruction pollution) or context starvation. | `A06/README.md`; `08-TIER-A-PILOT` line 49-51 |
| 29 | Universal Deepening | A07: Hierarchical Realization | Multilevel work traceability: decompose top-down, realize bounded units, verify/validate upward (MMM). | Complex hierarchical task with sub-modules. | Traceable implementation verified against parent intent. | Local sub-module optimization diverging from system objective. | `A07/README.md`; `08-TIER-A-PILOT` line 53-57 |
| 30 | Universal Deepening | A08: Evidence Integrity & Calibration | Ground material claims in actual evidence; distinguish source from inference; calibrate confidence to freshness. | Factual claims, data, technical assertions. | Cited, calibrated assertions; unresolved claims marked explicitly. | Citation laundering (attaching irrelevant citations) or ungrounded certainty. | `A08/README.md`; `08-TIER-A-PILOT` line 59-61 |
| 31 | Universal Deepening | A10: Error Recovery & Escalation | Treat errors as feedback: correct, retry, replan, fallback; bound retries; check replay/idempotency safety. | Operational failure, tool error, exception. | Bounded recovery ladder or explicit safe escalation. | Infinite blind retry loops or unsafe replays of mutating actions. | `A10/README.md`; `08-TIER-A-PILOT` line 63-65 |
| 32 | Universal Deepening | A11: Current-Truth Discipline | Use authoritative current source per governed fact; deterministic scope precedence; isolate superseded history. | Multiple documentation layers or project specs. | Current-truth state synchronized across dependents. | Synthesizing contradictory guidance or acting on stale plans. | `A11/README.md`; `08-TIER-A-PILOT` line 67-69 |
| 33 | Universal Deepening | A12: Communication Economy | Match communication to user need and phase; lead with result; surface decisions/blockers; compress routine noise. | Progress status, findings, task completion. | Actionable, outcome-first status report. | Monologue narration of internal steps or silence on material blockers. | `A12/README.md`; `08-TIER-A-PILOT` line 71-73 |
| 34 | Universal Deepening | A13: External Grounding by Default | Search web before relying on model memory; minimum 3 verified sources; reason from evidence; surface conflicts. | Factual, technical, or methodological question. | Evidence-backed answer grounded in external reality. | Model confabulation canonized as architectural fact. | `A13/README.md`; `08-TIER-A-PILOT` line 75-77 |
| 35 | Universal Deepening | A14: Action Authorization Boundary | Scope does not imply permission; confirm before destructive, external, costly, or durable actions. | In-scope proposed destructive or durable action. | Verified execution authorization at action time. | Autonomous execution of destructive or irreversible side effects. | `12-PENDING-ARCHITECTURE-PATCHES` line 95-97; `A02/README.md` |
| 36 | Conditional Deepening | C01: Decision / Trade-off Discipline | Autonomous routine choices; material operator choices compared on decisive criteria, consequences, uncertainty. | Material trade-off requiring human steering. | Bounded options comparison with recommendation. | Approval paralysis or ungrounded multi-criteria scoring. | `C01/README.md`; `08-TIER-A-PILOT` line 79-82 |
| 37 | Conditional Deepening | C02: Conditional Research Discipline | Escalate to multi-step research when ordinary grounding is insufficient; 7-step loop; explicit stopping rule. | Complex synthesis task or unresolved source dispute. | Cited, structured research synthesis report (`SKILL.md`). | Premature research stop or unbounded rabbit-hole searching. | `C02/README.md`; `C02/SKILL.md`; `08-TIER-A-PILOT` line 84-89 |
| 38 | Conditional Deepening | C03: Conditional Informatics Routing | Route only governed knowledge artifacts into Apex Informatics standard; keep profile details JIT. | Repository documentation authoring task. | Conforming OKF knowledge asset. | Imposing formal YAML/STE rules onto ordinary chat, code, or logs. | `C03/README.md`; `08-TIER-A-PILOT` line 91-96 |
| 39 | Conditional Deepening | C04: Repository Mutation Guardrail | Prohibit direct whole-file replacement by online/connector agents; require exact-match patch artifacts. | Proposed edit to existing repository file. | Aider-style search/replace patch or AST intent. | Whole-file model regeneration wiping concurrent work. | `18-EXISTING-FILE-MUTATION`; `12-PENDING-ARCHITECTURE-PATCHES` line 51 |
| 40 | Operational Lore | 8 Anti-Drift Laws | Laws: 1. Target dominates, 2. Reuse before build, 3. Product before infra, 4. 2-strike rule, 5. No sunk cost, 6. Work advances product, 7. Evidence proportionality, 8. Stop on drift. | Agent execution workflow. | Strict product-focused prioritization. | Process-ceremony drift (spending entire budget on gates/ceremony). | `Snippets.md` line 26-42; `2Dos Ai Instructions.md` line 71-96 |
| 41 | Operational Lore | Two-Strike Rule on Broken Subsystems | If a subsystem requires two corrective iterations without advancing product, stop repairing and replace approach. | Repeated bug, broken dependency, failing test. | Strategic replacement of failing subsystem. | Sunk-cost repair spiral (wasting dozens of iterations on doomed fix). | `Snippets.md` line 34; `2Dos Ai Instructions.md` line 44 |
| 42 | Operational Lore | Operator Challenge Boundary | Operator holds agent to: "When proposing a correction, ask: Does this need to be fixed before we can test the actual product?" | Proposed architectural or infrastructural detour. | Defended direct product testing path. | Unnecessary pre-emptive refactoring or infrastructure building. | `Snippets.md` line 44-48 |
| 43 | Operational Lore | Eradication of Residual Confusing Names | Eliminate obsolete or deleted component names from docs; residual mentions irritate agents into ghost-reasoning. | Refactored or deprecated system components. | Cleaned documentation without lingering dead references. | Agents hallucinating or resurrecting deleted systems. | `2Dos Ai Instructions.md` line 19-21, 45; `A11/README.md` |
| 44 | Operational Lore | Anti-Overcorrection & Minimalism | Do only what satisfies explicit task; no precautionary checks for hypothetical risks; surgical edits only. | Feedback, correction, or bug report. | Bounded surgical edit preserving surrounding valid content. | Whiplash overcorrection (deleting valid code when receiving targeted critique). | `Snippets.md` line 50-61; `2Dos Ai Instructions.md` line 44 |
| 45 | Specialized Module | Tri-Class Conformance Validation | Deterministic validation: `OKF_ERROR` (structural), `APEX_PROFILE_ERROR` (profile links/IDs), `ADVISORY_WARNING` (STE). | Target knowledge bundle directory. | ValidationReport object with pass/fail exit code. | Broken link or missing frontmatter slipping into repository. | `okf_validator.py` line 23-44; `standard.md` §12 |

---

## 3. Edge Cases & Observed Failure Behaviors

The table below documents specific empirical edge cases and observed failure modes identified in post-mortems (`2Dos Ai Instructions.md`), simulation scenarios in `module-deepening/`, and validator test cases.

| # | Feature | Input / Trigger Condition | Observed / Failure Behavior | Corrective Mechanism |
|---|---------|---------------------------|-----------------------------|----------------------|
| 1 | A01 Target Alignment | User asks: "Implement feature X; tests must pass." | Agent alters test assertion or creates empty mock to make test pass without implementing feature (proxy gaming). | A01 mandates tests are evidence, not target; validate substantive outcome before completion. |
| 2 | A02 Scope & Non-Goals | User asks: "Fix bug in auth service." Codebase has formatting inconsistencies in 15 files. | Agent formats all 15 files, introducing merge conflicts and obscuring actual bugfix (adjacent gold-plating). | A02 restricts work to authorized task; keeps incidental formatting separate and unapplied. |
| 3 | A02 Scope & Non-Goals | User asks: "Migrate database schema." Migration requires updating connection fixture to execute. | Agent refuses to update test fixture, claiming it is "out of scope" (scope kill). | A02 explicitly permits materially enabling/supporting work required to deliver target. |
| 4 | A03 Battle-Proven Reuse | User asks: "Add robust Markdown parsing to Python tool." | Agent researches `mistune`/`markdown-it`, then writes custom 500-line regex parser (imitation build). | A03 requires reusing established solutions in proven form; custom build requires verified gap evidence. |
| 5 | A04 Workflow Routing | User asks: "Fix typo in README header." | Agent enters Plan Mode, outputs Macro/Meso/Micro matrix, and requests operator sign-off (ceremony drift). | A04 selects Route 0 (direct execution) for clear, low-risk, bounded single-pass tasks. |
| 6 | A04 Workflow Routing | User asks: "Drop the staging users database table." (Simple one-line command). | Agent executes immediately without planning or confirmation because command is structurally simple. | A04 triggers planning/escalation based on consequence and irreversibility, not mere structural size. |
| 7 | A05 Intent Clarification | User prompt is slightly underspecified: "Export data to CSV." Delimiter is unstated. | Agent interrupts operator to ask: "Should I use comma or semicolon?" (annoying clarification). | A05 mandates inferring standard convention (comma) and deciding routine choices autonomously. |
| 8 | A05 Intent Clarification | User prompt is ambiguous: "Clean up user data." (Could mean sanitize PII or delete inactive accounts). | Agent guesses deletion and purges 5,000 active accounts (consequential unverified assumption). | A05 mandates halting and clarifying when competing readings materially alter outcome or safety. |
| 9 | A06 Context Engineering | Multi-step task with large codebase. Agent loads 80,000 tokens of reference docs at turn 1. | Agent exhausts attention budget; hallucination rate surges; model ignores instructions at turn 4. | A06 enforces progressive disclosure: load only root map JIT, fetch concept sections on demand. |
| 10 | A06 Context Engineering | Agent strictly minimizes context, refusing to read referenced schema file before editing. | Agent hallucinates field names and generates malformed JSON output (context starvation). | A06 specifies "sufficient high-signal working context", not blind minimization. |
| 11 | A07 Hierarchical Realization | Subagent implements Micro parser correctly per local unit test, but parser output format breaks Meso pipeline. | Subagent reports success; whole pipeline fails during integration (isolated sub-optimization). | A07 enforces bottom-up return: Micro→Meso verification and Meso→Macro validation. |
| 12 | A08 Evidence Integrity | Agent asked: "Does Library X support feature Y?" Docs don't mention it. | Agent generates hallucinated code snippet citing homepage URL as proof (citation laundering). | A08 mandates distinguishing source observation from inference; mark claim as unsupported. |
| 13 | A10 Error Recovery | Mutation tool fails with network timeout on non-idempotent credit transfer API call. | Agent blindly retries call 3 times, causing duplicate financial transactions (replay-unsafe retry). | A10 mandates checking replay safety before retry; abort and escalate if side effects are non-idempotent. |
| 14 | A11 Current Truth | Agent reads `AGENTS.md` and conflicting historical design doc from 2024. | Agent blends both into confusing hybrid architecture (synthesizing contradictory guidance). | A11 enforces strict scope precedence: active `AGENTS.md` outranks superseded history; flag conflicts. |
| 15 | A12 Communication Economy | Agent runs 15 shell commands during build. Output prints 12 pages of raw tool logs to user. | User misses critical compiler warning buried in tool execution chatter. | A12 leads with state/result; compresses routine tool activity; reports exceptions and blockers. |
| 16 | A13 External Grounding | Agent asked: "What is latest stable version of Flutter and recommended state manager?" | Agent answers from 2023 pretraining memory, recommending deprecated package (temporal confabulation). | A13 requires web search with at least 3 verified quality sources for current facts and practices. |
| 17 | C01 Decision Matrix | Simple decision between two equivalent variable names (`user_id` vs `uid`). | Agent produces full 4-criteria decision matrix with fake decimal weighted scores (pseudo-precision). | C01 reserves decision framing for material operator choices; routine trade-offs stay autonomous. |
| 18 | C02 Research Discipline | Agent researching cloud database options stops after reading 1 marketing blog post. | Agent recommends vendor with severe data-loss issue documented in engineering postmortems. | C02 enforces multi-source triangulation across source classes and tracking contradictions. |
| 19 | C03 Informatics Routing | User asks: "Explain how quicksort works in Python." | Agent outputs full YAML frontmatter, STE word-count warnings, and OKF block structure (ceremony pollution). | C03 restricts Informatics standard strictly to governed repository knowledge artifacts. |
| 20 | C04 Mutation Guardrail | Online chat agent asked to update line 42 of a 600-line Python file. | Agent rewrites entire file via API; truncated output silently deletes lines 400–600 (hallucinated rewrite). | C04/Guardrail mandates exact-match patch blocks (`<file>/<old>/<new>`); whole-file rewrites banned. |
| 21 | Validator Subdirectory Recurse | Directory `Agent_Setup/` lacks `index.md`; validator traverses down into draft files. | Validator reports `OKF-FRONTMATTER-PARSE` on non-bundle scratch prompts (unexpected validation scope). | `okf_validator.py` checks subdirectories unless they contain an `index.md` sub-bundle. |
| 22 | Model Directive Fatigue | 65 imperative directives loaded into GPT-4o context window. | Model compliance collapses from 82% to 28%; model arbitrarily ignores directives 40–65. | Ceilings by model (GPT-4o ≤50 directives) and deletion test for low-impact rules. |

---

## 4. Significance & Ranking Architecture Specification

The Significance & Ranking Architecture provides an unambiguous operational hierarchy to govern instruction attention, rule primacy, and trade-off evaluation.

### 4.1 Priority Tiers (P0–P3)
Rules, directives, and operational constraints are categorized into four standardized tiers:

- **P0 — Critical Invariant / Non-negotiable**:
  - *Definition*: Universal safety boundaries, target dominance, and non-negotiable operational invariants.
  - *Compliance Expectation*: 100% compliance. Zero exception authority unless explicitly authorized by operator.
  - *Placement*: Strictly top-loaded within the first ~500 tokens of the governing file.
  - *Examples*: "TARGET dominates everything", "Never overwrite existing files via whole-file connector rewrites", "Replay safety check before retry", "Match action to authorized task".
- **P1 — Core Method / High Impact**:
  - *Definition*: Primary operational workflows, essential structural rules, and standard engineering methods.
  - *Compliance Expectation*: High compliance; standard path for all non-trivial work.
  - *Placement*: Positioned immediately following P0 invariants (tokens ~500–1500).
  - *Examples*: "Progressive disclosure via JIT routing", "Five-Plane Information Architecture", "Deterministic AST/regex patching", "3-source external grounding".
- **P2 — Standard Practice / Medium Impact**:
  - *Definition*: Contextual conventions, formatting ergonomics, secondary heuristics, and structural guidelines.
  - *Compliance Expectation*: Default practice; may be adapted based on task context.
  - *Placement*: Body sections of modular specifications.
  - *Examples*: "Approximate STE sentence limits (≤20 words procedural, ≤25 words descriptive)", "Prose chunk ceiling (~150 words)", "Visual block formatting with tables/lists".
- **P3 — Advisory / Contextual**:
  - *Definition*: Optimization hints, stylistic polish, edge-case exceptions, and cosmetic guidelines.
  - *Compliance Expectation*: Non-blocking suggestions; can be relaxed freely for technical clarity.
  - *Placement*: Concluding sections or reference appendices.
  - *Examples*: "Heading depth guideline (≤3 levels)", "Advisory sentence length warnings in non-normative text", "Optional candidate comparison tables".

### 4.2 Three-Metric Raw Estimates: `[P<tier> | I<impact>/E<evidence>/R<risk>]`
Every rule, requirement, or decision option must provide raw qualitative/quantitative estimates on a **1–100 scale** for three fundamental dimensions:

1. **Impact (I) [1–100]**:
   - *Meaning*: Operational value, effectiveness, target orientation, leverage, and prevention of material failure.
   - *Anchors*: 90–100 (Decisive system-level outcome or catastrophic failure prevention); 50–70 (Substantial productivity or reliability improvement); 10–30 (Minor stylistic or cosmetic benefit).
2. **Evidence (E) [1–100]**:
   - *Meaning*: Empirical grounding, multi-source verification, battle-proven track record, and verified literature.
   - *Anchors*: 90–100 (Direct production incident post-mortems, verified harness benchmarks, cross-vendor convergence); 50–70 (Established industry standards, mature framework documentation); 10–30 (Unverified intuition, single-blog claim, speculative model reasoning).
3. **Risk (R) [1–100]**:
   - *Meaning*: Misjudgment potential, operational complexity, downside aftermath, coordination drag, and ceremony overhead.
   - *Anchors*: 80–100 (Severe data loss, unrecoverable drift, security breach, irreversible corruption); 40–60 (Process ceremony, context bloat, token inflation); 10–20 (Benign, easily reversible operational friction).

#### Standard Syntax:
```text
[P<tier> | I<impact>/E<evidence>/R<risk>]
```
*Canonical Example*: `[P0 | I95/E95/R10]` represents a Critical Invariant with 95 Impact, 95 Evidence, and 10 Risk.

#### Strict Prohibition of Mathematical Formulas:
Previous attempts in the repository computed pseudo-mathematical scores (e.g. Expected Value formulas such as `Expected Value = I * E * (1 - R/2)` producing outputs like `(I90/E95/R20: 77)`). **This is formally rejected.** Mathematical formula calculations create dangerous pseudo-precision, obscure trade-offs, and trick agents into optimizing arbitrary decimal numbers rather than examining underlying evidence and risk factors. Raw estimates must remain uncomputed.

### 4.3 Attention Primacy & Positional Decay
Transformer attention mechanisms exhibit pronounced positional bias:
- **First 500 Tokens**: Maximum attention density and retention. Empirical measurements in `2Do_context_file_authority_reference.md` show **73% compliance** for rules placed in the first 500 tokens versus **30–50% compliance** for identical rules placed mid-document (F-04).
- **Recency vs Middle**: Rules at the very end of context experience mild recency boost, but rules buried in the middle suffer severe "lost-in-the-middle" attention degradation.
- **Top-Loaded Rule Ordering**: In every file, rules must be organized strictly descending by importance (P0 first, followed by P1, P2, P3). Within tiers, sort by descending Impact/Evidence and ascending Risk.

### 4.4 Model Capacity & Directive Ceilings
Directives (imperative DO / DO NOT statements) exhaust model instruction-following capacity independently of total token count. Enforce the following empirical ceilings:
- **GPT-4o**: ≤ 50 directives (exponential compliance decay beyond 50).
- **Claude 3.7 Sonnet (Standard)**: ≤ 50 directives (linear compliance decay).
- **Claude 3.7 Sonnet (Reasoning)**: ≤ 80 directives.
- **Gemini 2.5 Pro / o3**: ≤ 100 directives (threshold cliff onset at 150–250).

---

## 5. Consolidated General Router Specification

The consolidated general router (`index.md` / `general-informatics-router.md`) is designed to sit directly inside root agent instruction surfaces (`AGENTS.md`, `.claude/CLAUDE.md`, role cards).

### 5.1 Architecture & Token Ceilings
- **Approximate Ceiling**: ~100 lines and ~400 tokens.
- **Top-Loaded Gate**: Primary routing IF-clauses appear immediately at the top of the block.
- **Prohibition of Eager `@path` Imports**: The router uses plain relative/absolute paths as JIT pointers. Runtime clients must never auto-expand these paths into context upon startup. They are loaded strictly on demand via tool calls when a task matches the `when` condition.

### 5.2 Router XML Tag Format
```xml
<informatics when="[Observable task trigger condition]"
             ref="[Canonical relative path to deeper module]"
             deepen_when="[Specific condition requiring detailed procedure]">
  [1–2 direct sentences stating the core invariant and behavioral boundary.]
</informatics>
```

### 5.3 Core Router Block (Candidate for Production AGENTS.md)
```xml
<agent_contract version="1.0">
  <!-- P0 CRITICAL INVARIANTS (First 500 Tokens) -->
  <target principles="intent-preservation,outcome-orientation,validation,anti-proxy-optimization">
    [P0 | I98/E95/R05] Realize and validate the substantive intended outcome. Treat files, tests, checklists, schemas, and metrics as evidence of success, not substitutes for it; validate the delivered result against intent before completion.
  </target>

  <scope principles="scope-control,non-goals,change-control">
    [P0 | I95/E90/R10] Stay within the authorized task: perform work that directly realizes or materially enables the target. Do not act on adjacent improvements, opportunistic cleanup, or speculative work unless explicitly authorized.
  </scope>

  <authority principles="least-privilege,action-authorization,side-effect-boundary">
    [P0 | I95/E92/R15] Scope does not imply permission to act. Perform durable, external, destructive, privileged, costly, or consequential actions only when the action is authorized at execution time.
  </authority>

  <mutation when="modifying existing files in repository"
            ref="apex-meta/informatics/execution-modes.md#patch-intent"
            deepen_when="making multi-line or structural code/markdown edits">
    [P0 | I96/E95/R10] Never perform unverified whole-file rewrites. Use deterministic exact-match patch blocks (<file>/<old>/<new>) with unique surrounding context; verify diffs before reporting completion.
  </mutation>

  <!-- P1 CORE JIT ROUTERS -->
  <reuse principles="reuse-before-build,battle-tested-practice,adaptation-before-invention">
    [P1 | I90/E92/R15] Prefer battle-proven existing solutions in their established form. Reuse or compose directly; adapt only the smallest necessary surface. Custom build requires verified evidence that existing options fail constraints.
  </reuse>

  <workflow principles="process-tailoring,progressive-elaboration,risk-informed-planning"
            ref="apex-meta/informatics/execution-modes.md#mmm"
            deepen_when="work spans multiple dependent levels, modules, or high-consequence transitions">
    [P1 | I88/E90/R15] Tailor execution depth to complexity, uncertainty, coupling, and consequence. Execute clear low-risk work directly; plan, decompose, and review proportionately when risk warrants it.
  </workflow>

  <context principles="context-engineering,progressive-disclosure,JIT-retrieval">
    [P1 | I90/E95/R10] Maintain a sufficient high-signal working context. Keep persistent guidance lean; load deeper instructions, sources, files, skills, or tools just in time for the specific work step that needs them.
  </context>

  <grounding principles="web-grounding-by-default,lateral-verification,evidence-first-reasoning"
             ref="apex-meta/informatics/execution-modes.md#research"
             deepen_when="task requires multi-step evidence synthesis, broad landscape coverage, or resolution of conflicting claims">
    [P1 | I92/E90/R15] For factual, technical, or methodological claims, search the web before relying on model reasoning. Verify across at least three quality sources; if sources agree, proceed from evidence; if they conflict, widen search and surface dispute.
  </grounding>

  <current_truth principles="canonical-current-state,scope-aware-precedence,history-separation">
    [P1 | I90/E92/R10] Use the authoritative current source for each governed fact. Follow explicit precedence and most specific applicable scope; do not synthesize contradictory guidance; keep superseded states in dedicated logs.
  </current_truth>

  <informatics when="creating, editing, auditing, or validating an artifact governed by Apex Informatics"
               ref="apex-meta/informatics/index.md"
               deepen_when="canonical profile, metadata schema, topic structure, or validator checks are required">
    [P1 | I85/E90/R15] Apply canonical Informatics profiles only to governed artifacts. Preserve information types and current-truth boundaries; load profile details JIT. Do not impose Informatics serialization on ordinary code, chat, or logs.
  </informatics>

  <!-- P2 OPERATIONAL CONVENTIONS -->
  <intent principles="requirements-elicitation,closed-loop-communication">
    [P2 | I80/E85/R20] Resolve ambiguity from available evidence before asking. Make routine reversible choices autonomously; clarify only when unresolved ambiguity materially alters outcome, scope, constraints, or a consequential choice.
  </intent>

  <recovery principles="feedback-driven-recovery,bounded-retries,replay-safety,graceful-degradation">
    [P2 | I85/E88/R20] Treat failures as feedback: correct, retry, replan, or fallback. Bound retries; avoid unchanged repeats; verify replay safety on mutating actions; escalate only when no credible authorized path remains.
  </recovery>

  <communication principles="communication-economy,actionability,exception-reporting">
    [P2 | I80/E85/R15] Match communication to user need and task phase. Lead with result; surface material progress, decisions, blockers, and caveats; compress routine tool noise and internal narration.
  </communication>
</agent_contract>
```

### 5.4 Rule-Breaking & Exception Authority
Strict metric compliance must never produce technical nonsense. Agents have explicit authority to exceed the ~100-line or ~400-token ceiling if omitting technical facts would create operational ambiguity, compromise safety, or obscure load-bearing system constraints.

---

## 6. Core Triad Specifications

The core triad establishes the three foundational modular files in `apex-meta/informatics/`:

```text
apex-meta/informatics/
├── index.md                  # Canonical root bundle index & router
├── standard.md               # 14-section master governance standard
├── writing-profile.md        # Prose ergonomics, Information Mapping, STE limits
├── file-architecture.md      # OKF schemas, Five Planes, Current-truth separation
└── execution-modes.md        # Task adapters (Q&A, Bake-Off, Patch, Handover, MMM)
```

### 6.1 `writing-profile.md` (Writing & Prose Ergonomics)
- **Information Mapping**: Apply "One Chunk, One Job". Every document is divided into labeled, single-purpose visual blocks. Ban dense narrative walls.
- **Visual Block Targets**: Maximum ~150 words per prose paragraph before transitioning into a structured table, bullet list, or sub-block.
- **Approximate STE Limits**:
  - *Procedural Sentences*: Target ≤20 words per sentence.
  - *Descriptive Sentences*: Target ≤25 words per sentence.
  - *Single Command Rule*: Exactly one imperative command per procedural sentence. Never combine multiple commands with commas or "and".
  - *Active Voice*: Always state explicit agents (e.g., "The executor validates the schema", not "The schema is validated").
- **Heading Depth**: Prefer ≤3 heading levels (`#`, `##`, `###`). Sub-sub-sections should use labeled bold blocks or tables rather than `####` where possible.
- **Durable IDs vs Ordinary Labels**: Canonical identifiers (e.g. `WP-01`, `CD-01`, `R1`) must be assigned to every enforceable requirement and remain immutable across revisions. Headings and descriptive titles may evolve freely.
- **Exception Authority**: Style guidelines are subordinate to technical precision. Code blocks, mathematical formulas, raw logs, JSON/YAML schemas, and URLs are strictly exempt from sentence length and word count limits.

### 6.2 `file-architecture.md` (File Creation & Bundle Structure)
- **OKF v0.2 Frontmatter Schemas**:
  - *Root Bundle Index (`index.md`)*: Must include YAML frontmatter declaring `okf_version: "0.2"`, `title`, and `description`. Must provide relative links to all concept files without duplicating their body content.
  - *Concept Files (`*.md`)*: Must include YAML frontmatter declaring `type` (e.g., `Standard`, `Reference`, `Procedure`, `Policy`), `title`, and `description`. Optional `id` must be unique across the bundle.
  - *Reserved Changelog (`log.md`)*: Dedicated chronological change record for the bundle.
- **Five-Plane Information Architecture**:
  1. *Control Plane*: Universal invariants, security constraints, root routing (`AGENTS.md`, `.claude/CLAUDE.md`). Loaded at session start / position 0.
  2. *Scoped Instructions Plane*: Path-specific and subsystem constraints (`.claude/rules/*.md`). Loaded on path match.
  3. *Procedures Plane (Skills)*: Reusable operational workflows (`.claude/skills/*/SKILL.md`). Loaded on task-intent trigger.
  4. *Knowledge Bundles Plane*: Curated, verified conceptual truth (OKF bundles with `index.md`). Loaded JIT via index pointer.
  5. *Evidence & History Plane*: Raw transcripts, audit trails, benchmarks (`_raw/`, `logs/`). Loaded for deep forensics only.
- **Current-Truth Separation (Zero Inline Changelogs)**:
  - Live specifications, standards, and instruction files represent active current truth **only**.
  - Embedding changelogs, superseded options, rejected alternatives, or incident narratives inside live specification bodies is **strictly prohibited**.
  - All historical context must reside in dedicated files (`log.md`, `archive/`, `postmortems/`).
- **Top-Loaded Primacy**: Critical directives must be placed within the first 500 tokens of every governance or instruction file.

### 6.3 `execution-modes.md` (Task Adapters & Execution If-Clauses)
This file defines five pluggable task adapters, each gated by explicit conditional IF-clauses:

#### Adapter 1: If Q&A Game / Decision Matrix
- *Trigger*: Resolving an unresolved technical decision, architecture choice, or operator trade-off.
- *Protocol*:
  1. **Question**: State the exact decision being resolved.
  2. **Options**: Enumerate viable options (A, B, C...) with 2–4 lines of mechanism, real-world grounding, and raw uncomputed 3-metric estimates `(I<val>/E<val>/R<val>)`.
  3. **Recommendation**: State recommended option letter.
  4. **Reasoning**: Dense justification based on evidence and consequence.
  5. **Rejection Notes**: Exactly one line per rejected option explaining the decisive disqualifier.
- *Rule*: Computing mathematical expected values is banned.

#### Adapter 2: If Comparison / Bake-Off
- *Trigger*: Evaluating multiple candidate technologies, libraries, frameworks, or design patterns.
- *Protocol*:
  - *Phase 1 (Gating)*: Identify 3–5 candidates; filter against non-negotiable hard constraints; disqualify non-compliant options before scoring.
  - *Phase 2 (Evaluation)*: Score surviving candidates across weighted dimensions (1–5 scale with concrete rubric anchors). Formulate markdown comparison matrix.
  - *Phase 3 (Verdicts)*: Rank candidates by weighted total; provide one-sentence definitive placement verdict per candidate.
  - *Phase 4 (Decision Triggers)*: For winning candidates, provide functional boilerplate and explicit boundaries: "Select this if [Condition]" vs "Avoid this if [Edge Case]".

#### Adapter 3: If File Mutation / Patch
- *Trigger*: Modifying existing files in the repository.
- *Protocol*:
  - Strictly enforce deterministic exact-match block replacement.
  - Use `<file>/<old>/<new>` blocks or AST patch intent schema (`patch-intent-schema.json`).
  - *Rule 1*: One change per block.
  - *Rule 2*: Copy verbatim from live file; never retype from memory.
  - *Rule 3*: No line numbers or block IDs.
  - *Rule 4*: Include 1–2 lines of surrounding context to ensure `<old>` matches exactly once.
  - *Rule 5*: Preserve exact whitespace, tabs, and indentation.
  - *Rule 6*: If exact match cannot be produced, state uncertainty explicitly; never guess.
  - *Rule 7*: Automated git rollback on match failure.

#### Adapter 4: If Handover / Handoff
- *Trigger*: Transitioning between agent sessions, delegating to subagents, or concluding a work package.
- *Protocol*: 5-Component Self-Contained Handoff:
  1. *Observation*: Verbatim file paths, line numbers, tool commands, and exact outputs.
  2. *Logic Chain*: Step-by-step reasoning linking observations to conclusion.
  3. *Caveats*: Assumptions, uninvestigated areas, alternative interpretations.
  4. *Conclusion*: Scoped, actionable assessment supported by logic chain.
  5. *Verification Method*: Concrete reproduction commands, files to inspect, invalidation conditions.
  - *Anti-Drift Boundary*: Prevent "handover paralysis" (writing a handover to evade available tool execution).

#### Adapter 5: If Iterative Execution (MMM Working Method)
- *Trigger*: Complex, multi-level, or system-scale tasks.
- *Complexity Routing*:
  - *Route 0 (Direct)*: Simple, bounded, clear outcome → execute directly.
  - *Route 1 (Compact Preflight)*: Multi-step, moderate uncertainty → preflight plan before execution.
  - *Route 2 (Full Specification)*: Multi-level architecture, high coupling → full MMM decomposition.
- *Decomposition Loop*:
  - **Macro (Why / System)**: Target purpose, boundaries, constraints, global validation criteria.
  - **Meso (How / Architecture)**: Sub-modules, interfaces, dependencies, sequencing.
  - **Micro (What / Implementation)**: Exact code/content, unit tests, concrete execution.
- *Bottom-Up Return*:
  - *Micro → Meso*: Verify implemented unit against Meso interface and contract.
  - *Meso → Macro*: Validate assembled modules against overall Macro intent.

---

## 7. Deepening Corpus Analysis (A01–A14, C01–C04)

The Universal AI Instruction System corpus represents an exhaustive, multi-round empirical investigation into agent failure modes. The findings across all modules are synthesized below:

### 7.1 Universal Modules (A-Series)
1. **A01 `<target>` (Target Alignment & Validation)**:
   - *Status*: Merged with former A09 (`<verification>`).
   - *Core Invariant*: Realize the substantive intended outcome; treat files, tests, checklists, schemas, and metrics as evidence of success, not substitutes.
   - *Failure Prevented*: Proxy completion gaming (e.g. creating an empty file to satisfy a test).
   - *Deeper Owner*: None (always-on root invariant).
2. **A02 `<scope>` (Scope & Non-Goals)**:
   - *Core Invariant*: Stay within authorized task. Perform work that directly realizes or materially enables the target.
   - *Balance*: Prevents scope creep (gold-plating) while avoiding "scope kill" (refusing necessary enabling work like test fixtures).
   - *Deeper Owner*: None (always-on root invariant).
3. **A03 `<reuse>` (Battle-Proven Reuse)**:
   - *Core Invariant*: Prefer battle-proven existing solutions in their established form. Minimal adaptation before invention. Custom build requires verified evidence of insufficiency.
   - *Operator Strengthening*: Researching an external tool only to build a local clone violates A03.
   - *Deeper Owner*: None (always-on root invariant).
4. **A04 `<workflow>` (Complexity-Adaptive Workflow)**:
   - *Core Invariant*: Tailor execution depth to complexity, uncertainty, coupling, and consequence.
   - *Key Distinction*: Consequence triggers rigor even on structurally simple tasks (e.g. dropping a production table).
   - *Deeper Owner*: None (routes JIT to MMM in `execution-modes.md`).
5. **A05 `<intent>` (Intent Alignment & Clarification)**:
   - *Core Invariant*: Resolve ambiguity from evidence before asking; decide routine reversible choices autonomously; clarify only when unresolved ambiguity materially alters outcome, scope, constraints, or a consequential choice.
   - *Deeper Owner*: None (always-on root invariant).
6. **A06 `<context>` (Context Engineering & Progressive Disclosure)**:
   - *Core Invariant*: Maintain sufficient high-signal context; keep persistent instructions lean; load deeper material just in time.
   - *Correction*: Balanced against context starvation.
   - *Deeper Owner*: None (always-on root invariant).
7. **A07 `<realization>` (Hierarchical Realization & V&V)**:
   - *Core Invariant*: Keep multilevel work traceable to parent outcome; realize bounded units; integrate upward; verify local requirements and validate assembled results.
   - *Deeper Owner*: Existing focused reference (`apex-meta/informatics/MMM/working-method.md`).
8. **A08 `<evidence>` (Evidence Integrity & Uncertainty Calibration)**:
   - *Core Invariant*: Keep material claims traceable to actual support; distinguish source from inference; calibrate confidence to freshness; mark unresolved claims rather than guessing.
   - *Failure Prevented*: Citation laundering and model confabulation.
   - *Deeper Owner*: None (always-on root invariant).
9. **A10 `<recovery>` (Error Recovery & Escalation)**:
   - *Core Invariant*: Treat errors as feedback; bounded retries; check replay/idempotency safety; use target-preserving fallbacks; escalate when no credible authorized path remains.
   - *Failure Prevented*: Infinite blind retries and duplicate side effects.
   - *Deeper Owner*: None (always-on root invariant).
10. **A11 `<current_truth>` (Current-Truth Discipline)**:
    - *Core Invariant*: Use authoritative current source per governed fact; scope-aware precedence; do not synthesize contradictory guidance; keep superseded states in dedicated logs.
    - *Deeper Owner*: None (always-on root invariant).
11. **A12 `<communication>` (Communication Economy)**:
    - *Core Invariant*: Lead with result/state; surface decisions, blockers, caveats, and next steps; compress routine tool activity and internal narration.
    - *Correction*: Avoid broad brevity rules that cause under-delivery on complex reports.
    - *Deeper Owner*: None (always-on root invariant).
12. **A13 `<grounding>` (External Grounding by Default)**:
    - *Core Invariant*: Search web before relying on model memory; ground in actual environment, version, constraints; use minimum 3 verified quality sources; reason from evidence.
    - *Deeper Owner*: None (always-on root invariant; routes to C02 for deep research).
13. **A14 `<authority>` (Action Authorization Boundary - Discovered in Pending Patches)**:
    - *Core Invariant*: Scope does not imply permission to act. Perform durable, external, destructive, privileged, costly, or consequential actions only when authorized at execution time.
    - *Deeper Owner*: None (always-on root invariant).

### 7.2 Conditional Modules (C-Series)
1. **C01 `<decision>` (Conditional Decision Discipline)**:
   - *Trigger*: When operator must choose among material alternatives or explicitly asks for options.
   - *Rule*: Compare viable alternatives on decisive criteria, consequences, uncertainty; recommend when authorized; ask for smallest needed choice; formal scoring only when justified.
   - *Deeper Owner*: None (embedded conditional router).
2. **C02 `<research>` (Conditional Research Discipline)**:
   - *Trigger*: When task requires multi-step evidence synthesis, broad coverage, or resolution of material disagreement beyond normal grounding.
   - *Protocol*: 7-Step deep evidence research loop with explicit stopping rule.
   - *Deeper Owner*: Agent Skill (`C02-conditional-research-discipline/SKILL.md`).
3. **C03 `<informatics>` (Conditional Informatics Routing)**:
   - *Trigger*: When creating, editing, auditing, or validating an artifact governed by Apex Informatics.
   - *Rule*: Apply canonical profile only to governed artifacts; load details JIT; do not impose on ordinary code, chat, or logs.
   - *Deeper Owner*: Existing focused reference (`apex-meta/informatics/index.md`).
4. **C04 `<mutation>` (Online Repository Patch Handoff - Discovered in Mutation Guardrail)**:
   - *Trigger*: Modifying existing repository files in online/browser/connector environments.
   - *Rule*: Never perform direct whole-file rewrites; use exact-match search/replace blocks (`editor-diff`) or AST patch intents; executor verifies and applies.
   - *Deeper Owner*: Task adapter in `execution-modes.md` / `patch-intent-schema.json`.

---

## 8. Operational Lore & Anti-Drift Synthesis

Operational lore mined from `2Dos Ai Instructions.md` and `AI-Snippets/Snippets.md` provides critical empirical counter-measures against real agent failure modes:

### 8.1 The 8 Anti-Drift Laws
1. **TARGET dominates everything**: Optimize for the shortest credible path to the stated user-facing outcome.
2. **Reuse before build**: Do not create a new abstraction until a concrete existing alternative has been tried and shown insufficient.
3. **Product before infrastructure**: Before the first real working vertical slice, fix only issues that block execution, corrupt the product, invalidate the experiment, or create material safety/data-loss risk.
4. **Two-strike rule**: If the same subsystem needs two corrective iterations without advancing the user-facing product, stop repairing it and reconsider/replace the approach.
5. **No sunk-cost reasoning**: Existing implementation effort gives an approach zero additional authority.
6. **Every work unit must advance the product**: If it neither runs something real, teaches us something about product quality, nor materially moves toward the TARGET, defer it.
7. **Evidence proportionality**: Do not build more verification machinery than the risk/value of the thing being verified.
8. **Stop on drift**: If you notice work becoming primarily architecture, orchestration, schemas, provenance, wrappers, or test infrastructure instead of the TARGET, explicitly stop and return to the shortest product path.

### 8.2 Operator Challenge Boundary
Whenever an agent proposes an architectural detour or infrastructure expansion, it must submit to the operator challenge:
> **"Does this need to be fixed before we can test the actual product?"**

If the answer is no, the detour is deferred.

### 8.3 Context Hygiene & Residual Information Eradication
- **Conscious Step-by-Step Context Loading**: Bulk-loading massive context at session start degrades reasoning. Load context incrementally as decisions require it.
- **Eradication of Residual Confusing Names**: When a system, component, or file is deleted or renamed, all references to its old name must be thoroughly eradicated from active guidance. Lingering ghost mentions irritate agents and cause them to hallucinate resurrected dead architectures.
- **Anti-Overcorrection**: When receiving a critique or correction, make surgical, localized edits. Never wipe out surrounding valid code or invert the entire system design in response to a narrow critique.

---

## 9. Specialized Candidate Modules Justification

Beyond the Core Triad, domain analysis justifies four specialized modular specifications:

### 9.1 `anti-drift-rules.md` (Anti-Drift & Anti-Overengineering Invariants)
- *Justification*: Mined from severe production drift incidents (e.g. Swarm orchestrator consuming $100 on S0 stage alone reading process docs and re-running gates instead of executing).
- *Contents*: The 8 Anti-Drift Laws, Two-Strike Rule, Sunk-Cost Prohibition, Operator Challenge Rule, and Minimalism Directives.
- *Priority*: P0 / P1.

### 9.2 `patch-discipline.md` (Deterministic Code Mutation & Rollback)
- *Justification*: Prevents the catastrophic failure mode where browser/connector agents regenerate entire 600-line files to change 2 lines, resulting in silent code truncation and loss of parallel edits.
- *Contents*: Verbatim block replacement format (`<file>/<old>/<new>`), AST patch intent schema (`patch-intent-schema.json`), unique context requirements, and automated git rollback.
- *Priority*: P0.

### 9.3 `governance-schemas.md` (Validation Profiles & Tri-Class Conformance)
- *Justification*: Operationalizes the deterministic Python validator (`okf_validator.py`) and standardizes frontmatter schemas across knowledge bundles.
- *Contents*: OKF v0.2 frontmatter schemas, link integrity rules, durable ID uniqueness, and tri-class diagnostics (`OKF_ERROR`, `APEX_PROFILE_ERROR`, `ADVISORY_WARNING`).
- *Priority*: P1 / P2.

### 9.4 `research-discipline.md` (Deep Evidence Research Protocol)
- *Justification*: Directly codifies the mature `C02-conditional-research-discipline/SKILL.md` into the informatics suite.
- *Contents*: The 7-step research loop (Frame, Map, Orientation scan, Verify load-bearing evidence, Iterate leads, Track gaps/conflicts, Stopping criteria) and source triangulation rules.
- *Priority*: P1 (Conditional).

---

## 10. Traceability Matrix & Verification Plan

### 10.1 Requirement Traceability
| Original Requirement | Discovered Feature / Module | Corroborating Corpus Files | Target File in Architecture |
|----------------------|-----------------------------|----------------------------|-----------------------------|
| R1: Significance & Ranking | P0–P3 Tiers, Raw `[P<tier> \| I/E/R]` | `2Do_context_file_authority_reference.md`, `Snippets.md`, `C01/README.md` | All generated modules |
| R1: Top-Loaded Primacy | Attention Primacy (first 500 tokens) | `2Do_context_file_authority_reference.md` CD-01, AP-07 | `index.md`, `standard.md`, all modules |
| R2: Approximate Ceilings | ~100L / ~400T Router, ~150W prose | `02-GLOBAL-SNIPPET-GRAMMAR.md`, `06-RECOMMENDED-AGENT-CONSTITUTION` | `index.md`, `writing-profile.md` |
| R2: Exception Authority | Rule-breaking for technical clarity | `standard.md` §13, `08-TIER-A-PILOT` | `writing-profile.md`, `standard.md` |
| R3: Consolidated Router | Lean XML IF-tags, JIT routing | `08-TIER-A-PILOT` lines 28–97, `C03/README.md` | `index.md` / `general-informatics-router.md` |
| R4: Core Triad - Writing | Information Mapping, STE limits | `standard.md` §5–6, `Snippets.md` line 5 | `writing-profile.md` |
| R4: Core Triad - File Arch | OKF frontmatter, Five-Plane IA | `standard.md` §3–4, 11, `okf_validator.py` | `file-architecture.md` |
| R4: Core Triad - Execution | Q&A, Bake-off, Patch, Handover, MMM | `Snippets.md`, `MMM/working-method.md`, `patch-intent-schema.json` | `execution-modes.md` |
| R5: Empirical Synthesis | 8 Anti-Drift Laws, 2-strike, Minimalism | `2Dos Ai Instructions.md`, `Snippets.md` line 24–61, A01–A13 | `anti-drift-rules.md`, all modules |

### 10.2 Verification Plan
1. **Deterministic OKF Validation**:
   ```powershell
   python apex-meta/scripts/okf_validator.py --target apex-meta/informatics
   ```
   *Acceptance Criteria*: Reports `0 OKF Errors` and `0 APEX_PROFILE Errors`.
2. **Significance Ranking Audit**:
   - Verify every newly authored rule is tagged with `[P<tier> | I<impact>/E<evidence>/R<risk>]`.
   - Verify uncomputed raw estimates (1–100 scale); confirm absence of computed mathematical formulas.
   - Verify P0 invariants are strictly top-loaded in the first 500 tokens of each file.
3. **Router Compactness & Primacy Verification**:
   - Verify consolidated general router adheres approximately to ~100 lines and ~400 tokens.
   - Verify critical routing logic is positioned at the top of the router block.
4. **Context Isolation Simulation**:
   - Simulate an agent executing a pure prose editing task: verify it accesses only `writing-profile.md` without loading `file-architecture.md` or `execution-modes.md`.
5. **Traceability Audit**:
   - Verify all 8 Anti-Drift Laws, Two-Strike Rule, and 5 Execution Adapters are formally codified.
