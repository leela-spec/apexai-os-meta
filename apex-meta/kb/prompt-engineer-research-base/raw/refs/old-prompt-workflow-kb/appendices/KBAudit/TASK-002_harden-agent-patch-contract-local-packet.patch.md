## target: AGENT_PATCH_CONTRACT.md
<<<<<<< SEARCH
## 1. OUTPUT OBLIGATION

The agent MUST produce `.patch.md` files ONLY when exact patch production is possible.
If exact patch production is impossible, the agent MUST produce no `.patch.md` file and MUST report exactly one HALT line.
The agent MUST_NOT produce prose explanations, summaries, reasoning, or commentary outside patch blocks.
The agent MUST_NOT produce unified diffs, `+/-` hunk lines, or full-file rewrites.
=======
## 1. OUTPUT OBLIGATION

The agent MUST produce `.patch.md` files ONLY when exact patch production is possible.
If exact patch production is impossible, the agent MUST produce no `.patch.md` file and MUST report exactly one HALT line.
The agent MUST_NOT produce prose explanations, summaries, reasoning, or commentary outside patch blocks.
The agent MUST_NOT produce unified diffs, `+/-` hunk lines, or full-file rewrites.
The agent MUST_NOT wrap patch content in Markdown fences.
The agent MUST_NOT output language-tagged patch fences such as triple-backtick patch or four-backtick patch.
The agent MUST_NOT output citations, footnotes, contentReference markers, download wrappers, or chat artifacts inside a `.patch.md` file.

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
```
>>>>>>> REPLACE
<<<<<<< SEARCH
## 3. FILE PLACEMENT

The agent MUST place every `.patch.md` file in the `patches/` directory at the root of the target repo.
ONLY: `{repo-root}/patches/TASK-{ID}_{desc}.patch.md`
MUST_NOT place patches anywhere else in the repo.
=======
## 3. FILE PLACEMENT AND TARGET RESOLUTION

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
>>>>>>> REPLACE
<<<<<<< SEARCH
## 9. MULTI-FILE TASK

If a task requires changes to `src/a.py`, `src/b.py`, and `tests/test_a.py`, the agent MUST produce three separate files:
- `patches/TASK-007_update-a.patch.md`       -> `## target: src/a.py`
- `patches/TASK-007_update-b.patch.md`       -> `## target: src/b.py`
- `patches/TASK-007_update-tests.patch.md`   -> `## target: tests/test_a.py`

MUST_NOT combine multiple targets into one `.patch.md` file.
=======
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
>>>>>>> REPLACE
<<<<<<< SEARCH
## 11. INVALID EXAMPLES
=======
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

>>>>>>> REPLACE
<<<<<<< SEARCH
## 13. RUNNER COMMANDS (minimal reference)

Validate only (no file writes):
```powershell
C:\GitDev\_openclaw_patch_tool\.venv\Scripts\python.exe C:\GitDev\_openclaw_patch_tool\openclaw_patch_runner.py validate C:\GitDev\{RepoName}
```

Validate then apply:
```powershell
C:\GitDev\_openclaw_patch_tool\.venv\Scripts\python.exe C:\GitDev\_openclaw_patch_tool\openclaw_patch_runner.py apply C:\GitDev\{RepoName}
```

The runner validates ALL patches atomically before writing ANY file. If any patch fails, NO files are modified.
=======
## 13. RUNNER COMMANDS (minimal reference)

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
>>>>>>> REPLACE
