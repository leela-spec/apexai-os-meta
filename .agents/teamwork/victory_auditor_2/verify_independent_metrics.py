#!/usr/bin/env python3
import sys
from pathlib import Path
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

repo_root = Path("c:/GitDev/apexai-os-meta")
c3a_path = repo_root / "apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/13-candidate-3A-xml.md"
c3b_path = repo_root / "apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/14-candidate-3B-hybrid.md"
bp_path = repo_root / "apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/03-BLUEPRINT-agents.md"
agents_path = repo_root / "AGENTS.md"

def extract_contract_block(path):
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    start = None
    end = None
    for i, line in enumerate(lines):
        if line.strip().startswith('<apex_contract'):
            start = i
        if line.strip().startswith('</apex_contract>'):
            end = i + 1
            break
    if start is None or end is None:
        raise ValueError(f"Could not find <apex_contract> in {path}")
    block = "".join(lines[start:end])
    return block, start + 1, end, len(lines[start:end])

def compute_metrics(text):
    chars = len(text)
    words = len(text.split())
    lines = len(text.splitlines())
    div4 = chars // 4
    w13 = int(words * 1.3)
    bpe = len(enc.encode(text))
    return {
        "chars": chars,
        "words": words,
        "lines": lines,
        "div4": div4,
        "w13": w13,
        "bpe": bpe,
        "bytes": len(text.encode("utf-8"))
    }

print("=== INDEPENDENT RECOMPUTATION OF METRICS ===")

# Candidate 3A block
c3a_block, s3a, e3a, l3a = extract_contract_block(c3a_path)
m_c3a = compute_metrics(c3a_block)
print(f"Candidate 3A Contract Block (Lines {s3a}-{e3a}):")
print(f"  Lines: {m_c3a['lines']} | Chars: {m_c3a['chars']} | Words: {m_c3a['words']} | Repo (chars//4): {m_c3a['div4']} | Repo (words*1.3): {m_c3a['w13']} | BPE: {m_c3a['bpe']}")

# Candidate 3B block
c3b_block, s3b, e3b, l3b = extract_contract_block(c3b_path)
m_c3b = compute_metrics(c3b_block)
print(f"Candidate 3B Contract Block (Lines {s3b}-{e3b}):")
print(f"  Lines: {m_c3b['lines']} | Chars: {m_c3b['chars']} | Words: {m_c3b['words']} | Repo (chars//4): {m_c3b['div4']} | Repo (words*1.3): {m_c3b['w13']} | BPE: {m_c3b['bpe']}")

print(f"Delta (3B - 3A):")
print(f"  Lines: {m_c3b['lines'] - m_c3a['lines']} | Chars: {m_c3b['chars'] - m_c3a['chars']} | Words: {m_c3b['words'] - m_c3a['words']} | Repo (chars//4): {m_c3b['div4'] - m_c3a['div4']} | BPE: {m_c3b['bpe'] - m_c3a['bpe']}")

# Full files
print("\nFull File Metrics:")
for name, p in [("13-candidate-3A-xml.md", c3a_path), ("14-candidate-3B-hybrid.md", c3b_path), ("03-BLUEPRINT-agents.md", bp_path)]:
    txt = p.read_text(encoding="utf-8")
    m = compute_metrics(txt)
    print(f"{name}:")
    print(f"  Bytes: {m['bytes']} | Lines: {m['lines']} | Chars: {m['chars']} | Words: {m['words']} | chars//4: {m['div4']} | words*1.3: {m['w13']} | BPE: {m['bpe']}")

# Root AGENTS.md
txt_agents = agents_path.read_text(encoding="utf-8")
m_agents = compute_metrics(txt_agents)
print("\nLive AGENTS.md:")
print(f"  Lines: {m_agents['lines']} | Chars: {m_agents['chars']} | Words: {m_agents['words']} | chars//4: {m_agents['div4']} | words*1.3: {m_agents['w13']} | BPE: {m_agents['bpe']}")
