# AGENT_PATCH_CONTRACT

version: 1.0
surface: agent_project_instructions
scope: openclaw_patch_runner (openclaw_patch_runner.py)
default_mode: local_packet_patch
default_action: patch_existing_file
new_file_creation_default: forbidden
codex_role: optional_thin_operator

---

## 1. OUTPUT OBLIGATION

The agent MUST produce `.patch.md` files ONLY when exact patch production is possible.
If exact patch production is impossible, the agent MUST produce no `.patch.md` file and MUST report exactly one HALT line.
The agent MUST_NOT produce prose explanations, summaries, reasoning, or commentary outside patch blocks.
The agent MUST_NOT produce unified diffs, `+/-` hunk lines, or full-file rewrites.
The agent MUST_NOT wrap patch content in Markdown fences.
The agent MUST_NOT output language-tagged patch fences such as triple-backtick patch or four-backtick patch.
The agent MUST_NOT output citations, footnotes, contentReference markers, download wrappers, or chat artifacts inside a `.patch.md` file.
The agent MUST patch the existing target file unless the operator explicitly requests new-file creation.
The agent MUST_NOT create `_v2`, replacement, archive, sidecar, or duplicate target files as a workaround.
If the existing target contains forbidden chat artifacts, the agent MUST patch clean neighboring exact text or HALT.

Machine-readable blocker prevention gates:

```yaml
blocker_prevention_rules:
  - if: "output_contains_markdown_fence_wrapper"
    then: "invalid_patch_do_not_emit"
  - if: "output_contains_spaced_delimiter"
    then: "invalid_patch_do_not_emit"
  - if: "output_contains_commented_delimiter"
    then: "invalid_patch_do_not_emit"
  - if: "output_contains_content_reference_or_citation_artifact"
    then: "invalid_patch_do_not_emit"
  - if: "execution_mode_is_local_packet_patch"
    then: "place_patch_file_in_packet_folder_and_use_target_relative_to_packet_folder"
  - if: "execution_mode_is_repo_root_patch"
    then: "place_patch_file_in_repo_root_patches_folder_and_use_target_relative_to_repo_root"
  - if: "exact_current_preimage_is_unavailable"
    then: "emit_no_patch_file_and_report_exactly_one_halt_line"
  - if: "search_text_would_match_zero_or_multiple_times"
    then: "emit_no_patch_file_until_search_text_is_exactly_once_matching"
  - if: "operator_did_not_explicitly_request_new_file_creation"
    then: "patch_existing_target_file_only"
  - if: "target_contains_forbidden_chat_artifact"
    then: "patch_clean_neighboring_exact_text_or_halt"
  - if: "agent_would_create_v2_replacement_or_sidecar_file"
    then: "invalid_patch_do_not_emit"
  - if: "codex_runner_command_is_blocked"
    then: "stop_and_report_blocked_command_no_manual_workaround"
  - if: "upstream_agent_patch_is_malformed_but_intent_is_clear"
    then: "codex_may_translate_once_to_runner_valid_temp_patch"
  - if: "malformed_patch_has_quote_prefixes_markdown_wrappers_or_bad_delimiters"
    then: "strip_or_normalize_in_translated_patch_only"
  - if: "patch_target_name_is_wrong_but_packet_target_is_clear"
    then: "rewrite_target_header_in_translated_patch_only"
  - if: "translated_search_block_mismatches_target"
    then: "codex_may_repair_search_once_using_exact_current_target_snippet"
  - if: "translated_patch_still_fails_after_one_repair"
    then: "report_compact_translation_failure"
  - if: "task_is_small_patch"
    then: "use_bounded_translation_then_one_validation_one_apply"
```

---

## 2. FILE NAMING

Pattern: `TASK-{ID}_{short-description}.patch.md`
Examples:
  VALID:   `TASK-042_fix-auth-redirect.patch.md`
  VALID:   `TASK-001_add-logging.patch.md`
  INVALID: `changes.md`
  INVALID: `patch.txt`
  INVALID: `TASK-042.patch`

---

## 3. FILE PLACEMENT AND TARGET RESOLUTION

Default mode is `local_packet_patch`.

The agent MUST obey the execution mode selected by the operator.

### Mode A: repo_root_patch

Use this mode when the operator says patches go in the repo root patch folder.

```yaml
mode: repo_root_patch
patch_location: "{repo-root}/patches/"
target_resolution: "repo_root_relative"
valid_patch_name: "TASK-{ID}_{desc}.patch.md"
example_target: "OpenClaw/path/from/repo/root/file.md"
```

In `repo_root_patch` mode, every `.patch.md` file MUST be placed in `{repo-root}/patches/`.

### Mode B: local_packet_patch

Use this mode when the operator puts the target file, source files, and patch file in the same working packet folder.

```yaml
mode: local_packet_patch
patch_location: "same directory as target file or packet folder"
target_resolution: "relative_to_patch_file_directory"
valid_patch_name: "TASK-{ID}_{desc}.patch.md"
example_target: "DRPrompt4INf&KBRedesign.md"
```

In `local_packet_patch` mode, the patch file MUST be placed in the packet folder and the `## target:` path MUST be relative to that packet folder.

The agent MUST_NOT place a patch in an arbitrary folder without an explicit execution mode.

---

## 4. ONE FILE PER PATCH

Each `.patch.md` file MUST target EXACTLY one source file.
If a task modifies N files, the agent MUST produce N separate `.patch.md` files.

---

## 5. CANONICAL BLOCK FORMAT

```
## target: <repo-relative/path/to/file.ext>
<<<<<<< SEARCH
<exact current content>
=======
<replacement content>
>>>>>>> REPLACE
```

Rules:
- `## target:` MUST appear before the first SEARCH/REPLACE block in each `.patch.md` file.
- Target path MUST be repo-relative (forward slashes, no leading `/`).
- Target path MUST_NOT be absolute. MUST_NOT escape repo root (`../`).
- `<<<<<<< SEARCH` MUST be spelled exactly including spaces and case.
- `=======` MUST be a bare divider line with no trailing text.
- `>>>>>>> REPLACE` MUST be spelled exactly including spaces and case.
- There MUST be no blank lines or text between `## target:` and the first `<<<<<<< SEARCH`.
- There MUST be no text outside `## target:` headers and SEARCH/REPLACE blocks.

---

## 6. SEARCH CONTENT RULES

- SEARCH content MUST be copied verbatim from the current working tree.
- SEARCH content MUST match the target file character-for-character including whitespace, indentation, and line endings.
- SEARCH content MUST match EXACTLY once in the target file. If the text appears multiple times, the agent MUST expand the SEARCH block to include enough surrounding context to uniquely identify the location.
- SEARCH MUST_NOT be reconstructed from memory, inference, or prior conversation context.
- If the agent does not have access to the exact current file content, it MUST_NOT produce a SEARCH block. It MUST stop and report: `HALT: exact preimage unavailable for <path>`.

---

## 7. NEW FILE CREATION

New-file creation is forbidden by default.

The agent MAY create a new file only when the operator explicitly says to create a new file.

When new-file creation is explicitly allowed, use an empty SEARCH block:

```
## target: path/to/newfile.ext
<<<<<<< SEARCH
=======
<full content of new file>
>>>>>>> REPLACE
```

The parent directory MUST already exist in the repo. MUST_NOT invent directory structure.
The agent MUST_NOT use new-file creation to avoid patching a difficult existing file.

---

## 8. MULTI-BLOCK SAME FILE

Multiple SEARCH/REPLACE blocks for the same target file MUST appear in one `.patch.md` file under a single `## target:` header.

```
## target: src/module.py
<<<<<<< SEARCH
old_line_a
=======
new_line_a
>>>>>>> REPLACE
<<<<<<< SEARCH
old_line_b
=======
new_line_b
>>>>>>> REPLACE
```

Each block MUST target a unique, non-overlapping region of the file.

---

## 9. MULTI-FILE TASK

If a task requires changes to `src/a.py`, `src/b.py`, and `tests/test_a.py`, the agent MUST produce three separate files.

In `repo_root_patch` mode:
- `patches/TASK-007_update-a.patch.md`       -> `## target: src/a.py`
- `patches/TASK-007_update-b.patch.md`       -> `## target: src/b.py`
- `patches/TASK-007_update-tests.patch.md`   -> `## target: tests/test_a.py`

In `local_packet_patch` mode:
- `TASK-007_update-a.patch.md`       -> `## target: src/a.py`
- `TASK-007_update-b.patch.md`       -> `## target: src/b.py`
- `TASK-007_update-tests.patch.md`   -> `## target: tests/test_a.py`

MUST_NOT combine multiple targets into one `.patch.md` file.

---

## 10. VALID EXAMPLE

File: `patches/TASK-012_rename-constant.patch.md`

```
## target: src/config.py
<<<<<<< SEARCH
MAX_RETRIES = 3
=======
MAX_RETRIES = 5
>>>>>>> REPLACE
```

---

## 11. INVALID EXAMPLES

INVALID -- Markdown fence wrapper around patch:
```
````patch
## target: file.md
...
````
```

INVALID -- spaced delimiter:
```
> > > > > > > REPLACE
```

INVALID -- commented delimiter:
```
# <<<<<<< SEARCH
```

INVALID -- chat artifact:
```
::contentReference[oaicite:3]{index=3}
```


INVALID -- prose outside blocks:
```
This patch updates the retry count.
## target: src/config.py
<<<<<<< SEARCH
MAX_RETRIES = 3
=======
MAX_RETRIES = 5
>>>>>>> REPLACE
```

INVALID -- absolute path:
```
## target: /home/user/repo/src/config.py
```

INVALID -- multiple targets in one file:
```
## target: src/a.py
<<<<<<< SEARCH
...
=======
...
>>>>>>> REPLACE
## target: src/b.py
<<<<<<< SEARCH
...
=======
...
>>>>>>> REPLACE
```

INVALID -- invented SEARCH content:
```
## target: src/config.py
<<<<<<< SEARCH
MAX_RETRIES = 3  # (agent assumed this exists)
=======
MAX_RETRIES = 5
>>>>>>> REPLACE
```

---

## 12. FAILURE BEHAVIOR

| Condition | Required agent behavior |
|---|---|
| Exact current file content unavailable | `HALT: exact preimage unavailable for <path>` -- do not emit SEARCH block |
| SEARCH would match 0 times | `HALT: patch_check_fail -- no match in <path>` |
| SEARCH would match >1 times | Expand SEARCH block to uniquely identify location; if impossible, `HALT: ambiguous match in <path>` |
| Target path escapes repo root | `HALT: invalid target path <path>` |
| Task requires changes to multiple files | Produce one `.patch.md` per file; never combine |

---

## 13. RUNNER COMMANDS (minimal reference)

Default local packet validate only:
```powershell
C:\GitDev\_openclaw_patch_tool\ocpatch.cmd patch-dir-validate C:\path\to\packet
```

Default local packet validate then apply:
```powershell
C:\GitDev\_openclaw_patch_tool\ocpatch.cmd patch-dir-apply C:\path\to\packet
```

Repo-root validate only:
```powershell
C:\GitDev\_openclaw_patch_tool\.venv\Scripts\python.exe C:\GitDev\_openclaw_patch_tool\openclaw_patch_runner.py validate C:\GitDev\{RepoName}
```

Repo-root validate then apply:
```powershell
C:\GitDev\_openclaw_patch_tool\.venv\Scripts\python.exe C:\GitDev\_openclaw_patch_tool\openclaw_patch_runner.py apply C:\GitDev\{RepoName}
```

Local packet validate only:
```powershell
C:\GitDev\_openclaw_patch_tool\.venv\Scripts\python.exe C:\GitDev\_openclaw_patch_tool\openclaw_patch_runner.py patch-dir-validate C:\path\to\packet
```

Local packet validate then apply:
```powershell
C:\GitDev\_openclaw_patch_tool\.venv\Scripts\python.exe C:\GitDev\_openclaw_patch_tool\openclaw_patch_runner.py patch-dir-apply C:\path\to\packet
```

The runner validates ALL patches atomically before writing ANY file. If any patch fails, NO files are modified.

---

## 14. CODEX OPTIONAL EXECUTION RULES

Codex MAY execute patch validation/application for the operator using only short `ocpatch.cmd` commands.

```yaml
codex_optional_execution:
  role: "thin_operator"
  allowed_commands:
    - "ocpatch.cmd patch-file-validate <packet-folder> <patch-file>"
    - "ocpatch.cmd patch-file-apply <packet-folder> <patch-file>"
    - "ocpatch.cmd patch-dir-validate <packet-folder>"
    - "ocpatch.cmd patch-dir-apply <packet-folder>"
  forbidden_actions:
    - "manual target rewrite"
    - "manual patch application through ad hoc scripts"
    - "long inline Python commands during normal operation"
    - "creating _v2 or replacement files unless explicitly requested"
    - "copying files between folders unless explicitly requested"
  blocked_command_behavior:
    - "stop"
    - "report exact blocked command"
    - "do not improvise a workaround"
  response_budget:
    - "report validation result"
    - "report apply result"
    - "avoid long narration unless validation fails"
```
