
# Claude Skill Package Prompt Flow — Design Guidance for GPT Agents
# Version: 1.0
# Audience: GPT model operating in extended-thinking mode
# Scope: Structural and formatting rules for generating Claude-native SKILL.md packages
# NOT scope: Any specific skill content, domain logic, or project-specific decisions

```yaml
guidance_metadata:
  purpose: >
    Provide GPT with the precise structural, formatting, and sequencing rules
    required to generate Claude-native skill packages that pass machine
    readability, token efficiency, and resilient simplicity validation.
  derived_from:
    - audit of project-status-overview skill package v1 (all 7 files)
    - comparison against validated v2/v3 SKILL.md and contract files
    - defect pattern analysis across 3 review cycles
  applies_to: any_future_claude_skill_package_generation
  does_not_apply_to: skill_domain_logic_or_content_decisions
```

---

# PART 1 — Defect Inventory from Observed Prompt Flow

These are the precise failure modes the previous prompt flow produced.
Every item is a structural or formatting defect, not a content decision.

```yaml
observed_defects:

  defect_01:
    id: yaml_indentation_collapse
    severity: critical
    description: >
      All YAML blocks in generated files were collapsed to single-line strings
      with no indentation. This makes every block unparseable by Claude and
      unreadable by humans.
    affected_files_in_audit:
      - project-status-overview-contract.md
      - ranking-and-validation-rules.md
      - package-manifest.md
      - current-project-status-overview-template.md
      - starter-manual-test-overview.md
    root_cause: >
      The prompt flow did not instruct GPT to produce properly indented YAML.
      GPT defaulted to prose-like YAML output that collapsed during rendering.
    fix_required: >
      Every prompt must explicitly state: produce all YAML blocks with correct
      2-space indentation. After generating each file, verify that every YAML
      block is parseable as valid YAML before outputting.

  defect_02:
    id: skill_description_wrong_pattern
    severity: critical
    description: >
      The SKILL.md description field used action verbs at the start
      ('create, normalize, update...') instead of Claude's trigger-intent
      pattern. Claude routes skills based on intent phrases, not action verb lists.
    root_cause: >
      The prompt flow said 'description must clearly trigger when the operator
      asks Claude to...' but did not enforce the exact opening phrase pattern
      that Claude's routing uses.
    fix_required: >
      Every SKILL.md description MUST begin with the exact phrase:
      "Use this skill when"
      followed by the trigger condition. This is not stylistic — it is the
      routing key Claude matches against.
    correct_example: >
      "Use this skill when the operator asks to create, update, normalize,
      rank, or validate a compact cross-project project status overview."
    incorrect_example: >
      "create, normalize, update, rank, or validate a compact cross-project
      project status overview from manual notes..."

  defect_03:
    id: procedure_over_granularity
    severity: high
    description: >
      The procedure was decomposed into 27 steps across 8 phases for a skill
      that has 6 logical actions. Steps were split at the sub-action level,
      not the phase level. This burns tokens on every invocation and makes the
      skill harder to follow, not easier.
    root_cause: >
      The prompt specified a 10-item numbered requirement list for the
      procedure. GPT expanded each requirement into multiple sub-steps.
    fix_required: >
      Procedures must be written at the phase/action grain:
      one step = one complete action with one observable outcome.
      Target: 5-8 steps for a standard single-responsibility skill.
      Never split one logical action across multiple numbered steps.
    correct_grain_example:
      - "Sort material. Assign project-specific content to projects. Put
         unresolved items in Unassigned. Remove from Unassigned once assigned."
    incorrect_grain_example:
      - "3. Separate material that clearly belongs to a project from material
         that is still unassigned."
      - "4. Put unresolved incoming infos, tasks, and project candidates into
         an Unassigned section only when they cannot yet be placed."
      - "5. Remove an item from Unassigned once it has been assigned."

  defect_04:
    id: supporting_files_prose_format
    severity: high
    description: >
      Supporting file references were written as prose bullet points with
      natural-language load conditions. Claude cannot reliably parse
      natural-language load conditions to determine when to load each file.
    root_cause: >
      The prompt specified 'Reference supporting files' with a bullet list.
      No machine-readable read_when conditions were required.
    fix_required: >
      Supporting files must always be a YAML block with a path field and
      a read_when list of snake_case condition identifiers per file.
      Never use prose bullets for supporting file references.
    correct_pattern: |
      ```yaml
      supporting_files:
        - path: references/some-contract.md
          read_when:
            - validating_output_structure
            - operator_asks_for_contract_fields
      ```

  defect_05:
    id: missing_failure_modes_section
    severity: high
    description: >
      The SKILL.md had no Failure Modes section. Claude had no recovery
      path for missing input, invalid data, or constraint violations.
    root_cause: >
      The prompt flow did not include a Failure Modes requirement for SKILL.md.
    fix_required: >
      Every SKILL.md must include a Failure Modes section as a YAML block.
      Each failure mode must have exactly two fields:
        trigger: one sentence describing the condition
        correction: one sentence describing the required response
      8 failure modes or fewer. More than 8 suggests the skill scope is too broad.

  defect_06:
    id: completion_gate_as_prose_bullets
    severity: medium
    description: >
      The completion gate was a prose bullet list. Claude cannot use a prose
      bullet list as a machine-checkable gate condition.
    fix_required: >
      Completion gate must be a YAML boolean checklist. Every check is a
      snake_case key with value: true. Claude evaluates each key before
      marking the skill complete.
    correct_pattern: |
      ```yaml
      completion_gate:
        hierarchy_is_project_task_subtask: true
        ratings_use_priority_urgency_date: true
        ranked_task_view_present: true
      ```

  defect_07:
    id: rating_format_as_display_strings
    severity: medium
    description: >
      Rating type constraints were written as human-readable strings
      ("integer 1-100") rather than typed validation objects. Claude reads
      these as string values, not as enforced constraints.
    affected_in: skill_contract.rating_format, contract.rating_contract
    root_cause: >
      The prompt specified 'priority 1-100, urgency 1-100' as plain text
      requirements. GPT wrote them as display labels, not typed objects.
    fix_required: >
      Numeric range constraints must always use typed validation objects:
        type: integer
        min: <value>
        max: <value>
      String constraints must use:
        type: string
        allowed: [<value_list>]
    correct_pattern: |
      priority:
        type: integer
        min: 1
        max: 100
      date:
        type: string
        allowed: ["DD-MM", "NA"]

  defect_08:
    id: schema_triple_definition
    severity: critical
    description: >
      The contract file defined the same schema three times across three
      separate sections: artifact_contract, Normalized Structure, and
      Section Contracts. This cost approximately 800 redundant tokens per load.
    root_cause: >
      The prompt specified multiple requirement bullets that each triggered
      a full schema definition. GPT interpreted these as additive and
      generated each independently.
    fix_required: >
      Define each schema EXACTLY ONCE. Reference by key name elsewhere.
      If the prompt specifies multiple structural requirements, GPT must
      merge them into one canonical block, not repeat per requirement.

  defect_09:
    id: non_goals_as_identifier_keys
    severity: low
    description: >
      Non-goals were written as snake_case identifier keys
      (no_detailed_project_database) rather than imperative sentences.
      Identifiers are ambiguous; Claude cannot act on them as instructions.
    fix_required: >
      Non-goals must be written as short imperative sentences:
      "Do not create a detailed project database."
      Not as identifiers: no_detailed_project_database

  defect_10:
    id: key_name_inconsistency_across_files
    severity: medium
    description: >
      The same concept used different key names in different files:
      - operator_validation vs operator_review_needed
      - pin vs pinned (for ranking override action)
      - unassigned vs unassigned_if_needed (for section name)
      Claude treats different key names as different concepts.
    root_cause: >
      The prompt flow defined canonical names in binding_decisions but
      did not enforce them per-prompt. Each prompt independently named
      its own keys.
    fix_required: >
      The flow must declare a canonical_key_names block in the global
      rules section. Every per-prompt output must be verified against
      this dictionary before acceptance.

  defect_11:
    id: prompt_0_wasted_turn
    severity: medium
    description: >
      Prompt 0 consumed one full GPT extended-thinking turn to produce a
      package plan that was then discarded. All decisions in Prompt 0 were
      already encoded in binding_decisions at the top of the flow.
    fix_required: >
      Remove Prompt 0 entirely. The binding_decisions block IS the package
      plan. Start file generation at Prompt 1. If operator review of the
      plan is needed before generation, make it a pre-flow operator gate,
      not a GPT-generated output.

  defect_12:
    id: validation_checklist_repetition
    severity: medium
    description: >
      Each prompt had its own VALIDATION CHECKLIST repeating 6-8 identical
      items with only 1-2 file-specific variations. Across 7 prompts this
      created ~280 tokens of repeated boilerplate.
    fix_required: >
      Define a global_validation_checklist in the flow header covering the
      universal checks that apply to every file. Each per-prompt checklist
      adds only file-specific items (2-3 maximum). Instruct GPT to apply
      both lists, not to reprint the global list per prompt.

  defect_13:
    id: canonical_values_defined_in_multiple_places
    severity: medium
    description: >
      canonical_projects_initial was defined in binding_decisions and then
      hardcoded again inside the requirements text of Prompts 3, 4, and 5.
      GPT has two sources for the same value, which can drift.
    fix_required: >
      All canonical values (project lists, format strings, key names) must
      be defined ONLY in binding_decisions. Per-prompt requirements must
      reference binding_decisions by key name, never hardcode values.
      Instruction pattern: "Use canonical_projects_initial from
      binding_decisions. Do not redefine the list here."

  defect_14:
    id: per_prompt_requirements_restating_output_file
    severity: medium
    description: >
      Prompt 5 (ranking-and-validation-rules) listed 13 requirement bullets
      that were nearly identical to the content of the generated file.
      The prompt restated the entire file specification as requirements,
      then GPT wrote the same content as output. Net value: zero.
    fix_required: >
      Per-prompt requirements must specify STRUCTURE and CONSTRAINTS,
      not content. If the content is fully predetermined, compress requirements
      to: structural pattern, max 3 content constraints, reference to
      binding_decisions for all values.

  defect_15:
    id: manifest_became_second_contract
    severity: high
    description: >
      The package-manifest.md grew into a second contract file with 600+
      tokens of file inventory metadata, repeated acceptance checks, and
      manual test instructions. A manifest is an index, not a contract.
    root_cause: >
      The prompt specified: 'For each file include purpose, when Claude
      should read it, validation role.' This triggered GPT to write a
      full documentation entry per file.
    fix_required: >
      Manifest prompts must specify: file path + one-line purpose +
      read_when (3 conditions max). No validation_role. No test instructions
      (those belong in the example file). Target: under 60 lines total.
```

---

# PART 2 — Mandatory Rules for Every Future Claude Skill Prompt Flow

```yaml
mandatory_flow_rules:

  rule_01_yaml_indentation:
    applies_to: every_generated_file
    instruction: >
      All YAML blocks must use 2-space indentation. Nested objects must be
      indented relative to their parent. Lists use "- " prefix at the
      correct indentation level. After generating each file, perform a
      self-check: read each YAML block and verify it would parse with a
      standard YAML parser. If any block is flat or collapsed, regenerate it.
    enforcement: per_file_self_check_before_output

  rule_02_description_trigger:
    applies_to: every_SKILL_md_frontmatter
    instruction: >
      The description field of every SKILL.md frontmatter MUST begin with
      the exact string: "Use this skill when"
      The trigger condition follows immediately. The description must also
      name: (1) what input is accepted, (2) what output is produced,
      (3) what the skill explicitly does not do.
      Maximum length: 75 words.
    enforcement: string_match_check_before_accepting_SKILL_md

  rule_03_procedure_grain:
    applies_to: every_SKILL_md_procedure_section
    instruction: >
      Each procedure step = one complete action + one observable outcome.
      Target step count: 5-8 for single-responsibility skills.
      Do not split one logical action across multiple steps.
      Do not include sub-bullets under procedure steps.
      If a procedure exceeds 10 steps, flag it as a scope violation.
    enforcement: step_count_check_and_single_action_per_step_check

  rule_04_supporting_files_format:
    applies_to: every_SKILL_md_supporting_files_section
    instruction: >
      Supporting files section must always be a YAML block.
      Each entry must have exactly two fields: path and read_when.
      read_when must be a list of snake_case identifiers.
      No prose bullets. No natural language load conditions.
    enforcement: yaml_block_format_check

  rule_05_failure_modes_required:
    applies_to: every_SKILL_md
    instruction: >
      Every SKILL.md must contain a Failure Modes section as a YAML block.
      Each failure mode has exactly: trigger (one sentence) and
      correction (one sentence). Maximum 8 failure modes. If the skill
      needs more than 8, the skill scope must be narrowed.
    enforcement: section_presence_check_and_field_count_per_mode

  rule_06_completion_gate_format:
    applies_to: every_SKILL_md
    instruction: >
      Completion gate must be a YAML block of boolean checks.
      Format: snake_case_check_name: true
      Target: 6-10 checks. No prose. No bullet lists.
    enforcement: yaml_boolean_format_check

  rule_07_typed_constraints:
    applies_to: any_numeric_or_enum_constraint_in_any_file
    instruction: >
      Numeric range constraints: use type/min/max, not string labels.
      Enum constraints: use type/allowed list, not prose.
      Never write "integer 1-100" as a string.
      Always write: type: integer / min: 1 / max: 100
    enforcement: constraint_type_check_before_accepting_schema_blocks

  rule_08_single_schema_definition:
    applies_to: every_contract_and_reference_file
    instruction: >
      Each schema or contract structure must be defined EXACTLY ONCE.
      If multiple sections need to reference the same structure, use a
      key reference, not a copy. If a prompt inadvertently creates a
      duplicate definition, merge into one canonical block before output.
    enforcement: duplicate_key_scan_before_output

  rule_09_canonical_key_names:
    applies_to: every_file_in_the_package
    instruction: >
      All files in one package must use identical key names for the same
      concept. Before generating each file, load the canonical_key_names
      dictionary from binding_decisions and verify all keys match.
      Do not introduce synonyms or alternative names for established keys.
    enforcement: key_name_cross_check_against_binding_decisions

  rule_10_no_prompt_0:
    applies_to: flow_structure
    instruction: >
      Do not generate a package plan as a separate prompt turn.
      binding_decisions in the flow header IS the plan.
      Begin file generation at Prompt 1 (SKILL.md).
      If operator review is needed before generation, the operator must
      approve binding_decisions manually before running Prompt 1.
    enforcement: flow_starts_at_prompt_1

  rule_11_global_validation_checklist:
    applies_to: flow_structure
    instruction: >
      Define one global_validation_checklist in the flow header containing
      all checks that apply to every generated file. Per-prompt checklists
      must contain ONLY file-specific checks (2-3 maximum).
      GPT applies both lists to every file. GPT does not reprint the global
      list inside each prompt output.
    enforcement: global_list_defined_once_per_prompt_list_is_delta_only

  rule_12_binding_decisions_is_single_source:
    applies_to: all_per_prompt_requirements
    instruction: >
      All canonical values (lists, formats, key names, metric syntax) live
      only in binding_decisions. Per-prompt requirements reference these
      values by key name. Never hardcode a canonical value inside a
      per-prompt requirement block.
      Pattern: "Use canonical_projects_initial from binding_decisions."
      Anti-pattern: "Use projects: Leela, Apex, MasterOfArts..."
    enforcement: canonical_value_reference_check_per_prompt

  rule_13_manifest_is_an_index:
    applies_to: package_manifest_generation_prompt
    instruction: >
      The package manifest must be an index only. Each file entry:
        - path: exact file path
        - purpose: one sentence maximum
        - read_when: list of 3 conditions maximum
      No validation_role field. No test instructions. No acceptance checks
      beyond a single must_pass list of 5-8 boolean items.
      Target total manifest length: under 60 lines.
    enforcement: line_count_check_and_no_validation_role_field

  rule_14_non_goals_as_imperatives:
    applies_to: non_goals_sections_in_any_file
    instruction: >
      Non-goals must be written as short imperative sentences beginning
      with "Do not". Never as snake_case identifiers.
    correct: "Do not create a detailed project database."
    incorrect: "no_detailed_project_database"
    enforcement: string_pattern_check_on_non_goals_list

  rule_15_no_cross_file_schema_duplication:
    applies_to: files_within_same_package
    instruction: >
      If File A defines a schema (e.g. rating_contract), File B must not
      redefine it. File B may include a one-line reference:
        canonical_source: path/to/file-a.md
      Only one file owns each schema. The prompt flow must assign ownership
      explicitly in the file_schema_ownership block.
    enforcement: ownership_declaration_required_per_schema
```

---

# PART 3 — Required Flow Structure for Future Prompts

```yaml
required_flow_structure:

  header:
    required_blocks:
      - prompt_flow_metadata
      - binding_decisions
      - canonical_key_names        # NEW — was missing in prior flow
      - file_schema_ownership      # NEW — was missing in prior flow
      - global_output_contract
      - global_validation_checklist  # NEW — replaces per-prompt repetition
      - allowed_paths
      - forbidden_outputs
      - language_rules

  prompt_flow_metadata_required_fields:
    - id
    - target_skill_name
    - output_mode                  # must be: one_file_per_prompt
    - file_creation_location       # must be: chat_output_only
    - claude_skill_package_version # NEW — version of the skill format targeted

  binding_decisions_required_fields:
    - skill_role_one_sentence
    - hierarchy_allowed_levels
    - hierarchy_forbidden_levels
    - canonical_output_format
    - canonical_key_names          # all key names used across files
    - metric_format_with_typed_constraints
    - non_goals_as_imperatives

  file_schema_ownership:
    description: >
      Declares which file is the canonical owner of each named schema.
      No other file may redefine an owned schema.
    format: |
      file_schema_ownership:
        rating_contract: references/ranking-and-validation-rules.md
        task_contract: references/project-contract.md
        subtask_contract: references/project-contract.md
        validation_record: references/project-contract.md

  global_validation_checklist_required_items:
    - exactly_one_file_produced: true
    - file_path_matches_allowed_paths: true
    - all_yaml_blocks_are_indented: true
    - no_claude_native_key_violations: true
    - no_schema_defined_more_than_once: true
    - all_key_names_match_canonical_key_names: true
    - no_prose_in_non_goal_list: true
    - no_forbidden_output_types_present: true

  per_prompt_required_fields:
    - target_path                  # exact allowed path
    - file_type                    # skill_main | contract | template | example | reference | manifest
    - schema_ownership_note        # which schemas this file owns (or references only)
    - context_carry_forward        # which previously generated files must be loaded
    - structure_constraints        # STRUCTURE only — not content
    - max_3_content_constraints    # content-specific rules maximum 3
    - file_specific_checklist      # 2-3 items only, delta from global

  context_carry_forward_rule:
    instruction: >
      Every prompt after Prompt 1 must explicitly list which previously
      generated files GPT must load before generating the current file.
      This ensures cross-file key name consistency.
    format: |
      context_carry_forward:
        load_before_generating:
          - .claude/skills/skill-name/SKILL.md  # for key name alignment
```

---

# PART 4 — Claude SKILL.md Canonical Structure

This is the exact section sequence every SKILL.md must follow.
No sections may be added. No sections may be removed.
Section names must match exactly.

```yaml
SKILL_md_canonical_sections:
  order:
    1: frontmatter           # YAML frontmatter block: name + description only
    2: "# <Skill Name>"      # H1 heading matching the name field
    3: "## Skill Contract"   # YAML block: output, hierarchy, format, ratings, ranking, boundaries
    4: "## Supporting Files" # YAML block: path + read_when per file
    5: "## Procedure"        # Numbered steps, prose, no sub-bullets
    6: "## Failure Modes"    # YAML block: trigger + correction per mode
    7: "## Output Requirements"  # YAML block: required_sections + section rules
    8: "## Completion Gate"  # YAML boolean checklist

  frontmatter_rules:
    allowed_fields: [name, description]
    forbidden_fields: [version, status, author, tags, any_other_field]
    description_must_start_with: "Use this skill when"
    description_max_words: 75

  skill_contract_required_keys:
    - primary_output
    - output_role
    - hierarchy
    - compact_format
    - rating_format           # must use typed constraints
    - ranking_order
    - boundaries.must_not_create

  procedure_rules:
    step_format: "N. **Verb phrase.** Outcome sentence."
    max_steps: 8
    min_steps: 4
    no_sub_bullets: true
    failure_mode_reference_required_in_last_step: true

  failure_modes_rules:
    format: yaml_block
    per_mode_fields: [trigger, correction]
    max_modes: 8
    no_prose_outside_yaml: true

  output_requirements_rules:
    required_keys:
      - required_sections       # list of section names
      - per_section_rules       # one sub-block per required section
    key_names_must_match: canonical_key_names_in_binding_decisions

  completion_gate_rules:
    format: yaml_boolean_block
    all_values_must_be: true
    min_checks: 6
    max_checks: 12
```

---

# PART 5 — Self-Check Protocol for GPT Before Outputting Each File

GPT must run this protocol before outputting any file in the flow.
If any check fails, correct the file before outputting it.

```yaml
pre_output_self_check:

  check_01_yaml_parse:
    instruction: "Read every YAML block. Verify indentation is correct and the block would parse. If any block is flat or collapsed, fix it."
    fail_action: regenerate_affected_yaml_block

  check_02_description_trigger:
    applies_to: SKILL_md_only
    instruction: "Verify description starts with 'Use this skill when'. If not, rewrite the opening."
    fail_action: rewrite_description_opening

  check_03_key_name_consistency:
    instruction: "Compare every key name in the file against canonical_key_names in binding_decisions. Any mismatch must be corrected."
    fail_action: replace_noncanonical_key_names

  check_04_schema_uniqueness:
    instruction: "Scan for any schema that is already defined in a previously generated file per file_schema_ownership. If found, replace with canonical_source reference."
    fail_action: remove_duplicate_replace_with_reference

  check_05_typed_constraints:
    instruction: "Scan for any string that looks like 'integer N-M' or 'N-M'. Replace with typed object: type/min/max or type/allowed."
    fail_action: convert_string_constraints_to_typed_objects

  check_06_non_goals_format:
    instruction: "Scan non_goals list. Every item must start with 'Do not'. Replace any snake_case identifier with an imperative sentence."
    fail_action: rewrite_non_goals_as_imperatives

  check_07_procedure_step_count:
    applies_to: SKILL_md_only
    instruction: "Count procedure steps. If fewer than 4 or more than 8, flag as scope issue and request operator guidance before proceeding."
    fail_action: flag_and_pause

  check_08_failure_modes_present:
    applies_to: SKILL_md_only
    instruction: "Verify Failure Modes section exists as a YAML block. If missing, add it before outputting."
    fail_action: add_failure_modes_section

  check_09_completion_gate_format:
    applies_to: SKILL_md_only
    instruction: "Verify completion gate is a YAML boolean block. If it is a prose list, convert it."
    fail_action: convert_to_yaml_boolean_block

  check_10_manifest_line_count:
    applies_to: manifest_file_only
    instruction: "Count total lines. If more than 60, identify what expanded beyond index scope and trim."
    fail_action: trim_to_index_only_content
```
