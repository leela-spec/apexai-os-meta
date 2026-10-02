import os

base_dir = r"C:\Quasi Desktop\AI_PreperationUntil_06-26\LostAgents\PromptsAndWorkflows"

total_files = 0
all_valid = True

for root, dirs, files in os.walk(base_dir):
    for f in sorted(files):
        total_files += 1
        full_path = os.path.join(root, f)
        exists = os.path.exists(full_path)
        size = os.path.getsize(full_path) if exists else -1
        try:
            with open(full_path, 'r', encoding='utf-8', errors='ignore') as fp:
                lines = sum(1 for _ in fp)
        except Exception as e:
            lines = -1
        
        rel_path = os.path.relpath(full_path, base_dir)
        print(f"[{total_files:02d}] {rel_path:60s} | Size: {size:7,d} bytes | Lines: {lines:5,d} | Exists: {exists}")
        if not exists or size == 0:
            all_valid = False

print(f"\nTotal staged files: {total_files}")
print(f"All files physically exist and are non-zero size: {all_valid}")
