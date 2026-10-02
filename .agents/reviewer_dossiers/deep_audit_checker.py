import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

DOSSIER_DIR = r"c:\GitDev\apexai-os-meta\FutureDevelopments&Research\AgentAudit\PerAgentDeepDives"
INDEX_FILE = os.path.join(DOSSIER_DIR, "ALL_AGENTS_DEEP_AUDIT_INDEX.md")

DOSSIERS = [
    "META_OPS_DEEP_AUDIT.md",
    "META_DETECTIVE_DEEP_AUDIT.md",
    "META_STRATEGY_DEEP_AUDIT.md",
    "PROMPTS_AND_WORKFLOWS_DEEP_AUDIT.md",
    "INFORMATICS_DESIGN_DEEP_AUDIT.md",
    "KNOWLEDGE_BANK_DEEP_AUDIT.md",
    "AI_HANDLING_AND_ROUTING_DEEP_AUDIT.md",
    "HYGIENE_CLEAN_DEEP_AUDIT.md",
]

def analyze_section4(dossier_name, content):
    sec4_match = re.search(r"## 4\.(.*?)(?=## 5\.)", content, re.DOTALL)
    if not sec4_match:
        return {"error": "Section 4 not found"}
    sec4_text = sec4_match.group(1)
    
    # Extract details
    lines = [line.strip() for line in sec4_text.splitlines() if line.strip()]
    details = {}
    for line in lines:
        if "File Name" in line and "file_name" not in details:
            details["file_name"] = line
        elif ("Physical Path" in line or "Verified Path" in line) and "path" not in details:
            details["path"] = line
        elif "Size" in line and ("byte" in line.lower() or "verified" in line.lower()) and "size" not in details:
            details["size"] = line
        elif "Line Count" in line and "lines" not in details:
            details["lines"] = line
        elif "Score" in line and "score" not in details:
            details["score"] = line
    
    citations = re.findall(r"(?:Citation|line\s+[0-9]+|lines\s+[0-9]+|§\s*[0-9]+)", sec4_text, re.IGNORECASE)
    details["citation_count"] = len(citations)
    return details

print("=== SECTION 4 CROWN JEWELS DETAILS ===")
for d in DOSSIERS:
    p = os.path.join(DOSSIER_DIR, d)
    with open(p, "r", encoding="utf-8", errors="replace") as f:
        c = f.read()
    res = analyze_section4(d, c)
    print(f"\n>>> {d} <<<")
    for k, v in res.items():
        print(f"  {k}: {v}")

print("\n=== MASTER INDEX CROWN JEWEL MATRIX CHECK ===")
with open(INDEX_FILE, "r", encoding="utf-8", errors="replace") as f:
    idx_content = f.read()

sec3_idx = re.search(r"## 3\..*?(?=## 4\.)", idx_content, re.DOTALL)
if sec3_idx:
    print("Found Section 3 in Master Index. Snippet:")
    print("\n".join(sec3_idx.group(0).splitlines()[:40]))
else:
    print("FAIL: Section 3 not found in Master Index")
