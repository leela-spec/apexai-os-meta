import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

DOSSIER_DIR = r"c:\GitDev\apexai-os-meta\FutureDevelopments&Research\AgentAudit\PerAgentDeepDives"

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

print("=== CHECKING SECTIONS 7 AND 9 ACROSS ALL DOSSIERS ===")

for d in DOSSIERS:
    p = os.path.join(DOSSIER_DIR, d)
    with open(p, "r", encoding="utf-8", errors="replace") as f:
        c = f.read()
    
    sec7_m = re.search(r"## 7\.(.*?)(?=## 8\.)", c, re.DOTALL)
    sec9_m = re.search(r"## 9\.(.*)", c, re.DOTALL)
    
    sec7_text = sec7_m.group(1).strip() if sec7_m else "MISSING"
    sec9_text = sec9_m.group(1).strip() if sec9_m else "MISSING"
    
    # Check for ADR-002, WSL2, ext4 mentions in sec 9
    wsl2_mentions = len(re.findall(r"wsl2|adr-002|ext4|single-engine|docker desktop", sec9_text, re.IGNORECASE))
    
    # Check lines in sec 7 and sec 9
    sec7_lines = len(sec7_text.splitlines())
    sec9_lines = len(sec9_text.splitlines())
    
    print(f"\n[{d}]")
    print(f"  Sec 7 (Unmigrated Lore): {sec7_lines} lines")
    print(f"    Snippet: {sec7_text.splitlines()[0] if sec7_lines > 0 else 'EMPTY'}")
    print(f"  Sec 9 (WSL2/ADR-002 Roadmap): {sec9_lines} lines | WSL2/ADR-002 keywords: {wsl2_mentions}")
    print(f"    Snippet: {sec9_text.splitlines()[0] if sec9_lines > 0 else 'EMPTY'}")
