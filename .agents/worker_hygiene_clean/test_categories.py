import json
import os

census_path = r'c:\GitDev\apexai-os-meta\.agents\worker_hygiene_clean\hygiene_clean_verified_census.json'
with open(census_path, 'r', encoding='utf-8') as f:
    census = json.load(f)

def assign_category(fn, p):
    fn_lower = fn.lower()
    p_lower = p.lower()
    if 'qa_hygiene_protocol' in fn_lower:
        return 'Cat 7 (Execution Control)'
    elif 'essence' in fn_lower:
        return 'Cat 1 (Essence)'
    elif 'doctrine' in fn_lower or 'agent_card' in fn_lower or ('special_ops__hygiene_clean.md' in fn_lower and 'agent_kb' not in p_lower):
        return 'Cat 2 (Role Card)'
    elif 'best_practices' in fn_lower or 'learning' in fn_lower:
        return 'Cat 3 (Best Practices)'
    elif 'mistake' in fn_lower or 'anti_drift' in fn_lower or 'validation_report' in fn_lower or 'changes' in fn_lower:
        return 'Cat 4 (Mistakes & Traps)'
    elif 'templates' in fn_lower or 'ranking_ledger' in fn_lower or 'candidate_ledger' in fn_lower:
        return 'Cat 5 (Templates & Instruments)'
    else:
        return 'Cat 6 (Research & Blueprints)'

for item in census:
    item['category'] = assign_category(item['file_name'], item['absolute_path'])

print(f"Loaded {len(census)} census entries and assigned categories.")
