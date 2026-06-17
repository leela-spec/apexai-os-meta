[FILE_OUTPUT v1.0]
TRIGGER: task_type = file_write

JSON OUTPUT SCHEMA:
{
  "output_type":      "file_write",
  "task_id":          "TASK-{XX}",
  "filename":         "{FILENAME.ext}",
  "repo_path":        "{/absolute/path}",
  "full_path":        "{repo_path}/{filename}",
  "scope_confirmed":  "{repeat task scope verbatim}",
  "content":          "{complete file content as escaped string}",
  "line_count":       {n},
  "scope_respected":  true,
  "additions_beyond_scope": null
}

SERVER WRITE PROTOCOL:
1. Parse response JSON
2. Validate: scope_respected=true AND additions_beyond_scope=null
3. Write content to full_path (create or overwrite)
4. Run blob-equality check if task_type was move-only
5. On validation fail: discard output, trigger HALT, log violation
6. On success: pass to STATE_KEEPER for TASK_CLOSURE

FORBIDDEN IN CONTENT STRING:
- Markdown headers not in original spec
- Added commentary or inline notes
- Structural additions beyond task scope
