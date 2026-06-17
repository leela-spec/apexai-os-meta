[DIFF_OUTPUT v1.0]
TRIGGER: task_type = diff_patch

JSON OUTPUT SCHEMA:
{
  "output_type":    "diff_patch",
  "task_id":        "TASK-{XX}",
  "target_file":    "{/absolute/full_path.ext}",
  "patch_content":  "--- a/{filename}\n+++ b/{filename}\n@@ ... @@\n{unified diff}",
  "lines_added":    {n},
  "lines_removed":  {n},
  "hunks":          {n},
  "scope_respected": true,
  "apply_command":  "git apply --check {task_id}.patch && git apply {task_id}.patch"
}

SERVER APPLY PROTOCOL:
1. Write patch_content to /openclaw/patches/{task_id}.patch
2. Run: git apply --check {task_id}.patch
3. On check pass: git apply {task_id}.patch
4. On check fail: HALT — do not force apply. Log diff + error.
5. Fetch-back: read written file, confirm hunk count matches.

RULES:
- Never full-file replacement when diff is possible
- Max 3 context lines per hunk
- One logical change per hunk
