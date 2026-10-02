import os
import re

dossier_dir = rc:\GitDev\apexai-os-meta\FutureDevelopments&Research\AgentAudit\PerAgentDeepDives
files = [
    META_OPS_DEEP_AUDIT.md,
    META_DETECTIVE_DEEP_AUDIT.md,
    META_STRATEGY_DEEP_AUDIT.md,
    PROMPTS_AND_WORKFLOWS_DEEP_AUDIT.md,
    INFORMATICS_DESIGN_DEEP_AUDIT.md,
    KNOWLEDGE_BANK_DEEP_AUDIT.md,
    AI_HANDLING_AND_ROUTING_DEEP_AUDIT.md,
    HYGIENE_CLEAN_DEEP_AUDIT.md
]

total_checked = 0
total_missing = 0
size_matches = 0
size_mismatches = 0
line_matches = 0
line_mismatches = 0

mismatch_details = []

for fname in files:
    path = os.path.join(dossier_dir, fname)
    with open(path, r, encoding=utf-8, errors=replace) as f:
        content = f.read()

    # Look for table rows with paths: e.g. c:\... or C:\...
    # Match lines like | ... | (path) | or containing c:\...
    rows = [line for line in content.splitlines() if | in line and (c:\ in line.lower())]
    
    print(f=== {fname}: Found {len(rows)} path-bearing table rows ===)
    
    for row in rows:
        cols = [c.strip() for c in row.split(|)]
        # find path
        found_paths = re.findall(r([a-zA-Z]:\\[^]+), row)
        if not found_paths:
            # try without backticks
            found_paths = re.findall(r([a-zA-Z]:\\[^\s|]+), row)
        
        for p in found_paths:
            p_clean = p.strip()
            total_checked += 1
            if not os.path.exists(p_clean):
                total_missing += 1
                mismatch_details.append(fMISSING FILE: {p_clean} in {fname})
            else:
                # check size and lines if present in row
                actual_size = os.path.getsize(p_clean)
                try:
                    with open(p_clean, r, encoding=utf-8, errors=replace) as pf:
                        actual_lines = len(pf.readlines())
                except Exception as e:
                    actual_lines = -1
                
                # Try to extract reported size and lines from columns
                # Typically columns contain numbers like 5,950 or 521 B or 60
                # Let's inspect cols
                # print first 5 rows of first file as sample
                if total_checked <= 5:
                    print(f Sample: {os.path.basename(p_clean)} -> actual size: {actual_size}, actual lines: {actual_lines})

print(f\nTOTAL PATHS CHECKED: {total_checked})
print(fTOTAL MISSING FILES: {total_missing})
if mismatch_details:
    print(\nFIRST 20 MISMATCHES / MISSING:)
    for m in mismatch_details[:20]:
        print(f {m})
