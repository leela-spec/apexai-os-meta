import os

base = r"C:\Quasi Desktop\AI_PreperationUntil_06-26\LostAgents\InformaticsDesign"
print(f"Auditing Staged LostAgents Repository: {base}\n")

total_files = 0
total_bytes = 0
total_lines = 0

all_verified = True

for root, dirs, files in os.walk(base):
    rel = os.path.relpath(root, base)
    if files:
        print(f"Folder: {rel} ({len(files)} files)")
        print("-" * 80)
        for f in sorted(files):
            p = os.path.join(root, f)
            if not os.path.exists(p):
                print(f"  [MISSING] {f}")
                all_verified = False
                continue
            sz = os.path.getsize(p)
            if sz == 0:
                print(f"  [ZERO BYTES] {f}")
                all_verified = False
                continue
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                lines = sum(1 for _ in fp)
            total_files += 1
            total_bytes += sz
            total_lines += lines
            print(f"  [OK] {f:45s} | {sz:7,d} B | {lines:4d} L")
        print()

print("=" * 80)
print(f"Summary Verification: Total Files: {total_files} | Total Bytes: {total_bytes:,} | Total Lines: {total_lines:,}")
print(f"Integrity Status: {'100% VERIFIED ON PHYSICAL DISK' if all_verified else 'VERIFICATION FAILED'}")
