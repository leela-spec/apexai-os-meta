"""
Independent Forensic Verification Script for Milestone 1 Deliverables
Auditor: auditor_m1_1
Target Deliverables:
- apex-meta/informatics/Agent_Setup/index.md
- apex-meta/informatics/file-architecture.md
- apex-meta/informatics/writing-profile.md
- apex-meta/informatics/execution-modes.md
"""

import sys
import re
from pathlib import Path

REPO_ROOT = Path("c:/GitDev/apexai-os-meta")
INFORMATICS_DIR = REPO_ROOT / "apex-meta" / "informatics"

# Files to audit
M1_FILES = [
    INFORMATICS_DIR / "Agent_Setup" / "index.md",
    INFORMATICS_DIR / "file-architecture.md",
    INFORMATICS_DIR / "writing-profile.md",
    INFORMATICS_DIR / "execution-modes.md",
]

def check_file_existence():
    results = []
    for f in M1_FILES:
        exists = f.exists()
        size = f.stat().st_size if exists else 0
        results.append((str(f.relative_to(REPO_ROOT)), exists, size))
    return results

def detect_hardcoded_test_strings():
    """Detect hardcoded test results, expected output strings, or fake test artifacts."""
    suspicious_patterns = [
        r"Ran 14[0-9] tests",
        r"100% SPEC CONFORMANCE",
        r"OK \(skipped=",
        r"0 OKF Errors",
        r"0 APEX_PROFILE Errors",
        r"0 Advisories",
        r"Total Tests Executed",
        r"Final Verdict:\s*PASSED",
    ]
    findings = []
    for f in M1_FILES:
        content = f.read_text(encoding="utf-8")
        for pat in suspicious_patterns:
            matches = re.findall(pat, content, re.IGNORECASE)
            if matches:
                findings.append((str(f.relative_to(REPO_ROOT)), pat, matches))
    return findings

def detect_facade_implementations():
    """Detect placeholder text, TODOs, stub methods, or ungrounded templates."""
    facade_patterns = [
        r"\bTODO\b",
        r"\bTBD\b",
        r"\bFIXME\b",
        r"\bLorem ipsum\b",
        r"placeholder",
        r"implement later",
        r"not yet implemented",
    ]
    findings = []
    for f in M1_FILES:
        content = f.read_text(encoding="utf-8")
        for pat in facade_patterns:
            matches = re.findall(pat, content, re.IGNORECASE)
            if matches:
                findings.append((str(f.relative_to(REPO_ROOT)), pat, matches))
    return findings

def audit_significance_tags():
    """
    Examine all significance tags:
    - Syntax: [P<0-3> | I<1-100>/E<1-100>/R<1-100>]
    - Check for formula leakage (EV=, arithmetic, score suffix)
    - Check for descending sort order
    - Check token position of first P0 (top-loaded primacy <= 500 tokens)
    """
    tag_regex = re.compile(r"\[(P[0-3])\s*\|\s*I([0-9]+)/E([0-9]+)/R([0-9]+)\]")
    any_tag_regex = re.compile(r"\[(P[0-9]+)[^\]]*\]")
    
    tier_order = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
    
    results = {}
    
    for f in [INFORMATICS_DIR / "file-architecture.md", INFORMATICS_DIR / "writing-profile.md", INFORMATICS_DIR / "execution-modes.md"]:
        content = f.read_text(encoding="utf-8")
        raw_tags = any_tag_regex.findall(content)
        parsed_tags = []
        formula_violations = []
        
        # Check for formula tokens inside or near tag
        formula_pattern = re.compile(r"\[P[0-9]+[^\]]*(?:EV\s*=|[:=]\s*\d+|\+|\*|(?<!/)/(?!E|R)\d+)[^\]]*\]")
        for m in formula_pattern.finditer(content):
            formula_violations.append(m.group(0))
            
        for match in tag_regex.finditer(content):
            tier, i_val, e_val, r_val = match.groups()
            parsed_tags.append({
                "tag": match.group(0),
                "tier": tier,
                "impact": int(i_val),
                "evidence": int(e_val),
                "risk": int(r_val),
                "pos": match.start()
            })
            
        # Check token estimate of first P0
        first_p0_token = None
        for pt in parsed_tags:
            if pt["tier"] == "P0":
                prefix = content[:pt["pos"]]
                # Approximate token count (words * 1.3 or whitespace splits)
                token_count = len(re.findall(r"\w+|[^\w\s]", prefix))
                first_p0_token = token_count
                break
                
        # Check sorting order
        order_violations = []
        for i in range(len(parsed_tags) - 1):
            curr_tier = tier_order[parsed_tags[i]["tier"]]
            next_tier = tier_order[parsed_tags[i+1]["tier"]]
            if curr_tier > next_tier:
                order_violations.append((parsed_tags[i]["tag"], parsed_tags[i+1]["tag"]))
                
        results[str(f.relative_to(REPO_ROOT))] = {
            "total_raw_tags": len(raw_tags),
            "total_valid_tags": len(parsed_tags),
            "formula_violations": formula_violations,
            "order_violations": order_violations,
            "first_p0_token": first_p0_token,
            "tags": parsed_tags
        }
        
    return results

def check_prepopulated_artifacts():
    """Check if any test logs, results, or attestation files exist in apex-meta/informatics/"""
    results = []
    for p in INFORMATICS_DIR.glob("**/*"):
        if p.is_file():
            if p.suffix in [".log", ".result", ".output"] or "test_result" in p.name.lower():
                results.append(str(p.relative_to(REPO_ROOT)))
    return results

if __name__ == "__main__":
    print("=== FORENSIC INTEGRITY AUDIT CHECKS ===")
    
    print("\n1. File Existence & Sizing:")
    for path, exists, size in check_file_existence():
        print(f"  - {path}: {'EXISTS' if exists else 'MISSING'} ({size} bytes)")
        
    print("\n2. Hardcoded Test String Detection:")
    hardcoded = detect_hardcoded_test_strings()
    if hardcoded:
        print(f"  FAILED: Detected {len(hardcoded)} suspicious strings:")
        for path, pat, matches in hardcoded:
            print(f"    {path}: pattern '{pat}' matched: {matches}")
    else:
        print("  CLEAN: 0 hardcoded test output strings found.")
        
    print("\n3. Facade / Placeholder Detection:")
    facades = detect_facade_implementations()
    if facades:
        print(f"  FAILED: Detected {len(facades)} placeholder occurrences:")
        for path, pat, matches in facades:
            print(f"    {path}: pattern '{pat}' matched: {matches}")
    else:
        print("  CLEAN: 0 placeholder / facade markers found.")
        
    print("\n4. Pre-Populated Artifact Detection:")
    artifacts = check_prepopulated_artifacts()
    if artifacts:
        print(f"  FLAGGED: Found pre-populated artifacts: {artifacts}")
    else:
        print("  CLEAN: 0 pre-populated log or result artifacts found.")
        
    print("\n5. Significance Tag & Formula Analysis:")
    sig_audit = audit_significance_tags()
    for fpath, data in sig_audit.items():
        print(f"  File: {fpath}")
        print(f"    Valid Significance Tags: {data['total_valid_tags']} / {data['total_raw_tags']}")
        print(f"    Formula Violations: {len(data['formula_violations'])} {data['formula_violations']}")
        print(f"    Priority Inversions: {len(data['order_violations'])} {data['order_violations']}")
        print(f"    First P0 Token Position: {data['first_p0_token']} (Target: <= 500)")


def dump_detailed_tag_analysis():
    files = [
        INFORMATICS_DIR / "writing-profile.md",
        INFORMATICS_DIR / "file-architecture.md",
        INFORMATICS_DIR / "execution-modes.md"
    ]
    report = []
    report.append("\n=== DETAILED SIGNIFICANCE TAG AUDIT ===")
    for f in files:
        report.append(f"\n--- {f.name} ---")
        lines = f.read_text(encoding="utf-8").splitlines()
        for i, line in enumerate(lines, 1):
            m = re.search(r"(\[P[0-3]\s*\|\s*I(\d+)/E(\d+)/R(\d+)\])", line)
            if m:
                tag, i_v, e_v, r_v = m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4))
                # Check bounds
                valid_bounds = (1 <= i_v <= 100) and (1 <= e_v <= 100) and (1 <= r_v <= 100)
                report.append(f"Line {i:3d}: {tag} (I={i_v}, E={e_v}, R={r_v}, valid_bounds={valid_bounds})")
    return "\n".join(report)

if __name__ == "__main__":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    print(dump_detailed_tag_analysis())
