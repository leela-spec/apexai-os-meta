construction_guide:  
guide_purpose: "Define the target standard for building machine-readable files."  
depends_on:  
companion_file: "transformation_guide.yaml"  
relationship: "The transformation guide converts existing files into the standard defined here."  
source_document: "KB_Audit_v2.md "  
extraction_policy:  
preserve_verbatim: true  
include_implied_guidance: true  
exclude_transformation_workflows: true  
canonical_file_standard:  
recommended_format: "Markdown + YAML-frontmatter KB file with active structured YAML policy surfaces and human-only appendices."  
required_sections:  
- section_name: "YAML frontmatter"  
required: true  
purpose: "Declare machine-readable metadata for versioning, validation, model targeting, scope, and governance."  
ordering_rule: "Appears at the beginning of the file before the body."  
verbatim_evidence: "Add a machine-readable YAML frontmatter block containing: version, last_validated_at, target_model_min, max_active_rules, context_mode."  
source_reference: "Active Rules — RECOMMENDED Tier / BP-REC1"  
- section_name: "Critical Path"  
required: true  
purpose: "Expose the highest-priority constraints before any other rule is read."  
ordering_rule: "These 4 constraints are enforced before any other rule is read."  
verbatim_evidence: "Put all critical-tier rules within the first 500 tokens of the KB file."  
source_reference: "ACTIVE POLICY / Critical Path"  
- section_name: "Active Policy"  
required: true  
purpose: "Contain active machine-consumed rules and checks in compact YAML."  
ordering_rule: "Active policy section contains ≤100 tokens of non-YAML prose."  
verbatim_evidence: "Encode all active rules, checks, and templates as parse-valid YAML."  
source_reference: "ACTIVE POLICY / Critical Path"  
- section_name: "Critical Rules"  
required: true  
purpose: "Contain rules whose violation causes near-certain execution failure."  
ordering_rule: "Place all critical-tier rules within the first 500 tokens of the KB file, before any prose, metadata, or examples."  
verbatim_evidence: "Violating causes near-certain execution failure"  
source_reference: "Active Rules — CRITICAL Tier"  
- section_name: "Required Rules"  
required: true  
purpose: "Contain rules whose violation causes likely degradation."  
ordering_rule: "Document section order is CRITICAL → REQUIRED → RECOMMENDED."  
verbatim_evidence: "Violating causes likely degradation"  
source_reference: "Active Rules — REQUIRED Tier"  
- section_name: "Recommended Rules"  
required: true  
purpose: "Contain lower-stakes guidance."  
ordering_rule: "Place recommended-tier rules at the end of the KB file to use residual recency attention for low-stakes guidance."  
verbatim_evidence: "Violating causes marginal degradation"  
source_reference: "Active Rules — RECOMMENDED Tier"  
- section_name: "Audit Checklist"  
required: true  
purpose: "Define machine-readable validation checks and deployment verdict logic."  
ordering_rule: "Run before every deployment. All critical must pass."  
verbatim_evidence: "Active deployment checks: 8"  
source_reference: "AUDIT CHECKLIST / Active Deployment Checks"  
- section_name: "Appendices"  
required: true  
purpose: "Hold human-readable evidence, anti-pattern explanations, and extended checks outside active context."  
ordering_rule: "Human-readable reference. Not loaded into active agent context."  
verbatim_evidence: "Separate active policy from evidence prose; move explanations to appendices."  
source_reference: "ACTIVE POLICY / Critical Path"  
required_metadata:  
- field_name: "version"  
purpose: "Identify the KB file version."  
required: true  
verbatim_evidence: "Frontmatter contains version, last_validated_at, target_model_min, max_active_rules, and context_mode."  
source_reference: "KB-ACHK-08"  
- field_name: "last_validated_at"  
purpose: "Enable staleness detection."  
required: true  
verbatim_evidence: "Frontmatter contains version, last_validated_at, target_model_min, max_active_rules, and context_mode."  
source_reference: "KB-ACHK-08"  
- field_name: "target_model_min"  
purpose: "Declare the weakest supported model for safe instruction density."  
required: true  
verbatim_evidence: "Frontmatter contains target_model_min and rule count stays below that model's safe threshold."  
source_reference: "CHK-10"  
- field_name: "max_active_rules"  
purpose: "Declare the configured ceiling for active rules."  
required: true  
verbatim_evidence: "Total active rule count is below the configured max_active_rules limit."  
source_reference: "KB-ACHK-03"  
- field_name: "context_mode"  
purpose: "Declare context loading mode."  
required: true  
verbatim_evidence: "Frontmatter contains version, last_validated_at, target_model_min, max_active_rules, and context_mode."  
source_reference: "KB-ACHK-08"  
construction_guidelines:  
- id: "CG-001"  
category: "critical_path"  
tier: "critical"  
guideline_type: "placement"  
verbatim_text: "Put all critical-tier rules within the first 500 tokens of the KB file."  
operational_interpretation: "Critical constraints must be near the beginning of the machine-readable file."  
applies_to: ["critical_rules", "critical_path"]  
required_fields: []  
forbidden_patterns: ["mid-document critical constraints"]  
validation_logic: "critical_rules_max_token_position <= 500"  
source_reference:  
section: "ACTIVE POLICY"  
subsection: "Critical Path"  
line_or_location: "KB-CP-01"  
context_excerpt: "These 4 constraints are enforced before any other rule is read."  
confidence: 1.0  
- id: "CG-002"  
category: "parseability"  
tier: "critical"  
guideline_type: "encoding"  
verbatim_text: "Encode all active rules, checks, and templates as parse-valid YAML."  
operational_interpretation: "Every active machine-consumed policy object must be valid YAML, not pseudo-structured prose."  
applies_to: ["rules", "checks", "templates"]  
required_fields: []  
forbidden_patterns: ["malformed YAML", "pseudo-code", "prose lists"]  
validation_logic: "yaml_parse_errors == 0"  
source_reference:  
section: "ACTIVE POLICY"  
subsection: "Critical Path"  
line_or_location: "KB-CP-02"  
context_excerpt: "Encode all active rules, checks, and templates as parse-valid YAML."  
confidence: 1.0  
- id: "CG-003"  
category: "surface_separation"  
tier: "critical"  
guideline_type: "structure"  
verbatim_text: "Separate active policy from evidence prose; move explanations to appendices."  
operational_interpretation: "Machine-loaded policy should remain compact; explanatory material belongs in appendices."  
applies_to: ["active_policy", "appendices", "evidence"]  
required_fields: []  
forbidden_patterns: ["research evidence in active policy", "long explanations in active policy"]  
validation_logic: "active_policy_prose_tokens <= 100"  
source_reference:  
section: "ACTIVE POLICY"  
subsection: "Critical Path"  
line_or_location: "KB-CP-03"  
context_excerpt: "Separate active policy from evidence prose; move explanations to appendices."  
confidence: 1.0  
- id: "CG-004"  
category: "output_contracts"  
tier: "critical"  
guideline_type: "schema"  
verbatim_text: "Use schema-enforced outputs for every machine-consumed artifact."  
operational_interpretation: "Any output meant for downstream machine consumption must be governed by an enforced schema."  
applies_to: ["machine_consumed_outputs", "templates", "artifacts"]  
required_fields: ["schema_reference"]  
forbidden_patterns: ["prose-only output contracts"]  
validation_logic: "schema_enforced_outputs == true AND prose_only_output_contracts == 0"  
source_reference:  
section: "ACTIVE POLICY"  
subsection: "Critical Path"  
line_or_location: "KB-CP-04"  
context_excerpt: "Use schema-enforced outputs for every machine-consumed artifact."  
confidence: 1.0  
- id: "CG-005"  
category: "rule_count"  
tier: "critical"  
guideline_type: "limit"  
verbatim_text: "Keep total rule count below 50 for standard deployment; never exceed 150 even for reasoning-class models."  
operational_interpretation: "Machine-readable KB files must keep active rule volume within model-compliance thresholds."  
applies_to: ["active_rules"]  
required_fields: ["rule_count", "max_active_rules"]  
forbidden_patterns: ["rule proliferation creep", "high-density rule blocks"]  
validation_logic: "rule_count < 50 OR reasoning_model_rule_count < 150"  
source_reference:  
section: "Active Rules — CRITICAL Tier"  
subsection: "BP-C2"  
line_or_location: "BP-C2"  
context_excerpt: "instruction-following cliff; compliance collapses non-linearly at high density"  
confidence: 1.0  
- id: "CG-006"  
category: "output_contracts"  
tier: "critical"  
guideline_type: "schema"  
verbatim_text: "Never rely on prose output instructions for machine-consumed outputs; enforce structure via API-level schema (strict: true or equivalent)."  
operational_interpretation: "Prose descriptions of required output shape are insufficient for machine-consumed artifacts."  
applies_to: ["machine_consumed_outputs"]  
required_fields: ["api_schema", "strict"]  
forbidden_patterns: ["always respond as JSON", "prose-only output instructions"]  
validation_logic: "prose_only_output_contracts == 0"  
source_reference:  
section: "Active Rules — CRITICAL Tier"  
subsection: "BP-C3"  
line_or_location: "BP-C3"  
context_excerpt: "invalid downstream structures; prose contracts work 'most of the time' only"  
confidence: 1.0  
- id: "CG-007"  
category: "tiering"  
tier: "critical"  
guideline_type: "metadata"  
verbatim_text: "Assign an explicit tier tag (critical | required | recommended) inline on every rule, not in a separate legend."  
operational_interpretation: "Each rule object must carry its own priority label."  
applies_to: ["rules"]  
required_fields: ["tier"]  
forbidden_patterns: ["tier legend only", "untiered rules"]  
validation_logic: "rules_missing_tier_tag == 0"  
source_reference:  
section: "Active Rules — CRITICAL Tier"  
subsection: "BP-C4"  
line_or_location: "BP-C4"  
context_excerpt: "unlabeled rules treated as equal-weight by the model"  
confidence: 1.0  
- id: "CG-008"  
category: "yaml_rules"  
tier: "critical"  
guideline_type: "format"  
verbatim_text: "Use YAML blocks — not prose paragraphs or JSON — to encode all structured rules, constraints, and checklists."  
operational_interpretation: "Structured KB content should be represented as YAML."  
applies_to: ["rules", "constraints", "checklists"]  
required_fields: []  
forbidden_patterns: ["prose paragraphs for structured rules", "JSON for instruction blocks"]  
validation_logic: "structured_blocks_format == yaml"  
source_reference:  
section: "Active Rules — CRITICAL Tier"  
subsection: "BP-C5"  
line_or_location: "BP-C5"  
context_excerpt: "ambiguous rule parsing; prose rules are token-wasteful and semantically hedged"  
confidence: 1.0  
- id: "CG-009"  
category: "rule_quality"  
tier: "required"  
guideline_type: "minimality"  
verbatim_text: "Run a deletion test on every rule before committing: if removal causes no observable behavioral change in >90% of cases, delete the rule."  
operational_interpretation: "Every rule must justify its presence by producing observable behavioral change."  
applies_to: ["rules"]  
required_fields: []  
forbidden_patterns: ["redundant rules", "decorative rules"]  
validation_logic: "rules_without_behavioral_effect == 0"  
source_reference:  
section: "Active Rules — REQUIRED Tier"  
subsection: "BP-R1"  
line_or_location: "BP-R1"  
context_excerpt: "rule proliferation creep; redundant rules suppress compliance of necessary ones"  
confidence: 1.0  
- id: "CG-010"  
category: "long_context"  
tier: "required"  
guideline_type: "recitation"  
verbatim_text: "Recite all critical rules verbatim in an Active Constraints block immediately before the task input in long-session agents (>8K tokens)."  
operational_interpretation: "Long-session KB systems need a documented critical-rule recitation mechanism."  
applies_to: ["critical_rules", "long_session_agents"]  
required_fields: ["active_constraints_block"]  
forbidden_patterns: ["critical rules only at session start"]  
validation_logic: "active_constraints_injection_documented == true"  
source_reference:  
section: "Active Rules — REQUIRED Tier"  
subsection: "BP-R2"  
line_or_location: "BP-R2"  
context_excerpt: "lost-in-the-middle drift; critical rules loaded at session start decay out of effective attention"  
confidence: 1.0  
- id: "CG-011"  
category: "token_budget"  
tier: "required"  
guideline_type: "limit"  
verbatim_text: "Limit the instruction block to ≤2,000 tokens to preserve context budget for task content, retrieved documents, and conversation history."  
operational_interpretation: "Active instruction content should remain compact."  
applies_to: ["instruction_block", "active_policy"]  
required_fields: []  
forbidden_patterns: ["active surface bloat"]  
validation_logic: "instruction_block_tokens <= 2000"  
source_reference:  
section: "Active Rules — REQUIRED Tier"  
subsection: "BP-R3"  
line_or_location: "BP-R3"  
context_excerpt: "task context crowding; effective range ≠ max context window"  
confidence: 1.0  
- id: "CG-012"  
category: "examples"  
tier: "required"  
guideline_type: "limit"  
verbatim_text: "Use 1–3 examples only for rules that are formatting-critical or genuinely ambiguous; rewrite unclear rules instead of adding examples."  
operational_interpretation: "Examples are limited and only justified for ambiguity or formatting precision."  
applies_to: ["examples", "rules"]  
required_fields: []  
forbidden_patterns: ["example overload", "examples for clear rules"]  
validation_logic: "examples_per_rule <= 3 AND examples_only_for_ambiguous_or_formatting_rules == true"  
source_reference:  
section: "Active Rules — REQUIRED Tier"  
subsection: "BP-R4"  
line_or_location: "BP-R4"  
context_excerpt: "example overload; excessive few-shot examples degrade performance in some models"  
confidence: 1.0  
- id: "CG-013"  
category: "sectioning"  
tier: "required"  
guideline_type: "structure"  
verbatim_text: "Organize KB sections with stable labeled Markdown headers and XML-style section tags so compression routines can selectively preserve or drop entire sections."  
operational_interpretation: "The document should expose durable section boundaries for automated context handling."  
applies_to: ["sections", "headers", "context_compression"]  
required_fields: []  
forbidden_patterns: ["unstable headings", "unlabeled prose blocks"]  
validation_logic: "all_required_section_headers_present == true"  
source_reference:  
section: "Active Rules — REQUIRED Tier"  
subsection: "BP-R5"  
line_or_location: "BP-R5"  
context_excerpt: "arbitrary context compression dropping critical chunks"  
confidence: 1.0  
- id: "CG-014"  
category: "model_targeting"  
tier: "required"  
guideline_type: "compatibility"  
verbatim_text: "Design the KB file for the weakest model in the deployment fleet; never assume Gemini 2.5 Pro or o3 safe thresholds apply fleet-wide."  
operational_interpretation: "Rule density and structure must be safe for the least capable target model."  
applies_to: ["frontmatter", "rules", "deployment_fleet"]  
required_fields: ["target_model_min"]  
forbidden_patterns: ["frontier-model-only threshold assumptions"]  
validation_logic: "target_model_min_present == true AND rule_count_within_model_threshold == true"  
source_reference:  
section: "Active Rules — REQUIRED Tier"  
subsection: "BP-R6"  
line_or_location: "BP-R6"  
context_excerpt: "10× compliance gap between weakest and strongest models at high instruction density"  
confidence: 1.0  
- id: "CG-015"  
category: "deduplication"  
tier: "required"  
guideline_type: "consistency"  
verbatim_text: "Never duplicate a rule across multiple sections; a rule appearing twice with any paraphrase creates contradiction drift."  
operational_interpretation: "Each rule must have one canonical source of truth."  
applies_to: ["rules"]  
required_fields: []  
forbidden_patterns: ["semantic duplicate rules", "prose restatements of YAML rules"]  
validation_logic: "semantic_duplicate_rule_count == 0"  
source_reference:  
section: "Active Rules — REQUIRED Tier"  
subsection: "BP-R7"  
line_or_location: "BP-R7"  
context_excerpt: "context clash — one of the four primary context failure modes in production agents"  
confidence: 1.0  
- id: "CG-016"  
category: "frontmatter"  
tier: "recommended"  
guideline_type: "metadata"  
verbatim_text: "Add a machine-readable YAML frontmatter block containing: version, last_validated_at, target_model_min, max_active_rules, context_mode."  
operational_interpretation: "These fields form the minimum metadata contract for the KB file."  
applies_to: ["frontmatter"]  
required_fields: ["version", "last_validated_at", "target_model_min", "max_active_rules", "context_mode"]  
forbidden_patterns: ["missing frontmatter", "unstructured metadata"]  
validation_logic: "frontmatter_required_fields_present == true"  
source_reference:  
section: "Active Rules — RECOMMENDED Tier"  
subsection: "BP-REC1"  
line_or_location: "BP-REC1"  
context_excerpt: "stale or model-mismatched KB loading; no automated staleness detection possible without it"  
confidence: 1.0  
- id: "CG-017"  
category: "section_order"  
tier: "recommended"  
guideline_type: "ordering"  
verbatim_text: "Place recommended-tier rules at the end of the KB file to use residual recency attention for low-stakes guidance."  
operational_interpretation: "Recommended rules should not occupy high-priority attention positions."  
applies_to: ["recommended_rules"]  
required_fields: []  
forbidden_patterns: ["recommended rules before critical or required rules"]  
validation_logic: "recommended_rules_section_position == end"  
source_reference:  
section: "Active Rules — RECOMMENDED Tier"  
subsection: "BP-REC2"  
line_or_location: "BP-REC2"  
context_excerpt: "mid-document attention loss on optional rules"  
confidence: 1.0  
- id: "CG-018"  
category: "token_budget"  
tier: "recommended"  
guideline_type: "measurement"  
verbatim_text: "Token-count the assembled context (system prompt + KB + task input) before inference; log per-component proportions to detect instruction crowding."  
operational_interpretation: "The KB standard includes measurable context-budget observability."  
applies_to: ["assembled_context", "deployment"]  
required_fields: ["token_count_assembled_context"]  
forbidden_patterns: ["unmeasured assembled context"]  
validation_logic: "assembled_context_tokens_logged == true"  
source_reference:  
section: "Active Rules — RECOMMENDED Tier"  
subsection: "BP-REC3"  
line_or_location: "BP-REC3"  
context_excerpt: "silent quality degradation from context proportion shift"  
confidence: 1.0  
- id: "CG-019"  
category: "rule_style"  
tier: "recommended"  
guideline_type: "wording"  
verbatim_text: "Write all rule text in active imperative voice; remove hedging words (modal verbs) to eliminate optionality signals."  
operational_interpretation: "Rule language should be direct and non-optional."  
applies_to: ["rule_text"]  
required_fields: []  
forbidden_patterns: ["should", "may", "might", "could"]  
validation_logic: "modal_verb_count_in_rule_text == 0"  
source_reference:  
section: "Active Rules — RECOMMENDED Tier"  
subsection: "BP-REC4"  
line_or_location: "BP-REC4"  
context_excerpt: "model interpreting hedged rules as optional"  
confidence: 1.0  
- id: "CG-020"  
category: "staleness"  
tier: "recommended"  
guideline_type: "metadata"  
verbatim_text: "Add a validity_window field on time-sensitive or model-version-specific rules to enable automated staleness detection."  
operational_interpretation: "Rules dependent on time, benchmark state, or model version need explicit expiry semantics."  
applies_to: ["time_sensitive_rules", "model_version_specific_rules"]  
required_fields: ["validity_window"]  
forbidden_patterns: ["stale model-specific rules without validity windows"]  
validation_logic: "model_specific_rules_without_validity_window == 0"  
source_reference:  
section: "Active Rules — RECOMMENDED Tier"  
subsection: "BP-REC5"  
line_or_location: "BP-REC5"  
context_excerpt: "memory pollution from un-expired stale rules in long-running systems"  
confidence: 1.0  
anti_patterns:  
- id: "AP-001"  
anti_pattern_name: "Rule Proliferation Creep"  
problem_verbatim: "Adding a rule for every observed failure without removing obsolete ones until the KB exceeds the model's reliable instruction threshold."  
machine_readability_failure: "Excessive rule count causes instruction-following degradation and suppresses compliance with necessary rules."  
required_fix_verbatim: "After adding any new rule, run the deletion test on all existing rules and remove at least one."  
source_reference: "APPENDIX A — Anti-Patterns / Common KB Design Mistakes / 1"  
- id: "AP-002"  
anti_pattern_name: "Prose Contract for Structured Output"  
problem_verbatim: "Instructing the model in prose to "always respond as JSON" instead of enforcing a schema at the API level."  
machine_readability_failure: "Downstream consumers receive outputs governed only by prose rather than constrained schemas."  
required_fix_verbatim: "Replace all prose output format instructions with an OpenAI Structured Outputs schema or equivalent constrained-decoding mechanism."  
source_reference: "APPENDIX A — Anti-Patterns / Common KB Design Mistakes / 2"  
- id: "AP-003"  
anti_pattern_name: "Mid-Document Rule Burial"  
problem_verbatim: "Placing critical constraints in the middle of a long KB file where positional attention is weakest."  
machine_readability_failure: "Critical constraints are less likely to be followed due to positional attention loss."  
required_fix_verbatim: "Audit token position of every critical rule and move all of them to within the first 500 tokens."  
source_reference: "APPENDIX A — Anti-Patterns / Common KB Design Mistakes / 3"  
- id: "AP-004"  
anti_pattern_name: "Example Overload"  
problem_verbatim: "Adding more than 3 examples per rule assuming "more examples = better compliance," causing context pollution."  
machine_readability_failure: "Examples consume context budget and can reduce compliance."  
required_fix_verbatim: "Reduce to 1 canonical example per ambiguous rule; remove examples entirely from clearly stated rules."  
source_reference: "APPENDIX A — Anti-Patterns / Common KB Design Mistakes / 4"  
- id: "AP-005"  
anti_pattern_name: "Rule Duplication with Paraphrase"  
problem_verbatim: "Stating the same constraint in two places with different wording, creating contradiction drift the model cannot resolve."  
machine_readability_failure: "The KB contains multiple competing formulations of the same rule."  
required_fix_verbatim: "Establish a single canonical YAML rule block as the source of truth; delete all prose restatements."  
source_reference: "APPENDIX A — Anti-Patterns / Common KB Design Mistakes / 5"  
- id: "AP-006"  
anti_pattern_name: "Modal Hedging in Rule Text"  
problem_verbatim: "Writing rules as "the agent should return X" instead of "Return X," giving the model implicit permission to treat the rule as optional."  
machine_readability_failure: "The model may interpret mandatory rules as optional guidance."  
required_fix_verbatim: "Replace all modal verbs (should, may, might, could) in rule text with imperative form."  
source_reference: "APPENDIX A — Anti-Patterns / Common KB Design Mistakes / 6"  
- id: "AP-007"  
anti_pattern_name: "Static KB for Multi-Model Fleet"  
problem_verbatim: "Designing KB instruction density for the strongest model and deploying the same file to weaker models that cliff at far lower counts."  
machine_readability_failure: "The same KB exceeds safe thresholds for weaker models."  
required_fix_verbatim: "Add `target_model_min` to frontmatter and validate rule count against that model's safe threshold."  
source_reference: "APPENDIX A — Anti-Patterns / Common KB Design Mistakes / 7"  
- id: "AP-008"  
anti_pattern_name: "No Recitation for Long Sessions"  
problem_verbatim: "Loading critical rules only at session start with no mechanism to re-inject them near the active turn."  
machine_readability_failure: "Critical rules decay out of effective attention in long contexts."  
required_fix_verbatim: "Prepend critical rules as an Active Constraints block to each agent reasoning step in sessions exceeding ~8K tokens."  
source_reference: "APPENDIX A — Anti-Patterns / Common KB Design Mistakes / 8"  
- id: "AP-009"  
anti_pattern_name: "Malformed Machine Blocks"  
problem_verbatim: "Presenting rules as pseudo-code, double-backtick blocks, or prose lists while claiming "machine-readable YAML.""  
machine_readability_failure: "Structured content cannot be parsed reliably."  
required_fix_verbatim: "Lint every structured block; reject any file where `yaml.safe_load()` raises an error."  
source_reference: "APPENDIX A — Anti-Patterns / Common KB Design Mistakes / 9"  
- id: "AP-010"  
anti_pattern_name: "Active Surface Bloat"  
problem_verbatim: "Loading research evidence, anti-pattern explanations, audit templates, and changelogs into the active inference context."  
machine_readability_failure: "Human-only material crowds the active inference context."  
required_fix_verbatim: "Move all human-only content to appendices; keep active policy section below 2,000 tokens."  
source_reference: "APPENDIX A — Anti-Patterns / Common KB Design Mistakes / 10"  
validation_checks:  
- id: "VC-001"  
check_verbatim: "All YAML blocks in the file parse without errors."  
pass_condition: "yaml_parse_errors == 0"  
fail_condition: "yaml_parse_errors > 0"  
severity: "critical"  
source_reference: "KB-ACHK-01"  
- id: "VC-002"  
check_verbatim: "All critical-tier rules appear within the first 500 tokens of the file."  
pass_condition: "critical_rules_max_token_position <= 500"  
fail_condition: "critical_rules_max_token_position > 500"  
severity: "critical"  
source_reference: "KB-ACHK-02"  
- id: "VC-003"  
check_verbatim: "Total active rule count is below the configured max_active_rules limit."  
pass_condition: "active_rule_count <= max_active_rules"  
fail_condition: "active_rule_count > max_active_rules"  
severity: "critical"  
source_reference: "KB-ACHK-03"  
- id: "VC-004"  
check_verbatim: "Every machine-consumed output references an API-enforced schema, not prose-only instructions."  
pass_condition: "schema_enforced_outputs == true AND prose_only_output_contracts == 0"  
fail_condition: "schema_enforced_outputs != true OR prose_only_output_contracts > 0"  
severity: "critical"  
source_reference: "KB-ACHK-04"  
- id: "VC-005"  
check_verbatim: "No duplicate or semantically paraphrased rules exist in the file."  
pass_condition: "semantic_duplicate_rule_count == 0"  
fail_condition: "semantic_duplicate_rule_count > 0"  
severity: "required"  
source_reference: "KB-ACHK-05"  
- id: "VC-006"  
check_verbatim: "Every rule has tier, prevents, and evidence_refs fields populated."  
pass_condition: "rules_missing_required_fields == 0"  
fail_condition: "rules_missing_required_fields > 0"  
severity: "required"  
source_reference: "KB-ACHK-06"  
- id: "VC-007"  
check_verbatim: "Active policy section contains ≤100 tokens of non-YAML prose."  
pass_condition: "active_policy_prose_tokens <= 100"  
fail_condition: "active_policy_prose_tokens > 100"  
severity: "required"  
source_reference: "KB-ACHK-07"  
- id: "VC-008"  
check_verbatim: "Frontmatter contains version, last_validated_at, target_model_min, max_active_rules, and context_mode."  
pass_condition: "frontmatter_required_fields_present == true"  
fail_condition: "frontmatter_required_fields_present != true"  
severity: "required"  
source_reference: "KB-ACHK-08"  
- id: "VC-009"  
check_verbatim: "Every rule entry has an inline tier tag (critical | required | recommended)."  
pass_condition: "rules_missing_tier_tag == 0"  
fail_condition: "rules_missing_tier_tag > 0"  
severity: "critical"  
source_reference: "CHK-05"  
- id: "VC-010"  
check_verbatim: "Every rule has a documented prevents field (failure scenario it guards against)."  
pass_condition: "rules_missing_prevents_field == 0"  
fail_condition: "rules_missing_prevents_field > 0"  
severity: "required"  
source_reference: "CHK-06"  
- id: "VC-011"  
check_verbatim: "Instruction block token count is ≤2,000."  
pass_condition: "instruction_block_tokens <= 2000"  
fail_condition: "instruction_block_tokens > 2000"  
severity: "required"  
source_reference: "CHK-07"  
- id: "VC-012"  
check_verbatim: "KB file has stable labeled section headers for: metadata, critical rules, required rules, examples (if any), recommended rules."  
pass_condition: "all_required_section_headers_present == true AND unlabeled_prose_block_tokens <= 100"  
fail_condition: "all_required_section_headers_present != true OR unlabeled_prose_block_tokens > 100"  
severity: "required"  
source_reference: "CHK-09"  
- id: "VC-013"  
check_verbatim: "Total examples ≤10 across the file; no more than 3 per rule."  
pass_condition: "examples_per_rule <= 3 AND total_examples <= 10"  
fail_condition: "examples_per_rule > 3 OR total_examples > 10"  
severity: "required"  
source_reference: "CHK-11"  
- id: "VC-014"  
check_verbatim: "A recitation mechanism exists for critical rules in long-session agents."  
pass_condition: "active_constraints_injection_documented == true"  
fail_condition: "active_constraints_injection_documented != true"  
severity: "required"  
source_reference: "CHK-12"  
- id: "VC-015"  
check_verbatim: "All rule text uses active imperative voice; zero modal verbs (should, may, might, could) in rule text."  
pass_condition: "modal_verb_count_in_rule_text == 0"  
fail_condition: "modal_verb_count_in_rule_text > 0"  
severity: "recommended"  
source_reference: "CHK-14"  
- id: "VC-016"  
check_verbatim: "Document section order is CRITICAL → REQUIRED → RECOMMENDED."  
pass_condition: "section_order_correct == true"  
fail_condition: "section_order_correct != true"  
severity: "recommended"  
source_reference: "CHK-15"  
- id: "VC-017"  
check_verbatim: "No YAML rule is restated as a prose paragraph in the same section."  
pass_condition: "prose_restatements_of_yaml_rules == 0"  
fail_condition: "prose_restatements_of_yaml_rules > 0"  
severity: "recommended"  
source_reference: "CHK-16"  
- id: "VC-018"  
check_verbatim: "Time-sensitive or model-version-specific rules contain a validity_window field."  
pass_condition: "model_specific_rules_without_validity_window == 0"  
fail_condition: "model_specific_rules_without_validity_window > 0"  
severity: "recommended"  
source_reference: "CHK-17"