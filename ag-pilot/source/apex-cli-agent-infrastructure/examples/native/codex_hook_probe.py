#!/usr/bin/env python3
"""Offline canary encoder. It does not execute the requested tool or load rules."""
import json
import sys

CANARY = 'APEX_PROBE_CONTEXT: delivery only; no authorization or compliance claim.'
DENY_MARKER = 'APEX_PROBE_DENY'

def encode(payload):
    if not isinstance(payload, dict):
        raise ValueError('Expected an object')
    event = payload.get('hook_event_name')
    if event in {'UserPromptSubmit', 'SessionStart'}:
        return {'hookSpecificOutput': {'hookEventName': event, 'additionalContext': CANARY}}
    if event == 'PreToolUse':
        if payload.get('tool_name') != 'Bash' or not isinstance(payload.get('tool_input'), dict):
            raise ValueError('Canary supports Bash input only')
        if payload['tool_input'].get('command') == DENY_MARKER:
            return {'hookSpecificOutput': {'hookEventName': event, 'permissionDecision': 'deny', 'permissionDecisionReason': 'Offline canary denial; no operation was executed.'}}
        return {}
    raise ValueError('Unsupported canary event')

def semantic_errors(event, out):
    """Deliberately narrow proposed adapter contract, not a complete Codex validator."""
    errors = []
    if event not in {'UserPromptSubmit','SessionStart','PreToolUse'}:
        return ['This adapter has no control or injection contract for this event']
    if not isinstance(out, dict):
        return ['Output must be an object']
    h = out.get('hookSpecificOutput', {})
    if not isinstance(h, dict):
        return ['hookSpecificOutput must be an object']
    if h and h.get('hookEventName') != event:
        errors.append('Output event mismatch')
    if event == 'PreToolUse':
        if h.get('permissionDecision') == 'ask': errors.append('ask is parsed but unsupported')
        if out.get('decision') == 'approve': errors.append('legacy approve is unsupported')
        if out.get('continue') is False: errors.append('continue:false is unsupported')
        if any(k in out for k in ('stopReason','suppressOutput')): errors.append('Unsupported PreToolUse control field')
        if 'updatedInput' in h and h.get('permissionDecision') != 'allow': errors.append('updatedInput requires allow')
    return errors

if __name__ == '__main__':
    try:
        result = encode(json.load(sys.stdin))
    except (ValueError, TypeError) as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)
    print(json.dumps(result, separators=(',', ':')))
