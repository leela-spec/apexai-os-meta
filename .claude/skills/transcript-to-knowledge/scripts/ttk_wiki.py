#!/usr/bin/env python3
"""Deterministic Macro/Meso/Micro Markdown wiki compiler."""
from ttk_verify import *
def slug(value: str, fallback: str = "note") -> str:
    base = _SAFE_SLUG.sub("-", value.casefold()).strip("-")
    return (base[:80] or fallback).strip("-")


def stable_claim_id(claim: dict[str, Any]) -> str:
    key = f"{norm_text(claim.get('claim_text', ''))}|{clean(claim.get('speaker')).casefold()}"
    return "Claim-" + hashlib.sha256(key.encode("utf-8")).hexdigest()[:12]


def _anchor_text(seg: dict[str, Any]) -> str:
    timing = seg.get("start_hms") or "timing unavailable"
    return f"`{seg['id']}` · {timing}"


def compile_wiki(run_dir: Path, strict: bool = True) -> dict[str, Any]:
    reduce_state = validate_reduce(run_dir)
    if reduce_state["status"] != "valid":
        raise TTKError(f"cannot compile: reduce result is {reduce_state['status']}")
    result = read_json(run_dir / "work" / "results" / "reduce.json")
    lookup = _segment_lookup(run_dir)
    if strict:
        unsupported = [c.get("claim_ref") for c in result.get("micro", []) if c.get("source_support") == "UNSUPPORTED"]
        if unsupported:
            raise TTKError(f"strict compile rejected unsupported final claims: {unsupported}")
    verify_state = validate_verify_results(run_dir)
    verification: dict[str, dict[str, Any]] = {}
    if verify_state["status"] == "invalid":
        raise TTKError("cannot compile with invalid verification results; remove/fix them or regenerate the queue")
    if verify_state["status"] == "valid":
        vr = read_json(run_dir / "work" / "results" / "verify" / "results.json")
        verification = {row["claim_ref"]: row for row in vr.get("results", [])}

    wiki = run_dir / "wiki"
    # The wiki subtree is compiler-owned. Remove only previously generated
    # Markdown pages before rebuilding so a changed semantic result cannot
    # leave stale modules/claims/entities behind after a resume or rerun.
    for folder in ("summaries", "modules", "claims", "entities", "concepts"):
        target = wiki / folder
        target.mkdir(parents=True, exist_ok=True)
        for old_page in target.glob("*.md"):
            old_page.unlink()

    entity_names = sorted(
        {clean(name) for module in result.get("meso", []) for name in module.get("entities", []) if clean(name)}
        | {clean(name) for c in result.get("micro", []) for name in c.get("entities", []) if clean(name)}
    )
    concept_names = sorted(
        {clean(name) for module in result.get("meso", []) for name in module.get("concepts", []) if clean(name)}
        | {clean(name) for c in result.get("micro", []) for name in c.get("topics", []) if clean(name)}
    )
    entity_pages = {name: slug(name) for name in entity_names}
    concept_pages = {name: slug(name) for name in concept_names}

    def concept_link(name: str) -> str:
        target = concept_pages.get(name, slug(name))
        return f"[[concepts/{target}|{name}]]"

    def entity_link(name: str) -> str:
        target = entity_pages.get(name, slug(name))
        return f"[[entities/{target}|{name}]]"

    claim_map: dict[str, str] = {}
    claim_rows: list[dict[str, Any]] = []
    for claim in result.get("micro", []):
        cid = stable_claim_id(claim)
        claim_map[claim["claim_ref"]] = cid
        ext = verification.get(claim["claim_ref"])
        external_status = ext["status"] if ext else ("UNVERIFIED" if claim.get("claim_kind") == "fact" else "NOT_APPLICABLE")
        lines = [
            f"# {cid}", "",
            f"**Proposition:** {claim['claim_text']}",
            f"**Kind:** {claim['claim_kind']}",
            f"**Source support:** {claim['source_support']}",
            f"**External status:** [{external_status}]",
            f"**Speaker:** {claim.get('speaker') or 'unknown'}", "",
            "## Transcript evidence", "",
        ]
        for quote in claim.get("quote_evidence", []):
            seg = lookup[quote["segment_id"]]
            lines.extend([f"- {_anchor_text(seg)}", f"  > {quote['quote']}"])
        if claim.get("context"):
            lines.extend(["", "## Context", "", clean(claim["context"])])
        if ext:
            lines.extend(["", "## External verification", "", f"**Verdict rationale:** {clean(ext.get('rationale')) or 'Not provided.'}", ""])
            for item in ext.get("evidence", []):
                meta = " · ".join(x for x in [clean(item.get("publisher")), clean(item.get("date"))] if x)
                lines.append(f"- [{item['stance']}] {item['title']} — {item['url']}{(' · ' + meta) if meta else ''}")
                if clean(item.get("note")):
                    lines.append(f"  - {clean(item['note'])}")
        links = [concept_link(name) for name in claim.get("topics", [])]
        links += [entity_link(name) for name in claim.get("entities", [])]
        if links:
            lines.extend(["", "## Links", "", " · ".join(links)])
        (wiki / "claims" / f"{cid}.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
        claim_rows.append({**claim, "claim_id": cid, "external_status": external_status})

    module_pages: dict[str, str] = {}
    for module in result.get("meso", []):
        filename = slug(module["title"], module["meso_ref"])
        module_pages[module["meso_ref"]] = filename
        lines = [f"# {module['title']}", "", module["summary"], "", "## Source", ""]
        lines.append("- " + ", ".join(_anchor_text(lookup[sid]) for sid in module["source_segment_ids"]))
        sections = [
            ("Mechanisms", module.get("mechanisms", [])),
            ("Protocols", module.get("protocols", [])),
            ("Arguments", module.get("arguments", [])),
            ("Caveats", module.get("caveats", [])),
        ]
        for title, values in sections:
            if values:
                lines.extend(["", f"## {title}", ""])
                for value in values:
                    lines.append(f"- {value}" if isinstance(value, str) else f"- {stable_json(value)}")
        links = [concept_link(name) for name in module.get("concepts", [])]
        links += [entity_link(name) for name in module.get("entities", [])]
        links += [f"[[claims/{claim_map[ref]}|{claim_map[ref]}]]" for ref in module.get("claim_refs", []) if ref in claim_map]
        if links:
            lines.extend(["", "## Related", "", " · ".join(links)])
        (wiki / "modules" / f"{filename}.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    macro = result["macro"]
    macro_lines = ["# Transcript Knowledge — Macro", "", "## Thesis", "", macro["thesis"], "", "## Summary", "", macro["summary"]]
    if macro.get("takeaways"):
        macro_lines.extend(["", "## Global Takeaways", ""])
        for item in macro["takeaways"]:
            refs = [f"[[modules/{module_pages[r]}|{next((m['title'] for m in result.get('meso', []) if m['meso_ref'] == r), r)}]]" for r in item.get("meso_refs", []) if r in module_pages]
            anchors = ", ".join(item.get("source_segment_ids", []))
            suffix = " · ".join(refs + ([f"`{anchors}`"] if anchors else []))
            macro_lines.append(f"- {item['text']}{(' — ' + suffix) if suffix else ''}")
    for title, values in (("Taxonomy", macro.get("taxonomy", [])), ("Speaker / Context", macro.get("speaker_context", [])), ("Contradictions / Uncertainty", macro.get("contradictions_or_uncertainty", []))):
        if values:
            macro_lines.extend(["", f"## {title}", ""])
            for value in values:
                macro_lines.append(f"- {value if isinstance(value, str) else stable_json(value)}")
    macro_lines.extend(["", "## Meso Modules", ""])
    for module in result.get("meso", []):
        macro_lines.append(f"- [[modules/{module_pages[module['meso_ref']]}|{module['title']}]]")
    (wiki / "summaries" / "Macro.md").write_text("\n".join(macro_lines).rstrip() + "\n", encoding="utf-8")

    for kind, names in (("entities", entity_names), ("concepts", concept_names)):
        pages = entity_pages if kind == "entities" else concept_pages
        for name in names:
            lines = [f"# {name}", "", "## Related modules", ""]
            for module in result.get("meso", []):
                field = "entities" if kind == "entities" else "concepts"
                if name in module.get(field, []):
                    lines.append(f"- [[modules/{module_pages[module['meso_ref']]}|{module['title']}]]")
            lines.extend(["", "## Related claims", ""])
            for row in claim_rows:
                field = "entities" if kind == "entities" else "topics"
                if name in row.get(field, []):
                    lines.append(f"- [[claims/{row['claim_id']}|{row['claim_id']}]] — {row['claim_text']}")
            (wiki / kind / f"{pages[name]}.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    index_lines = [
        "# Transcript Knowledge", "", "- [[summaries/Macro|Macro]]", "", "## Modules", "",
        *[f"- [[modules/{module_pages[m['meso_ref']]}|{m['title']}]]" for m in result.get("meso", [])],
        "", "## Claims", "",
        *[f"- [[claims/{row['claim_id']}|{row['claim_id']}]] — {row['claim_text']}" for row in claim_rows],
        "", "## Concepts", "", *[f"- {concept_link(name)}" for name in concept_names],
        "", "## Entities", "", *[f"- {entity_link(name)}" for name in entity_names],
    ]
    (wiki / "index.md").write_text("\n".join(index_lines).rstrip() + "\n", encoding="utf-8")
    compiled = {
        "schema": "ttk.compiled.v2",
        "reduce_result_sha256": file_hash(run_dir / "work" / "results" / "reduce.json"),
        "verify_results_sha256": (
            file_hash(run_dir / "work" / "results" / "verify" / "results.json")
            if verify_state["status"] == "valid"
            else None
        ),
        "macro": "wiki/summaries/Macro.md",
        "module_count": len(module_pages),
        "claim_count": len(claim_rows),
        "concept_count": len(concept_names),
        "entity_count": len(entity_names),
        "verification_state": verify_state["status"],
    }
    write_json(run_dir / "wiki" / "compiled.json", compiled)
    return compiled



__all__ = [name for name in globals() if not name.startswith("__")]
