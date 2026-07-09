---
name: deterministic-markdown-patcher2
description: >
  Use this skill when the operator asks for deterministic Markdown, frontmatter, or config patch planning/execution. Accepts natural-language change requests, patch_intent.json, patch_policy.json, or executor reports. Produces semantic patch intents, validation guidance, or executor-based mutation reports. Does not hand-author unified diffs or mutate files directly when an executor is available.
---

# Deterministic Markdown Patcher 2

## Skill Contract

```yaml
skill_contract:
  primary_output: patch_intent_or_execution_report
  output_role: deterministic_patch_control_plane
  accepted_inputs:
    type: list
    allowed:
      - natural_language_change_request
      - patch_intent_json
      - patch_policy_json
      - executor_report_json
  architecture:
    planner_ai: semantic_intent_and_replacement_content
    executor: live_target_resolution_and_bounded_mutation
    proof: git_generated_diff_after_mutation
  schema_owners:
    patch_intent: references/patch-intent-schema.json
    patch_policy: references/patch-policy.schema.json
  boundaries:
    - Do not mutate Markdown, frontmatter, or config files directly when an approved executor is available.
    - Do not use AI-authored unified diffs as the primary executable artifact.
    - Do not use line numbers, line ranges, or hunk offsets as executable mutation targets.
    - Do not require AI-authored old_text as executable input.
    - Do not continue when live target resolution is ambiguous.
```

## Supporting Files

```yaml
supporting_files:
  - path: references/patch-intent-schema.json
    read_when:
      - creating_patch_intent
      - validating_patch_intent
  - path: references/patch-policy.schema.json
    read_when:
      - creating_patch_policy
      - validating_patch_policy
  - path: references/executor-contract.md
    read_when:
      - invoking_executor
      - reviewing_executor_report
  - path: references/tool-classification.md
    read_when:
      - classifying_tools
      - checking_core_boundary
  - path: references/failure-modes.md
    read_when:
      - resolving_failure
      - writing_failure_report
  - path: templates/patch_intent.template.json
    read_when:
      - drafting_patch_intent_example
  - path: templates/patch_policy.template.json
    read_when:
      - drafting_patch_policy_example
  - path: templates/fixture_spec.template.json
    read_when:
      - drafting_fixture_example
```

## Procedure

1. Classify the request as intent drafting, policy drafting, executor invocation, validation review, or failure analysis; produce the matching route before loading details.
2. Load only the supporting files needed for the route; identify the schema owner or contract that controls the next artifact.
3. Create semantic patch intents that name the operation, target file guess, heading path or nearby phrases as hints, replacement content, validation expectations, and safety constraints; produce valid JSON when an intent artifact is requested.
4. Validate policy constraints against the target paths, allowed operations, protected paths, report directory, and validation commands; reject any path or operation outside policy.
5. Use the approved executor for live file resolution and mutation when available; require it to resolve exact spans, frontmatter, or heading sections before writing.
6. Review executor output, git diff proof, and validation results; accept only bounded changes to allowed paths with passing checks.
7. Produce the requested intent, report, or failure packet; when any condition in Failure Modes applies, stop normal completion and apply that correction.

## Failure Modes

```yaml
failure_modes:
  target_path_outside_allowlist:
    trigger: The target path is not covered by patch_policy.path_allowlist or is covered by patch_policy.protected_paths.
    correction: Stop and report the rejected path with the governing policy field.
  zero_target_matches:
    trigger: The executor cannot resolve any live target from the supplied hints.
    correction: Stop and request stronger semantic anchors or a different operation.
  multiple_target_matches:
    trigger: The executor resolves more than one viable target span or heading path.
    correction: Stop and report candidate locations without mutating files.
  duplicate_or_ambiguous_heading_path:
    trigger: The heading path is missing, duplicated, or insufficient to isolate one section.
    correction: Stop and require a full unique heading path or a narrower target file.
  frontmatter_missing_when_required:
    trigger: A frontmatter operation targets a file without a parseable frontmatter block.
    correction: Stop unless policy explicitly allows creating frontmatter for that path.
  validation_failed:
    trigger: A validation command, fixture, schema check, or diff-scope check fails.
    correction: Roll back or leave the worktree unchanged and emit the failing command output.
  diff_touches_unallowed_path:
    trigger: Git diff includes a path outside the approved mutation scope.
    correction: Stop, roll back the mutation, and report every unallowed path.
  optional_tool_requested_as_core:
    trigger: The plan depends on a trial-only or rejected tool as the core mutator.
    correction: Replace it with the Python executor path or mark the request as unsupported.
```

## Output Requirements

```yaml
output_requirements:
  patch_intent:
    format: valid_json
    schema_owner: references/patch-intent-schema.json
    must_include_semantic_hints: true
    must_not_include_executable_old_text: true
  patch_policy:
    format: valid_json
    schema_owner: references/patch-policy.schema.json
    full_file_rewrite_default: false
  executor_report:
    include_operation_status: true
    include_resolved_target_summary: true
    include_git_diff_reference: true
    include_validation_results: true
    include_failure_report_when_failed: true
  direct_response:
    state_whether_executor_was_available: true
    state_whether_mutation_was_performed: true
```

## Completion Gate

```yaml
completion_gate:
  frontmatter_has_only_name_and_description: true
  description_begins_with_use_this_skill_when: true
  supporting_files_have_path_and_read_when_only: true
  schemas_are_referenced_by_owner: true
  patch_intent_avoids_executable_old_text: true
  ai_authored_unified_diff_is_not_primary_input: true
  direct_markdown_mutation_forbidden_when_executor_available: true
  ambiguity_fails_closed: true
  output_matches_requested_artifact_type: true
```
