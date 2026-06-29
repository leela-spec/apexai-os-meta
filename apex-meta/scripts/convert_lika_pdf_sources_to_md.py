#!/usr/bin/env python3
"""
Convert Lika Verein Taxes Accounting PDF source files to Markdown using pymupdf4llm.

Scope:
- deterministic source extraction helper
- no semantic analysis
- no wiki generation
- no Phase 1 or Phase 2 writes
- writes only inside apex-meta/kb/lika-verein-taxes-accounting/
"""

from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import pymupdf4llm
except Exception as exc:  # pragma: no cover
    print("ERROR: pymupdf4llm is not importable in this environment.", file=sys.stderr)
    print(f"Import error: {exc}", file=sys.stderr)
    print("Install/activate the local environment that contains pymupdf4llm, then rerun.", file=sys.stderr)
    sys.exit(2)


REPO_ROOT = Path.cwd()

KB_ROOT = REPO_ROOT / "apex-meta" / "kb" / "lika-verein-taxes-accounting"
PDF_ROOT = KB_ROOT / "raw" / "refs"
OUT_DIR = PDF_ROOT / "_pdf_extracted_md"
REPORT_DIR = KB_ROOT / "manifests" / "pdf-extraction"

PDF_FILES = [
    PDF_ROOT / "DRV_K5001_Kuenstlersozialabgabe.pdf",
    PDF_ROOT / "IHK-Niederbayern_Checkliste-Kleinbetragsrechnungen.pdf",
    PDF_ROOT / "K5001.pdf",
    PDF_ROOT / "LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.pdf",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def ensure_inside(child: Path, parent: Path) -> None:
    child_resolved = child.resolve()
    parent_resolved = parent.resolve()
    if parent_resolved not in [child_resolved, *child_resolved.parents]:
        raise RuntimeError(f"Refusing to write outside parent. child={child} parent={parent}")


def convert_pdf(pdf_path: Path) -> dict[str, Any]:
    if not pdf_path.exists():
        return {
            "pdf_path": rel(pdf_path),
            "status": "missing",
            "error": "PDF file does not exist",
        }

    out_path = OUT_DIR / f"{pdf_path.stem}.md"
    ensure_inside(out_path, KB_ROOT)

    pdf_hash = sha256_file(pdf_path)

    try:
        md_body = pymupdf4llm.to_markdown(str(pdf_path))
    except Exception as exc:
        return {
            "pdf_path": rel(pdf_path),
            "pdf_sha256": pdf_hash,
            "status": "conversion_failed",
            "error": repr(exc),
        }

    if not isinstance(md_body, str) or not md_body.strip():
        return {
            "pdf_path": rel(pdf_path),
            "pdf_sha256": pdf_hash,
            "status": "empty_output",
            "error": "pymupdf4llm returned empty or non-string Markdown output",
        }

    generated_at = utc_now()
    header = f"""---
generated_by: "pymupdf4llm"
generated_at: "{generated_at}"
kb_slug: "lika-verein-taxes-accounting"
source_pdf_path: "{rel(pdf_path)}"
source_pdf_sha256: "{pdf_hash}"
artifact_role: "pdf_text_extraction_for_phase0_and_phase1_source_review"
semantic_status: "not_semantically_analyzed"
phase2_ready: false
---

# PDF Extraction: {pdf_path.stem}

> Deterministic PDF-to-Markdown extraction. This file is not a source-authoritative rewrite.
> Use it as extracted text evidence and verify against the original PDF where precision matters.

"""

    final_md = header + md_body.rstrip() + "\n"
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path.write_text(final_md, encoding="utf-8", newline="\n")

    return {
        "pdf_path": rel(pdf_path),
        "pdf_sha256": pdf_hash,
        "markdown_path": rel(out_path),
        "markdown_sha256": sha256_text(final_md),
        "status": "converted",
        "markdown_chars": len(final_md),
        "generated_at": generated_at,
    }


def write_reports(results: list[dict[str, Any]]) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    report_json = {
        "generated_at": utc_now(),
        "kb_slug": "lika-verein-taxes-accounting",
        "tool": "pymupdf4llm",
        "input_pdf_count": len(PDF_FILES),
        "converted_count": sum(1 for r in results if r.get("status") == "converted"),
        "failed_count": sum(1 for r in results if r.get("status") != "converted"),
        "results": results,
    }

    json_path = REPORT_DIR / "pdf-extraction-report.json"
    md_path = REPORT_DIR / "pdf-extraction-report.md"

    ensure_inside(json_path, KB_ROOT)
    ensure_inside(md_path, KB_ROOT)

    json_path.write_text(json.dumps(report_json, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    lines = [
        "# PDF Extraction Report",
        "",
        f"Generated: `{report_json['generated_at']}`",
        "",
        f"Tool: `pymupdf4llm`",
        f"KB: `lika-verein-taxes-accounting`",
        "",
        "## Summary",
        "",
        f"- Input PDFs: `{report_json['input_pdf_count']}`",
        f"- Converted: `{report_json['converted_count']}`",
        f"- Failed: `{report_json['failed_count']}`",
        "",
        "## Results",
        "",
        "| status | pdf | markdown | markdown_chars |",
        "|---|---|---|---:|",
    ]

    for r in results:
        lines.append(
            f"| `{r.get('status')}` | `{r.get('pdf_path', '')}` | `{r.get('markdown_path', '')}` | `{r.get('markdown_chars', '')}` |"
        )

    lines.extend([
        "",
        "## Boundary",
        "",
        "This extraction created Markdown text artifacts from preserved PDF sources only.",
        "It did not create Phase 1 semantic analyses, Phase 2 wiki pages, embeddings, vector stores, retrieval query packets, or Apex planning/session/sync state.",
        "",
    ])

    md_path.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def main() -> int:
    if not KB_ROOT.exists():
        print(f"ERROR: KB root does not exist: {KB_ROOT}", file=sys.stderr)
        return 2

    results = [convert_pdf(path) for path in PDF_FILES]
    write_reports(results)

    converted = sum(1 for r in results if r.get("status") == "converted")
    failed = [r for r in results if r.get("status") != "converted"]

    print(f"PDF extraction complete: converted={converted} failed={len(failed)}")
    for r in results:
        print(f"- {r.get('status')}: {r.get('pdf_path')} -> {r.get('markdown_path', '')}")

    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
