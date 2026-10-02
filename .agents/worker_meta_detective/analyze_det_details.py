import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\GitDev\apexai-os-meta\.agents\worker_meta_detective\det_enriched.json', 'r', encoding='utf-8') as f:
    det = json.load(f)

print("=== STATUS BREAKDOWN ===")
statuses = {}
for f in det:
    s = f.get('status')
    statuses[s] = statuses.get(s, 0) + 1
for s, c in statuses.items():
    print(f"  {s}: {c}")

print("\n=== TOP 25 BY COMPOSITE SCORE ===")
for i, f in enumerate(sorted(det, key=lambda x: -x.get('composite_score', 0))[:25]):
    print(f"{i+1:2d}. [{f['composite_score']:.2f}] (Q:{f['quality']} Qt:{f['quantity']} MR:{f['machine_readability']} OV:{f['operational_value']}) {f['file_name']:<35} | {f['actual_size']:>6} B | {f['actual_lines']:>4} L | {f['status'][:12]} | {f['absolute_path']}")

print("\n=== STUBS / EMPTY FILES (Score < 5.0 or Empty) ===")
stubs = [f for f in det if f.get('status') == 'Empty Scaffold / Stub' or f.get('composite_score', 0) < 5.0]
print(f"Total stubs/low score: {len(stubs)}")
for s in stubs:
    print(f"  [{s['composite_score']:.2f}] {s['file_name']:<30} | {s['actual_size']} B | {s['actual_lines']} L | {s['absolute_path']}")

