import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

DOSSIER_DIR = r"c:\GitDev\apexai-os-meta\FutureDevelopments&Research\AgentAudit\PerAgentDeepDives"
INDEX_FILE = os.path.join(DOSSIER_DIR, "ALL_AGENTS_DEEP_AUDIT_INDEX.md")
LOSTAGENTS_BASE = r"C:\Quasi Desktop\AI_PreperationUntil_06-26\LostAgents"

DOSSIER_MAP = {
    "MetaOps": "META_OPS_DEEP_AUDIT.md",
    "MetaDetective": "META_DETECTIVE_DEEP_AUDIT.md",
    "MetaStrategy": "META_STRATEGY_DEEP_AUDIT.md",
    "PromptsAndWorkflows": "PROMPTS_AND_WORKFLOWS_DEEP_AUDIT.md",
    "InformaticsDesign": "INFORMATICS_DESIGN_DEEP_AUDIT.md",
    "KnowledgeBank": "KNOWLEDGE_BANK_DEEP_AUDIT.md",
    "AIHandlingAndRouting": "AI_HANDLING_AND_ROUTING_DEEP_AUDIT.md",
    "HygieneClean": "HYGIENE_CLEAN_DEEP_AUDIT.md",
}

print("="*80)
print("AUDITING 8 AGENT DOSSIERS & MASTER INDEX")
print("="*80)

# Check staged files in LostAgents for each agent
print("\n>>> VERIFYING LOSTAGENTS STAGING HUBS ON PHYSICAL DISK <<<")
hub_stats = {}
for hub_name, dossier_fname in DOSSIER_MAP.items():
    hub_path = os.path.join(LOSTAGENTS_BASE, hub_name)
    if not os.path.exists(hub_path):
        print(f"FAIL: Hub directory missing: {hub_path}")
        continue
    
    subdirs = sorted(os.listdir(hub_path))
    files_in_hub = []
    total_bytes = 0
    for root, dirs, files in os.walk(hub_path):
        for f in files:
            fp = os.path.join(root, f)
            sz = os.path.getsize(fp)
            with open(fp, "r", encoding="utf-8", errors="replace") as fh:
                ln = len(fh.readlines())
            rel = os.path.relpath(fp, hub_path)
            files_in_hub.append((rel, sz, ln))
            total_bytes += sz
    
    hub_stats[hub_name] = {
        "file_count": len(files_in_hub),
        "total_bytes": total_bytes,
        "subdirs": subdirs,
        "files": files_in_hub
    }
    print(f"Hub: {hub_name:22} | Files: {len(files_in_hub):2} | Bytes: {total_bytes:10,} | Subdirs: {subdirs}")

# Also check Alfred benchmark hub
alfred_path = os.path.join(LOSTAGENTS_BASE, "Alfred")
if os.path.exists(alfred_path):
    alfred_files = []
    alfred_bytes = 0
    for root, dirs, files in os.walk(alfred_path):
        for f in files:
            fp = os.path.join(root, f)
            sz = os.path.getsize(fp)
            alfred_files.append(fp)
            alfred_bytes += sz
    print(f"Hub: {'Alfred (Benchmark)':22} | Files: {len(alfred_files):2} | Bytes: {alfred_bytes:10,} | Subdirs: {sorted(os.listdir(alfred_path))}")
    total_all_hubs_files = sum(s["file_count"] for s in hub_stats.values()) + len(alfred_files)
    total_all_hubs_bytes = sum(s["total_bytes"] for s in hub_stats.values()) + alfred_bytes
    print(f"TOTAL 9 HUBS: {total_all_hubs_files} files, {total_all_hubs_bytes:,} bytes")

print("\n" + "="*80)
print("VERIFYING EACH DOSSIER'S REPORTED STAGING VS ACTUAL PHYSICAL DISK")
print("="*80)

for hub_name, dossier_fname in DOSSIER_MAP.items():
    dp = os.path.join(DOSSIER_DIR, dossier_fname)
    with open(dp, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    
    print(f"\n>>> Checking {dossier_fname} (Hub: {hub_name}) <<<")
    # Section 8 check
    sec8_match = re.search(r"## 8\.(.*?)(?=## 9\.)", content, re.DOTALL)
    if not sec8_match:
        print(f"  FAIL: Section 8 missing in {dossier_fname}")
        continue
    sec8_text = sec8_match.group(1)
    
    # Check reported staged count in text
    cnt_match = re.search(r"(\d+)\s+verified physical files", sec8_text)
    rep_cnt = int(cnt_match.group(1)) if cnt_match else None
    
    actual_cnt = hub_stats[hub_name]["file_count"]
    actual_bytes = hub_stats[hub_name]["total_bytes"]
    print(f"  Reported Staged Files: {rep_cnt} | Actual on Disk: {actual_cnt} (Match: {rep_cnt == actual_cnt})")
    print(f"  Actual Bytes in Staging: {actual_bytes:,}")
    
    # Check files listed in section 8 tables or trees vs disk
    # Let's check table rows in section 8
    staged_rows = re.findall(r"^\|\s*[`*]*([0-9a-zA-Z_\\/.-]+(?:_empty)?\.[a-zA-Z0-9]+)[`*]*\s*\|", sec8_text, re.MULTILINE)
    print(f"  Files listed in Sec 8 table: {len(staged_rows)}")
    # check each listed file exists in hub
    missing_staged = []
    for sf in staged_rows:
        sf_clean = sf.replace("/", "\\")
        target_path = os.path.join(LOSTAGENTS_BASE, hub_name, sf_clean)
        if not os.path.exists(target_path):
            missing_staged.append(sf_clean)
    if missing_staged:
        print(f"  WARNING: {len(missing_staged)} files in Sec 8 table NOT found in hub: {missing_staged}")
    else:
        print(f"  All {len(staged_rows)} staged files listed in Sec 8 table confirmed on disk!")

print("\n" + "="*80)
print("VERIFYING QUARANTINE REGISTERS ACROSS ALL DOSSIERS AND MASTER INDEX")
print("="*80)

total_quarantine_across_dossiers = 0
for hub_name, dossier_fname in DOSSIER_MAP.items():
    dp = os.path.join(DOSSIER_DIR, dossier_fname)
    with open(dp, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    
    sec6_match = re.search(r"## 6\.(.*?)(?=## 7\.)", content, re.DOTALL)
    if not sec6_match:
        print(f"  FAIL: Section 6 missing in {dossier_fname}")
        continue
    sec6_text = sec6_match.group(1)
    
    # Look for count in text
    cnt_match = re.search(r"(\d+)\s+empty scaffold", sec6_text, re.IGNORECASE)
    if not cnt_match:
        cnt_match = re.search(r"(\d+)\s+quarantined", sec6_text, re.IGNORECASE)
    rep_cnt = int(cnt_match.group(1)) if cnt_match else None
    
    # Also check how many files are in 90_SUPERSEDED in the hub
    sup_path = os.path.join(LOSTAGENTS_BASE, hub_name, "90_SUPERSEDED")
    sup_files = os.listdir(sup_path) if os.path.exists(sup_path) else []
    
    print(f"[{dossier_fname:36}] Sec 6 Reported Quarantined: {rep_cnt} | In 90_SUPERSEDED: {len(sup_files)} ({sup_files})")
    if rep_cnt:
        total_quarantine_across_dossiers += rep_cnt

print(f"Total Quarantined Reported across 8 dossiers: {total_quarantine_across_dossiers}")

# Master Index Quarantine section check
with open(INDEX_FILE, "r", encoding="utf-8", errors="replace") as f:
    idx_content = f.read()

sec6_idx = re.search(r"## 6\.(.*?)(?=## 7\.)", idx_content, re.DOTALL)
if sec6_idx:
    print("\nMaster Index Section 6 Summary:")
    print("\n".join(sec6_idx.group(1).splitlines()[:20]))
