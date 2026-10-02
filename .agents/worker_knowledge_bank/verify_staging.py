import os

staging_root = r"C:\Quasi Desktop\AI_PreperationUntil_06-26\LostAgents\KnowledgeBank"
total_files = 0
total_bytes = 0

print("Verification of Staged Files in LostAgents/KnowledgeBank:\n")
for root, dirs, files in os.walk(staging_root):
    rel = os.path.relpath(root, staging_root)
    for f in sorted(files):
        p = os.path.join(root, f)
        total_files += 1
        size = os.path.getsize(p)
        total_bytes += size
        assert size > 0, f"File {p} is empty!"
        with open(p, 'r', encoding='utf-8', errors='ignore') as fl:
            lines = sum(1 for _ in fl)
        print(f"[{rel}] {f}: {size} bytes, {lines} lines - OK")

print(f"\nTotal Staged Files: {total_files}")
print(f"Total Bytes: {total_bytes} bytes ({total_bytes / (1024*1024):.2f} MB)")
