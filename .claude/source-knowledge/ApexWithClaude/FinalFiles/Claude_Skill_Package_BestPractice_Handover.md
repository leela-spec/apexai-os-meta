# Claude Skill Package — Best Practice Handover Guide
# Distilled from: full skill package design, audit, iteration, and validation cycle
# Scope: How to create final, Claude-compatible, deployment-ready skill files
# Audience: Any AI or operator starting a new Claude skill package from scratch

---

## 0. What This Guide Is

This guide captures every validated rule, format pattern, and defect-prevention
measure from a complete build-audit-iterate cycle on a real Claude skill package.
It is written as machine-readable instructions for a GPT or Claude agent that will
generate Claude Code skill files.

Read this entire guide before generating any file.
All rules apply to every file unless explicitly scoped otherwise.

---

## 1. Claude Skill Package — Anatomy

A Claude skill package is a folder under `.claude/skills/<skill-name>/` containing:

```yaml
canonical_package_structure:
  required:
    - SKILL.md                   # entrypoint — triggers the skill, defines procedure
  recommended_references:
    - references/<contract>.md   # owns schemas and output contracts
    - references/<rules>.md      # owns validation, ranking, failure modes (full)
  optional:
    - templates/<template>.md    # blank copy-paste template for skill output
    - examples/<example>.md      # filled example for manual testing
    - package-manifest.md        # lightweight file index

  forbidden_in_package:
    - source_mapping files       # derivation notes do not belong in final files
    - CI_or_deployment_files
    - runtime_state_files
    - task_board_files
    - scheduler_files
    - workflow_index
    - settings_json
    - tests_or_evals
    - calendar_api_integration_files
```

---

## 2. The Three Quality Dimensions — Definitions

Every file is evaluated on three dimensions. All three must score ≥8/10 for
a file to be considered best practice.

```yaml
quality_dimensions:

  machine_readability:
    definition: >
      Claude can parse, route, and execute based on the file content without
      ambiguity. YAML blocks are valid. Key names are consistent. Schemas are
      typed. Trigger phrases are exact.
    common_failures:
      - YAML collapsed to single-line strings
      - Description does not start with "Use this skill when"
      - Numeric constraints written as string labels ("1-100")
      - Key names differ between files for the same concept

  token_efficiency:
    definition: >
      The file contains no redundant content. Every token contributes to
      Claude's execution. No schema is defined more than once. No section
      is repeated. Validation checklists are not reprinted per-file.
    common_failures:
      - Same schema defined in 3 separate sections of one file
      - Non-goals list duplicated in body and in header block
      - Per-prompt validation checklists reprinting 10 global items per file
      - Manifest file that became a second contract document

  resilient_simplicity:
    definition: >
      The file remains correct and executable even when inputs are missing,
      malformed, or ambiguous. Procedure is coarse-grained. Failure modes
      cover recovery paths. Operator gates are explicit.
    common_failures:
      - 27-step procedure for a 6-action skill
      - No failure modes section
      - Completion gate as prose bullets (not machine-checkable)
      - No "read_when" conditions — Claude loads every support file always
```

---

## 3. SKILL.md — Canonical Format (Mandatory)

Every SKILL.md must follow this exact section order. No additions. No removals.

```yaml
SKILL_md_mandatory_sections:
  order:
    1: yaml_frontmatter          # name + description only
    2: "# <Skill Name>"          # H1 matching name field
    3: "## Skill Contract"       # compact YAML block
    4: "## Supporting Files"     # YAML block, path + read_when
    5: "## Procedure"            # numbered steps, prose
    6: "## Failure Modes"        # YAML block
    7: "## Output Requirements"  # YAML block
    8: "## Completion Gate"      # YAML boolean checklist
```

### 3.1 Frontmatter Rules

```yaml
frontmatter_rules:
  allowed_fields_only:
    - name
    - description
  forbidden_fields:
    - version
    - status
    - author
    - tags
    - any_other_field
  name_format: lowercase-kebab-case
  description_rules:
    MUST_begin_with_exact_string: "Use this skill when"
    must_name:
      - trigger_condition
      - accepted_inputs
      - primary_output
      - at_least_one_boundary
    max_words: 80
    format: single_paragraph_no_line_breaks
```

**Correct description pattern:**
```
description: >
  Use this skill when the operator asks to [trigger condition].
  Accepts [input types]. Produces [primary output].
  Does not [boundary 1] or [boundary 2].
```

**Incorrect pattern (causes routing failure):**
```
description: >
  create, normalize, update, rank, or validate a compact overview...
```
The description MUST start with "Use this skill when" — this is Claude's
routing key, not a stylistic choice.

### 3.2 Skill Contract

One compact YAML block. Contains everything Claude needs to understand the
skill without reading any other section.

```yaml
skill_contract_required_keys:
  primary_output: <snake_case artifact name>
  output_role: <one phrase>
  hierarchy:
    - <level 1>
    - <level 2>
  compact_format: |
    <human-readable output format example>
  rating_format:             # if skill uses ratings
    syntax: "[priority/urgency/date]"
    priority:
      type: integer
      min: 1
      max: 100
    urgency:
      type: integer
      min: 1
      max: 100
    date:
      type: string
      allowed: ["DD-MM", "NA"]
  ranking_order:             # if skill ranks items
    - manual_override_if_present
    - deadline_first
    - priority_second
    - urgency_third
  boundaries:
    must_not_create:
      - <forbidden output 1>
      - <forbidden output 2>
```

**Critical:** Numeric range constraints must ALWAYS use typed objects.
Never use string labels. This defect appeared in every v1 file and required
a dedicated patch round.

```yaml
WRONG:   priority: "1-100"
CORRECT: priority: { type: integer, min: 1, max: 100 }

WRONG:   date: "DD-MM or NA"
CORRECT: date: { type: string, allowed: ["DD-MM", "NA"] }
```

### 3.3 Supporting Files

Always a YAML block. Never prose bullets. Each file needs a `path` and a
`read_when` list. `read_when` items are snake_case condition identifiers —
not natural language. This allows Claude to lazy-load files only when needed.

```yaml
# CORRECT pattern:
supporting_files:
  - path: references/output-contract.md
    read_when:
      - validating_output_structure
      - operator_asks_for_contract_fields
  - path: references/validation-rules.md
    read_when:
      - ranking_tasks
      - validating_rating_format

# WRONG pattern (Claude cannot parse load conditions):
# - `references/output-contract.md` — use when the operator asks for contract-level structure
```

### 3.4 Procedure

Numbered steps. Prose only (no sub-bullets). 5–8 steps for a single-responsibility skill.

```yaml
procedure_rules:
  step_format: "N. **Verb phrase.** Outcome sentence."
  target_step_count: "5-8"
  max_step_count: 8
  one_action_per_step: true
  no_sub_bullets: true
  last_step_must_reference_failure_modes: true
  flag_as_scope_violation_if: more_than_10_steps
```

**Wrong grain (27 steps for 6 actions):**
```
3. Separate material that clearly belongs to a project from material that is still unassigned.
4. Put unresolved incoming infos, tasks, and project candidates into an Unassigned section.
5. Remove an item from Unassigned once it has been assigned to a project.
```

**Correct grain (1 step for the same 3 actions):**
```
2. **Sort material.** Assign project-specific content to the correct project.
   Put unresolved items into Unassigned. Remove from Unassigned once assigned.
```

### 3.5 Failure Modes

YAML block only. Each mode: exactly one `trigger` sentence + one `correction` sentence.
Maximum 8 modes in SKILL.md. If more are needed, the skill scope is too broad.
Full validation logic lives in the references file, not in SKILL.md.

```yaml
failure_modes:
  no_context:
    trigger: "No project notes, prior overview, or incoming items supplied."
    correction: "Ask for source notes or offer the blank template."
  invalid_rating:
    trigger: "Rating is not [number/number/DD-MM] or [number/number/NA], or value is outside 1-100."
    correction: "Keep item, mark rating invalid, request operator review."
```

### 3.6 Output Requirements

YAML block. Lists required sections and one rule per section. Key names
must match canonical_key_names exactly.

```yaml
output_requirements:
  required_sections:
    - overview_metadata
    - project_sections
    - ranked_task_view
    - unassigned          # key name must be consistent across ALL files
    - operator_validation # key name must be consistent across ALL files
  unassigned:
    include_only_when_unresolved_items_exist: true
  operator_validation:
    include_only_relevant_flags: true
```

### 3.7 Completion Gate

YAML boolean checklist only. No prose. No bullet lists. 6–12 checks.
Every value is `true`. Claude evaluates each key before marking the skill done.

```yaml
completion_gate:
  hierarchy_is_project_task_subtask: true
  ratings_use_priority_urgency_date: true
  ranked_task_view_present: true
  manual_override_preserved: true
  no_workstreams: true
  no_detailed_project_database: true
  operator_review_flags_present_when_needed: true
```

---

## 4. Reference Files — Rules

Reference files own schemas and rules that SKILL.md refers to but does not
define inline.

```yaml
reference_file_rules:

  structure:
    - "# File Title"
    - yaml_header_block_with_file_role
    - numbered_sections_with_headers
    - yaml_first_for_every_rule_set
    - non_goals_at_end

  schema_ownership:
    rule: >
      Each schema is defined in EXACTLY ONE file. No other file may redefine it.
      Other files that need to reference a schema write:
        canonical_source: references/filename.md
    consequence_of_violation: >
      Triple definition was found in the v1 contract file — same schema in
      artifact_contract, Normalized Structure, and Section Contracts.
      Cost: ~800 redundant tokens per load.

  non_goals_format:
    rule: "All non-goals must be short imperative sentences beginning with Do not."
    correct: "Do not create a detailed project database."
    incorrect: "no_detailed_project_database"

  contract_file_target_length: "under 100 lines"
  manifest_file_target_length: "under 60 lines"
```

---

## 5. YAML Formatting — The Most Critical Rule

YAML indentation collapse was the most widespread defect in the v1 package —
it affected 5 of 7 files and made every block unparseable.

```yaml
yaml_formatting_rules:
  indentation: "2 spaces"
  nested_objects: "indented 2 spaces relative to parent"
  list_items: "- at correct indent level"
  must_be_parseable: true
  no_collapsed_yaml: true

  self_check_before_output:
    instruction: >
      After generating each file, read every YAML block and verify it would
      parse with a standard YAML linter. If any block is flat or collapsed,
      regenerate it before outputting.

  correct_example: |
    rating_format:
      syntax: "[priority/urgency/date]"
      priority:
        type: integer
        min: 1
        max: 100

  incorrect_example: |
    rating_format: syntax: "[priority/urgency/date]" priority: type: integer min: 1 max: 100
```

---

## 6. Cross-File Consistency Rules

These rules prevent the most common inter-file defects.

```yaml
cross_file_consistency:

  canonical_key_names:
    rule: >
      All files in one package must use identical key names for the same concept.
      Define all key names once in a binding_decisions or canonical_key_names block
      before generating any file. Verify each file against this dictionary before output.
    defect_found: >
      operator_validation vs operator_review_needed were used interchangeably.
      pin vs pinned were used for the same override action.
      unassigned vs unassigned_if_needed referred to the same section.
      Claude treats different key names as different concepts.

  project_list_single_source:
    rule: >
      The canonical project list is defined once in binding_decisions.
      No per-file content hardcodes the project list.
      Reference it as: "Use project list from binding_decisions.projects.fixed"
    defect_found: >
      The project list was hardcoded in 4 separate per-prompt requirement blocks,
      creating drift risk.

  no_schema_duplication:
    rule: >
      Each schema block appears in one file only (the schema owner).
      Other files that reference the schema write canonical_source only.

  context_carry_forward:
    rule: >
      When generating files sequentially, load all previously generated files
      before writing the next one. Verify: (a) no schema you are about to write
      is already owned by a prior file, (b) all key names match prior files.
```

---

## 7. Non-Goals — Format Rules

Non-goals that are identifiers break Claude's ability to act on them.

```yaml
non_goals_format:
  correct_format: imperative_sentence_starting_with_Do_not
  examples_correct:
    - "Do not create a detailed project database."
    - "Do not create workstreams."
    - "Do not require project IDs in human-facing output."
    - "Do not generate calendar events; produce proposals only."
  examples_incorrect:
    - no_detailed_project_database
    - no_workstreams
    - no_project_ids_required_in_human_output
```

---

## 8. Manifest File Rules

A manifest is an index, not a contract. The v1 manifest became a second
contract document (~600 tokens of redundant file inventory metadata)
and scored 4.0/10 on token efficiency.

```yaml
manifest_rules:
  purpose: lightweight_package_index_only
  max_lines: 60
  per_file_entry_allowed_fields:
    - path
    - purpose_one_sentence
    - read_when_max_3_conditions
  forbidden_in_manifest:
    - validation_role_per_file
    - test_instructions           # these belong in the example file
    - duplicated_acceptance_checks
    - full_file_descriptions
  must_include:
    - package_metadata
    - file_index
    - package_boundaries_flat_list
    - one_acceptance_checks_block_max_8_items
    - read_when_condition_for_the_manifest_itself
```

---

## 9. Prompt Flow Design — Rules for GPT-Driven Generation

When using a GPT agent (especially GPT 5.5 extended thinking) to generate
Claude skill files, the prompt flow itself must follow these rules.

```yaml
prompt_flow_design_rules:

  no_prompt_0:
    rule: >
      Do not use a "package plan validation" prompt as Prompt 0.
      The binding_decisions block IS the plan. Start file generation at Prompt 1.
    token_cost_of_violation: "one full extended-thinking turn wasted"

  binding_decisions_is_single_source:
    rule: >
      All canonical values (project lists, rating syntax, format strings,
      key names) are defined ONLY in binding_decisions.
      Per-prompt requirements reference these values by key name.
      Never hardcode a canonical value inside a per-prompt requirement.

  global_validation_checklist:
    rule: >
      Define one global_validation_checklist covering checks that apply
      to every file. Each per-prompt checklist adds only file-specific items
      (2-3 maximum). GPT applies both silently. GPT does not reprint global
      items in each response.
    token_saving: "~350 tokens per prompt, ~2,450 tokens across 7-prompt flow"

  output_contract_structure:
    every_response_must_follow:
      - "# FILE: <exact target path>"
      - "<complete final file content>"
      - "---"
      - "# VALIDATION — FILE-SPECIFIC CHECKS"
      - "<2-3 file-specific checks only>"
      - "---"
      - "# NEXT PROMPT"
      - "> <pre-filled next instruction>"
    no_commentary_outside_this_structure: true

  self_check_protocol:
    gpt_must_run_before_every_output:
      - yaml_indentation_check
      - description_trigger_check      # SKILL.md only
      - key_name_consistency_check
      - schema_uniqueness_check
      - typed_constraints_check
      - non_goals_format_check
      - procedure_step_count_check     # SKILL.md only
      - failure_modes_present_check    # SKILL.md only
      - completion_gate_format_check   # SKILL.md only
      - forbidden_content_check

  file_schema_ownership:
    rule: >
      Before starting file generation, declare which file owns each schema.
      GPT must verify per file that it is not defining a schema already
      owned by another file in the package.

  canonical_key_names_enforcement:
    rule: >
      Declare a canonical_key_names dictionary in the flow header.
      GPT checks every key name in each generated file against this dictionary
      before outputting. Any mismatch is corrected silently.
```

---

## 10. Validated Scores — Reference Benchmarks

These are the actual before/after scores from the build-audit cycle.
Use as calibration benchmarks for future audits.

```yaml
validated_benchmarks:
  scoring_scale: "0-10 per dimension. Best practice = 9+. Below 6 = rework required."
  dimensions: [MR, TE, RS]  # Machine Readability, Token Efficiency, Resilient Simplicity

  project_status_overview_v1:
    SKILL_md:                    { MR: 6, TE: 5, RS: 7, avg: 6.0 }
    contract_md:                 { MR: 4, TE: 3, RS: 5, avg: 4.0 }
    ranking_and_validation:      { MR: 7, TE: 5, RS: 6, avg: 6.0 }
    package_manifest:            { MR: 5, TE: 3, RS: 4, avg: 4.0 }
    template:                    { MR: 6, TE: 7, RS: 8, avg: 7.0 }
    starter_example:             { MR: 7, TE: 8, RS: 9, avg: 8.0 }
    prompt_flow:                 { MR: 8, TE: 5, RS: 6, avg: 6.3 }

  project_status_overview_v3_after_audit:
    SKILL_md:                    { MR: 10, TE: 9, RS: 9, avg: 9.3 }
    contract_md:                 { MR: 9,  TE: 9, RS: 9, avg: 9.0 }
    notes: "v1→v3 required 2 feedback rounds. Typed constraints defect persisted through v2."

  top_defect_by_frequency:
    rank_1: yaml_indentation_collapse          # affected 5 of 7 files in v1
    rank_2: skill_description_wrong_trigger    # 1 file, highest routing impact
    rank_3: typed_constraints_as_strings       # persisted through v2, required patch
    rank_4: schema_triple_definition           # ~800 wasted tokens in contract file
    rank_5: key_name_inconsistency_across_files
```

---

## 11. Complete Defect Checklist — Run Before Accepting Any File

```yaml
pre_acceptance_defect_checklist:

  yaml:
    - every_yaml_block_has_2_space_indentation: true
    - no_yaml_block_collapsed_to_single_line: true
    - all_yaml_blocks_parse_with_standard_linter: true

  skill_md_only:
    - description_begins_with_Use_this_skill_when: true
    - description_names_trigger_inputs_output_boundary: true
    - description_is_under_80_words: true
    - procedure_has_5_to_8_steps_only: true
    - no_sub_bullets_in_procedure: true
    - failure_modes_section_present_as_yaml_block: true
    - each_failure_mode_has_trigger_and_correction_only: true
    - completion_gate_is_yaml_boolean_block: true
    - supporting_files_is_yaml_block_with_read_when: true
    - no_inline_schemas_that_belong_in_reference_files: true

  all_files:
    - schema_not_defined_in_more_than_one_file: true
    - all_key_names_match_canonical_key_names: true
    - numeric_constraints_use_typed_objects_not_strings: true
    - enum_constraints_use_type_allowed_list: true
    - non_goals_are_imperative_sentences_starting_with_Do_not: true
    - no_forbidden_terms_present: true   # Hermes, draft, source document, citation, etc.
    - no_cross_file_value_duplication: true

  reference_files_only:
    - each_reference_file_owns_exactly_its_declared_schemas: true
    - no_schema_copied_from_another_file: true
    - file_under_target_line_count: true  # contract<100, manifest<60

  prompt_flow:
    - starts_at_prompt_1_no_prompt_0: true
    - canonical_values_in_binding_decisions_only: true
    - global_validation_checklist_defined_once: true
    - per_prompt_checklist_has_max_3_file_specific_items: true
    - file_schema_ownership_declared: true
    - canonical_key_names_dictionary_present: true
    - context_carry_forward_specified_per_prompt: true
```

---

## 12. Quickstart for a New Skill Package

Follow this exact sequence to build a new Claude skill package from scratch.

```yaml
quickstart_sequence:

  step_1_define_before_writing:
    - write binding_decisions block with all canonical values
    - declare canonical_key_names dictionary
    - declare file_schema_ownership map
    - confirm skill_role in one sentence
    - confirm what the skill must NOT do (imperative sentences)

  step_2_generate_SKILL_md_first:
    - enforce description starts with "Use this skill when"
    - use typed constraints in skill_contract.rating_format
    - write 5-8 coarse-grained procedure steps
    - write max 6 failure modes (trigger + correction only)
    - write completion gate as YAML boolean block
    - reference all schemas to their owner files — do not define inline

  step_3_generate_reference_files_in_dependency_order:
    - contract/schema files before validation files
    - validation/rules files after schema files are stable
    - each file: verify schema ownership, verify key names match SKILL.md

  step_4_generate_template_and_example_last:
    - template: blank copy-paste version of the output
    - example: filled realistic data, all ratings marked operator-review-needed
    - verify key names in template match contract file exactly

  step_5_generate_manifest_last:
    - index only: path + one-line purpose + 3 read_when conditions per file
    - under 60 lines total
    - one acceptance_checks block at the end

  step_6_audit_every_file_before_accepting:
    - run pre_acceptance_defect_checklist (Section 11) on every file
    - score MR, TE, RS — must be ≥8 on all three to accept
    - if any score <8, identify the specific defect category and fix before proceeding
```
