#!/usr/bin/env python3
"""Run the unchanged retained OKF checker on a temporary authored-document view.

No source or live configuration is changed. Native configuration and frozen source
subtrees receive temporary sub-bundle boundaries so their distinct/original schemas
are not misrepresented as newly authored OKF concepts. The exact source files are
copied unchanged; only the temporary boundaries are added to the probe projection.
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--package',type=Path,default=Path(__file__).resolve().parents[1])
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();root=args.package.resolve()
    source=root/'evidence/repository/apex-meta/informatics/final/tools/okf_validator.py'
    dep=source.with_name('check_decision_bakeoff_shape.py')
    boundaries=['evidence/repository','examples/native','compatibility/native-schemas']
    with tempfile.TemporaryDirectory(prefix='apex-authored-okf-') as tmp:
        target=Path(tmp)/'package';shutil.copytree(root,target,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
        for name in boundaries:
            p=target/name/'index.md';p.parent.mkdir(parents=True,exist_ok=True)
            p.write_text('---\nokf_version: "0.2"\ntitle: Probe exclusion boundary\n---\n')
        run=subprocess.run([sys.executable,'-B',str(source),'--target',str(target),'--json'],capture_output=True,text=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
        try:report=json.loads(run.stdout)
        except json.JSONDecodeError:report={'execution_error':run.stderr,'stdout':run.stdout}
        if 'target' in report:report['target']='<temporary-authored-document-projection>'
    out=dict(execution_status='executed_unchanged_retained_validator',native_platform_execution=False,source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),dependency_sha256=hashlib.sha256(dep.read_bytes()).hexdigest(),excluded_subtrees=boundaries,projection_note='Exclusions preserve native configuration schemas and frozen evidence. The final package validator checks every snapshot and machine file separately.',returncode=run.returncode,report=report,interpretation='Raw retained diagnostics. Review errors against actual owner semantics; table-aware independent checks and human review remain necessary. Do not silently convert this report into a zero-error pass.')
    args.output.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'returncode':run.returncode,'okf_errors':report.get('okf_errors'),'apex_profile_errors':report.get('apex_profile_errors'),'advisories':report.get('advisory_warnings')}))
    return 0 if 'execution_error' not in report else 1

if __name__=='__main__':raise SystemExit(main())
