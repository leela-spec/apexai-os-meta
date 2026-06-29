#!/usr/bin/env python3
"""
convert-lika-verein-downloaded-pdfs.py

Convert newly downloaded / report-listed PDF sources in the
lika-verein-taxes-accounting Apex KB into Markdown.

Policy:
- Use pymupdf4llm first.
- Use marker-pdf only when the pymupdf4llm output fails a lightweight QC check.
- Keep Markdown next to the PDF.
- Write one .conversion-report.json next to each PDF.
- Write one aggregate summary under manifests/pdf-transformations/.
- Do not run Apex KB Phase 1.
- Do not create wiki files.
- Do not delete PDFs or downloaded sources.

Intended repo root:
  C:\\GitDev\\apexai-os-meta

Default report:
  apex-meta/kb/lika-verein-taxes-accounting/manifests/downloads/missing-source-download-report_20260629_171832.json
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCRIPT_NAME = "convert-lika-verein-downloaded-pdfs.py"
DEFAULT_KB_REL = Path("apex-meta/kb/lika-verein-taxes-accounting")
DEFAULT_REPORT_REL = DEFAULT_KB_REL / "manifests/downloads/missing-source-download-report_20260629_171832.json"
PDF_SUFFIX = ".pdf"


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")


def iso_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def resolve_repo_root(start: Path | None = None) -> Path:
    current = (start or Path.cwd()).resolve()
    for candidate in [current, *current.parents]:
        if (candidate / ".git").exists() or (candidate / "apex-meta").exists():
            return candidate
    return current


def relpath(path: Path, root: Path) -> str:
    try:
        return str(path.resolve().relative_to(root.resolve())).replace("\\", "/")
    except ValueError:
        return str(path)


def normalize_report_path(raw_path: str, repo_root: Path, kb_root: Path) -> Path:
    """Resolve paths from the download report.

    The report mixes repo-relative paths such as:
      apex-meta\\kb\\...\\raw\\refs\\file.pdf
    with KB-relative paths such as:
      raw/refs/file.pdf
    and absolute Windows paths.
    """
    cleaned = raw_path.strip().replace("\\", "/")
    if not cleaned:
        return Path()

    # Windows absolute path: C:/GitDev/...
    if re.match(r"^[A-Za-z]:/", cleaned):
        return Path(cleaned)

    path = Path(cleaned)
    if cleaned.startswith("apex-meta/"):
        return repo_root / path
    if cleaned.startswith("raw/") or cleaned.startswith("sources/") or cleaned.startswith("manifests/"):
        return kb_root / path
    return repo_root / path


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def iter_nested_values(obj: Any) -> Any:
    if isinstance(obj, dict):
        for value in obj.values():
            yield from iter_nested_values(value)
    elif isinstance(obj, list):
        for item in obj:
            yield from iter_nested_values(item)
    else:
        yield obj


def collect_report_pdf_paths(report: dict[str, Any], repo_root: Path, kb_root: Path) -> list[Path]:
    """Collect all PDF paths explicitly mentioned by the download report."""
    pdfs: set[Path] = set()

    manifest = report.get("manifest") if isinstance(report.get("manifest"), dict) else {}
    for source_path in manifest.get("source_paths", []) or []:
        if isinstance(source_path, str) and source_path.lower().endswith(PDF_SUFFIX):
            pdfs.add(normalize_report_path(source_path, repo_root, kb_root))

    # Capture any nested field that looks like a PDF path, including target_path,
    # targets[".pdf"], and absolute paths.
    for value in iter_nested_values(report.get("results", {})):
        if isinstance(value, str) and value.lower().endswith(PDF_SUFFIX):
            pdfs.add(normalize_report_path(value, repo_root, kb_root))

    return sorted(pdfs)


def collect_all_kb_pdfs(kb_root: Path) -> list[Path]:
    return sorted(kb_root.rglob("*.pdf")) if kb_root.exists() else []


def run(cmd: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=str(cwd) if cwd else None,
        text=True,
        capture_output=True,
        check=False,
    )


def convert_with_pymupdf4llm(pdf: Path, out_md: Path, repo_root: Path) -> dict[str, Any]:
    py = f"""
import pymupdf4llm
from pathlib import Path
pdf = Path(r'''{str(pdf)}''')
out = Path(r'''{str(out_md)}''')
md = pymupdf4llm.to_markdown(str(pdf))
out.write_text(md, encoding='utf-8')
print(len(md))
"""
    result = run([sys.executable, "-c", py], cwd=repo_root)
    return {
        "converter": "pymupdf4llm",
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }


def convert_with_marker(pdf: Path, out_md: Path, repo_root: Path) -> dict[str, Any]:
    """Try common marker-pdf CLI variants without assuming one exact install."""
    out_dir = out_md.parent / f"{pdf.stem}.marker-output"
    out_dir.mkdir(parents=True, exist_ok=True)

    candidates = [
        ["marker_single", str(pdf), "--output_dir", str(out_dir)],
        ["marker_single", str(pdf), str(out_dir)],
        ["marker", str(pdf), "--output_dir", str(out_dir)],
        [sys.executable, "-m", "marker", str(pdf), "--output_dir", str(out_dir)],
    ]

    attempts: list[dict[str, Any]] = []
    for cmd in candidates:
        result = run(cmd, cwd=repo_root)
        attempts.append(
            {
                "cmd": cmd,
                "returncode": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
            }
        )
        if result.returncode == 0:
            md_candidates = list(out_dir.rglob("*.md"))
            if md_candidates:
                best = max(md_candidates, key=lambda p: p.stat().st_size)
                out_md.write_text(best.read_text(encoding="utf-8", errors="replace"), encoding="utf-8")
                return {
                    "converter": "marker-pdf",
                    "returncode": 0,
                    "attempts": attempts,
                    "selected_output": relpath(best, repo_root),
                }

    return {
        "converter": "marker-pdf",
        "returncode": 1,
        "attempts": attempts,
    }


def quality_check(md_path: Path) -> dict[str, Any]:
    if not md_path.exists():
        return {
            "status": "fail",
            "reason": "markdown_not_created",
            "warnings": ["markdown_not_created"],
            "size_chars": 0,
            "heading_count": 0,
            "tableish_count": 0,
            "line_count": 0,
        }

    text = md_path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    size_chars = len(text)
    heading_count = sum(1 for line in lines if line.lstrip().startswith("#"))
    tableish_count = text.count("|---") + text.count("<table") + text.count("</table>")
    replacement_char_count = text.count("\ufffd")

    warnings: list[str] = []
    if size_chars < 2000:
        warnings.append("low_text_volume")
    if heading_count < 3:
        warnings.append("low_heading_count")
    if tableish_count > 3:
        warnings.append("table_heavy")
    if replacement_char_count > 20:
        warnings.append("many_replacement_chars")

    return {
        "status": "review" if warnings else "pass",
        "warnings": warnings,
        "size_chars": size_chars,
        "heading_count": heading_count,
        "tableish_count": tableish_count,
        "replacement_char_count": replacement_char_count,
        "line_count": len(lines),
    }


def transform_pdf(
    pdf: Path,
    repo_root: Path,
    force: bool,
    marker: bool,
    dry_run: bool,
) -> dict[str, Any]:
    out_md = pdf.with_suffix(".md")
    marker_md = pdf.with_suffix(".marker.md")
    report_path = pdf.with_suffix(".conversion-report.json")

    report: dict[str, Any] = {
        "pdf": relpath(pdf, repo_root),
        "markdown": relpath(out_md, repo_root),
        "marker_markdown": relpath(marker_md, repo_root),
        "conversion_report": relpath(report_path, repo_root),
        "created_at": iso_now(),
        "script": SCRIPT_NAME,
        "policy": "pymupdf4llm first; marker-pdf only if quality check fails",
        "dry_run": dry_run,
        "force": force,
        "steps": [],
    }

    if not pdf.exists():
        report["status"] = "missing_pdf"
        report["error"] = "PDF path listed in report does not exist in the local repo."
        return report

    if out_md.exists() and out_md.stat().st_size > 0 and not force:
        qc = quality_check(out_md)
        report["status"] = "skipped_existing_markdown"
        report["quality_check_existing_markdown"] = qc
        report["selected_markdown"] = relpath(out_md, repo_root)
        report["selection_reason"] = "existing_markdown_present_use_force_to_regenerate"
        if not dry_run:
            report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
        return report

    if dry_run:
        report["status"] = "would_convert"
        report["selected_markdown"] = relpath(out_md, repo_root)
        return report

    primary_step = convert_with_pymupdf4llm(pdf, out_md, repo_root)
    report["steps"].append(primary_step)

    qc = quality_check(out_md)
    report["quality_check_after_pymupdf4llm"] = qc

    if primary_step.get("returncode") != 0:
        report["status"] = "pymupdf4llm_failed"
        if marker:
            marker_step = convert_with_marker(pdf, marker_md, repo_root)
            report["steps"].append(marker_step)
            marker_qc = quality_check(marker_md)
            report["quality_check_after_marker"] = marker_qc
            if marker_step.get("returncode") == 0 and marker_md.exists() and marker_md.stat().st_size > 0:
                report["status"] = "converted_with_marker_after_pymupdf4llm_failure"
                report["selected_markdown"] = relpath(marker_md, repo_root)
                report["selection_reason"] = "pymupdf4llm_failed_marker_succeeded"
        report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
        return report

    if qc["status"] != "pass" and marker:
        marker_step = convert_with_marker(pdf, marker_md, repo_root)
        report["steps"].append(marker_step)
        marker_qc = quality_check(marker_md)
        report["quality_check_after_marker"] = marker_qc

        # Prefer marker if it succeeded and appears materially larger or has more headings.
        marker_better = (
            marker_step.get("returncode") == 0
            and marker_md.exists()
            and (
                marker_qc.get("size_chars", 0) > qc.get("size_chars", 0) * 1.10
                or marker_qc.get("heading_count", 0) > qc.get("heading_count", 0)
            )
        )
        if marker_better:
            report["status"] = "converted_marker_selected"
            report["selected_markdown"] = relpath(marker_md, repo_root)
            report["selection_reason"] = "marker_output_larger_or_structurally_better_after_pymupdf4llm_review"
        else:
            report["status"] = "converted_pymupdf4llm_retained_after_marker_review"
            report["selected_markdown"] = relpath(out_md, repo_root)
            report["selection_reason"] = "pymupdf4llm_output_retained"
    else:
        report["status"] = "converted_pymupdf4llm_selected"
        report["selected_markdown"] = relpath(out_md, repo_root)
        report["selection_reason"] = "pymupdf4llm_quality_pass_or_marker_disabled"

    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    return report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert PDF sources listed in the Lika Verein download report to Markdown."
    )
    parser.add_argument(
        "--repo-root",
        default=None,
        help="Repository root. Defaults to nearest parent with .git or apex-meta.",
    )
    parser.add_argument(
        "--kb-root",
        default=str(DEFAULT_KB_REL),
        help="KB root relative to repo root or absolute path.",
    )
    parser.add_argument(
        "--download-report",
        default=str(DEFAULT_REPORT_REL),
        help="Download report path relative to repo root or absolute path.",
    )
    parser.add_argument(
        "--all-kb-pdfs",
        action="store_true",
        help="Convert all PDFs under the KB root, not only PDFs mentioned in the download report.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Regenerate Markdown even when a non-empty .md already exists next to the PDF.",
    )
    parser.add_argument(
        "--no-marker",
        action="store_true",
        help="Disable marker-pdf fallback even when QC fails.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report what would be converted without writing Markdown/report files.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve() if args.repo_root else resolve_repo_root()

    kb_root_arg = Path(args.kb_root)
    kb_root = kb_root_arg if kb_root_arg.is_absolute() else repo_root / kb_root_arg

    report_arg = Path(args.download_report)
    report_path = report_arg if report_arg.is_absolute() else repo_root / report_arg

    if not kb_root.exists():
        print(f"ERROR: KB root not found: {kb_root}", file=sys.stderr)
        return 2

    pdfs: list[Path] = []
    source_mode = "download_report"
    report: dict[str, Any] | None = None

    if args.all_kb_pdfs:
        pdfs = collect_all_kb_pdfs(kb_root)
        source_mode = "all_kb_pdfs"
    else:
        if not report_path.exists():
            print(f"ERROR: Download report not found: {report_path}", file=sys.stderr)
            return 2
        report = load_json(report_path)
        pdfs = collect_report_pdf_paths(report, repo_root, kb_root)

    # Keep only existing or intended KB PDFs; missing paths are still reported by transform_pdf.
    pdfs = sorted(dict.fromkeys(pdfs))

    summary: dict[str, Any] = {
        "generated_at": iso_now(),
        "script": SCRIPT_NAME,
        "repo_root": str(repo_root),
        "kb_root": relpath(kb_root, repo_root),
        "download_report": relpath(report_path, repo_root),
        "source_mode": source_mode,
        "dry_run": args.dry_run,
        "force": args.force,
        "marker_enabled": not args.no_marker,
        "pdf_count": len(pdfs),
        "results": [],
    }

    for pdf in pdfs:
        result = transform_pdf(
            pdf=pdf,
            repo_root=repo_root,
            force=args.force,
            marker=not args.no_marker,
            dry_run=args.dry_run,
        )
        summary["results"].append(result)

    if args.dry_run:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
        return 0

    summary_dir = kb_root / "manifests" / "pdf-transformations"
    summary_dir.mkdir(parents=True, exist_ok=True)
    summary_path = summary_dir / f"pdf-transformation-summary_{utc_stamp()}.json"
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    converted = [r for r in summary["results"] if str(r.get("status", "")).startswith("converted")]
    skipped = [r for r in summary["results"] if str(r.get("status", "")).startswith("skipped")]
    missing = [r for r in summary["results"] if r.get("status") == "missing_pdf"]

    print(f"PDFs considered: {len(pdfs)}")
    print(f"Converted: {len(converted)}")
    print(f"Skipped existing Markdown: {len(skipped)}")
    print(f"Missing PDF paths: {len(missing)}")
    print(f"Summary: {relpath(summary_path, repo_root)}")
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
