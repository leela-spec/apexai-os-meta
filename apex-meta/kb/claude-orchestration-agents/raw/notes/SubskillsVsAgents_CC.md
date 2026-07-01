Now I have comprehensive primary source data. Let me compile the full report.

---

# Claude Skill Package Architecture Research Report

---

## 1. Executive Verdict

text

`can_we_define_canonical_skill_package_architecture: yes can_we_define_canonical_subskills: no can_we_define_modular_package_best_practices: yes should_final_kb_use_term_subskill: no recommended_safe_terms:   - companion file  - reference file  - skill family / sibling skills  - progressive-disclosure resource  - modular skill package  - workflow module`

The official Agent Skills specification at [agentskills.io/specification](https://agentskills.io/specification) is concrete, authoritative, and sufficient to define macro/meso/micro architecture. "Subskill" is **not** an official term. Nested SKILL.md packages are neither supported nor demonstrated in canonical sources.[[anthropic.mintlify](https://anthropic.mintlify.app/en/docs/agents-and-tools/agent-skills/best-practices)]

---

## 2. Macro Architecture

## Skill Discovery Model

|Claim|Evidence Level|Source|Confidence|Apex Implication|
|---|---|---|---|---|
|At startup, `name` + `description` from ALL skills' YAML frontmatter are loaded into system prompt (~100 tokens each)|canonical_official|[agentskills.io/spec](https://agentskills.io/specification)|high|Description quality is the #1 activation lever|
|Claude selects a skill from 100+ by matching description to task|canonical_official|[Anthropic best-practices](https://anthropic.mintlify.app/en/docs/agents-and-tools/agent-skills/best-practices)|high|Description must discriminate reliably at scale|
|Full SKILL.md body loaded only after activation, not at discovery|canonical_official|agentskills.io/spec|high|SKILL.md body is not a discovery signal; description is|
|Reference/script/asset files loaded on-demand via bash Read, zero context cost until accessed|canonical_official|best-practices docs|high|Large reference files are safe to bundle|

## Activation Model

Activation is **description-match-driven**: Claude reads all skill `description` fields at startup and activates a skill when the task matches. The full SKILL.md body is then loaded. Scripts are **executed** (not loaded into context) — only the script's output consumes tokens.[[clauder-navi](https://clauder-navi.com/en/claude-skills-rules)]

## Progressive Disclosure Tiers (Official)

text

`Tier 1 — Discovery (~100 tokens):   name + description (always loaded) Tier 2 — Activation (<5000 tokens): Full SKILL.md body (loaded on match) Tier 3 — On-demand (any size):      references/, scripts/, assets/ (loaded/run only when needed)`

## Macro Failure Modes

- **Vague description** → skill never activates (50% vs 80%+ success rate delta)[[prg](https://prg.sh/notes/Claude-Code-Agent-Skills)]
    
- **SKILL.md > 500 lines** → performance degrades, split required[[clauder-navi](https://clauder-navi.com/en/claude-skills-rules)]
    
- **Deeply nested references** → Claude uses `head -100` partial reads, information loss[[anthropic.mintlify](https://anthropic.mintlify.app/en/docs/agents-and-tools/agent-skills/best-practices)]
    
- **No feedback loops** → quality-critical tasks fail silently[[anthropic.mintlify](https://anthropic.mintlify.app/en/docs/agents-and-tools/agent-skills/best-practices)]
    
- **Windows-style paths** → bash navigation fails[[anthropic.mintlify](https://anthropic.mintlify.app/en/docs/agents-and-tools/agent-skills/best-practices)]
    

## Portability

Skills are portable across Claude.ai (paid), Claude Code (via `/plugin`), and the Anthropic API. The `compatibility` field (max 500 chars) signals environment requirements; omit for most skills.[[github](https://github.com/anthropics/skills/blob/main/spec/agent-skills-spec.md)]

---

## 3. Meso Architecture — Files and Relationships

## File-Role Map

|File/Folder|Official?|Role|Loaded When|Should Contain|Should NOT Contain|Evidence Level|
|---|---|---|---|---|---|---|
|`SKILL.md`|**Yes (required)**|Entry point: metadata + instructions|On activation|`name`, `description` frontmatter; step-by-step instructions; examples inline; links to companion files|API docs, large datasets, deeply nested chains|canonical_official|
|`name` (frontmatter)|**Yes (required)**|Unique ID, ≤64 chars, lowercase+hyphens, matches directory name|Discovery startup|Gerund-form verb phrase recommended|Uppercase, reserved words, consecutive hyphens|canonical_official|
|`description` (frontmatter)|**Yes (required)**|Activation selector, ≤1024 chars|Discovery startup|What + when + key domain terms|Vague text, XML tags, reserved words|canonical_official|
|`references/`|Yes (optional)|On-demand documentation|When SKILL.md explicitly links and Claude follows|Domain-specific docs, API references, schemas, form guides|Instructions that belong in SKILL.md, deeply chained references|canonical_official|
|`scripts/`|Yes (optional)|Executable code, run via bash|When explicitly invoked|Self-contained scripts with error handling, no voodoo constants|Logic that should be in references; assumed-available packages|canonical_official|
|`assets/`|Yes (optional)|Static resources|When explicitly accessed|Templates, images, data files, lookup tables|Executable code|canonical_official|
|`examples/`|official_example|Concrete I/O pattern illustrations|When SKILL.md links|Input/output pairs, concrete not abstract|Abstract descriptions already in SKILL.md|official_example|
|`templates/`|official_example|Reusable output templates|When SKILL.md links|Structured output formats, report scaffolds|Dynamic logic (belongs in scripts)|official_example|
|`schemas/`|official_example|Data schemas for structured output|When SKILL.md links|JSON/YAML schemas|Narrative documentation|official_example|
|`README.md`|No (not in spec)|Human documentation only|Never by Claude|Human setup notes|Claude-facing instructions|inferred|
|Nested `SKILL.md`|**No**|Not supported|N/A|N/A|N/A|speculative_or_unsupported|

## Meso Decision Rules (Official)

- **Stay in SKILL.md**: Quick-start code, decision trees, workflow checklists, short examples — anything Claude needs immediately on activation[[anthropic.mintlify](https://anthropic.mintlify.app/en/docs/agents-and-tools/agent-skills/best-practices)]
    
- **Move to references/**: Content >100 lines, domain-specific details only relevant to subtasks, API references, legal/finance domain splits[[anthropic.mintlify](https://anthropic.mintlify.app/en/docs/agents-and-tools/agent-skills/best-practices)]
    
- **Use scripts/**: Deterministic, fragile, or batch operations where consistency is critical; anywhere "low freedom" applies[[anthropic.mintlify](https://anthropic.mintlify.app/en/docs/agents-and-tools/agent-skills/best-practices)]
    
- **Use assets/**: Templates for output format, static data, images for visual analysis[[github](https://github.com/anthropics/skills/blob/main/spec/agent-skills-spec.md)]
    
- **Create a separate skill**: When activation context differs, domain differs, or combined SKILL.md would exceed 500 lines with no clean internal split[[anthropic.mintlify](https://anthropic.mintlify.app/en/docs/agents-and-tools/agent-skills/best-practices)]
    
- **When modularization is harmful**: When it creates deeply nested reference chains, when SKILL.md becomes a bare table of contents with no executable content, when skills share the same trigger context
    

---

## 4. Micro Information Design

## Description Triggering

|Pattern|Good Template|Anti-Pattern|Evidence Level|
|---|---|---|---|
|**What + When + Keywords**|`Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.`|`Helps with PDFs.`|canonical_official|
|**Third-person specificity**|`Analyzing React component performance`|`Does code review`|official_example|
|**Near-miss boundary**|`Use when analyzing .xlsx files. Not for CSV files.`|_(boundary omitted)_|inferred_best_practice|

## Progressive Disclosure Reference

text

`**Form filling**: See [FORMS.md](FORMS.md) for complete guide **API reference**: See [REFERENCE.md](REFERENCE.md) for all methods`

— Named inline links are superior to generic "see references/" folder mentions. Claude navigates by following explicit links.[[anthropic.mintlify](https://anthropic.mintlify.app/en/docs/agents-and-tools/agent-skills/best-practices)]

**BAD (deeply nested):**

text

`SKILL.md → advanced.md → details.md → actual content`

**GOOD (one level deep):**

text

`SKILL.md → advanced.md (terminal) SKILL.md → reference.md (terminal) SKILL.md → examples.md (terminal)`

## Freedom Spectrum (Official)

|Level|Use When|Form|
|---|---|---|
|**High freedom**|Multiple valid approaches, context-dependent|Prose instructions|
|**Medium freedom**|Preferred pattern exists, some variation OK|Pseudocode / parameterized script|
|**Low freedom**|Fragile, critical sequence, batch/destructive|Exact command: `Run exactly: python scripts/migrate.py --verify --backup. Do not modify.`|

[[anthropic.mintlify](https://anthropic.mintlify.app/en/docs/agents-and-tools/agent-skills/best-practices)]

## Workflow Checklist Pattern (Official)

text

`Copy this checklist and check off as you complete them: - [ ] Step 1: Analyze the form (run analyze_form.py) - [ ] Step 2: Create field mapping (edit fields.json) - [ ] Step 3: Validate mapping (run validate_fields.py) - [ ] Step 4: Fill the form (run fill_form.py) - [ ] Step 5: Verify output (run verify_output.py)`

— Copy-paste checklists both structure Claude's execution and make progress visible to users.[[anthropic.mintlify](https://anthropic.mintlify.app/en/docs/agents-and-tools/agent-skills/best-practices)]

## Validation / Feedback Loop Pattern (Official)

text

``Run: `python scripts/validate_fields.py fields.json` Fix any errors before continuing. If validation fails, return to Step 2.``

The "plan → validate → execute → verify" loop with `changes.json` intermediate output is the official pattern for batch/destructive operations.[[anthropic.mintlify](https://anthropic.mintlify.app/en/docs/agents-and-tools/agent-skills/best-practices)]

## Script Boundary Wording

|Intent|Wording|
|---|---|
|Execute|`Run analyze_form.py to extract fields`|
|Read as reference|`See analyze_form.py for the extraction algorithm`|
|Conditional execute|`Run only when [condition]. Do not modify the command or add flags.`|

[[anthropic.mintlify](https://anthropic.mintlify.app/en/docs/agents-and-tools/agent-skills/best-practices)]

## Naming Conventions (Official)

- **Recommended**: gerund form — `processing-pdfs`, `analyzing-spreadsheets`
    
- **Acceptable**: noun phrase — `pdf-processing`, `spreadsheet-analysis`
    
- **Avoid**: `helper`, `utils`, `tools`, `documents`, `data`, `files`
    
- **Forbidden**: `anthropic-*`, `claude-*`, uppercase, consecutive hyphens[[anthropic.mintlify](https://anthropic.mintlify.app/en/docs/agents-and-tools/agent-skills/best-practices)]
    

---

## 5. Subskills / Nested Packages Assessment

text

`official_term:   question: "Is 'subskill' an official term?"  answer: NO  source_evidence: >    Not present in agentskills.io/specification, Anthropic best-practices docs,    or anthropics/skills README. No official definition found anywhere.  confidence: high nested_skill_support:   question: "Are nested SKILL.md packages officially supported?"  answer: NO  source_evidence: >    The spec defines one SKILL.md per skill directory. No mention of    nested SKILL.md files. Best-practices docs explicitly warn against    deeply nested reference chains; nested SKILL.md would be worse.  confidence: high skill_family_pattern:   question: "Are skill families/sibling skills a better model than subskills?"  answer: YES — sibling skills in separate directories are the canonical pattern  evidence: >    anthropics/skills repo uses flat sibling structure: skills/pdf, skills/docx,    skills/pptx, skills/xlsx — not skills/documents/pdf with nested SKILL.md.    Each is self-contained.  confidence: medium package_module_pattern:   question: "Are references/scripts/templates the canonical replacement for subskills?"  answer: YES  evidence: >    The three progressive-disclosure tiers (SKILL.md → references/ → scripts/assets/)    are the official modularization mechanism. Domain splits use reference/finance.md,    reference/sales.md etc. within one skill rather than nested child skills.  confidence: high final_recommendation:   question: "Should Apex Claude Skill Design teach subskills?"  answer: NO — teach modular skill packages and companion files instead  safe_wording:    - "companion file"    - "reference file (references/)"    - "sibling skill"    - "skill family (flat)"    - "progressive-disclosure resource"    - "domain split within a skill"  unsafe_wording_to_avoid:    - "subskill"    - "nested skill"    - "child skill"    - "nested SKILL.md"`

---

## 6. Source Matrix

|Source|Type|Authority|Macro|Meso|Micro|Subskills|Notes|
|---|---|---|---|---|---|---|---|
|[agentskills.io/specification](https://agentskills.io/specification)|Spec|**A**|✓|✓|✓|✓|Primary canonical spec|
|[Anthropic best-practices docs](https://anthropic.mintlify.app/en/docs/agents-and-tools/agent-skills/best-practices)|Docs|**A**|✓|✓|✓✓|✓|Richest micro wording source|
|[anthropics/skills GitHub](https://github.com/anthropics/skills)|Repo|**B**|✓|✓|partial|✓|Official examples, flat structure|
|[clauder-navi.com/claude-skills-rules](https://clauder-navi.com/en/claude-skills-rules)|Guide|**C**|partial|✓|✓|partial|Confirms 500-line, 64-char, 1024-char limits|
|[prg.sh/claude-code-agent-skills](https://prg.sh/notes/Claude-Code-Agent-Skills)|Blog|**C**|partial|—|✓|—|80% vs 50% activation rate claim|
|eigent-ai/agent-skills|Repo|**C**|—|partial|—|—|External collection; not analyzed deeply|
|antigravity-awesome-skills-main|Repo|**D**|—|partial|—|—|Not located in official sources|

---

## 7. Best-Practice Taxonomy

text

`macro:   - discovery: description-match at startup, all skills' frontmatter loaded  - activation: full SKILL.md body loaded on match  - progressive_disclosure: 3-tier (metadata → SKILL.md → resources)  - portability: claude.ai / Claude Code / API via compatibility field  - repository_integration: .claude/skills/ convention for Claude Code  - lifecycle_evaluation: build evals BEFORE extensive docs; iterate Claude A/B pattern meso:   - entrypoint: SKILL.md (required, ≤500 lines, ≤5000 tokens)  - companion_references: references/ one-level-deep, focused files with ToC if >100 lines  - executable_scripts: scripts/ self-contained, explicit error handling, no magic constants  - static_assets: assets/ templates, images, data files  - examples_fixtures: examples.md or examples/ as companion file  - package_metadata: name + description frontmatter (only required fields)  - skill_family: flat sibling skills, NOT nested SKILL.md micro:   - trigger_description: what+when+keywords, ≤1024 chars, third-person, specific  - instruction_sections: freedom spectrum (high/medium/low) matching task fragility  - gotchas: time-sensitive info in <details> legacy section; no Windows paths  - checklists: copy-paste [ ] workflow checklists for complex multi-step processes  - validation_loops: run → validate → fix → repeat; intermediate output files  - exact_commands: low-freedom tasks get verbatim commands + "do not modify" guard  - reference_loading_cues: named inline markdown links, not generic "see folder"  - output_templates: strict vs flexible template variants based on task criticality`

---

## 8. Canonical Rules vs Design Recommendations

## Canonical Rules (official spec/docs)

|Claim|Source|Evidence Level|
|---|---|---|
|`name`: ≤64 chars, lowercase+hyphens, no consecutive `--`, matches directory name|agentskills.io/spec|canonical_official|
|`description`: ≤1024 chars, non-empty, no XML tags|agentskills.io/spec|canonical_official|
|SKILL.md body ≤500 lines|best-practices + clauder-navi|canonical_official|
|File references one level deep from SKILL.md|best-practices|canonical_official|
|Scripts executed via bash; only output consumes tokens|best-practices|canonical_official|
|No nested SKILL.md structure defined or supported|spec + examples|canonical_official|
|Three optional directories: `scripts/`, `references/`, `assets/`|agentskills.io/spec|canonical_official|
|`allowed-tools` field is experimental|agentskills.io/spec|canonical_official|

## Design Recommendations (inferred from official examples/principles)

|Recommendation|Derived From|Confidence|
|---|---|---|
|Gerund-form names (`processing-pdfs`)|best-practices naming section|high|
|Include both "what" and "when" in description|best-practices|high|
|Use copy-paste [] checklists for complex workflows|best-practices examples|high|
|Build evaluations before extensive documentation|best-practices eval section|high|
|Use Claude A/B iteration pattern for skill development|best-practices|medium|
|Add ToC to reference files >100 lines|best-practices|medium|
|Organize references by domain (finance.md, sales.md)|best-practices pattern 2|medium|
|Use `<details>` tag for legacy/deprecated content|best-practices|medium|

## Open Questions

|Question|Why Unresolved|What Would Resolve It|
|---|---|---|
|Exact activation rate mechanics (50% vs 80% claim)|Third-party blog claim, not official|Anthropic publishing trigger eval methodology|
|`allowed-tools` behavior across implementations|Marked "experimental" in spec|Stable spec update or Claude Code changelog|
|Whether skills can reference MCP tools across servers|Best-practices mentions it but no spec detail|Full MCP × Skills integration spec|
|Whether `.claude/skills/` is the only valid path for Claude Code|Mentioned in examples, not in spec|Claude Code documentation update|

---

## 9. Copyable Wording Library

## Description Trigger Template

text

`[Gerund action]: [object/domain]. Use when [trigger context] or when the user mentions [key terms]. Not for [near-miss exclusion].`

**Example:**

text

`Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction. Not for image-only scans requiring OCR — use ocr-processing skill instead.`

**Template origin:** `official_adapted`

---

## Progressive Disclosure Reference Template

text

`**[Feature name]**: See [filename.md](filename.md) for [specific scope].`

**Example:**

text

`**Form filling**: See [FORMS.md](FORMS.md) for complete field-mapping guide. **API reference**: See [REFERENCE.md](REFERENCE.md) for all pdfplumber methods.`

**Do NOT write:** `See references/ for more details.` — this is a generic pointer that gives Claude no actionable cue.  
**Template origin:** `official_adapted`

---

## Script Boundary Template (Low Freedom)

text

`Run exactly this script: ```bash python scripts/[script].py [required-args] ``` Do not modify the command or add additional flags. If it fails, report the error output and stop.`

**Template origin:** `official_adapted`

---

## Workflow Checklist Template

text

`Copy this checklist and check off items as you complete them: - [ ] Step 1: [Action] (run [script.py] / read [file.md]) - [ ] Step 2: [Action] - [ ] Step 3: Validate ([command]) - [ ] Step 4: [Action] - [ ] Step N: If [condition fails], return to Step [N-2]`

**Template origin:** `official_adapted`

---

## Validation Loop Template

text

``Run: `python scripts/validate.py [input]` Fix any errors before continuing. If validation fails, return to Step [N]. Only proceed when validation passes.``

**Template origin:** `official_adapted`

---

## Split-Skill Decision Template

text

`create_separate_skill_when:   - activation context is distinct (different trigger description)  - domain expertise is non-overlapping  - combined SKILL.md would exceed 500 lines with no clean domain split  - different user populations or tool environments keep_as_one_skill_when:   - same activation trigger  - same workflow / same user intent  - content can be split into companion reference files  - the skill would be trivially small if split`

**Template origin:** `researcher_recommendation` (inferred from official guidance)

---

## Reference File ToC Template

text

`# [Reference Title] ## Contents - [Section 1 name](#section-1) - [Section 2 name](#section-2) - [Section 3 name](#section-3) ## Section 1 ...`

Use for any reference file >100 lines.[[anthropic.mintlify](https://anthropic.mintlify.app/en/docs/agents-and-tools/agent-skills/best-practices)]  
**Template origin:** `official_adapted`

---

## Evaluation Query Template (Official Structure)

json

`{   "skills": ["skill-name"],  "query": "Perform [specific task] on [specific input]",  "files": ["test-files/input.ext"],  "expected_behavior": [    "Does X using appropriate tool/library",    "Handles edge case Y correctly",    "Produces output in Z format"  ] }`

Build ≥3 evaluations. Test with Haiku, Sonnet, and Opus.[[anthropic.mintlify](https://anthropic.mintlify.app/en/docs/agents-and-tools/agent-skills/best-practices)]  
**Template origin:** `official_adapted`

---

## 10. Gap Analysis

text

``enough_for_final_kb_macro_architecture: yes enough_for_final_kb_meso_architecture: yes enough_for_final_kb_micro_wording_library: yes enough_for_final_kb_subskills: yes  # answer is "not supported/not canonical" missing_sources:   - source_type: Official Claude Code `.claude/skills/` path specification    why_needed: Confirm canonical install path for repo-native skills    suggested_query: "Claude Code skills folder path .claude/skills/ specification"   - source_type: Official trigger eval methodology / activation rate benchmarks    why_needed: Validate the 80% vs 50% claim; calibrate description quality    suggested_query: "Anthropic agent skills description activation eval benchmark"   - source_type: Official `allowed-tools` stable spec    why_needed: Currently marked experimental; behavior may vary    suggested_query: "agent skills allowed-tools stable support Claude Code"   - source_type: Full anthropics/skills examples analysis (pdf, docx, pptx, xlsx)    why_needed: Empirical meso-file pattern validation from production skills    suggested_query: GitHub anthropics/skills pdf SKILL.md references scripts``

---

## 11. Final Recommendation

text

`proceed_with_phase1_now: yes add_sources_before_phase1: no  # official sources are sufficient add_sources_before_phase2: yes sources_to_add_before_phase2:   - Full file-level analysis of anthropics/skills/pdf, docx, pptx, xlsx (production skills)  - Claude Code path specification (.claude/skills/)  - allowed-tools stable spec when published claims_to_avoid_until_more_evidence:   - "Subskills are supported" — unsupported  - "Nested SKILL.md files work" — unsupported  - "allowed-tools is production-ready" — marked experimental  - Any specific activation rate percentages (80%/50%) without Anthropic source proposed_chapter_structure_for_final_kb:   - Chapter 1: What is an Agent Skill (canonical definition, discovery model)  - Chapter 2: Macro Architecture (3-tier progressive disclosure, portability)  - Chapter 3: The SKILL.md File (frontmatter fields, body limits, naming)  - Chapter 4: Companion Files (references/, scripts/, assets/ — when + how)  - Chapter 5: Micro Information Design (descriptions, freedom spectrum, workflows)  - Chapter 6: Skill Families vs Modular Skills (sibling pattern, NOT subskills)  - Chapter 7: Evaluation and Iteration (eval-first, Claude A/B method)  - Chapter 8: Anti-Patterns (what to avoid — canonical list)  - Appendix A: Wording Library (copy-paste templates)  - Appendix B: Checklist for Effective Skills (official checklist)`

---

## Appendix A — Sources Read

|#|URL|Type|Used For|
|---|---|---|---|
|1|https://agentskills.io/specification|Canonical spec|Macro, Meso, Micro, Subskills|
|2|https://anthropic.mintlify.app/en/docs/agents-and-tools/agent-skills/best-practices|Official docs|Micro wording, patterns, evaluation|
|3|https://github.com/anthropics/skills|Official repo|Meso (structure), Macro (portability)|
|4|https://clauder-navi.com/en/claude-skills-rules|Community guide|Constraint confirmation|
|5|https://prg.sh/notes/Claude-Code-Agent-Skills|Blog|Activation rate claims|
|6|https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview|Overview docs|Macro definition|

---

## Appendix B — Claims Not Supported

|Claim|Why Rejected|Evidence Level|
|---|---|---|

|Claim|Why Rejected|Evidence Level|
|---|---|---|
|"Subskills" are an official construct|No mention in spec or official docs|speculative_or_unsupported|
|Nested SKILL.md files in subdirectories|Not in spec; spec shows flat structure; explicitly warned against deep chains|speculative_or_unsupported|
|SKILL.md can exceed 500 lines without penalty|Contradicted by spec and best-practices|speculative_or_unsupported|
|`allowed-tools` is a stable production feature|Spec explicitly marks it "experimental"|speculative_or_unsupported|
|Reference files can themselves reference other reference files safely|Explicitly warned: causes partial `head -100` reads, information loss|speculative_or_unsupported|
|`README.md` is a Claude-facing file|No role in progressive disclosure; human documentation only|speculative_or_unsupported|