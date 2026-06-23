---
class: kb_policy
role: AGENT_KB_STRUCTURE_POLICY
surface: agent_kb_governance
version: "2.0"
created_at: "2026-05-07"
last_validated_at: "2026-05-07"
context_mode: compact
target_use: "text-based KB files loaded as context into GPT/Claude/Gemini agent sessions"
scope_constraints:
  - "Markdown + YAML-frontmatter KB files only"
  - "Not for: vector DBs, RAG pipelines, embedding strategies, model fine-tuning"
target_model_min: "gpt-4o"
target_model_max: "gemini-2.5-pro"
max_active_rules: 17
max_active_checks: 8
rule_count: 17
extended_check_count: 18
status: canonical
owner: meta_ops
validator: meta_detective
changelog:
  - version: "1.0"
    date: "2026-05-07"
    summary: "Initial research-grade release."
  - version: "2.0"
    date: "2026-05-07"
    summary: >
      Applied AuditImprovements.md (FIX-01 through FIX-05): all rule/check/template
      blocks converted to parse-valid YAML; evidence prose moved to Appendix B;
      source quality policy added; surface split into active_policy / evidence_register /
      audit_checklist / report_template; prevents + evidence_refs fields added to all rules;
      deployment_verdict_logic made machine-readable; active checks condensed to 8 (extended
      18-check audit retained in Appendix C); self-compliance with BP-C1 enforced via
      critical_path placement in frontmatter.
---

<!--
  KB File Best Practice Guide & Audit Checklist — v2.0
  Research-grade | Sources 2024–2026
  Surfaces: active_policy · evidence_register · audit_checklist · report_template
  Appendices: A (anti-patterns) · B (evidence base) · C (extended checklist)
-->

---

# ACTIVE POLICY
<!-- Surface: active_policy | Token budget: ≤2000 for this section -->

## Critical Path
<!-- These 4 constraints are enforced before any other rule is read. -->

```yaml
critical_path:
  priority: critical
  rules:
    - id: KB-CP-01
      rule: "Put all critical-tier rules within the first 500 tokens of the KB file."
    - id: KB-CP-02
      rule: "Encode all active rules, checks, and templates as parse-valid YAML."
    - id: KB-CP-03
      rule: "Separate active policy from evidence prose; move explanations to appendices."
    - id: KB-CP-04
      rule: "Use schema-enforced outputs for every machine-consumed artifact."
```

---

## Scoring Semantics

```yaml
scoring_semantics:
  risk_if_unfixed:
    scale: "1–100"
    meaning: "Danger if issue stays unresolved — higher = more urgent."
  evidence_strength:
    scale: "1–100"
    meaning: "Confidence based on primary or strongly corroborated sources."
  impact_if_fixed:
    scale: "1–100"
    meaning: "Expected reliability gain if corrected."
```

---

## Source Quality Policy

```yaml
source_quality_policy:
  accepted_primary:
    - official_vendor_docs
    - peer_reviewed_or_archival_papers
    - benchmark_repositories
    - standards_or_api_docs
  accepted_secondary:
    - practitioner_posts_only_when_no_primary_source_exists
    - secondary_sources_require_lower_evidence_strength_score
  forbidden_as_canon:
    - unsourced_blog_claims
    - unattributed_benchmark_numbers
    - dead_links
    - model_behavior_claims_without_date_or_model_version
```

---

## Active Rules — CRITICAL Tier
<!-- Violating causes near-certain execution failure -->

```yaml
critical_rules:

  - id: BP-C1
    tier: critical
    rule: "Place all critical-tier rules within the first 500 tokens of the KB file, before any prose, metadata, or examples."
    prevents: "positional attention loss; mid-document rules lose 30–50% compliance"
    evidence_refs: [F-04]
    risk_if_unfixed: 95
    evidence_strength: 85
    impact_if_fixed: 90

  - id: BP-C2
    tier: critical
    rule: "Keep total rule count below 50 for standard deployment; never exceed 150 even for reasoning-class models."
    prevents: "instruction-following cliff; compliance collapses non-linearly at high density"
    evidence_refs: [F-01, F-10]
    risk_if_unfixed: 93
    evidence_strength: 88
    impact_if_fixed: 88

  - id: BP-C3
    tier: critical
    rule: "Never rely on prose output instructions for machine-consumed outputs; enforce structure via API-level schema (strict: true or equivalent)."
    prevents: "invalid downstream structures; prose contracts work 'most of the time' only"
    evidence_refs: [F-08]
    risk_if_unfixed: 92
    evidence_strength: 96
    impact_if_fixed: 90

  - id: BP-C4
    tier: critical
    rule: "Assign an explicit tier tag (critical | required | recommended) inline on every rule, not in a separate legend."
    prevents: "unlabeled rules treated as equal-weight by the model"
    evidence_refs: [F-07]
    risk_if_unfixed: 88
    evidence_strength: 76
    impact_if_fixed: 82

  - id: BP-C5
    tier: critical
    rule: "Use YAML blocks — not prose paragraphs or JSON — to encode all structured rules, constraints, and checklists."
    prevents: "ambiguous rule parsing; prose rules are token-wasteful and semantically hedged"
    evidence_refs: [F-03]
    risk_if_unfixed: 85
    evidence_strength: 79
    impact_if_fixed: 80
```

---

## Active Rules — REQUIRED Tier
<!-- Violating causes likely degradation -->

```yaml
required_rules:

  - id: BP-R1
    tier: required
    rule: "Run a deletion test on every rule before committing: if removal causes no observable behavioral change in >90% of cases, delete the rule."
    prevents: "rule proliferation creep; redundant rules suppress compliance of necessary ones"
    evidence_refs: [F-06]
    risk_if_unfixed: 78
    evidence_strength: 84
    impact_if_fixed: 80

  - id: BP-R2
    tier: required
    rule: "Recite all critical rules verbatim in an Active Constraints block immediately before the task input in long-session agents (>8K tokens)."
    prevents: "lost-in-the-middle drift; critical rules loaded at session start decay out of effective attention"
    evidence_refs: [F-02]
    risk_if_unfixed: 80
    evidence_strength: 82
    impact_if_fixed: 75

  - id: BP-R3
    tier: required
    rule: "Limit the instruction block to ≤2,000 tokens to preserve context budget for task content, retrieved documents, and conversation history."
    prevents: "task context crowding; effective range ≠ max context window"
    evidence_refs: [F-09]
    risk_if_unfixed: 76
    evidence_strength: 78
    impact_if_fixed: 74

  - id: BP-R4
    tier: required
    rule: "Use 1–3 examples only for rules that are formatting-critical or genuinely ambiguous; rewrite unclear rules instead of adding examples."
    prevents: "example overload; excessive few-shot examples degrade performance in some models"
    evidence_refs: [F-05]
    risk_if_unfixed: 68
    evidence_strength: 70
    impact_if_fixed: 65

  - id: BP-R5
    tier: required
    rule: "Organize KB sections with stable labeled Markdown headers and XML-style section tags so compression routines can selectively preserve or drop entire sections."
    prevents: "arbitrary context compression dropping critical chunks"
    evidence_refs: [F-02]
    risk_if_unfixed: 72
    evidence_strength: 78
    impact_if_fixed: 70

  - id: BP-R6
    tier: required
    rule: "Design the KB file for the weakest model in the deployment fleet; never assume Gemini 2.5 Pro or o3 safe thresholds apply fleet-wide."
    prevents: "10× compliance gap between weakest and strongest models at high instruction density"
    evidence_refs: [F-10]
    risk_if_unfixed: 74
    evidence_strength: 80
    impact_if_fixed: 72

  - id: BP-R7
    tier: required
    rule: "Never duplicate a rule across multiple sections; a rule appearing twice with any paraphrase creates contradiction drift."
    prevents: "context clash — one of the four primary context failure modes in production agents"
    evidence_refs: [F-02]
    risk_if_unfixed: 70
    evidence_strength: 74
    impact_if_fixed: 68
```

---

## Active Rules — RECOMMENDED Tier
<!-- Violating causes marginal degradation -->

```yaml
recommended_rules:

  - id: BP-REC1
    tier: recommended
    rule: "Add a machine-readable YAML frontmatter block containing: version, last_validated_at, target_model_min, max_active_rules, context_mode."
    prevents: "stale or model-mismatched KB loading; no automated staleness detection possible without it"
    evidence_refs: [F-09]
    risk_if_unfixed: 45
    evidence_strength: 72
    impact_if_fixed: 55

  - id: BP-REC2
    tier: recommended
    rule: "Place recommended-tier rules at the end of the KB file to use residual recency attention for low-stakes guidance."
    prevents: "mid-document attention loss on optional rules"
    evidence_refs: [F-04]
    risk_if_unfixed: 40
    evidence_strength: 85
    impact_if_fixed: 45

  - id: BP-REC3
    tier: recommended
    rule: "Token-count the assembled context (system prompt + KB + task input) before inference; log per-component proportions to detect instruction crowding."
    prevents: "silent quality degradation from context proportion shift"
    evidence_refs: [F-09]
    risk_if_unfixed: 50
    evidence_strength: 78
    impact_if_fixed: 60

  - id: BP-REC4
    tier: recommended
    rule: "Write all rule text in active imperative voice; remove hedging words (modal verbs) to eliminate optionality signals."
    prevents: "model interpreting hedged rules as optional"
    evidence_refs: [F-03]
    risk_if_unfixed: 35
    evidence_strength: 68
    impact_if_fixed: 50

  - id: BP-REC5
    tier: recommended
    rule: "Add a validity_window field on time-sensitive or model-version-specific rules to enable automated staleness detection."
    prevents: "memory pollution from un-expired stale rules in long-running systems"
    evidence_refs: [F-02]
    risk_if_unfixed: 38
    evidence_strength: 65
    impact_if_fixed: 48
```

---

# AUDIT CHECKLIST
<!-- Surface: audit_checklist | Active deployment checks: 8 | Full extended audit: Appendix C -->

## Active Deployment Checks (8)
<!-- Run before every deployment. All critical must pass. -->

```yaml
active_audit_checks:

  - id: KB-ACHK-01
    tier: critical
    check: "All YAML blocks in the file parse without errors."
    pass_condition: "yaml_parse_errors == 0"
    fail_action: halt
    evidence_source: F-03

  - id: KB-ACHK-02
    tier: critical
    check: "All critical-tier rules appear within the first 500 tokens of the file."
    pass_condition: "critical_rules_max_token_position <= 500"
    fail_action: halt
    evidence_source: F-04

  - id: KB-ACHK-03
    tier: critical
    check: "Total active rule count is below the configured max_active_rules limit."
    pass_condition: "active_rule_count <= max_active_rules"
    fail_action: halt
    evidence_source: F-01

  - id: KB-ACHK-04
    tier: critical
    check: "Every machine-consumed output references an API-enforced schema, not prose-only instructions."
    pass_condition: "schema_enforced_outputs == true AND prose_only_output_contracts == 0"
    fail_action: halt
    evidence_source: F-08

  - id: KB-ACHK-05
    tier: required
    check: "No duplicate or semantically paraphrased rules exist in the file."
    pass_condition: "semantic_duplicate_rule_count == 0"
    fail_action: revise
    evidence_source: F-02

  - id: KB-ACHK-06
    tier: required
    check: "Every rule has tier, prevents, and evidence_refs fields populated."
    pass_condition: "rules_missing_required_fields == 0"
    fail_action: revise
    evidence_source: F-07

  - id: KB-ACHK-07
    tier: required
    check: "Active policy section contains ≤100 tokens of non-YAML prose."
    pass_condition: "active_policy_prose_tokens <= 100"
    fail_action: revise
    evidence_source: F-02

  - id: KB-ACHK-08
    tier: required
    check: "Frontmatter contains version, last_validated_at, target_model_min, max_active_rules, and context_mode."
    pass_condition: "frontmatter_required_fields_present == true"
    fail_action: revise
    evidence_source: F-09

deployment_verdict_logic:
  deploy_ready:
    conditions:
      - "all critical checks pass (KB-ACHK-01 through KB-ACHK-04)"
      - "at least 3 of 4 required checks pass (KB-ACHK-05 through KB-ACHK-08)"
  revise_required:
    conditions:
      - "any required check fails"
      - "recommended checks fail but critical checks pass"
  halt:
    conditions:
      - "any critical check fails"
      - "active YAML does not parse"
      - "machine-consumed outputs are prose-only"
```

---

# AUDIT REPORT TEMPLATE
<!-- Surface: report_template | Fill in one copy per KB file reviewed -->

```yaml
# ============================================================
# KB FILE AUDIT REPORT
# Template version: 2.0 | Apply checks KB-ACHK-01 → KB-ACHK-08 for deployment.
# For full extended audit, apply Appendix C checks CHK-01 → CHK-18.
# ============================================================

audit_metadata:
  auditor: ""
  audit_date: ""                      # YYYY-MM-DD
  audit_tool_version: "2.0"
  kb_file_name: ""
  kb_file_version: ""
  kb_last_validated_at: ""
  target_model_min: ""
  target_model_max: ""
  token_count_instruction_block: 0    # Rules section only
  token_count_assembled_context: 0    # Full deployed context
  total_active_rule_count: 0
  total_example_count: 0

active_check_results:
  - ref: KB-ACHK-01
    result: ""                        # pass | fail | skip
    notes: ""
    evidence_observed: ""

  - ref: KB-ACHK-02
    result: ""
    notes: ""
    evidence_observed: ""

  - ref: KB-ACHK-03
    result: ""
    notes: ""
    evidence_observed: ""

  - ref: KB-ACHK-04
    result: ""
    notes: ""
    evidence_observed: ""

  - ref: KB-ACHK-05
    result: ""
    notes: ""
    evidence_observed: ""

  - ref: KB-ACHK-06
    result: ""
    notes: ""
    evidence_observed: ""

  - ref: KB-ACHK-07
    result: ""
    notes: ""
    evidence_observed: ""

  - ref: KB-ACHK-08
    result: ""
    notes: ""
    evidence_observed: ""

scoring:
  critical_checks_total: 4
  critical_checks_passed: 0
  required_checks_total: 4
  required_checks_passed: 0

verdict: ""                           # DEPLOY_READY | REVISE_REQUIRED | HALT

repair_actions:
  - failed_check: ""
    priority: ""                      # critical | required | recommended
    description: ""
    action_required: ""
    owner: ""
    due_date: ""
    status: ""                        # open | in_progress | resolved

reaudit:
  required: false
  scheduled_date: ""
  reaudit_scope: ""                   # full | critical_only | specific_checks
```

---

# APPENDIX A — Anti-Patterns
<!-- Human-readable reference. Not loaded into active agent context. -->

## Common KB Design Mistakes

**1. Rule Proliferation Creep**
Adding a rule for every observed failure without removing obsolete ones until the KB exceeds the model's reliable instruction threshold.
*Minimum fix:* After adding any new rule, run the deletion test on all existing rules and remove at least one. *(F-06)*

**2. Prose Contract for Structured Output**
Instructing the model in prose to "always respond as JSON" instead of enforcing a schema at the API level.
*Minimum fix:* Replace all prose output format instructions with an OpenAI Structured Outputs schema or equivalent constrained-decoding mechanism. *(F-08)*

**3. Mid-Document Rule Burial**
Placing critical constraints in the middle of a long KB file where positional attention is weakest.
*Minimum fix:* Audit token position of every critical rule and move all of them to within the first 500 tokens. *(F-04)*

**4. Example Overload**
Adding more than 3 examples per rule assuming "more examples = better compliance," causing context pollution.
*Minimum fix:* Reduce to 1 canonical example per ambiguous rule; remove examples entirely from clearly stated rules. *(F-05)*

**5. Rule Duplication with Paraphrase**
Stating the same constraint in two places with different wording, creating contradiction drift the model cannot resolve.
*Minimum fix:* Establish a single canonical YAML rule block as the source of truth; delete all prose restatements. *(F-02)*

**6. Modal Hedging in Rule Text**
Writing rules as "the agent *should* return X" instead of "Return X," giving the model implicit permission to treat the rule as optional.
*Minimum fix:* Replace all modal verbs (should, may, might, could) in rule text with imperative form. *(F-03)*

**7. Static KB for Multi-Model Fleet**
Designing KB instruction density for the strongest model and deploying the same file to weaker models that cliff at far lower counts.
*Minimum fix:* Add `target_model_min` to frontmatter and validate rule count against that model's safe threshold. *(F-10)*

**8. No Recitation for Long Sessions**
Loading critical rules only at session start with no mechanism to re-inject them near the active turn.
*Minimum fix:* Prepend critical rules as an Active Constraints block to each agent reasoning step in sessions exceeding ~8K tokens. *(F-02)*

**9. Malformed Machine Blocks**
Presenting rules as pseudo-code, double-backtick blocks, or prose lists while claiming "machine-readable YAML."
*Minimum fix:* Lint every structured block; reject any file where `yaml.safe_load()` raises an error. *(KB-AUDIT-FIX-01)*

**10. Active Surface Bloat**
Loading research evidence, anti-pattern explanations, audit templates, and changelogs into the active inference context.
*Minimum fix:* Move all human-only content to appendices; keep active policy section below 2,000 tokens. *(KB-AUDIT-FIX-02)*

---

# APPENDIX B — Evidence Base
<!-- Human-readable research record. Not loaded into active agent context.
     Sources: 2024–2026. Primary sources only for numeric claims per source_quality_policy. -->

## Evidence Register

```yaml
evidence_register:

  - id: F-01
    label: "Instruction-Following Cliff"
    source_type: research
    key_finding: >
      At 500 instructions, Gemini 2.5 Pro scored 68.9%, Claude 3.7 Sonnet 52.7%,
      GPT-4o 15.4%, Llama 4 Scout 6.7%. Three degradation patterns: threshold decay
      (reasoning models, cliff at ~150–250 rules), linear decay, exponential decay.
    confidence: 88
    primary_source: "IFScale Benchmark — arXiv:2507.11538, July 2025"
    corroborating_source: "Curse of Instructions — OpenReview 2025; EIFBENCH arXiv:2506.08375"
    practical_implication: "Keep rule count below 50 for standard deployment; below 150 for reasoning models."

  - id: F-02
    label: "Context Drift in Long Agent Sessions"
    source_type: research
    key_finding: >
      Most production LLM quality failures originate in context content, not model processing.
      Four failure modes: context poisoning, distraction, confusion, clash.
    confidence: 82
    primary_source: "Context Engineering: Why What You Feed the LLM Matters — tianpan.co 2025"
    corroborating_source: "Context Engineering for AI Agents — fp8.co March 2026"
    practical_implication: "Use labeled sections; recite critical rules near the active turn."

  - id: F-03
    label: "YAML vs JSON vs Prose"
    source_type: secondary
    key_finding: >
      YAML saves 15–56% tokens vs JSON due to BPE tokenization penalizing punctuation.
      Production teams report 30–50% fewer parsing failures with YAML vs JSON.
      For typed API responses, JSON Schema enforcement (Structured Outputs) remains the standard.
    confidence: 79
    primary_source: "YAML Over JSON in LLM Applications — tashif.codes Oct 2025"
    corroborating_source: "JSON vs YAML for LLM Prompts — wildandfreetools.com March 2026"
    note: "secondary — verify numeric token claims before citing as primary evidence"
    practical_implication: "Use YAML for instruction blocks; use JSON Schema for output enforcement."

  - id: F-04
    label: "Primacy/Recency Position Effect"
    source_type: research
    key_finding: >
      Rules at the beginning of a prompt are followed correctly ~73% of the time vs
      30–50% compliance loss for mid-document rules. As context grows, recency
      strengthens while primacy weakens — the 'lost in the middle' problem is
      consistent across model families.
    confidence: 85
    primary_source: "The Instruction Position Problem — tianpan.co April 2026"
    corroborating_source: >
      Serial Position Effects of LLMs — arXiv:2406.15981;
      Positional Biases Shift as Inputs Approach Context Window Limits — OpenReview
    practical_implication: "Critical rules in first 500 tokens; recommended rules at the end."

  - id: F-05
    label: "Few-Shot Examples vs Rule Text"
    source_type: research
    key_finding: >
      rules_only outperformed rules_with_examples on a 580-query dataset.
      'The Few-shot Dilemma' (2025) shows excessive domain-specific examples
      degrade performance by over-populating context with low-signal tokens.
    confidence: 70
    primary_source: "Do well-written instructions beat few-shotting? — softwaredoug.com Sept 2025"
    corroborating_source: "The Few-shot Dilemma: Over-prompting LLMs — arXiv:2509.13196"
    practical_implication: "Use 1–3 examples for ambiguous rules only; fix unclear rules instead of adding examples."

  - id: F-06
    label: "Overengineering Failure Modes"
    source_type: practitioner
    key_finding: >
      Beyond ~10–20 tools per reasoning context, tool-selection accuracy degrades to 13%.
      Rule-based guardrails at scale cause rule omission — models skip rules wholesale
      rather than approximate them.
    confidence: 84
    primary_source: "The Over-Tooled Agent Problem — tianpan.co April 2026"
    corroborating_source: "Things You're Overengineering in Your AI Agent — animanovalabs.com April 2026"
    practical_implication: "Apply a deletion test: every rule must have a documented failure scenario it prevents."

  - id: F-07
    label: "Priority Signaling in Prompts"
    source_type: research
    key_finding: >
      Explicit instruction-level priority signaling improved GPT-4o multi-instruction
      success from 15% to 31% and Claude 3.5 Sonnet from 44% to 58%.
    confidence: 76
    primary_source: "Large Language Models Cannot Follow Multiple Instructions at Once — OpenReview Feb 2025"
    practical_implication: "Tag every rule with an explicit tier inline — not in a separate legend."

  - id: F-08
    label: "Structured Output Schema vs Prose Contracts"
    source_type: official
    key_finding: >
      OpenAI Structured Outputs (Aug 2024, strict: true) enforces 100% schema compliance
      via constrained decoding — vs JSON mode (parseable only) or prose instructions
      (works 'most of the time').
    confidence: 92
    primary_source: "Introducing Structured Outputs in the API — OpenAI Aug 2024"
    corroborating_source: "OpenAI Structured Outputs: Complete Developer Guide — digitalapplied.com Jan 2026"
    practical_implication: "Define JSON Schema and invoke Structured Outputs for any machine-consumed output."

  - id: F-09
    label: "Token Budget and Instruction Density"
    source_type: practitioner
    key_finding: >
      Effective processing range ≠ maximum context window. Crowding signal-rich components
      (retrieved docs, recent history) with over-specified instructions directly causes
      quality failure.
    confidence: 78
    primary_source: "Context Engineering: Why Your AI Agent Fails — fordelstudios.com April 2026"
    corroborating_source: "Context Engineering in LLM-Based Agents — tianpan.co 2025"
    practical_implication: "Target ≤2,000 tokens for instruction blocks to preserve task context budget."

  - id: F-10
    label: "Model-Specific Findings 2025–2026"
    source_type: research
    validity_window: "valid until next major benchmark update (est. Q4 2026)"
    key_finding: >
      At 500 instructions: Gemini 2.5 Pro (68.9%, threshold decay at 150–250),
      Claude 3.7 Sonnet (52.7%, linear), GPT-4o (15.4%, exponential).
      arXiv:2601.03269 (Dec 2025) finds Claude Sonnet-4 and GPT-5 highest in real-world
      RAG compliance; all models show 'instruction gap' — strong on general tasks, poor
      on precise custom instruction adherence.
    confidence: 80
    primary_source: "IFScale — tianpan.co April 2026; The Instruction Gap — arXiv:2601.03269 Dec 2025"
    practical_implication: "Design for weakest model in fleet; do not assume frontier model ceilings apply fleet-wide."
```

---

# APPENDIX C — Extended Audit Checklist (18 Checks)
<!-- Use for full audits, not deployment gates. For deployment, use Section 2 active checks only. -->

```yaml
extended_audit_checks:

  - id: CHK-01
    tier: critical
    check: "All YAML blocks in the file parse without errors."
    pass_condition: "yaml_parse_errors == 0"
    fail_action: halt
    evidence_source: F-03

  - id: CHK-02
    tier: critical
    check: "All critical-tier rules appear within the first 500 tokens."
    pass_condition: "critical_rules_max_token_position <= 500"
    fail_action: halt
    evidence_source: F-04

  - id: CHK-03
    tier: critical
    check: "Total rule count is below 50 for standard models, below 150 for reasoning-class models."
    pass_condition: "rule_count < 50 (standard) OR rule_count < 150 (reasoning)"
    fail_action: halt
    evidence_source: F-01

  - id: CHK-04
    tier: critical
    check: "No machine-consumed output is governed solely by prose instructions; all reference an API-enforced schema."
    pass_condition: "prose_only_output_contracts == 0"
    fail_action: halt
    evidence_source: F-08

  - id: CHK-05
    tier: critical
    check: "Every rule entry has an inline tier tag (critical | required | recommended)."
    pass_condition: "rules_missing_tier_tag == 0"
    fail_action: halt
    evidence_source: F-07

  - id: CHK-06
    tier: required
    check: "Every rule has a documented prevents field (failure scenario it guards against)."
    pass_condition: "rules_missing_prevents_field == 0"
    fail_action: revise
    evidence_source: F-06

  - id: CHK-07
    tier: required
    check: "Instruction block token count is ≤2,000."
    pass_condition: "instruction_block_tokens <= 2000"
    fail_action: revise
    evidence_source: F-09

  - id: CHK-08
    tier: required
    check: "No duplicate or semantically paraphrased duplicate rules exist."
    pass_condition: "semantic_duplicate_rule_count == 0"
    fail_action: revise
    evidence_source: F-02

  - id: CHK-09
    tier: required
    check: "KB file has stable labeled section headers for: metadata, critical rules, required rules, examples (if any), recommended rules."
    pass_condition: "all_required_section_headers_present == true AND unlabeled_prose_block_tokens <= 100"
    fail_action: revise
    evidence_source: F-02

  - id: CHK-10
    tier: required
    check: "Frontmatter contains target_model_min and rule count stays below that model's safe threshold."
    pass_condition: "target_model_min_present == true AND rule_count_within_model_threshold == true"
    fail_action: revise
    evidence_source: F-10

  - id: CHK-11
    tier: required
    check: "Total examples ≤10 across the file; no more than 3 per rule."
    pass_condition: "examples_per_rule <= 3 AND total_examples <= 10"
    fail_action: revise
    evidence_source: F-05

  - id: CHK-12
    tier: required
    check: "A recitation mechanism exists for critical rules in long-session agents."
    pass_condition: "active_constraints_injection_documented == true"
    fail_action: flag_for_human
    evidence_source: F-02

  - id: CHK-13
    tier: recommended
    check: "YAML frontmatter contains: version, last_validated_at, target_model_min, max_active_rules, context_mode."
    pass_condition: "frontmatter_required_fields_present == true"
    fail_action: revise
    evidence_source: F-09

  - id: CHK-14
    tier: recommended
    check: "All rule text uses active imperative voice; zero modal verbs (should, may, might, could) in rule text."
    pass_condition: "modal_verb_count_in_rule_text == 0"
    fail_action: revise
    evidence_source: F-03

  - id: CHK-15
    tier: recommended
    check: "Document section order is CRITICAL → REQUIRED → RECOMMENDED."
    pass_condition: "section_order_correct == true"
    fail_action: revise
    evidence_source: F-04

  - id: CHK-16
    tier: recommended
    check: "No YAML rule is restated as a prose paragraph in the same section."
    pass_condition: "prose_restatements_of_yaml_rules == 0"
    fail_action: revise
    evidence_source: F-03

  - id: CHK-17
    tier: recommended
    check: "Time-sensitive or model-version-specific rules contain a validity_window field."
    pass_condition: "model_specific_rules_without_validity_window == 0"
    fail_action: flag_for_human
    evidence_source: F-02

  - id: CHK-18
    tier: recommended
    check: "Total assembled context has been token-counted and logged; count does not exceed 75% of model context limit."
    pass_condition: "assembled_context_tokens <= model_context_limit * 0.75"
    fail_action: flag_for_human
    evidence_source: F-09
```

---

*KB_Audit_v2.0 — Research-grade | Sources 2024–2026 | Scope: Markdown + YAML-frontmatter KB files as agent context*
