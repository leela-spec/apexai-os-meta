import os
import sys

staging_root = r'C:\Quasi Desktop\AI_PreperationUntil_06-26\LostAgents\HygieneClean'

print(f"Verifying staging repository: {staging_root}")
total_files = 0
all_valid = True

for root, dirs, files in os.walk(staging_root):
    rel_dir = os.path.relpath(root, staging_root)
    print(f"\nDirectory: {rel_dir}")
    for f in sorted(files):
        total_files += 1
        fp = os.path.join(root, f)
        sz = os.path.getsize(fp)
        with open(fp, 'rb') as fh:
            lines = len(fh.readlines())
        
        valid = (sz > 0 and lines > 0)
        if not valid:
            all_valid = False
        status_str = "OK" if valid else "FAIL"
        print(f"  [{status_str}] {f} — {sz:,} bytes, {lines} lines")

print(f"\n==========================================")
print(f"Total Staged Files: {total_files}")
print(f"All files physically exist and non-zero: {all_valid}")
print(f"==========================================")
