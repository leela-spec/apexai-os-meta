import os
import re
import urllib.parse
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

base_dir = r"c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb"
repo_root = r"c:\GitDev\apexai-os-meta"

rule_files = [
    "rule-16-authoring.md",
    "rule-17-trade-off.md",
    "rule-18-handover.md",
    "rule-19-iterative.md",
    "rule-20-schemas.md",
    "rule-21-sync.md",
    "rule-22-pointers.md"
]

plane4_files = {
    "WP": r"c:\GitDev\apexai-os-meta\apex-meta\informatics\writing-profile.md",
    "FA": r"c:\GitDev\apexai-os-meta\apex-meta\informatics\file-architecture.md",
    "EM": r"c:\GitDev\apexai-os-meta\apex-meta\informatics\execution-modes.md",
    "AD": r"c:\GitDev\apexai-os-meta\apex-meta\informatics\anti-drift-rules.md",
    "GS": r"c:\GitDev\apexai-os-meta\apex-meta\informatics\governance-schemas.md"
}

# 1. Extract all existing rule IDs from Plane 4 files
plane4_rules = {}
for prefix, path in plane4_files.items():
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    found = set(re.findall(rf"\b({prefix}-\d+)\b", text))
    plane4_rules[prefix] = found
    print(f"Plane 4 {prefix} defined rules: {len(found)}")

print("\n--- Auditing Plane 4 citations in Rules 16-22 ---")
all_valid_citations = True
for rf in rule_files:
    full_path = os.path.join(base_dir, rf)
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Find all citations like WP-xx, FA-xx, EM-xx, AD-xx, GS-xx
    citations = set(re.findall(r"\b(WP-\d+|FA-\d+|EM-\d+|AD-\d+|GS-\d+)\b", content))
    invalid = []
    for c in sorted(citations):
        prefix = c.split("-")[0]
        if c not in plane4_rules[prefix]:
            invalid.append(c)
    if invalid:
        print(f"[FAIL] {rf} cites unknown Plane 4 rules: {invalid}")
        all_valid_citations = False
    else:
        print(f"[PASS] {rf} cites {len(citations)} valid Plane 4 rules: {sorted(citations)}")

print("\n--- Auditing Relative Links in Rules 16-22 ---")
broken_links = []
total_links = 0
for rf in rule_files:
    full_path = os.path.join(base_dir, rf)
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
    for text, url in links:
        if url.startswith("http://") or url.startswith("https://") or url.startswith("#") or url.startswith("mailto:"):
            continue
        total_links += 1
        clean_url = urllib.parse.unquote(url.split("#")[0])
        resolved = os.path.normpath(os.path.join(base_dir, clean_url))
        if not os.path.exists(resolved):
            broken_links.append((rf, text, url, resolved))

print(f"Total checked links: {total_links}")
if broken_links:
    print(f"[FAIL] Broken links: {len(broken_links)}")
    for b in broken_links:
        print("  ", b)
else:
    print(f"[PASS] All {total_links} relative links resolve to existing files on disk.")

print("\n--- Auditing BPE Token Counts in Rules 16-22 ---")
for rf in rule_files:
    full_path = os.path.join(base_dir, rf)
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract Rollup table rows
    # | **1. Current `v1.0-3A` Baseline** | `<tag...> ... </tag>` | **`123`** | ...
    table_match = re.search(r"## 3\. Whole-Rule Recomposition Rollup.*?\n(.*?)(?:\n## |\Z)", content, re.DOTALL)
    if table_match:
        table_text = table_match.group(1)
        # Parse rows
        rows = re.findall(r"\|\s*\*\*(\d+\.\s*[^|]+)\*\*\s*\|\s*([^|]+)\|\s*\*\*`?(\d+)`?\*\*\s*\|", table_text)
        print(f"\n{rf} Rollup Table Verification:")
        for label, text, reported_bpe in rows:
            text_clean = text.strip()
            # If text is wrapped in code tags or backticks, strip
            if text_clean.startswith("`") and text_clean.endswith("`"):
                text_clean = text_clean[1:-1]
            actual_bpe = len(enc.encode(text_clean))
            reported = int(reported_bpe)
            status = "PASS" if actual_bpe == reported else f"FAIL (actual={actual_bpe})"
            print(f"  [{status}] {label.strip()}: reported {reported}, measured {actual_bpe}")

print("\n--- Section 4 & 5 Verification ---")
for rf in rule_files:
    full_path = os.path.join(base_dir, rf)
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check §4 completeness
    sec4_match = re.search(r"## 4\. Complete Bidirectional Research & Provenance Links.*?\n(.*?)(?:\n## 5|\Z)", content, re.DOTALL)
    if not sec4_match:
        print(f"[FAIL] {rf}: Missing §4")
    else:
        sec4_text = sec4_match.group(1)
        has_internal = "4.1 Internal Project Research Corpus" in sec4_text
        has_external = "4.2 External Peer-Reviewed" in sec4_text
        has_plane4 = "4.3 Canonical Plane 4 Infrastructure Modules" in sec4_text
        has_results = "RESULTS-" in sec4_text
        has_lineage = "Historical Contract Lineage" in sec4_text
        print(f"{rf} §4: Internal={has_internal}, External={has_external}, Plane4={has_plane4}, RESULTS={has_results}, Lineage={has_lineage}")
    
    # Check §5 completeness
    sec5_match = re.search(r"## 5\. Failure Modes & Not-To-Dos.*?\n(.*?)(?:\Z)", content, re.DOTALL)
    if not sec5_match:
        print(f"[FAIL] {rf}: Missing §5")
    else:
        sec5_text = sec5_match.group(1)
        bullets = [line.strip() for line in sec5_text.strip().split("\n") if line.strip().startswith("- ")]
        print(f"{rf} §5: {len(bullets)} failure modes defined. WP-25 referenced: {'WP-25' in sec5_text or 'WP-25' in content}")
