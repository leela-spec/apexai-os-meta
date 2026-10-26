import os
import re
import sys
import tiktoken

sys.stdout.reconfigure(encoding='utf-8')
enc = tiktoken.get_encoding("cl100k_base")

KB_DIR = r"c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb"
CANDIDATE_3A = r"c:\GitDev\apexai-os-meta\apex-meta\informatics\final\candidates\13-candidate-3A-xml.md"

TARGET_RULES = [
    ("rule-02-product-first.md", "product_first"),
    ("rule-03-scope.md", "scope"),
    ("rule-04-communication.md", "communication"),
    ("rule-05-hold-position.md", "hold_position"),
    ("rule-06-ground.md", "ground"),
    ("rule-07-reuse.md", "reuse"),
    ("rule-08-context.md", "context")
]

def get_3a_rules():
    with open(CANDIDATE_3A, "r", encoding="utf-8") as f:
        c3a = f.read()
    block = re.search(r'```xml\r?\n<apex_contract[^>]*>\r?\n\r?\n(.*?)\r?\n</apex_contract>\r?\n```', c3a, re.DOTALL).group(1)
    tags = dict(re.findall(r'<([a-zA-Z0-9_]+)(?:\s+[^>]*)?>\r?\n?(.*?)\r?\n?</\1>', block, re.DOTALL))
    return {k: v.strip() for k, v in tags.items()}

def verify_single_rule(filename, tag_name, rules_3a):
    filepath = os.path.join(KB_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    print(f"\n{'='*90}\nVERIFYING {filename} (<{tag_name}>)\n{'='*90}")
    
    issues = []
    
    # 1. Frontmatter Verification
    fm_match = re.match(r'^---\r?\n(.*?)\r?\n---\r?\n', content, re.DOTALL)
    if not fm_match:
        issues.append("CRITICAL: Missing YAML frontmatter")
    else:
        fm = fm_match.group(1)
        required_fields = ["type: Reference", "id: ", "title: ", "description: ", "status: current_truth", "tags: "]
        for req in required_fields:
            if req not in fm:
                issues.append(f"Frontmatter missing or mismatch: {req}")

    # 2. Section Headings Check
    required_sections = [
        (r'## 1\.\s+Original Rule & Atomic Semantic Block Inventory', "§1 Title"),
        (r'### 1\.1\s+Current `v1\.0-3A` Full Text', "§1.1 Subtitle"),
        (r'### 1\.2\s+Atomic Semantic Block Inventory \(Bullet List\)', "§1.2 Subtitle"),
        (r'## 2\.\s+Chapter-by-Chapter Semantic Block Analysis & Alternatives', "§2 Title"),
        (r'## 3\.\s+Whole-Rule Recomposition Rollup for `<' + tag_name + r'>`', "§3 Title"),
        (r'## 4\.\s+Complete Bidirectional Research & Provenance Links', "§4 Title"),
        (r'## 5\.\s+Failure Modes & Not-To-Dos \(`WP-25`\)', "§5 Title")
    ]
    for pattern, name in required_sections:
        if not re.search(pattern, content):
            issues.append(f"Section heading missing or malformed: {name} (pattern: {pattern})")

    # 3. Ground Truth Text Verification (§1.1 code block vs 13-candidate-3A-xml.md)
    code_match = re.search(r'### 1\.1\s+Current `v1\.0-3A` Full Text[^\n]*\r?\n\r?\n```xml\r?\n(.*?)\r?\n```', content, re.DOTALL)
    if not code_match:
        issues.append("CRITICAL: Could not find §1.1 XML code block")
        file_xml = ""
        file_inner = ""
    else:
        file_xml = code_match.group(1).strip()
        inner_m = re.search(rf'<{tag_name}>(.*?)</{tag_name}>', file_xml, re.DOTALL)
        if not inner_m:
            issues.append(f"CRITICAL: §1.1 XML does not have expected wrapper <{tag_name}>...</{tag_name}>")
            file_inner = ""
        else:
            file_inner = inner_m.group(1).strip()
            expected_inner = rules_3a[tag_name]
            if file_inner != expected_inner:
                issues.append(f"MISMATCH against 13-candidate-3A-xml.md:\nExpected: {repr(expected_inner)}\nFound:    {repr(file_inner)}")
            else:
                print("  [OK] Ground truth text matches 13-candidate-3A-xml.md exactly character-for-character.")

    # 4. Measure Metrics for §1.1
    # Full block
    block_bpe = len(enc.encode(file_xml))
    block_chars = len(file_xml)
    block_repo = block_chars // 4
    block_words = len(file_xml.split())

    # Inner text
    inner_bpe = len(enc.encode(file_inner))
    inner_chars = len(file_inner)
    inner_repo = inner_chars // 4
    inner_words = len(file_inner.split())

    print(f"  Live Measured Metrics:")
    print(f"    - Full Block (with <{tag_name}> tags): {block_bpe} BPE | {block_chars} chars | {block_repo} repo | {block_words} words")
    print(f"    - Inner Text (without tags):          {inner_bpe} BPE | {inner_chars} chars | {inner_repo} repo | {inner_words} words")

    # Extract reported header numbers in §1.1
    header_m = re.search(r'### 1\.1\s+Current `v1\.0-3A` Full Text \((.*?)\)', content)
    if header_m:
        header_text = header_m.group(1)
        print(f"  Reported in §1.1 Header: ({header_text})")
        # Check claims in header
        # Patterns like: `62 BPE block` | `55 BPE inner` | `70 repo tokens` | `280 chars` | `45 words`
        # or `56 BPE tokens` ...
        rep_block_bpe = re.search(r'(\d+)\s+BPE\s+block', header_text)
        rep_inner_bpe = re.search(r'(\d+)\s+BPE\s+inner', header_text)
        rep_tokens_bpe = re.search(r'(\d+)\s+BPE\s+tokens', header_text)
        rep_repo = re.search(r'(\d+)\s+repo tokens', header_text)
        rep_chars = re.search(r'(\d+)\s+chars', header_text)
        rep_words = re.search(r'(\d+)\s+words', header_text)

        if rep_block_bpe:
            val = int(rep_block_bpe.group(1))
            if val != block_bpe:
                issues.append(f"§1.1 header block BPE mismatch: reported {val}, actual {block_bpe}")
        elif rep_tokens_bpe and not rep_inner_bpe:
            val = int(rep_tokens_bpe.group(1))
            if val != block_bpe and val != inner_bpe:
                issues.append(f"§1.1 header BPE mismatch: reported {val}, actual block={block_bpe}, inner={inner_bpe}")

        if rep_inner_bpe:
            val = int(rep_inner_bpe.group(1))
            if val != inner_bpe:
                issues.append(f"§1.1 header inner BPE mismatch: reported {val}, actual {inner_bpe}")

        if rep_repo:
            val = int(rep_repo.group(1))
            if val != inner_repo and val != block_repo:
                issues.append(f"§1.1 header repo tokens mismatch: reported {val}, actual inner={inner_repo}, block={block_repo}")

        if rep_chars:
            val = int(rep_chars.group(1))
            if val != inner_chars and val != block_chars:
                issues.append(f"§1.1 header chars mismatch: reported {val}, actual inner={inner_chars}, block={block_chars}")

        if rep_words:
            val = int(rep_words.group(1))
            if val != inner_words and val != block_words:
                issues.append(f"§1.1 header words mismatch: reported {val}, actual inner={inner_words}, block={block_words}")
    else:
        issues.append("CRITICAL: §1.1 header missing metrics parentheses")

    # 5. Semantic Blocks in §1.2
    # Example line:
    # - **`SB-02.1` — Core Product Invariant (`10 BPE tokens` | `55 chars`):** *"Build the working thing before the machinery around it."*
    print("\n  Semantic Blocks Inventory (§1.2):")
    # Also check wrapper tag line if mentioned
    wrapper_m = re.search(r'plus the XML tag wrapper \(`<' + tag_name + r'>\.\.\.</' + tag_name + r'>`,\s*`?(\d+)\s+BPE\s+tokens`?\):', content)
    if wrapper_m:
        rep_wrap_bpe = int(wrapper_m.group(1))
        # Actual wrapper tokens = block_bpe - inner_bpe or len(enc.encode(f"<{tag_name}></{tag_name}>"))
        # Note: in XML, <tag>text</tag>
        # Let's check wrapper tokens:
        wrap_text = f"<{tag_name}></{tag_name}>"
        wrap_bpe = len(enc.encode(wrap_text))
        print(f"    XML Tag wrapper reported: {rep_wrap_bpe} BPE (wrapper text BPE: {wrap_bpe}, block - inner = {block_bpe - inner_bpe} BPE)")

    sb_lines = re.findall(r'-\s+\*\*`([A-Z0-9_\-\.]+)`\s+[—\-]\s+(.*?)\s+\((.*?)\):\*\*\s+(?:\*")?(.*?)(?:"\*)?\r?\n', content)
    concat_sb_text = []
    for sb_id, sb_title, metrics_str, sb_text in sb_lines:
        clean_text = sb_text.strip().strip('*').strip('"')
        concat_sb_text.append(clean_text)
        actual_sb_bpe = len(enc.encode(clean_text))
        actual_sb_chars = len(clean_text)

        rep_sb_bpe_m = re.search(r'(\d+)\s+BPE', metrics_str)
        rep_sb_chars_m = re.search(r'(\d+)\s+chars', metrics_str)
        rep_sb_bpe = int(rep_sb_bpe_m.group(1)) if rep_sb_bpe_m else None
        rep_sb_chars = int(rep_sb_chars_m.group(1)) if rep_sb_chars_m else None

        status_bpe = "OK" if rep_sb_bpe == actual_sb_bpe else f"MISMATCH (rep={rep_sb_bpe}, act={actual_sb_bpe})"
        status_chars = "OK" if rep_sb_chars == actual_sb_chars else f"MISMATCH (rep={rep_sb_chars}, act={actual_sb_chars})"

        print(f"    - {sb_id} ({sb_title}):")
        print(f"        text: {repr(clean_text)}")
        print(f"        BPE: {status_bpe} | Chars: {status_chars}")

        if rep_sb_bpe != actual_sb_bpe:
            # Check if leading space makes a difference
            act_with_space = len(enc.encode(" " + clean_text))
            if rep_sb_bpe == act_with_space:
                print(f"        NOTE: matches when prefixed with space ({act_with_space} BPE)")
            else:
                issues.append(f"§1.2 {sb_id} BPE mismatch: reported {rep_sb_bpe}, actual {actual_sb_bpe} (with space: {act_with_space})")
        if rep_sb_chars != actual_sb_chars:
            issues.append(f"§1.2 {sb_id} chars mismatch: reported {rep_sb_chars}, actual {actual_sb_chars}")

    # Check reconstruction of inner text
    reconstructed = " ".join(concat_sb_text)
    if reconstructed == file_inner:
        print("    [OK] Concatenation of semantic blocks reconstructed inner text 100% exactly.")
    else:
        # Check normalized whitespace
        if re.sub(r'\s+', ' ', reconstructed) == re.sub(r'\s+', ' ', file_inner):
            print("    [OK] Concatenation matches inner text modulo whitespace.")
        else:
            print("    [NOTE] Semantic blocks differ from inner text:")
            print(f"      Reconstructed: {repr(reconstructed)}")
            print(f"      Inner text:    {repr(file_inner)}")

    # 6. Chapter-by-Chapter Section 2 Options Verification
    print("\n  Chapter Analysis (§2) Options Check:")
    # Find all options: Option A, Option B, Option C
    options = re.findall(r'-\s+\*\*Option ([ABC])\s+\(([^\)]*)\):\*\*\s+\*"(.*?)"\*', content)
    for opt_letter, opt_hdr, opt_text in options:
        opt_bpe_act = len(enc.encode(opt_text))
        rep_bpe_m = re.search(r'(\d+)\s+BPE', opt_hdr)
        rep_bpe = int(rep_bpe_m.group(1)) if rep_bpe_m else None
        
        status = "OK" if rep_bpe == opt_bpe_act else f"MISMATCH (rep={rep_bpe}, act={opt_bpe_act})"
        if rep_bpe != opt_bpe_act:
            # Check with leading space
            with_sp = len(enc.encode(" " + opt_text))
            if rep_bpe == with_sp:
                status = f"OK (with leading space = {with_sp})"
            elif rep_bpe == 0 and "0" in opt_hdr:
                status = "OK (omitted/fused = 0)"
            else:
                issues.append(f"§2 Option {opt_letter} BPE mismatch in '{opt_hdr}': reported {rep_bpe}, actual {opt_bpe_act}")
        print(f"    - Option {opt_letter}: BPE {status} | text: {repr(opt_text)}")

    # 7. Whole-Rule Recomposition Rollup Table (§3)
    print("\n  Recomposition Rollup Table (§3) Verification:")
    table_m = re.search(r'## 3\.\s+Whole-Rule Recomposition Rollup[^\n]*\r?\n\r?\n(.*?)(?:\r?\n\r?\n---|\r?\n\r?\n## 4)', content, re.DOTALL)
    if not table_m:
        issues.append("CRITICAL: §3 Rollup table not found")
    else:
        tbl_text = table_m.group(1).strip()
        rows = [r.strip() for r in tbl_text.splitlines() if r.strip().startswith('|') and not r.strip().startswith('|---') and not 'Rollup Option' in r]
        
        baseline_bpe = None
        for idx, r in enumerate(rows):
            cols = [c.strip() for c in r.split('|')[1:-1]]
            if len(cols) < 4:
                issues.append(f"§3 Table row {idx+1} invalid column count: {r}")
                continue
            opt_title = cols[0]
            opt_code = cols[1]
            opt_bpe_str = cols[2]
            opt_savings_str = cols[3]

            # Extract XML from code
            code_m = re.search(r'`(<[^>]+>.*?</[^>]+>)`', opt_code, re.DOTALL)
            if not code_m:
                code_m = re.search(r'(<[^>]+>.*?</[^>]+>)', opt_code, re.DOTALL)
            code_text = code_m.group(1) if code_m else opt_code.strip('`')

            actual_bpe = len(enc.encode(code_text))
            
            # Reported BPE
            rep_bpe_m = re.search(r'(\d+)', opt_bpe_str)
            reported_bpe = int(rep_bpe_m.group(1)) if rep_bpe_m else None

            # Reported diff & pct
            diff_m = re.search(r'[-−](\d+)\s+BPE', opt_savings_str)
            pct_m = re.search(r'[-−]?(\d+(?:\.\d+)?)\s*%', opt_savings_str)
            
            rep_diff = int(diff_m.group(1)) if diff_m else (0 if '0' in opt_savings_str else None)
            rep_pct = float(pct_m.group(1)) if pct_m else (0.0 if '0' in opt_savings_str else None)

            bpe_match = (reported_bpe == actual_bpe)
            print(f"    Row {idx+1}: {opt_title[:35]:<35} | Actual BPE: {actual_bpe} | Rep BPE: {reported_bpe} ({'OK' if bpe_match else 'FAIL'})")
            if not bpe_match:
                issues.append(f"§3 Table Row {idx+1} BPE mismatch: text measured {actual_bpe} BPE, but table reports {reported_bpe} BPE.\nCode text: {repr(code_text)}")

            if idx == 0:
                baseline_bpe = actual_bpe
            else:
                if baseline_bpe is not None and reported_bpe is not None:
                    # Math verification
                    calc_diff = baseline_bpe - actual_bpe
                    calc_pct = (calc_diff / baseline_bpe) * 100.0

                    diff_ok = (rep_diff == calc_diff)
                    # Pct check within 0.25% for rounding
                    pct_ok = (rep_pct is not None and abs(rep_pct - calc_pct) <= 0.25)

                    print(f"      Savings Math: Expected −{calc_diff} BPE ({calc_pct:.1f}%) | Reported: −{rep_diff} BPE ({rep_pct}%) | Diff: {'OK' if diff_ok else 'FAIL'}, Pct: {'OK' if pct_ok else 'FAIL'}")

                    if not diff_ok:
                        issues.append(f"§3 Row {idx+1} BPE savings math error: baseline ({baseline_bpe}) - actual ({actual_bpe}) = {calc_diff}, but reported diff is {rep_diff}")
                    if not pct_ok:
                        issues.append(f"§3 Row {idx+1} percentage savings math error: expected {calc_pct:.1f}%, reported {rep_pct}%")

    # 8. Research and Provenance Links (§4) & Failure Modes (§5)
    sec4_match = re.search(r'## 4\.\s+Complete Bidirectional Research.*?\r?\n(.*?)(?=\r?\n## 5)', content, re.DOTALL)
    if sec4_match:
        sec4_text = sec4_match.group(1)
        # Check for expected links
        has_internal = bool(re.search(r'### 4\.1\s+Internal', sec4_text))
        has_external = bool(re.search(r'### 4\.2\s+External', sec4_text))
        has_modules = bool(re.search(r'### 4\.3\s+Canonical Plane 4', sec4_text))
        if not (has_internal and has_external and has_modules):
            issues.append(f"§4 missing expected subsections (Internal={has_internal}, External={has_external}, Plane4={has_modules})")
    else:
        issues.append("CRITICAL: §4 content missing")

    sec5_match = re.search(r'## 5\.\s+Failure Modes & Not-To-Dos.*?\r?\n(.*)', content, re.DOTALL)
    if sec5_match:
        sec5_text = sec5_match.group(1).strip()
        if len(sec5_text) < 50:
            issues.append("§5 content too brief or empty")
    else:
        issues.append("CRITICAL: §5 content missing")

    print("\n  Summary of Issues:")
    if issues:
        for iss in issues:
            print(f"    [FAIL] {iss}")
    else:
        print("    [PASS] ZERO ISSUES FOUND! Conforms 100% to all specifications.")

    return issues

if __name__ == "__main__":
    rules_3a = get_3a_rules()
    total_issues = 0
    file_results = {}
    for filename, tag in TARGET_RULES:
        issues = verify_single_rule(filename, tag, rules_3a)
        file_results[filename] = issues
        total_issues += len(issues)

    print("\n" + "#"*90)
    print("FINAL SUMMARY REPORT FOR MILESTONE 1 (RULES 02-08):")
    print("#"*90)
    for fn, issues in file_results.items():
        status = "PASSED (0 issues)" if not issues else f"FAILED ({len(issues)} issues)"
        print(f"  {fn:<30}: {status}")

    if total_issues == 0:
        print("\nOVERALL VERDICT: APPROVE (100% Empirical Verification Succeeded)")
        sys.exit(0)
    else:
        print(f"\nOVERALL VERDICT: REQUEST_CHANGES ({total_issues} Total Issues Detected)")
        sys.exit(1)
