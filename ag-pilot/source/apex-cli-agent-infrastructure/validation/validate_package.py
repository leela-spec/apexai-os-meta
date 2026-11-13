#!/usr/bin/env python3
"""Read-only cross-artifact checks for this proposed design package.

Requires Python 3.11+, jsonschema and PyYAML. No network, agent host, git command,
configuration installation or source mutation is performed. --write-report is an
explicit optional output. Source/shape checks do not establish native adherence.
"""
from __future__ import annotations
import argparse
import copy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path, PurePosixPath
import posixpath
import re
import sys
import tomllib
import xml.etree.ElementTree as ET
import importlib.metadata

import jsonschema
import yaml

REV = '6c93ad31e42a72de74119218b9365bdd9d6ee386'
XML_PATH = 'apex-meta/informatics/final/specs/apex_contract_v1.0_ultra.xml'

def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--package',type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument('--write-report',type=Path)
    parser.add_argument('--skip-manifest',action='store_true',help='Assembly only; final review must run without this option.')
    args=parser.parse_args();root=args.package.resolve();repo=root/'evidence/repository'
    checks=[]
    def record(id,errors,detail):
        checks.append(dict(id=id,status='pass' if not errors else 'fail',detail=detail,errors=errors))
    def load(p):return json.loads((root/p).read_text(encoding='utf-8'))
    def unique(values):return len(values)==len(set(values))

    # Parse actual deliverables, including examples, without executing them.
    parsed={};errors=[]
    for p in sorted(root.rglob('*.json')):
        if '__pycache__' in p.parts:continue
        try:parsed[p.relative_to(root).as_posix()]=json.loads(p.read_text())
        except Exception as e:errors.append(f'{p.relative_to(root)}: {type(e).__name__}: {e}')
    toml_count=0
    for p in sorted(root.rglob('*.toml')):
        try:tomllib.loads(p.read_text());toml_count+=1
        except Exception as e:errors.append(f'{p.relative_to(root)}: {e}')
    record('PKG-PARSE',errors,{'json_files':len(parsed),'toml_files':toml_count})

    registry=load('registry/rules.json');rules=registry['rules'];ids=[r['id'] for r in rules];idset=set(ids)
    schema=load('registry/rule-registry.schema.json')
    errors=[]
    try:jsonschema.Draft202012Validator.check_schema(schema);jsonschema.Draft202012Validator(schema).validate(registry)
    except Exception as e:errors.append(str(e)[:1500])
    if not unique(ids):errors.append('Duplicate rule IDs')
    if registry['source_revision']!=REV:errors.append('Registry revision mismatch')
    for r in rules:
        missing=set(r['dependencies'])-idset
        if missing:errors.append(f'{r["id"]}: unresolved dependencies {sorted(missing)}')
        seen=set();current=r['id']
        while True:
            if current in seen:errors.append(f'{r["id"]}: owner cycle');break
            seen.add(current);row=next((x for x in rules if x['id']==current),None)
            if row is None:errors.append(f'{r["id"]}: missing owner {current}');break
            nxt=row['canonical_owner']['rule_id']
            if nxt==current:break
            current=nxt
    record('REG-SCHEMA-IDENTITY-OWNERS',errors,{'rules':len(rules),'owner_chains_checked':len(rules)})

    xt=ET.fromstring((repo/XML_PATH).read_bytes());tags={c.tag for c in xt};xmlids={r['id'][4:] for r in rules if r['kind']=='xml_rule'}
    errors=[]
    if tags!=xmlids:errors.append(f'XML tag difference: {sorted(tags^xmlids)}')
    matched_refs=0
    for node in xt:
        if 'ref' not in node.attrib:continue
        matched_refs+=1;target=posixpath.normpath(posixpath.join(xt.attrib['base_ref'],node.attrib['ref']))
        row=next(r for r in rules if r['id']=='XML.'+node.tag)
        if target not in row['activation']['delivery_plan']['required_on_match']:errors.append(f'{row["id"]}: ref missing from required_on_match: {target}')
        if not (repo/target).is_file():errors.append(f'Unresolved current XML ref: {target}')
    record('REG-CURRENT-XML-COVERAGE',errors,{'current_tags':len(tags),'explicit_xml_refs':matched_refs,'exact_set_equality':tags==xmlids})

    errors=[];recorded=0
    for r in rules:
        s=r['source'];p=repo/s['path'];data=p.read_bytes();lines=data.decode('utf-8').splitlines()
        if digest(data)!=s['sha256']:errors.append(f'{r["id"]}: source SHA-256 mismatch')
        win='\n'.join(lines[s['lines']['start']-1:s['lines']['end']])
        if win.strip('\n')!=s['quote'].strip('\n'):errors.append(f'{r["id"]}: exact source excerpt mismatch')
        q=r['source_priority']
        if q['origin']=='recorded':
            recorded+=1
            if q['raw'] not in s['quote']:errors.append(f'{r["id"]}: raw authored tag not in exact excerpt')
            m=re.fullmatch(r'\[(P[0-3])\s*\|\s*I(\d+)/E(\d+)/R(\d+)\]',q['raw'])
            if not m or [q['tier'],q['impact'],q['evidence'],q['risk']]!=[m[1],int(m[2]),int(m[3]),int(m[4])]:errors.append(f'{r["id"]}: source metric mismatch')
        elif any(q[k] is not None for k in ['raw','tier','impact','evidence','risk']):errors.append(f'{r["id"]}: fabricated source metric')
        for pth in r['activation']['delivery_refs']:
            if not (repo/pth).is_file():errors.append(f'{r["id"]}: missing delivery owner {pth}')
    record('REG-SOURCE-QUOTES-PRIORITIES',errors,{'source_excerpts_checked':len(rules),'authored_raw_tags_checked':recorded,'unscored_records_remain_null':len(rules)-recorded})

    sr=load('evidence/repository-sources.json');errors=[]
    for s in sr['sources']:
        p=root/s['snapshot'];data=p.read_bytes();blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        if digest(data)!=s['sha256'] or blob!=s['git_blob_sha1'] or any(v!=blob for v in s['reported_blob_sha1']):errors.append(s['path']+': source integrity mismatch')
        if len(data)!=s['bytes'] or len(data.decode().splitlines())!=s['line_count']:errors.append(s['path']+': source size/line mismatch')
        if s['revision']!=REV:errors.append(s['path']+': revision mismatch')
    record('EVIDENCE-BYTE-FIDELITY',errors,{'snapshots':len(sr['sources']),'exact_path_404_records':len(sr['exact_path_access_gaps'])})

    ext=load('evidence/external-sources.json')['sources'];extids={s['id'] for s in ext};errors=[]
    if len(extids)!=len(ext):errors.append('Duplicate external source IDs')
    for s in ext:
        if not s.get('url','').startswith('https://'):errors.append(s['id']+': non-public/absent primary URL')
    decisions=load('design/decisions.json')['decisions'];decision_ids={d['id'] for d in decisions};options=0
    if len(decision_ids)!=len(decisions):errors.append('Duplicate decision IDs')
    for d in decisions:
        options+=len(d['options']);oids=[o['option_id'] for o in d['options']]
        if len(oids)<2 or not unique(oids) or d['selected_option'] not in oids:errors.append(d['id']+': invalid alternatives/selection')
        if set(d['external_evidence'])-extids:errors.append(d['id']+': missing external evidence')
        for field in ['problem','selection_reason','tradeoff','primary_failure_mode','reconsider_if','originating_decisions','repository_evidence','affected_components']:
            if not d.get(field):errors.append(d['id']+': missing '+field)
        for o in d['options']:
            for key in ['mechanism','grounding','disposition','cost_to_reverse']:
                if not o.get(key):errors.append(d['id']+'/'+o['option_id']+': missing '+key)
            for key in ['impact','evidence','risk']:
                if not isinstance(o['estimate'][key],int) or not 1<=o['estimate'][key]<=100:errors.append(d['id']+': invalid new estimate')
            if o['estimate']['origin']!='new_design_estimate_not_measurement':errors.append(d['id']+': ambiguous estimate origin')
        for component in d['affected_components']:
            if not (root/component).exists():errors.append(d['id']+': unresolved component '+component)
    record('DECISIONS-ALTERNATIVES-EVIDENCE',errors,{'decisions':len(decisions),'options':options,'external_sources':len(ext)})

    integ=load('design/integration-map.json')['entries'];errors=[]
    if not unique([x['id'] for x in integ]):errors.append('Duplicate integration IDs')
    for x in integ:
        if set(x['decision_ids'])-decision_ids:errors.append(x['id']+': unresolved decision')
        if set(x['rule_ids'])-idset:errors.append(x['id']+': unresolved rule')
        if x['existing_path']:
            p=repo/x['existing_path']
            if not p.is_file() or digest(p.read_bytes())!=x['observed_sha256']:errors.append(x['id']+': existing source mismatch')
        elif x['target_state']!='proposed_not_installed':errors.append(x['id']+': ambiguous new target status')
        for material in x['package_material']:
            if not (root/material).exists():errors.append(x['id']+': unresolved package material '+material)
        if x['adoption_stage'] not in ['S0','S1','S2','S3','S4']:errors.append(x['id']+': unknown stage')
    record('INTEGRATION-TRACEABILITY',errors,{'entries':len(integ),'existing_source_entries':sum(bool(x['existing_path']) for x in integ),'new_target_entries':sum(x['existing_path'] is None for x in integ)})

    patches=load('design/pointer-patch-proposals.json')['proposals'];errors=[]
    for x in patches:
        p=repo/x['path'];data=p.read_bytes();s=data.decode()
        if digest(data)!=x['source_sha256'] or s.count(x['old_text'])!=1:errors.append(x['id']+': stale hash or nonunique match')
        if x['applied'] is not False or x['safety']['allow_full_file_rewrite'] is not False:errors.append(x['id']+': incorrect mutation status/safety')
        for link in re.findall(r'\]\(([^)]+)\)',x['new_text']):
            resolved=posixpath.normpath(str(PurePosixPath(x['path']).parent/link))
            if not (repo/resolved).is_file():errors.append(x['id']+': replacement target missing '+resolved)
    record('PATCH-PROPOSALS-EXACTNESS',errors,{'proposals':len(patches),'files':len({x['path'] for x in patches}),'applied':False})

    cs=load('evaluation/cases.json')['cases'];errors=[];focused=set()
    if not unique([c['id'] for c in cs]):errors.append('Duplicate case IDs')
    for c in cs:
        focused.update(c['expected_rule_ids'])
        if set(c['expected_rule_ids'])-idset:errors.append(c['id']+': unresolved focused rule')
        if c['execution_status']!='proposed_unexecuted' or c['measured_results'] is not None:errors.append(c['id']+': unsupported execution/measurement')
        for key in ['prompt','setup','required_observations','oracle','expected_activation']:
            if not c.get(key):errors.append(c['id']+': missing '+key)
        if 'variants' not in c or not isinstance(c['variants'],list):errors.append(c['id']+': variants must be an explicit list; an empty list is valid for a single-condition case')
        for p in c['required_source_refs']:
            path=p.split('#')[0]
            if not (repo/path).is_file():errors.append(c['id']+': unresolved case source '+path)
    expected_xml={'XML.'+tag for tag in tags}
    if expected_xml-focused:errors.append('XML rules without focused case assertions: '+str(sorted(expected_xml-focused)))
    record('EVALUATION-COVERAGE-STATUS',errors,{'cases':len(cs),'focused_xml_id_coverage':len(expected_xml&focused),'explicit_negative_cases':sum(c['negative_case'] for c in cs),'native_agent_trials_executed':0})

    cap=load('compatibility/claims.json')['claims'];probes=load('compatibility/probe-plan.json')['probes'];pids={p['probe_id'] for p in probes};errors=[]
    if not unique([c['claim_id'] for c in cap]):errors.append('Duplicate capability claims')
    for c in cap:
        if set(c['source_ids'])-extids:errors.append(c['claim_id']+': unresolved primary source')
        if set(c['probe_ids'])-pids:errors.append(c['claim_id']+': unresolved probe')
        if not c.get('version_condition') or c['status']!='documented_capability':errors.append(c['claim_id']+': incomplete version/evidence status')
    for p in probes:
        if p['status']!='not_executed':errors.append(p['probe_id']+': unsupported native execution')
    record('CAPABILITY-CLAIMS-PROBES',errors,{'claims':len(cap),'unexecuted_native_probes':len(probes)})

    ss=load('examples/activation-state.schema.json');sample=load('examples/activation-state.example.json');errors=[]
    try:jsonschema.Draft202012Validator.check_schema(ss);jsonschema.validate(sample,ss)
    except Exception as e:errors.append('Proposed sidecar fixture: '+str(e)[:600])
    for mutation in ['authority_promotion','fake_native_pass']:
        bad=copy.deepcopy(sample)
        if mutation=='authority_promotion':bad['authority']={'state':'verified'}
        else:bad['profile']['installed_probe_status']='passed_for_named_conditions'
        try:jsonschema.validate(bad,ss);errors.append('Sidecar admitted '+mutation)
        except jsonschema.ValidationError:pass
    if set(sample['active_rule_ids'])-idset:errors.append('Sidecar unresolved rule')
    record('PROPOSED-STATE-SCHEMA-BOUNDARY',errors,{'positive_fixture':1,'invalid_authority_or_execution_fixtures_rejected':2})

    bake=load('design/architecture-bakeoff.json');weights={c['id']:c['weight'] for c in bake['criteria']};errors=[]
    if abs(sum(weights.values())-1)>1e-9:errors.append('Criterion weights do not sum to one')
    for c in bake['candidates']:
        total=sum(c['criterion_scores'][k]*v for k,v in weights.items())
        if abs(total-c['weighted_criterion_total'])>1e-8:errors.append(c['option_id']+': arithmetic mismatch')
        alt=sum(c['criterion_scores'][k]*v for k,v in bake['sensitivity']['weights'].items())
        if abs(alt-bake['sensitivity']['totals'][c['option_id']])>1e-8:errors.append(c['option_id']+': sensitivity mismatch')
        if c['status']!='new_design_estimate_not_experiment':errors.append(c['option_id']+': ambiguous criterion evidence')
    if not bake['scores_are_not_IER']:errors.append('Criterion scores conflated with IER')
    record('CRITERION-ARITHMETIC-STATUS',errors,{'estimated_candidates':len(bake['candidates']),'IER_aggregations':0})

    errors=[];offline_count=0
    for name in ['offline-results.json','codex-offline-results.json']:
        res=load('examples/native/'+name);offline_count+=len(res['results'])
        if not res['passed'] or res['native_platform_execution'] or any(not row['passed'] for row in res['results']):errors.append(name+': recorded offline failure/status mismatch')
    released=load('compatibility/native-schemas/codex/provenance.json')+load('compatibility/native-schemas/codex/license-provenance.json')
    for f in released:
        data=(root/'compatibility/native-schemas/codex'/f['name']).read_bytes()
        blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        if digest(data)!=f['sha256'] or blob!=f['blob_sha']:errors.append(f['name']+': pinned release integrity mismatch')
    scored=load('evaluation/scorer-probe-results.json')
    if not scored['not_agent_trials'] or len(scored['results'])!=4 or not all(x['finding_confirmed'] for x in scored['results']):errors.append('Scorer diagnostic record mismatch')
    if digest((repo/scored['scorer_source']).read_bytes())!=scored['scorer_sha256']:errors.append('Scorer source hash mismatch')
    record('EXECUTED-DIAGNOSTIC-EVIDENCE',errors,{'offline_native_encoding_schema_checks':offline_count,'synthetic_scorer_counterexamples':len(scored['results']),'pinned_upstream_schema_license_files':len(released),'scope':'Recorded executions plus exact release-copy checks; actual reproduction commands in report. Not native adherence trials.'})

    # New authored Markdown only. Frozen evidence and native configuration examples
    # retain their own original/native schemas rather than receiving OKF fields.
    errors=[];docids=[];authored=[]
    for p in sorted(root.rglob('*.md')):
        rel=p.relative_to(root).as_posix()
        if rel.startswith('evidence/repository/') or '.example.' in p.name:continue
        authored.append(p);text=p.read_text()
        if not text.startswith('---\n'):errors.append(rel+': missing frontmatter');continue
        parts=text.split('---',2)
        try:fm=yaml.safe_load(parts[1])
        except Exception as e:errors.append(rel+': YAML error '+str(e));continue
        for line in parts[1].splitlines():
            if line.strip() and not line.lstrip().startswith('#') and (':' not in line or line.startswith(' ') or line.lstrip().startswith('- ')):errors.append(rel+': nonflat frontmatter')
        if p.name=='index.md' and rel=='index.md':
            if str(fm.get('okf_version'))!='0.2':errors.append('Root index version')
        else:
            for key in ['type','id','title','description','status']:
                if not fm.get(key):errors.append(rel+': missing '+key)
            if fm.get('type') not in ['Specification','Standard','Profile','Adapter','Governance','Policy','Reference']:errors.append(rel+': unsupported concept type')
            docids.append(fm.get('id'))
    if not unique(docids):errors.append('Duplicate authored concept IDs')
    record('AUTHORED-OKF-FRONTMATTER',errors,{'authored_documents':len(authored),'native_and_frozen_source_exclusions':'Native configuration examples use their platform schemas; frozen repository sources are unmodified evidence.'})

    errors=[];links=0
    for p in authored:
        rel=p.relative_to(root).as_posix();text=re.sub(r'```.*?```','',p.read_text(),flags=re.S)
        for match in re.finditer(r'(?<!!)\[[^\]]+\]\(([^)\s]+)(?:\s+"[^"]*")?\)',text):
            link=match[1]
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',link) or link.startswith('#'):continue
            target=link.split('#',1)[0];links+=1
            resolved=(p.parent/target).resolve()
            if not resolved.is_relative_to(root) or not resolved.exists():errors.append(rel+': broken/outside link '+link)
        if re.search(r'https://github\.com/leela-spec/apexai-os-meta',text):errors.append(rel+': repository citation should be root-relative')
    record('AUTHORED-LOCAL-LINKS',errors,{'local_file_links_checked':links,'frozen_snapshot_links':'Preserved as evidence; known original defects have exact unapplied proposals.'})

    errors=[]
    required=['00-START-HERE.md','01-findings.md','02-decisions.md','03-architecture.md','04-integration-map.md','07-validation-report.md','index.md','registry/rules.json','registry/rule-registry.schema.json','registry/history.json','compatibility/compatibility.md','evaluation/evaluation-plan.md','examples/end-to-end-flows.md','evidence/external-sources.json','design/integration-map.json']
    for p in required:
        if not (root/p).is_file():errors.append('Missing required artifact '+p)
    unwanted=[p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and (p.suffix=='.pyc' or '__pycache__' in p.parts or p.name.startswith('build_'))]
    errors.extend('Unwanted build artifact '+p for p in unwanted)
    record('PACKAGE-COMPLETENESS-SANITY',errors,{'required_artifacts':len(required),'source_snapshots_included':True,'production_installation':'not_performed'})

    if not args.skip_manifest:
        errors=[]
        if not (root/'manifest.json').is_file():errors.append('Missing manifest')
        else:
            manifest=load('manifest.json');actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p.name!='manifest.json'};listed={x['path'] for x in manifest['files']}
            if actual!=listed:errors.append('Manifest inventory difference: '+str(sorted(actual^listed)))
            for f in manifest['files']:
                p=root/f['path']
                if not p.is_file() or digest(p.read_bytes())!=f['sha256'] or p.stat().st_size!=f['bytes']:errors.append('Manifest hash/size mismatch '+f['path'])
            if manifest['source_revision']!=REV or manifest['adoption_status']!='proposed_for_operator_review':errors.append('Manifest authority/revision mismatch')
        record('MANIFEST-INVENTORY-HASHES',errors,{'self_hash':'manifest.json intentionally excluded','scope':'All other delivered files'})

    result=dict(schema_version='apex_package_validation.v1',execution_status='executed_artifact_checks',created_at_utc=datetime.now(timezone.utc).isoformat(),source_revision=REV,command='python validation/validate_package.py'+(' --skip-manifest' if args.skip_manifest else ''),runtime=dict(python=sys.version.split()[0],jsonschema=importlib.metadata.version('jsonschema'),PyYAML=importlib.metadata.version('PyYAML')),checks=checks,passed=all(c['status']=='pass' for c in checks),limits=['No native loading, hook invocation, permission or agent adherence trial.','No empirical architecture win established.','Source fidelity and structure do not replace independent semantic review.','Manifest verification is required separately when assembly mode skips it.'])
    if args.write_report:
        args.write_report.parent.mkdir(parents=True,exist_ok=True);args.write_report.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(dict(passed=result['passed'],checks=len(checks),failed=[c for c in checks if c['status']=='fail']),ensure_ascii=False,indent=2))
    return 0 if result['passed'] else 1

if __name__=='__main__':raise SystemExit(main())
