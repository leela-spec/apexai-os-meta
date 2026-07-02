# Deep Research Prompt — Rebuild Special Ops Informatics + Knowledge Bank Agent KB Scaffolds

````text
ROLE

You are Deep Research operating as a senior knowledge-base architect, informatics designer, agent-orchestration failure analyst, and machine-readable file-system designer.

Your task is NOT to write a research essay.

Your task is to produce the FINAL FULL-BODY CONTENTS of the new Special Ops agent KB scaffold files.

Use only the source classes explicitly authorized in this prompt. Do not let promptflow, patching, runtime, Codex, Apex, or prior Deep Research prompt materials drift the output into other system areas.

You must not write to the repository. Deep Research is read-only. Your final answer must be a downloadable Markdown report containing the complete final file bodies that can later be copied into the repo by a separate executor.

---

# OBJECTIVE

Rebuild from scratch the final machine-readable, token-efficient, failure-resilient KB scaffold files for exactly two Special Ops agents:

1. `special_ops__informatics_design`
2. `special_ops__knowledge_bank`

The previous scaffold hypothesis is a 5-file scaffold per agent:

1. `ESSENCE.md`
2. `BEST_PRACTICES.md`
3. `LEARNING.md`
4. `MISTAKES.md`
5. `TEMPLATES.md`

You must validate whether this 5-file scaffold is still the best scaffold architecture for these two agents.

Default expectation:
- preserve the 5-file scaffold if it remains the most token-efficient, machine-readable, operationally complete structure;
- change the scaffold only if research clearly shows a better scaffold architecture for the two target agents;
- if changing the scaffold, explain the decision briefly in the scaffold decision block and then output the final chosen complete file set.

The scaffold is the readable, organizational, always-usable layer.
Appendices and source files are the deep source layer.
Each scaffold file must be layered internally: critical rules first, required rules second, recommended rules third, compact source or appendix references last.
The scaffold files must reference source material without becoming bloated by copied evidence prose.

This is a full-body final-file generation task.

This is NOT a patching task.
This is NOT a diff task.
This is NOT a candidate/draft task.
This is NOT a future implementation plan.
This is NOT a general research report.

The output must be the final files in one downloadable Markdown report.

---

# HARD TARGET

Produce the complete final full-body contents for the chosen scaffold files under exactly these two target roots:

```text
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__informatics_design/
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/
```

Start by researching and designing the complete `special_ops__informatics_design` scaffold.
Then use that informatics design result as the structural basis for the `special_ops__knowledge_bank` scaffold.

Default file targets if the 5-file scaffold is validated:

```text
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__informatics_design/ESSENCE.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__informatics_design/BEST_PRACTICES.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__informatics_design/LEARNING.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__informatics_design/MISTAKES.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__informatics_design/TEMPLATES.md

OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/ESSENCE.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/BEST_PRACTICES.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/LEARNING.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/MISTAKES.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/TEMPLATES.md
```

If you choose a different scaffold architecture, the output must still stay inside the two target roots above and must still produce complete final file bodies.

Do not create appendices as separate output files.  
Do not output patch plans.  
Do not output a research report instead of files.

---

# SCAFFOLD DECISION GATE

Before writing the final files, validate the scaffold architecture.

Default scaffold hypothesis:

```text
ESSENCE.md
BEST_PRACTICES.md
LEARNING.md
MISTAKES.md
TEMPLATES.md
```

Definitions:

```yaml
scaffold_file_contract:
  ESSENCE.md:
    role: "compressed operating essence"
    content: "mission, boundaries, critical rules, routing, decision priorities"
    style: "short, dense, machine-readable"
  BEST_PRACTICES.md:
    role: "validated active best practices"
    content: "critical / required / recommended practices with prevents/evidence/impact metadata"
    style: "YAML-first, minimal prose"
  LEARNING.md:
    role: "learning lifecycle and validated lessons"
    content: "how lessons enter, get scored, validated, promoted, rejected, archived"
    style: "state-machine + schemas + compact rules"
  MISTAKES.md:
    role: "known failure modes and anti-patterns"
    content: "human mistakes, AI mistakes, file-design mistakes, drift patterns, prevention"
    style: "failure table + countermeasure contracts"
  TEMPLATES.md:
    role: "machine-readable templates"
    content: "schemas and reusable blocks for the agent’s outputs and internal records"
    style: "parse-valid YAML templates, no decorative prose"
```

---

# PRIMARY SOURCE PRIORITY

Use sources in this order:

1. Current repo files under `leela-spec/MasterOfArts`, limited to the two target agent KB roots unless a file inside those roots explicitly links to a necessary local source:
    
    - `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__informatics_design/`
    - `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/`
        
2. Uploaded `KB_Audit_v2` file.  
    Treat this as the high-authority design reference for the new KB file style.  
    It is especially important for:
    
    - YAML-first active policy
    - critical rules near the top
    - layered critical / required / recommended structure
    - evidence/prose separation
    - machine-readable rule metadata
    - active rule count discipline
    - audit checks
    - source quality policy
    - avoiding duplicated / paraphrased rules
    - designing for weakest model in the deployment fleet
    - avoiding over-engineered variable-heavy formats that waste tokens
        
3. Official vendor docs or primary research sources where needed to validate current best practice.  
    Use web only for up-to-date external validation. Do not let generic web content override repo/source-specific requirements.

Do not use uploaded promptflow, patching, state, task, output-router, runtime, Codex, Apex, or prior Deep Research prompt files as source material for the scaffold contents. Those files informed this prompt design only. They must not pull the Deep Research output into promptflow, patch execution, Apex, Codex, runtime, or orchestration redesign.
    

---

# SOURCE AUTHORITY RULES

Use this conflict order:

```yaml
source_authority_order:
  highest:
    - "explicit user target in this prompt"
    - "scaffold decision gate in this prompt"
    - "repo files inside the two target agent KB roots"
    - "KB_Audit_v2 active policy"
  high:
    - "official vendor docs or primary research sources used only for current best-practice validation"
  low:
    - "blog posts, unsourced claims, stale model behavior claims"
  excluded:
    - "promptflow files as scaffold-content sources"
    - "patching files as scaffold-content sources"
    - "prior Deep Research prompts as scaffold-content sources"
    - "ApexAI_OS or repo-topology files as scaffold-content sources"
    - "runtime execution files as scaffold-content sources"
```

If sources conflict:

```yaml
conflict_resolution:
  - "Never convert this task into patching."
  - "Never output draft/candidate files."
  - "Never let promptflow, patching, Apex, Codex, runtime, or generic orchestration sources redirect the task."
  - "Prefer the five-file scaffold unless the scaffold decision gate finds a clearly better file system for these two agents."
  - "Prefer machine-readable YAML contracts over prose."
  - "Prefer compact active policy with deep evidence compressed into referenced entries."
  - "Prefer fewer variables when the same reliability can be achieved with simpler structure."
```

---

# HARD EXCLUSIONS

Do not include:

```yaml
forbidden_outputs:
  - "implementation-ready research packet instead of files"
  - "file map only"
  - "patch plan"
  - "unified diff"
  - "search/replace blocks"
  - "candidate/draft scaffold"
  - "future implementation roadmap"
  - "recommendations without final file bodies"
  - "unvalidated new scaffold shape"
  - "appendix files as output"
  - "generic agent architecture essay"
  - "ApexAI_OS repo design"
  - "promptflow primary redesign"
  - "Codex execution design"
  - "runtime execution design"
  - "repo topology design"
  - "state/task/output-router redesign"
  - "MCP discussion unless directly relevant to Markdown KB file structure"
  - "vector database / embedding / RAG pipeline design unless directly relevant to Markdown KB file structure"
```

---

# DESIGN REQUIREMENTS FOR EVERY FILE

Before generating files, validate whether these requirements are sufficient and not over-engineered.

Every generated file must be:

```yaml
file_design_requirements:
  machine_readable: true
  markdown_with_yaml_frontmatter: true
  yaml_blocks_parse_valid: true
  prose_minimized: true
  critical_rules_near_top: true
  layered_rule_structure: "critical -> required -> recommended -> references"
  token_efficient: true
  no_rule_duplication: true
  no_modal_hedging: true
  no_decorative_language: true
  no_unscored_claims_where_risk_relevant: true
  no_future_todo_placeholders: true
  no_candidate_status: true
  final_status_only: true
  appendix_reference_layer: true
  overengineering_guard: "Use the fewest metadata fields and variables that preserve machine readability and operational safety."
```

Each file must include frontmatter with at least:

```yaml
frontmatter_required_fields:
  class: ""
  role: ""
  surface: "agent_kb"
  agent: ""
  scaffold_file: ""
  version: "1.0"
  status: "final"
  context_mode: "compact"
  target_model_min: ""
  target_model_max: ""
  max_active_rules: 20
  owner: ""
  validator: ""
  last_validated_at: ""
```

Do not invent unsupported owners if repo evidence gives a better answer. If owner/validator cannot be fully verified, use the most conservative repo-consistent assignment and mark the uncertainty inside a compact YAML field, not in prose.

---

# STYLE REQUIREMENTS FROM KB_AUDIT_v2

Use `KB_Audit_v2` as the most important style and structure reference.

Apply these rules:

```yaml
kb_audit_style_requirements:
  critical_path:
    - "Put critical operational rules early."
    - "Encode active rules, checks, and templates as parse-valid YAML."
    - "Separate active policy from evidence prose."
    - "Use schema-oriented outputs for machine-consumed artifacts."
  active_policy:
    - "Prefer YAML blocks over prose paragraphs."
    - "Every rule has tier, prevents, evidence_refs, risk_if_unfixed, evidence_strength, impact_if_fixed where applicable."
    - "Do not duplicate rules across sections."
    - "Keep rule count low enough for always-loaded context."
  evidence_handling:
    - "Use compact evidence references rather than long evidence essays."
    - "Do not promote weak or unsourced claims to canon."
    - "Mark time-sensitive model claims with validity_window if used."
  audit:
    - "Include file-specific checks only when they are operationally useful."
    - "Avoid adding guardrails for their own sake."
```

---

# AGENT-SPECIFIC REQUIREMENTS

## A. `special_ops__informatics_design`

This agent owns information structure.

Its files must define how to design KB/file systems that are:

```yaml
informatics_design_scope:
  owns:
    - "file taxonomy"
    - "information architecture"
    - "section architecture"
    - "machine-readable layout"
    - "frontmatter standards"
    - "token-efficient organization"
    - "retrieval-oriented file design"
    - "naming and placement logic"
    - "context loading surfaces"
    - "anti-drift file structure"
  does_not_own:
    - "truth promotion authority"
    - "agent runtime execution"
    - "Codex patch execution"
    - "business/domain decisions"
    - "promptflow redesign except as structural input"
```

The Informatics Design scaffold must be able to answer:

```yaml
informatics_design_questions:
  - "Where should this knowledge live?"
  - "What file shape makes it machine-readable?"
  - "What should be active policy versus appendix/evidence?"
  - "What should be always-loaded versus retrieved?"
  - "What structure prevents rule duplication and context clutter?"
  - "What naming or frontmatter makes the file auditable?"
```

## B. `special_ops__knowledge_bank`

This agent owns KB lifecycle and knowledge governance.

Its files must define how knowledge is:

```yaml
knowledge_bank_scope:
  owns:
    - "knowledge intake"
    - "source classification"
    - "evidence grading"
    - "candidate-to-canon lifecycle"
    - "learning capture"
    - "mistake capture"
    - "promotion/rejection/archive logic"
    - "KB freshness"
    - "cross-file knowledge consistency"
    - "agent KB governance"
  does_not_own:
    - "file taxonomy as primary authority"
    - "runtime execution"
    - "Codex patch execution"
    - "business/domain decisions"
    - "promptflow redesign except as source material"
```

The Knowledge Bank scaffold must be able to answer:

```yaml
knowledge_bank_questions:
  - "Is this knowledge accepted, candidate, rejected, stale, or archived?"
  - "What evidence supports this rule?"
  - "What failure does this rule prevent?"
  - "Which agent owns this knowledge?"
  - "Who validates it?"
  - "When should this be promoted?"
  - "When should this be rejected or quarantined?"
```

---

# FAILURE MODES TO DESIGN AGAINST

Every file must be designed to prevent the current repeated failures:

```yaml
mandatory_failure_modes:
  - id: FM-01
    name: "scope drift disguised as diligence"
    prevention: "hard target first; no extra deliverables"
  - id: FM-02
    name: "wrong scaffold shape"
    prevention: "five-file scaffold is locked"
  - id: FM-03
    name: "machine-unreadable prose"
    prevention: "YAML-first active rules and templates"
  - id: FM-04
    name: "token bloat"
    prevention: "compact rules; no repeated evidence prose"
  - id: FM-05
    name: "candidate/canon confusion"
    prevention: "explicit status and lifecycle rules"
  - id: FM-06
    name: "rule duplication and paraphrase conflict"
    prevention: "single canonical rule block per rule"
  - id: FM-07
    name: "critical rules buried mid-file"
    prevention: "critical path within first active section"
  - id: FM-08
    name: "full-body generation loses requirements"
    prevention: "manifest + exact file count + EOF markers + final audit"
  - id: FM-09
    name: "agent owns the wrong decision"
    prevention: "owns / does_not_own blocks"
  - id: FM-10
    name: "research becomes implementation plan instead of files"
    prevention: "final output only full file bodies"
```

---

# OUTPUT FORMAT

Create one downloadable Markdown report/file named:

```text
SPECIAL_OPS_INF_KB_SCAFFOLD_FINAL.md
```

Do not rely on a single fragile chat code block as the deliverable.
The report/file must contain the final full-body file contents in clearly separated file sections.

The downloadable Markdown report must have exactly these top-level sections and no others:

```text
# SCAFFOLD DECISION
# FILE MANIFEST
# SOURCE BASIS USED
# FINAL FILES
# FINAL COMPLETENESS AUDIT
```

Do not add an executive summary.  
Do not add a research essay.  
Do not add recommendations after the files.  
Do not add implementation instructions after the files.

---

## Section 1: `# SCAFFOLD DECISION`

Output a compact YAML block only:

```yaml
scaffold_decision:
  validated_default_five_file_scaffold: true | false
  chosen_scaffold_files:
    - ""
  reason_if_changed: null
  overengineering_check: "pass | fail"
  layered_model_confirmed: true
  generation_order:
    - "special_ops__informatics_design"
    - "special_ops__knowledge_bank"
```

If the five-file scaffold is retained, `reason_if_changed` must be `null`.

---

## Section 2: `# FILE MANIFEST`

Output a table with one row per final file.

Use this table format:

```markdown
| Seq | Repo-relative path | Agent | Scaffold file | Primary function | Status |
|---:|---|---|---|---|---|
```

Every status must be `final`.

---

## Section 3: `# SOURCE BASIS USED`

Briefly list the source classes used.

Use this format only:

```yaml
source_basis_used:
  repo_sources:
    - ""
  uploaded_sources:
    - ""
  web_sources:
    - ""
  source_authority_notes:
    - ""
```

Keep this section short. Do not write a research essay.

---

## Section 4: `# FINAL FILES`

For each final file, output a full file section.

Use this wrapper format for every file inside the downloadable Markdown report:

`````markdown
## FILE {seq}: {repo-relative path}

````markdown
{complete file content here}
````

EOF: {repo-relative path}
`````

Use four-backtick fences around file contents to reduce syntax breakage when the generated file itself contains triple-backtick YAML blocks.

Rules:

```yaml
file_block_rules:
  - "Every file block must contain the complete final file content."
  - "No placeholders."
  - "No TODO."
  - "No 'draft'."
  - "No 'candidate'."
  - "No ellipses."
  - "No summary instead of content."
  - "No omitted sections."
  - "No patch markers."
  - "No diff markers."
  - "Each file must include YAML frontmatter."
  - "Each file must be valid Markdown."
  - "All YAML blocks inside files must be parse-valid YAML."
  - "Each file must implement a layered rule structure: critical first, required second, recommended third, references/evidence last."
  - "Each file must reference appendix/source layers compactly instead of copying long evidence prose into active rules."
```

---

## Section 5: `# FINAL COMPLETENESS AUDIT`

Output this exact audit table and fill it:

```markdown
| Check | Required result | Actual result | Pass/fail |
|---|---|---|---|
| Scaffold decision completed | yes |  |  |
| Informatics Design generated before Knowledge Bank | yes |  |  |
| File count matches chosen scaffold | yes |  |  |
| Only target agent roots used | yes |  |  |
| All files full-body final content | yes |  |  |
| Downloadable Markdown report produced | yes |  |  |
| Four-backtick file wrappers used | yes |  |  |
| No patch plans included | yes |  |  |
| No unified diffs included | yes |  |  |
| No candidate/draft status | yes |  |  |
| KB_Audit_v2 style applied | yes |  |  |
| Layered critical/required/recommended structure applied | yes |  |  |
| Appendix/source reference layer represented compactly | yes |  |  |
| Machine-readable YAML active policy used | yes |  |  |
| EOF marker present for every file | yes |  |  |
```

End immediately after this table.

---

# COMPLETENESS RULE

If you cannot fit all 10 full file bodies in one response, do not silently shorten or summarize.

Instead, output only:

```yaml
SPLIT_REQUIRED:
  reason: "Full final file bodies exceed safe output size"
  proposed_parts:
    - part: 1
      files: "special_ops__informatics_design complete chosen scaffold"
    - part: 2
      files: "special_ops__knowledge_bank complete chosen scaffold"
  next_action: "Run the same prompt split by agent, preserving the scaffold decision from part 1."
```

But prefer completing all 10 files in one output if feasible.

---

# FINAL REMINDER

Your final answer must be the final files.

Do not answer with analysis.  
Do not answer with a plan.  
Do not answer with patches.  
Do not answer with a research packet.  
Do not invent a different scaffold without passing the scaffold decision gate.  
Do not add files outside the two target agent roots.

The default scaffold hypothesis is:

```text
ESSENCE.md
BEST_PRACTICES.md
LEARNING.md
MISTAKES.md
TEMPLATES.md
```

The target is exactly two agents:

```text
special_ops__informatics_design
special_ops__knowledge_bank
```

The final output is the complete full-body final file set for the chosen scaffold.

```
::contentReference[oaicite:3]{index=3}
```