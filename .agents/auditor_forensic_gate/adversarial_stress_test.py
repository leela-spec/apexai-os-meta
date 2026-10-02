import os
import json
import hashlib
import sys
sys.stdout.reconfigure(encoding="utf-8")

print("=" * 80)
print("ADVERSARIAL STRESS-TEST 1: Mathematical Parity of Composite Scores in Census")
census_path = r"c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit\agent_knowledge_matrix.json"
with open(census_path, "r", encoding="utf-8") as f:
    census_data = json.load(f)

score_discrepancies = []
for rec in census_data:
    q = rec.get("quality", 0)
    qt = rec.get("quantity", 0)
    mr = rec.get("machine_readability", 0)
    ov = rec.get("operational_value", 0)
    expected = round((q * 0.30) + (qt * 0.20) + (mr * 0.20) + (ov * 0.30), 2)
    actual = rec.get("composite_score", 0)
    if abs(expected - actual) > 0.05:
        score_discrepancies.append((rec["file_name"], expected, actual))

print(f"Total census records checked: {len(census_data)}")
print(f"Composite score mathematical discrepancies: {len(score_discrepancies)}")
if score_discrepancies:
    print("  Discrepancy samples:", score_discrepancies[:5])

print("\n" + "=" * 80)
print("ADVERSARIAL STRESS-TEST 2: Cross-Hub File Duplication & Integrity in LostAgents")
base_lost = r"C:\Quasi Desktop\AI_PreperationUntil_06-26\LostAgents"
hashes = {}
duplicates = []
total_files = 0

for root, dirs, files in os.walk(base_lost):
    for f in files:
        total_files += 1
        fp = os.path.join(root, f)
        with open(fp, "rb") as fh:
            h = hashlib.sha256(fh.read()).hexdigest()
        if h in hashes:
            duplicates.append((fp, hashes[h]))
        else:
            hashes[h] = fp

print(f"Total files in LostAgents: {total_files}")
print(f"Unique content hashes: {len(hashes)}")
print(f"Content collisions: {len(duplicates)}")
# Note: Empty stubs across hubs might share template content; let's inspect collisions
stub_collisions = [d for d in duplicates if "90_SUPERSEDED" in d[0] and "90_SUPERSEDED" in d[1]]
active_collisions = [d for d in duplicates if "90_SUPERSEDED" not in d[0] and "90_SUPERSEDED" not in d[1]]
cross_active_superseded = [d for d in duplicates if ("90_SUPERSEDED" in d[0]) != ("90_SUPERSEDED" in d[1])]

print(f"  Collisions between quarantined stubs (expected identical templates): {len(stub_collisions)}")
print(f"  Collisions between active files: {len(active_collisions)}")
for ac in active_collisions:
    print(f"    Active collision: {os.path.basename(ac[0])} <==> {os.path.basename(ac[1])}")
print(f"  Collisions between active and quarantined: {len(cross_active_superseded)}")

print("\n" + "=" * 80)
print("ADVERSARIAL STRESS-TEST 3: Dossier Text Uniqueness & Anti-Plagiarism")
dossier_dir = r"c:\GitDev\apexai-os-meta\FutureDevelopments&Research\AgentAudit\PerAgentDeepDives"
dossiers = [f for f in sorted(os.listdir(dossier_dir)) if f.endswith("_DEEP_AUDIT.md")]
dossier_texts = {}
for d in dossiers:
    with open(os.path.join(dossier_dir, d), "r", encoding="utf-8") as f:
        dossier_texts[d] = f.read()

# Check Jaccard similarity of 5-grams
def get_ngrams(text, n=5):
    words = [w.lower() for w in re.findall(r"\b[a-zA-Z]{3,}\b", text)]
    return set(zip(*[words[i:] for i in range(n)]))

import re
dossier_ngrams = {d: get_ngrams(t) for d, t in dossier_texts.items()}
max_sim = 0
max_pair = None
for i in range(len(dossiers)):
    for j in range(i+1, len(dossiers)):
        d1, d2 = dossiers[i], dossiers[j]
        s1, s2 = dossier_ngrams[d1], dossier_ngrams[d2]
        sim = len(s1 & s2) / len(s1 | s2)
        if sim > max_sim:
            max_sim = sim
            max_pair = (d1, d2)

print(f"Max 5-gram Jaccard similarity across dossiers: {max_sim*100:.2f}% between {max_pair}")
