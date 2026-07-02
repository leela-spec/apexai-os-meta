---
version: "1.0.0"
created_at: "2026-05-09"
purpose: >
  Authoritative reference for writing, structuring, and validating every file
  loaded by any sub-agent in this orchestration system.
scope: "All file types produced or consumed by orchestration sub-agents"
load_surface: "orchestrator_system_prompt"
directive_ceilings:
  gpt_4o:          50   # exponential decay; F-10
  claude_3_7_sonnet_standard: 50   # linear decay; F-10
  claude_3_7_sonnet_reasoning: 80  # linear decay, reasoning tasks; F-10
  gemini_2_5_pro:  100  # threshold decay, cliff onset 150-250; F-10
  o3:              100  # threshold decay, cliff onset 150-250; F-10
this_file_directive_count: 28
do_not_load_if:
  - "session token count > 80,000 tokens already consumed"
  - "another governance file is already active in this context window"
  - "file version does not match system manifest version"
  - "this_file_directive_count > directive_ceiling for active model"
---

# Context File Authority Reference

```yaml
# ════════════════════════════════════════════════════════════════
# SECTION 1 — CRITICAL DIRECTIVES  (must appear in first 500 tokens)
# ════════════════════════════════════════════════════════════════
critical_directives:

  - id: CD-01
    tier: critical
    directive: >
      Place all critical directives in the first 500 tokens of every file.
    prevents: "mid-document burial causing 30-50% compliance drop"
    evidence_ref: F-04

  - id: CD-02
    tier: critical
    directive: >
      Count compliance directives (imperative do/don't commands) separately
      from knowledge content; enforce model-specific ceiling on directives only.
    prevents: "premature ceiling breach on knowledge-heavy files"
    evidence_ref: F-01

  - id: CD-03
    tier: critical
    directive: >
      Attach an inline priority tag (critical/required/recommended) to every
      directive at point of declaration.
    prevents: "GPT-4o compliance falling below 31%; Claude below 58%"
    evidence_ref: F-07

  - id: CD-04
    tier: critical
    directive: >
      Use only imperative verbs with no modal hedging in every directive.
    prevents: "model treating directive as optional due to should/may/might/could"
    evidence_ref: F-06

  - id: CD-05
    tier: critical
    directive: >
      Separate system_prompt, knowledge_base, workflow, and tool_definition
      content into distinct files; never combine them in one file.
    prevents: "context clash and cascade failure from mixed-type files"
    evidence_ref: F-02
```

```yaml
# ════════════════════════════════════════════════════════════════
# SECTION 2 — FILE TYPE TAXONOMY
# ════════════════════════════════════════════════════════════════
file_type_taxonomy:

  system_prompt:
    purpose: "Defines agent role, constraints, and behavioral directives"
    token_budget: 2000
    directive_count_limit: "per model ceiling (see directive_ceilings)"
    load_frequency: "every session, position 0"
    required_sections:
      - role_statement
      - critical_directives
      - stop_and_escalate_conditions
    forbidden_patterns:
      - knowledge_corpus_inline
      - workflow_steps_inline
      - tool_schemas_inline
      - governance_meta_commentary
      - duplicate_directives_with_paraphrase

  knowledge_base:
    purpose: "Provides domain facts, reference data, and lookup content"
    token_budget: 100000
    directive_count_limit: 0
    load_frequency: "on-demand via retrieval"
    required_sections:
      - source_metadata
      - content_body
    forbidden_patterns:
      - imperative_directives
      - behavioral_constraints
      - workflow_logic
      - tool_schemas

  workflow:
    purpose: "Encodes sequential steps, branching logic, and handoff rules"
    token_budget: 4000
    directive_count_limit: 15
    load_frequency: "per task invocation"
    required_sections:
      - preconditions
      - steps
      - stop_conditions
      - escalation_path
    forbidden_patterns:
      - role_definitions
      - knowledge_corpus_inline
      - tool_schemas_inline
      - open_ended_loops_without_stop

  tool_definition:
    purpose: "Declares tool name, parameters, schema, and usage constraints"
    token_budget: 1000
    directive_count_limit: 5
    load_frequency: "per session alongside system_prompt"
    required_sections:
      - tool_name
      - description
      - input_schema
      - output_schema
      - error_handling
    forbidden_patterns:
      - prose_output_contracts
      - behavioral_agent_rules
      - knowledge_content
      - ambiguous_parameter_types
```

```yaml
# ════════════════════════════════════════════════════════════════
# SECTION 3 — DIRECTIVE WRITING RULES
# ════════════════════════════════════════════════════════════════
directive_writing_rules:

  - id: DWR-01
    tier: critical
    rule: >
      Start every directive with an imperative verb; omit modal verbs entirely.
    correct_example: "Return exactly one JSON object per response."
    wrong_example: "You should try to return a JSON object if possible."
    prevents: "optional interpretation of mandatory behavior"
    evidence_ref: F-06

  - id: DWR-02
    tier: critical
    rule: >
      Encode one action per directive; split compound actions into separate entries.
    correct_example: "Validate the schema before writing output."
    wrong_example: "Validate the schema, write output, and log the result."
    prevents: "partial compliance counted as full compliance"
    evidence_ref: F-01

  - id: DWR-03
    tier: required
    rule: >
      Tag every directive inline with tier (critical/required/recommended).
    correct_example: "# tier: critical — Halt execution on schema violation."
    wrong_example: "See legend at end of file for priority levels."
    prevents: "GPT-4o compliance drop below 31%"
    evidence_ref: F-07

  - id: DWR-04
    tier: required
    rule: >
      Add examples only for genuinely ambiguous directives; limit to two examples maximum.
    correct_example: "Ambiguous format rule with one correct and one wrong example."
    wrong_example: "Five examples illustrating the same straightforward directive."
    prevents: "example proliferation degrading task performance"
    evidence_ref: F-05

  - id: DWR-05
    tier: required
    rule: >
      Include a concrete stop_and_escalate condition in every workflow or system_prompt file.
    correct_example: "If input schema validation fails twice, return error_code:E002 and halt."
    wrong_example: "Try your best to handle unexpected inputs gracefully."
    prevents: "agent hallucination in the absence of stop conditions"
    evidence_ref: F-02

  - id: DWR-06
    tier: required
    rule: >
      Run the deletion test before finalizing any directive set; remove any rule
      that changes behavior in fewer than 10% of realistic cases.
    correct_example: "Removed: 'Do not use Comic Sans font' — zero production impact."
    wrong_example: "Retaining 47 rules accumulated from past incident reports."
    prevents: "rule proliferation creep and inter-rule conflict"
    evidence_ref: F-06

  - id: DWR-07
    tier: recommended
    rule: >
      Use YAML for instruction delivery blocks; use JSON Schema with strict:true
      for any machine-consumed structured output.
    correct_example: "output_schema defined as JSON Schema with strict: true."
    wrong_example: "Output should look like: { name: string, value: number }."
    prevents: "parsing failures and non-structural output compliance gaps"
    evidence_ref: F-03, F-08
```

```yaml
# ════════════════════════════════════════════════════════════════
# SECTION 4 — IF-THEN DECISION RULES
# ════════════════════════════════════════════════════════════════
decision_rules:

  - id: DR-01
    condition: "content includes agent role + behavioral constraints only"
    action: "write as system_prompt type; target ≤2000 tokens"
    fallback: "extract knowledge content to separate knowledge_base file first"
    evidence_ref: F-09

  - id: DR-02
    condition: "single file contains directives + knowledge corpus + workflow steps"
    action: "split into three separate typed files before loading"
    fallback: "if split is not possible, load knowledge_base segments via retrieval only"
    evidence_ref: F-02, F-05

  - id: DR-03
    condition: "directive count exceeds model ceiling for active model"
    action: "run deletion test; remove rules with <10% behavioral impact until under ceiling"
    fallback: "if cannot reduce, escalate to human author for consolidation"
    evidence_ref: F-01, F-06, F-10

  - id: DR-04
    condition: "a rule is ambiguous and produces inconsistent model behavior"
    action: "add one correct and one wrong example inline (max 2 total)"
    fallback: "if ambiguity persists with examples, rewrite directive as IF-THEN logic"
    evidence_ref: F-05

  - id: DR-05
    condition: "agent cannot resolve input with available context after two attempts"
    action: "return structured error with error_code and halt; do not fabricate"
    fallback: "escalate to orchestrator with partial state snapshot"
    evidence_ref: F-02

  - id: DR-06
    condition: "output will be consumed by another machine process"
    action: "enforce JSON Schema with strict:true on all outputs"
    fallback: "if schema unavailable, return plain JSON with explicit field list"
    evidence_ref: F-08

  - id: DR-07
    condition: "critical rule must be added to an existing file"
    action: "insert within first 500 tokens; renumber surrounding directives"
    fallback: "if first-500-token block is full, extract lower-priority rules to appendix"
    evidence_ref: F-04

  - id: DR-08
    condition: "session is long and context drift is suspected"
    action: "re-inject critical directives (CD-01 through CD-05) as a prefix reminder"
    fallback: "start a new session with clean context window"
    evidence_ref: F-02, F-04
```

```yaml
# ════════════════════════════════════════════════════════════════
# SECTION 5 — ANTI-PATTERNS
# ════════════════════════════════════════════════════════════════
anti_patterns:

  - id: AP-01
    pattern_name: "Rule Proliferation Creep"
    what_fails: "Every incident appends a new rule; total directive count exceeds model ceiling, causing wholesale rule omission."
    minimum_fix: "Apply deletion test after every new rule addition; cap file at model ceiling."
    evidence_ref: F-06

  - id: AP-02
    pattern_name: "Governance File as Live Context"
    what_fails: "Loading rules-about-rules into the active context window introduces a second layer of meta-directives that conflict with object-level rules."
    minimum_fix: "Load this file into orchestrator context only; sub-agents receive compiled directives, not this reference."
    evidence_ref: F-02

  - id: AP-03
    pattern_name: "Knowledge Embedded in Directives"
    what_fails: "Domain facts hidden inside imperative statements obscure sub-rules and create instruction-count inflation."
    minimum_fix: "Move all knowledge content to a knowledge_base file; directives reference it by ID."
    evidence_ref: F-01, F-02

  - id: AP-04
    pattern_name: "Duplicate Paraphrase Rules"
    what_fails: "Semantically identical rules phrased differently across sections create contradiction drift and inflate directive count."
    minimum_fix: "Assign each rule a unique ID; search for semantic duplicates before committing."
    evidence_ref: F-02, F-06

  - id: AP-05
    pattern_name: "Modal Hedging"
    what_fails: "Directives using should/may/might/could are treated as optional by the model, making enforcement unreliable."
    minimum_fix: "Replace all modal verbs with imperative forms (do, return, halt, validate)."
    evidence_ref: F-06

  - id: AP-06
    pattern_name: "No Stop Conditions"
    what_fails: "Agent loops or fabricates outputs when no halt criterion is defined for ambiguous or failed states."
    minimum_fix: "Add explicit stop_and_escalate block with error codes to every workflow and system_prompt."
    evidence_ref: F-02

  - id: AP-07
    pattern_name: "Mid-Document Critical Rules"
    what_fails: "Rules placed past the first 500 tokens suffer 30–50% compliance reduction due to positional attention decay."
    minimum_fix: "Move all critical-tier directives to within the first 500 tokens."
    evidence_ref: F-04

  - id: AP-08
    pattern_name: "Recursive Governance"
    what_fails: "Audit files that reference other audit files create circular dependency chains; a single rule change triggers cascade rewrites."
    minimum_fix: "Governance reference lives in one file only; no file audits this file."
    evidence_ref: F-02

  - id: AP-09
    pattern_name: "Mixed-Type Monolith"
    what_fails: "A single file mixing system_prompt, knowledge_base, workflow, and tool_definition creates context clash and prevents targeted reloading."
    minimum_fix: "Split into four typed files following FILE TYPE TAXONOMY; load each at correct frequency."
    evidence_ref: F-02, F-05
```

```yaml
# ════════════════════════════════════════════════════════════════
# SECTION 6 — MINIMAL VIABLE FILE TEST
# ════════════════════════════════════════════════════════════════
minimal_viable_file_test:

  - check_id: MVT-01
    question: "Are all critical-tier directives located within the first 500 tokens?"
    fail_action: "Move critical directives to document start before marking load-ready."

  - check_id: MVT-02
    question: "Is the total directive count at or below the ceiling for the target model?"
    fail_action: "Run deletion test; remove lowest-impact directives until at or below ceiling."

  - check_id: MVT-03
    question: "Does the file contain content from exactly one file type (system_prompt / knowledge_base / workflow / tool_definition)?"
    fail_action: "Split file into typed components; load each independently."

  - check_id: MVT-04
    question: "Does every directive use an imperative verb with no modal hedging and carry an inline tier tag?"
    fail_action: "Rewrite non-compliant directives before loading."
```

```yaml
# ════════════════════════════════════════════════════════════════
# SECTION 7 — QUICK REFERENCE
# ════════════════════════════════════════════════════════════════
quick_reference:

  directive_ceilings_by_model:
    gpt_4o:                          50
    claude_3_7_sonnet_standard:      50
    claude_3_7_sonnet_reasoning:     80
    gemini_2_5_pro:                 100
    o3:                             100

  token_budgets_by_file_type:
    system_prompt:       2000
    knowledge_base:    100000
    workflow:            4000
    tool_definition:     1000

  position_rules:
    - "Critical directives: first 500 tokens (73% compliance vs 30-50% mid-doc)"
    - "Primacy > recency > middle for all rule placement"
    - "Re-inject critical block at session restart or after context drift detection"

  format_rules:
    - "Use YAML for instruction delivery (15-56% token savings over JSON)"
    - "Use JSON Schema strict:true for all machine-consumed structured outputs"
    - "Limit examples to ≤2 per ambiguous rule; zero examples for clear rules"

  forbidden_patterns:
    - "should / may / might / could in any directive"
    - "knowledge content inside directive blocks"
    - "duplicate rules with paraphrase across sections"
    - "governance files loaded as live sub-agent context"
    - "missing stop_and_escalate conditions in workflows"
    - "mixed file types in a single file"
    - "critical directives placed past token position 500"
    - "recursive audit file chains"
    - "directive count exceeding model-specific ceiling"
    - "inline priority legend instead of per-rule inline tags"
```
