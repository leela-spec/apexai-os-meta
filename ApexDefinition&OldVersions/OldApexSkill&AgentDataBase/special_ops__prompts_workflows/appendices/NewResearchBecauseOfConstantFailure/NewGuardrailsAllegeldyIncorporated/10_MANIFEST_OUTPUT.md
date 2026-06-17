[MANIFEST_OUTPUT v1.0]
TRIGGER: task_type = manifest (multi-file session planning)

JSON OUTPUT SCHEMA:
{
  "output_type": "manifest",
  "task_id":     "TASK-{XX}",
  "project":     "{PROJECT_NAME}",
  "files": [
    {
      "seq":         1,
      "filename":    "{FILENAME_A.ext}",
      "full_path":   "{/absolute/path}",
      "task_type":   "file_write | diff_patch",
      "scope":       "{one-line atomic scope}",
      "depends_on":  null
    },
    {
      "seq":         2,
      "filename":    "{FILENAME_B.ext}",
      "full_path":   "{/absolute/path}",
      "task_type":   "file_write",
      "scope":       "{one-line atomic scope}",
      "depends_on":  1
    }
  ],
  "execution_order": "sequential",
  "total_files":     {n},
  "awaiting_approval": true
}

SERVER RULES:
- Manifest is produced by PLANNER agent — never EXECUTOR
- Server holds manifest until operator sets awaiting_approval=false
- Executor receives one file payload at a time — never full manifest
- depends_on field enforces write order — server blocks out-of-order execution
