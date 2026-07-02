import os
os.makedirs("output/openclaw", exist_ok=True)

templates = {}

# ── TEMPLATE 00: SYSTEM BOOTSTRAP ──────────────────────────────────────────
templates["00_SYSTEM_BOOTSTRAP"] = """\
[OPENCLAW_SYSTEM_BOOTSTRAP v1.0]
RUNTIME: server-side | Hetzner cloud | API-native
AGENT_ROLE: {executor | planner | verifier | state_keeper}
MODEL_PIN: {gpt-5-mini | gpt-5-nano | gpt-4.1} ← never use "auto" or "latest"
TEMPERATURE: 0.0
MAX_TOKENS: {set per task type — see TEMPLATE_01}
STREAM: false ← disable for structured output integrity

EXECUTION_CONTRACT:
- one_task_per_api_call: true
- no_scope_expansion: true
- no_implicit_state_inference: true
- output_format: machine_readable_only
- forbidden: [prose_explanation, markdown_headers_in_json, nested_unspecified_keys]

AUTHORITY_HIERARCHY:
  L0: SYSTEM_PROMPT ← immutable, set at server init
  L1: STATE_BLOCK ← injected per call, read-only
  L2: TASK_PAYLOAD ← per-call instruction
  L3: AGENT_REASONING ← lowest priority, never overrides L0-L2

GATE_PROTOCOL:
- Before execution: agent outputs GATE_CHECK block (see TEMPLATE_08)
- On constraint violation detected: output HALT block (see TEMPLATE_09)
- On ambiguity: output CLARIFY block (see TEMPLATE_09). Do not proceed.
"""

# ── TEMPLATE 01: API CALL STRUCTURE ─────────────────────────────────────────
templates["01_API_CALL_STRUCTURE"] = """\
[API_CALL_STRUCTURE v1.0]
PURPOSE: standard payload structure for every OpenClaw agent API call

PAYLOAD:
{
  "model": "{MODEL_PIN}",
  "temperature": 0.0,
  "max_tokens": {
    "file_write":     4096,
    "diff_patch":     2048,
    "state_update":   512,
    "research_block": 8192,
    "gate_check":     256,
    "clarify":        128
  }[task_type],
  "response_format": {"type": "json_object"},
  "messages": [
    {"role": "system",    "content": "{SYSTEM_BOOTSTRAP + AGENT_ROLE}"},
    {"role": "user",      "content": "{STATE_BLOCK + TASK_PAYLOAD}"}
  ]
}

RULES:
- system message = BOOTSTRAP only. Never inject task here.
- user message = STATE_BLOCK first, TASK_PAYLOAD second. Always.
- No conversation history injected. State is passed via STATE_BLOCK only.
- response_format json_object enforced on all calls except raw file writes.
- Each call is stateless. Agent never reads prior call outputs from context.
"""

# ── TEMPLATE 02: STATE BLOCK (SERVER-INJECTED) ───────────────────────────────
templates["02_STATE_BLOCK"] = """\
[STATE_BLOCK v1.0]
PURPOSE: replaces chat history — injected at top of every user message

FORMAT (JSON — parsed server-side before injection):
{
  "state": {
    "project":          "{PROJECT_NAME}",
    "session_id":       "{YYYY-MM-DD}-{seq}",
    "active_agent":     "{executor | planner | verifier}",
    "active_task_id":   "TASK-{XX}",
    "completed_tasks":  ["TASK-01", "TASK-02"],
    "last_written_file": "{FILENAME.ext | null}",
    "active_constraints": [
      "mode:move-only",
      "output:single-artifact-per-call",
      "forbidden:restructure,expand,rewrite"
    ],
    "open_items":       [{"id": "TASK-03", "description": "{...}"}],
    "repo_path":        "{/absolute/server/path/to/repo}",
    "next_task":        "TASK-03"
  }
}

SERVER RULES:
- State file lives at: /openclaw/state/{PROJECT_NAME}.json
- Updated by STATE_KEEPER agent after every successful TASK_CLOSURE
- Never updated by executor agent directly
- On state read failure: HALT. Do not proceed with stale state.
"""

# ── TEMPLATE 03: TASK PAYLOAD ────────────────────────────────────────────────
templates["03_TASK_PAYLOAD"] = """\
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
"""

# ── TEMPLATE 04: OUTPUT ROUTER ───────────────────────────────────────────────
templates["04_OUTPUT_ROUTER"] = """\
[OUTPUT_ROUTER v1.0]
PURPOSE: maps task_type to exact output schema — agent selects and follows

ROUTE_TABLE:
┌─────────────────┬──────────────────────────────────────────────┐
│ task_type       │ output_schema                                │
├─────────────────┼──────────────────────────────────────────────┤
│ file_write      │ TEMPLATE_05: FILE_OUTPUT                     │
│ diff_patch      │ TEMPLATE_06: DIFF_OUTPUT                     │
│ research_block  │ TEMPLATE_07: RESEARCH_OUTPUT                 │
│ state_update    │ TEMPLATE_02: STATE_BLOCK (write mode)        │
│ manifest        │ TEMPLATE_10: MANIFEST_OUTPUT                 │
│ gate_check      │ TEMPLATE_08: GATE_CHECK                      │
│ clarify/halt    │ TEMPLATE_09: CONTROL_SIGNALS                 │
└─────────────────┴──────────────────────────────────────────────┘

RULE: agent outputs ONLY the schema for its assigned task_type.
      Any additional keys or prose outside schema = SCOPE_VIOLATION.
"""

# ── TEMPLATE 05: FILE OUTPUT ─────────────────────────────────────────────────
templates["05_FILE_OUTPUT"] = """\
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
"""

# ── TEMPLATE 06: DIFF OUTPUT ─────────────────────────────────────────────────
templates["06_DIFF_OUTPUT"] = """\
[DIFF_OUTPUT v1.0]
TRIGGER: task_type = diff_patch

JSON OUTPUT SCHEMA:
{
  "output_type":    "diff_patch",
  "task_id":        "TASK-{XX}",
  "target_file":    "{/absolute/full_path.ext}",
  "patch_content":  "--- a/{filename}\\n+++ b/{filename}\\n@@ ... @@\\n{unified diff}",
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
"""

# ── TEMPLATE 07: RESEARCH OUTPUT ─────────────────────────────────────────────
templates["07_RESEARCH_OUTPUT"] = """\
[RESEARCH_OUTPUT v1.0]
TRIGGER: task_type = research_block

JSON OUTPUT SCHEMA:
{
  "output_type":  "research_block",
  "task_id":      "TASK-{XX}",
  "topic":        "{bounded topic string}",
  "format":       "bullets | table | numbered | prose",
  "depth":        "surface | standard | exhaustive",
  "content":      "{output in declared format — no additional structure}",
  "sources":      [{"label": "{name}", "ref": "{url or filename}"}],
  "scope_respected": true,
  "recommendations_included": false
}

RULES:
- recommendations_included must be false unless task explicitly requested them
- content key contains only the declared format — no mixed formats
- sources array empty if no external refs used — never omit key
- If depth=exhaustive and content approaches 8192 tokens:
    set "split_required": true, "part": 1, "parts_total": {n}
    server triggers continuation call automatically
"""

# ── TEMPLATE 08: GATE CHECK ──────────────────────────────────────────────────
templates["08_GATE_CHECK"] = """\
[GATE_CHECK v1.0]
TRIGGER: first output of every agent call — before any task execution

JSON OUTPUT SCHEMA:
{
  "gate_check": {
    "task_id":              "TASK-{XX}",
    "agent_role":           "{executor | planner | verifier}",
    "task_type_understood": "{file_write | diff_patch | ...}",
    "scope_understood":     "{repeat scope from payload verbatim}",
    "target_file":          "{filename | null}",
    "active_constraints":   ["{list from state}"],
    "ambiguity_detected":   false,
    "ready_to_execute":     true
  }
}

SERVER RULES:
- Server parses gate_check BEFORE allowing agent to produce task output
- If ambiguity_detected=true: server triggers CLARIFY flow (TEMPLATE_09)
- If ready_to_execute=false: server triggers HALT (TEMPLATE_09)
- Gate check max_tokens: 256 — agent must be concise
- Gate check is a separate API call — not prepended to task output call
"""

# ── TEMPLATE 09: CONTROL SIGNALS ─────────────────────────────────────────────
templates["09_CONTROL_SIGNALS"] = """\
[CONTROL_SIGNALS v1.0]
PURPOSE: HALT and CLARIFY signals — terminate or pause execution safely

HALT SCHEMA:
{
  "signal":    "HALT",
  "task_id":   "TASK-{XX}",
  "reason":    "constraint_violation | state_read_failure | patch_check_fail | scope_exceeded",
  "detail":    "{one-line machine-readable description}",
  "safe_state": true,
  "recovery":  "manual_review_required | retry_with_corrected_payload | split_task"
}

CLARIFY SCHEMA:
{
  "signal":    "CLARIFY",
  "task_id":   "TASK-{XX}",
  "question":  "{one specific question — one dimension only}",
  "blocking":  "{the exact ambiguous field in TASK_PAYLOAD}",
  "options":   ["{option_a}", "{option_b}"]
}

SERVER RULES:
- On HALT: write to /openclaw/logs/halts.jsonl. Stop all downstream calls.
- On CLARIFY: pause task queue. Route question to operator interface.
- No agent proceeds past a HALT in its call chain.
- HALT logs are append-only — never overwritten.
"""

# ── TEMPLATE 10: MANIFEST OUTPUT ─────────────────────────────────────────────
templates["10_MANIFEST_OUTPUT"] = """\
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
"""

# ── TEMPLATE 11: TASK CLOSURE (STATE KEEPER) ─────────────────────────────────
templates["11_TASK_CLOSURE"] = """\
[TASK_CLOSURE v1.0]
TRIGGER: after every successful file write, diff apply, or research output
AGENT: STATE_KEEPER only

JSON OUTPUT SCHEMA:
{
  "closure": {
    "task_id":                "TASK-{XX}",
    "output_type":            "{file_write | diff_patch | research_block}",
    "filename":               "{FILENAME.ext | null}",
    "full_path":              "{/absolute/path | null}",
    "scope_respected":        true,
    "additions_beyond_scope": null,
    "state_update": {
      "add_to_completed":     "TASK-{XX}",
      "update_last_written":  "{FILENAME.ext}",
      "set_next_task":        "TASK-{XX+1} | null"
    },
    "log_entry": "{YYYY-MM-DD}T{HH:MM:SS}Z | TASK-{XX} | {output_type} | {filename} | OK"
  }
}

SERVER WRITE PROTOCOL:
1. Parse closure JSON
2. Update /openclaw/state/{PROJECT}.json with state_update values
3. Append log_entry to /openclaw/logs/task_log.jsonl
4. If set_next_task != null: enqueue next task payload
5. If set_next_task = null: set project status = COMPLETE
"""

for name, content in templates.items():
    path = f"output/openclaw/{name}.md"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Files written:")
for name in templates:
    print(f"  output/openclaw/{name}.md")