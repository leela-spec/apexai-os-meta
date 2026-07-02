# PATCH_PROCESS_PLAN

version: 1.0
default_mode: local_packet_patch
goal: "Patch existing files in-place with minimal token and command overhead."

---

## Correct Process

```yaml
process:
  mode: local_packet_patch
  folder_rule: "target file and .patch.md file live in the same packet folder"
  target_rule: "## target is relative to the packet folder"
  apply_rule: "validate all patches first; apply none if any patch fails"
  default_action: "patch_existing_file"
  new_file_creation: "forbidden unless operator explicitly requests it"
```

## Operator Commands

```powershell
C:\GitDev\_openclaw_patch_tool\ocpatch.cmd patch-dir-validate .
C:\GitDev\_openclaw_patch_tool\ocpatch.cmd patch-dir-apply .
```

Run these commands from the packet folder, or replace `.` with the packet folder path.

## Agent Contract

```yaml
agent_must:
  - "read AGENT_PATCH_CONTRACT.md"
  - "produce exactly one TASK-{ID}_{desc}.patch.md per target file"
  - "use ## target relative to the packet folder"
  - "copy SEARCH text exactly from the current target file"
  - "patch the existing target file"
agent_must_not:
  - "create _v2 files unless explicitly requested"
  - "wrap patch content in markdown fences"
  - "include contentReference, citations, explanations, or chat artifacts"
  - "use spaced or commented delimiters"
  - "copy the patch to another repo or folder"
```

## Failure Handling

```yaml
if_then:
  - if: "exact SEARCH text is unavailable"
    then: "HALT; do not emit a patch file"
  - if: "SEARCH text includes forbidden chat artifact"
    then: "use clean neighboring exact text or HALT"
  - if: "SEARCH would match zero times"
    then: "HALT; do not emit a patch file"
  - if: "SEARCH would match more than once"
    then: "expand SEARCH context until exactly once or HALT"
  - if: "runner command is blocked"
    then: "stop; do not manually apply the patch as a workaround"
```

## Token-Efficiency Rule

Use the short wrapper commands. Do not run long inline Python commands during normal operation.

## Learning: Token-Efficient Patch Translation Layer

The 2026-05-09 PreCap patch attempt showed that upstream AI-generated patch files should be treated as patch intent, not trusted executable patch files. The efficient operator job is to translate malformed patch-shaped material into one runner-valid `.patch.md`, then let the Python runner validate and apply it.

Simple explanation of the failure:
- The source patch was not directly executable by the Python runner.
- The target filename in the patch did not exactly match the real local target filename.
- The patch delimiters and quoting were malformed.
- The agent treated this as a normal runner failure instead of running a cheap translation step.
- Too much context was spent inspecting, explaining, and recovering instead of converting the bad patch into a clean patch file and validating once.

```yaml
token_efficiency_learning:
  failure_observed: "small patch consumed excessive Codex tokens because malformed upstream patch intent was not translated into runner-valid format first"
  next_time_default: "expect upstream patch files to be malformed; run bounded translation; validate translated patch; apply only through runner"
  patch_input_classification:
    executable_patch: "already matches AGENT_PATCH_CONTRACT and runner validates"
    patch_intent: "contains intended SEARCH/REPLACE or edit instructions but has malformed delimiters, wrong target name, quote prefixes, markdown wrappers, or chat artifacts"
    unusable_intent: "does not identify target, old text, and replacement text clearly enough to translate"
  bounded_translation_budget:
    max_packet_listing_commands: 1
    max_source_patch_reads: 1
    max_target_snippet_reads: 2
    max_translation_attempts: 1
    max_validation_commands_after_translation: 1
  if_then:
    - if: "upstream_patch_is_runner_valid"
      then: "validate_and_apply_with_runner"
    - if: "upstream_patch_is_patch_intent_not_runner_valid"
      then: "translate_to_temp_runner_valid_patch_once_then_validate"
    - if: "source_has_quote_prefixes_or_markdown_fences"
      then: "strip wrappers_in_temp_patch_only"
    - if: "source_has_malformed_delimiters"
      then: "normalize_to_exact_SEARCH_DIVIDER_REPLACE_delimiters_in_temp_patch_only"
    - if: "target_filename_is_ambiguous"
      then: "resolve_by_one_packet_file_listing_and_user_instruction_context"
    - if: "patch_header_target_differs_from_real_target_but_intent_is_clear"
      then: "rewrite_target_header_in_temp_patch_only"
    - if: "translated_SEARCH_block_mismatch_occurs"
      then: "repair_SEARCH_once_by_exact_target_snippet_if_replacement_intent_is_clear"
    - if: "SEARCH_still_mismatch_after_one_exact_snippet_repair"
      then: "HALT_with_compact_translation_failure"
    - if: "runner_wrapper_fails_due_to_shell_path_issue"
      then: "use direct python runner command once; do not write custom scripts"
    - if: "manual_edit_is_needed_to_finish_after_translation_failure"
      then: "state_that_this_is_outside_patch_process_then_do_scoped_exact_replacements_only_if_user_orders_finish_anyway"
  compact_report_format:
    - "Classified input: executable_patch|patch_intent|unusable_intent"
    - "Translated: YES|NO"
    - "Validated: PASS|FAIL"
    - "Applied: YES|NO"
    - "Changed files: explicit list"
  temp_patch_rule: "translated patch lives in temp or packet-local scratch only; target file stays in original packet folder; no _v2 sidecar"
```

## Codex Optional Loop

```yaml
codex_role:
  allowed:
    - "run ocpatch.cmd patch-file-validate"
    - "run ocpatch.cmd patch-file-apply"
    - "run ocpatch.cmd patch-dir-validate"
    - "run ocpatch.cmd patch-dir-apply"
    - "report compact pass/fail output"
  forbidden:
    - "manual target rewrite when validation fails"
    - "manual patch application through ad hoc scripts"
    - "long inline Python commands during normal operation"
    - "copying patches or target files between folders without explicit operator request"
    - "creating _v2 files unless explicitly requested"
  on_blocked_command:
    - "stop"
    - "report exact blocked command"
    - "do not improvise a workaround"
```

Normal Codex response shape:

```text
Validated: <patch-file> (<N> blocks)
Applied: <target-file>
```
