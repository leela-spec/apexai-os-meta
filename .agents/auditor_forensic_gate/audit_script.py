import os
import re

dossier_dir = r"c:\GitDev\apexai-os-meta\FutureDevelopments&Research\AgentAudit\PerAgentDeepDives"
dossiers = [f for f in sorted(os.listdir(dossier_dir)) if f.endswith("_DEEP_AUDIT.md")]

base_quasi = r"C:\Quasi Desktop\AI_PreperationUntil_06-26"
base_git = r"c:\GitDev\apexai-os-meta"

def find_file_on_disk(fname_or_path):
    if os.path.isabs(fname_or_path) and os.path.exists(fname_or_path):
        return fname_or_path
    cand1 = os.path.normpath(os.path.join(base_git, fname_or_path))
    if os.path.exists(cand1):
        return cand1
    cand2 = os.path.normpath(os.path.join(base_quasi, fname_or_path))
    if os.path.exists(cand2):
        return cand2
    bname = os.path.basename(fname_or_path)
    for root, dirs, files in os.walk(base_git):
        if bname in files:
            return os.path.join(root, bname)
    for root, dirs, files in os.walk(base_quasi):
        if bname in files:
            return os.path.join(root, bname)
    return None

for d in dossiers:
    fp = os.path.join(dossier_dir, d)
    with open(fp, "r", encoding="utf-8") as f:
        text = f.read()

    m = re.search(r"##\s*4\.[^\n]*\n(.*?)(?=\n##\s*5\.)", text, re.DOTALL)
    sec4_text = m.group(1) if m else ""
    
    print("=" * 80)
    print("DOSSIER:", d)
    
    lines = sec4_text.splitlines()
    cite_lines = [l.strip() for l in lines if any(k in l.lower() for k in ["line ", "lines ", "section ", "verbatim", "citation"])]
    print("Citations count in Sec 4:", len(cite_lines))
    for c in cite_lines[:4]:
        print("  Citation sample:", c)
        
    quoted = re.findall(r"`([^`]+\.md)`", sec4_text)
    cited_files = sorted(set(quoted))
    print("Cited .md files in Sec 4:", len(cited_files))
    for cf in cited_files:
        p = find_file_on_disk(cf)
        status = "FOUND: " + p if p else "NOT FOUND!"
        print(f"  {cf} -> {status}")
