#!/usr/bin/env python3
"""
patch_apex_kb_hardening.py

Deterministic anchored search/replace patch script for hardening apex-kb.

Safety model:
- dry-run is the default
- --apply is required to write changes
- --verify checks whether each active patch is pending/applied/conflicted
- exact text anchors must match exactly once unless expected_count says otherwise
- no git add/commit/push/reset/branch operations are ever executed
- only an explicit allowlist of package/script files may be modified
- optional reports are written under _reports/

Run from repo root:
  python scripts/patch_apex_kb_hardening.py --dry-run
  python scripts/patch_apex_kb_hardening.py --apply --write-report
  python scripts/patch_apex_kb_hardening.py --verify --write-report
"""

from __future__ import annotations

import argparse
import dataclasses
import datetime as dt
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Iterable, Literal

Mode = Literal["dry-run", "apply", "verify"]

REPORT_JSON = Path("_reports/apex-kb-hardening-patch-report.json")
REPORT_MD = Path("_reports/apex-kb-hardening-patch-report.md")

ALLOWLIST = {
    Path(".claude/skills/apex-kb/SKILL.md"),
    Path(".claude/skills/apex-kb/package-manifest.md"),
    Path(".claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md"),
    Path(".claude/skills/apex-kb/references/kb-contract.md"),
    Path(".claude/skills/apex-kb/templates/ingest-analysis-template.md"),
    Path("apex-meta/scripts/apex_kb.py"),
}

FORBIDDEN_PREFIXES = (
    Path("apex-meta/kb/claude-skill-design"),
    Path("source-knowledge"),
    Path("FutureDevelopments&Research"),
    Path("ApexDefinition&OldVersions"),
    Path("_verification"),
)

DEFERRED_PATCHES = [
    {
        "id": "G4-DEFER-STALE-INDEX-HASH",
        "group": "group_4_stale_index",
        "target_files": [
            "apex-meta/scripts/apex_kb.py",
            ".claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md",
        ],
        "status": "deferred",
        "reason": (
            "Stale-index behavior is a script-behavior change. This script records the gap but does not "
            "patch it until an explicit deterministic index freshness contract is approved. Current apex_kb.py "
            "reports stale_index=False and stale_index_hash=NA, so the weakness is real but should not be "
            "changed through an unreviewed broad code edit."
        ),
        "recommendation": "Add a later exact patch that stores and compares a deterministic wiki page content hash in the machine index.",
    },
    {
        "id": "G5-DEFER-GOLDEN-FIXTURE",
        "group": "group_5_fixture_plan",
        "target_files": [
            "apex-meta/tests/apex-kb/**",
            "apex-meta/kb/_fixtures/apex-kb-golden/**",
        ],
        "status": "deferred",
        "reason": (
            "The handover allows optional isolated tests/fixtures only if justified. This patch pass touches no "
            "optional fixture paths to keep unrelated changes out of the first hardening patch."
        ),
        "recommendation": "Create fixture/test files in a separate reviewable patch after the document/script parity pass lands.",
    },
]


@dataclasses.dataclass(frozen=True)
class Patch:
    id: str
    group: str
    file: Path
    description: str
    old: str
    new: str
    expected_count: int = 1
    risk: int = 50
    impact: int = 50
    evidence: int = 50


@dataclasses.dataclass
class PatchResult:
    id: str
    group: str
    file: str
    description: str
    status: str
    old_match_count: int
    new_match_count: int
    changed: bool
    old_sha256: str | None
    new_sha256: str | None
    risk: int
    impact: int
    evidence: int
    message: str = ""


class PatchError(RuntimeError):
    pass


def normalize_path(path: Path) -> Path:
    path_text = path.as_posix()
    if path_text.startswith("./"):
        path_text = path_text[2:]
    return Path(path_text)


def ensure_allowed_target(path: Path) -> None:
    normalized = normalize_path(path)
    if normalized not in ALLOWLIST:
        raise PatchError(f"Unexpected target file outside allowlist: {normalized}")
    for prefix in FORBIDDEN_PREFIXES:
        try:
            normalized.relative_to(prefix)
        except ValueError:
            continue
        raise PatchError(f"Forbidden target path: {normalized}")


def run_git(args: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", *args], text=True, capture_output=True, check=check)


def repo_root() -> Path:
    try:
        proc = run_git(["rev-parse", "--show-toplevel"])
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        raise PatchError("Not inside a Git repository, or git is unavailable.") from exc
    return Path(proc.stdout.strip())


def current_head() -> str:
    try:
        return run_git(["rev-parse", "HEAD"]).stdout.strip()
    except Exception:
        return "UNKNOWN"


def current_branch() -> str:
    try:
        return run_git(["branch", "--show-current"]).stdout.strip() or "DETACHED"
    except Exception:
        return "UNKNOWN"


def dirty_target_files(targets: Iterable[Path]) -> list[str]:
    args = ["diff", "--name-only", "--", *[p.as_posix() for p in targets]]
    proc = run_git(args, check=False)
    if proc.returncode not in (0, 1):
        raise PatchError(f"git diff failed: {proc.stderr.strip()}")
    return [line.strip() for line in proc.stdout.splitlines() if line.strip()]


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def apply_one_patch(text: str, patch: Patch) -> tuple[str, int, int, bool]:
    old_count = text.count(patch.old)
    new_count = text.count(patch.new)
    if old_count != patch.expected_count:
        raise PatchError(
            f"{patch.id}: expected {patch.expected_count} old anchor match(es), found {old_count}. "
            f"New-anchor count is {new_count}. Refusing partial or duplicate patch."
        )
    updated = text.replace(patch.old, patch.new, patch.expected_count)
    return updated, old_count, updated.count(patch.new), updated != text


def verify_one_patch(text: str, patch: Patch) -> tuple[str, int, int, bool, str]:
    old_count = text.count(patch.old)
    new_count = text.count(patch.new)
    if old_count == patch.expected_count and new_count == 0:
        return "pending", old_count, new_count, False, "Old anchor is present exactly as expected."
    if old_count == 0 and new_count == patch.expected_count:
        return "applied", old_count, new_count, False, "New anchor is present exactly as expected."
    if old_count == 0 and new_count == 0:
        return "missing", old_count, new_count, False, "Neither old nor new anchor is present."
    return "conflicted", old_count, new_count, False, "Unexpected old/new anchor counts."


def build_report(results: list[PatchResult], mode: Mode) -> dict[str, object]:
    changed_files = sorted({r.file for r in results if r.changed})
    statuses: dict[str, int] = {}
    for result in results:
        statuses[result.status] = statuses.get(result.status, 0) + 1
    return {
        "artifact_name": "apex_kb_hardening_patch_report",
        "generated_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "mode": mode,
        "repo_head": current_head(),
        "repo_branch": current_branch(),
        "active_patch_count": len(results),
        "status_counts": statuses,
        "changed_files": changed_files,
        "allowlist": sorted(p.as_posix() for p in ALLOWLIST),
        "deferred_patches": DEFERRED_PATCHES,
        "results": [dataclasses.asdict(r) for r in results],
    }


def write_reports(report: dict[str, object]) -> None:
    REPORT_JSON.parent.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = [
        "# Apex KB Hardening Patch Report",
        "",
        f"- mode: `{report['mode']}`",
        f"- repo_head: `{report['repo_head']}`",
        f"- repo_branch: `{report['repo_branch']}`",
        f"- active_patch_count: `{report['active_patch_count']}`",
        "",
        "## Changed Files",
    ]
    changed_files = report.get("changed_files", [])
    if changed_files:
        lines.extend(f"- `{path}`" for path in changed_files)  # type: ignore[arg-type]
    else:
        lines.append("- none")
    lines.extend(["", "## Active Patch Results", "", "| ID | File | Status | Changed | Old matches | New matches |", "|---|---|---:|---:|---:|---:|"])
    for item in report["results"]:  # type: ignore[index]
        lines.append(
            f"| `{item['id']}` | `{item['file']}` | `{item['status']}` | `{item['changed']}` | "
            f"{item['old_match_count']} | {item['new_match_count']} |"
        )
    lines.extend(["", "## Deferred Patches", ""])
    for item in report["deferred_patches"]:  # type: ignore[index]
        lines.append(f"- `{item['id']}` — {item['reason']}")
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


PATCHES: list[Patch] = [
    Patch(
        id="G1-KB-CONTRACT-DATA-ROOT-REFLOW",
        group="group_1_docs_readability",
        file=Path(".claude/skills/apex-kb/references/kb-contract.md"),
        description="Reformat compressed data_root_contract block into readable YAML.",
        risk=35,
        impact=88,
        evidence=92,
        old='''data_root_contract:  root_template: "apex-meta/kb/<kb-slug>/"  required_root_files:    - path: "README.md"      role: "Human orientation for this KB instance."    - path: "kb-schema.md"      role: "KB-local schema and operating policy. Replaces blueprint CLAUDE.md inside KB roots."  required_directories:    raw:      path: "raw/"      role: "Immutable or pointer-preserved source intake."      children:        - "articles/"        - "papers/"        - "notes/"        - "refs/"    ingest_analysis:      path: "ingest-analysis/"      role: "Phase 1 ingest analysis outputs before operator approval."    wiki:      path: "wiki/"      role: "Compiled AI-consumable knowledge pages."      children:        - "index.md"        - "concepts/"        - "entities/"        - "summaries/"    manifests:      path: "manifests/"      role: "Source manifest, hash records, and deterministic state metadata."      required_files:        - "source-manifest.json"    audit:      path: "audit/"      role: "Open human feedback, correction, contradiction, and quality items."      children:        - "resolved/"    outputs:      path: "outputs/"      role: "Saved query outputs and reusable synthesis artifacts."      children:        - "queries/"    log:      path: "log/"      role: "Operation history and durable maintenance notes."  forbidden_root_files:    - path: "CLAUDE.md"      reason: "Reserved Claude Code root-context convention; KB-local schema must be kb-schema.md."    - path: "SKILL.md"      reason: "Skill entrypoint belongs in .claude/skills/apex-kb/, not in a KB data root."''',
        new='''data_root_contract:
  root_template: "apex-meta/kb/<kb-slug>/"
  required_root_files:
    - path: "README.md"
      role: "Human orientation for this KB instance."
    - path: "kb-schema.md"
      role: "KB-local schema and operating policy. Replaces blueprint CLAUDE.md inside KB roots."
  required_directories:
    raw:
      path: "raw/"
      role: "Immutable or pointer-preserved source intake."
      children:
        - "articles/"
        - "papers/"
        - "notes/"
        - "refs/"
    ingest_analysis:
      path: "ingest-analysis/"
      role: "Phase 1 ingest analysis outputs before operator approval."
    wiki:
      path: "wiki/"
      role: "Compiled AI-consumable knowledge pages."
      children:
        - "index.md"
        - "concepts/"
        - "entities/"
        - "summaries/"
    manifests:
      path: "manifests/"
      role: "Source manifest, hash records, and deterministic state metadata."
      required_files:
        - "source-manifest.json"
    audit:
      path: "audit/"
      role: "Open human feedback, correction, contradiction, and quality items."
      children:
        - "resolved/"
    outputs:
      path: "outputs/"
      role: "Saved query outputs and reusable synthesis artifacts."
      children:
        - "queries/"
    log:
      path: "log/"
      role: "Operation history and durable maintenance notes."
  forbidden_root_files:
    - path: "CLAUDE.md"
      reason: "Reserved Claude Code root-context convention; KB-local schema must be kb-schema.md."
    - path: "SKILL.md"
      reason: "Skill entrypoint belongs in .claude/skills/apex-kb/, not in a KB data root."''',
    ),
    Patch(
        id="G1-KB-CONTRACT-KB-SCHEMA-REFLOW",
        group="group_1_docs_readability",
        file=Path(".claude/skills/apex-kb/references/kb-contract.md"),
        description="Reformat compressed kb_schema_contract block into readable YAML.",
        risk=35,
        impact=88,
        evidence=92,
        old='''kb_schema_contract:  file: "apex-meta/kb/<kb-slug>/kb-schema.md"  role: "KB-local schema, authority, language, taxonomy, and operator-review policy."  required_fields:    kb_topic_title:      type: string      required: true      purpose: "Human-readable topic or domain represented by this KB."    kb_source_authority_list:      type: list      required: true      purpose: "Ordered source-authority rules for resolving conflicts."    kb_concept_taxonomy_top_level:      type: list      required: true      purpose: "Top-level concept buckets used to organize concept pages."    kb_language_policy:      type: string_or_map      required: true      purpose: "Defines output language, source-language handling, and translation behavior."    kb_operator_review_policy:      type: map      required: true      purpose: "Defines when Phase 1, contradictions, source conflicts, and audit items require operator review."  must_not_contain:    - repo_global_claude_instructions    - model_identity_rules    - project_wide_agent_behavior    - unrelated_apex_package_rules''',
        new='''kb_schema_contract:
  file: "apex-meta/kb/<kb-slug>/kb-schema.md"
  role: "KB-local schema, authority, language, taxonomy, and operator-review policy."
  required_fields:
    kb_topic_title:
      type: string
      required: true
      purpose: "Human-readable topic or domain represented by this KB."
    kb_source_authority_list:
      type: list
      required: true
      purpose: "Ordered source-authority rules for resolving conflicts."
    kb_concept_taxonomy_top_level:
      type: list
      required: true
      purpose: "Top-level concept buckets used to organize concept pages."
    kb_language_policy:
      type: string_or_map
      required: true
      purpose: "Defines output language, source-language handling, and translation behavior."
    kb_operator_review_policy:
      type: map
      required: true
      purpose: "Defines when Phase 1, contradictions, source conflicts, and audit items require operator review."
  must_not_contain:
    - repo_global_claude_instructions
    - model_identity_rules
    - project_wide_agent_behavior
    - unrelated_apex_package_rules''',
    ),
    Patch(
        id="G1-KB-CONTRACT-SOURCE-POLICY-REFLOW",
        group="group_1_docs_readability",
        file=Path(".claude/skills/apex-kb/references/kb-contract.md"),
        description="Reformat compressed source_policy block into readable YAML.",
        risk=35,
        impact=88,
        evidence=92,
        old='''source_policy:  raw_sources_are_immutable: true  preserve_exact_source_filename: true  preserve_exact_source_path: true  source_pointer_required_on_generated_pages: true  source_manifest_required: true  source_hash_required_when_possible: true  accepted_source_forms:    local_markdown_or_text:      action: "Copy or preserve under raw/ with exact filename."    local_large_or_binary_file:      action: "Create pointer reference under raw/refs/ with path, metadata, and operator-provided context."    url_or_external_reference:      action: "Store as source pointer only unless operator supplies local content."    prior_kb_page:      action: "Treat as compiled context, not raw source."  forbidden_source_behavior:    - infer_content_from_filename_only    - treat_missing_source_as_verified    - overwrite_raw_source_without_operator_instruction    - erase_old_source_identity_on_reingest    - silently_collapse_conflicting_sources''',
        new='''source_policy:
  raw_sources_are_immutable: true
  preserve_exact_source_filename: true
  preserve_exact_source_path: true
  source_pointer_required_on_generated_pages: true
  source_manifest_required: true
  source_hash_required_when_possible: true
  accepted_source_forms:
    local_markdown_or_text:
      action: "Copy or preserve under raw/ with exact filename."
    local_large_or_binary_file:
      action: "Create pointer reference under raw/refs/ with path, metadata, and operator-provided context."
    url_or_external_reference:
      action: "Store as source pointer only unless operator supplies local content."
    prior_kb_page:
      action: "Treat as compiled context, not raw source."
  forbidden_source_behavior:
    - infer_content_from_filename_only
    - treat_missing_source_as_verified
    - overwrite_raw_source_without_operator_instruction
    - erase_old_source_identity_on_reingest
    - silently_collapse_conflicting_sources''',
    ),
    Patch(
        id="G2-PYTHON-CLAIM-LABEL-VOCABULARY",
        group="group_2_claim_labels",
        file=Path("apex-meta/scripts/apex_kb.py"),
        description="Align Python claim_label vocabulary with SKILL.md and operation rules.",
        risk=42,
        impact=94,
        evidence=95,
        old='''ALLOWED_CLAIM_LABEL_VALUES = {
    "direct_source_claim",
    "synthesis",
    "inference",
    "hypothesis",
    "contradiction",
    "open_question",
    "operator_note",
}''',
        new='''ALLOWED_CLAIM_LABEL_VALUES = {
    "raw_source",
    "source_backed_summary",
    "behavioral_inference",
    "working_hypothesis",
    "operator_question",
    "practitioner_question",
}''',
    ),
    Patch(
        id="G2-TEMPLATE-CLAIM-LABEL-FIELD",
        group="group_2_claim_labels",
        file=Path(".claude/skills/apex-kb/templates/ingest-analysis-template.md"),
        description="Change claim candidate field from claim_type to canonical claim_label vocabulary.",
        risk=42,
        impact=94,
        evidence=95,
        old='''    claim_type: "definition | decision | fact | recommendation | warning | open_question | other"''',
        new='''    claim_label: "raw_source | source_backed_summary | behavioral_inference | working_hypothesis | operator_question | practitioner_question"''',
    ),
    Patch(
        id="G3-SCRIPT-CONTRACT-PARITY-MANIFEST-STATUS",
        group="group_3_script_contract_parity",
        file=Path(".claude/skills/apex-kb/package-manifest.md"),
        description="Update package manifest to reflect that apex_kb.py exists on main instead of being only next_file_to_generate.",
        risk=30,
        impact=82,
        evidence=88,
        old='''      status: "next_file_to_generate"''',
        new='''      status: "present_on_main_requires_contract_validation"''',
    ),
]


def process_patches(mode: Mode, *, allow_dirty_targets: bool) -> list[PatchResult]:
    root = repo_root()
    if Path.cwd().resolve() != root.resolve():
        raise PatchError(f"Run from repo root: {root}")

    for patch in PATCHES:
        ensure_allowed_target(patch.file)
        if not patch.file.exists():
            raise PatchError(f"Patch target missing: {patch.file}")

    targets = sorted({p.file for p in PATCHES}, key=lambda p: p.as_posix())
    if mode == "apply" and not allow_dirty_targets:
        dirty = dirty_target_files(targets)
        if dirty:
            raise PatchError(
                "Target files have unstaged changes. Refusing to apply. "
                "Review/stash/commit them, or pass --allow-dirty-targets. Dirty targets: " + ", ".join(dirty)
            )

    results: list[PatchResult] = []
    for patch in PATCHES:
        text = read_text(patch.file)
        before_hash = sha256_text(text)
        if mode == "verify":
            status, old_count, new_count, changed, message = verify_one_patch(text, patch)
            after_hash = before_hash
        else:
            try:
                updated, old_count, new_count, changed = apply_one_patch(text, patch)
            except PatchError:
                raise
            status = "would_apply" if mode == "dry-run" and changed else "applied"
            message = "Patch validated and would change file." if mode == "dry-run" else "Patch applied."
            after_hash = sha256_text(updated)
            if mode == "apply" and changed:
                write_text(patch.file, updated)
        results.append(
            PatchResult(
                id=patch.id,
                group=patch.group,
                file=patch.file.as_posix(),
                description=patch.description,
                status=status,
                old_match_count=old_count,
                new_match_count=new_count,
                changed=changed,
                old_sha256=before_hash,
                new_sha256=after_hash,
                risk=patch.risk,
                impact=patch.impact,
                evidence=patch.evidence,
                message=message,
            )
        )
    return results


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Deterministic apex-kb hardening patch script")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="Validate anchors and preview changes. Default.")
    mode.add_argument("--apply", action="store_true", help="Apply validated patches.")
    mode.add_argument("--verify", action="store_true", help="Verify whether patches are pending, applied, or conflicted.")
    parser.add_argument("--write-report", action="store_true", help="Write JSON and Markdown reports under _reports/.")
    parser.add_argument("--allow-dirty-targets", action="store_true", help="Allow applying even if allowlisted target files are dirty.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    mode: Mode = "apply" if args.apply else "verify" if args.verify else "dry-run"
    try:
        results = process_patches(mode, allow_dirty_targets=args.allow_dirty_targets)
        report = build_report(results, mode)
        if args.write_report:
            write_reports(report)
        print(json.dumps(report, indent=2, ensure_ascii=False))
        bad_verify = mode == "verify" and any(r.status in {"missing", "conflicted"} for r in results)
        return 2 if bad_verify else 0
    except PatchError as exc:
        error_report = {
            "artifact_name": "apex_kb_hardening_patch_report",
            "status": "failed_closed",
            "generated_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
            "error": str(exc),
            "repo_head": current_head(),
            "repo_branch": current_branch(),
        }
        print(json.dumps(error_report, indent=2, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
