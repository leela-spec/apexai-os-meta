import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

options_data = [
    (16, "authoring",
     '<authoring when="creating, editing or validating a governed knowledge or specification file" ref="index.md">',
     '</authoring>',
     "Flat YAML frontmatter: every line has a colon, lists use inline brackets, never multiline dashes. Concept files declare type, id, title, description, status. Front-load critical rules; close on the failure-mode guard. Tag governed rules [P0-P3 | I/E/R] 1-100, never combined. One responsibility per file. Link every file you list. Do not impose this on chat, code or logs. Open ref for tier definitions or bundle layout.",
     "Flat YAML frontmatter: colons on every line, inline bracket lists, no multiline dashes. Concept files declare type, id, title, description, status. Front-load invariants; close on failure guards. Tag rules [P0-P3 | I/E/R] 1-100 uncombined. One purpose per file; link listed files. Exclude chat, code, and logs. Open ref for tier definitions or bundle layout.",
     "Flat YAML frontmatter: inline brackets for lists, no multiline dashes. Declare type, id, title, description, status. Front-load invariants; close on failure guards. Tag rules [P0-P3 | I/E/R] 1-100 uncombined. One purpose per file; link listed files. Exclude chat, code, and logs. Open ref for tier/bundle specs."
    ),
    (17, "trade_off",
     '<trade_off when="the operator must choose between material alternatives, or asks for options" ref="execution-modes.md">',
     '</trade_off>',
     "Decide routine reversible choices yourself. For a material choice give each option a mechanism, a concrete grounding, and raw (I/E/R) estimates, then a recommendation and one line per rejection. Open ref for multi-candidate bake-offs.",
     "Decide routine reversible choices yourself. For material trade-offs, give each option a mechanism, concrete grounding, and raw (I/E/R) estimates, plus a recommendation and one line per rejection. Open ref for multi-candidate bake-offs.",
     "Decide routine reversible choices yourself. For material trade-offs, provide each option's mechanism, grounding, and raw (I/E/R) metrics, plus recommendation and one-line rejections. Open ref for multi-candidate bake-offs."
    ),
    (18, "handover",
     '<handover when="ending a session, delegating to a subagent, or writing any handoff" ref="execution-modes.md">',
     '</handover>',
     "Never write a handover to defer what you can resolve now. When genuinely needed: what was observed, the reasoning chain, caveats, conclusion, and exact commands to reproduce. Open ref for delegation contracts (input ledger, process, output, DoD).",
     "Never write a handover to defer resolvable work. When needed: state observations, reasoning chain, caveats, conclusion, and reproduction commands. Open ref for delegation contracts (input ledger, process, output, DoD).",
     "Never write a handover to defer resolvable work. When needed: include observation, reasoning chain, caveats, conclusion, and reproduction commands. Open ref for delegation contracts (input ledger, process, output, DoD)."
    ),
    (19, "iterative",
     '<iterative when="the task spans multiple modules, needs research, or cannot finish in one pass" ref="execution-modes.md">',
     '</iterative>',
     "Execute a clear single-step task directly. For multi-step work write a short preflight — target, inputs, scope, output, active step — then proceed step by step. For a multi-module project create a file per step. Open ref for the route ladder or MMM decomposition.",
     "Execute single-step tasks directly. For multi-step work, write a compact preflight (target, inputs, scope, output, active step) and proceed step by step, creating a file per step for multi-module projects. Open ref for route ladder or MMM decomposition.",
     "Execute single-step tasks directly. For multi-step work, draft a short preflight (target, inputs, scope, output, active step) and proceed step by step, creating a file per step for multi-module projects. Open ref for route ladder or MMM decomposition."
    ),
    (20, "schemas",
     '<schemas when="emitting a patch intent, or validating bundle or schema conformance" ref="governance-schemas.md">',
     '</schemas>',
     "Satisfy the declared schema exactly. Never invent fields. Target edits by heading path and surrounding text, never line number. Open ref for exact JSON or YAML schemas.",
     "Conform to declared schemas exactly; never invent fields. Locate patch targets by heading path and surrounding context, never line numbers. Open ref for exact JSON or YAML schemas.",
     "Satisfy declared schemas exactly with zero invented fields. Target edits via heading path and context, never line numbers. Open ref for exact JSON or YAML schemas."
    ),
    (21, "sync",
     '<sync when="the operator asks to sync, commit or push">',
     '</sync>',
     "Run the git commands first, not repository analysis. Preserve every file: commit unrelated dirty files separately rather than dropping them. On non-fast-forward, pull with rebase and retry.",
     "Execute git commands immediately, not repo analysis. Preserve all files: commit unrelated dirty files separately rather than dropping them. On non-fast-forward, pull with rebase and retry.",
     "Run git commands immediately without repo analysis. Preserve all files: commit unrelated dirty files separately instead of dropping them. On non-fast-forward, pull --rebase and retry."
    ),
    (22, "pointers",
     '<pointers>',
     '</pointers>',
     "Paths are just-in-time pointers relative to base_ref. Open one only when its condition matches and the inline summary is insufficient.",
     "Paths are just-in-time pointers relative to base_ref. Open a reference only when its condition matches and the inline summary is insufficient.",
     "Paths are JIT pointers relative to base_ref. Open a reference only when its condition triggers and the inline summary is insufficient."
    )
]

for r_id, name, topen, tclose, optA, optB, optC in options_data:
    print(f"\n================ Rule {r_id} <{name}> ================")
    for label, text in [("A", optA), ("B", optB), ("C", optC)]:
        if topen == f"<{name}>":
            block = f"{topen}{text}{tclose}"
        else:
            block = f"{topen}\n{text}\n{tclose}"
        bpe = len(enc.encode(block))
        inner_bpe = len(enc.encode(text))
        print(f"Option {label}: Block={bpe} BPE, Inner={inner_bpe} BPE")
