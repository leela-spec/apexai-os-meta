import os
import re
import sys

dossier_dir = r"c:\GitDev\apexai-os-meta\FutureDevelopments&Research\AgentAudit\PerAgentDeepDives"
dossiers = [
    "META_OPS_DEEP_AUDIT.md",
    "META_DETECTIVE_DEEP_AUDIT.md",
    "META_STRATEGY_DEEP_AUDIT.md",
    "PROMPTS_AND_WORKFLOWS_DEEP_AUDIT.md",
    "INFORMATICS_DESIGN_DEEP_AUDIT.md",
    "KNOWLEDGE_BANK_DEEP_AUDIT.md",
    "AI_HANDLING_AND_ROUTING_DEEP_AUDIT.md",
    "HYGIENE_CLEAN_DEEP_AUDIT.md",
]
master_index = "ALL_AGENTS_DEEP_AUDIT_INDEX.md"

categories = [
    "Essence",
    "Contract",
    "Best Practice",
    "Mistake",
    "Template",
    "Appendix",
    "Execution"
]

print("=== VERIFYING DOSSIERS & SCHEMA ===")
for d in dossiers:
    p = os.path.join(dossier_dir, d)
    if not os.path.exists(p):
        print(f"MISSING: {d}")
        continue
    with open(p, "r", encoding="utf-8") as f:
        content = f.read()
    
    has_highest_val = bool(re.search(r"Highest-Value|Crown Jewel", content, re.I))
    cat_matches = [cat for cat in categories if re.search(cat, content, re.I)]
    
    print(f"{d:38s} | Lines: {len(content.splitlines()):4d} | Size: {len(content.encode('utf-8')):6d} B | "
          f"HighestVal: {has_highest_val} | Cats: {len(cat_matches)}/7")

master_p = os.path.join(dossier_dir, master_index)
if os.path.exists(master_p):
    with open(master_p, "r", encoding="utf-8") as f:
        mcontent = f.read()
    print(f"{master_index:38s} | Lines: {len(mcontent.splitlines()):4d} | Size: {len(mcontent.encode('utf-8')):6d} B")
else:
    print(f"MISSING: {master_index}")
