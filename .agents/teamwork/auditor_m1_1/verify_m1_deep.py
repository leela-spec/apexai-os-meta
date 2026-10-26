import os
import re
import sys
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")
kb_dir = r"c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb"
rules = [f"rule-{i:02d}-{name}.md" for i, name in [
    (2, "product-first"),
    (3, "scope"),
    (4, "communication"),
    (5, "hold-position"),
    (6, "ground"),
    (7, "reuse"),
    (8, "context")
]]

print("================================================================================")
print("             DEEP FORENSIC INTEGRITY AUDIT: RULES 02 - 08                       ")
print("================================================================================")

all_passed = True
results = {}

for r in rules:
    path = os.path.join(kb_dir, r)
    if not os.path.exists(path):
        print(f"[CRITICAL FAIL] File not found: {r}")
        all_passed = False
        continue
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    bpe = len(enc.encode(content))
    words = len(content.split())
    chars = len(content)
    lines = len(content.splitlines())
    
    res = {
        "bpe": bpe,
        "words": words,
        "chars": chars,
        "lines": lines,
        "errors": [],
        "warnings": [],
        "sb_blocks": [],
        "tags": []
    }
    
    # 1. Frontmatter
    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not fm_match:
        res["errors"].append("Missing or invalid frontmatter")
    else:
        fm = fm_match.group(1)
        if "type: Reference" not in fm:
            res["errors"].append("Frontmatter missing 'type: Reference'")
        id_m = re.search(r"id:\s*(V2-LAYERED-KB-RULE-\d\d-[A-Z\-]+)", fm)
        if not id_m:
            res["errors"].append("Frontmatter missing or invalid 'id:' format")
        if "status: current_truth" not in fm:
            res["errors"].append("Frontmatter missing 'status: current_truth'")
        if "tags:" not in fm:
            res["errors"].append("Frontmatter missing 'tags:'")
            
    # 2. Mandatory sections
    for sec_num, sec_title in [
        (1, "Original Rule & Atomic Semantic Block"),
        (2, "Chapter-by-Chapter Semantic Block Analysis"),
        (3, "Whole-Rule Recomposition Rollup"),
        (4, "Complete Bidirectional Research & Provenance Links"),
        (5, "Failure Modes & Not-To-Dos")
    ]:
        if not re.search(rf"^## {sec_num}\.\s+.*{re.escape(sec_title.split()[0])}", content, re.MULTILINE):
            res["errors"].append(f"Missing mandatory section {sec_num}: {sec_title}")
            
    # 3. Semantic blocks in 1.2 vs 2.x
    sec1_text = content.split("## 2.")[0]
    sb_in_sec1 = sorted(list(set(re.findall(r"[`'\"](SB-\d\d\.\d+)[`'\"]", sec1_text))))
    sb_in_sec2 = sorted(list(set(re.findall(r"### 2\.\d+\s+Chapter\s+[`'\"]?(SB-\d\d\.\d+)[`'\"]?:", content))))
    
    res["sb_blocks"] = sb_in_sec1
    if not sb_in_sec1:
        res["errors"].append("No semantic blocks listed in Section 1.2")
    if set(sb_in_sec1) != set(sb_in_sec2):
        res["errors"].append(f"Mismatch between Section 1.2 blocks {sb_in_sec1} and Section 2 chapters {sb_in_sec2}")

        
    # 4. Each block must have Critique, Options A, B, C
    for sb in sb_in_sec1:
        sb_pattern = rf"### 2\.\d+\s+Chapter\s+[`'\"]?{sb}[`'\"]?:(.*?)(?=### 2\.\d+|## 3\.|$)"
        sb_match = re.search(sb_pattern, content, re.DOTALL)
        if not sb_match:
            res["errors"].append(f"Could not parse chapter for {sb}")
            continue
        sb_text = sb_match.group(1)
        if "What It Means & Failure Mode Addressed:" not in sb_text:
            res["errors"].append(f"{sb} missing 'What It Means & Failure Mode Addressed:'")
        if "Value & Necessity Critique" not in sb_text:
            res["errors"].append(f"{sb} missing 'Value & Necessity Critique'")
        if "Option A" not in sb_text:
            res["errors"].append(f"{sb} missing Option A")
        if "Option B" not in sb_text:
            res["errors"].append(f"{sb} missing Option B")
        if "Option C" not in sb_text:
            res["errors"].append(f"{sb} missing Option C")
            
    # 5. Significance tags [P0-P3 | I/E/R]
    tags = re.findall(r"\[P[0-3]\s*\|\s*I\d+/E\d+/R\d+\]", content)
    res["tags"] = tags
    if len(tags) < len(sb_in_sec1):
        res["errors"].append(f"Fewer [P|I/E/R] tags ({len(tags)}) than semantic blocks ({len(sb_in_sec1)})")
        
    # Check for computed math formulas in tag contexts (e.g. arithmetic operations like * + or equations like =)
    raw_formula_calc = re.findall(r"\[P[0-3]\s*\|\s*[^\]]*[\*\+\=][^\]]*\]", content)
    if raw_formula_calc:
        res["errors"].append(f"Calculated math formula found inside significance tag: {raw_formula_calc}")

        
    # 6. Check for dummy / placeholder tokens
    for forbidden in ["TODO", "TBD", "FIXME", "placeholder", "lorem ipsum"]:
        matches = [m.start() for m in re.finditer(rf"\b{forbidden}\b", content, re.IGNORECASE)]
        if matches:
            # Check context to distinguish "WP-25 forbids TODOs" from an actual TODO
            real_todos = []
            for idx in matches:
                ctx = content[max(0, idx-40):min(len(content), idx+40)].replace("\n", " ")
                if "never" in ctx.lower() or "not" in ctx.lower() or "forbid" in ctx.lower() or "not-to-do" in ctx.lower():
                    continue # negative rule
                real_todos.append(ctx)
            if real_todos:
                res["errors"].append(f"Forbidden placeholder '{forbidden}' detected in context: {real_todos}")
                
    # 7. Check BPE token range (~2500 - 3500)
    if bpe < 2400 or bpe > 3600:
        res["warnings"].append(f"BPE token count {bpe} outside nominal ~2500-3500 range")
        if bpe < 1500:
            res["errors"].append(f"BPE token count {bpe} severely below threshold (< 1500)")
            
    # 8. Section 3 Rollup table verification
    sec3_match = re.search(r"## 3\..*?\n(.*?)(?=## 4\.|$)", content, re.DOTALL)
    if not sec3_match or "|" not in sec3_match.group(1):
        res["errors"].append("Section 3 rollup table missing or malformed")
    else:
        table_text = sec3_match.group(1)
        if "Baseline" not in table_text and "Current" not in table_text:
            res["errors"].append("Section 3 rollup missing Baseline row")
        if "Option B" not in table_text and "Surgical" not in table_text:
            res["errors"].append("Section 3 rollup missing Option B row")
        if "Option C" not in table_text and "Aggressive" not in table_text:
            res["errors"].append("Section 3 rollup missing Option C row")
            
    # 9. Section 4 provenance subsections
    for sub in ["4.1", "4.2", "4.3"]:
        if f"### {sub}" not in content:
            res["errors"].append(f"Section 4 missing subsection ### {sub}")
            
    # 10. Section 5 not-to-dos
    sec5_match = re.search(r"## 5\..*?\n(.*)", content, re.DOTALL)
    if not sec5_match or "-" not in sec5_match.group(1):
        res["errors"].append("Section 5 missing bulleted failure modes / not-to-dos")
        
    results[r] = res
    if res["errors"]:
        all_passed = False

for r, res in results.items():
    status = "PASS" if not res["errors"] else "FAIL"
    print(f"\n--- {r} [{status}] ---")
    print(f"  BPE: {res['bpe']} | Words: {res['words']} | Chars: {res['chars']} | Lines: {res['lines']}")
    print(f"  Semantic Blocks: {res['sb_blocks']}")
    print(f"  [P|I/E/R] Tags ({len(res['tags'])}): {res['tags']}")
    if res["warnings"]:
        for w in res["warnings"]:
            print(f"  [WARN] {w}")
    if res["errors"]:
        for e in res["errors"]:
            print(f"  [ERROR] {e}")

print("\n" + "="*80)
print(f"DEEP AUDIT VERDICT: {'CLEAN (All 7 files conform 100%)' if all_passed else 'INTEGRITY VIOLATION'}")
print("="*80)
