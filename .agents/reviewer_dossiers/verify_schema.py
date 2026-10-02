import os
import re

dossier_dir = r"c:\GitDev\apexai-os-meta\FutureDevelopments&Research\AgentAudit\PerAgentDeepDives"
files = [
    "META_OPS_DEEP_AUDIT.md",
    "META_DETECTIVE_DEEP_AUDIT.md",
    "META_STRATEGY_DEEP_AUDIT.md",
    "PROMPTS_AND_WORKFLOWS_DEEP_AUDIT.md",
    "INFORMATICS_DESIGN_DEEP_AUDIT.md",
    "KNOWLEDGE_BANK_DEEP_AUDIT.md",
    "AI_HANDLING_AND_ROUTING_DEEP_AUDIT.md",
    "HYGIENE_CLEAN_DEEP_AUDIT.md"
]

expected_categories = [
    "Essence",
    "Contract",
    "Best Practices",
    "Mistakes",
    "Operational Templates",
    "Appendices",
    "Execution Control"
]

for fname in files:
    path = os.path.join(dossier_dir, fname)
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    
    print(f"=== {fname} ===")
    missing_secs = []
    for i in range(1, 10):
        m = re.search(rf"^##\s+{i}\.\s+(.*)", content, re.MULTILINE)
        if m:
            print(f"  Sec {i}: {m.group(1).strip()[:50]}")
        else:
            missing_secs.append(i)
    if missing_secs:
        print(f"  FAILED SECTIONS: {missing_secs}")
    else:
        print("  All 9 sections present.")

    sec3_match = re.search(r"## 3\..*?(?=## 4\.)", content, re.DOTALL)
    if sec3_match:
        sec3_text = sec3_match.group(0)
        found_cats = []
        missing_cats = []
        for cat in expected_categories:
            if re.search(rf"{cat}", sec3_text, re.IGNORECASE):
                found_cats.append(cat)
            else:
                missing_cats.append(cat)
        print(f"  Found categories: {len(found_cats)}/7 ({', '.join(found_cats)})")
        if missing_cats:
            print(f"  MISSING CATEGORIES: {missing_cats}")
    else:
        print("  Section 3 block not matched!")
    print()

