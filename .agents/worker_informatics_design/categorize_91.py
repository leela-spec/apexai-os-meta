import json
import os

with open('c:/GitDev/apexai-os-meta/.agents/worker_informatics_design/informatics_verified_91.json', 'r', encoding='utf-8') as f:
    files = json.load(f)

def categorize(f):
    fn = f['file_name'].lower()
    p = f['path'].lower()
    
    # 1. Essence / Functional Identity
    if fn in ['essence.md', 'role-seed.md', 'information_design_80_20_essence.md', 'information_design_80_20_aggregate_snippet.md', 'core.md'] or 'agent_card.md' in fn:
        if 'core.md' in fn:
            return 'Cat 1: Essence / Functional Identity' # or Cat 2/7, but CORE defines identity & boundary
        return 'Cat 1: Essence / Functional Identity'
    
    # 2. Agent Contract / Role Card
    if fn in ['informatics-design.md', 'information_design.md', 'agent_card.md'] or ('agents' in p and fn.endswith('.md')):
        return 'Cat 2: Agent Contract / Role Card'
        
    # 3. Best Practices
    if 'best_practices' in fn:
        return 'Cat 3: Best Practices'
        
    # 4. Mistakes, Traps & Failure Modes
    if 'mistakes' in fn or 'failure' in fn:
        return 'Cat 4: Mistakes, Traps & Failure Modes'
        
    # 5. Operational Templates & Instruments
    if 'template' in fn or 'schema' in fn or 'fixture' in fn or 'workspace.json' in fn or 'learning' in fn or '2dos' in fn:
        return 'Cat 5: Operational Templates & Instruments'
        
    # 6. Appendices & Deep Research Blueprints
    if 'appendix' in fn or 'source_index' in fn or 'deep_research' in fn or 'promptflow' in fn:
        return 'Cat 6: Appendices & Deep Research Blueprints'
        
    # 7. Execution Control & Interaction Workflows
    # Skills, scripts, repair-packs, patchers, standards
    return 'Cat 7: Execution Control & Interaction Workflows'

cat_counts = {}
for f in files:
    cat = categorize(f)
    f['category'] = cat
    cat_counts[cat] = cat_counts.get(cat, 0) + 1

print("Category distribution across 91 files:")
for k, v in sorted(cat_counts.items()):
    print(f"  {k}: {v}")

with open('c:/GitDev/apexai-os-meta/.agents/worker_informatics_design/informatics_categorized_91.json', 'w', encoding='utf-8') as f:
    json.dump(files, f, indent=2)

print("Saved informatics_categorized_91.json successfully.")
