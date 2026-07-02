[TASK_PAYLOAD v1.0]
PURPOSE: per-call task instruction — injected after STATE_BLOCK

FORMAT:
{
  "task": {
    "id":          "TASK-{XX}",
    "type":        "file_write | diff_patch | research_block | state_update | manifest",
    "target_file": "{FILENAME.ext | null}",
    "repo_path":   "{/absolute/path | inherit_from_state}",
    "scope":       "{one-line atomic description — no compound tasks}",
    "output_format": "see OUTPUT_ROUTER (TEMPLATE_04)",
    "constraints": ["inherit_from_state", "{additional_if_any}"],
    "input_refs":  ["{filename or null — files agent may read}"],
    "forbidden":   ["{explicit list — overrides general constraints if stricter}"]
  }
}

RULES:
- scope must be one sentence. If not: server rejects payload before sending.
- compound tasks (AND/THEN in scope) → split into separate API calls.
- input_refs: only files explicitly listed may be read. No directory scans.
- target_file must be absolute path if type=file_write or diff_patch.
