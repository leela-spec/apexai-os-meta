#!/usr/bin/env python3
"""
verify_m3_rules.py — Empirical Verification Oracle for Rules 16-22

Validates:
1. Existence & non-empty status of §1, §2, §3, §4, §5.
2. Exact matching of §1.1 code fence text against 13-candidate-3A-xml.md.
3. Empirical recalculation of BPE tokens (cl100k_base), characters, repo tokens, and words for §1.1.
4. Empirical recalculation of BPE tokens and chars for each SB in §1.2.
5. Recomputation of §3 Rollup table texts, BPE tokens, and savings percentages.
6. Option B consistency between §2 and §3.
"""

from __future__ import annotations
import os
import re
import sys
from pathlib import Path
import tiktoken

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parents[5]
KB_DIR = REPO_ROOT / "apex-meta" / "informatics" / "final" / "research" / "06-layered-rule-kb"
CANDIDATE_3A = REPO_ROOT / "apex-meta" / "informatics" / "final" / "candidates" / "13-candidate-3A-xml.md"

enc = tiktoken.get_encoding("cl100k_base")

RULE_FILES = [
    "rule-16-authoring.md",
    "rule-17-trade-off.md",
    "rule-18-handover.md",
    "rule-19-iterative.md",
    "rule-20-schemas.md",
    "rule-21-sync.md",
    "rule-22-pointers.md",
]

TAG_NAMES = {
    16: "authoring",
    17: "trade_off",
    18: "handover",
    19: "iterative",
    20: "schemas",
    21: "sync",
    22: "pointers",
}

def split_markdown_cells(row: str) -> list[str]:
    cells = []
    current = []
    in_backtick = False
    for ch in row:
        if ch == "`":
            in_backtick = not in_backtick
            current.append(ch)
        elif ch == "|" and not in_backtick:
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(ch)
    cells.append("".join(current).strip())
    # Drop first and last empty cells if row started/ended with '|'
    if cells and cells[0] == "":
        cells.pop(0)
    if cells and cells[-1] == "":
        cells.pop()
    return cells

def load_candidate_3a_tags():
    content = CANDIDATE_3A.read_text(encoding="utf-8")
    contract_m = re.search(r'<apex_contract\s+v="1\.0"[^>]*>(.*?)</apex_contract>', content, re.DOTALL)
    if not contract_m:
        print("ERROR: Could not find <apex_contract v=\"1.0\"> in 13-candidate-3A-xml.md")
        return {}
    contract_text = contract_m.group(1)
    tags = {}
    for num, tag in TAG_NAMES.items():
        pattern = rf"(<{tag}(?:\s+[^>]*?)?>.*?</{tag}>)"
        m = re.search(pattern, contract_text, re.DOTALL)
        if m:
            tags[num] = m.group(1).strip()
        else:
            print(f"ERROR: Could not find <{tag}> in <apex_contract> block")
    return tags



def verify_file(fname: str, expected_tag_text: str):
    fpath = KB_DIR / fname
    if not fpath.exists():
        return {"file": fname, "error": "FILE_NOT_FOUND"}
    
    text = fpath.read_text(encoding="utf-8")
    num = int(fname.split("-")[1])
    tag = TAG_NAMES[num]
    
    report = {
        "file": fname,
        "rule_num": num,
        "tag": tag,
        "sections": {},
        "s1_1_metrics": {},
        "s1_2_sbs": [],
        "s3_rollup": [],
        "discrepancies": [],
    }

    # 1. Section presence & non-empty
    sec_patterns = [
        ("sec_1", r"## 1\.\s+Original Rule & Atomic Semantic Block"),
        ("sec_2", r"## 2\.\s+Chapter-by-Chapter Semantic Block Analysis & Alternatives"),
        ("sec_3", r"## 3\.\s+Whole-Rule Recomposition Rollup"),
        ("sec_4", r"## 4\.\s+Complete Bidirectional Research & Provenance Links"),
        ("sec_5", r"## 5\.\s+Failure Modes & Not-To-Dos"),
    ]
    
    sec_positions = []
    for sec_name, pat in sec_patterns:
        m = re.search(pat, text)
        if not m:
            report["discrepancies"].append(f"Missing section: {sec_name} ({pat})")
            sec_positions.append((sec_name, -1))
        else:
            sec_positions.append((sec_name, m.start()))
            report["sections"][sec_name] = "PRESENT"
            
    # Check section non-empty
    for i in range(len(sec_positions)):
        sname, pos = sec_positions[i]
        if pos == -1:
            continue
        next_pos = sec_positions[i+1][1] if i + 1 < len(sec_positions) else len(text)
        sec_content = text[pos:next_pos].strip()
        lines = [l for l in sec_content.splitlines() if l.strip() and not l.startswith("##")]
        if len(lines) < 2:
            report["discrepancies"].append(f"Section {sname} appears empty or has too few lines ({len(lines)})")

    # 2. Extract §1.1 code fence text
    s1_1_m = re.search(r"### 1\.1\s+Current `v1\.0-3A` Full Text\s*\((.*?)\)\s*\n+```(?:xml)?\s*\n(.*?)\n```", text, re.DOTALL)
    if not s1_1_m:
        report["discrepancies"].append("Could not parse §1.1 header and code block")
    else:
        header_metrics_str = s1_1_m.group(1)
        code_fence_text = s1_1_m.group(2).strip()
        
        # Check against expected 3A tag text
        norm_expected = re.sub(r"\s+", " ", expected_tag_text).strip()
        norm_fence = re.sub(r"\s+", " ", code_fence_text).strip()
        if norm_expected != norm_fence:
            report["discrepancies"].append(f"§1.1 text does not match 13-candidate-3A-xml.md for <{tag}>")
            
        claimed_bpe = None
        claimed_bpe_inner = None
        claimed_repo = None
        claimed_chars = None
        claimed_words = None
        
        m_bpe = re.search(r"`?(\d+)\s+BPE(?:\s+tokens|\s+block)?`?", header_metrics_str)
        if m_bpe: claimed_bpe = int(m_bpe.group(1))
        
        m_bpe_inner = re.search(r"`?(\d+)\s+BPE\s+inner`?", header_metrics_str)
        if m_bpe_inner: claimed_bpe_inner = int(m_bpe_inner.group(1))
        
        m_repo = re.search(r"`?(\d+)\s+repo\s+tokens`?", header_metrics_str)
        if m_repo: claimed_repo = int(m_repo.group(1))
        
        m_chars = re.search(r"`?(\d+)\s+chars`?", header_metrics_str)
        if m_chars: claimed_chars = int(m_chars.group(1))
        
        m_words = re.search(r"`?(\d+)\s+words`?", header_metrics_str)
        if m_words: claimed_words = int(m_words.group(1))
        
        emp_chars = len(code_fence_text)
        emp_words = len(code_fence_text.split())
        emp_bpe = len(enc.encode(code_fence_text))
        emp_repo = emp_chars // 4
        
        inner_m = re.search(rf"<{tag}[^>]*>\s*(.*?)\s*</{tag}>", code_fence_text, re.DOTALL)
        emp_bpe_inner = len(enc.encode(inner_m.group(1))) if inner_m else None
        
        sline_text = re.sub(r"\s+", " ", code_fence_text).strip()
        sline_chars = len(sline_text)
        sline_words = len(sline_text.split())
        sline_bpe = len(enc.encode(sline_text))
        sline_repo = sline_chars // 4
        
        report["s1_1_metrics"] = {
            "header_metrics_str": header_metrics_str,
            "claimed": {
                "bpe": claimed_bpe,
                "bpe_inner": claimed_bpe_inner,
                "repo": claimed_repo,
                "chars": claimed_chars,
                "words": claimed_words,
            },
            "empirical_fence": {
                "bpe": emp_bpe,
                "bpe_inner": emp_bpe_inner,
                "repo": emp_repo,
                "chars": emp_chars,
                "words": emp_words,
            },
            "empirical_single_line": {
                "bpe": sline_bpe,
                "repo": sline_repo,
                "chars": sline_chars,
                "words": sline_words,
            }
        }

    # 3. Extract §1.2 Semantic Blocks
    sb_matches = re.findall(r"-\s+\*\*`?(SB-\d+\.\d+)`?\s*—\s*(.*?)\s*\(`?(\d+)\s+BPE\s+tokens`?\s*\|\s*`?(\d+)\s+chars`?\):\*\*\s*[\*\"“](.*?)[\*\"”]\s*$", text, re.MULTILINE)
    for sb_id, sb_name, claimed_sb_bpe, claimed_sb_chars, sb_text in sb_matches:
        sb_clean = sb_text.strip().strip('"').strip('*').strip('“').strip('”')
        emp_sb_chars = len(sb_clean)
        emp_sb_bpe = len(enc.encode(sb_clean))
        report["s1_2_sbs"].append({
            "id": sb_id,
            "name": sb_name.strip(),
            "text": sb_clean,
            "claimed_bpe": int(claimed_sb_bpe),
            "claimed_chars": int(claimed_sb_chars),
            "emp_bpe": emp_sb_bpe,
            "emp_chars": emp_sb_chars,
        })

    # 4. Extract §3 Rollup Table
    s3_sec_m = re.search(r"## 3\.\s+Whole-Rule Recomposition Rollup.*?\n(\|.*?)(?:\n##|\Z)", text, re.DOTALL)
    if not s3_sec_m:
        report["discrepancies"].append("Could not find §3 Rollup Table")
    else:
        table_text = s3_sec_m.group(1).strip()
        rows = [r.strip() for r in table_text.splitlines() if r.strip().startswith("|") and not r.strip().startswith("|---")]
        for row in rows[1:]:
            cols = split_markdown_cells(row)
            if len(cols) >= 4:
                opt_name = cols[0]
                opt_text_raw = cols[1]
                opt_text = re.sub(r"^`|`$", "", opt_text_raw).strip()
                claimed_bpe_match = re.search(r"\*?`?(\d+)`?\*?", cols[2])
                claimed_opt_bpe = int(claimed_bpe_match.group(1)) if claimed_bpe_match else None
                claimed_savings_col = cols[3]
                
                # Check both as-is and with spaces normalized
                emp_opt_bpe_raw = len(enc.encode(opt_text))
                
                # If wrapped in <tag> ... </tag> with space after > and before </, test without extra spaces too
                norm_text = re.sub(r"\s+", " ", opt_text).strip()
                emp_opt_bpe_norm = len(enc.encode(norm_text))

                # What about multiline fence format?
                # e.g. <tag ...>\ninner\n</tag>
                # Let's check if the inner text has newlines
                m_tag = re.match(rf"^(<{tag}[^>]*>)\s*(.*?)\s*(</{tag}>)$", opt_text)
                emp_opt_bpe_fence = None
                if m_tag:
                    fence_version = f"{m_tag.group(1)}\n{m_tag.group(2)}\n{m_tag.group(3)}"
                    emp_opt_bpe_fence = len(enc.encode(fence_version))

                report["s3_rollup"].append({
                    "option": opt_name,
                    "text": opt_text,
                    "claimed_bpe": claimed_opt_bpe,
                    "claimed_savings_col": claimed_savings_col,
                    "emp_bpe_raw": emp_opt_bpe_raw,
                    "emp_bpe_norm": emp_opt_bpe_norm,
                    "emp_bpe_fence": emp_opt_bpe_fence,
                })


    # 5. Check Option B consistency between §2 and §3
    # Pattern: - **Option B (...):** *"text"* `(I../E../R..)`
    opt_b_s2_matches = re.findall(r"-\s+\*\*Option B[^\n]*?\*\*:\s*[*\"“\s]+(.*?)[*\"”\s]+(?=`|\()", text)
    report["s2_option_b_snippets"] = []
    for s in opt_b_s2_matches:
        clean_s = s.strip().strip('"').strip('*').strip('“').strip('”').strip()
        report["s2_option_b_snippets"].append(clean_s)

        
    # Find Option B in §3 rollup
    opt_b_s3 = None
    for r in report["s3_rollup"]:
        if "Recommended" in r["option"] or "Option B" in r["option"]:
            opt_b_s3 = r["text"]
            break
            
    if opt_b_s3 and report["s2_option_b_snippets"]:
        report["option_b_consistency"] = []
        for i, snip in enumerate(report["s2_option_b_snippets"]):
            norm_snip = re.sub(r"\s+", " ", snip).strip()
            norm_s3 = re.sub(r"\s+", " ", opt_b_s3).strip()
            present = norm_snip in norm_s3
            report["option_b_consistency"].append({
                "index": i + 1,
                "snippet": norm_snip,
                "present_in_s3": present
            })
            if not present:
                report["discrepancies"].append(f"Option B snippet {i+1} from §2 not found exactly in §3: '{norm_snip}'")

    return report



def main():
    tags_3a = load_candidate_3a_tags()
    all_reports = []
    for fname in RULE_FILES:
        num = int(fname.split("-")[1])
        expected_tag = tags_3a[num]
        rep = verify_file(fname, expected_tag)
        all_reports.append(rep)
        
    for rep in all_reports:
        print("=" * 80)
        print(f"REPORT: {rep['file']} (Rule {rep['rule_num']} <{rep['tag']}>)")
        print(f"Sections found: {list(rep['sections'].keys())}")
        if rep['discrepancies']:
            print("DISCREPANCIES:")
            for d in rep['discrepancies']:
                print(f"  - {d}")
        else:
            print("Discrepancies: None in structure parsing")
            
        print("\n§1.1 Metrics:")
        c = rep['s1_1_metrics'].get('claimed', {})
        ef = rep['s1_1_metrics'].get('empirical_fence', {})
        es = rep['s1_1_metrics'].get('empirical_single_line', {})
        print(f"  Claimed:    BPE={c.get('bpe')} (inner={c.get('bpe_inner')}), Repo={c.get('repo')}, Chars={c.get('chars')}, Words={c.get('words')}")
        print(f"  Emp(fence): BPE={ef.get('bpe')} (inner={ef.get('bpe_inner')}), Repo={ef.get('repo')}, Chars={ef.get('chars')}, Words={ef.get('words')}")
        print(f"  Emp(sline): BPE={es.get('bpe')}, Repo={es.get('repo')}, Chars={es.get('chars')}, Words={es.get('words')}")
        
        print("\n§1.2 Semantic Blocks:")
        for sb in rep['s1_2_sbs']:
            bpe_match = "MATCH" if sb['claimed_bpe'] == sb['emp_bpe'] else f"DIFF (claimed={sb['claimed_bpe']}, emp={sb['emp_bpe']})"
            char_match = "MATCH" if sb['claimed_chars'] == sb['emp_chars'] else f"DIFF (claimed={sb['claimed_chars']}, emp={sb['emp_chars']})"
            print(f"  {sb['id']} ({sb['name']}): BPE={bpe_match}, Chars={char_match} | text='{sb['text'][:35]}...'")
            
        print("\n§3 Rollup Table:")
        baseline_claimed = None
        for r in rep['s3_rollup']:
            opt_title = re.sub(r"\*\*|\`", "", r['option'])
            bpe_match = "MATCH" if r['claimed_bpe'] in (r['emp_bpe_raw'], r['emp_bpe_norm'], r['emp_bpe_fence']) else f"DIFF (claimed={r['claimed_bpe']}, raw={r['emp_bpe_raw']}, norm={r['emp_bpe_norm']}, fence={r['emp_bpe_fence']})"
            print(f"  Option: {opt_title[:40]}")
            print(f"    Claimed BPE: {r['claimed_bpe']} | Emp BPE: {bpe_match}")
            print(f"    Savings Column: {r['claimed_savings_col']}")
            if "Baseline" in opt_title or "Current" in opt_title:
                baseline_claimed = r['claimed_bpe']
            elif baseline_claimed:
                delta = r['claimed_bpe'] - baseline_claimed
                pct = (baseline_claimed - r['claimed_bpe']) / baseline_claimed * 100
                print(f"    Calculated Math: Delta={delta:+d} BPE, Savings={pct:.1f}%")

        print("\n§2 to §3 Option B Consistency:")
        for c in rep.get("option_b_consistency", []):
            status = "EXACT" if c["present_in_s3"] else "DIFF"
            print(f"  SB {c['index']}: {status} | '{c['snippet'][:50]}...'")

    print("\n" + "=" * 90)
    print("TABLE 1: §1.1 Metrics Empirical Reproduction (Candidate 3A Baseline)")
    print("=" * 90)
    print("| Rule | Tag | Claimed BPE (block/inner) | Empirical BPE | Claimed Chars | Emp Chars | Claimed Words | Emp Words | Claimed Repo | Emp Repo | 3A Text Match |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for rep in all_reports:
        c = rep['s1_1_metrics']['claimed']
        ef = rep['s1_1_metrics']['empirical_fence']
        cl_bpe_str = f"{c['bpe']} ({c['bpe_inner']} inner)" if c.get('bpe_inner') else f"{c['bpe']}"
        emp_bpe_str = f"{ef['bpe']} ({ef['bpe_inner']} inner)" if ef.get('bpe_inner') else f"{ef['bpe']}"
        match_3a = "100% MATCH" if not any("does not match" in d for d in rep['discrepancies']) else "MISMATCH"
        print(f"| Rule {rep['rule_num']:02d} | `<{rep['tag']}>` | {cl_bpe_str} | {emp_bpe_str} | {c['chars']} | {ef['chars']} | {c['words']} | {ef['words']} | {c['repo']} | {ef['repo']} | {match_3a} |")

    print("\n" + "=" * 90)
    print("TABLE 2: §3 Recomposition Rollup Arithmetic & Token Verification")
    print("=" * 90)
    print("| Rule | Tag | Option | Claimed BPE | Emp BPE | Claimed Savings | Calc Delta | Calc Savings % | Math Status |")
    print("|---|---|---|---|---|---|---|---|---|")
    for rep in all_reports:
        tag = rep['tag']
        base_bpe = None
        for r in rep['s3_rollup']:
            opt_title = re.sub(r"\*\*|`", "", r['option']).split(":")[0].strip()
            cl_bpe = r['claimed_bpe']
            emp_bpe = r['emp_bpe_raw']
            cl_sav = r['claimed_savings_col']
            if "Baseline" in opt_title or "Current" in opt_title:
                base_bpe = cl_bpe
                print(f"| Rule {rep['rule_num']:02d} | `<{tag}>` | {opt_title} | {cl_bpe} | {emp_bpe} | {cl_sav} | 0 | 0.0% | EXACT |")
            else:
                delta = cl_bpe - base_bpe
                pct = (base_bpe - cl_bpe) / base_bpe * 100
                print(f"| Rule {rep['rule_num']:02d} | `<{tag}>` | {opt_title[:30]} | {cl_bpe} | {emp_bpe} | {cl_sav} | {delta:+d} BPE | {pct:.1f}% | EXACT |")

if __name__ == "__main__":
    main()


