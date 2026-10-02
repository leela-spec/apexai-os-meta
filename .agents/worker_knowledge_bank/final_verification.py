import os

audit_file = r"c:\GitDev\apexai-os-meta\FutureDevelopments&Research\AgentAudit\PerAgentDeepDives\KNOWLEDGE_BANK_DEEP_AUDIT.md"
staging_root = r"C:\Quasi Desktop\AI_PreperationUntil_06-26\LostAgents\KnowledgeBank"

print("--- 1. VERIFY AUDIT DOSSIER ---")
assert os.path.exists(audit_file), "Audit file missing!"
size = os.path.getsize(audit_file)
with open(audit_file, 'r', encoding='utf-8') as f:
    lines = sum(1 for _ in f)
print(f"KNOWLEDGE_BANK_DEEP_AUDIT.md: {size} bytes, {lines} lines - PASS")

print("\n--- 2. VERIFY LOSTAGENTS DIRECTORIES ---")
subdirs = ["00_INDEX", "01_CURRENT_KNOWLEDGE_BANK", "02_RESEARCH_AND_DESIGN", "90_SUPERSEDED"]
for sd in subdirs:
    p = os.path.join(staging_root, sd)
    assert os.path.exists(p) and os.path.isdir(p), f"Directory {p} missing!"
    count = len(os.listdir(p))
    print(f"Directory {sd}: {count} files - PASS")

print("\n--- 3. VERIFY ALL STAGED FILES (PHYSICAL EXISTENCE, NON-ZERO SIZE) ---")
total_staged = 0
for root, dirs, files in os.walk(staging_root):
    rel = os.path.relpath(root, staging_root)
    for f in sorted(files):
        p = os.path.join(root, f)
        total_staged += 1
        fsize = os.path.getsize(p)
        assert fsize > 0, f"File {p} is empty!"
        with open(p, 'r', encoding='utf-8', errors='ignore') as fl:
            flines = sum(1 for _ in fl)
        print(f"[{rel}] {f} ({fsize} B, {flines} L) - PASS")

print(f"\nTotal Verified Staged Files: {total_staged} (all non-zero bytes)")
print("ALL VERIFICATIONS PASSED SUCCESSFULLY.")
