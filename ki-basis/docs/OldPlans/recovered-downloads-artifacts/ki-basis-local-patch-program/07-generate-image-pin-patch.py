#!/usr/bin/env python3
from pathlib import Path
import subprocess,json,difflib,re
compose=Path('ki-basis/compose.yaml')
if not compose.exists(): raise SystemExit('Run from apexai-os-meta repository root.')
mapping={
'postgres':('ki-basis-postgres','pgvector/pgvector'),
'valkey':('ki-basis-valkey','valkey/valkey'),
'firefly':('ki-basis-firefly','fireflyiii/core'),
'paperless':('ki-basis-paperless','ghcr.io/paperless-ngx/paperless-ngx'),
'openproject':('ki-basis-openproject','openproject/openproject'),
'nginx':('ki-basis-nginx','nginx'),
'hermes':('ki-basis-hermes','nousresearch/hermes-agent'),
}
def inspect(c): return json.loads(subprocess.check_output(['docker','inspect',c],text=True))[0]
text=compose.read_text(encoding='utf-8-sig'); new=text; pins={}
for service,(container,repo) in mapping.items():
    info=inspect(container); config_image=info['Config']['Image']; digests=info.get('RepoDigests') or []
    cand=[d for d in digests if d.startswith(repo+'@sha256:')]
    if not cand: cand=[d for d in digests if d.split('@',1)[0].endswith('/'+repo) or d.split('@',1)[0]==repo]
    if not cand: raise SystemExit(f'No immutable RepoDigest found for {container} ({config_image}). Do not guess a version.')
    pins[service]=(config_image,cand[0])
for service,(old,digest) in pins.items():
    pat=re.compile(rf'(?ms)(^  {re.escape(service)}:\n.*?^    image:\s*)([^\n#]+)(\s*(?:#.*)?$)')
    m=pat.search(new)
    if not m: raise SystemExit(f'Could not locate image line for {service}')
    new=new[:m.start(2)]+digest+new[m.end(2):]
out=Path('07-image-pins.generated.patch')
diff=''.join(difflib.unified_diff(text.splitlines(True),new.splitlines(True),fromfile='a/ki-basis/compose.yaml',tofile='b/ki-basis/compose.yaml'))
out.write_text(diff,encoding='utf-8')
print('Generated:',out)
for service,(old,digest) in pins.items(): print(f'{service:12} {old} -> {digest}')
print(f'Next: git apply --check {out} && git apply {out}')
