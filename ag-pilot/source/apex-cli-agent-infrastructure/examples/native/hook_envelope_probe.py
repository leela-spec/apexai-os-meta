#!/usr/bin/env python3
"""PROPOSED OFFLINE EXAMPLE: encode a fixed canary, not a rule engine.
Reads JSON stdin, emits JSON stdout. No writes, execution, networking or installation.
The supplied native settings are inert examples. Run in a host only after approval.
"""
import argparse
import json
import sys

CANARY = 'APEX_PROBE_CONTEXT: This is a delivery canary, not authorization or compliance evidence.'
p = argparse.ArgumentParser()
p.add_argument('--platform', choices=['claude', 'antigravity', 'gemini'], required=True)
p.add_argument('--event', required=True)
a = p.parse_args()
payload = json.load(sys.stdin)
if not isinstance(payload, dict):
    raise SystemExit('Expected a JSON object on stdin')
# Host event shapes differ deliberately. Never forward arbitrary prompt text as policy.
if (a.platform, a.event) == ('claude', 'UserPromptSubmit'):
    if payload.get('hook_event_name') != a.event:
        raise SystemExit('Wrong Claude event payload')
    out = {'hookSpecificOutput': {'hookEventName': a.event, 'additionalContext': CANARY}}
elif (a.platform, a.event) == ('antigravity', 'PreInvocation'):
    if not isinstance(payload.get('invocationNum'), int):
        raise SystemExit('Missing Antigravity invocation number')
    out = {'injectSteps': [{'ephemeralMessage': CANARY}]}
elif (a.platform, a.event) == ('gemini', 'BeforeAgent'):
    if payload.get('hook_event_name') != a.event:
        raise SystemExit('Wrong Gemini event payload')
    out = {'hookSpecificOutput': {'additionalContext': CANARY}}
else:
    raise SystemExit('This example supports only documented context-delivery events')
print(json.dumps(out, separators=(',', ':')))
