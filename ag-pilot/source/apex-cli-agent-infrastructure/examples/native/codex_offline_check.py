#!/usr/bin/env python3
"""Offline artifact validation only; never invokes Codex or any other agent host."""
import hashlib
import json
from pathlib import Path
import sys
import tomllib
import jsonschema
from codex_hook_probe import encode, semantic_errors

here=Path(__file__).resolve().parent
package=here.parents[1]
schemas=package/'compatibility/native-schemas/codex'
names={'PreToolUse':'pre-tool-use.command.output.schema.json','UserPromptSubmit':'user-prompt-submit.command.output.schema.json','SessionStart':'session-start.command.output.schema.json'}
rows=[]
for p in sorted(schemas.glob('*.schema.json')):
    jsonschema.Draft7Validator.check_schema(json.loads(p.read_text()))
    rows.append({'case':'schema_definition_'+p.name,'passed':True,'kind':'schema_meta_validation'})
for f in json.loads((here/'codex-hook-fixtures.json').read_text())['cases']:
    schema=json.loads((schemas/names[f['event']]).read_text())
    shape=jsonschema.Draft7Validator(schema).is_valid(f['output'])
    errors=semantic_errors(f['event'],f['output'])
    sem=not errors
    rows.append({'case':f['case'],'passed':shape==f['expected_schema_valid'] and sem==f['expected_semantic_valid'],'schema_valid':shape,'semantic_valid':sem,'adapter_accepted':shape and sem,'semantic_errors':errors,'kind':'wire_and_semantic_fixture'})
for event,payload in [('UserPromptSubmit',{'hook_event_name':'UserPromptSubmit'}),('SessionStart',{'hook_event_name':'SessionStart'}),('PreToolUse',{'hook_event_name':'PreToolUse','tool_name':'Bash','tool_input':{'command':'APEX_PROBE_DENY'}})]:
    out=encode(payload)
    jsonschema.Draft7Validator(json.loads((schemas/names[event]).read_text())).validate(out)
    rows.append({'case':'encoder_'+event,'passed':not semantic_errors(event,out),'kind':'offline_canary_encoding','output':out})
try:
    encode({'hook_event_name':'PreModelRequest'})
    rejected=False
except ValueError:
    rejected=True
rows.append({'case':'diagnostic_event_rejected','passed':rejected,'kind':'semantic_negative'})
input_payload={'cwd':'/fixture','hook_event_name':'PreToolUse','model':'fixture-model','permission_mode':'default','session_id':'fixture-session','tool_input':{'command':'APEX_PROBE_DENY'},'tool_name':'Bash','tool_use_id':'fixture-call','transcript_path':None,'turn_id':'fixture-turn'}
jsonschema.Draft7Validator(json.loads((schemas/'pre-tool-use.command.input.schema.json').read_text())).validate(input_payload)
rows.append({'case':'pretool_input_shape','passed':True,'kind':'wire_fixture'})
for p in sorted(here.glob('codex-*.example.toml')):
    parsed=tomllib.loads(p.read_text())
    if 'verifier' in p.name:
        ok=all(isinstance(parsed.get(k),str) and parsed[k] for k in ['name','description','developer_instructions']) and not any(k in parsed for k in ['sandbox_mode','approval_policy','mcp_servers'])
    else:
        ok=parsed.get('features',{}).get('hooks') is False and parsed.get('sandbox_mode')=='read-only'
    rows.append({'case':p.name,'passed':bool(ok),'kind':'toml_parse_and_narrow_contract'})
h=json.loads((here/'codex-hooks.example.json').read_text())
rows.append({'case':'codex_hook_container','passed':set(h['hooks'])==set(names),'kind':'json_parse_and_narrow_contract'})
for f in json.loads((schemas/'provenance.json').read_text()):
    data=(schemas/f['name']).read_bytes()
    actual=hashlib.sha256(data).hexdigest()
    blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    rows.append({'case':'digest_'+f['name'],'passed':actual==f['sha256'] and blob==f['blob_sha'],'kind':'release_copy_integrity'})
result={'execution_status':'executed_offline_simulation','native_platform_execution':False,'semantic_adherence_measured':False,'runtime_version_tested':None,'schema_release':'rust-v0.167.2','test_runtime':{'python':sys.version.split()[0],'jsonschema':__import__('importlib.metadata').metadata.version('jsonschema')},'purpose':'Validate copied schema definitions, fixed response envelopes and proposed semantic allowlist. Unsupported native output fields are negative fixtures; no actual native invocation is claimed.','results':rows,'passed':all(r['passed'] for r in rows)}
(here/'codex-offline-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'cases':len(rows),'status':result['execution_status'],'native_execution':False}))
raise SystemExit(0 if result['passed'] else 1)
