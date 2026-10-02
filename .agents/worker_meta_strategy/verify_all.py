import os
import json

deep_audit = r'c:\GitDev\apexai-os-meta\FutureDevelopments&Research\AgentAudit\PerAgentDeepDives\META_STRATEGY_DEEP_AUDIT.md'
unified_doc = r'c:\GitDev\apexai-os-meta\FutureDevelopments&Research\AgentAudit\PerAgentDeepDives\META_STRATEGY_UNIFIED_DOCTRINE.md'

assert os.path.exists(deep_audit), 'Missing META_STRATEGY_DEEP_AUDIT.md'
assert os.path.getsize(deep_audit) > 10000, 'META_STRATEGY_DEEP_AUDIT.md too small'
print('Passed: META_STRATEGY_DEEP_AUDIT.md', os.path.getsize(deep_audit), 'bytes')

assert os.path.exists(unified_doc), 'Missing META_STRATEGY_UNIFIED_DOCTRINE.md'
assert os.path.getsize(unified_doc) > 10000, 'META_STRATEGY_UNIFIED_DOCTRINE.md too small'
print('Passed: META_STRATEGY_UNIFIED_DOCTRINE.md', os.path.getsize(unified_doc), 'bytes')

staged_root = r'C:\Quasi Desktop\AI_PreperationUntil_06-26\LostAgents\MetaStrategy'
staged_files = []
for root, dirs, files in os.walk(staged_root):
    for f in files:
        p = os.path.join(root, f)
        assert os.path.exists(p)
        sz = os.path.getsize(p)
        assert sz > 0, f'File {p} is empty'
        staged_files.append((p, sz))

print(f'Passed: Staged files count = {len(staged_files)} (all non-empty)')

# Check all 41 census files
matrix = json.load(open(r'c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit\agent_knowledge_matrix.json', encoding='utf-8'))
strategy = [x for x in matrix if x.get('agent') == 'Meta Strategy']
assert len(strategy) == 41, f'Expected 41 files, found {len(strategy)}'
for f in strategy:
    path = f['absolute_path']
    assert os.path.exists(path), f"Missing file {path}"

print('Passed: All 41 census files exist on physical disk!')
