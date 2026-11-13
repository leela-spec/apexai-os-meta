#!/usr/bin/env python3
"""Deterministic envelope-fixture checks only. Does not launch any agent host."""
import json
from pathlib import Path
import subprocess
import sys
p=Path(__file__).resolve().parent
fixtures=json.loads((p/'offline-fixtures.json').read_text())
rows=[]
for f in fixtures:
 r=subprocess.run([sys.executable,str(p/'hook_envelope_probe.py'),'--platform',f['platform'],'--event',f['event']],input=json.dumps(f['input']),capture_output=True,text=True)
 out=json.loads(r.stdout) if r.returncode==0 else None
 if f['platform']=='claude':
  ok=r.returncode==0 and out['hookSpecificOutput']['hookEventName']=='UserPromptSubmit' and 'APEX_PROBE_CONTEXT:' in out['hookSpecificOutput']['additionalContext']
 elif f['platform']=='antigravity':
  ok=r.returncode==0 and 'APEX_PROBE_CONTEXT:' in out['injectSteps'][0]['ephemeralMessage'] and 'permissionOverrides' not in out
 else:
  ok=r.returncode==0 and 'APEX_PROBE_CONTEXT:' in out['hookSpecificOutput']['additionalContext']
 rows.append({'case':f['platform']+'_context_envelope','passed':bool(ok),'stdout':out,'exit_code':r.returncode})
# Wrong host/event combinations must not silently emit a malformed host envelope.
for platform,event,payload in [('claude','PreInvocation',{}),('antigravity','PreInvocation',{}),('gemini','BeforeAgent',{'hook_event_name':'AfterAgent'})]:
 r=subprocess.run([sys.executable,str(p/'hook_envelope_probe.py'),'--platform',platform,'--event',event],input=json.dumps(payload),capture_output=True,text=True)
 rows.append({'case':platform+'_invalid_event_or_payload','passed':r.returncode!=0 and not r.stdout,'exit_code':r.returncode,'stderr':r.stderr.strip()})
for fp in sorted(p.glob('*.example.json')):
 json.loads(fp.read_text())
 rows.append({'case':fp.name+'_parse','passed':True})
result={'execution_status':'executed_offline_simulation','native_platform_execution':False,'semantic_adherence_measured':False,'purpose':'Check JSON parseability and platform-specific envelope conversion, including negative fixtures.','results':rows,'passed':all(r['passed'] for r in rows)}
(p/'offline-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'cases':len(rows),'status':result['execution_status']}))
raise SystemExit(0 if result['passed'] else 1)
