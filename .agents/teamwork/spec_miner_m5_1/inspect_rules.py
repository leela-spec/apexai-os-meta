import sys
sys.stdout.reconfigure(encoding="utf-8")
import tiktoken
import re
from pathlib import Path

enc = tiktoken.get_encoding("cl100k_base")
repo_root = Path(r"c:\GitDev\apexai-os-meta")
kb_dir = repo_root / "apex-meta" / "informatics" / "final" / "research" / "06-layered-rule-kb"
cand_13_text = (repo_root / "apex-meta" / "informatics" / "final" / "candidates" / "13-candidate-3A-xml.md").read_text(encoding="utf-8")

# Extract the code block first
m_block = re.search(r"```xml\s*\n(.*?)\n```", cand_13_text, re.DOTALL)
block_3a_text = m_block.group(1)

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
    if cells and cells[0] == "":
        cells.pop(0)
    if cells and cells[-1] == "":
        cells.pop()
    return cells

tags_data = []

for num in range(1, 23):
    fpath = next(kb_dir.glob(f"rule-{num:02d}*.md"), None)
    text = fpath.read_text(encoding="utf-8")
    s3_sec_m = re.search(r"## 3\.\s+Whole-Rule Recomposition Rollup.*?\n(\|.*?)(?:\n##|\Z)", text, re.DOTALL)
    table_text = s3_sec_m.group(1).strip()
    rows = [r.strip() for r in table_text.splitlines() if r.strip().startswith("|") and not r.strip().startswith("|---")]
    
    cols_base = split_markdown_cells(rows[1])
    cols_optb = split_markdown_cells(rows[2])
    
    base_text = re.sub(r"^`|`$", "", cols_base[1]).strip()
    optb_text = re.sub(r"^`|`$", "", cols_optb[1]).strip()
    
    tag_m = re.match(r"^<([a-z_]+)", optb_text)
    tag_name = tag_m.group(1)
    
    # Search INSIDE block_3a_text
    m_3a = re.search(rf"(<{tag_name}(?:\s+[^>]*?)?>.*?</{tag_name}>)", block_3a_text, re.DOTALL)
    text_3a = m_3a.group(1).strip() if m_3a else base_text
    
    bpe_3a = len(enc.encode(text_3a))
    bpe_optb_single = len(enc.encode(optb_text))
    
    if 13 <= num <= 21:
        m = re.match(r"^(<[a-z_]+(?:\s+[^>]*?)?>)(.*?)(</[a-z_]+>)$", optb_text)
        optb_multi = f"{m.group(1)}\n{m.group(2).strip()}\n{m.group(3)}" if m else optb_text
    else:
        optb_multi = optb_text
    bpe_optb_multi = len(enc.encode(optb_multi))
    
    tags_data.append({
        "num": num,
        "tag": tag_name,
        "file": fpath.name,
        "text_3a": text_3a,
        "bpe_3a": bpe_3a,
        "optb_single": optb_text,
        "optb_multi": optb_multi,
        "bpe_optb_single": bpe_optb_single,
        "bpe_optb_multi": bpe_optb_multi,
        "delta": bpe_optb_multi - bpe_3a,
        "pct": (bpe_optb_multi - bpe_3a) / bpe_3a * 100
    })

print(f"{'#':<3} | {'Rule Tag':<17} | {'3A BPE':<8} | {'Ultra BPE':<10} | {'Delta':<8} | {'Savings %':<10}")
print("-" * 65)
for d in tags_data:
    n = d["num"]
    t = f"<{d['tag']}>"
    b3a = d["bpe_3a"]
    b_u = d["bpe_optb_multi"]
    dl = d["delta"]
    pc = d["pct"]
    print(f"{n:<3} | {t:<17} | {b3a:<8} | {b_u:<10} | {dl:<8} | {pc:<10.1f}%")

tot_3a = sum(d["bpe_3a"] for d in tags_data)
tot_u = sum(d["bpe_optb_multi"] for d in tags_data)
tot_dl = tot_u - tot_3a
print("-" * 65)
print(f"Total tag-level BPE: 3A={tot_3a}, Ultra={tot_u}, Delta={tot_dl:+d} ({tot_dl/tot_3a*100:.1f}%)")

print("\n" + "=" * 40 + " VERBATIM OPTION B TAGS " + "=" * 40)
for d in tags_data:
    print(f"<!-- RULE {d['num']:02d}: {d['tag']} -->")
    print(d["optb_multi"])
    print()
