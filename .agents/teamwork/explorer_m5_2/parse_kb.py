import os
import re
import sys
from pathlib import Path
import tiktoken

REPO_ROOT = Path(".").resolve()
KB_DIR = REPO_ROOT / "apex-meta" / "informatics" / "final" / "research" / "06-layered-rule-kb"
OUT_FILE = REPO_ROOT / ".agents" / "teamwork" / "explorer_m5_2" / "rule_inventory_clean.txt"

enc = tiktoken.get_encoding("cl100k_base")

rule_files = sorted([f for f in KB_DIR.iterdir() if f.name.startswith("rule-") and f.suffix == ".md"])
audit_files = sorted([f for f in KB_DIR.iterdir() if f.name.startswith("audit-") and f.suffix == ".md"])

rules_data = []

for rf in rule_files:
    content = rf.read_text(encoding="utf-8")
    
    # Extract tag
    tag_m = re.search(r"title:\s*Rule\s+\d+\s+Deep-Dive\s*[—–-]\s*<([^>]+)>", content)
    tag = tag_m.group(1) if tag_m else "unknown"
    
    # Extract ID
    id_m = re.search(r"id:\s*([^\n\r]+)", content)
    doc_id = id_m.group(1).strip() if id_m else ""
    
    # Extract title
    title_m = re.search(r"title:\s*([^\n\r]+)", content)
    title = title_m.group(1).strip() if title_m else ""
    
    # Extract Chapter 3 Whole-Rule Recomposition Rollup
    ch3_pos = content.find("## 3.")
    ch4_pos = content.find("## 4.", ch3_pos) if ch3_pos != -1 else -1
    ch3_text = content[ch3_pos:ch4_pos] if (ch3_pos != -1 and ch4_pos != -1) else ""
    
    base_bpe, opt_b_bpe, opt_c_bpe = 0, 0, 0
    opt_b_savings = ""
    opt_c_savings = ""
    opt_b_text = ""
    
    for line in ch3_text.splitlines():
        if not line.strip().startswith("|"):
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) >= 5:
            lbl = parts[1]
            txt = parts[2]
            bpe_col = parts[3]
            sav_col = parts[4]
            
            # parse bpe number: find first digits in bpe_col
            bpe_digits = re.search(r"\b(\d+)\b", bpe_col)
            bpe_val = int(bpe_digits.group(1)) if bpe_digits else 0
            
            if any(k in lbl for k in ["1.", "Baseline", "Current"]):
                base_bpe = bpe_val
            elif any(k in lbl for k in ["2.", "Option B", "Surgical", "Recommended"]):
                opt_b_bpe = bpe_val
                opt_b_savings = sav_col.replace("`", "").replace("*", "").strip()
                opt_b_text = txt
            elif any(k in lbl for k in ["3.", "Option C", "Aggressive", "Alternative"]):
                opt_c_bpe = bpe_val
                opt_c_savings = sav_col.replace("`", "").replace("*", "").strip()

    # If base_bpe is still 0 (like in rule-01), extract from section 1.1 or specific line
    if base_bpe == 0:
        base_match = re.search(r"(\d+)\s+BPE", content[:2000])
        if base_match:
            base_bpe = int(base_match.group(1))
    if opt_b_bpe == 0 and "rule-01" in rf.name:
        base_bpe = 56
        opt_b_bpe = 40
        opt_b_savings = "-16 BPE (-28.6%)"
        opt_c_bpe = 36

    # Extract Plane 4 owners
    plane4_m = re.findall(r"\b(WP-\d{2}|FA-\d{2}|EM-\d{2}|AD-\d{2}|GS-\d{2})\b", content)
    plane4_owners = sorted(list(set(plane4_m)))
    
    # Extract Research Packets
    rp_m = re.findall(r"\b(RP-\d{2})\b", content)
    research_packets = sorted(list(set(rp_m)))

    rules_data.append({
        "num": rf.name.split("-")[1],
        "file": rf.name,
        "id": doc_id,
        "tag": tag,
        "title": title,
        "base_bpe": base_bpe,
        "opt_b_bpe": opt_b_bpe,
        "opt_c_bpe": opt_c_bpe,
        "opt_b_savings": opt_b_savings,
        "opt_c_savings": opt_c_savings,
        "plane4_owners": plane4_owners,
        "research_packets": research_packets
    })

out_lines = []
out_lines.append("| Rule | File | Tag | Baseline (BPE) | Option B (BPE) | Savings vs 3A | Option C (BPE) | Canonical Owner | Research |")
out_lines.append("|---|---|---|---:|---:|---|---:|---|---|")

total_base = 0
total_b = 0
total_c = 0

for r in rules_data:
    total_base += r["base_bpe"]
    total_b += r["opt_b_bpe"]
    total_c += r["opt_c_bpe"]
    owners = ", ".join(r["plane4_owners"][:3]) if r["plane4_owners"] else "-"
    rps = ", ".join(r["research_packets"]) if r["research_packets"] else "-"
    out_lines.append(f"| {r['num']} | [{r['file']}]({r['file']}) | `<{r['tag']}>` | {r['base_bpe']} | {r['opt_b_bpe']} | {r['opt_b_savings']} | {r['opt_c_bpe']} | {owners} | {rps} |")

savings_pct = ((total_base - total_b) / total_base * 100) if total_base else 0
out_lines.append(f"| **Total** | **22 Rules** | **All 22 Tags** | **{total_base}** | **{total_b}** | **-{total_base - total_b} BPE (-{savings_pct:.1f}%)** | **{total_c}** | | |")

OUT_FILE.write_text("\n".join(out_lines), encoding="utf-8")
print(f"Total Base: {total_base}, Total B: {total_b}, Total C: {total_c}")
