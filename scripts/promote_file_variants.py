#!/usr/bin/env python3
"""Promote variant files into canonical paths with deterministic backups.

This script moves existing canonical files into a backup root, preserving their
repo-relative path, then moves variant files into the canonical paths. It does
not copy file contents or rewrite bytes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Mapping:
    variant: Path
    canonical: Path
    backup: Path


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def repo_relative(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def resolve_repo_path(raw_path: str) -> Path:
    path = (REPO_ROOT / raw_path).resolve()
    if not path.is_relative_to(REPO_ROOT):
        raise ValueError(f"Path escapes repo root: {raw_path}")
    return path


def parse_pair(raw_pair: str) -> tuple[Path, Path]:
    if "=" not in raw_pair:
        raise ValueError(f"Mapping must be VARIANT=CANONICAL: {raw_pair}")
    variant_raw, canonical_raw = raw_pair.split("=", 1)
    if not variant_raw or not canonical_raw:
        raise ValueError(f"Mapping must have non-empty paths: {raw_pair}")
    return resolve_repo_path(variant_raw), resolve_repo_path(canonical_raw)


def load_manifest(path: Path) -> list[tuple[Path, Path]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError("Manifest must be a JSON list")
    pairs: list[tuple[Path, Path]] = []
    for item in payload:
        if not isinstance(item, dict) or "variant" not in item or "canonical" not in item:
            raise ValueError("Each manifest item must contain variant and canonical")
        pairs.append((resolve_repo_path(item["variant"]), resolve_repo_path(item["canonical"])))
    return pairs


def build_mappings(
    pairs: list[tuple[Path, Path]],
    backup_root: Path,
) -> list[Mapping]:
    mappings: list[Mapping] = []
    seen_variants: set[Path] = set()
    seen_canonicals: set[Path] = set()
    for variant, canonical in pairs:
        if variant in seen_variants:
            raise ValueError(f"Duplicate variant path: {repo_relative(variant)}")
        if canonical in seen_canonicals:
            raise ValueError(f"Duplicate canonical path: {repo_relative(canonical)}")
        seen_variants.add(variant)
        seen_canonicals.add(canonical)
        backup = backup_root / canonical.relative_to(REPO_ROOT)
        mappings.append(Mapping(variant=variant, canonical=canonical, backup=backup))
    return mappings


def validate_mappings(mappings: list[Mapping]) -> None:
    for mapping in mappings:
        if not mapping.variant.exists() or not mapping.variant.is_file():
            raise ValueError(f"Missing variant file: {repo_relative(mapping.variant)}")
        if mapping.backup.exists():
            raise ValueError(f"Backup target already exists: {repo_relative(mapping.backup)}")
        if mapping.variant == mapping.canonical:
            raise ValueError(f"Variant and canonical are the same path: {repo_relative(mapping.variant)}")

    variant_paths = {mapping.variant for mapping in mappings}
    for mapping in mappings:
        if mapping.canonical in variant_paths:
            raise ValueError(
                f"Canonical path is also a variant path in this run: {repo_relative(mapping.canonical)}"
            )


def describe(mappings: list[Mapping]) -> None:
    for mapping in mappings:
        variant_hash = sha256_file(mapping.variant)
        print(f"variant:   {repo_relative(mapping.variant)} sha256={variant_hash}")
        if mapping.canonical.exists():
            print(
                f"canonical: {repo_relative(mapping.canonical)} "
                f"sha256={sha256_file(mapping.canonical)}"
            )
            print(f"backup:    {repo_relative(mapping.backup)}")
        else:
            print(f"canonical: {repo_relative(mapping.canonical)} (missing; no backup move)")
        print()


def apply_moves(mappings: list[Mapping]) -> None:
    completed: list[tuple[Path, Path]] = []
    try:
        for mapping in mappings:
            if mapping.canonical.exists():
                mapping.backup.parent.mkdir(parents=True, exist_ok=True)
                mapping.canonical.rename(mapping.backup)
                completed.append((mapping.backup, mapping.canonical))
                print(f"MOVED old -> backup: {repo_relative(mapping.backup)}")

            mapping.canonical.parent.mkdir(parents=True, exist_ok=True)
            mapping.variant.rename(mapping.canonical)
            completed.append((mapping.canonical, mapping.variant))
            print(f"MOVED variant -> canonical: {repo_relative(mapping.canonical)}")
    except Exception:
        print("ERROR: move failed after partial progress; no automatic rollback attempted", file=sys.stderr)
        print("Completed moves:", file=sys.stderr)
        for src, dst in completed:
            print(f"  {src} <= from {dst}", file=sys.stderr)
        raise


def verify_post_move(mappings: list[Mapping], expected_variant_hashes: dict[Path, str]) -> None:
    for mapping in mappings:
        if mapping.variant.exists():
            raise ValueError(f"Variant path still exists after promotion: {repo_relative(mapping.variant)}")
        if not mapping.canonical.exists():
            raise ValueError(f"Canonical path missing after promotion: {repo_relative(mapping.canonical)}")
        actual_hash = sha256_file(mapping.canonical)
        expected_hash = expected_variant_hashes[mapping.variant]
        if actual_hash != expected_hash:
            raise ValueError(
                f"Promoted canonical hash mismatch for {repo_relative(mapping.canonical)}: "
                f"expected {expected_hash}, got {actual_hash}"
            )


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--backup-root",
        default="source-knowledge/Apex&Claude_old",
        help="repo-relative backup root for old canonical files",
    )
    parser.add_argument(
        "--map",
        action="append",
        default=[],
        metavar="VARIANT=CANONICAL",
        help="variant-to-canonical mapping, repo-relative",
    )
    parser.add_argument(
        "--manifest",
        help="JSON manifest list of {variant, canonical} mappings, repo-relative",
    )
    parser.add_argument("--apply", action="store_true", help="perform moves; default is dry-run")
    args = parser.parse_args(argv)

    pairs: list[tuple[Path, Path]] = []
    if args.manifest:
        pairs.extend(load_manifest(resolve_repo_path(args.manifest)))
    pairs.extend(parse_pair(raw_pair) for raw_pair in args.map)
    if not pairs:
        raise ValueError("Provide at least one --map or --manifest")

    backup_root = resolve_repo_path(args.backup_root)
    mappings = build_mappings(pairs, backup_root)
    validate_mappings(mappings)
    describe(mappings)

    if not args.apply:
        print("DRY-RUN: no files moved. Re-run with --apply to promote variants.")
        return 0

    expected_variant_hashes = {mapping.variant: sha256_file(mapping.variant) for mapping in mappings}
    apply_moves(mappings)
    verify_post_move(mappings, expected_variant_hashes)
    print("PROMOTION VERIFIED")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
