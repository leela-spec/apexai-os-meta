import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

sbs = {
    # Rule 16
    "SB-16.1": "Flat YAML frontmatter: every line has a colon, lists use inline brackets, never multiline dashes.",
    "SB-16.2": "Concept files declare type, id, title, description, status.",
    "SB-16.3": "Front-load critical rules; close on the failure-mode guard.",
    "SB-16.4": "Tag governed rules [P0-P3 | I/E/R] 1-100, never combined.",
    "SB-16.5": "One responsibility per file. Link every file you list.",
    "SB-16.6": "Do not impose this on chat, code or logs. Open ref for tier definitions or bundle layout.",
    # Rule 17
    "SB-17.1": "Decide routine reversible choices yourself.",
    "SB-17.2": "For a material choice give each option a mechanism, a concrete grounding, and raw (I/E/R) estimates, then a recommendation and one line per rejection.",
    "SB-17.3": "Open ref for multi-candidate bake-offs.",
    # Rule 18
    "SB-18.1": "Never write a handover to defer what you can resolve now.",
    "SB-18.2": "When genuinely needed: what was observed, the reasoning chain, caveats, conclusion, and exact commands to reproduce.",
    "SB-18.3": "Open ref for delegation contracts (input ledger, process, output, DoD).",
    # Rule 19
    "SB-19.1": "Execute a clear single-step task directly.",
    "SB-19.2": "For multi-step work write a short preflight — target, inputs, scope, output, active step — then proceed step by step.",
    "SB-19.3": "For a multi-module project create a file per step.",
    "SB-19.4": "Open ref for the route ladder or MMM decomposition.",
    # Rule 20
    "SB-20.1": "Satisfy the declared schema exactly.",
    "SB-20.2": "Never invent fields.",
    "SB-20.3": "Target edits by heading path and surrounding text, never line number.",
    "SB-20.4": "Open ref for exact JSON or YAML schemas.",
    # Rule 21
    "SB-21.1": "Run the git commands first, not repository analysis.",
    "SB-21.2": "Preserve every file: commit unrelated dirty files separately rather than dropping them.",
    "SB-21.3": "On non-fast-forward, pull with rebase and retry.",
    # Rule 22
    "SB-22.1": "Paths are just-in-time pointers relative to base_ref.",
    "SB-22.2": "Open one only when its condition matches and the inline summary is insufficient."
}

for k, v in sbs.items():
    bpe = len(enc.encode(v))
    chars = len(v)
    print(f"{k}: {bpe} BPE, {chars} chars -> \"{v}\"")
