#!/usr/bin/env python3
"""
verify_m2_rules.py — Comprehensive Empirical Verification Harness for M2 (Rules 09-15)
Author: Milestone 2 Challenger 1 (critic, specialist)
Working Directory: c:\\GitDev\\apexai-os-meta\\.agents\\teamwork\\challenger_m2_1

Empirically verifies:
1. Exact match with Layer 0 canonical contract (13-candidate-3A-xml.md)
2. Frontmatter integrity (OKF v0.2, flat YAML, required fields)
3. Mandatory section presence and non-emptiness (§1, §2, §3, §4, §5)
4. Empirical metrics computation:
   - §1.1 block & inner text: BPE (cl100k_base), chars, words, repo tokens (chars // 4)
   - §1.2 Semantic Blocks: individual BPE, chars, and concatenation completeness
   - §2 Chapter-by-chapter Options A/B/C BPE metrics and significance tags
   - §3 Recomposition Rollup table: text BPE, mathematical formula calculations (delta, percentage)
5. Relative link resolution across disk
"""

from __future__ import annotations
import os
import re
import sys
from pathlib import Path
import tiktoken

REPO_ROOT = Path("c:/GitDev/apexai-os-meta")
LAYERED_KB_DIR = REPO_ROOT / "apex-meta" / "informatics" / "final" / "research" / "06-layered-rule-kb"
CANDIDATE_3A = REPO_ROOT / "apex-meta" / "informatics" / "final" / "candidates" / "13-candidate-3A-xml.md"

M2_RULES = [
    ("rule-09-recovery.md", "recovery"),
    ("rule-10-stop-repairing.md", "stop_repairing"),
    ("rule-11-current-truth.md", "current_truth"),
    ("rule-12-surgical.md", "surgical"),
    ("rule-13-editing.md", "editing"),
    ("rule-14-new-machinery.md", "new_machinery"),
    ("rule-15-detour.md", "detour"),
]

enc = tiktoken.get_encoding("cl100k_base")

def get_bpe(text: str) -> int:
    return len(enc.encode(text))

def extract_3a_tags(path: Path) -> dict[str, str]:
    content = path.read_text(encoding="utf-8")
    # extract xml blocks inside ```xml ... ```
    m = re.search(r"```xml\s*(<apex_contract.*?</apex_contract>)\s*```", content, re.DOTALL)
    if not m:
        raise ValueError("Could not find <apex_contract> block in 13-candidate-3A-xml.md")
    xml_block = m.group(1)
    
    tags = {}
    for rule_name, tag in M2_RULES:
        # Match tag with optional attributes
        pattern = rf"(<{tag}(?:\s+[^>]*?)?>.*?</{tag}>)"
        tag_match = re.search(pattern, xml_block, re.DOTALL)
        if not tag_match:
            raise ValueError(f"Tag <{tag}> not found in 13-candidate-3A-xml.md")
        tags[tag] = tag_match.group(1).strip()
    return tags

def verify_file(fname: str, tag: str, expected_3a_block: str) -> dict:
    fpath = LAYERED_KB_DIR / fname
    results = {
        "file": fname,
        "tag": tag,
        "errors": [],
        "warnings": [],
        "metrics": {},
    }
    
    if not fpath.exists():
        results["errors"].append(f"File not found: {fpath}")
        return results

    content = fpath.read_text(encoding="utf-8")
    lines = content.splitlines()

    # 1. Frontmatter verification
    if not content.startswith("---"):
        results["errors"].append("Missing YAML frontmatter opening '---'")
    else:
        parts = content.split("---", 2)
        if len(parts) < 3:
            results["errors"].append("Malformed YAML frontmatter (missing closing '---')")
        else:
            fm_text = parts[1]
            for i, fm_line in enumerate(fm_text.strip().splitlines(), 1):
                if fm_line.strip() and ":" not in fm_line:
                    results["errors"].append(f"Frontmatter line {i} missing colon: '{fm_line}'")
            if "type: Reference" not in fm_text:
                results["errors"].append("Frontmatter missing 'type: Reference'")
            if f"V2-LAYERED-KB-RULE-" not in fm_text:
                results["errors"].append("Frontmatter missing 'id: V2-LAYERED-KB-RULE-...'")
            if "status: current_truth" not in fm_text:
                results["warnings"].append("Frontmatter status is not 'current_truth'")

    # 2. Section Checks (§1, §2, §3, §4, §5)
    sections = [
        ("Position in Layered Knowledge Base", r"> \*\*Position in Layered Knowledge Base:\*\*"),
        ("§1 Original Rule", r"## 1\. Original Rule"),
        ("§2 Chapter-by-Chapter", r"## 2\. Chapter-by-Chapter"),
        ("§3 Whole-Rule Recomposition Rollup", r"## 3\. Whole-Rule Recomposition Rollup"),
        ("§4 Bidirectional Research & Provenance Links", r"## 4\. Complete Bidirectional Research"),
        ("§5 Failure Modes & Not-To-Dos", r"## 5\. Failure Modes & Not-To-Dos"),
    ]
    for sname, spattern in sections:
        if not re.search(spattern, content):
            results["errors"].append(f"Missing mandatory section: {sname}")

    # 3. §1.1 Verification against 13-candidate-3A-xml.md
    s1_1_match = re.search(r"### 1\.1 Current `v1\.0-3A` Full Text \((.*?)\)\s*```xml\s*(.*?)\s*```", content, re.DOTALL)
    if not s1_1_match:
        results["errors"].append("Could not parse §1.1 Full Text and code block")
    else:
        header_metrics_str = s1_1_match.group(1)
        actual_block_text = s1_1_match.group(2).strip()

        # Check exact text match with 13-candidate-3A-xml.md
        # Normalize line endings to \n
        norm_actual = "\n".join(l.rstrip() for l in actual_block_text.splitlines())
        norm_expected = "\n".join(l.rstrip() for l in expected_3a_block.splitlines())
        if norm_actual != norm_expected:
            results["errors"].append(f"§1.1 text does not match 13-candidate-3A-xml.md!\nActual:\n{norm_actual}\nExpected:\n{norm_expected}")

        # Compute empirical metrics of the block
        actual_block_bpe = get_bpe(norm_actual)
        actual_block_chars = len(norm_actual)
        actual_block_words = len(norm_actual.split())
        actual_block_repo = actual_block_chars // 4

        # Extract inner text (inside <tag ...>...</tag>)
        inner_m = re.search(rf"<{tag}(?:\s+[^>]*?)?>\s*(.*?)\s*</{tag}>", norm_actual, re.DOTALL)
        if not inner_m:
            results["errors"].append(f"Could not extract inner text from tag <{tag}>")
            inner_text = norm_actual
        else:
            inner_text = inner_m.group(1).strip()
            # replace internal multiple whitespace with single space for inner text
            inner_text_norm = " ".join(inner_text.split())

        inner_bpe = get_bpe(inner_text)
        inner_chars = len(inner_text)
        inner_words = len(inner_text.split())
        inner_repo = inner_chars // 4

        results["metrics"]["3A_block_bpe"] = actual_block_bpe
        results["metrics"]["3A_inner_bpe"] = inner_bpe
        results["metrics"]["3A_inner_chars"] = inner_chars
        results["metrics"]["3A_inner_words"] = inner_words
        results["metrics"]["3A_inner_repo"] = inner_repo

        # Parse claimed numbers from header string, e.g.
        # "38 BPE block | 31 BPE inner | 44 repo tokens | 179 chars | 25 words"
        claimed_block_bpe = re.search(r"(\d+)\s*BPE\s*block", header_metrics_str)
        claimed_inner_bpe = re.search(r"(\d+)\s*BPE\s*inner", header_metrics_str)
        claimed_repo = re.search(r"(\d+)\s*repo tokens", header_metrics_str)
        claimed_chars = re.search(r"(\d+)\s*chars", header_metrics_str)
        claimed_words = re.search(r"(\d+)\s*words", header_metrics_str)

        if claimed_block_bpe and int(claimed_block_bpe.group(1)) != actual_block_bpe:
            results["errors"].append(f"§1.1 header block BPE mismatch: claimed {claimed_block_bpe.group(1)}, actual {actual_block_bpe}")
        if claimed_inner_bpe and int(claimed_inner_bpe.group(1)) != inner_bpe:
            # Check if inner_text_norm matches
            if int(claimed_inner_bpe.group(1)) != get_bpe(inner_text_norm):
                results["errors"].append(f"§1.1 header inner BPE mismatch: claimed {claimed_inner_bpe.group(1)}, actual {inner_bpe} (norm {get_bpe(inner_text_norm)})")
        if claimed_repo and int(claimed_repo.group(1)) not in (inner_repo, actual_block_repo):
            results["errors"].append(f"§1.1 header repo tokens mismatch: claimed {claimed_repo.group(1)}, inner {inner_repo}, block {actual_block_repo}")
        if claimed_chars and int(claimed_chars.group(1)) not in (inner_chars, len(inner_text_norm), actual_block_chars):
            results["errors"].append(f"§1.1 header chars mismatch: claimed {claimed_chars.group(1)}, inner {inner_chars}, block {actual_block_chars}")
        if claimed_words and int(claimed_words.group(1)) not in (inner_words, actual_block_words):
            results["errors"].append(f"§1.1 header words mismatch: claimed {claimed_words.group(1)}, inner {inner_words}, block {actual_block_words}")

    # 4. §1.2 Semantic Blocks Inventory
    sb_pattern = r"- \*\*`(SB-\d+\.\d+)`\s*—\s*[^`*]+\(`(\d+)\s*BPE tokens`\s*\|\s*`(\d+)\s*chars`\):\*\*\s*[\"“*]*(.*?)[\"”*]*$"
    sb_matches = re.findall(sb_pattern, content, re.MULTILINE)
    if not sb_matches:
        results["errors"].append("Could not parse any semantic blocks in §1.2")
    else:
        results["metrics"]["num_sb"] = len(sb_matches)
        extracted_sb_texts = []
        for sb_id, claimed_bpe, claimed_chars, sb_text_raw in sb_matches:
            # Clean quotes or markdown formatting
            sb_text = sb_text_raw.strip().strip('*').strip('"').strip('“').strip('”')
            calc_bpe = get_bpe(sb_text)
            calc_chars = len(sb_text)
            extracted_sb_texts.append(sb_text)
            if calc_bpe != int(claimed_bpe):
                results["errors"].append(f"§1.2 {sb_id} BPE mismatch: claimed {claimed_bpe}, calculated {calc_bpe} for text '{sb_text}'")
            if calc_chars != int(claimed_chars):
                results["errors"].append(f"§1.2 {sb_id} chars mismatch: claimed {claimed_chars}, calculated {calc_chars} for text '{sb_text}'")

        # Check concatenation against inner text
        # If we join by space, does it contain all words?
        joined_sb = " ".join(extracted_sb_texts)
        # Compare word set / sequence
        sb_words = joined_sb.split()
        inner_words_list = inner_text.split()
        if sb_words != inner_words_list:
            # Check if difference is trivial punctuation or whitespace
            if "".join(re.findall(r"\w+", joined_sb)) != "".join(re.findall(r"\w+", inner_text)):
                results["warnings"].append(f"Semantic block concatenation does not match inner text word-for-word")

    # 5. §3 Whole-Rule Recomposition Rollup Table
    # Parse markdown table
    s3_match = re.search(r"## 3\. Whole-Rule Recomposition Rollup.*?\n\n(.*?)(?=\n## 4|\Z)", content, re.DOTALL)
    if not s3_match:
        results["errors"].append("Could not find §3 section content")
    else:
        table_text = s3_match.group(1).strip()
        table_lines = [l.strip() for l in table_text.splitlines() if l.strip().startswith("|")]
        if len(table_lines) < 4:
            results["errors"].append(f"§3 table has fewer than 4 rows (header + divider + rows), found {len(table_lines)}")
        else:
            # table_lines[0] is header, [1] is divider, [2:] are rows
            header_cols = [c.strip() for c in table_lines[0].split("|")[1:-1]]
            rows = []
            for row_line in table_lines[2:]:
                cols = [c.strip() for c in row_line.split("|")[1:-1]]
                if len(cols) >= 4:
                    rows.append(cols)

            if len(rows) < 3:
                results["errors"].append(f"§3 table has fewer than 3 data rows, found {len(rows)}")
            else:
                baseline_bpe = None
                for idx, row in enumerate(rows):
                    opt_name = row[0]
                    opt_text_raw = row[1]
                    # strip code ticks if any
                    opt_text = opt_text_raw.strip('`')
                    bpe_str = row[2].strip('*').strip('`')
                    savings_str = row[3]

                    actual_row_bpe = get_bpe(opt_text)
                    claimed_row_bpe = int(bpe_str) if bpe_str.isdigit() else None

                    if claimed_row_bpe is not None and claimed_row_bpe != actual_row_bpe:
                        results["errors"].append(f"§3 Row {idx+1} ({opt_name}) BPE mismatch: claimed {claimed_row_bpe}, actual {actual_row_bpe}")

                    if idx == 0:
                        baseline_bpe = claimed_row_bpe or actual_row_bpe
                        results["metrics"]["table_baseline_bpe"] = baseline_bpe
                    else:
                        # Check savings calculation
                        if "Option B" in opt_name or idx == 1:
                            results["metrics"]["table_opt_b_bpe"] = claimed_row_bpe or actual_row_bpe
                        elif "Option C" in opt_name or idx == 2:
                            results["metrics"]["table_opt_c_bpe"] = claimed_row_bpe or actual_row_bpe

                        if baseline_bpe:
                            expected_delta = (claimed_row_bpe or actual_row_bpe) - baseline_bpe
                            expected_pct = (expected_delta / baseline_bpe) * 100

                            # Look for delta in savings_str, e.g. "−4 BPE" or "-4 BPE" or "+1 BPE"
                            # Unicode minus: \u2212 or ascii -
                            delta_match = re.search(r"([+−-]\d+)\s*BPE", savings_str)
                            pct_match = re.search(r"([+−-]?\d+(?:\.\d+)?)\s*%", savings_str)

                            if delta_match:
                                claimed_delta = int(delta_match.group(1).replace("−", "-"))
                                if claimed_delta != expected_delta:
                                    results["errors"].append(f"§3 Row {idx+1} savings delta mismatch: claimed {claimed_delta}, computed {expected_delta}")
                            if pct_match:
                                claimed_pct = float(pct_match.group(1).replace("−", "-"))
                                # Allow rounding tolerance +/- 0.5%
                                if abs(claimed_pct - expected_pct) > 0.6:
                                    results["errors"].append(f"§3 Row {idx+1} savings pct mismatch: claimed {claimed_pct}%, computed {expected_pct:.1f}%")

    # 6. Relative links resolution
    link_pattern = r"\[([^\]]+)\]\(([^)]+)\)"
    all_links = re.findall(link_pattern, content)
    broken_links = []
    for ltext, lurl in all_links:
        if lurl.startswith("http://") or lurl.startswith("https://") or lurl.startswith("#"):
            continue
        # Strip anchors
        import urllib.parse
        target_path_raw = lurl.split("#")[0]
        if not target_path_raw:
            continue
        target_path_str = urllib.parse.unquote(target_path_raw)
        resolved_path = (fpath.parent / target_path_str).resolve()
        if not resolved_path.exists():
            broken_links.append((lurl, str(resolved_path)))

    if broken_links:
        for orig, res in broken_links:
            results["errors"].append(f"Broken relative link: '{orig}' -> '{res}' does not exist")
    else:
        results["metrics"]["relative_links_verified"] = len([l for l in all_links if not (l[1].startswith("http") or l[1].startswith("#"))])

    # 7. Significance tags audit
    sig_tags = re.findall(r"\[(P[0-3])\s*\|\s*I(\d{1,3})/E(\d{1,3})/R(\d{1,3})\]", content)
    results["metrics"]["sig_tags_count"] = len(sig_tags)
    for p, i, e, r in sig_tags:
        if not (1 <= int(i) <= 100 and 1 <= int(e) <= 100 and 1 <= int(r) <= 100):
            results["errors"].append(f"Invalid significance tag range: [{p} | I{i}/E{e}/R{r}]")

    return results

def main():
    print("================================================================================")
    print("MILESTONE 2 EMPIRICAL TOKEN & CONTENT VERIFICATION HARNESS (RULES 09-15)")
    print("================================================================================")

    tags_3a = extract_3a_tags(CANDIDATE_3A)
    print(f"Loaded {len(tags_3a)} canonical tags from 13-candidate-3A-xml.md\n")

    overall_passed = True
    summary_table = []

    for fname, tag in M2_RULES:
        res = verify_file(fname, tag, tags_3a[tag])
        status = "PASS" if not res["errors"] else "FAIL"
        if status == "FAIL":
            overall_passed = False

        m = res["metrics"]
        summary_table.append((
            fname,
            tag,
            m.get("3A_block_bpe", "N/A"),
            m.get("3A_inner_bpe", "N/A"),
            m.get("3A_inner_chars", "N/A"),
            m.get("3A_inner_words", "N/A"),
            m.get("table_opt_b_bpe", "N/A"),
            m.get("table_opt_c_bpe", "N/A"),
            len(res["errors"]),
            len(res["warnings"]),
            status
        ))

        print(f"--- {fname} (<{tag}>) ---")
        print(f"  Status: {status}")
        print(f"  Metrics: Block BPE={m.get('3A_block_bpe')}, Inner BPE={m.get('3A_inner_bpe')}, Chars={m.get('3A_inner_chars')}, Words={m.get('3A_inner_words')}, Repo={m.get('3A_inner_repo')}")
        print(f"  Rollup Table: Baseline={m.get('table_baseline_bpe')}, Opt B={m.get('table_opt_b_bpe')}, Opt C={m.get('table_opt_c_bpe')}")
        print(f"  Semantic Blocks: {m.get('num_sb')}, Significance Tags: {m.get('sig_tags_count')}, Links Verified: {m.get('relative_links_verified')}")
        if res["warnings"]:
            for w in res["warnings"]:
                print(f"  [WARN] {w}")
        if res["errors"]:
            for e in res["errors"]:
                print(f"  [ERROR] {e}")
        print()

    print("================================================================================")
    print("SUMMARY AUDIT TABLE:")
    print("================================================================================")
    print(f"{'Rule File':<26} | {'Tag':<16} | {'Block':<5} | {'Inner':<5} | {'Chars':<5} | {'Words':<5} | {'Opt B':<5} | {'Opt C':<5} | {'Err':<3} | {'Status'}")
    print("-" * 105)
    for row in summary_table:
        print(f"{row[0]:<26} | {row[1]:<16} | {row[2]:<5} | {row[3]:<5} | {row[4]:<5} | {row[5]:<5} | {row[6]:<5} | {row[7]:<5} | {row[8]:<3} | {row[10]}")
    print("-" * 105)
    
    total_baseline = sum(r[2] for r in summary_table if isinstance(r[2], int))
    total_opt_b = sum(r[6] for r in summary_table if isinstance(r[6], int))
    total_opt_c = sum(r[7] for r in summary_table if isinstance(r[7], int))
    total_errs = sum(r[8] for r in summary_table)
    savings_b = total_opt_b - total_baseline
    pct_b = (savings_b / total_baseline) * 100 if total_baseline else 0
    print(f"{'TOTAL M2 (Rules 09-15)':<26} | {'7 Rules':<16} | {total_baseline:<5} | {'-':<5} | {'-':<5} | {'-':<5} | {total_opt_b:<5} | {total_opt_c:<5} | {total_errs:<3} | {'APPROVE' if overall_passed else 'REQUEST_CHANGES'}")
    print(f"Net Option B Compression: {savings_b:+d} BPE ({pct_b:+.1f}%) across all 7 rules.")
    print("================================================================================")

    if not overall_passed:
        print("\nOVERALL VERDICT: REQUEST_CHANGES (Errors detected)")
        sys.exit(1)
    else:
        print("\nOVERALL VERDICT: APPROVE (All empirical verification tests passed with 0 errors)")
        sys.exit(0)

if __name__ == "__main__":
    main()
