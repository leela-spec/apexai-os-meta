import tiktoken
from pathlib import Path

enc = tiktoken.get_encoding("cl100k_base")

V2_DIR = Path(r"c:\GitDev\apexai-os-meta\apex-meta\informatics\Agent_Setup\NextIteration\v2-always-on-architecture")

def analyze_full_file(path: Path):
    raw_bytes = path.read_bytes()
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    chars = len(text)
    words = len(text.split())
    repo_tokens_chars = chars // 4
    repo_tokens_words = int(words * 1.3)
    bpe_tokens = len(enc.encode(text))
    return {
        "bytes": len(raw_bytes),
        "lines": len(lines),
        "chars": chars,
        "words": words,
        "repo_div4": repo_tokens_chars,
        "repo_w13": repo_tokens_words,
        "bpe": bpe_tokens
    }

print("=== FULL FILE METRICS ===")
for fname in ["13-candidate-3A-xml.md", "14-candidate-3B-hybrid.md", "03-BLUEPRINT-agents.md"]:
    m = analyze_full_file(V2_DIR / fname)
    print(fname, m)

def extract_block(path: Path, start_tag: str, end_tag: str):
    text = path.read_text(encoding="utf-8")
    start_idx = text.find(start_tag)
    end_idx = text.find(end_tag) + len(end_tag)
    block = text[start_idx:end_idx]
    lines = block.splitlines()
    chars = len(block)
    words = len(block.split())
    repo_tokens_chars = chars // 4
    repo_tokens_words = int(words * 1.3)
    bpe_tokens = len(enc.encode(block))
    return {
        "lines": len(lines),
        "chars": chars,
        "words": words,
        "repo_div4": repo_tokens_chars,
        "repo_w13": repo_tokens_words,
        "bpe": bpe_tokens
    }

print("\n=== CONTRACT BLOCK METRICS ===")
c3a_block = extract_block(V2_DIR / "13-candidate-3A-xml.md", '<apex_contract v="1.0"', '</apex_contract>')
print("3A contract block:", c3a_block)

c3b_block = extract_block(V2_DIR / "14-candidate-3B-hybrid.md", '<apex_contract v="1.0"', '</apex_contract>')
print("3B contract block:", c3b_block)

# Check delta
print("Delta (3B - 3A):")
for k in c3a_block:
    print(f"  {k}: {c3b_block[k] - c3a_block[k]}")

# Assembled blueprint:
# Let's inspect 03-BLUEPRINT-agents.md Layer 2
bp_text = (V2_DIR / "03-BLUEPRINT-agents.md").read_text(encoding="utf-8")
# Find Layer 2 start
layer2_start = bp_text.find("<!-- LAYER 2:")
layer2_block = bp_text[layer2_start:] if layer2_start != -1 else ""
print("\nLayer 2 block in blueprint:")
print({
    "lines": len(layer2_block.splitlines()),
    "chars": len(layer2_block),
    "words": len(layer2_block.split()),
    "repo_div4": len(layer2_block) // 4,
    "bpe": len(enc.encode(layer2_block))
})

# Let's check live AGENTS.md
agents_text = Path(r"c:\GitDev\apexai-os-meta\AGENTS.md").read_text(encoding="utf-8")
print("\nLive AGENTS.md:")
print({
    "lines": len(agents_text.splitlines()),
    "chars": len(agents_text),
    "words": len(agents_text.split()),
    "repo_div4": len(agents_text) // 4,
    "repo_w13": int(len(agents_text.split()) * 1.3),
    "bpe": len(enc.encode(agents_text))
})
