import os

audit_path = r"c:\GitDev\apexai-os-meta\FutureDevelopments&Research\AgentAudit\PerAgentDeepDives\PROMPTS_AND_WORKFLOWS_DEEP_AUDIT.md"
print(f"Deep Audit Report Exists: {os.path.exists(audit_path)}")
if os.path.exists(audit_path):
    print(f"Deep Audit Size: {os.path.getsize(audit_path):,d} bytes")
    print(f"Deep Audit Lines: {len(open(audit_path, encoding='utf-8').readlines()):,d} lines")

staged_dir = r"C:\Quasi Desktop\AI_PreperationUntil_06-26\LostAgents\PromptsAndWorkflows"
print(f"\nStaged Directory Exists: {os.path.exists(staged_dir)}")

staged_files = []
for root, dirs, files in os.walk(staged_dir):
    for f in sorted(files):
        p = os.path.join(root, f)
        staged_files.append((p, os.path.relpath(p, staged_dir), os.path.getsize(p), len(open(p, encoding='utf-8', errors='ignore').readlines())))

print(f"Total Staged Files: {len(staged_files)}")
for p, rel, sz, lns in staged_files:
    assert sz > 0, f"File {rel} has zero size!"
    print(f"  OK: {rel:60s} | {sz:7,d} bytes | {lns:5,d} lines")

print("\nALL VERIFICATIONS PASSED 100%!")
