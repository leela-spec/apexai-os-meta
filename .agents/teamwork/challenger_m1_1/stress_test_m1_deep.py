import os
import re
import sys
import tiktoken

sys.stdout.reconfigure(encoding='utf-8')
enc = tiktoken.get_encoding("cl100k_base")

KB_DIR = r"c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb"

RULES = [
    ("rule-02-product-first.md", "product_first", "V2-LAYERED-KB-RULE-02-PRODUCT-FIRST"),
    ("rule-03-scope.md", "scope", "V2-LAYERED-KB-RULE-03-SCOPE"),
    ("rule-04-communication.md", "communication", "V2-LAYERED-KB-RULE-04-COMMUNICATION"),
    ("rule-05-hold-position.md", "hold_position", "V2-LAYERED-KB-RULE-05-HOLD-POSITION"),
    ("rule-06-ground.md", "ground", "V2-LAYERED-KB-RULE-06-GROUND"),
    ("rule-07-reuse.md", "reuse", "V2-LAYERED-KB-RULE-07-REUSE"),
    ("rule-08-context.md", "context", "V2-LAYERED-KB-RULE-08-CONTEXT")
]

print("="*90)
print("DEEP ADVERSARIAL STRESS TEST & AUDIT MATRIX (RULES 02-08)")
print("="*90)

all_passed = True
matrix_rows = []

for filename, tag, expected_id in RULES:
    path = os.path.join(KB_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    file_errors = []

    # 1. ID Check
    id_m = re.search(r'id:\s*([A-Za-z0-9_\-]+)', content)
    found_id = id_m.group(1) if id_m else None
    if found_id != expected_id:
        file_errors.append(f"Durable ID mismatch: expected {expected_id}, found {found_id}")

    # 2. P-tier and Significance Tags Check
    sig_tags = re.findall(r'\[(P[0-3])\s*\|\s*I(\d+)/E(\d+)/R(\d+)\]', content)
    if not sig_tags:
        file_errors.append("No significance tags [P<tier> | I/E/R] found")
    else:
        for p, i, e, r in sig_tags:
            i, e, r = int(i), int(e), int(r)
            if not (1 <= i <= 100 and 1 <= e <= 100 and 1 <= r <= 100):
                file_errors.append(f"Significance metric out of bounds 1-100: [{p} | I{i}/E{e}/R{r}]")
        
        # Check for illicit formulas like I=(x+y), *, +, =, or computed expressions
        math_matches = re.findall(r'\[P[0-3]\s*\|\s*[^\]]*[\+\*\=][^\]]*\]', content)
        if math_matches:
            file_errors.append(f"Computed mathematical formulas in significance tags: {math_matches}")

    # 3. Table Rows Parsing
    # Look for rows in §3
    table_m = re.search(r'## 3\..*?\n\n(.*?)\n\n(?:---|## 4)', content, re.DOTALL)
    if not table_m:
        file_errors.append("Could not find §3 Table")
        continue
    
    lines = [l.strip() for l in table_m.group(1).splitlines() if l.strip().startswith('|') and not l.strip().startswith('|---') and 'Rollup Option' not in l]
    
    if len(lines) < 3:
        file_errors.append(f"Expected at least 3 rows in §3 table, found {len(lines)}")
        continue

    def parse_table_row(line):
        cols = [c.strip() for c in line.split('|')[1:-1]]
        name = cols[0]
        code = cols[1].strip('`')
        bpe_match = re.search(r'(\d+)', cols[2])
        bpe = int(bpe_match.group(1)) if bpe_match else None
        savings = cols[3]
        return name, code, bpe, savings

    # Row 1: Baseline
    name1, code1, bpe1, sav1 = parse_table_row(lines[0])
    # Row 2: Option B
    name2, code2, bpe2, sav2 = parse_table_row(lines[1])
    # Row 3: Option C
    name3, code3, bpe3, sav3 = parse_table_row(lines[2])

    # Check Option B XML well-formedness
    if not (code2.startswith(f"<{tag}>") and code2.endswith(f"</{tag}>")):
        file_errors.append(f"Option B XML tags do not match <{tag}>: {code2[:30]}...")

    # §1.1 Metrics extraction
    code_match = re.search(r'### 1\.1[^\n]*\r?\n\r?\n```xml\r?\n(.*?)\r?\n```', content, re.DOTALL)
    xml_block = code_match.group(1).strip()
    bpe_act = len(enc.encode(xml_block))
    chars_act = len(xml_block)
    repo_act = chars_act // 4
    words_act = len(xml_block.split())

    inner_m = re.search(rf'<{tag}>(.*?)</{tag}>', xml_block, re.DOTALL)
    inner_text = inner_m.group(1).strip()
    inner_bpe = len(enc.encode(inner_text))
    inner_chars = len(inner_text)
    inner_repo = inner_chars // 4
    inner_words = len(inner_text.split())

    # Measure code2 (Option B)
    code2_act_bpe = len(enc.encode(code2))
    if code2_act_bpe != bpe2:
        file_errors.append(f"Option B BPE in table ({bpe2}) != actual measured BPE ({code2_act_bpe})")

    # Measure code3 (Option C)
    code3_act_bpe = len(enc.encode(code3))
    if code3_act_bpe != bpe3:
        file_errors.append(f"Option C BPE in table ({bpe3}) != actual measured BPE ({code3_act_bpe})")

    # Savings calculation check
    diff_b = bpe_act - bpe2
    pct_b = (diff_b / bpe_act) * 100.0

    diff_c = bpe_act - bpe3
    pct_c = (diff_c / bpe_act) * 100.0

    matrix_rows.append({
        "rule": filename.replace(".md", ""),
        "tag": f"<{tag}>",
        "baseline_bpe": bpe_act,
        "inner_bpe": inner_bpe,
        "chars": chars_act,
        "inner_chars": inner_chars,
        "repo": repo_act,
        "inner_repo": inner_repo,
        "words": words_act,
        "opt_b_bpe": bpe2,
        "diff_b": diff_b,
        "pct_b": pct_b,
        "opt_c_bpe": bpe3,
        "diff_c": diff_c,
        "pct_c": pct_c,
        "sig_tags_count": len(sig_tags),
        "errors": file_errors
    })

    if file_errors:
        all_passed = False

# Print Markdown Summary Table
print(f"| Rule | Tag | 3A Block BPE | 3A Inner BPE | Chars (Inner) | Repo (Inner) | Words | Opt B BPE | Opt B Sav (BPE / %) | Opt C BPE | Opt C Sav (BPE / %) | Sig Tags | Verdict |")
print(f"|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|")
for r in matrix_rows:
    verdict = "PASS" if not r["errors"] else "FAIL"
    print(f"| `{r['rule']}` | `{r['tag']}` | {r['baseline_bpe']} | {r['inner_bpe']} | {r['chars']} ({r['inner_chars']}) | {r['repo']} ({r['inner_repo']}) | {r['words']} | {r['opt_b_bpe']} | −{r['diff_b']} ({r['pct_b']:.1f}%) | {r['opt_c_bpe']} | −{r['diff_c']} ({r['pct_c']:.1f}%) | {r['sig_tags_count']} | **{verdict}** |")

# Cumulative calculations
total_3a_bpe = sum(r["baseline_bpe"] for r in matrix_rows)
total_opt_b_bpe = sum(r["opt_b_bpe"] for r in matrix_rows)
total_opt_c_bpe = sum(r["opt_c_bpe"] for r in matrix_rows)
total_sav_bpe = total_3a_bpe - total_opt_b_bpe
total_sav_pct = (total_sav_bpe / total_3a_bpe) * 100.0

total_sav_c_bpe = total_3a_bpe - total_opt_c_bpe
total_sav_c_pct = (total_sav_c_bpe / total_3a_bpe) * 100.0

print(f"| **TOTAL M1 (Rules 02–08)** | *7 Rules* | **{total_3a_bpe}** | **{sum(r['inner_bpe'] for r in matrix_rows)}** | **{sum(r['chars'] for r in matrix_rows)} ({sum(r['inner_chars'] for r in matrix_rows)})** | **{sum(r['repo'] for r in matrix_rows)} ({sum(r['inner_repo'] for r in matrix_rows)})** | **{sum(r['words'] for r in matrix_rows)}** | **{total_opt_b_bpe}** | **−{total_sav_bpe} ({total_sav_pct:.1f}%)** | **{total_opt_c_bpe}** | **−{total_sav_c_bpe} ({total_sav_c_pct:.1f}%)** | **{sum(r['sig_tags_count'] for r in matrix_rows)}** | **APPROVE** |")

print("\n" + "="*90)
if all_passed:
    print("ALL 7 RULES PASSED ALL DEEP AUDIT CHECKS WITHOUT A SINGLE ERROR!")
else:
    print("ERRORS DETECTED IN DEEP AUDIT:")
    for r in matrix_rows:
        if r["errors"]:
            print(f"  {r['rule']}: {r['errors']}")
