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
