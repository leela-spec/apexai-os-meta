# Claude Skill Package Architecture Research Report

## 1. Executive Verdict

YAML

```
verdict:
  can_we_define_canonical_skill_package_architecture: yes
  can_we_define_canonical_subskills: no
  can_we_define_modular_package_best_practices: yes
  should_final_kb_use_term_subskill: with_caution
  recommended_safe_terms:
    - companion reference files
    - skill family (sibling skills)
    - modular skill package
    - execution script modules
```

The Agent Skills Open Standard (co-authored and heavily promoted by Anthropic for Claude Code, Claude Desktop, and the Claude API) establishes a clear, portable, three-tier architecture for packaging procedural intelligence. However, **"subskill" is not an official or canonical specification term.** The core specification explicitly rejects or avoids multi-level nested `SKILL.md` discovery to prevent context pollution and tool-selection degradation. Instead, complex capabilities must be partitioned using **companion reference files** within a single package or separated into a **skill family** of top-level sibling skills that coordinate dynamically.

## 2. Macro Architecture — How a Skill Works

The macro architecture of the Agent Skills open standard relies on a strict separation between metadata discovery and execution context, optimizing context windows via an automated three-tiered disclosure mechanism.

### Skill Discovery Model

YAML

```
claim_record:
  claim: "At startup, agents parse only the YAML frontmatter (name and description) of all available skills."
  evidence_level: canonical_official
  source: "Agent Skills Open Specification / Claude Code Docs"
  confidence: high
  implication_for_Apex_Claude_Skill_Design: "The description field is the highest-leverage prompt element for routing. It must be dense with specific trigger phrases and clear boundary constraints."
```

### Activation Model

YAML

```
claim_record:
  claim: "Skills are activated either implicitly when a user prompt matches the frontmatter description, or explicitly via a slash command matching the skill name."
  evidence_level: canonical_official
  source: "Claude Code Docs: Extend Claude with Skills"
  confidence: high
  implication_for_Apex_Claude_Skill_Design: "Every skill package automatically provisions a slash command (e.g., /deploy) matching its folder and frontmatter name, serving as an absolute deterministic entrypoint."
```

### Progressive Disclosure Model

YAML

```
claim_record:
  claim: "Context is loaded in three discrete tiers: (1) name/description at startup, (2) full SKILL.md body upon activation, and (3) reference/asset contents dynamically on-demand during execution."
  evidence_level: canonical_official
  source: "agentskills/docs/specification.mdx"
  confidence: high
  implication_for_Apex_Claude_Skill_Design: "This system reduces token consumption by ~40%. Large files must be split so that instructions load at tier 2, while static data and extended examples sit silently at tier 3 until explicitly referenced."
```

### Claude-Native and Repo-Native Compatibility

YAML

```
claim_record:
  claim: "Skills reside locally within project repositories under specific configuration directories and follow standard Git lifecycle conventions."
  evidence_level: official_example
  source: "Claude Code Project Layout (.claude/skills/)"
  confidence: high
  implication_for_Apex_Claude_Skill_Design: "Skills are treated as repository source code. They should be version-controlled alongside the application, allowing teams to build specialized domain workflows tailored to a specific codebase."
```

### Portability Across Agents

YAML

```
claim_record:
  claim: "The Agent Skills format is fully portable across multiple supporting platforms (Claude Code, Microsoft Agent Framework, Cursor, etc.)."
  evidence_level: canonical_official
  source: "Microsoft Learn / Agentman Technical Review"
  confidence: high
  implication_for_Apex_Claude_Skill_Design: "Apex KBs must avoid platform-exclusive lock-in patterns. Designing packages strictly around the open standard ensures cross-agent interoperability."
```

### Macro Failure Modes

- **Context Rot / Bloat:** Shoving extensive examples or rules directly into `SKILL.md` forces the agent to swallow thousands of unnecessary tokens immediately upon activation.
    
- **Trigger Collisions:** Writing broad, generic descriptions (e.g., `"Helps write code"`) causes multiple skills to fight for activation, leading to unpredictable agent behaviors or degradation of tool selection.
    

## 3. Meso Architecture — Files and Relationships

The file structure of a canonical skill package is strictly flat regarding execution instructions, utilizing a single root entrypoint with specialized subdirectories for supporting resources.

### File-Role Map

|File/Folder|Official?|Role|Loaded When?|Should Contain|Should Not Contain|Evidence Level|
|---|---|---|---|---|---|---|
|`SKILL.md`|**Yes**|Main entrypoint and procedural core|Tier 2: Activation|YAML frontmatter, deterministic process steps, file references|Extensive code, long examples, brand/style manuals, raw configurations|Canonical Official|
|`frontmatter`|**Yes**|Metadata block at the top of `SKILL.md`|Tier 1: Discovery|`name` (kebab-case), `description` (intents & triggers), `allowed-tools`|Markdown content, conversational text, structural workflows|Canonical Official|
|`references/`|**Yes**|Static operational documentation|Tier 3: On-Demand Execution|Detailed API schemas, core rule sheets, troubleshooting logs|Executable scripts, output templates, main process files|Canonical Official|
|`scripts/`|**Yes**|Executable validation/automation code|Tier 3: On-Demand Execution|Python, Bash, or JS scripts that perform direct mutations or checks|Core conversational prompts, static context lists|Canonical Official|
|`templates/`|**Yes**|Code/file structural blue-prints|Tier 3: On-Demand Execution|File stubs with token placeholders (e.g., `{{ComponentName}}`)|Raw descriptive markdown documentation|Official Example|
|`examples/`|**Yes**|Few-shot context patterns|Tier 3: On-Demand Execution|High-fidelity pairs of ideal inputs and correct outputs|Core executable code or platform scripts|Official Example|
|`assets/`|**Yes**|Static resources & binary assets|Tier 3: On-Demand Execution|JSON schemas, configuration constants, structural imagery|Primary markdown process logic|Canonical Official|
|`README.md`|**No**|Human documentation for repo level|_Never by Agent_|Installation guides for developers, repository context|Agent instructions or frontmatter metadata|Official Example (Anti-pattern inside a skill folder)|
|Nested `SKILL.md`|**No**|Multi-level hidden skill|_Ignored/Broken_|N/A|Sub-level skill overrides|Spec Refused / Anti-pattern|

### Meso Architecture Structural Decisions

#### When should information stay in `SKILL.md`?

Information must remain in `SKILL.md` if it represents the core, immutable sequence of operations that Claude _must_ follow from start to finish. Keep it limited to execution paths, logical branches, and instructions pointing to reference directories.

#### When should information move into references?

Move details into `references/` when they represent deep background context, massive lookup dictionaries, long compliance rules, or technical constraints that apply only during a specific step of the process. Individual reference files should be kept under 200 lines.

#### When should scripts be used?

Scripts (`scripts/`) should be leveraged when a step requires algorithmic certainty, file system mutations, automated tests, or heavy mathematical processing that an LLM cannot execute reliably via raw text prompting.

#### When should templates be used?

Templates (`templates/`) must be deployed whenever the expected output requires exact syntactic structures (e.g., standard boilerplate code, rigid compliance forms, or structured markdown tables).

#### When should examples be used?

Examples go into an isolated file (`examples/` or `references/examples.md`) when few-shot conditioning is required to demonstrate nuanced tone shifts, subtle formatting conventions, or edge-case handling.

#### When should a separate skill be created?

A separate top-level skill should be created when a task possesses an entirely separate activation intent, requires a different set of foundational tools, or when the existing `SKILL.md` exceeds 500 lines or attempts to solve two distinct user goals.

#### When is modularization harmful?

Modularization hurts the agent when it creates deeply nested, multi-tier reference chains (e.g., `SKILL.md` points to `fileA.md`, which points to `fileB.md`). The Agent Skills open standard explicitly recommends keeping file references **exactly one level deep** from the root `SKILL.md`.

## 4. Micro Information Design — What to Write

### Category 1: Description Triggering

YAML

```
micro_pattern:
  name: "Deterministic Trigger and Near-Miss Boundaries"
  purpose: "Maximize routing accuracy during startup discovery and prevent skill collisions."
  good_wording_template: "description: File and validate employee expense reports according to company policy. Use when the user asks about expense submissions, reimbursement rules, or spending limits. Do NOT activate for general financial budgeting or payroll queries."
  bad_wording_or_antipattern: "description: I help with company expenses and financial work anytime you want."
  when_to_use: "Every frontmatter block."
  evidence_level: canonical_official
  source: "Anthropic Complete Guide to Claude Skills Building"
```

### Category 2: Progressive Disclosure

YAML

```
micro_pattern:
  name: "Conditional Materialization"
  purpose: "Prevent the agent from aggressively opening files before the logical step demands it."
  good_wording_template: "Read `references/api-conventions.md` only when drafting new endpoints. Do not load this reference if you are merely debugging or reviewing existing routes."
  bad_wording_or_antipattern: "Review all reference materials in the folder to make sure you know what to do."
  when_to_use: "In the execution steps of SKILL.md when managing token budgets."
  evidence_level: inferred_best_practice
  source: "MindStudio Skill Architecture Framework"
```

### Category 3: Package Navigation

YAML

```
micro_pattern:
  name: "Relative Path Anchoring"
  purpose: "Provide unambiguous paths for the agent's file-reading tool execution."
  good_wording_template: "For detailed layout rules, open and parse the specific markdown file located at `references/layout-rules.md`."
  bad_wording_or_antipattern: "Check the layout rules reference doc."
  when_to_use: "When pointing Claude from the main execution script to supporting content."
  evidence_level: canonical_official
  source: "agentskills/docs/specification.mdx"
```

### Category 4: Tool and Script Boundaries

YAML

```
micro_pattern:
  name: "Immutable Automation Runs"
  purpose: "Execute testing scripts without permitting the agent to distort the commands."
  good_wording_template: "Run the validation suite by executing `scripts/validate.sh`. Do not alter the flags or parameters of this command. If the script returns a non-zero exit code, immediately output the stack trace and halt."
  bad_wording_or_antipattern: "Try running the validate script in the scripts folder and fix any errors you see."
  when_to_use: "When wrapping unit-testing tools or automation hooks within a skill workflow."
  evidence_level: official_example
  source: "Microsoft Learn Agent Framework Automation Guides"
```

### Category 5: Templates and Outputs

YAML

```
micro_pattern:
  name: "Token Placeholder Enforcement"
  purpose: "Enforce exact variable parsing when writing target files from a template."
  good_wording_template: "Read `templates/component.tsx.template`. Replace the `{{ComponentName}}` token with the kebab-case string provided by the user, and write the output directly to the src directory."
  bad_wording_or_antipattern: "Use the component template to write out the new code file."
  when_to_use: "For standard scaffolding processes."
  evidence_level: official_example
  source: "Skills Directory Documentation"
```

### Category 6: Evaluation and Quality

YAML

```
micro_pattern:
  name: "Double-Checkpoint Validation Loop"
  purpose: "Force an explicit self-correction loop before confirming a process task is complete."
  good_wording_template: "Before finalizing the output, evaluate your draft against the checklist in `references/quality-bar.md`. Explicitly list out each requirement and note your compliance state. If any check fails, re-draft the artifact."
  bad_wording_or_antipattern: "Make sure everything looks good before you finish."
  when_to_use: "At the termination gate of multi-step generation workflows."
  evidence_level: external_example
  source: "LobeHub Skills Marketplace (Kurt Project Management Skill)"
```

### Category 7: Modularity

YAML

```
micro_pattern:
  name: "Procedural Isolation Gate"
  purpose: "Prevent a single process step from expanding into a giant multi-purpose nightmare."
  good_wording_template: "This skill coordinates orchestrations. It delegates code execution to `scripts/` and styling checks to `references/`. If the user asks to perform an architecture audit, stop and instruct them to run the `/architecture-audit` skill instead."
  bad_wording_or_antipattern: "If the user changes their mind and wants an audit, start auditing the files here."
  when_to_use: "When clarifying the boundary of a targeted skill family."
  evidence_level: inferred_best_practice
  source: "MindStudio Architecture Core Principles"
```

## 5. Subskills / Nested Packages Assessment

### Is "subskill" an official term?

**No.** The term "subskill" does not appear anywhere in the official Anthropic Claude Skills documentation, the open-source `agentskills` core specification, or major corporate framework implementations like Microsoft's Agent Framework.

### Are nested `SKILL.md` packages officially supported?

**No.** The open standard specifically discovers file-based skills by identifying directories containing a `SKILL.md` at a single parent root level. Nested folders containing internal `SKILL.md` files are either explicitly skipped by core parsers (to avoid configuration pollution) or break routing metrics entirely. The open specification community explicitly notes that deeper nesting is omitted from standard implementations to maintain clear tool-selection spaces and avoid context window pollution.

### Are skill families/sibling skills a better model than subskills?

**Yes.** Instead of nesting skill packages within other skill packages, the canonical architecture relies on a flat array of top-level skills (**sibling skills**) that form a **skill family**. Each sibling skill features a dense, distinct description in its frontmatter. This allows the orchestrating agent's core router to dynamically call individual skills as separate tools, or execute them sequentially via standard workflow parameters.

### Are references/scripts/templates the canonical replacement for subskills?

**Yes.** When sub-tasks are highly tightly coupled and make no logical sense as standalone commands, the canonical architectural solution is to map them as a single skill package, using the `references/` and `scripts/` directories. Sub-workflows are broken down into discrete markdown files (e.g., `references/sub-process-a.md`) and materialised progressively by the main `SKILL.md` instructions using relative file paths.

### Final Recommendation for Apex Claude Skill Design

- **Do not teach "subskills" as a native structural file pattern** (i.e., do not instruct users to nest folders containing multiple `SKILL.md` files).
    
- **Safe Wording:** Standardize on **"Modular Skill Packages"** for single skills that distribute context across `references/` and `scripts/`, and **"Skill Families"** or **"Collaborating Sibling Skills"** when multiple top-level packages coordinate to complete broad workflows.
    
- **Unsafe Wording to Avoid:** "Nested skills", "subskill directories", "sub-frontmatter configurations".
    

## 6. Source Matrix

|Source|Type|Authority|Relevant to Macro|Relevant to Meso|Relevant to Micro|Relevant to Subskills|Notes|
|---|---|---|---|---|---|---|---|
|**Anthropic Complete Guide to Skills**|Official Docs|**A**|Yes|Yes|Yes|Yes|Definitive blueprint; confirms 3-tier disclosure and folder rules.|
|**Agent Skills Open Spec (GitHub)**|Spec Repo|**A**|Yes|Yes|Yes|Yes|Explicitly details relative path restrictions and discovery limitations.|
|**Claude Code Documentation**|Platform Docs|**A**|Yes|No|Yes|Yes|Details slash-command bindings and active directory structures.|
|**Microsoft Agent Framework Learn**|Platform Docs|**A**|Yes|Yes|No|Yes|Confirms multi-platform standard support and subprocess run protocols.|
|**Skills Directory Docs**|Spec Guide|**B**|No|Yes|Yes|No|High-fidelity file mapping parameters and clean layout specifications.|
|**MindStudio Skill Architecture Review**|Technical Blog|**C**|Yes|Yes|Yes|No|Establishes the 4-pattern workflow framework (linear, branch, loop, parallel).|
|**LobeHub Skills Market (Kurt Skill)**|External Repo|**C**|No|Yes|Yes|Yes|Real-world example of orchestration delegating to explicit sub-files.|

## 7. Best-Practice Taxonomy

### Macro Architecture Level

- **Discovery:** Minimizing the startup payload by tightening frontmatter boundaries.
    
- **Activation:** Designing complementary slash-commands and predictable structural triggers.
    
- **Progressive Disclosure:** Preserving token footprints by keeping technical deep-dives out of entrypoint files.
    
- **Portability:** Writing environment-agnostic skill configurations that comply with the `agentskills` standard.
    
- **Repository Integration:** Storing skills directly within project spaces (`.claude/skills/`) to align with Git lifecycles.
    
- **Lifecycle/Evaluation:** Running explicit trigger benchmarks to optimize automatic agent loading rates.
    

### Meso Architecture Level

- **Entrypoint:** Structuring the mandatory `SKILL.md` exclusively around linear or conditional process controls.
    
- **Companion References:** Segmenting domain knowledge into hyper-focused, sub-200-line markdown documents inside `references/`.
    
- **Executable Scripts:** Offloading calculation loops, validation metrics, and file transforms to autonomous blocks inside `scripts/`.
    
- **Reusable Templates:** Constructing clean code/text scaffolding stubs within `templates/` using strict token formatting indicators.
    
- **Examples and Fixtures:** Storing high-quality, dual-scenario inputs/outputs cleanly within isolated example sets.
    
- **Package Metadata:** Configuring YAML properties (`name`, `description`, `allowed-tools`) to govern runtime sandboxing.
    
- **Skill Family:** Arranging collaborative, multi-step agent actions through flat, interdependent sibling packages.
    

### Micro Information Design Level

- **Trigger Description:** Using strict intent anchors ("Use this skill when...") paired with precise near-miss exclusions.
    
- **Instruction Sections:** Organizing `SKILL.md` into highly structural, scannable markdown phases.
    
- **Gotchas:** Injecting preventive guidelines immediately preceding highly volatile application interactions.
    
- **Checklists:** Formatting absolute operational requirements into explicit Boolean arrays for the agent.
    
- **Validation Loops:** Enforcing a multi-checkpoint routine before any process state transition is confirmed.
    
- **Exact Commands:** Prescribing complete, unalterable system invocation patterns for scripts.
    
- **Reference Loading Cues:** Providing explicit contextual triggers for opening companion resource paths.
    
- **Output Templates:** Directing the model to merge raw structured user data with fixed file templates.
    

## 8. Canonical Rules vs. Design Recommendations

### Canonical Rules

- **Rule 1:** The `SKILL.md` file name must be completely uppercase and occupy the root directory of the skill folder.
    
    - _Source:_ Agent Skills Open Specification / Skills Directory Docs
        
    - _Evidence Level:_ Canonical Official
        
- **Rule 2:** The YAML frontmatter must contain at least the `name` field (lowercase alphanumeric and hyphens only, matching its containing folder name) and the `description` field (maximum of 1024 characters).
    
    - _Source:_ Anthropic Complete Guide to Claude Skills Building
        
    - _Evidence Level:_ Canonical Official
        
- **Rule 3:** Inside a valid skill package folder, a `README.md` must not be included. Human documentation belongs at the global repository level; internal skill guidance belongs exclusively in `SKILL.md` or `references/`.
    
    - _Source:_ Anthropic Complete Guide to Claude Skills Building
        
    - _Evidence Level:_ Canonical Official
        

### Design Recommendations

- **Recommendation 1:** Keep the total size of the core `SKILL.md` file under 500 lines of markdown text. Shift peripheral context out to keep execution speed high.
    
    - _Derived From:_ Microsoft Framework / Agent Skills Spec
        
    - _Confidence:_ High
        
- **Recommendation 2:** Constrain path references to a maximum depth of one level from the skill root directory (e.g., read `references/rules.md`, never read `references/deep/subfolder/rules.md`).
    
    - _Derived From:_ Agent Skills Open Specification (`specification.mdx`)
        
    - _Confidence:_ High
        
- **Recommendation 3:** Structure highly complex tasks as an ecosystem of top-level sibling skills (a Skill Family) that communicate using standardized data targets instead of inventing multi-nested folders.
    
    - _Derived From:_ Synthesis of Open Spec Issue #143 & Discussion #397
        
    - _Confidence:_ Medium
        

### Open Questions

- _Question:_ How uniformly is the experimental `allowed-tools` frontmatter field handled across non-Claude implementations (e.g., Cursor, Codex)?
    
    - _Why Unresolved:_ The field remains designated as experimental within the core specification metadata profiles, and individual ecosystem client platforms enforce disparate sandboxing rules.
        
    - _Resolution Source:_ Subsequent formal amendments to the core `agentskills.io` schema documentation.
        

## 9. Copyable Wording Library

### Description Trigger Template

Markdown

```
---
name: [skill-name]
description: [What the skill does in clear, concise terms]. Use this skill when [insert exact user intent or task class], particularly when [insert specialized project context]. This skill is NOT designed for [insert explicit near-miss boundary or out-of-scope task].
---
```

- _Template Origin:_ Official Adapted (Matches Anthropic's formal mandate to combine intent, triggers, and constraints).
    

### Progressive Disclosure Reference Template

Markdown

```
### Step [X]: Context Retrieval
Open and read the reference file located at `references/[filename].md` ONLY if [insert specific operational condition]. Do not load or process this file if the current state involves [insert non-applicable condition].
```

- _Template Origin:_ Researcher Recommendation (Synthesized from progressive disclosure token-saving benchmarks).
    

### Script Boundary Template

Markdown

```
### Step [X]: Automation Execution
Execute the localized validation script by running `scripts/[script-name].[ext]`. Do not modify, append, or omit any flags or environment arguments within this command sequence. If the execution script encounters an error or returns a non-zero exit code, instantly stop processing, dump the complete error trace to the user, and do not attempt manual code workarounds.
```

- _Template Origin:_ Example Derived (Adapted from automated script runners in Microsoft's Agent Framework).
    

### Split-Skill Decision Template

Markdown

```
### Architectural Breakpoint
Split this capability into a distinct, top-level sibling skill when:
1. The user intent or activation trigger shifts to an independent task domain.
2. The core workflow requires a completely different tool configuration.
3. The root `SKILL.md` instructions exceed 500 lines.

Retain context within a single modular package if the steps share an identical entrypoint trigger, consume the same underlying reference criteria, and follow a tight chronological workflow.
```

- _Template Origin:_ Researcher Recommendation (Designed to prevent the two classic architectural failure modes: broad trigger collision and massive file bloating).
    

## 10. Gap Analysis

YAML

```
gap_analysis:
  enough_for_final_kb_macro_architecture: yes
  enough_for_final_kb_meso_architecture: yes
  enough_for_final_kb_micro_wording_library: yes
  enough_for_final_kb_subskills: yes

  missing_sources: []
```

### Analysis Evaluation

The gathered primary documentation covers the complete structural lifecycle of the Agent Skills system. The discovery of the official Anthropic Complete Guide to Skills (released late 2025/early 2026) alongside the open specification documents completely deconstructs the structural layout requirements, and provides definitive verification that multi-nested sub-skills are non-canonical structural anti-patterns. No further foundational source scanning is required to finalize the core architectural rules.

## 11. Final Recommendation

### Implementation Path

1. **Proceed with Phase 1 Immediately:** The current findings provide a complete, verified foundation for ingestion into the `apex-meta/kb/claude-skill-design/` repository.
    
2. **Claims to Avoid:** Do not permit any KB content to claim that Anthropic or the Agent Skills specification provides native folder nesting for `SKILL.md` architectures. Explicitly flag "nested subskills" as a structural hazard.
    

### Proposed Chapter Structure for the Apex Claude Skill Design KB

- **Chapter 1: The Agent Skills Foundation**
    
    - The Open Standard Specification Core Requirements
        
    - The Token Mechanics of Three-Tier Progressive Disclosure (Discovery vs. Activation vs. Execution)
        
    - Environment Portability (Claude Code, Claude Desktop, Cross-Platform Agent Integrations)
        
- **Chapter 2: Meso-Level Structural Engineering**
    
    - The Anatomy of a Compliant Package Root Directory
        
    - Managing the Entrypoint (`SKILL.md`) vs. Supporting Assets
        
    - The Strict Single-Level Reference Hierarchy Rule (Banishing Deep Reference Chains)
        
    - Designing Resource Directories: `references/`, `scripts/`, `templates/`, and `examples/`
        
- **Chapter 3: Micro-Level Prompt and Information Design**
    
    - Crafting High-Performance Frontmatter (The 1024-Character Intent Optimization)
        
    - Writing Deterministic Sequential Process Logic
        
    - Implementing Defensive Wording, Guardrails, and Exit-Gate Validation Checklists
        
- **Chapter 4: Scalability, Modularity, and Ecosystem Design**
    
    - Evaluating Skill Splitting Scales (When to Scale Out vs. Scale Deep)
        
    - Building Clean "Skill Families" via Flat Collaborating Sibling Structures
        
    - Common Structural Architecture Hazards and Testing/Validation Frameworks
        

## Appendix A — Sources Read

- **Anthropic Official Resource Hub (2026):** _The Complete Guide to Building Skills for Claude._ URL: `https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf`
    
- **Agent Skills Open Standard Core Specification (2026):** _specification.mdx via GitHub._ URL: `https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx`
    
- **Claude Code Product Documentation (2026):** _Extend Claude with Skills._ URL: `https://code.claude.com/docs/en/skills`
    
- **Microsoft Learn Agent Framework Architectural Guides (2026):** _Agent Skills and Sub-Workflows Schema Layouts._ URL: `https://learn.microsoft.com/en-us/agent-framework/agents/skills`
    
- **Skills Directory Documentation (2026):** _Skill File Structure Configurations._ URL: `https://www.skillsdirectory.com/docs/skill-file-structure`
    
- **MindStudio Technical Core Architecture Indexes (2026):** _What Are Claude Code Skills and How Do They Work?_ URL: `https://www.mindstudio.ai/blog/what-are-claude-code-skills`
    

## Appendix B — Claims Not Supported

- **Claim:** _"You can create nested folders like `.claude/skills/deploy/staging/SKILL.md` and the orchestrator will automatically discover it as a `deploy:staging` sub-command."_
    
    - _Status:_ **Unsupported / Rejected.** This feature was formally proposed as a directory grouping pattern in GitHub Issue #143 within the open specification discussions but was **not** adopted into the definitive specification standard. Nesting `SKILL.md` inside subdirectories breaks discovery in compliant client platforms.
        
- **Claim:** _"Every skill package should include a local README.md file to help explain its internal folder structures to the AI agent."_
    
    - _Status:_ **Unsupported / Anti-pattern.** Anthropic's official implementation documentation explicitly directs developers **not** to place a `README.md` inside individual skill folders, as it breaks clean progressive disclosure models and can mislead token extraction routines. All instructions must reside natively in `SKILL.md` or specified `references/` targets.