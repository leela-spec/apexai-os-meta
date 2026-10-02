import os
import json
import re

# Load census
census_path = r"c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit\agent_knowledge_matrix.json"
with open(census_path, "r", encoding="utf-8") as f:
    census_data = json.load(f)

# Build map of filename to absolute path
file_map = {}
for rec in census_data:
    fn = rec["file_name"]
    ap = rec["absolute_path"]
    file_map[fn] = ap
    file_map[fn.lower()] = ap

dossier_dir = r"c:\GitDev\apexai-os-meta\FutureDevelopments&Research\AgentAudit\PerAgentDeepDives"
dossiers = [f for f in sorted(os.listdir(dossier_dir)) if f.endswith("_DEEP_AUDIT.md")]

print(f"Total census files mapped: {len(file_map)}")

for d in dossiers:
    fp = os.path.join(dossier_dir, d)
    with open(fp, "r", encoding="utf-8") as f:
        text = f.read()

    m = re.search(r"##\s*4\.[^\n]*\n(.*?)(?=\n##\s*5\.)", text, re.DOTALL)
    sec4_text = m.group(1) if m else ""

    print("=" * 80)
    print("DOSSIER:", d)
    
    # Check cited markdown files in Sec 4
    quoted = re.findall(r"`([^`]+\.md)`", sec4_text)
    cited_files = sorted(set(quoted))
    print(f"Cited .md files in Sec 4: {len(cited_files)}")
    for cf in cited_files:
        bn = os.path.basename(cf)
        resolved = file_map.get(bn) or file_map.get(bn.lower())
        if not resolved:
            # check directly on disk
            for prefix in [r"c:\GitDev\apexai-os-meta", r"C:\Quasi Desktop\AI_PreperationUntil_06-26", r"C:\Quasi Desktop\AI_PreperationUntil_06-26\LostAgents"]:
                cand = os.path.join(prefix, cf.replace("/", "\\"))
                if os.path.exists(cand):
                    resolved = cand
                    break
        if resolved and os.path.exists(resolved):
            sz = os.path.getsize(resolved)
            print(f"  [OK] {cf} -> {resolved} ({sz} bytes)")
        else:
            print(f"  [MISSING] {cf} -> NOT FOUND")

    # Sample citations
    cite_lines = [l.strip() for l in sec4_text.splitlines() if any(k in l.lower() for k in ["line ", "lines ", "section ", "verbatim", "citation"])]
    print(f"Total citation lines in Sec 4: {len(cite_lines)}")
    for cl in cite_lines[:3]:
        print("   Sample:", cl[:120])
