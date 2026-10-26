import re
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

candidate_3a = r"c:\GitDev\apexai-os-meta\apex-meta\informatics\final\candidates\13-candidate-3A-xml.md"

with open(candidate_3a, "r", encoding="utf-8") as f:
    text = f.read()

# Grab the xml code block
xml_match = re.search(r"```xml\s*([\s\S]*?)\s*```", text)
xml_content = xml_match.group(1)

tags = [
    "authoring",
    "trade_off",
    "handover",
    "iterative",
    "schemas",
    "sync",
    "pointers"
]

for tag in tags:
    pattern = rf"(<{tag}(?:\s+[^>]*)?>[\s\S]*?</{tag}>)"
    match = re.search(pattern, xml_content)
    if not match:
        print(f"FAILED TO FIND {tag}")
        continue
    block = match.group(1)
    
    # Extract inner
    inner_pattern = rf"<{tag}(?:\s+[^>]*)?>\s*([\s\S]*?)\s*</{tag}>"
    inner_match = re.search(inner_pattern, block)
    inner = inner_match.group(1).replace("\n", " ").strip()
    
    block_bpe = len(enc.encode(block))
    inner_bpe = len(enc.encode(inner))
    chars = len(block)
    inner_chars = len(inner)
    words = len(block.split())
    inner_words = len(inner.split())
    repo_tokens = chars // 4
    
    print(f"=== Rule <{tag}> ===")
    print(f"Block: {block_bpe} BPE, {repo_tokens} repo tokens, {chars} chars, {words} words")
    print(f"Inner: {inner_bpe} BPE, {inner_chars} chars, {inner_words} words")
    print(f"Exact block:\n{block}\n")
