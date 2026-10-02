import os
import re

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

for d in dossiers:
    p = os.path.join(dossier_dir, d)
    with open(p, "r", encoding="utf-8") as f:
        text = f.read()
    m = re.search(r"## 4\..*?(?=## 5|\Z)", text, re.S)
    print(f"=== {d} ===")
    if m:
        crown_sec = m.group(0)
        for line in crown_sec.splitlines()[:25]:
            print(" ", line)
    else:
        print("  NO SECTION 4 FOUND")
