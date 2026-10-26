import os
import re
import sys
import tiktoken

ENC = tiktoken.get_encoding("cl100k_base")

FILES = [
    "rule-02-product-first.md",
    "rule-03-scope.md",
    "rule-04-communication.md",
    "rule-05-hold-position.md",
    "rule-06-ground.md",
    "rule-07-reuse.md",
    "rule-08-context.md"
]

KB_DIR = r"c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb"

SUSPICIOUS_PATTERNS = [
    r"\bTODO\b",
    r"\bTBD\b",
    r"\bFIXME\b",
    r"\bplaceholder\b",
    r"lorem ipsum",
    r"\[insert\b",
    r"as above",
    r"\.\.\.",
    r"to be added"
]

MATH_FORMULA_PATTERNS = [
    r"=\s*\(?\s*I\s*[\*\+\-\/]\s*E",
    r"score\s*=\s*",
    r"I\d+\s*[\*\+]\s*E\d+",
    r"formula",
    r"calculated score"
]

TAG_REGEX = re.compile(r"\[P[0-3]\s*\|\s*I\d+/E\d+/R\d+\]")

def run_audit():
    print("=== STARTING FORENSIC INTEGRITY AUDIT FOR MILESTONE 1 (RULES 02-08) ===")
    overall_pass = True
    
    file_stats = {}
    
    for fname in FILES:
        fpath = os.path.join(KB_DIR, fname)
        if not os.path.exists(fpath):
            print(f"[FAIL] Missing file: {fname}")
            overall_pass = False
            continue
            
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Metrics
        bpe_tokens = len(ENC.encode(content))
        char_count = len(content)
        word_count = len(content.split())
        line_count = len(content.splitlines())
        
        file_stats[fname] = {
            "bpe": bpe_tokens,
            "chars": char_count,
            "words": word_count,
            "lines": line_count
        }
        
        # 1. Depth check (~2500 - 3500 BPE tokens)
        depth_ok = (2400 <= bpe_tokens <= 3600)
        if not depth_ok:
            print(f"[WARN/FAIL] Depth out of nominal range: {fname} has {bpe_tokens} BPE tokens")
            if bpe_tokens < 1500:
                overall_pass = False
                print(f"[FAIL] Severe stub detection: {fname} is under 1500 BPE tokens!")
        else:
            print(f"[PASS] Depth OK: {fname} -> {bpe_tokens} BPE tokens, {word_count} words, {char_count} chars, {line_count} lines")
            
        # 2. Section Checks
        required_sections = [
            (r"^## 1\.", "Section 1 (Original Rule & Semantic Block List)"),
            (r"^## 2\.", "Section 2 (Chapter-by-Chapter Semantic Block Analysis)"),
            (r"^## 3\.", "Section 3 (Whole-Rule Recomposition Rollup)"),
            (r"^## 4\.", "Section 4 (Complete Bidirectional Research & Provenance Links)"),
            (r"^## 5\.", "Section 5 (Failure Modes & Not-To-Dos)")
        ]
        
        for sec_pattern, sec_name in required_sections:
            if not re.search(sec_pattern, content, re.MULTILINE):
                print(f"[FAIL] {fname} missing {sec_name}")
                overall_pass = False
            else:
                pass
                
        # 3. Frontmatter checks
        if not content.startswith("---"):
            print(f"[FAIL] {fname} missing frontmatter delimiter")
            overall_pass = False
        else:
            fm_match = re.search(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
            if not fm_match:
                print(f"[FAIL] {fname} invalid frontmatter structure")
                overall_pass = False
            else:
                fm_text = fm_match.group(1)
                for field in ["type:", "id:", "title:", "description:", "status:", "tags:"]:
                    if field not in fm_text:
                        print(f"[FAIL] {fname} missing frontmatter field: {field}")
                        overall_pass = False
                        
        # 4. Semantic block analysis checks
        # Must have Options A, B, C
        opt_a_count = len(re.findall(r"\bOption A\b", content))
        opt_b_count = len(re.findall(r"\bOption B\b", content))
        opt_c_count = len(re.findall(r"\bOption C\b", content))
        
        if opt_a_count == 0 or opt_b_count == 0 or opt_c_count == 0:
            print(f"[FAIL] {fname} missing formulation options (A: {opt_a_count}, B: {opt_b_count}, C: {opt_c_count})")
            overall_pass = False
        else:
            print(f"[PASS] Options present in {fname}: A={opt_a_count}, B={opt_b_count}, C={opt_c_count}")
            
        # 5. Significance tags [P0-P3 | I/E/R]
        tags = TAG_REGEX.findall(content)
        if len(tags) == 0:
            print(f"[FAIL] {fname} has 0 [P|I/E/R] significance tags!")
            overall_pass = False
        else:
            print(f"[PASS] {fname} has {len(tags)} valid [P|I/E/R] significance tags.")
            
        # Check for formula calculation in tags or text
        for mp in MATH_FORMULA_PATTERNS:
            formula_matches = re.findall(mp, content, re.IGNORECASE)
            if formula_matches:
                print(f"[FAIL] {fname} contains mathematical formula pattern '{mp}': {formula_matches}")
                overall_pass = False
                
        # 6. Suspicious / placeholder patterns
        for pat in SUSPICIOUS_PATTERNS:
            matches = re.findall(pat, content, re.IGNORECASE)
            # Filter legitimate occurrences if any (e.g., in a code block or explaining 'do not leave TODOs')
            if matches:
                # print context
                for m in re.finditer(pat, content, re.IGNORECASE):
                    start = max(0, m.start() - 30)
                    end = min(len(content), m.end() + 30)
                    snippet = content[start:end].replace('\n', ' ')
                    # Check if it's discussing failure modes or literally a placeholder
                    if "todo" in pat.lower() and "WP-25" in snippet or "never" in snippet.lower() or "not" in snippet.lower() or "audit" in snippet.lower():
                        continue # descriptive mention of avoiding TODOs
                    if pat == r"\.\.\." and ("`" in snippet or "(" in snippet or ".." in snippet):
                        continue # legitimate range notation or citation
                    print(f"[WARN/SUSPICION] {fname} matched pattern '{pat}': ...{snippet}...")
                    
        # 7. Check relative links
        links = re.findall(r"\[.*?\]\((.*?)\)", content)
        broken_links = []
        for l in links:
            if l.startswith("http") or l.startswith("#"):
                continue
            # target path relative to fpath
            resolved = os.path.normpath(os.path.join(os.path.dirname(fpath), l))
            if not os.path.exists(resolved):
                broken_links.append((l, resolved))
                
        if broken_links:
            print(f"[WARN] {fname} has broken relative links: {broken_links}")
            # Note: evaluate whether broken links violate integrity or are known caveats
        else:
            print(f"[PASS] All relative file links exist for {fname} ({len(links)} links checked)")
            
    print("\n=== SUMMARY METRICS ===")
    for fname, stats in file_stats.items():
        print(f"{fname:26} | Lines: {stats['lines']:4} | Words: {stats['words']:4} | Chars: {stats['chars']:5} | BPE: {stats['bpe']:4}")
        
    print(f"\nFinal Verdict: {'CLEAN' if overall_pass else 'INTEGRITY VIOLATION'}")

if __name__ == "__main__":
    run_audit()
