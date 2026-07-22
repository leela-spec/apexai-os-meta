from __future__ import annotations

import json
import zipfile
from pathlib import Path
from typing import Any

from pypdf import PdfWriter

from apex_kb.config import normalize_config, preview_config
from apex_kb.io import atomic_json, load_json
from apex_kb.lifecycle import create_manifest, derive_next_action, initial_state, load_run, write_new_run


def write_docx(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body><w:p><w:r><w:t>{text}</w:t></w:r></w:p></w:body></w:document>'''
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("word/document.xml", xml)


def write_pptx(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><p:cSld><p:spTree><p:sp><p:txBody><a:p><a:r><a:t>{text}</a:t></a:r></a:p></p:txBody></p:sp></p:spTree></p:cSld></p:sld>'''
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("ppt/slides/slide1.xml", xml)


def write_xlsx(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    shared = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><si><t>{text}</t></si></sst>'''
    sheet = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData><row r="1"><c r="A1" t="s"><v>0</v></c></row></sheetData></worksheet>'''
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("xl/sharedStrings.xml", shared)
        archive.writestr("xl/worksheets/sheet1.xml", sheet)


def write_pdf(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    writer = PdfWriter()
    writer.add_blank_page(width=72, height=72)
    with path.open("wb") as handle:
        writer.write(handle)



def write_text_pdf(path: Path, text: str) -> None:
    """Write a tiny uncompressed one-page PDF with extractable text."""
    path.parent.mkdir(parents=True, exist_ok=True)
    escaped = text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
    stream = f"BT /F1 12 Tf 72 720 Td ({escaped}) Tj ET".encode("latin-1")
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
        b"<< /Length " + str(len(stream)).encode("ascii") + b" >>\nstream\n" + stream + b"\nendstream",
    ]
    content = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for index, body in enumerate(objects, 1):
        offsets.append(len(content))
        content.extend(f"{index} 0 obj\n".encode("ascii"))
        content.extend(body)
        content.extend(b"\nendobj\n")
    xref = len(content)
    content.extend(f"xref\n0 {len(objects)+1}\n".encode("ascii"))
    content.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        content.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    content.extend(f"trailer\n<< /Size {len(objects)+1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode("ascii"))
    path.write_bytes(bytes(content))

def default_topics() -> list[dict[str, Any]]:
    return [
        {
            "topic_id": "skill-tree",
            "name": "Skill Tree",
            "primary_phrases": ["skill tree", "skilltree"],
            "aliases": ["spatial skill tree"],
            "supporting_terms": ["epic", "block", "chunk"],
            "negative_terms": ["tree care"],
            "ambiguous_terms": ["tree"],
            "target_queries": [
                {
                    "query_id": "skill-tree-definition",
                    "priority": "critical",
                    "question": "What is the current Skill Tree and what does it own?",
                    "answer_requirements": ["definition", "ownership", "hierarchy"],
                }
            ],
            "expected_routes": {"dossier": "wiki/concepts/skill-tree.md", "source_atlas": "wiki/summaries/skill-tree-source-atlas.md"},
        },
        {
            "topic_id": "sequencing",
            "name": "Sequencing",
            "primary_phrases": ["sequencing workflow"],
            "aliases": ["sequence editor"],
            "supporting_terms": ["timeline", "chunk order"],
            "negative_terms": [],
            "ambiguous_terms": ["sequence"],
            "target_queries": [
                {
                    "query_id": "sequencing-definition",
                    "priority": "routine",
                    "question": "How does the sequencing workflow order chunks?",
                    "answer_requirements": ["workflow", "order"],
                }
            ],
            "expected_routes": {"dossier": "wiki/concepts/sequencing.md", "source_atlas": "wiki/summaries/sequencing-source-atlas.md"},
        },
    ]


def make_workspace(tmp_path: Path, *, output: str = "query_ready", handling: str = "pointer_only", topics: list[dict[str, Any]] | None = None, include_formats: bool = True) -> tuple[Path, Path, dict[str, Any]]:
    source_repo = tmp_path / "leela"
    source = source_repo / "LeelaAppDevelopment"
    destination = tmp_path / "apex"
    source.mkdir(parents=True)
    destination.mkdir()
    (source / "01_Features").mkdir()
    (source / "01_Features" / "102 - Epics (Database + Skill Tree).md").write_text(
        "# Skill Tree\n\nThe current Skill Tree is a read-only graph of Epic, Block, and Chunk content.\n\n## Ownership\nIt navigates content but does not mutate it.\n",
        encoding="utf-8",
    )
    (source / "01_Features" / "210 - Sequencing.md").write_text(
        "# Sequencing workflow\n\nThe sequencing workflow orders chunks on a timeline.\n",
        encoding="utf-8",
    )
    (source / "Archive").mkdir()
    (source / "Archive" / "Skill Tree v1.md").write_text("# Old Skill Tree\nHistorical skill tree prototype.\n", encoding="utf-8")
    (source / "Notes").mkdir()
    (source / "Notes" / "tree-care.md").write_text("# Tree care\nWater a tree.\n", encoding="utf-8")
    (source / "Generated").mkdir()
    (source / "Generated" / "skill-tree-generated.md").write_text("skill tree generated export", encoding="utf-8")
    (source / "Duplicates").mkdir()
    duplicate = "# Spatial Skill Tree\nEpic and Block graph.\n"
    (source / "Duplicates" / "skill-tree-copy-a.md").write_text(duplicate, encoding="utf-8")
    (source / "Duplicates" / "skill-tree-copy-b.md").write_text(duplicate, encoding="utf-8")
    if include_formats:
        write_docx(source / "Formats" / "skill-tree.docx", "Skill Tree office specification")
        write_pptx(source / "Formats" / "sequencing.pptx", "Sequencing workflow slide")
        write_xlsx(source / "Formats" / "skill-tree.xlsx", "Skill Tree spreadsheet")
        write_pdf(source / "Formats" / "skill-tree.pdf")
        (source / "Formats" / "skill-tree.png").write_bytes(b"not-a-real-png")
        (source / "Formats" / "skill-tree.bin").write_bytes(b"\x00\x01\x02")
    raw = {
        "schema": "apex.kb.run-config.v2",
        "source": {"repository": "leela-spec/leela", "root": str(source_repo), "folders": ["LeelaAppDevelopment"]},
        "destination": {"repository": "leela-spec/apexai-os-meta", "root": str(destination), "folder": "apex-meta/kb/leela-canary"},
        "exclusions": [{"path": "LeelaAppDevelopment/Generated", "reason": "generated_output", "rule_id": "exclude-generated"}],
        "topics": topics or default_topics(),
        "run_options": {
            "source_handling": handling,
            "semantic_depth": "standard",
            "output": output,
            "non_text": "inventory_and_report",
            "git_metadata": False,
            "graph_depth": "links",
            "ai_help_after_preflight": False,
            "max_semantic_repairs": 2,
        },
    }
    config = normalize_config(raw)
    return source_repo, destination, config


def initialize(tmp_path: Path, *, output: str = "query_ready", handling: str = "pointer_only", topics: list[dict[str, Any]] | None = None, include_formats: bool = True) -> tuple[Path, Path, dict[str, Any]]:
    source_repo, _, config = make_workspace(tmp_path, output=output, handling=handling, topics=topics, include_formats=include_formats)
    run_root, _, preview = preview_config(config)
    manifest = create_manifest(config, run_root, preview)
    state = initial_state(manifest)
    write_new_run(run_root, config, manifest, state)
    return run_root, source_repo, config


def _phase1_result(run_root: Path, task: dict[str, Any], allowlist: dict[str, Any]) -> dict[str, Any]:
    reviews = []
    capsules_by_hash: dict[str, dict[str, Any]] = {}
    for source in allowlist["sources"]:
        blocked = source["extraction_status"] in {"unsupported", "error", "metadata_only"}
        reused = bool(source.get("reusable_capsule_path"))
        if blocked:
            read_status, disposition = "blocked", "blocked_unsupported"
        elif reused:
            read_status, disposition = "capsule_reused", "core"
        else:
            read_status, disposition = "full", "core"
        review = {
            "source_id": source["source_id"],
            "repository_path": source["repository_path"],
            "content_hash": source["content_hash"],
            "read_status": read_status,
            "disposition": disposition,
            "summary": f"Review of {source['repository_path']}",
            "individual_value": "Provides source-grounded topic evidence." if not blocked else "Visible candidate but text was unavailable.",
            "authority": "candidate_requires_context",
            "freshness": "current_or_unknown",
            "pointers": [reason["pointers"][0] for reason in source["match_reasons"] if reason["pointers"]][:3],
            "questions_supported": [item["query_id"] for item in task["target_queries"]] if not blocked else [],
            "duplicate_or_supersession": None,
        }
        reviews.append(review)
        if disposition == "core" and not reused and source["content_hash"] not in capsules_by_hash:
            capsules_by_hash[source["content_hash"]] = {
                "schema": "apex.kb.source-capsule.v2",
                "source_id": source["source_id"],
                "repository_path": source["repository_path"],
                "content_hash": source["content_hash"],
                "title": Path(source["repository_path"]).stem,
                "summary": f"Capsule for {source['repository_path']}",
                "key_claims": ["Contains evidence for the configured topic."],
                "contributions": ["Supports the locked target questions."],
                "contradictions": [],
                "uncertainties": [],
                "authority": "candidate_requires_context",
                "freshness": "current_or_unknown",
                "pointers": review["pointers"],
            }
    return {
        "schema": "apex.kb.phase1-result.v2",
        "run_id": task["run_id"],
        "config_hash": task["config_hash"],
        "task_id": task["task_id"],
        "phase": "phase1",
        "topic_id": task["topic_id"],
        "topic_name": task["topic"]["name"],
        "worker_context_id": f"ctx-{task['task_id']}",
        "source_reviews": reviews,
        "source_capsules": list(capsules_by_hash.values()),
        "topic_analysis": {
            "macro": f"{task['topic']['name']} matters to the wider Leela experience.",
            "meso": f"{task['topic']['name']} is a bounded project capability.",
            "micro": "The implementation is described by the reviewed source set.",
            "target_answers": [
                {"query_id": item["query_id"], "answer": f"Answer for {item['question']}", "citations": [review["source_id"] for review in reviews if review["read_status"] != "blocked"][:2]}
                for item in task["target_queries"]
            ],
            "contradictions": [],
            "uncertainties": [],
        },
    }


def _phase2_result(run_root: Path, task: dict[str, Any]) -> dict[str, Any]:
    analysis = load_json(Path(task["phase1_analysis_path"]))
    reviews = analysis["source_reviews"]
    return {
        "schema": "apex.kb.phase2-result.v2",
        "run_id": task["run_id"],
        "config_hash": task["config_hash"],
        "task_id": task["task_id"],
        "phase": "phase2",
        "topic_id": task["topic_id"],
        "worker_context_id": f"draft-{task['task_id']}",
        "dossier": {
            "route": task["required_routes"]["dossier"],
            "title": task["topic"]["name"],
            "executive_summary": f"Accepted durable overview of {task['topic']['name']}.",
            "macro": analysis["topic_analysis"]["macro"],
            "meso": analysis["topic_analysis"]["meso"],
            "micro": analysis["topic_analysis"]["micro"],
            "target_answers": [
                {
                    "query_id": item["query_id"],
                    "question": item["question"],
                    "answer": f"Compiled answer for {item['question']}",
                    "citations": [{"source_id": reviews[0]["source_id"], "pointer": reviews[0]["pointers"][0] if reviews[0]["pointers"] else "document"}],
                }
                for item in task["target_queries"]
            ],
            "key_claims": [{"claim": f"{task['topic']['name']} has a defined current role.", "state": "present", "citations": [{"source_id": reviews[0]["source_id"], "pointer": reviews[0]["pointers"][0] if reviews[0]["pointers"] else "document"}]}],
            "evolution": ["Historical and current candidates are preserved in the source atlas."],
            "contradictions": analysis["topic_analysis"]["contradictions"],
            "uncertainties": analysis["topic_analysis"]["uncertainties"],
        },
        "atlas": {
            "route": task["required_routes"]["source_atlas"],
            "title": f"{task['topic']['name']} source atlas",
            "entries": [
                {
                    "source_id": review["source_id"],
                    "repository_path": review["repository_path"],
                    "disposition": review["disposition"],
                    "read_status": review["read_status"],
                    "content_snapshot": review["summary"],
                    "individual_value": review["individual_value"],
                    "authority": review["authority"],
                    "freshness": review["freshness"],
                    "duplicate_or_supersession": review["duplicate_or_supersession"],
                    "pointers": review["pointers"],
                    "questions_supported": review["questions_supported"],
                }
                for review in reviews
            ],
        },
    }


def _acceptance_result(task: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema": "apex.kb.acceptance-result.v2",
        "run_id": task["run_id"],
        "config_hash": task["config_hash"],
        "task_id": task["task_id"],
        "phase": "acceptance",
        "topic_id": task["topic_id"],
        "evaluator_context_id": f"fresh-evaluator-{task['task_id']}",
        "verdict": "semantic_pass",
        "question_evaluations": [
            {"query_id": item["query_id"], "verdict": "pass", "answer_summary": "Directly answered from compiled pages.", "page_pointers": [task["page_paths"][0] + "#direct-answers"], "raw_source_required": False}
            for item in task["target_queries"]
        ],
        "claim_checks": [{"claim": "Sampled material claim", "verdict": "pass", "evidence_pointers": task["evidence_paths"][:1]}],
        "failed_items": [],
        "notes": ["Fresh-context page-only acceptance passed."],
    }


def satisfy_active_task(run_root: Path) -> dict[str, Any] | None:
    manifest, state = load_run(run_root)
    active = state.get("active_task")
    if not active:
        return None
    incoming = Path(active["incoming_path"])
    if incoming.is_file():
        return None
    packet = Path(active["packet_dir"])
    task = load_json(packet / "task.json")
    allowlist = load_json(packet / "source-allowlist.json")
    if active["task_kind"] == "phase1":
        result = _phase1_result(run_root, task, allowlist)
    elif active["task_kind"] == "phase2":
        result = _phase2_result(run_root, task)
    else:
        result = _acceptance_result(task)
    incoming.parent.mkdir(parents=True, exist_ok=True)
    atomic_json(incoming, result)
    return result


def current_action(run_root: Path) -> dict[str, Any]:
    manifest, state = load_run(run_root)
    return derive_next_action(manifest, state)
