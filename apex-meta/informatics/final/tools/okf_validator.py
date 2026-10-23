#!/usr/bin/env python3
"""
okf_validator.py — Deterministic OKF v0.2 and Apex Informatics Profile Validator.

Enforces tri-class diagnostics:
1. OKF (Errors): Upstream OKF v0.2 specification compliance.
2. APEX_PROFILE (Errors): Apex OS repository profile rules.
3. ADVISORY (Warnings): Stylistic and writing-doctrine recommendations.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


@dataclass
class Finding:
    severity: str  # 'OKF_ERROR', 'APEX_PROFILE_ERROR', 'ADVISORY_WARNING'
    path: str
    rule: str
    message: str
    line: Optional[int] = None


@dataclass
class ValidationReport:
    target: str
    okf_errors: int
    apex_profile_errors: int
    advisory_warnings: int
    findings: List[Finding]

    @property
    def passed(self) -> bool:
        return self.okf_errors == 0 and self.apex_profile_errors == 0


def parse_frontmatter(content: str) -> Tuple[Optional[Dict[str, Any]], str, Optional[str]]:
    """
    Parses frontmatter from Markdown text.
    Returns (frontmatter_dict, body_text, error_message).
    """
    if not content.startswith("---"):
        return None, content, "No YAML frontmatter header ('---') found at start of file"

    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, content, "Unterminated YAML frontmatter ('---' closing delimiter missing)"

    fm_raw = parts[1]
    body = parts[2]

    # Lightweight deterministic YAML parser for flat/nested maps without external PyYAML dependency
    fm_dict: Dict[str, Any] = {}
    for line_num, line in enumerate(fm_raw.splitlines(), start=2):
        line_clean = line.strip()
        if not line_clean or line_clean.startswith("#"):
            continue
        if ":" not in line_clean:
            return None, content, f"Malformed frontmatter on line {line_num}: missing ':'"

        key, val = line_clean.split(":", 1)
        key = key.strip()
        val = val.strip()

        # Handle simple quotes
        if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
            val = val[1:-1]
        elif val.startswith("[") and val.endswith("]"):
            # Simple list
            items = [item.strip().strip("'\"") for item in val[1:-1].split(",") if item.strip()]
            val = items

        fm_dict[key] = val

    return fm_dict, body, None


def extract_links(markdown_text: str) -> List[str]:
    """Extracts relative Markdown links [text](target.md) from text, ignoring URLs."""
    links = []
    # Match markdown link target [text](link)
    matches = re.findall(r"\[.*?\]\((.*?)\)", markdown_text)
    for m in matches:
        link = m.split("#")[0].strip()
        if link and not link.startswith(("http://", "https://", "mailto:", "#")):
            links.append(link)
    return links


def check_writing_style(path: str, body_text: str) -> List[Finding]:
    """Applies advisory technical prose checks (sentence length, etc.) with strict exemptions."""
    findings = []
    # Remove fenced code blocks
    text_no_code = re.sub(r"```[\s\S]*?```", "", body_text)
    # Remove inline code
    text_no_code = re.sub(r"`.*?`", "", text_no_code)
    # Remove markdown tables
    text_no_tables = "\n".join([l for l in text_no_code.splitlines() if not l.strip().startswith("|")])

    # Split into sentences (simple period/question/exclamation followed by space or newline)
    sentences = re.split(r"(?<=[.!?])\s+", text_no_tables)
    for s in sentences:
        s_clean = s.strip()
        if not s_clean or s_clean.startswith(("#", "-", "*", ">")):
            continue
        words = [w for w in s_clean.split() if w]
        # Ignore sentences that are mostly URLs or math formulas
        if any(w.startswith("http") or "$" in w for w in words):
            continue

        if len(words) > 30:
            findings.append(
                Finding(
                    severity="ADVISORY_WARNING",
                    path=path,
                    rule="STE-SENTENCE-LENGTH",
                    message=f"Sentence exceeds recommended limit ({len(words)} words > 25-30 words): '{s_clean[:60]}...'",
                )
            )

    return findings


def validate_bundle(target_dir: str) -> ValidationReport:
    """Validates an OKF bundle directory according to OKF v0.2 and Apex Profile rules."""
    target_path = Path(target_dir).resolve()
    if not target_path.is_dir():
        return ValidationReport(
            target=str(target_dir),
            okf_errors=1,
            apex_profile_errors=0,
            advisory_warnings=0,
            findings=[
                Finding(
                    severity="OKF_ERROR",
                    path=str(target_dir),
                    rule="BUNDLE-EXISTS",
                    message=f"Target bundle directory does not exist: {target_dir}",
                )
            ],
        )

    findings: List[Finding] = []
    root_index = target_path / "index.md"

    # 1. Root index.md validation
    if not root_index.is_file():
        findings.append(
            Finding(
                severity="OKF_ERROR",
                path="index.md",
                rule="OKF-ROOT-INDEX-EXISTS",
                message="Bundle root index.md does not exist",
            )
        )
    else:
        content = root_index.read_text(encoding="utf-8", errors="replace")
        fm, body, err = parse_frontmatter(content)
        if err:
            findings.append(
                Finding(
                    severity="OKF_ERROR",
                    path="index.md",
                    rule="OKF-INDEX-FRONTMATTER",
                    message=f"Invalid root index.md frontmatter: {err}",
                )
            )
        elif not fm or fm.get("okf_version") != "0.2":
            findings.append(
                Finding(
                    severity="OKF_ERROR",
                    path="index.md",
                    rule="OKF-VERSION-DECLARATION",
                    message="Root index.md must declare okf_version: '0.2'",
                )
            )

        # Apex profile check: verify links in root index resolve to existing files
        links = extract_links(content)
        for link in links:
            resolved = (target_path / link).resolve()
            if not resolved.exists():
                findings.append(
                    Finding(
                        severity="APEX_PROFILE_ERROR",
                        path="index.md",
                        rule="APEX-LINK-INTEGRITY",
                        message=f"Governed index link does not resolve to target file: '{link}'",
                    )
                )

    # 2. Iterate through concept files inside the bundle (excluding .git and sub-bundles)
    durable_ids: Dict[str, str] = {}

    for root, dirs, files in os.walk(target_path):
        # Exclude subdirectories that are separate bundles (have their own index.md)
        current_dir = Path(root)
        if current_dir != target_path and (current_dir / "index.md").exists():
            dirs.clear()  # Do not recurse into separate sub-bundle
            continue

        for f in files:
            if not f.endswith(".md"):
                continue

            file_path = current_dir / f
            rel_path = file_path.relative_to(target_path).as_posix()

            # Reserved files
            if rel_path == "index.md":
                continue
            if rel_path == "log.md":
                # Reserved changelog
                continue

            content = file_path.read_text(encoding="utf-8", errors="replace")

            # Check pseudo-OKF drift within governed target
            if f.endswith(".okf.md") and not content.startswith("---"):
                findings.append(
                    Finding(
                        severity="APEX_PROFILE_ERROR",
                        path=rel_path,
                        rule="APEX-PSEUDO-OKF-DRIFT",
                        message="File uses '.okf.md' extension but lacks real YAML frontmatter",
                    )
                )

            fm, body, err = parse_frontmatter(content)
            if err:
                findings.append(
                    Finding(
                        severity="OKF_ERROR",
                        path=rel_path,
                        rule="OKF-FRONTMATTER-PARSE",
                        message=f"YAML frontmatter error: {err}",
                    )
                )
                continue

            if not fm:
                findings.append(
                    Finding(
                        severity="OKF_ERROR",
                        path=rel_path,
                        rule="OKF-FRONTMATTER-MISSING",
                        message="Concept file must have YAML frontmatter",
                    )
                )
                continue

            # OKF rule: type is required and non-empty
            concept_type = fm.get("type")
            if not concept_type or not str(concept_type).strip():
                findings.append(
                    Finding(
                        severity="OKF_ERROR",
                        path=rel_path,
                        rule="OKF-TYPE-REQUIRED",
                        message="Frontmatter must contain a non-empty 'type' field",
                    )
                )

            # Apex profile check: unique durable ID
            if "id" in fm:
                doc_id = str(fm["id"]).strip()
                if doc_id in durable_ids:
                    findings.append(
                        Finding(
                            severity="APEX_PROFILE_ERROR",
                            path=rel_path,
                            rule="APEX-UNIQUE-DURABLE-ID",
                            message=f"Duplicate durable ID '{doc_id}' (previously defined in '{durable_ids[doc_id]}')",
                        )
                    )
                else:
                    durable_ids[doc_id] = rel_path

            # Advisory writing checks
            advisories = check_writing_style(rel_path, body)
            findings.extend(advisories)

    okf_errors = sum(1 for f in findings if f.severity == "OKF_ERROR")
    apex_profile_errors = sum(1 for f in findings if f.severity == "APEX_PROFILE_ERROR")
    advisory_warnings = sum(1 for f in findings if f.severity == "ADVISORY_WARNING")

    return ValidationReport(
        target=str(target_dir),
        okf_errors=okf_errors,
        apex_profile_errors=apex_profile_errors,
        advisory_warnings=advisory_warnings,
        findings=findings,
    )


def main():
    parser = argparse.ArgumentParser(description="Deterministic OKF v0.2 & Apex Profile Validator")
    parser.add_argument("--target", required=True, help="Target OKF bundle directory")
    parser.add_argument("--json", action="store_true", help="Output report in JSON format")
    args = parser.parse_args()

    report = validate_bundle(args.target)

    if args.json:
        print(json.dumps(asdict(report), indent=2))
    else:
        print("=" * 60)
        print(f"OKF Validator Report for: {report.target}")
        print("=" * 60)
        print(f"Summary: OKF Errors: {report.okf_errors} | Apex Profile Errors: {report.apex_profile_errors} | Advisories: {report.advisory_warnings}")
        print("-" * 60)
        if report.findings:
            for f in report.findings:
                print(f"[{f.severity}] {f.path}: {f.rule} — {f.message}")
        else:
            print("All checks passed cleanly with 0 errors and 0 warnings.")
        print("=" * 60)

    sys.exit(0 if report.passed else 1)


if __name__ == "__main__":
    main()
