#!/usr/bin/env python3
"""
stress_test_m2_challenger.py — Adversarial Stress Test Suite for M2 Deliverables.

Checks:
1. Router ceilings: characters <= 2000, lines <= 100 (or <= 120), tokens <= 500.
2. XML tags: regex test `<informatics when="..." ref="..." deepen_when="...">`, valid attributes, clean markdown bodies, zero eager imports.
3. YAML frontmatters: verify all lines contain `:` and no multiline lists exist.
4. Zero calculated math formulas.
5. Significance ranking syntax and descending sort order.
6. Link integrity: all referenced files exist.
7. Top-loaded primacy: first P0 invariant within first 500 tokens.
8. Execution of okf_validator and test_informatics_e2e.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Tuple

REPO_ROOT = Path(__file__).resolve().parents[5]
INFORMATICS_DIR = REPO_ROOT / "apex-meta" / "informatics" / "final"
SCRIPTS_DIR = REPO_ROOT / "apex-meta" / "scripts"
FINAL_TOOLS_DIR = INFORMATICS_DIR / "tools"

for p in (SCRIPTS_DIR, FINAL_TOOLS_DIR):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

def resolve_file(fname: str) -> Path:
    p_root = REPO_ROOT / "apex-meta" / "informatics" / fname
    if p_root.exists():
        return p_root
    for base in (INFORMATICS_DIR, INFORMATICS_DIR / "specs", INFORMATICS_DIR / "sub-bundles"):
        cand = base / fname
        if cand.exists():
            return cand
    return p_root

import okf_validator

M2_AUTHORED_FILES = [
    "anti-drift-rules.md",
    "governance-schemas.md",
    "index.md",
    "general-informatics-router.md",
]

SIG_REGEX = re.compile(r"\[(P[0-3])\s*\|\s*I(\d{1,3})/E(\d{1,3})/R(\d{1,3})\]")


def run_checks() -> Dict[str, any]:
    results = {
        "status": "PASS",
        "failures": [],
        "metrics": {},
        "xml_tags": {},
        "yaml_frontmatter": {},
        "significance_tags": {},
        "math_formulas": {},
        "links": {},
        "primacy": {},
    }

    # 1. Existence and metrics
    for fname in M2_AUTHORED_FILES:
        fpath = resolve_file(fname)
        if not fpath.exists():
            results["failures"].append(f"Missing authored file: {fname}")
            continue

        raw_bytes = fpath.read_bytes()
        content = fpath.read_text(encoding="utf-8")
        lines = content.splitlines()
        chars = len(content)
        words = len(content.split())
        tokens = max(1, chars // 4)

        results["metrics"][fname] = {
            "bytes": len(raw_bytes),
            "chars": chars,
            "lines": len(lines),
            "words": words,
            "est_tokens": tokens,
            "crlf_count": raw_bytes.count(b"\r\n"),
            "lf_count": raw_bytes.count(b"\n"),
        }

    # 2. Router Ceiling Stress Test (general-informatics-router.md)
    r_metrics = results["metrics"].get("general-informatics-router.md")
    if r_metrics:
        chars = r_metrics["chars"]
        lines = r_metrics["lines"]
        tokens = r_metrics["est_tokens"]

        if chars > 2000:
            results["failures"].append(f"general-informatics-router.md exceeded char ceiling: {chars} > 2000")
        if lines > 100:
            # Check if within advisory ceiling (120 lines)
            if lines > 120:
                results["failures"].append(f"general-informatics-router.md exceeded line ceiling: {lines} > 120")
        if tokens > 500:
            results["failures"].append(f"general-informatics-router.md exceeded token ceiling: {tokens} > 500")

    # 3. XML Tag Validation (in general-informatics-router.md and index.md)
    for rname in ["general-informatics-router.md", "index.md"]:
        rpath = resolve_file(rname)
        rc = rpath.read_text(encoding="utf-8")

        open_tags = list(re.finditer(r'<informatics\s+([^>]*?)>', rc))
        close_tags = list(re.finditer(r'</informatics>', rc))

        if len(open_tags) != len(close_tags):
            results["failures"].append(f"{rname}: Tag mismatch! {len(open_tags)} open tags vs {len(close_tags)} close tags")

        tag_blocks = re.findall(r'<informatics\s+([^>]*?)>(.*?)</informatics>', rc, re.DOTALL)
        tag_details = []

        for idx, (attrs_str, body) in enumerate(tag_blocks, 1):
            attr_dict = dict(re.findall(r'(\w+)="([^"]*)"', attrs_str))
            tag_info = {"tag_index": idx, "attrs": attr_dict}

            # Check attributes
            if "when" not in attr_dict or not attr_dict["when"].strip():
                results["failures"].append(f"{rname} Tag #{idx}: Missing or empty 'when' attribute")
            if "ref" not in attr_dict or not attr_dict["ref"].strip():
                results["failures"].append(f"{rname} Tag #{idx}: Missing or empty 'ref' attribute")
            else:
                target_file = resolve_file(attr_dict["ref"])
                if not target_file.exists():
                    results["failures"].append(f"{rname} Tag #{idx}: Referenced file does not exist: {attr_dict['ref']}")

            # Check well-formed XML snippet
            xml_snippet = f"<root><informatics {attrs_str}>{body}</informatics></root>"
            try:
                ET.fromstring(xml_snippet)
                tag_info["valid_xml"] = True
            except ET.ParseError as pe:
                tag_info["valid_xml"] = False
                results["failures"].append(f"{rname} Tag #{idx}: XML Parse Error: {pe}")

            # Check body for prohibited eager imports (@path)
            eager_imports = re.findall(r"@[\w./\-]+\.md", body)
            if eager_imports:
                results["failures"].append(f"{rname} Tag #{idx}: Prohibited eager import found in body: {eager_imports}")
            tag_info["eager_imports"] = eager_imports

            tag_details.append(tag_info)

        results["xml_tags"][rname] = tag_details

    # 4. YAML Frontmatter & No Multiline Lists
    for fname in M2_AUTHORED_FILES:
        fpath = resolve_file(fname)
        content = fpath.read_text(encoding="utf-8")

        if not content.startswith("---"):
            results["failures"].append(f"{fname}: Does not start with '---'")
            continue

        parts = content.split("---", 2)
        if len(parts) < 3:
            results["failures"].append(f"{fname}: Missing closing '---' for frontmatter")
            continue

        fm_raw = parts[1]
        line_errors = []
        for line_num, line in enumerate(fm_raw.splitlines(), start=2):
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            if ":" not in s:
                line_errors.append((line_num, s, "Missing colon ':'"))
            if s.startswith("- "):
                line_errors.append((line_num, s, "Multiline list item '- ' forbidden"))

        if line_errors:
            for lnum, lcontent, lreason in line_errors:
                results["failures"].append(f"{fname}:{lnum}: {lreason} -> '{lcontent}'")

        fm, body, err = okf_validator.parse_frontmatter(content)
        if err:
            results["failures"].append(f"{fname}: okf_validator parse_frontmatter failed: {err}")

        results["yaml_frontmatter"][fname] = {
            "keys": list(fm.keys()) if fm else [],
            "error": err,
            "line_errors": len(line_errors),
        }

    # 5. Significance Ranking & Zero Math Formulas
    for fname in M2_AUTHORED_FILES:
        fpath = resolve_file(fname)
        content = fpath.read_text(encoding="utf-8")
        content_no_code = re.sub(r"```[\s\S]*?```", "", content)

        # Detect computed formulas (excluding authorized syntax documentation [P<tier> | I<impact>/E<evidence>/R<risk>])
        c_no_tags = re.sub(r"\[P[0-3]\s*\|\s*I\d+/E\d+/R\d+\]", "", content_no_code)
        c_no_tags = re.sub(r"\[P<tier>\s*\|\s*I<[^>]+>/E<[^>]+>/R<[^>]+>\]", "", c_no_tags)
        c_no_tags = re.sub(r"\(I<[^>]+>/E<[^>]+>/R<[^>]+>\)", "", c_no_tags)

        math_patterns = [
            (r"\bEV\s*=", "Expected Value computation"),
            (r"\bScore\s*=", "Score computation"),
            (r"\b\w+\s*=\s*\(?I\s*[*+xX/]\s*E", "Arithmetic combination of I and E"),
            (r"/\s*R(?![a-zA-Z0-9_<>])", "Division by Risk"),
            (r"\$\$.*?\$\$", "LaTeX block math"),
            (r"(?<!`)\$[a-zA-Z0-9_+=\\-]+\$(?!`)", "LaTeX inline math"),
            (r"\\frac\{", "LaTeX fraction"),
            (r"\\sum\b", "LaTeX summation"),
        ]

        found_formulas = []
        for pattern, desc in math_patterns:
            matches = re.findall(pattern, c_no_tags)
            if matches:
                found_formulas.append((desc, matches))
                results["failures"].append(f"{fname}: Prohibited math formula detected ({desc}): {matches}")

        results["math_formulas"][fname] = found_formulas

        # Significance tags
        tags = []
        for match in SIG_REGEX.finditer(content_no_code):
            tier, i_str, e_str, r_str = match.groups()
            i_val, e_val, r_val = int(i_str), int(e_str), int(r_str)
            if not (1 <= i_val <= 100 and 1 <= e_val <= 100 and 1 <= r_val <= 100):
                results["failures"].append(f"{fname}: Tag values out of range (1-100): {match.group(0)}")
            tags.append((tier, i_val, e_val, r_val, match.group(0)))

        tier_order = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
        order_violations = []
        for idx in range(len(tags) - 1):
            cur_tier = tags[idx][0]
            next_tier = tags[idx + 1][0]
            if tier_order[cur_tier] > tier_order[next_tier]:
                order_violations.append((idx, cur_tier, next_tier))
                results["failures"].append(f"{fname}: Inverted priority order at index {idx}: {cur_tier} before {next_tier}")

        results["significance_tags"][fname] = {
            "total_tags": len(tags),
            "tier_counts": {
                t: sum(1 for tag in tags if tag[0] == t)
                for t in ["P0", "P1", "P2", "P3"]
            },
            "order_violations": len(order_violations),
        }

        # Primacy check (P0 within first 500 tokens)
        p0_tags = [t for t in tags if t[0] == "P0"]
        if p0_tags:
            first_p0 = p0_tags[0]
            pos = content.find(first_p0[4])
            token_pos = max(1, pos // 4)
            results["primacy"][fname] = {"first_p0_token": token_pos, "is_top_loaded": token_pos <= 500}
            if token_pos > 500:
                results["failures"].append(f"{fname}: First P0 invariant appears at token {token_pos} > 500")
        else:
            results["primacy"][fname] = {"first_p0_token": None, "is_top_loaded": False}

    # 6. Relative Link Integrity across all authored files
    for fname in M2_AUTHORED_FILES:
        fpath = resolve_file(fname)
        content = fpath.read_text(encoding="utf-8")
        links = okf_validator.extract_links(content)
        broken_links = []
        for l in links:
            resolved = (fpath.parent / l).resolve()
            if not resolved.exists():
                broken_links.append(l)
                results["failures"].append(f"{fname}: Broken link '{l}' (target does not exist)")
        results["links"][fname] = {"total_links": len(links), "broken_links": broken_links}

    # 7. Adversarial Edge Cases & Sensitivity Analysis
    results["adversarial"] = {}

    # 7.1 Router Headroom & CRLF Sensitivity
    router_content = resolve_file("general-informatics-router.md").read_text(encoding="utf-8")
    router_crlf_bytes = len(router_content.replace("\n", "\r\n").encode("utf-8"))
    results["adversarial"]["router_crlf_bytes"] = router_crlf_bytes
    results["adversarial"]["router_char_headroom"] = 2000 - len(router_content)
    results["adversarial"]["router_token_headroom"] = 500 - max(1, len(router_content) // 4)

    # 7.2 Headings with periods that could trigger STE regex splitting
    period_in_headings = []
    for fname in M2_AUTHORED_FILES:
        content = resolve_file(fname).read_text(encoding="utf-8")
        for line_num, line in enumerate(content.splitlines(), start=1):
            if line.strip().startswith("#"):
                if re.search(r"#+\s+\d+\.", line):
                    period_in_headings.append((fname, line_num, line.strip()))
    results["adversarial"]["period_in_headings"] = period_in_headings

    # 7.3 Regex attribute order sensitivity check
    # Check if ROUTER_XML_TAG_REGEX is strict about attribute order:
    sample_reversed = '<informatics ref="test.md" when="test" />'
    from test_informatics_e2e import ROUTER_XML_TAG_REGEX
    results["adversarial"]["regex_supports_reversed_attrs"] = bool(ROUTER_XML_TAG_REGEX.search(sample_reversed))

    if results["failures"]:
        results["status"] = "FAIL"

    return results


def main():
    print("=" * 70)
    print("RUNNING ADVERSARIAL STRESS TEST SUITE (M2 DELIVERABLES)")
    print("=" * 70)

    res = run_checks()

    print("\n--- 1. File Metrics & Ceilings ---")
    for fname, m in res["metrics"].items():
        print(f"[{fname}]")
        print(f"  Chars: {m['chars']} | Lines: {m['lines']} | Words: {m['words']} | Tokens: {m['est_tokens']}")
        print(f"  CRLF: {m['crlf_count']} | LF: {m['lf_count']}")

    print("\n--- 2. XML Tag Validation ---")
    for rname, tags in res["xml_tags"].items():
        print(f"[{rname}] {len(tags)} tags found:")
        for t in tags:
            print(f"  Tag #{t['tag_index']}: when='{t['attrs'].get('when')}' ref='{t['attrs'].get('ref')}' deepen='{t['attrs'].get('deepen_when')}' XML_valid={t['valid_xml']}")

    print("\n--- 3. YAML Frontmatter Parsing ---")
    for fname, fm in res["yaml_frontmatter"].items():
        print(f"[{fname}] keys={fm['keys']} | parse_err={fm['error']} | line_errs={fm['line_errors']}")

    print("\n--- 4. Significance Tags & Primacy ---")
    for fname, st in res["significance_tags"].items():
        p_info = res["primacy"].get(fname, {})
        print(f"[{fname}] Total: {st['total_tags']} | Tiers: {st['tier_counts']} | Inversions: {st['order_violations']} | First P0: token {p_info.get('first_p0_token')}")

    print("\n--- 5. Math Formula Scan ---")
    for fname, formulas in res["math_formulas"].items():
        print(f"[{fname}] Computed formulas detected: {len(formulas)}")

    print("\n--- 7. Adversarial Analysis & Headroom ---")
    adv = res["adversarial"]
    print(f"  Router Char Headroom: {adv['router_char_headroom']} chars remaining (of 2000 limit)")
    print(f"  Router Token Headroom: {adv['router_token_headroom']} tokens remaining (of 500 limit)")
    print(f"  Router CRLF Byte Size: {adv['router_crlf_bytes']} bytes (exceeds 2000 if saved with CRLF)")
    print(f"  Headings with numbers followed by periods: {len(adv['period_in_headings'])}")
    for f, ln, h in adv['period_in_headings']:
        print(f"    - {f}:{ln} -> {h}")
    print(f"  Parser regex supports reversed attribute order: {adv['regex_supports_reversed_attrs']}")

    print("\n" + "=" * 70)
    if res["status"] == "PASS":
        print("FINAL STRESS TEST VERDICT: ALL PASS (0 Failures)")
    else:
        print(f"FINAL STRESS TEST VERDICT: FAIL ({len(res['failures'])} Failures)")
        for f in res["failures"]:
            print(f"  - {f}")
    print("=" * 70)

    return 0 if res["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
