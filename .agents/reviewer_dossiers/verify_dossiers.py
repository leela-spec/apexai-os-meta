import os
import re
import sys
import glob

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

print("=== 1. VERIFYING DOSSIER EXISTENCE AND SIZES ===")
for d in DOSSIERS:
    p = os.path.join(DOSSIER_DIR, d)
    if os.path.exists(p):
        size = os.path.getsize(p)
        with open(p, "r", encoding="utf-8", errors="replace") as f:
            lines = len(f.readlines())
        print(f"PASS: {d} exists: {size:,} bytes, {lines} lines")
    else:
        print(f"FAIL: {d} MISSING!")

p_idx = INDEX_FILE
if os.path.exists(p_idx):
    size = os.path.getsize(p_idx)
    with open(p_idx, "r", encoding="utf-8", errors="replace") as f:
        lines = len(f.readlines())
    print(f"PASS: ALL_AGENTS_DEEP_AUDIT_INDEX.md exists: {size:,} bytes, {lines} lines")
else:
    print("FAIL: Master Index MISSING!")

print("\n=== 2. VERIFYING 9-SECTION SCHEMA ACROSS 8 DOSSIERS ===")
for d in DOSSIERS:
    p = os.path.join(DOSSIER_DIR, d)
    with open(p, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    
    sections = re.findall(r"^##\s+([0-9])\.\s+(.*)$", content, re.MULTILINE)
    sec_dict = {int(num): title.strip() for num, title in sections}
    print(f"\n--- {d} ---")
    missing_secs = []
    for s in range(1, 10):
        if s in sec_dict:
            print(f"  Sec {s}: {sec_dict[s]}")
        else:
            missing_secs.append(s)
            print(f"  FAIL: Sec {s} MISSING!")
    if missing_secs:
        print(f"  RESULT: FAILED schema check (missing {missing_secs})")
    else:
        print(f"  RESULT: PASSED 9-section schema check.")

print("\n=== 3. VERIFYING 7 ARCHITECTURAL CATEGORIES IN SECTION 3 ===")
for d in DOSSIERS:
    p = os.path.join(DOSSIER_DIR, d)
    with open(p, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    
    # Find Section 3 to Section 4
    sec3_match = re.search(r"## 3\..*?(?=## 4\.)", content, re.DOTALL)
    if not sec3_match:
        print(f"FAIL: Could not extract Section 3 in {d}")
        continue
    sec3_text = sec3_match.group(0)
    
    cat_matches = re.findall(r"###\s+3\.([1-7])\s+Category\s+[0-9]:\s+(.*)", sec3_text)
    if not cat_matches:
        cat_matches = re.findall(r"###\s+3\.([1-7])\s+(.*)", sec3_text)
    
    print(f"\n--- {d}: Categories found ({len(cat_matches)}/7) ---")
    cats_found = {int(num): title.strip() for num, title in cat_matches}
    for i in range(1, 8):
        if i in cats_found:
            print(f"  Cat {i}: {cats_found[i]}")
        else:
            print(f"  FAIL: Cat {i} MISSING!")

print("\n=== 4. VERIFYING CROWN JEWELS (SECTION 4) ===")
crown_jewels = {}
for d in DOSSIERS:
    p = os.path.join(DOSSIER_DIR, d)
    with open(p, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    
    sec4_match = re.search(r"## 4\..*?(?=## 5\.)", content, re.DOTALL)
    if not sec4_match:
        print(f"FAIL: Could not extract Section 4 in {d}")
        continue
    sec4_text = sec4_match.group(0)
    
    fn = re.search(r"File Name:\s*[`\"]?([^`\"\n\r]+)[`\"]?", sec4_text)
    pp = re.search(r"Verified Physical Path:\s*[`\"]?([^`\"\n\r]+)[`\"]?", sec4_text)
    sz = re.search(r"Verified Size:\s*([0-9,]+)\s*bytes", sec4_text)
    ln = re.search(r"Verified Line Count:\s*([0-9,]+)\s*lines", sec4_text)
    
    file_name = fn.group(1).strip() if fn else "UNKNOWN"
    phys_path = pp.group(1).strip() if pp else "UNKNOWN"
    size_str = sz.group(1).replace(",", "") if sz else "UNKNOWN"
    lines_str = ln.group(1).replace(",", "") if ln else "UNKNOWN"
    
    has_citations = "Citation" in sec4_text or "line" in sec4_text.lower()
    
    exists = os.path.exists(phys_path) if phys_path != "UNKNOWN" else False
    actual_size = os.path.getsize(phys_path) if exists else None
    actual_lines = None
    if exists:
        with open(phys_path, "r", encoding="utf-8", errors="replace") as pf:
            actual_lines = len(pf.readlines())
    
    size_match = str(actual_size) == str(size_str)
    lines_match = str(actual_lines) == str(lines_str)
    
    print(f"[{d}]")
    print(f"  Crown Jewel: {file_name}")
    print(f"  Path: {phys_path} (Exists: {exists})")
    print(f"  Size: reported={size_str}, actual={actual_size} (Match: {size_match})")
    print(f"  Lines: reported={lines_str}, actual={actual_lines} (Match: {lines_match})")
    print(f"  Has Citations: {has_citations}")

print("\n=== 5. CHECKING QUARANTINE REGISTERS (SECTION 6) ===")
for d in DOSSIERS:
    p = os.path.join(DOSSIER_DIR, d)
    with open(p, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    sec6_match = re.search(r"## 6\..*?(?=## 7\.)", content, re.DOTALL)
    if not sec6_match:
        print(f"FAIL: Could not extract Section 6 in {d}")
        continue
    sec6_text = sec6_match.group(0)
    rows = re.findall(r"^\|\s*([0-9]+)\s*\|", sec6_text, re.MULTILINE)
    print(f"[{d}] Section 6 quarantine items listed: {len(rows)}")

print("\n=== 6. CHECKING STAGING DIRECTORIES IN LOSTAGENTS (SECTION 8) ===")
LOSTAGENTS_BASE = r"C:\Quasi Desktop\AI_PreperationUntil_06-26\LostAgents"
if os.path.exists(LOSTAGENTS_BASE):
    hubs = [f for f in os.listdir(LOSTAGENTS_BASE) if os.path.isdir(os.path.join(LOSTAGENTS_BASE, f))]
    print(f"Found {len(hubs)} directories under {LOSTAGENTS_BASE}: {hubs}")
    for h in hubs:
        h_path = os.path.join(LOSTAGENTS_BASE, h)
        subdirs = [s for s in os.listdir(h_path) if os.path.isdir(os.path.join(h_path, s))]
        total_files = 0
        total_bytes = 0
        for root, dirs, files in os.walk(h_path):
            for f in files:
                total_files += 1
                total_bytes += os.path.getsize(os.path.join(root, f))
        print(f"  Hub {h}: {len(subdirs)} subdirs ({subdirs}), {total_files} files, {total_bytes:,} bytes")
else:
    print(f"WARNING: LostAgents base path does not exist: {LOSTAGENTS_BASE}")
