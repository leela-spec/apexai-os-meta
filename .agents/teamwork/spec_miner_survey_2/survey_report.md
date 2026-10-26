# Survey Report 2: Operational Lore, Anti-Drift Laws & Empirical Primacy Authority

**Author**: Specification Miner (Survey 2 Subagent)  
**Date**: 2026-10-19  
**Scope**: Comprehensive forensic investigation and feature discovery across repository operational lore, behavioral snippets, empirical failure postmortems, and context file authority references.  
**Authoritative Sources Probed**:
1. `c:\GitDev\apexai-os-meta\apex-meta\AI-Snippets\Snippets.md`
2. `c:\GitDev\apexai-os-meta\apex-meta\AI-Snippets\Orga\2Dos Ai Instructions.md` & `2Dos.md`
3. `c:\GitDev\apexai-os-meta\apex-meta\kb\old-apex-full-orchestration-agent-kb\sources/primary/managed-agent-kb/special_ops__ai_handling_routing/2Do_context_file_authority_reference.md`
4. `c:\GitDev\apexai-os-meta\apex-meta\AI-Snippets\SnippetDocs\AnitOverEng.md`
5. `c:\GitDev\apexai-os-meta\apex-meta\AI-Snippets\AIFailure\` (Empirical failure logs: ASTRA destructive rewriting, RAG metadata over-engineering, Claude Code redundant verification, Claude Plan context hallucinations, OpenProject environment transport blind spots).

---

## Executive Summary

This survey establishes the complete catalog of operational rules, anti-drift laws, minimalism mandates, context hygiene protocols, operational execution snippets, and exception authorities required to formalize the next-generation Apex Informatics Architecture.

Historically, autonomous agents in the Apex ecosystem have suffered from two mirror-image failure modes:
1. **Process-Ceremony Drift & Paperwork Overreach**: An agent spends its entire budget on reading process docs, diagnosing pre-existing test baselines, and over-verifying without writing product code, ultimately writing a handover to defer action instead of invoking available tools (exemplified by the $100 S0 sequencing swarm failure in `2Dos Ai Instructions.md`).
2. **Destructive Regeneration & Over-Scaffolding**: An agent tasked with a surgical change or system separation treats existing assets as material to regenerate, introduces elaborate schemas, or runs automated transforms that strip comments, mutilate formatting, and delete critical business engines (exemplified by the ASTRA separation failure in `AIFailure/Insane GPT ASTRA Failure...`).

To eliminate both failure modes permanently, the new informatics suite must codify:
- **Primacy-loaded, single-action imperative directives** tagged inline with P0–P3 tiers and raw 3-metric qualitative/quantitative estimates `[P<tier> | I<impact>/E<evidence>/R<risk>]`.
- **Anti-Drift Laws** where `TARGET` strictly dominates all infrastructure, ceremony, and orchestration.
- **Minimalism & Anti-Overcorrection Disciplines** enforcing Gall's Law, Minto BLUF, and single flat-file Minimal Viable Artifacts (MVA).
- **Rigid Context Hygiene** enforcing step-by-step conscious context loading, strict current-truth separation, and the complete eradication of residual stale names.
- **Deterministic Operational Snippets** for Q&A decision matrices, exact-match block patches, Macro-Meso-Micro (MMM) decomposition, and lean execution.
- **Explicit Substance-Over-Ceremony Exception Authority**, freeing agents from mechanical metric compliance whenever technical accuracy and target delivery demand it.

---

## Features Discovered

| # | Category | Feature | Description | Inputs | Outputs | Error Behavior | Discovered Via |
|---|----------|---------|-------------|--------|---------|----------------|----------------|
| 1 | Anti-Drift | TARGET Dominance Invariant | TARGET dominates everything; optimize for shortest credible path to user-facing outcome. Adjacent work is additive, never silent substitute. | User goal / prompt task | Direct user-facing deliverable | Halts work if becoming primarily architecture/orchestration without advancing TARGET. | `Snippets.md:28`, `2Dos Ai Instructions.md:188` |
| 2 | Anti-Drift | Two-Strike Subsystem Rule | If the same subsystem requires two corrective iterations without advancing the user-facing product, stop repairing and reconsider/replace the approach. | 2 successive failed fix attempts on same component | Reconsidered or alternative approach | Disallows third repair loop; forces pivot or escalation. | `Snippets.md:34`, `2Do_context_file_authority_reference.md:243` |
| 3 | Anti-Drift | No Sunk-Cost Reasoning | Prior implementation effort or investment gives an approach zero additional authority or preservation preference. | Code candidate evaluation | Objective technical assessment | Prevents defending broken architectures due to prior work. | `Snippets.md:36` |
| 4 | Anti-Drift | Product Before Infrastructure | Before the first real working vertical slice, fix only issues that block execution, corrupt product, invalidate experiments, or risk data loss. | Proposed infrastructure / cleanup tasks | Filtered task queue (vertical slice only) | Defers secondary infrastructure until product functions. | `Snippets.md:32` |
| 5 | Anti-Drift | Evidence Proportionality | Do not construct more verification machinery, gates, or test frameworks than the risk/value of the item being verified. | Verification scope proposal | Lean test / verification plan | Flags over-verification; bans standalone re-runs when `--since` suffices. | `Snippets.md:40`, `CC_insanedrift...:17` |
| 6 | Anti-Drift | Stop on Drift | If work becomes primarily architecture, orchestration, schemas, provenance, wrappers, or test harness instead of TARGET, explicitly stop and return to product path. | Continuous execution self-check | Course correction to product deliverable | Immediate execution halt on drift detection. | `Snippets.md:42`, `2Dos.md:104` |
| 7 | Anti-Drift | Operator Pre-Test Question | When an operator or agent proposes a correction, ask: "Does this need to be fixed before we can test the actual product?" | Proposed fix / refactoring | Filtered necessity check | Drops fixes that do not block immediate testing. | `Snippets.md:47` |
| 8 | Anti-Drift | Checkable Ambiguity Resolution | Ambiguous but objectively checkable questions must be verified immediately with available tools; deferring to next session is forbidden. | Unclear fact or state | Immediate tool invocation & verified fact | Disallows writing a handover when tools can resolve it. | `2Dos Ai Instructions.md:199, 415` |
| 9 | Anti-Drift | Grounding vs. Citation | Opening an artifact originating a fact is required; citations of secondary summaries or self-referential notes do not constitute grounding. | Factual assertion / file path | Direct primary inspection (`path:line`) | Rejects claims based solely on secondary audits or memory. | `2Dos Ai Instructions.md:172`, `CLAUDE.md:174` |
| 10 | Anti-Drift | Command-Carrying Claims | Statements of zero, absence, or counts must include the exact command and scope that produced them. | Metric or count claim | Reproducible command + result | Invalidates unsupported claims like "zero readers" or "100% passes". | `2Dos Ai Instructions.md:181`, `ClaudePlanContextFuckup.md:34` |
| 11 | Anti-Drift | Pre-existing Red vs. Regression | A gate or test failure is a halt condition only if green on unmodified master HEAD and turned red by current edit; pre-existing redness is recorded, not halted on. | Test / gate run result | Categorized status (pre-existing vs regression) | Prevents whole-run halt on out-of-scope failures. | `2Dos Ai Instructions.md:300, 426` |
| 12 | Anti-Drift | Run Outcome Objective Banner | Pipeline close stage must inspect `git log` directly to classify outcome as `product-shipped`, `governance-only`, or `halted-preproduct`. | Git commit log of writable globs | Verified banner header | Overrides subjective self-congratulatory agent summaries. | `2Dos Ai Instructions.md:489` |
| 13 | Anti-Drift | Tool-First Imperative Rungs | Decision ladders and escalation gates must be worded as active imperative tool invocations ("invoke 3 parallel agents now"), never passive conditions. | Decision condition reached | Immediate tool call | Eliminates passive deferral / paperwork generation. | `2Dos Ai Instructions.md:415, 423` |
| 14 | Anti-Drift | No Exclusion Without Inventory | Quarantine, deferral, or "out of scope" rulings must enumerate every item individually and mark each kept or excluded; container banning is forbidden. | Set of items / files | Itemized disposition table | Rejects bulk hand-waving exclusions. | `2Dos Ai Instructions.md:179` |
| 15 | Minimalism | Task Minimalism Rule | Do only what is necessary to satisfy the explicit task. No precautionary defensive guardrails for hypothetical risks. | Explicit task prompt | Minimal sufficient deliverable | Drops unrequested scaffolding, roadmaps, or edge-case handling. | `Snippets.md:56`, `AnitOverEng.md:47` |
| 16 | Minimalism | Gall's Law Constraint | Complex systems evolve from working simple systems. Default to a single flat file; never create directories/modules until volume demands it. | Deliverable scope | Single flat file / minimal artifact | Flags premature directory nesting as system defect. | `AnitOverEng.md:7, 49` |
| 17 | Minimalism | Minto BLUF | Bottom Line Up Front: lead with the definitive conclusion or deliverable in sentence one; eliminate introductory wind-up. | Analysis / response | Sentence-1 bottom line + compact table | Prevents theoretical preamble and generic frameworks. | `AnitOverEng.md:9, 47` |
| 18 | Minimalism | Zero-Speculation Scope Ceiling | Anything not explicitly requested is out of scope by default. Exploration budget is strictly bounded. | Task boundaries | Delimited execution output | Rejects unprompted future phases, glossaries, or frameworks. | `AnitOverEng.md:13, 48` |
| 19 | Minimalism | Stop-and-Check Invariant | If an ambiguous task can be solved in 1 step or 5 steps, execute the 1-step solution. Propose larger architectures only as optional next step. | Multi-tier solution choices | Simplest viable execution | Avoids unrequested architectural over-engineering. | `AnitOverEng.md:52` |
| 20 | Minimalism | Deletion Test for Directives | Every new rule must be tested for impact: remove any directive that changes behavior in fewer than 10% of realistic cases. | Candidate directive set | Pruned directive set (<= ceiling) | Purges low-value rules accumulated from past incidents. | `2Do_context_file_authority_reference.md:194` |
| 21 | Anti-Overcorrection | Surgical Edits Invariant | Edits must be surgical block replacements; prevent wholesale file regenerations, rewriting valid text, or accidental loss of material info. | Target file & requested delta | Exact `<old>` / `<new>` replacement block | Rejects destructive regenerations and AST decompilers. | `Snippets.md:154`, `2Dos Ai Instructions.md:13, 44`, `AIFailure/ASTRA:84` |
| 22 | Anti-Overcorrection | Assets to Preserve, Not Regenerate | Treat existing files, comments, and scripts as assets to preserve, not material to regenerate or strip down. | Existing codebase assets | Preserved source with minimal delta | Forbids stripping comments, reducing scripts, or re-formatting. | `AIFailure/ASTRA:78, 88` |
| 23 | Anti-Overcorrection | Stale Residual Eradication | Purge all residual traces of deleted concepts or old names from documents; mentioning deleted names causes later agents to re-consider them. | Edited documentation | Clean current-truth text without stale ghost names | Eradicates confusion-inducing residual identifiers. | `2Dos Ai Instructions.md:19, 45` |
| 24 | Context Hygiene | Conscious Step-by-Step Context Loading | Do not front-load large context bundles; load context step-by-step just-in-time (JIT) based on the immediate execution step. | Task execution phase | Minimal relevant context chunk | Prevents context window saturation and attention dilution. | `2Dos Ai Instructions.md:11`, `Snippets.md:5` |
| 25 | Context Hygiene | Strict Current-Truth Separation | Maintain only active system state in live documents; changelogs, superseded proposals, and historic narratives belong in dedicated history planes. | System state documentation | Single current-truth specification | Forbids inline changelogs or historic rationale in specs. | `Snippets.md:5`, `AGENTS.md` |
| 26 | Context Hygiene | File Type Taxonomy Separation | Separate system_prompt, knowledge_base, workflow, and tool_definition into distinct single-responsibility files; never combine them. | System documentation corpus | Modular typed files | Eliminates context clashing and instruction-count inflation. | `2Do_context_file_authority_reference.md:61, 74` |
| 27 | Context Hygiene | Externalize & Re-ground | Externalize state to authoritative files (`STATUS.md` for execution, `STATE.md` for history); re-ground from owning file, not memory. | Session progress / outcome | State file updates | Prevents memory drift across long multi-turn sessions. | `2Dos Ai Instructions.md:183` |
| 28 | Context Hygiene | Entry Surface Budget Cap | Enforce strict byte/token ceilings on auto-loaded entry files (`CLAUDE.md`, `AGENTS.md`, router); prevent silent budget inflation. | Entry instruction surface | Bounded prompt (< 26kB / ~400 tokens) | Triggers CI / gate failure on unauthorized expansion. | `2Dos Ai Instructions.md:448` |
| 29 | Context Hygiene | Frontmatter Minimalism | Restrict frontmatter metadata to 3–4 natural fields (`title`, `summary`, `tags`, optional `source`); avoid relational DB schema sprawl. | Document metadata | Concise YAML frontmatter | Prevents over-filtering blindspots and vector dilution. | `AIFailure/AI-Failure-RAG...:36` |
| 30 | Directive Design | Top-Loaded Primacy (First 500 Tokens) | Place all non-negotiable critical invariants within the first 500 tokens of instruction files to counter positional attention decay. | Instruction file content | Top-loaded directive block | Prevents 30–50% compliance drop from mid-doc burial. | `2Do_context_file_authority_reference.md:31, 370` |
| 31 | Directive Design | Model-Specific Directive Ceilings | Cap imperative directives per model capacity (50 for GPT-4o / Claude Standard, 80 for Claude Reasoning, 100 for Gemini / o3). | Active model runtime | Calibrated directive count | Prevents rule omission cliff onset from overload. | `2Do_context_file_authority_reference.md:9, 357` |
| 32 | Directive Design | Single Action Per Directive | Encode exactly one imperative action per directive; compound sentences with multiple actions lead to partial compliance. | Directive draft | Atomic single-action rules | Splitting compound rules prevents partial execution bugs. | `2Do_context_file_authority_reference.md:157` |
| 33 | Directive Design | Imperative Verbs, Zero Modal Hedging | Start every rule with an imperative verb (do, validate, halt); strictly ban modal hedging (should, may, might, could). | Directive phrasing | Unambiguous imperative syntax | Prevents models treating mandatory rules as optional. | `2Do_context_file_authority_reference.md:56, 148, 298` |
| 34 | Directive Design | Inline Priority Tagging | Attach priority tier and 3-metric estimates inline at point of declaration: `[P<tier> | I<impact>/E<evidence>/R<risk>]`. | Rule declaration | Tagged directive syntax | Prevents compliance collapsing below 31% (GPT) / 58% (Claude). | `2Do_context_file_authority_reference.md:49, 166`, `ORIGINAL_REQUEST.md:30` |
| 35 | Directive Design | Example Frugality (<= 2) | Include examples only for genuinely ambiguous directives; restrict to maximum 2 (one correct, one incorrect); zero for clear rules. | Ambiguous rule definition | Minimal paired examples | Prevents example proliferation from degrading task focus. | `2Do_context_file_authority_reference.md:174, 378` |
| 36 | Directive Design | Concrete Stop & Escalate Conditions | Workflows and prompts must contain explicit halt/escalate criteria with structured error codes; no open-ended grace loops. | Ambiguous/failed state | Structured error code & execution halt | Halts execution immediately; stops fabrication loops. | `2Do_context_file_authority_reference.md:183, 304` |
| 37 | Directive Design | Anti-Self-Verification Trap | Prohibit verification scripts and protocols from defining their own success metrics detached from the actual user target. | Verification test suite | Independent grounding verification | Rejects circular self-validating scripts. | `2Dos Ai Instructions.md:17, 60` |
| 38 | Operational Snippet | Q&A & OKF Decision Matrix | Standard format for high-impact decisions: Question, Options (letter, mechanism, grounding, `(I/E/R)`), Recommendation, Reasoning, Notes. | Decision dilemma | Structured decision record | Prevents speculative debates; produces actionable choices. | `Snippets.md:11`, `ORIGINAL_REQUEST.md:52` |
| 39 | Operational Snippet | Formula REI Expected Value | Expected Value formula: `EV = Impact * Evidence * (1 - 0.5 * Risk)`. Syntax: `(I90/E95/R20: 77)`. Tagging uses raw metrics. | Qualitative/quantitative scores | Calibrated 1-100 metric orientation | Eliminates arbitrary 4-digit rankings; clarifies trade-offs. | `Snippets.md:78` |
| 40 | Operational Snippet | Exact-Match Block Patch Discipline | Surgical editing via exact-match substring replacement (`<file>`, `<old>`, `<new>`); copy verbatim, preserve whitespace, one change per block. | Live file & edit intent | Exact patch block | Rejects patch on mismatch; prevents partial overwrites. | `Snippets.md:154`, `ORIGINAL_REQUEST.md:54` |
| 41 | Operational Snippet | Macro-Meso-Micro (MMM) Decomposition | Structured three-layer architecture: Macro (Why? Strategy/Vision), Meso (How? Architecture/Interfaces), Micro (What? Code/Steps/Tests). | Complex project / topic | 3-layer progressive decomposition | Prevents mixing operational details into strategic specs. | `Snippets.md:85`, `2Dos Ai Instructions.md:49` |
| 42 | Operational Snippet | 4-Phase Analytical Evaluation Rubric | Exhaustive option evaluation: Phase 1 (Gating Hard Filters), Phase 2 (CoT Matrix), Phase 3 (Ranked Verdicts), Phase 4 (Prototypes & Triggers). | Solution candidate pool | Ranked matrix & decision boundaries | Ensures objective, reproducible technology evaluations. | `Snippets.md:107` |
| 43 | Operational Snippet | Adaptive Informatics Contract | Gating contract: apply formal YAML, STE prose, and info mapping for technical docs; use natural conversational tone for casual chat. | User prompt intent | Mode-switched response | Bypasses unnecessary serialization during quick chats. | `Snippets.md:4` |
| 44 | Operational Snippet | Lean Execution Contract | Anti-ceremony execution: batch docs, verify once per unit (`--since`), drop flaky paths after 2 tries, inline over subagents for <= 5 files. | Multi-step code/recon work | Lean execution trail | Eliminates repetitive gate runs and redundant subagents. | `2Dos Ai Instructions.md:225, 401`, `CC_insanedrift...:25` |
| 45 | Operational Snippet | Handover Definition Standard | Standard handover structure: intent/outcome focus, input/process/output definition with predefined examples, Definition of Done. | Multi-turn task handoff | Self-contained handover dossier | Prevents lost context and downstream task distortion. | `2Dos Ai Instructions.md:10`, `ORIGINAL_REQUEST.md:55` |
| 46 | Operational Snippet | Git Synchronization Protocol | Synchronize via clean pull & push, no deletions without explicit instruction, preserve un-tracked files, separate commits for present files. | Working tree git state | Atomic, clean git commits | Eliminates destructive worktree/stash accidents. | `2Dos Ai Instructions.md:3`, `Snippets.md:200` |
| 47 | Exception Authority | Substance Over Ceremony Invariant | Explicit rule-breaking authority: ceilings, word counts, and formatting rules may be relaxed whenever strict adherence harms accuracy or omits load-bearing context. | Technical conflict with formatting rule | Accurately completed deliverable | Overrides mechanical rule enforcement in favor of truth. | `ORIGINAL_REQUEST.md:39`, `2Dos Ai Instructions:81` |
| 48 | Exception Authority | Pre-Addition Check Rule | Before adding a new check, script, or gate: confirm ordinary use doesn't surface the problem in ~2 steps; fix data/logic instead of adding machinery. | Proposal for new verification gate | Rejection or streamlined logic fix | Halts proliferation of bureaucratic gatekeeping scripts. | `2Dos Ai Instructions.md:134, 204` |

---

## Edge Cases

| # | Feature | Input | Observed Behavior |
|---|---------|-------|-------------------|
| 1 | Exact-Match Patch Replacement | Source file indentation uses hard tabs, but patch generator copied spaces or paraphrased leading indentation. | Executor rejects entire edit block with match error; live file remains unmodified, preventing corruption. |
| 2 | Exact-Match Patch Replacement | Ambiguous `<old>` block matches 3 identical lines in different functions. | Edit fails because match is non-unique; executor enforces 1–2 surrounding disambiguating context lines. |
| 3 | S0 Baseline Test Verification | Full test suite has 4 pre-existing failures on master completely outside the task's writable scope. | Agent correctly records failures with exact reproduction command and continues task; does NOT trigger a whole-run HALT. |
| 4 | Two-Strike Subsystem Rule | Subsystem fails unit test on attempt 1; agent adjusts parameters; attempt 2 fails identically. | Agent stops repairing the subsystem; immediately switches to alternative strategy or escalates to human operator. |
| 5 | Deletion Test for Directives | A proposed rule ("Do not use Comic Sans font") has zero production incidents across 190 rows of history. | Rule fails the deletion test (<10% behavioral impact) and is omitted from the instruction set. |
| 6 | Model Directive Ceilings | Context author attempts to add 12 new rules to GPT-4o system prompt, bringing total to 62 directives. | Breaches 50-directive ceiling; file validator rejects file until 12 lowest-impact rules are pruned or moved to knowledge base. |
| 7 | Stale Residual Eradication | A retired service ("Nowa" or "SQLite-branch") is mentioned in a note warning "do not use Nowa". | Subagent misinterprets warning as an active component and generates a migration adapter for Nowa; rule mandates complete erasure of stale names. |
| 8 | Whole-File Rewrite Hallucination | Agent operating in chat interface needs to update a 5-line port mapping in a 400-line compose file. | Hallucinated surgical ability causes agent to output entire 400-line file with 30 unrelated lines dropped; exact patch discipline enforces single `<old>/<new>` block. |
| 9 | Substance Over Ceremony | Complex architectural spec requires a 220-word technical explanation before a table, exceeding the ~150-word prose block guideline. | Author exercises Substance Over Ceremony authority; preserves technical nuance without forced, unnatural splitting. |
| 10 | Grounding vs. Citation | Agent claims "Docker daemon is configured for rootless mode", citing an old audit report from 3 weeks prior. | Rule invalidates claim; forces agent to execute `docker info` directly to establish live grounding. |
| 11 | Command-Carrying Absence Claim | Agent asserts "no references exist for function `compute_hash`". | Assertion rejected unless accompanied by verbatim command: `grep_search(Query='compute_hash', SearchPath='c:\...')` returning 0 results. |
| 12 | Subagent Delegation Threshold | Simple refactoring touches only 2 files with straightforward replacements. | Spawning subagents is forbidden (delegation overhead costs 130k tokens for 0 benefit); agent executes edits inline. |
| 13 | Read-Only Exploration Over-Verification | Agent performing recon/discovery runs full CI gate suite 4 consecutive times. | Lean execution contract catches redundant execution; enforces single `--since` run and bans repetitive test executions. |
| 14 | AST Decompilation vs Preservation | Agent runs Python `ast.unparse()` on business logic to modify a port number. | Code decompiler wipes all inline comments and squashes formatting; surgical patch rule forbids AST regenerating. |
| 15 | RAG Frontmatter Metadata Sprawl | Knowledge file has 12 nested metadata attributes (`persona`, `tone`, `target_stage`). | Query with natural language synonym fails to match strict attribute; frontmatter minimalism restricts fields to 3–4 natural keys. |

---

## Deep Domain Analysis & Catalog

### 1. Anti-Drift Laws & Primacy of TARGET

The repo's empirical history proves that capable AI agents default to **process-ceremony drift**: substituting the production of governance documents, decision sheets, and test runs for shipping actual product deliverables.

#### The 8 Fundamental Anti-Drift Laws
1. **TARGET Dominates Everything**: The primary objective is the shortest credible path to the user-facing deliverable. Secondary tasks (orchestration, refactoring, meta-documentation) are additive and must never supplant the core output.
2. **Reuse Before Build**: Never construct a new abstraction, tool, or schema until existing components have been exercised and proven insufficient.
3. **Product Before Infrastructure**: Until a working vertical slice exists, fix only issues that directly block runtime execution, corrupt data, or invalidate testing.
4. **The Two-Strike Rule**: If a component or subsystem requires two corrective fix attempts without delivering product progress, stop repairing it. Discard the approach and pivot.
5. **No Sunk-Cost Reasoning**: Time or tokens already invested grant an approach zero additional authority. Be ruthless in abandoning failing branches.
6. **Every Work Unit Advances the Product**: Every action must either execute real code, reveal a definitive product quality insight, or directly advance toward the TARGET. Otherwise, defer it.
7. **Evidence Proportionality**: Never build heavier verification machinery than the risk and value of the target code justify.
8. **Stop on Drift**: If work begins to skew toward schemas, wrappers, audit files, or orchestration instead of the target outcome, immediately halt and reset to the shortest product path.

#### Forensic Operational Invariants
- **Checkable Ambiguity Resolution**: A checkable fact or question must be verified immediately with available tools. Writing a handover to ask the "next session" to check a fact is a recognized system failure (`SEQ-AUTO-2026-09-17-S0`).
- **Grounding Over Citation**: Opening the originating artifact is mandatory (`path:line`). Citations of secondary audits or self-referential summaries are prohibited.
- **Absence Claims Carry Commands**: Any negative claim ("no files found", "zero errors") must state the exact command and scope executed.
- **Run Outcome Classification**: Pipelines must objectively inspect `git log` to categorize runs as `product-shipped`, `governance-only`, or `halted-preproduct`.

---

### 2. Minimalism & Anti-Overcorrection Disciplines

Over-engineering in AI agents stems from **elaborative bias** and **taxonomic drift**—treating "thoroughness" as the multiplication of directories, schemas, and defensive procedures.

#### Core Minimalist Principles
- **Gall's Law**: All functioning complex systems evolved from functioning simple systems. Never create directory structures, modular wrappers, or complex scaffolding before the core asset functions in a single flat file.
- **The Minto Pyramid & BLUF**: Always deliver the bottom line up front in sentence one. Background and explanations exist solely to support the conclusion.
- **Minimal Viable Artifact (MVA)**: Deliver the smallest atomic unit that fulfills the requirement. Multiple files where one suffices is an operational failure.
- **Out-of-Scope Fencing**: Anything not explicitly requested is out of scope by default. Speculative expansion (roadmaps, future phases, generic error frameworks) is strictly banned.
- **Stop-and-Check Invariant**: When choosing between a 1-step and 5-step implementation, execute the 1-step solution.

#### Anti-Overcorrection Disciplines
- **Preserve, Do Not Regenerate**: Existing codebases and documentation are assets to be preserved. Automated scripts must never decompile, strip comments, or regenerate working assets.
- **Surgical Edits Only**: Edits must be exact-match string replacements targeting isolated chunks.
- **Purge Stale Residual Names**: Retaining deleted names, legacy branches, or deprecated tools in warning blocks causes downstream agents to resurrect them. Stale identifiers must be eradicated completely.
- **Directive Deletion Test**: Any rule that alters model behavior in fewer than 10% of realistic cases must be pruned.

---

### 3. Context Hygiene & Structural Authority

Context window saturation and mixed-type monoliths lead to exponential decay in rule compliance.

#### Context Management Invariants
- **Conscious Step-by-Step Loading**: Front-loading massive context windows degrades attention. Context must be retrieved just-in-time (JIT) via tool calls at the moment of execution.
- **Strict Current-Truth Separation**: Live documentation must reflect only active system truth. Historic retrospectives, superseded plans, and changelogs belong on dedicated history planes, never inline.
- **File Type Taxonomy**: File content must strictly adhere to single-purpose schemas:
  - `system_prompt`: Roles and constraints (ceiling: 2000 tokens).
  - `knowledge_base`: Domain facts and references (0 directives, load JIT).
  - `workflow`: Execution steps and branching logic (limit: 15 directives, 4000 tokens).
  - `tool_definition`: Tool parameters and schemas (limit: 5 directives, 1000 tokens).
- **Entry Surface Budgeting**: All entry files (`CLAUDE.md`, `AGENTS.md`, router) must be strictly bounded (< 26kB / ~400 tokens) to guarantee that essential instructions fit within the high-attention zone.

#### Top-Loaded Primacy Architecture
- **First 500 Tokens Rule**: Critical non-negotiable directives must reside within the first 500 tokens of the document. Compliance drops by 30–50% when rules are placed past token 500.
- **Imperative Verb Discipline**: Every directive begins with an imperative verb (e.g., `Verify`, `Halt`, `Enforce`). Modal hedging (`should`, `may`, `could`, `might`) is banned.
- **Inline Priority & 3-Metric Syntax**: Rules must carry inline tier tags and qualitative 1–100 estimates: `[P<tier> | I<impact>/E<evidence>/R<risk>]`.

---

### 4. Operational Execution Snippets & Protocols

#### A. Q&A Decision Matrix & OKF Standard
Used for architectural decisions and resolving trade-offs:
```markdown
- *Question:* [Exact problem/decision being resolved]
- *Options:* 
  - Option A: [Mechanism (2–4 lines), Grounding, Real-life example] `(I<1-100>/E<1-100>/R<1-100>)`
  - Option B: [Mechanism (2–4 lines), Grounding, Real-life example] `(I<1-100>/E<1-100>/R<1-100>)`
- *Recommendation:* [Selected Option Letter]
- *Reasoning:* [Dense justification for the choice]
- *Notes:* [One-line rejection reason per rejected option]
```
*Dimensions*:
- **Impact (I)**: Value, effectiveness, target orientation.
- **Evidence (E)**: Grounding, empirical support, battle-proven track record.
- **Risk (R)**: Misjudgment potential, operational complexity, downside aftermath.

#### B. Exact-Match Block Replacement (Patch Discipline)
Used for safe, deterministic code modifications:
```xml
<file>ABSOLUTE/PATH/TO/FILE</file>
<old>
exact original lines, copied verbatim
</old>
<new>
replacement lines
</new>
```
*Rules*:
1. One change per block.
2. Copy verbatim; do not retype or paraphrase whitespace.
3. No line numbers or block IDs.
4. Include 1–2 surrounding lines if needed to guarantee unique matching.
5. If unable to produce an exact match, state so explicitly.
6. Never assume an edit was applied until confirmed by the executor.

#### C. Macro-Meso-Micro (MMM) Decomposition
Used for structured analysis and complex knowledge extraction:
| Layer | Question | Focus | Contents |
|---|---|---|---|
| **Macro** | Why? | Strategic / System | Purpose, target value, system vision, external boundaries, success criteria |
| **Meso** | How? | Tactical / Architecture | Modules, interfaces, dependencies, sequencing, coordination constraints |
| **Micro** | What exactly? | Operational / Implementation | Concrete specifications, code, exact steps, test assertions, DoD |

#### D. Lean Execution Contract
For multi-step code and verification tasks:
- Run gates once per coherent unit (`python scripts/gates.py --since origin/master`).
- Do not run standalone test suites prior to running gates that already run those tests.
- Timebox troubleshooting: abandon flaky tool paths after 2 attempts.
- Execute trivial edits (<= 5 files) inline; do not spawn subagents.
- Batch documentation updates before regenerating SSOT status views.

---

### 5. Rule-Breaking & Exception Authority (Substance Over Ceremony)

Mechanical compliance with formatting guidelines or metric ceilings must never supersede engineering reality.

#### Explicit Exception Authority Mandate
1. **Substance Over Ceremony Invariant**: An agent or author is explicitly authorized to exceed approximate token ceilings, word counts, or structural constraints whenever strict adherence would compromise technical precision, omit load-bearing architectural details, create artificial distortions, or produce unreadable prose.
2. **Ceilings as Orientations**: Metric targets (e.g., ~100 lines for the general router, ~150 words per prose block, ~20 words per procedural sentence) are pragmatic operational targets, not fragile barricades.
3. **The Pre-Addition Check**: Before adding a new verification check, script, or gate, confirm that ordinary usage does not already catch the defect within 1–2 steps. If it does, correct the underlying logic instead of adding governance scaffolding.

---

## Traceability Matrix: Rules to Informatics Modules

This matrix maps every operational rule and snippet to its target codification module in the next-generation informatics architecture:
- **`router`**: `apex-meta/informatics/general-informatics-router.md` (or `index.md`)
- **`writing`**: `apex-meta/informatics/writing-profile.md`
- **`file-arch`**: `apex-meta/informatics/file-architecture.md`
- **`exec-modes`**: `apex-meta/informatics/execution-modes.md`
- **`gov-schemas`**: `apex-meta/informatics/governance-schemas.md` / `validation-profiles.md`

| Rule / Snippet ID | Source Location | Summary & Core Directive | Priority Tier | Raw Metrics (I/E/R) | Target Informatics Module | Target Section / Tag |
|---|---|---|---|---|---|---|
| AD-01 | `Snippets.md:28` | TARGET Dominates Everything | P0 | I98/E99/R05 | `router` & `exec-modes` | `<informatics when="execution">` / Anti-Drift Core |
| AD-02 | `Snippets.md:34` | Two-Strike Subsystem Rule | P1 | I90/E92/R15 | `exec-modes` | Iterative Execution / Failure Handling |
| AD-03 | `Snippets.md:36` | No Sunk-Cost Reasoning | P1 | I88/E90/R12 | `exec-modes` | Decision-Making Invariants |
| AD-04 | `Snippets.md:32` | Product Before Infrastructure | P0 | I95/E96/R08 | `exec-modes` | Task Prioritization / Vertical Slice |
| AD-05 | `Snippets.md:40` | Evidence Proportionality | P1 | I85/E90/R15 | `exec-modes` | Lean Verification Rules |
| AD-06 | `Snippets.md:42` | Stop on Drift | P0 | I96/E98/R05 | `router` & `exec-modes` | Invariant Guardrails / Drift Detection |
| AD-07 | `Snippets.md:47` | Operator Pre-Test Question | P2 | I80/E85/R10 | `exec-modes` | Interactive Feedback Gating |
| AD-08 | `2Dos:199, 415` | Checkable Ambiguity Resolved JIT | P0 | I95/E95/R10 | `router` & `exec-modes` | Ambiguity Handling & Anti-Deferral |
| AD-09 | `2Dos:172` | Grounding vs Citation Invariant | P0 | I96/E98/R05 | `router` & `writing` | Citation & Grounding Discipline |
| AD-10 | `2Dos:181` | Command-Carrying Claims | P1 | I90/E92/R10 | `writing` & `exec-modes` | Factual Assertions & Evidence Output |
| AD-11 | `2Dos:300` | Pre-existing Red vs Regression | P1 | I92/E95/R12 | `exec-modes` | Baseline Gates & Halt Criteria |
| AD-12 | `2Dos:489` | Objective Git Outcome Banner | P2 | I82/E88/R08 | `exec-modes` | Closeout / Run Outcome Banner |
| AD-13 | `2Dos:423` | Imperative Tool Invocations | P1 | I90/E94/R10 | `writing` & `exec-modes` | Escalation Ladders & Tool Contracts |
| AD-14 | `2Dos:179` | No Exclusion Without Inventory | P1 | I88/E90/R10 | `writing` | Scoping & Quarantine Rules |
| MN-01 | `Snippets.md:56` | Task Minimalism Invariant | P0 | I95/E95/R05 | `router` & `writing` | Minimalism & Scope Fencing |
| MN-02 | `AnitOverEng:7` | Gall's Law Scaffolding Ceiling | P1 | I90/E92/R10 | `file-arch` | Architecture Evolution & Flat Files |
| MN-03 | `AnitOverEng:9` | Minto BLUF | P1 | I90/E95/R05 | `writing` | Information Mapping / Sentence 1 |
| MN-04 | `AnitOverEng:13` | Zero-Speculation Scope Ceiling | P0 | I95/E96/R05 | `router` & `exec-modes` | Scope Boundaries / Out-of-Scope Default |
| MN-05 | `AnitOverEng:52` | Stop-and-Check Invariant (1 vs 5) | P1 | I88/E90/R10 | `exec-modes` | Complexity Minimization |
| MN-06 | `2Do_ref:194` | Deletion Test for Directives | P2 | I85/E90/R10 | `gov-schemas` | Directive Lifecycle & Maintenance |
| OC-01 | `Snippets:154` | Exact-Match Patch Discipline | P0 | I96/E98/R05 | `exec-modes` | File Mutation / Patch Intent Schema |
| OC-02 | `ASTRA:78` | Assets to Preserve, Not Regenerate | P0 | I98/E99/R02 | `exec-modes` | Safe File Handling / Anti-Regeneration |
| OC-03 | `2Dos:19, 45` | Stale Residual Eradication | P1 | I90/E92/R08 | `file-arch` & `writing` | Naming Conventions & Stale Name Purge |
| CH-01 | `2Dos:11` | Step-by-Step Context Loading | P0 | I96/E98/R05 | `router` | Context Routing / JIT Loading |
| CH-02 | `Snippets:5` | Strict Current-Truth Separation | P0 | I95/E96/R05 | `file-arch` | Five Planes & Current-Truth Boundary |
| CH-03 | `2Do_ref:61` | File Type Taxonomy Separation | P1 | I92/E94/R08 | `file-arch` | Single-Type File Taxonomy |
| CH-04 | `2Dos:183` | Externalize and Re-ground | P1 | I90/E92/R08 | `exec-modes` | State Management (`STATUS.md`/`STATE.md`) |
| CH-05 | `2Dos:448` | Entry Surface Budget Enforcement | P1 | I92/E94/R10 | `router` & `gov-schemas` | Token Ceilings & Entry Surface Gate |
| CH-06 | `AIF-RAG:36` | Frontmatter Minimalism (3–4 fields)| P2 | I84/E90/R10 | `file-arch` | OKF v0.2 Frontmatter Specification |
| DD-01 | `2Do_ref:31` | Top-Loaded Primacy (< 500 tokens) | P0 | I96/E98/R05 | `writing` & `file-arch` | Positional Attention & Layout |
| DD-02 | `2Do_ref:9` | Model Directive Ceilings | P1 | I90/E94/R10 | `router` & `gov-schemas` | Model Capacity Calibration |
| DD-03 | `2Do_ref:157` | Single Action Per Directive | P1 | I88/E92/R08 | `writing` | STE Prose & Directive Authoring |
| DD-04 | `2Do_ref:56` | Imperative Verbs, Ban Modals | P0 | I94/E96/R05 | `writing` | STE Grammar / Modal Prohibition |
| DD-05 | `2Do_ref:49` | Inline Priority & 3-Metric Syntax | P1 | I92/E95/R08 | `router` & `writing` | Significance & Ranking Annotation |
| DD-06 | `2Do_ref:174` | Example Frugality (<= 2) | P2 | I82/E88/R10 | `writing` | Example Budgeting |
| DD-07 | `2Do_ref:183` | Stop and Escalate Conditions | P0 | I95/E96/R05 | `exec-modes` | Halt Protocol & Error Codes |
| DD-08 | `2Dos:17` | Anti-Self-Verification Trap | P0 | I94/E96/R05 | `exec-modes` | Verification Grounding & Independent DoD |
| SN-01 | `Snippets:11` | Q&A Decision Matrix Standard | P1 | I90/E94/R08 | `exec-modes` | Q&A Game / Decision Matrix Adapter |
| SN-02 | `Snippets:78` | Formula REI Expected Value | P2 | I80/E85/R12 | `exec-modes` | Quantitative Option Evaluation |
| SN-03 | `Snippets:85` | Macro-Meso-Micro (MMM) | P1 | I90/E92/R08 | `exec-modes` | Iterative Decomposition (MMM) |
| SN-04 | `Snippets:107` | 4-Phase Analytical Evaluation | P2 | I85/E90/R10 | `exec-modes` | Candidate Bake-Off / Comparison Matrix |
| SN-05 | `Snippets:4` | Adaptive Informatics Contract | P1 | I88/E90/R10 | `router` | Gating IF-Clauses / Adaptive Standards |
| SN-06 | `2Dos:225` | Lean Execution Contract | P1 | I92/E95/R08 | `exec-modes` | Lean Execution Workflow Adapter |
| SN-07 | `2Dos:10` | Handover Protocol Standard | P1 | I90/E94/R08 | `exec-modes` | Handover / Handoff Specification |
| SN-08 | `2Dos:3` | Git Synchronization Protocol | P2 | I85/E90/R08 | `exec-modes` | Git Operations & Clean Commits |
| EX-01 | `ORIG_REQ:39` | Substance Over Ceremony Invariant | P0 | I98/E98/R05 | `router` & `writing` | Explicit Rule-Breaking Authority |
| EX-02 | `2Dos:134` | Pre-Addition Check Rule | P1 | I90/E92/R10 | `gov-schemas` | Gate Creation Restraint |

---

## Synthesis Recommendations for Informatics Program

1. **Root Router (`general-informatics-router.md`)**:
   - Embed within first 500 tokens the P0 Core Invariants: `TARGET Dominance`, `Checkable Ambiguity Resolution`, `Conscious JIT Context Loading`, and `Substance Over Ceremony`.
   - Provide lean conditional IF-triggers (`<informatics when="writing" ref="writing-profile.md">`, `<informatics when="patch" ref="execution-modes.md#patch">`) to guarantee strict context isolation.
   - Maintain the router under ~100 lines and ~400 tokens.

2. **Writing Profile (`writing-profile.md`)**:
   - Codify Simplified Technical English (STE): active voice, single-action commands, procedural sentences <= 20 words, descriptive sentences <= 25 words.
   - Forbid modal hedging (`should`, `may`, `might`, `could`).
   - Define visual block limits (~150 words per block before tables/lists) and Minto BLUF sentence-1 structures.
   - Enforce inline priority annotation `[P<tier> | I<impact>/E<evidence>/R<risk>]`.

3. **File Architecture (`file-architecture.md`)**:
   - Enforce the Five-Plane Information Architecture (Control, Scoped, Skills, Knowledge Bundles, Evidence & History).
   - Strict current-truth separation: 0 inline changelogs or superseded proposals in live specs.
   - OKF v0.2 frontmatter minimalism: restrict metadata to 3–4 natural fields.
   - Mandate Gall's Law flat-file conventions and top-loaded primacy (first 500 tokens).

4. **Execution Modes (`execution-modes.md`)**:
   - Codify dedicated task adapters:
     - `Decision Matrix / Q&A`: Question, Options with `(I/E/R)` qualitative estimates, Recommendation, Reasoning, and Rejection Notes.
     - `Exact-Match Block Patch Discipline`: `<file>`, `<old>`, `<new>` with zero AST decompilation and strict whitespace preservation.
     - `Macro-Meso-Micro (MMM)`: 3-tier decomposition.
     - `Lean Execution`: Single `--since` gate runs, inline execution for <= 5 files, two-strike rule.
     - `Handover Specification`: 5-component handoff standard.

5. **Governance & Validation Schemas (`validation-profiles.md` / `governance-schemas.md`)**:
   - Codify the Minimal Viable File Test (MVT-01 to MVT-04).
   - Enforce model-specific directive ceilings (50, 80, 100).
   - Enforce the Directive Deletion Test (<10% impact rule removal).
   - Enforce Pre-Addition Restraint on new gates and checks.
