import os
import sys
import csv
import json
import statistics
from collections import Counter

csv_path = r"c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit\agent_knowledge_matrix.csv"
json_path = r"c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit\agent_knowledge_matrix.json"
readme_path = r"c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit\README.md"

def normalize_path(p):
    p_clean = p.strip()
    if p_clean.startswith("\\\\?\\"):
        return p_clean
    if len(p_clean) >= 240 or " " in p_clean:
        return "\\\\?\\" + os.path.abspath(p_clean)
    return p_clean

print("=== STARTING FORENSIC AUDIT ===")

# 1. Schema & Syntax Forensics - CSV
print("\n--- 1. CSV Syntax & RFC 4180 Compliance ---")
with open(csv_path, "r", encoding="utf-8", errors="replace") as f:
    reader = csv.reader(f)
    csv_rows = list(reader)

csv_header = csv_rows[0]
csv_records = csv_rows[1:]
print(f"CSV Total Rows: {len(csv_rows)} (Header + {len(csv_records)} records)")
print(f"CSV Header ({len(csv_header)} cols): {csv_header}")

expected_header = ['Agent', 'File_Name', 'Absolute_Path', 'Quality', 'Quantity', 'Machine_Readability', 'Operational_Value', 'Composite_Score', 'Status', 'Lineage_Notes', 'Rationale']
assert csv_header == expected_header, f"Header mismatch: {csv_header} vs {expected_header}"

csv_col_mismatches = []
for idx, row in enumerate(csv_records):
    if len(row) != 11:
        csv_col_mismatches.append((idx+2, len(row)))

print(f"CSV Rows with column count != 11: {len(csv_col_mismatches)}")

# 2. Schema & Syntax Forensics - JSON
print("\n--- 2. JSON Syntax & Parsing ---")
with open(json_path, "r", encoding="utf-8") as f:
    json_data = json.load(f)

print(f"JSON Record Count: {len(json_data)}")
assert len(json_data) == 1153, f"Expected 1153 JSON records, got {len(json_data)}"
assert len(csv_records) == 1153, f"Expected 1153 CSV records, got {len(csv_records)}"

# Check 1-to-1 match between CSV and JSON
csv_paths = [r[2] for r in csv_records]
json_paths = [r["absolute_path"] for r in json_data]
path_diff_csv_json = set(csv_paths) ^ set(json_paths)
print(f"Path differences between CSV and JSON: {len(path_diff_csv_json)}")

# 3. Ground Truth Forensics (Disk Verification)
print("\n--- 3. Ground Truth Forensics (Physical Disk Verification) ---")
missing_files = []
size_mismatches = []
line_mismatches = []
total_bytes_on_disk = 0
total_lines_on_disk = 0

for item in json_data:
    raw_path = item["absolute_path"]
    norm_p = normalize_path(raw_path)
    
    if not os.path.exists(norm_p):
        # try without extended prefix or with
        if os.path.exists(raw_path):
            norm_p = raw_path
        else:
            missing_files.append(raw_path)
            continue
    
    actual_size = os.path.getsize(norm_p)
    total_bytes_on_disk += actual_size
    
    reported_size = item.get("byte_size")
    if reported_size is not None and reported_size != actual_size:
        size_mismatches.append((raw_path, reported_size, actual_size))
        
    # count lines
    try:
        with open(norm_p, "rb") as f_in:
            actual_lines = sum(1 for _ in f_in)
    except Exception as e:
        actual_lines = -1
    
    total_lines_on_disk += actual_lines
    reported_lines = item.get("line_count")
    if reported_lines is not None and reported_lines != actual_lines:
        line_mismatches.append((raw_path, reported_lines, actual_lines))

print(f"Missing (Phantom) Files: {len(missing_files)}")
print(f"Size Mismatches: {len(size_mismatches)}")
print(f"Line Count Mismatches: {len(line_mismatches)}")
print(f"Total Physical Bytes on Disk: {total_bytes_on_disk} ({total_bytes_on_disk / (1024*1024):.2f} MB)")
print(f"Total Physical Lines on Disk: {total_lines_on_disk}")

# 4. Evaluation Forensics - Score Distribution & Authenticity
print("\n--- 4. Evaluation Forensics (Scores & Authenticity) ---")
qualities = [int(r[3]) for r in csv_records]
quantities = [int(r[4]) for r in csv_records]
readabilities = [int(r[5]) for r in csv_records]
values = [int(r[6]) for r in csv_records]
composites = [float(r[7]) for r in csv_records]

def stats(name, vals):
    print(f"  {name}: min={min(vals)}, max={max(vals)}, mean={statistics.mean(vals):.2f}, stdev={statistics.stdev(vals):.2f}, unique={len(set(vals))}")

stats("Quality", qualities)
stats("Quantity", quantities)
stats("Machine_Readability", readabilities)
stats("Operational_Value", values)
stats("Composite_Score", composites)

# Status distribution
statuses = [r[8] for r in csv_records]
status_counts = Counter(statuses)
print(f"Status distribution: {dict(status_counts)}")

# Domain distribution
domains = [r[0] for r in csv_records]
domain_counts = Counter(domains)
print(f"Domain distribution: {dict(domain_counts)}")

# Check scores per status
print("Score distribution per Status:")
for st in status_counts:
    st_comps = [float(r[7]) for r in csv_records if r[8] == st]
    st_vals = [int(r[6]) for r in csv_records if r[8] == st]
    print(f"  Status '{st}' ({len(st_comps)} files): mean_comp={statistics.mean(st_comps):.2f}, mean_val={statistics.mean(st_vals):.2f}")

# Check rationales
rationales = [r[10] for r in csv_records]
unique_rationales = len(set(rationales))
print(f"Unique Rationales: {unique_rationales} / {len(rationales)}")
empty_rationales = sum(1 for r in rationales if not r.strip())
print(f"Empty Rationales: {empty_rationales}")

# Check lineage notes
lineages = [r[9] for r in csv_records]
unique_lineages = len(set(lineages))
print(f"Unique Lineage Notes: {unique_lineages} / {len(lineages)}")
empty_lineages = sum(1 for l in lineages if not l.strip())
print(f"Empty Lineage Notes: {empty_lineages}")

print("=== CHECK 1-4 COMPLETE ===")
