#!/usr/bin/env python3
"""Deterministic report and candidate artifact helpers for the Lika KB."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


DOMAIN_KEYWORDS = [
    "Umsatzsteuer",
    "Rechnung",
    "Kleinbetragsrechnung",
    "Verein",
    "GoBD",
    "Kassenf\u00fchrung",
    "ELSTER",
    "KSK",
    "K\u00fcnstlersozialabgabe",
    "\u00a7 50a",
    "Reverse Charge",
    "Vorverkaufsgeb\u00fchr",
    "Festveranstaltung",
    "Auslagenerstattung",
    "Verfahrensdokumentation",
]

NOISE_PHRASES = [
    "cookie",
    "cookies",
    "datenschutz",
    "privacy policy",
    "impressum",
    "newsletter",
    "subscribe",
    "follow us",
    "anzeige",
    "advertisement",
    "related articles",
    "you may also like",
    "teilen",
    "share this",
    "menu",
    "search",
    "kontakt",
    "terms",
]

SOURCE_EXTENSIONS = {".md", ".pdf", ".yaml", ".yml", ".txt"}
EXCLUDED_SUFFIXES = (".source-meta.json", ".conversion-report.json", ".marker.md")
EXCLUDED_PARTS = {"_pdf_extracted_md"}


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def timestamp() -> str:
    return now_utc().strftime("%Y%m%d_%H%M%S")


def iso_now() -> str:
    return now_utc().replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def rel_posix(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "source"


def title_from_path(path: Path) -> str:
    stem = path.stem
    return re.sub(r"[-_]+", " ", stem).strip().title()


def is_source_candidate(path: Path) -> bool:
    name = path.name
    if any(name.endswith(suffix) for suffix in EXCLUDED_SUFFIXES):
        return False
    if path.suffix.lower() not in SOURCE_EXTENSIONS:
        return False
    if any(part in EXCLUDED_PARTS or part.endswith(".marker-output") for part in path.parts):
        return False
    return True


def manifest_sources(kb_root: Path) -> list[dict]:
    with (kb_root / "manifests" / "source-manifest.json").open("r", encoding="utf-8") as handle:
        return json.load(handle).get("sources", [])


def generate_delta(kb_root: Path, stamp: str) -> dict:
    delta_dir = kb_root / "manifests" / "source-manifest-deltas"
    history_dir = kb_root / "manifests" / "source-history"
    delta_dir.mkdir(parents=True, exist_ok=True)
    history_dir.mkdir(parents=True, exist_ok=True)

    sources = manifest_sources(kb_root)
    known_paths = {source.get("source_path") for source in sources}
    known_hashes = {source.get("source_hash") for source in sources if source.get("source_hash")}
    run_id = f"lika-kb-lifecycle-{stamp}"
    scan_roots = [kb_root / "raw" / "refs", kb_root / "raw" / "notes", kb_root / "raw" / "notes" / "New_Research_Taxes_Accounting"]
    seen: set[Path] = set()
    records: list[dict] = []
    skipped_known = 0
    skipped_generated = 0
    duplicate_hashes = 0

    for scan_root in scan_roots:
        if not scan_root.exists():
            continue
        for path in sorted(scan_root.rglob("*")):
            if not path.is_file() or path in seen:
                continue
            seen.add(path)
            if not is_source_candidate(path):
                skipped_generated += 1
                continue
            source_path = rel_posix(path, kb_root)
            if source_path in known_paths:
                skipped_known += 1
                continue
            digest = sha256_file(path)
            if digest in known_hashes:
                duplicate_hashes += 1
            source_type = "note" if "/raw/notes/" in f"/{source_path}" else "ref"
            records.append(
                {
                    "source_id": slugify(Path(source_path).as_posix()),
                    "source_path": source_path,
                    "source_type": source_type,
                    "title": title_from_path(path),
                    "status": "active",
                    "source_storage_mode": "copy_into_kb",
                    "hash_algorithm": "sha256",
                    "source_hash": digest,
                    "added_at": iso_now(),
                    "ingest_status": "source_intake_only",
                    "original_source_path": "NA",
                    "no_hash_reason": "NA",
                    "derived_from": [],
                    "run_id": run_id,
                }
            )

    delta_path = delta_dir / f"source-manifest-delta_{stamp}.jsonl"
    with delta_path.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, sort_keys=True, ensure_ascii=False) + "\n")

    report = {
        "generated_at": iso_now(),
        "run_id": run_id,
        "delta_path": rel_posix(delta_path, kb_root),
        "scan_roots": [rel_posix(root, kb_root) for root in scan_roots if root.exists()],
        "records_created": len(records),
        "skipped_known_manifest_paths": skipped_known,
        "skipped_generated_sidecars": skipped_generated,
        "candidate_duplicate_hashes_against_manifest": duplicate_hashes,
        "records": records,
    }
    report_path = history_dir / f"source-manifest-delta-report_{stamp}.json"
    with report_path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(report, handle, indent=2, sort_keys=True, ensure_ascii=False)
        handle.write("\n")
    return {"delta_path": delta_path, "report_path": report_path, "summary": report}


def line_sequence_files(files: list[Path]) -> dict[tuple[str, ...], set[Path]]:
    seen_in_files: dict[tuple[str, ...], set[Path]] = defaultdict(set)
    for path in files:
        lines = [line.strip() for line in path.read_text(encoding="utf-8", errors="replace").splitlines() if line.strip()]
        for idx in range(0, max(0, len(lines) - 4)):
            seq = tuple(lines[idx : idx + 5])
            if sum(len(part) for part in seq) >= 80:
                seen_in_files[seq].add(path)
    return seen_in_files


def clutter_audit(kb_root: Path, stamp: str) -> dict:
    audit_dir = kb_root / "audit"
    log_dir = kb_root / "log"
    audit_dir.mkdir(parents=True, exist_ok=True)
    log_dir.mkdir(parents=True, exist_ok=True)
    files = [
        path
        for base in [kb_root / "raw" / "refs", kb_root / "raw" / "notes"]
        if base.exists()
        for path in sorted(base.rglob("*.md"))
        if path.is_file() and is_source_candidate(path)
    ]
    repeated_sequences = line_sequence_files(files)
    repeated_files: defaultdict[Path, int] = defaultdict(int)
    for file_set in repeated_sequences.values():
        if len(file_set) < 2:
            continue
        for path in file_set:
            repeated_files[path] += 1

    candidates: list[dict] = []
    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace")
        lower = text.lower()
        lines = [line for line in text.splitlines() if line.strip()]
        words = re.findall(r"\w+", text, flags=re.UNICODE)
        headings = [line.strip("# ").strip().lower() for line in lines if line.lstrip().startswith("#")]
        link_lines = sum(1 for line in lines if "](" in line or line.lstrip().startswith(("http://", "https://")))
        keyword_hits = sum(lower.count(keyword.lower()) for keyword in DOMAIN_KEYWORDS)
        domain_hits_per_1000 = (keyword_hits / max(1, len(words))) * 1000
        signals: list[str] = []
        if lines and link_lines / len(lines) > 0.25:
            signals.append("very_high_link_density")
        noisy_heading_count = sum(1 for heading in headings if any(phrase in heading for phrase in ["menu", "search", "contact", "newsletter", "related", "kontakt"]))
        if noisy_heading_count >= 2:
            signals.append("heading_noise_warning")
        phrase_hits = sorted({phrase for phrase in NOISE_PHRASES if phrase in lower})
        if phrase_hits:
            signals.extend([f"noise_phrase:{phrase}" for phrase in phrase_hits[:8]])
        if repeated_files[path] >= 1:
            signals.append("repeated_boilerplate_sequence")
        if len(words) >= 1500 and domain_hits_per_1000 < 3:
            signals.append("large_file_low_domain_keyword_density")
        if len(words) >= 500 and domain_hits_per_1000 < 1:
            signals.append("generic_text_warning")
        top_bottom = "\n".join(lines[:40] + lines[-40:]).lower()
        chrome_hits = sum(1 for phrase in ["menu", "kontakt", "newsletter", "datenschutz", "impressum", "search"] if phrase in top_bottom)
        if chrome_hits >= 3:
            signals.append("menu_category_footer_words_near_edges")

        score = min(100, 12 * len(signals) + min(20, int(max(0, (link_lines / max(1, len(lines)) - 0.25) * 100))))
        if score < 25:
            recommendation = "use_as_is"
            usefulness = "high" if domain_hits_per_1000 >= 5 else "unknown"
        elif score < 50:
            recommendation = "use_with_caution"
            usefulness = "medium" if domain_hits_per_1000 >= 3 else "unknown"
        elif score < 75:
            recommendation = "needs_cleaned_snapshot"
            usefulness = "medium" if domain_hits_per_1000 >= 3 else "low"
        else:
            recommendation = "exclude_from_phase1_until_review"
            usefulness = "low"
        if score == 0:
            continue
        candidates.append(
            {
                "path": rel_posix(path, kb_root),
                "clutter_score": score,
                "signals": signals,
                "estimated_usefulness": usefulness,
                "recommendation": recommendation,
                "notes": f"Deterministic signals: {len(signals)}; link lines {link_lines}/{len(lines)}; domain hits per 1000 words {domain_hits_per_1000:.2f}.",
            }
        )

    candidates.sort(key=lambda row: (-row["clutter_score"], row["path"]))
    jsonl_path = audit_dir / f"web-clutter-candidates_{stamp}.jsonl"
    with jsonl_path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in candidates:
            handle.write(json.dumps(row, sort_keys=True, ensure_ascii=False) + "\n")

    md_path = log_dir / f"web-clutter-audit_{stamp}.md"
    lines = [
        "# Web Clutter Audit",
        "",
        f"- Generated at: {iso_now()}",
        f"- Markdown files scanned: {len(files)}",
        f"- Candidates reported: {len(candidates)}",
        f"- Candidate JSONL: `{rel_posix(jsonl_path, kb_root)}`",
        "",
        "## Top candidates",
        "",
    ]
    for row in candidates[:20]:
        lines.append(f"- `{row['path']}` score={row['clutter_score']} recommendation={row['recommendation']} signals={', '.join(row['signals'][:6])}")
    lines.extend(
        [
            "",
            "## Future script improvement",
            "",
            "```yaml",
            "future_script_improvement:",
            "  add command: apex_kb.py web-clutter-audit",
            "  role: detect noisy web captures before semantic ingest",
            f"  output: audit/web-clutter-candidates_{stamp}.jsonl",
            "  non_goal: automatic deletion or semantic cleanup",
            "```",
        ]
    )
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"jsonl_path": jsonl_path, "report_path": md_path, "candidates": candidates, "files_scanned": len(files)}


def run_command(args: list[str], cwd: Path) -> dict:
    proc = subprocess.run(args, cwd=cwd, text=True, capture_output=True)
    return {
        "command": " ".join(args),
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
    }


def inventory(kb_root: Path, stamp: str) -> dict:
    log_dir = kb_root / "log"
    log_dir.mkdir(parents=True, exist_ok=True)
    paths = [
        "README.md",
        "kb-schema.md",
        "manifests/source-manifest.json",
        "manifests/downloads",
        "manifests/pdf-transformations",
        "manifests/phase0",
        "raw",
        "raw/refs",
        "raw/notes",
        "raw/notes/New_Research_Taxes_Accounting",
        "ingest-analysis",
        "wiki",
        "derived/search",
        "audit",
        "outputs/queries",
        "log",
    ]
    rows = []
    for item in paths:
        path = kb_root / item
        if path.is_dir():
            files = [child for child in path.rglob("*") if child.is_file()]
            rows.append({"path": item, "exists": True, "type": "dir", "file_count": len(files), "bytes": sum(child.stat().st_size for child in files)})
        elif path.is_file():
            rows.append({"path": item, "exists": True, "type": "file", "file_count": 1, "bytes": path.stat().st_size})
        else:
            rows.append({"path": item, "exists": False, "type": "missing", "file_count": 0, "bytes": 0})
    manifest_count = len(manifest_sources(kb_root))
    report_path = log_dir / f"lifecycle-preflight-inventory_{stamp}.md"
    lines = [
        "# Lifecycle Preflight Inventory",
        "",
        f"- Generated at: {iso_now()}",
        f"- KB root: `{kb_root.as_posix()}`",
        f"- Source manifest entries: {manifest_count}",
        "",
        "| Path | Exists | Type | Files | Bytes |",
        "|---|---:|---|---:|---:|",
    ]
    for row in rows:
        lines.append(f"| `{row['path']}` | {str(row['exists']).lower()} | {row['type']} | {row['file_count']} | {row['bytes']} |")
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"report_path": report_path, "rows": rows, "manifest_count": manifest_count}


def write_run_report(kb_root: Path, stamp: str, payload_path: Path) -> Path:
    payload = json.loads(payload_path.read_text(encoding="utf-8"))
    log_dir = kb_root / "log"
    report_path = log_dir / f"lifecycle-run-report_{stamp}.md"
    lines = [
        "# Lifecycle Run Report",
        "",
        f"- Generated at: {iso_now()}",
        f"- KB root: `{kb_root.as_posix()}`",
        "",
        "## Git state summary",
        "",
        f"- `git pull --ff-only origin main`: {payload['git_pull']}",
        f"- `git status --short` before run: {payload['git_status_initial'] or '(clean)'}",
        f"- Recent commits: {payload['git_log_summary']}",
        "",
        "## Skill/script files loaded",
        "",
        "- `.claude/skills/apex-kb/SKILL.md`",
        "- `.claude/skills/apex-kb/package-manifest.md`",
        "- `.claude/skills/apex-kb/references/kb-contract.md`",
        "- `.claude/skills/apex-kb/references/script-command-contract.md`",
        "- `.claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md`",
        "- `.claude/skills/apex-kb/references/lifecycle-state-machine.md`",
        "- `apex-meta/scripts/apex_kb.py --help`",
        "- `apex-meta/scripts/apex_kb_retrieval.py --help`",
        "",
        "## KB inventory summary",
        "",
        f"- Preflight inventory: `{payload['inventory_report']}`",
        f"- Source manifest entries before delta generation: {payload['manifest_entries_before']}",
        f"- Raw source candidate scan count: {payload['raw_source_candidates']}",
        "",
        "## Source manifest delta summary",
        "",
        f"- Delta file: `{payload['delta_path']}`",
        f"- Delta report: `{payload['delta_report_path']}`",
        f"- Delta records created: {payload['delta_records']}",
        f"- Merge dry-run: {payload['merge_dry_run']}",
        f"- Merge apply: {payload['merge_apply']}",
        "",
        "## PDF conversion state summary",
        "",
        "- Baseline summary preserved: `manifests/pdf-transformations/pdf-transformation-summary_20260629_155320.json`",
        "- Latest summary treated as current state: `manifests/pdf-transformations/pdf-transformation-summary_20260629_160032.json`",
        "- No PDF conversion rerun was performed.",
        "",
        "## Table-heavy PDF risk register",
        "",
        "- `raw/refs/IHK-Niederbayern_Checkliste-Kleinbetragsrechnungen.md`: low text volume, low heading count, table-heavy conversion warning.",
        "- `raw/refs/LfSt-Bayern_Merkblatt-Festveranstaltungen-2025.md`: table-heavy conversion warning.",
        "- `raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.md`: table-heavy conversion warning.",
        "",
        "## Web-clutter candidate summary",
        "",
        f"- Markdown files scanned: {payload['web_clutter_files_scanned']}",
        f"- Candidates written: {payload['web_clutter_candidates']}",
        f"- Candidate JSONL: `{payload['web_clutter_jsonl']}`",
        f"- Audit report: `{payload['web_clutter_report']}`",
        "",
        "## Phase 0 artifacts written",
        "",
    ]
    for artifact in payload["phase0_artifacts"]:
        lines.append(f"- `{artifact}`")
    lines.extend(
        [
            "",
            "## Index/lint/audit/status results",
            "",
        ]
    )
    for result in payload["lifecycle_results"]:
        lines.append(f"- `{result['name']}`: returncode={result['returncode']} summary={result['summary']}")
    lines.extend(
        [
            "",
            "## Files intentionally not modified",
            "",
            "- `wiki/summaries/*`",
            "- `wiki/concepts/*`",
            "- `wiki/entities/*`",
            "- `outputs/queries/*`",
            "- Apex Plan, Apex Sync, Apex Session, PreCap, FlowRecap, APSU/status-merge, and personal orchestration state.",
            "",
            "## Problems found",
            "",
        ]
    )
    if payload["problems"]:
        lines.extend(f"- {problem}" for problem in payload["problems"])
    else:
        lines.append("- No blocking deterministic preparation problem was found.")
    lines.extend(
        [
            "",
            "## Recommended deterministic script improvements",
            "",
            "```yaml",
            "future_script_improvement:",
            "  add command: apex_kb.py web-clutter-audit",
            "  role: detect noisy web captures before semantic ingest",
            f"  output: audit/web-clutter-candidates_{stamp}.jsonl",
            "  non_goal: automatic deletion or semantic cleanup",
            "```",
            "",
            "## Stop condition",
            "",
            "Stopped before LLM semantic ingest/wiki work. No wiki pages, semantic summaries, concept pages, entity pages, contradiction interpretations, query answers, or semantic audit items from claims were generated.",
            "",
            "Deterministic lifecycle preparation complete. The next step is LLM-owned Phase 1 ingest analysis. Phase 2 wiki creation remains blocked until: approve ingest",
        ]
    )
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report_path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kb-root", required=True)
    parser.add_argument("--stamp", default=timestamp())
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("inventory")
    sub.add_parser("generate-delta")
    sub.add_parser("web-clutter-audit")
    run_report_parser = sub.add_parser("run-report")
    run_report_parser.add_argument("--payload", required=True)
    args = parser.parse_args()

    kb_root = Path(args.kb_root)
    if args.command == "inventory":
        result = inventory(kb_root, args.stamp)
        print(json.dumps({"report_path": str(result["report_path"])}, indent=2))
    elif args.command == "generate-delta":
        result = generate_delta(kb_root, args.stamp)
        print(json.dumps({"delta_path": str(result["delta_path"]), "report_path": str(result["report_path"]), "records": result["summary"]["records_created"]}, indent=2))
    elif args.command == "web-clutter-audit":
        result = clutter_audit(kb_root, args.stamp)
        print(json.dumps({"jsonl_path": str(result["jsonl_path"]), "report_path": str(result["report_path"]), "candidates": len(result["candidates"]), "files_scanned": result["files_scanned"]}, indent=2))
    elif args.command == "run-report":
        print(json.dumps({"report_path": str(write_run_report(kb_root, args.stamp, Path(args.payload)))}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
