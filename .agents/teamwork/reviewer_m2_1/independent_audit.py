import os
import re
import sys
import tiktoken

base_dir = r"c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb"
files = [
    "rule-09-recovery.md",
    "rule-10-stop-repairing.md",
    "rule-11-current-truth.md",
    "rule-12-surgical.md",
    "rule-13-editing.md",
    "rule-14-new-machinery.md",
    "rule-15-detour.md",
]

expected_ids = {
    "rule-09-recovery.md": "V2-LAYERED-KB-RULE-09-RECOVERY",
    "rule-10-stop-repairing.md": "V2-LAYERED-KB-RULE-10-STOP-REPAIRING",
    "rule-11-current-truth.md": "V2-LAYERED-KB-RULE-11-CURRENT-TRUTH",
    "rule-12-surgical.md": "V2-LAYERED-KB-RULE-12-SURGICAL",
    "rule-13-editing.md": "V2-LAYERED-KB-RULE-13-EDITING",
    "rule-14-new-machinery.md": "V2-LAYERED-KB-RULE-14-NEW-MACHINERY",
    "rule-15-detour.md": "V2-LAYERED-KB-RULE-15-DETOUR",
}

enc = tiktoken.get_encoding("cl100k_base")

results = []
all_passed = True
total_links_checked = 0
broken_links_list = []

for fname in files:
    fpath = os.path.join(base_dir, fname)
    file_report = {"file": fname, "errors": [], "warnings": [], "stats": {}}
    
    if not os.path.exists(fpath):
        file_report["errors"].append(f"File not found: {fpath}")
        results.append(file_report)
        all_passed = False
        continue

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Frontmatter Verification
    if not content.startswith("---"):
        file_report["errors"].append("Missing leading YAML frontmatter delimiter (---)")
    fm_match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", content, re.DOTALL)
    if not fm_match:
        file_report["errors"].append("Failed to parse YAML frontmatter")
    else:
        fm = fm_match.group(1)
        if "type: Reference" not in fm:
            file_report["errors"].append("Frontmatter missing 'type: Reference'")
        exp_id = expected_ids[fname]
        if f"id: {exp_id}" not in fm:
            file_report["errors"].append(f"Frontmatter missing expected id: {exp_id}")
        if "status: current_truth" not in fm:
            file_report["errors"].append("Frontmatter missing 'status: current_truth'")
        if not re.search(r"^title:\s*.+", fm, re.MULTILINE):
            file_report["errors"].append("Frontmatter missing title")
        if not re.search(r"^description:\s*.+", fm, re.MULTILINE):
            file_report["errors"].append("Frontmatter missing description")
        if not re.search(r"^tags:\s*\[.+\]", fm, re.MULTILINE):
            file_report["errors"].append("Frontmatter missing tags array")

    # 2. Section Conformance Verification
    required_sections = [
        "Position in Layered Knowledge Base:",
        "## 1. Original Rule & Atomic Semantic Block Inventory",
        "## 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives",
        "## 3. Whole-Rule Recomposition Rollup",
        "## 4. Complete Bidirectional Research & Provenance Links",
        "## 5. Failure Modes & Not-To-Dos",
    ]
    for sec in required_sections:
        if sec not in content:
            file_report["errors"].append(f"Missing mandatory section/anchor: '{sec}'")

    # 3. Layer Links Verification
    layer_checks = [
        "Layer 0 (Essence Contract)",
        "Layer 1 (This File",
        "Layer 2 (Downstream Infrastructure Modules)",
    ]
    for lc in layer_checks:
        if lc not in content:
            file_report["errors"].append(f"Missing Layer positioning link block: '{lc}'")

    # 4. Check for Integrity Violations / Placeholders
    placeholders = ["TODO", "TBD", "FIXME", "XXX", "Lorem ipsum", "[placeholder]"]
    for ph in placeholders:
        if ph in content:
            file_report["errors"].append(f"Integrity warning: Placeholder text '{ph}' found")

    # 5. Metric Tag Syntax & Range Verification
    # Format: [P<tier> | I<impact>/E<evidence>/R<risk>]
    tag_matches = re.findall(r"\[(P[0-3])\s*\|\s*I(\d+)/E(\d+)/R(\d+)\]", content)
    raw_tag_matches = re.findall(r"\[(P[0-3][^\]]*)\]", content)
    file_report["stats"]["valid_tags"] = len(tag_matches)
    file_report["stats"]["raw_p_tags"] = len(raw_tag_matches)

    for tier, i, e, r in tag_matches:
        i_val, e_val, r_val = int(i), int(e), int(r)
        if not (1 <= i_val <= 100 and 1 <= e_val <= 100 and 1 <= r_val <= 100):
            file_report["errors"].append(f"Tag metric out of bounds (1-100): [{tier} | I{i}/E{e}/R{r}]")

    # Check for computed math formulas in tags (e.g., I*E/R or similar)
    if re.search(r"\[P[0-3]\s*\|[^\]]*[+\-*\/=][^\]]*\]", content):
        # make sure it's not the normal slash between I, E, R
        for m in re.finditer(r"\[P[0-3]\s*\|([^\]]+)\]", content):
            inner = m.group(1).strip()
            if not re.match(r"^I\d+/E\d+/R\d+$", inner):
                file_report["warnings"].append(f"Non-standard tag format: [{m.group(0)}]")

    # 6. Options A, B, C presence in Section 2
    for opt in ["Option A", "Option B", "Option C"]:
        if opt not in content:
            file_report["errors"].append(f"Missing '{opt}' in Section 2")

    # 7. Relative Link Verification
    links = re.findall(r"\[([^\]]*)\]\(([^)]+)\)", content)
    rel_links = [l for _, l in links if not l.startswith("http") and not l.startswith("#") and not l.startswith("mailto:")]
    file_report["stats"]["total_rel_links"] = len(rel_links)
    total_links_checked += len(rel_links)

    for l in rel_links:
        # handle anchors inside relative links: path#anchor
        link_path = l.split("#")[0]
        if not link_path:
            continue
        unquoted = link_path.replace("%20", " ")
        resolved_path = os.path.normpath(os.path.join(base_dir, unquoted))
        if not os.path.exists(resolved_path):
            file_report["errors"].append(f"Broken relative link: '{l}' -> '{resolved_path}'")
            broken_links_list.append((fname, l, resolved_path))

    # 8. Token calculation verification
    # Extract Section 1.1 code block
    xml_code_match = re.search(r"```xml\r?\n(.*?)\r?\n```", content, re.DOTALL)
    if xml_code_match:
        xml_text = xml_code_match.group(1).strip()
        actual_bpe = len(enc.encode(xml_text))
        file_report["stats"]["xml_block_bpe"] = actual_bpe
    else:
        file_report["errors"].append("Could not find ```xml code block in Section 1.1")

    if file_report["errors"]:
        all_passed = False

    results.append(file_report)

print("=" * 60)
print("INDEPENDENT AUDIT REPORT: MILESTONE 2 (Rules 09-15)")
print("=" * 60)
for r in results:
    status_str = "PASSED" if not r["errors"] else "FAILED"
    print(f"File: {r['file']} -> {status_str}")
    print(f"  Valid P-Tags: {r['stats'].get('valid_tags', 0)} | Rel Links: {r['stats'].get('total_rel_links', 0)} | XML BPE: {r['stats'].get('xml_block_bpe', 0)}")
    if r["errors"]:
        for e in r["errors"]:
            print(f"  [ERROR] {e}")
    if r["warnings"]:
        for w in r["warnings"]:
            print(f"  [WARN] {w}")

print("-" * 60)
print(f"Total files audited: {len(results)}")
print(f"Total relative links verified: {total_links_checked}")
print(f"Broken links: {len(broken_links_list)}")
print(f"Overall Conformance Status: {'PASSED' if all_passed else 'FAILED'}")
print("=" * 60)
