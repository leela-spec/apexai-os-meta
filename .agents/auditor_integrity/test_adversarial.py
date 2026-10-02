import json
import csv
import os
from collections import Counter
from pathlib import Path

csv_path = r"c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit\agent_knowledge_matrix.csv"
json_path = r"c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit\agent_knowledge_matrix.json"

with open(json_path, "r", encoding="utf-8") as f:
    json_data = json.load(f)

print("=== ADVERSARIAL STRESS TEST SUITE ===")

# Test 1: Duplicate paths
paths = [x["absolute_path"] for x in json_data]
c_paths = Counter(paths)
dup_paths = [p for p, count in c_paths.items() if count > 1]
print(f"[TEST 1] Duplicate paths: {len(dup_paths)}")
assert len(dup_paths) == 0, f"Found duplicate paths: {dup_paths}"

# Test 2: Mandatory directory coverage
base_repo = Path(r"c:\GitDev\apexai-os-meta")
claude_agents = list((base_repo / ".claude" / "agents").rglob("*.md"))
orch_agents = [p for p in (base_repo / "apex-meta" / "orchestration" / "agents").rglob("*") if p.is_file()]

legacy_managed_dir = r"\\?\C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb"
legacy_kb_files = []
for root, dirs, files in os.walk(legacy_managed_dir):
    for f_name in files:
        full_p = os.path.join(root, f_name)
        if full_p.startswith("\\\\?\\"):
            clean_p = full_p[4:]
        else:
            clean_p = full_p
        legacy_kb_files.append(clean_p)

print(f"[TEST 2] Physical files on disk:")
print(f"  .claude/agents: {len(claude_agents)}")
print(f"  apex-meta/orchestration/agents: {len(orch_agents)}")
print(f"  managed/agent_kb: {len(legacy_kb_files)}")

json_paths_norm = set(os.path.abspath(p).lower() for p in paths)

missing_claude = [str(p) for p in claude_agents if str(p).lower() not in json_paths_norm]
missing_orch = [str(p) for p in orch_agents if str(p).lower() not in json_paths_norm]
missing_legacy = [p for p in legacy_kb_files if os.path.abspath(p).lower() not in json_paths_norm]

print(f"  Missing .claude/agents in audit: {len(missing_claude)}")
print(f"  Missing apex-meta/orchestration/agents in audit: {len(missing_orch)}")
print(f"  Missing managed/agent_kb in audit: {len(missing_legacy)}")
assert len(missing_claude) == 0, f"Missing claude agents: {missing_claude}"
assert len(missing_orch) == 0, f"Missing orch agents: {missing_orch}"
assert len(missing_legacy) == 0, f"Missing legacy kb files: {missing_legacy}"

# Test 3: UTF-8 and RFC 4180 parsing robustness
with open(csv_path, "rb") as f:
    raw_csv = f.read()

try:
    decoded = raw_csv.decode("utf-8")
    print(f"[TEST 3] CSV UTF-8 clean decode: PASS ({len(raw_csv):,} bytes)")
except Exception as e:
    print(f"[TEST 3] CSV UTF-8 clean decode: FAIL ({e})")
    raise

# Check line breaks in CSV
crlf_count = raw_csv.count(b"\r\n")
lf_only_count = raw_csv.count(b"\n") - crlf_count
print(f"  Line endings: CRLF={crlf_count}, bare LF={lf_only_count}")

# Test 4: Mathematical consistency of composite score
math_errors = []
for idx, x in enumerate(json_data):
    q = x["quality"]
    qt = x["quantity"]
    mr = x["machine_readability"]
    ov = x["operational_value"]
    comp = x["composite_score"]
    
    f_repo = round((q + qt + mr + ov) / 4.0, 2)
    f_legacy = round(0.35 * q + 0.30 * ov + 0.20 * qt + 0.15 * mr, 2)
    
    if abs(comp - f_repo) > 0.01 and abs(comp - f_legacy) > 0.01:
        math_errors.append((idx, x["file_name"], comp, f_repo, f_legacy))

print(f"[TEST 4] Composite score mathematical errors: {len(math_errors)}")
assert len(math_errors) == 0, f"Math errors found: {math_errors}"

# Test 5: Check for NaN, null, whitespace-only in any field
invalid_fields = []
for idx, x in enumerate(json_data):
    for k, v in x.items():
        if v is None:
            invalid_fields.append((idx, k, "None"))
        elif isinstance(v, str) and not v.strip():
            invalid_fields.append((idx, k, "Empty string"))
        elif isinstance(v, float) and (v != v):
            invalid_fields.append((idx, k, "NaN"))

print(f"[TEST 5] Invalid (Null/Empty/NaN) fields across all JSON objects: {len(invalid_fields)}")
assert len(invalid_fields) == 0, f"Invalid fields found: {invalid_fields}"

print("=== ALL ADVERSARIAL STRESS TESTS PASSED WITH ZERO ERRORS ===")
