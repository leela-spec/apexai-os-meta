---
class: construction_guide
role: MACHINE_READABLE_FILE_CONSTRUCTION_STANDARD
surface: active_policy
version: "1.0"
created_at: "2026-05-09"
last_validated_at: "2026-05-09"
status: canonical
target_use: "building Markdown + YAML-frontmatter KB files loaded as context into agent sessions"
scope_constraints:
  - "Markdown + YAML-frontmatter KB files only"
  - "Not for vector databases, RAG pipelines, embedding strategies, or model fine-tuning"
context_mode: compact
target_model_min: "gpt-4o"
max_active_rules: 12
max_active_checks: 8
source_files:
  - canonical_name: "01-KB_Audit_v2.md"
    uploaded_name: "KB_Audit_v2.md"
    authority: 1
  - canonical_name: "02-AuditImprovements.md"
    uploaded_name: "AuditImprovements.md"
    authority: 2
  - canonical_name: "03-ConstructionGuide_From_KB_Audit_V2.md"
    uploaded_name: "ConstructionGuide_From_KB_Audit_V2.md"
    authority: 3
---

# ACTIVE CONSTRUCTION STANDARD

```yaml
construction_standard:
  purpose: Define the target shape of a valid machine-readable KB file.
  file_type: single Markdown document with YAML frontmatter
  active_surface: compact parse-valid YAML
  human_surface: appendix only
  active_rule_limit: 12
  active_check_limit: 8
critical_path:
  priority: critical
  rule_ids:
    - KB-C01
    - KB-C02
    - KB-C03
    - KB-C04
    - KB-C05
active_rule_schema:
  required_fields:
    - id
    - tier
    - rule
    - prevents
    - evidence_refs
    - validation
  allowed_tiers:
    - critical
    - required
    - recommended
  optional_fields:
    - validity_window
  validity_window_use: only for time-sensitive or model-version-specific guidance
active_rules:
  - id: KB-C01
    tier: critical
    rule: Place all critical rules in the first 500 tokens of active policy.
    prevents: positional attention loss
    evidence_refs:
      - F-04
    validation:
      pass_condition: critical_rules_max_token_position <= 500
      fail_action: halt
  - id: KB-C02
    tier: critical
    rule: Encode active rules, checks, and templates as parse-valid YAML.
    prevents: false machine-readability
    evidence_refs:
      - F-03
      - KB-AUDIT-FIX-01
    validation:
      pass_condition: yaml_parse_errors == 0
      fail_action: halt
  - id: KB-C03
    tier: critical
    rule: Separate active policy from evidence prose and human explanations.
    prevents: active context bloat
    evidence_refs:
      - F-02
      - KB-AUDIT-FIX-02
      - KB-AUDIT-FIX-05
    validation:
      pass_condition: active_policy_prose_tokens <= 100
      fail_action: halt
  - id: KB-C04
    tier: critical
    rule: Use schema-enforced contracts for every machine-consumed output.
    prevents: invalid downstream structures
    evidence_refs:
      - F-08
    validation:
      pass_condition: schema_enforced_outputs == true AND prose_only_output_contracts == 0
      fail_action: halt
  - id: KB-C05
    tier: critical
    rule: Give every rule an inline tier of critical, required, or recommended.
    prevents: unprioritized rule accumulation
    evidence_refs:
      - F-07
    validation:
      pass_condition: rules_missing_tier == 0
      fail_action: halt
  - id: KB-R01
    tier: required
    rule: Keep active rule count at or below max_active_rules.
    prevents: instruction-density failure
    evidence_refs:
      - F-01
      - F-10
    validation:
      pass_condition: active_rule_count <= max_active_rules
      fail_action: halt
  - id: KB-R02
    tier: required
    rule: Give each active rule exactly one canonical location.
    prevents: semantic duplicate drift
    evidence_refs:
      - F-02
    validation:
      pass_condition: semantic_duplicate_rule_count == 0
      fail_action: fail
  - id: KB-R03
    tier: required
    rule: Use examples only for formatting-critical or genuinely ambiguous cases.
    prevents: example overload
    evidence_refs:
      - F-05
    validation:
      pass_condition: examples_per_rule <= 3 AND examples_have_format_or_ambiguity_need == true
      fail_action: fail
  - id: KB-R04
    tier: required
    rule: Design rule density for the weakest declared target model.
    prevents: model-mismatched KB loading
    evidence_refs:
      - F-10
    validation:
      pass_condition: target_model_min_present == true AND active_rule_count <= max_active_rules
      fail_action: fail
  - id: KB-R05
    tier: required
    rule: Use stable short Markdown headings for the required body sections.
    prevents: unbounded section ambiguity
    evidence_refs:
      - F-02
    validation:
      pass_condition: required_body_sections_present == true
      fail_action: fail
  - id: KB-REC01
    tier: recommended
    rule: Write rule text in direct imperative form without hedging words.
    prevents: optional interpretation of mandatory guidance
    evidence_refs:
      - F-03
    validation:
      pass_condition: modal_verb_count_in_rule_text == 0
      fail_action: flag
  - id: KB-REC02
    tier: recommended
    rule: Place recommended rules after critical and required rules.
    prevents: low-priority guidance occupying high-priority positions
    evidence_refs:
      - F-04
    validation:
      pass_condition: tier_order == critical_required_recommended
      fail_action: flag
required_file_structure:
  order:
    - yaml_frontmatter
    - active_construction_standard
    - minimal_valid_file_template
    - appendix_human_reference_only
  sections:
    yaml_frontmatter:
      required: true
      format: YAML between opening and closing document markers
    active_construction_standard:
      required: true
      format: one YAML block containing active policy
      prose_limit_tokens: 100
    minimal_valid_file_template:
      required: true
      format: one compact example with parse-valid frontmatter and active YAML
    appendix_human_reference_only:
      required: true
      loaded_as_active_context: false
required_frontmatter_fields:
  class:
    required: true
    value_type: string
  role:
    required: true
    value_type: string
  surface:
    required: true
    value_type: string
  version:
    required: true
    value_type: string
  created_at:
    required: true
    value_type: date_string
  last_validated_at:
    required: true
    value_type: date_string
  status:
    required: true
    value_type: string
  target_use:
    required: true
    value_type: string
  scope_constraints:
    required: true
    value_type: list_of_strings
  context_mode:
    required: true
    value_type: string
  target_model_min:
    required: true
    value_type: string
  max_active_rules:
    required: true
    value_type: integer
  max_active_checks:
    required: true
    value_type: integer
  source_files:
    required: true
    value_type: list
output_contract_rules:
  machine_consumed_outputs:
    required: true
    contract_type: API-level schema or equivalent constrained decoding
    prose_only_contract_allowed: false
  templates:
    required: true
    parseable_structure: true
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
appendix_policy:
  active_context: false
  allowed_content:
    - anti_patterns
    - evidence_notes
    - extended_checklists
    - source_discussion
  required_marker: HUMAN REFERENCE ONLY
validation_gates:
  - id: KB-V01
    tier: critical
    check: Frontmatter parses as YAML.
    pass_condition: frontmatter_parse_errors == 0
    fail_action: halt
  - id: KB-V02
    tier: critical
    check: Active machine-readable YAML blocks parse.
    pass_condition: active_yaml_parse_errors == 0
    fail_action: halt
  - id: KB-V03
    tier: critical
    check: Active rule count does not exceed declared limit.
    pass_condition: active_rule_count <= max_active_rules
    fail_action: halt
  - id: KB-V04
    tier: critical
    check: Active check count does not exceed declared limit.
    pass_condition: active_check_count <= max_active_checks
    fail_action: halt
  - id: KB-V05
    tier: critical
    check: Every active rule has required schema fields.
    pass_condition: rules_missing_required_fields == 0
    fail_action: halt
  - id: KB-V06
    tier: critical
    check: Every tier value is allowed.
    pass_condition: invalid_tier_count == 0
    fail_action: halt
  - id: KB-V07
    tier: required
    check: No duplicate or semantically overlapping active rules exist.
    pass_condition: semantic_duplicate_rule_count == 0
    fail_action: fail
  - id: KB-V08
    tier: required
    check: Appendix is marked human-reference-only.
    pass_condition: appendix_human_reference_only == true
    fail_action: fail
deployment_verdict_logic:
  deploy_ready:
    conditions:
      - all critical validation gates pass
      - all required validation gates pass
  not_ready:
    conditions:
      - any required validation gate fails
  halt:
    conditions:
      - any critical validation gate fails
      - active YAML does not parse
      - machine-consumed outputs are prose-only
```

# MINIMAL VALID FILE TEMPLATE

````markdown
---
class: kb_policy
role: EXAMPLE_AGENT_KB_POLICY
surface: active_policy
version: "1.0"
created_at: "2026-05-09"
last_validated_at: "2026-05-09"
status: canonical
target_use: "loaded as compact context into agent sessions"
scope_constraints:
  - "Markdown + YAML-frontmatter KB file only"
context_mode: compact
target_model_min: "gpt-4o"
max_active_rules: 3
max_active_checks: 2
source_files:
  - "example_source.md"
---

# ACTIVE POLICY

```yaml
active_policy:
  critical_path:
    rule_ids: [EX-C01]
  active_rules:
    - id: EX-C01
      tier: critical
      rule: "Encode active policy as parse-valid YAML."
      prevents: "false machine-readability"
      evidence_refs: [EX-F01]
      validation:
        pass_condition: "yaml_parse_errors == 0"
        fail_action: halt
    - id: EX-R01
      tier: required
      rule: "Keep human-only notes outside active policy."
      prevents: "context bloat"
      evidence_refs: [EX-F02]
      validation:
        pass_condition: "human_notes_in_active_policy == 0"
        fail_action: fail
  validation_gates:
    - id: EX-V01
      tier: critical
      check: "All active YAML parses."
      pass_condition: "yaml_parse_errors == 0"
      fail_action: halt
    - id: EX-V02
      tier: required
      check: "Active rule count respects frontmatter limit."
      pass_condition: "active_rule_count <= max_active_rules"
      fail_action: fail
  deployment_verdict_logic:
    deploy_ready:
      conditions:
        - "all critical gates pass"
        - "all required gates pass"
    halt:
      conditions:
        - "any critical gate fails"
```

# APPENDIX A — HUMAN REFERENCE ONLY

This appendix is not part of active agent context.