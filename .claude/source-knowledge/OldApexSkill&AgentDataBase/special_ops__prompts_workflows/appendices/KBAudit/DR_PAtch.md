

````patch
## target: DRPrompt4INf&KBRedesign.md
<<<<<<< SEARCH
Each agent must receive exactly the same canonical 5-file scaffold shape:

1. `ESSENCE.md`
2. `BEST_PRACTICES.md`
3. `LEARNING.md`
4. `MISTAKES.md`
5. `TEMPLATES.md`

Therefore, your final output must contain exactly 10 complete file bodies.

This is a full-body final-file generation task.

This is NOT a patching task.
This is NOT a diff task.
This is NOT a candidate/draft task.
This is NOT a future implementation plan.
This is NOT a general research report.

The output must be the final files.
=======
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
Appendices are the deep source layer.
The scaffold files must reference appendix/source material without becoming bloated by it.

This is a full-body final-file generation task.

This is NOT a patching task.
This is NOT a diff task.
This is NOT a candidate/draft task.
This is NOT a future implementation plan.
This is NOT a general research report.

The output must be the final files in a downloadable Markdown report.
>>>>>>> REPLACE

<<<<<<< SEARCH
# HARD TARGET

Produce complete final contents for these 10 files:

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
````

Do not add additional scaffold files.  
Do not rename these files.  
Do not replace the 5-file scaffold with a 10-file-per-agent scaffold.  
Do not create appendices as separate output files.  
Do not output patch plans.

---

# LOCKED SCAFFOLD LAW

The canonical scaffold is always exactly five files per agent:

```text
ESSENCE.md
BEST_PRACTICES.md
LEARNING.md
MISTAKES.md
TEMPLATES.md
```

=======

# HARD TARGET

Produce the complete final full-body contents for the chosen scaffold files under exactly these two target roots:

```text
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__informatics_design/
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/
```

Start by designing and outputting the complete `special_ops__informatics_design` scaffold.  
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

> > > > > > > REPLACE

<<<<<<< SEARCH

# PRIMARY SOURCE PRIORITY

Use sources in this order:

1. Current repo files under `leela-spec/MasterOfArts`, especially:
    
    - `OpenClaw/07_finalopenclawsystem/managed/agent_kb/`
        
    - existing Special Ops agent files
        
    - existing managed rules and rituals
        
    - existing final-system docs
        
2. Uploaded `KB_Audit_v2` file.  
    Treat this as a high-authority design reference for the new KB file style.  
    It is especially important for:
    
    - YAML-first active policy
        
    - critical rules near the top
        
    - evidence/prose separation
        
    - machine-readable rule metadata
        
    - active rule count discipline
        
    - audit checks
        
    - source quality policy
        
    - avoiding duplicated / paraphrased rules
        
    - designing for weakest model in the deployment fleet
        
3. Uploaded failure-analysis files:
    
    - `AnotherConstantFailure.md`
        
    - `ConstantAIFailureAnalysis.md`
        
    - any other uploaded failure / postmortem / no-drift files
        
4. Uploaded scaffold / promptflow / process files:
    
    - `APPENDIX_KB_PREIMAGE_CHECKED_SCAFFOLD_MUTATION_PROCESS_v3.md`
        
    - promptflow templates
        
    - state / task / output router templates
        
    - API call structure templates
        
    - gate / closure / manifest files
        
5. Existing prior Deep Research prompts:
    
    - `DeepResearchPrompt_v2.md`
        
    - `DeepResearchPrompt_KB_Orchestration_Infrastructure.md`
        
    - related prompt-design files
        
6. Official vendor docs or primary research sources where needed to validate current best practice.  
    Use web only for up-to-date external validation. Do not let generic web content override repo/source-specific requirements.  
    =======
    

# PRIMARY SOURCE PRIORITY

Use sources in this order:

1. Current repo files under `leela-spec/MasterOfArts`, limited to the two target agent KB roots unless a linked source inside those roots explicitly points elsewhere:
    
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
    

Do not use uploaded promptflow, patching, state, task, output-router, or prior Deep Research prompt files as source material for the scaffold contents. Those files informed this prompt design only. They must not pull the Deep Research output into promptflow, patch execution, Apex, Codex, runtime, or orchestration redesign.

> > > > > > > REPLACE

# <<<<<<< SEARCH  
source_authority_order:  
highest:  
- "explicit user target in this prompt"  
- "locked five-file scaffold law"  
- "repo final-system files"  
- "KB_Audit_v2 active policy"  
high:  
- "uploaded appendices and promptflow files"  
- "failure-analysis files"  
- "current Special Ops agent KB material"  
medium:  
- "prior Deep Research outputs"  
- "external official vendor docs"  
low:  
- "blog posts, unsourced claims, stale model behavior claims"

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

> > > > > > > REPLACE

<<<<<<< SEARCH  
conflict_resolution:

- "Never override the five-file scaffold."
    
- "Never convert this task into patching."
    
- "Never output draft/candidate files."
    
- "Never add extra scaffold files."
    
- "Prefer machine-readable YAML contracts over prose."
    
- "Prefer compact active policy with deep evidence compressed into referenced entries."  
    =======  
    conflict_resolution:
    
- "Never convert this task into patching."
    
- "Never output draft/candidate files."
    
- "Never let promptflow, patching, Apex, Codex, runtime, or generic orchestration sources redirect the task."
    
- "Prefer the five-file scaffold unless the scaffold decision gate finds a clearly better file system for these two agents."
    
- "Prefer machine-readable YAML contracts over prose."
    
- "Prefer compact active policy with deep evidence compressed into referenced entries."
    
- "Prefer fewer variables when the same reliability can be achieved with simpler structure."
    

> > > > > > > REPLACE

<<<<<<< SEARCH

- "new 10-file scaffold per agent"
    
- "appendix files as output"
    
- "generic agent architecture essay"
    
- "ApexAI_OS repo design"
    
- "promptflow primary redesign"
    
- "Codex execution design"  
    =======
    
- "unvalidated new scaffold shape"
    
- "appendix files as output"
    
- "generic agent architecture essay"
    
- "ApexAI_OS repo design"
    
- "promptflow primary redesign"
    
- "Codex execution design"
    
- "runtime execution design"
    
- "repo topology design"
    
- "state/task/output-router redesign"
    

> > > > > > > REPLACE

<<<<<<< SEARCH

# DESIGN REQUIREMENTS FOR EVERY FILE

Every generated file must be:

```yaml
file_design_requirements:
  machine_readable: true
  markdown_with_yaml_frontmatter: true
  yaml_blocks_parse_valid: true
  prose_minimized: true
  critical_rules_near_top: true
  token_efficient: true
  no_rule_duplication: true
  no_modal_hedging: true
  no_decorative_language: true
  no_unscored_claims_where_risk_relevant: true
  no_future_todo_placeholders: true
  no_candidate_status: true
  final_status_only: true
```

=======

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

> > > > > > > REPLACE

<<<<<<< SEARCH

# OUTPUT FORMAT

Return exactly one Markdown answer.

The answer must have exactly these top-level sections and no others:

```text
# FILE MANIFEST
# SOURCE BASIS USED
# FINAL FILES
# FINAL COMPLETENESS AUDIT
```

# Do not add an executive summary.  
Do not add a research report.  
Do not add recommendations after the files.  
Do not add implementation instructions after the files.

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

> > > > > > > REPLACE

<<<<<<< SEARCH

## Section 1: `# FILE MANIFEST`

Output a table with exactly 10 rows.

Use this table format:

```markdown
| Seq | Repo-relative path | Agent | Scaffold file | Primary function | Status |
|---:|---|---|---|---|---|
```

Every status must be `final`.

---

## Section 2: `# SOURCE BASIS USED`

=======

## Section 1: `# SCAFFOLD DECISION`

Output a compact YAML block only:

```yaml
scaffold_decision:
  validated_default_five_file_scaffold: true | false
  chosen_scaffold_files:
    - ""
  reason_if_changed: ""
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

> > > > > > > REPLACE

<<<<<<< SEARCH

## Section 3: `# FINAL FILES`

For each of the 10 files, output a full file block.

Use exactly this wrapper format for every file:

````markdown
## FILE {seq}: {repo-relative path}

```markdown
{complete file content here}
```

EOF: {repo-relative path}
````

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
```

---

## Section 4: `# FINAL COMPLETENESS AUDIT`

=======

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

> > > > > > > REPLACE

# <<<<<<< SEARCH  
| Exactly 10 files output | 10 | | |  
| Exactly 5 files per agent | yes | | |  
| Only canonical scaffold filenames used | yes | | |  
| All files full-body final content | yes | | |  
| No patch plans included | yes | | |  
| No unified diffs included | yes | | |  
| No candidate/draft status | yes | | |  
| KB_Audit_v2 style applied | yes | | |  
| Machine-readable YAML active policy used | yes | | |  
| EOF marker present for every file | yes | | |

| Scaffold decision completed | yes | | |  
| Informatics Design generated before Knowledge Bank | yes | | |  
| File count matches chosen scaffold | yes | | |  
| Only target agent roots used | yes | | |  
| All files full-body final content | yes | | |  
| Downloadable Markdown report produced | yes | | |  
| Four-backtick file wrappers used | yes | | |  
| No patch plans included | yes | | |  
| No unified diffs included | yes | | |  
| No candidate/draft status | yes | | |  
| KB_Audit_v2 style applied | yes | | |  
| Layered critical/required/recommended structure applied | yes | | |  
| Appendix/source reference layer represented compactly | yes | | |  
| Machine-readable YAML active policy used | yes | | |  
| EOF marker present for every file | yes | | |

> > > > > > > REPLACE

# <<<<<<< SEARCH  
SPLIT_REQUIRED:  
reason: "10 full file bodies exceed safe output size"  
proposed_parts:  
- part: 1  
files: "special_ops__informatics_design five files"  
- part: 2  
files: "special_ops__knowledge_bank five files"  
next_action: "Run the same prompt split by agent."

SPLIT_REQUIRED:  
reason: "Full final file bodies exceed safe output size"  
proposed_parts:  
- part: 1  
files: "special_ops__informatics_design complete chosen scaffold"  
- part: 2  
files: "special_ops__knowledge_bank complete chosen scaffold"  
next_action: "Run the same prompt split by agent, preserving the scaffold decision from part 1."

> > > > > > > REPLACE

<<<<<<< SEARCH  
Do not invent a different scaffold.  
Do not add files.

The scaffold is exactly:

```text
ESSENCE.md
BEST_PRACTICES.md
LEARNING.md
MISTAKES.md
TEMPLATES.md
```

# The target is exactly two agents:

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

> > > > > > > REPLACE

# <<<<<<< SEARCH  
The final output is exactly 10 full-body final files.

The final output is the complete full-body final file set for the chosen scaffold.

> > > > > > > REPLACE

```
::contentReference[oaicite:3]{index=3}
```