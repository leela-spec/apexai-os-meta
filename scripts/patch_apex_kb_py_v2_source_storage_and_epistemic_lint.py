#!/usr/bin/env python3
"""
patch_apex_kb_py_v2_source_storage_and_epistemic_lint.py

Deterministic patcher for Apex KB v2 repairs.

Scope:
- Target file only: apex-meta/scripts/apex_kb.py
- No network.
- No shell-out to external commands.
- No GitHub/PR/issue/comment operations.
- No semantic KB generation.
- No docs/templates/contracts patching.

Implements only:
1. source_storage_mode in preflight and manifest validation.
2. confidence / claim_label frontmatter validation in lint.

Usage:
  python scripts/patch_apex_kb_py_v2_source_storage_and_epistemic_lint.py --check
  python scripts/patch_apex_kb_py_v2_source_storage_and_epistemic_lint.py --apply
  python scripts/patch_apex_kb_py_v2_source_storage_and_epistemic_lint.py --validate
"""

from __future__ import annotations

import argparse
import ast
import datetime as dt
import difflib
import re
import shutil
import sys
from pathlib import Path


TARGET = Path("apex-meta/scripts/apex_kb.py")

CONSTANTS_ANCHOR = '''PAGE_TYPE_DIRS = {
    "summary": "wiki/summaries",
    "concept": "wiki/concepts",
    "entity": "wiki/entities",
}
'''

CONSTANTS_INSERT = '''PAGE_TYPE_DIRS = {
    "summary": "wiki/summaries",
    "concept": "wiki/concepts",
    "entity": "wiki/entities",
}

SOURCE_STORAGE_MODES = {
    "pointer_only",
    "copy_into_kb",
    "snapshot_copy",
}

ALLOWED_CONFIDENCE_VALUES = {
    "high",
    "medium",
    "low",
    "mixed",
    "unknown",
}

ALLOWED_CLAIM_LABEL_VALUES = {
    "direct_source_claim",
    "synthesis",
    "inference",
    "hypothesis",
    "contradiction",
    "open_question",
    "operator_note",
}
'''

HELPERS_INSERT = '''

def resolve_source_storage_mode(source: Path, kb_root: Path, explicit_mode: str | None) -> str:
    """Resolve source storage mode deterministically for preflight output."""
    if explicit_mode:
        return explicit_mode

    if source.exists():
        try:
            source.resolve().relative_to(Path.cwd().resolve())
            return "pointer_only"
        except ValueError:
            return "copy_into_kb"
        except OSError:
            return "copy_into_kb"

    return "copy_into_kb"


def source_storage_flags(mode: str) -> dict[str, bool]:
    return {
        "copy_required": mode == "copy_into_kb",
        "snapshot_required": mode == "snapshot_copy",
    }


def validate_manifest_storage_fields(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    """Validate source storage metadata on source manifest entries."""
    findings: list[dict[str, Any]] = []

    for index, entry in enumerate(list_sources(manifest)):
        source_label = entry.get("source_id") or entry.get("id") or f"sources[{index}]"
        mode = entry.get("source_storage_mode")

        if not mode:
            findings.append({
                "severity": "warning",
                "code": "missing_source_storage_mode",
                "source": source_label,
            })
            continue

        if mode not in SOURCE_STORAGE_MODES:
            findings.append({
                "severity": "error",
                "code": "invalid_source_storage_mode",
                "source": source_label,
                "value": mode,
                "allowed": sorted(SOURCE_STORAGE_MODES),
            })
            continue

        if not entry.get("source_hash") and not entry.get("no_hash_reason"):
            findings.append({
                "severity": "warning",
                "code": "source_ref_missing_hash_or_no_hash_reason",
                "source": source_label,
            })

        if mode == "copy_into_kb" and not entry.get("copied_to"):
            findings.append({
                "severity": "warning",
                "code": "copy_into_kb_missing_copied_to",
                "source": source_label,
            })

        if mode == "snapshot_copy" and not entry.get("snapshot_path"):
            findings.append({
                "severity": "warning",
                "code": "snapshot_copy_missing_snapshot_path",
                "source": source_label,
            })

    return findings


def validate_epistemic_frontmatter(
    fm: dict[str, str],
    rel: str,
    require_confidence: bool,
) -> tuple[list[dict[str, Any]], list[dict[str, str]], list[dict[str, str]]]:
    findings: list[dict[str, Any]] = []
    invalid_confidence_values: list[dict[str, str]] = []
    invalid_claim_label_values: list[dict[str, str]] = []

    confidence = fm.get("confidence")
    if confidence:
        if confidence not in ALLOWED_CONFIDENCE_VALUES:
            invalid_confidence_values.append({"path": rel, "value": confidence})
            findings.append({
                "severity": "warning",
                "code": "invalid_confidence_value",
                "path": rel,
                "value": confidence,
                "allowed": sorted(ALLOWED_CONFIDENCE_VALUES),
            })
    elif require_confidence:
        findings.append({
            "severity": "warning",
            "code": "missing_confidence",
            "path": rel,
            "allowed": sorted(ALLOWED_CONFIDENCE_VALUES),
        })

    claim_label = fm.get("claim_label")
    if claim_label and claim_label not in ALLOWED_CLAIM_LABEL_VALUES:
        invalid_claim_label_values.append({"path": rel, "value": claim_label})
        findings.append({
            "severity": "warning",
            "code": "invalid_claim_label_value",
            "path": rel,
            "value": claim_label,
            "allowed": sorted(ALLOWED_CLAIM_LABEL_VALUES),
        })

    return findings, invalid_confidence_values, invalid_claim_label_values
'''

CMD_PREFLIGHT = '''def cmd_preflight(args: argparse.Namespace) -> int:
    kb_root = Path(args.kb_root)
    source = Path(args.source)
    missing, findings = validate_structure(kb_root)

    source_storage_mode = resolve_source_storage_mode(source, kb_root, args.source_storage_mode)
    storage_flags = source_storage_flags(source_storage_mode)

    source_hash = None
    no_hash_reason = None
    duplicate_candidates: list[dict[str, Any]] = []

    if source.exists() and source.is_file():
        source_hash = sha256_file(source)
    elif source.exists() and source.is_dir():
        source_hash = sha256_directory(source)
    else:
        no_hash_reason = "source_missing"
        findings.append({"severity": "error", "code": "source_missing", "path": source.as_posix()})

    manifest, manifest_findings = read_manifest(kb_root)
    findings.extend(manifest_findings)

    if source_hash:
        for entry in list_sources(manifest):
            if entry.get("source_hash") == source_hash:
                duplicate_candidates.append(entry)

    analysis_path = kb_root / "ingest-analysis" / f"{args.source_slug}.analysis.md"

    status = "passed" if not any(f.get("severity") == "error" for f in findings) else "failed"
    return emit(
        {
            "artifact_name": "ingest_preflight_report",
            "status": status,
            "kb_root": kb_root.as_posix(),
            "source_path": source.as_posix(),
            "source_exists": source.exists(),
            "source_storage_mode": source_storage_mode,
            "source_hash": source_hash,
            "no_hash_reason": no_hash_reason,
            "copy_required": storage_flags["copy_required"],
            "snapshot_required": storage_flags["snapshot_required"],
            "duplicate_source_candidates": duplicate_candidates,
            "analysis_path": analysis_path.as_posix(),
            "phase_2_allowed": False,
            "required_operator_phrase": "approve ingest",
            "required_paths_missing": missing,
            "findings": findings,
        },
        args.json,
        EXIT_OK if status == "passed" else EXIT_VALIDATION_FAILURE,
    )
'''

CMD_LINT = '''def cmd_lint(args: argparse.Namespace) -> int:
    kb_root = Path(args.kb_root)
    missing, findings = validate_structure(kb_root)

    pages = collect_wiki_pages(kb_root)
    slugs = {p.stem for p in pages}
    broken_links: list[dict[str, str]] = []
    missing_source_pointers: list[str] = []
    malformed_frontmatter: list[str] = []
    invalid_confidence_values: list[dict[str, str]] = []
    invalid_claim_label_values: list[dict[str, str]] = []

    for page in pages:
        rel = page.relative_to(kb_root).as_posix()
        text = page.read_text(encoding="utf-8", errors="replace")
        fm, _ = extract_frontmatter(text)

        is_index = page.name == "index.md"

        if not is_index and not fm:
            malformed_frontmatter.append(rel)
            findings.append({"severity": "warning", "code": "missing_frontmatter", "path": rel})

        if fm:
            epistemic_findings, bad_confidence, bad_claim_labels = validate_epistemic_frontmatter(
                fm=fm,
                rel=rel,
                require_confidence=not is_index,
            )
            findings.extend(epistemic_findings)
            invalid_confidence_values.extend(bad_confidence)
            invalid_claim_label_values.extend(bad_claim_labels)

        if not is_index and "source_refs" not in text and "source_pointers" not in text:
            missing_source_pointers.append(rel)
            findings.append({"severity": "warning", "code": "missing_source_pointer", "path": rel})

        for link in extract_wikilinks(text):
            if link not in slugs:
                broken_links.append({"from": rel, "to": link})
                findings.append({"severity": "warning", "code": "broken_wikilink", "from": rel, "to": link})

    status = "passed" if not any(f.get("severity") == "error" for f in findings) else "failed"
    exit_code = EXIT_OK if status == "passed" and not findings else (EXIT_FLAGS if status == "passed" else EXIT_VALIDATION_FAILURE)

    return emit(
        {
            "artifact_name": "lint_report",
            "status": status,
            "kb_root": kb_root.as_posix(),
            "checks_run": args.check,
            "missing_required_paths": missing,
            "malformed_frontmatter": malformed_frontmatter,
            "broken_links": broken_links,
            "orphan_pages": build_machine_index(kb_root)["orphan_pages"] if (kb_root / "wiki").exists() else [],
            "missing_source_pointers": missing_source_pointers,
            "invalid_confidence_values": invalid_confidence_values,
            "invalid_claim_label_values": invalid_claim_label_values,
            "stale_index": False,
            "manifest_issues": [f for f in findings if "manifest" in f.get("code", "")],
            "audit_shape_issues": [],
            "findings": findings,
        },
        args.json,
        exit_code,
    )
'''

CMD_MANIFEST = '''def cmd_manifest(args: argparse.Namespace) -> int:
    kb_root = Path(args.kb_root)
    manifest_path = kb_root / "manifests" / "source-manifest.json"
    manifest, findings = read_manifest(kb_root)
    findings.extend(validate_manifest_storage_fields(manifest))

    if args.validate_only or not args.allow_write:
        status = "passed" if not any(f.get("severity") == "error" for f in findings) else "failed"
        return emit(
            {
                "artifact_name": "manifest_report",
                "status": status,
                "kb_root": kb_root.as_posix(),
                "manifest_path": manifest_path.as_posix(),
                "source_entries_count": len(list_sources(manifest)),
                "validated_storage_fields": [
                    "source_storage_mode",
                    "source_hash",
                    "no_hash_reason",
                    "copied_to",
                    "snapshot_path",
                ],
                "changed_entries": [],
                "findings": findings,
                "writes_performed": False,
            },
            args.json,
            EXIT_OK if status == "passed" else EXIT_VALIDATION_FAILURE,
        )

    if not manifest:
        manifest = empty_manifest()
    manifest["updated_at"] = utc_now()
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\\n", encoding="utf-8")

    return emit(
        {
            "artifact_name": "manifest_report",
            "status": "passed",
            "kb_root": kb_root.as_posix(),
            "manifest_path": manifest_path.as_posix(),
            "source_entries_count": len(list_sources(manifest)),
            "validated_storage_fields": [
                "source_storage_mode",
                "source_hash",
                "no_hash_reason",
                "copied_to",
                "snapshot_path",
            ],
            "changed_entries": [],
            "writes_performed": True,
            "findings": findings,
        },
        args.json,
        EXIT_OK,
    )
'''

PREFLIGHT_PARSER_OLD = '''    p = sub.add_parser("preflight", help="Run ingest preflight")
    p.add_argument("--kb-root", required=True)
    p.add_argument("--source", required=True)
    p.add_argument("--source-slug", required=True)
    p.set_defaults(func=cmd_preflight)
'''

PREFLIGHT_PARSER_NEW = '''    p = sub.add_parser("preflight", help="Run ingest preflight")
    p.add_argument("--kb-root", required=True)
    p.add_argument("--source", required=True)
    p.add_argument("--source-slug", required=True)
    p.add_argument(
        "--source-storage-mode",
        choices=sorted(SOURCE_STORAGE_MODES),
        default=None,
        help="How this source is stored: pointer_only, copy_into_kb, or snapshot_copy",
    )
    p.set_defaults(func=cmd_preflight)
'''


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(2)


def read_target() -> str:
    if not TARGET.exists():
        fail(f"target file not found: {TARGET}")
    return TARGET.read_text(encoding="utf-8")


def find_function_block(text: str, name: str) -> tuple[int, int, str]:
    pattern = re.compile(rf"^def {re.escape(name)}\(.*?^def ", re.M | re.S)
    match = pattern.search(text)
    if match:
        start = match.start()
        end = match.end() - len("def ")
        return start, end, text[start:end]

    pattern_last = re.compile(rf"^def {re.escape(name)}\(.*", re.M | re.S)
    match_last = pattern_last.search(text)
    if match_last:
        start = match_last.start()
        return start, len(text), text[start:]

    fail(f"function anchor not found: {name}")


def replace_function(text: str, name: str, replacement: str) -> str:
    start, end, old = find_function_block(text, name)
    if old.count(f"def {name}") != 1:
        fail(f"ambiguous function block for: {name}")
    return text[:start] + replacement.rstrip() + "\n\n" + text[end:]


def replace_exact_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        fail(f"expected exactly one {label} anchor; found {count}")
    return text.replace(old, new, 1)


def insert_helpers(text: str) -> str:
    if "def resolve_source_storage_mode(" in text:
        return text

    start, end, block = find_function_block(text, "list_sources")
    if block.count("def list_sources") != 1:
        fail("ambiguous list_sources block")
    return text[:end] + HELPERS_INSERT + text[end:]


def patch_text(original: str) -> str:
    text = original

    if "SOURCE_STORAGE_MODES =" not in text:
        text = replace_exact_once(text, CONSTANTS_ANCHOR, CONSTANTS_INSERT, "PAGE_TYPE_DIRS constants")

    text = insert_helpers(text)

    text = replace_function(text, "cmd_preflight", CMD_PREFLIGHT)
    text = replace_function(text, "cmd_lint", CMD_LINT)
    text = replace_function(text, "cmd_manifest", CMD_MANIFEST)

    if "--source-storage-mode" not in text:
        text = replace_exact_once(text, PREFLIGHT_PARSER_OLD, PREFLIGHT_PARSER_NEW, "preflight parser block")

    return text


def validate_text(text: str) -> None:
    required = [
        "SOURCE_STORAGE_MODES =",
        "ALLOWED_CONFIDENCE_VALUES =",
        "ALLOWED_CLAIM_LABEL_VALUES =",
        "def resolve_source_storage_mode(",
        "def validate_manifest_storage_fields(",
        "def validate_epistemic_frontmatter(",
        "--source-storage-mode",
        '"source_storage_mode": source_storage_mode',
        '"copy_required": storage_flags["copy_required"]',
        '"snapshot_required": storage_flags["snapshot_required"]',
        '"invalid_confidence_values": invalid_confidence_values',
        '"invalid_claim_label_values": invalid_claim_label_values',
        '"validated_storage_fields": [',
    ]

    for needle in required:
        if needle not in text:
            fail(f"validation failed; missing required marker: {needle}")

    if text.count("def cmd_preflight(") != 1:
        fail("validation failed; cmd_preflight count is not 1")
    if text.count("def cmd_lint(") != 1:
        fail("validation failed; cmd_lint count is not 1")
    if text.count("def cmd_manifest(") != 1:
        fail("validation failed; cmd_manifest count is not 1")

    try:
        ast.parse(text)
    except SyntaxError as exc:
        fail(f"validation failed; patched Python is not syntactically valid: {exc}")


def print_diff(original: str, patched: str) -> None:
    diff = difflib.unified_diff(
        original.splitlines(keepends=True),
        patched.splitlines(keepends=True),
        fromfile=str(TARGET),
        tofile=f"{TARGET} [patched]",
    )
    sys.stdout.writelines(diff)


def backup_target() -> Path:
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup = TARGET.with_suffix(TARGET.suffix + f".bak.{stamp}")
    shutil.copy2(TARGET, backup)
    return backup


def main() -> int:
    parser = argparse.ArgumentParser(description="Patch apex_kb.py for v2 source storage and epistemic lint.")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Preview patch and validate patched text without writing.")
    mode.add_argument("--apply", action="store_true", help="Apply patch with backup.")
    mode.add_argument("--validate", action="store_true", help="Validate the current target file after patching.")
    args = parser.parse_args()

    original = read_target()

    if args.validate:
        validate_text(original)
        print(f"VALID: {TARGET}")
        return 0

    patched = patch_text(original)
    validate_text(patched)

    if patched == original:
        print("NO CHANGE: target already appears patched and valid.")
        return 0

    print_diff(original, patched)

    if args.check:
        print("\nCHECK PASSED: patch can be applied deterministically.")
        return 0

    if args.apply:
        backup = backup_target()
        TARGET.write_text(patched, encoding="utf-8", newline="\n")
        print(f"\nAPPLIED: {TARGET}")
        print(f"BACKUP:  {backup}")
        return 0

    fail("unreachable mode state")


if __name__ == "__main__":
    raise SystemExit(main())
