import os
import re
import urllib.parse
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

base_dir = r"c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb"

expected_files = [
    "rule-16-authoring.md",
    "rule-17-trade-off.md",
    "rule-18-handover.md",
    "rule-19-iterative.md",
    "rule-20-schemas.md",
    "rule-21-sync.md",
    "rule-22-pointers.md"
]

print("=== 1. Checking File Existence ===")
for fn in expected_files:
    full_path = os.path.join(base_dir, fn)
    assert os.path.exists(full_path), f"Missing file: {full_path}"
    print(f"[PASS] {fn} exists ({os.path.getsize(full_path)} bytes)")

print("\n=== 2. Checking Mandatory Sections & Metadata ===")
required_sections = [
    r"^## 1\. Original Rule & Atomic Semantic Block Inventory",
    r"^## 2\. Chapter-by-Chapter Semantic Block Analysis & Alternatives",
    r"^## 3\. Whole-Rule Recomposition Rollup for ",
    r"^## 4\. Complete Bidirectional Research & Provenance Links for ",
    r"^## 5\. Failure Modes & Not-To-Dos \(`WP-25`\)"
]

for fn in expected_files:
    full_path = os.path.join(base_dir, fn)
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check frontmatter
    assert content.startswith("---\n"), f"{fn}: Missing frontmatter start"
    fm_end = content.find("\n---\n", 4)
    assert fm_end != -1, f"{fn}: Missing frontmatter end"
    fm = content[4:fm_end]
    assert "type: Reference" in fm, f"{fn}: Missing 'type: Reference'"
    assert "id: V2-LAYERED-KB-RULE-" in fm, f"{fn}: Missing ID prefix"
    assert "status: current_truth" in fm, f"{fn}: Missing 'status: current_truth'"
    assert "tags: [" in fm, f"{fn}: Missing tags list"
    
    # Check Layer positioning
    assert "Layer 0 (Essence Contract)" in content, f"{fn}: Missing Layer 0"
    assert "Layer 1 (This File" in content, f"{fn}: Missing Layer 1"
    assert "Layer 2 (Downstream Infrastructure Modules)" in content, f"{fn}: Missing Layer 2"
    
    # Check 5 mandatory sections
    for sec_pat in required_sections:
        match = re.search(sec_pat, content, re.MULTILINE)
        assert match, f"{fn}: Missing section matching pattern '{sec_pat}'"
    
    # Check Option A, B, C presence
    assert "Option A (" in content, f"{fn}: Missing Option A"
    assert "Option B (" in content, f"{fn}: Missing Option B"
    assert "Option C (" in content, f"{fn}: Missing Option C"
    
    # Check I/E/R tags
    ier_matches = re.findall(r"\[P[0-3]\s*\|\s*I\d+/E\d+/R\d+\]", content)
    assert len(ier_matches) >= 2, f"{fn}: Too few [P | I/E/R] tags ({len(ier_matches)})"
    
    print(f"[PASS] {fn} satisfies all 5 sections, frontmatter, and layer headers.")

print("\n=== 3. Checking 100% Relative Link Resolution ===")
total_links = 0
broken_links = []

for fn in expected_files:
    full_path = os.path.join(base_dir, fn)
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    matches = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
    for text, url in matches:
        if url.startswith("http://") or url.startswith("https://") or url.startswith("#") or url.startswith("mailto:"):
            continue
        total_links += 1
        url_clean = urllib.parse.unquote(url.split("#")[0])
        if not url_clean:
            continue
        resolved = os.path.normpath(os.path.join(base_dir, url_clean))
        if not os.path.exists(resolved):
            broken_links.append((fn, text, url, resolved))

print(f"Total relative links checked across 7 files: {total_links}")
if broken_links:
    print(f"FAILED: Found {len(broken_links)} broken links:")
    for b in broken_links:
        print("  ", b)
    assert False, f"Broken relative links found: {len(broken_links)}"
else:
    print(f"[PASS] 100% of {total_links} relative links resolve to existing files on disk!")

print("\n=== ALL M3 DELIVERABLE VERIFICATIONS PASSED ===")
