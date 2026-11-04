#!/usr/bin/env python3
"""Detect near-duplicate content copied from one governed Markdown owner.

WP-23 requires a file that reuses another governed file's canonical block to reference
the owner instead of copying the block.  Canonical ownership is a product decision, so
this tool deliberately requires it as ``--owner`` rather than inferring it from path
order, timestamps, or text length.

Usage:
    python tools/check_governed_markdown_duplicates.py --selftest
    python tools/check_governed_markdown_duplicates.py --owner specs/writing-profile.md specs/file-architecture.md

The tool only accepts governed Markdown documents: files beginning with YAML frontmatter.
It compares substantial paragraph/code blocks after normalizing Markdown punctuation and
reports the most similar copied block for each candidate file.
"""

from __future__ import annotations

import argparse
import re
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


RULE = "WP-23"
DEFAULT_THRESHOLD = 0.86
MIN_TOKENS = 30
TOKEN_RE = re.compile(r"[a-z0-9]+")


@dataclass(frozen=True)
class Block:
    line: int
    text: str
    tokens: tuple[str, ...]


@dataclass(frozen=True)
class Finding:
    owner: Path
    candidate: Path
    owner_line: int
    candidate_line: int
    similarity: float

    def render(self) -> str:
        return (
            f"APEX_PROFILE_ERROR: {self.candidate}:{self.candidate_line}: {RULE}: "
            f"{self.similarity:.2f} near-duplicate block of "
            f"{self.owner}:{self.owner_line}; retain the block in {self.owner} and "
            "replace the copied block with a reference to that owner."
        )


def governed_body(path: Path) -> tuple[str, int]:
    """Return the Markdown body and its starting line, rejecting ungoverned files."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path} is not governed Markdown: missing opening YAML frontmatter")
    closing = text.find("\n---\n", 4)
    if closing == -1:
        raise ValueError(f"{path} is not governed Markdown: missing closing YAML frontmatter")
    return text[closing + 5 :], text[: closing + 5].count("\n") + 1


def normalize_tokens(text: str) -> tuple[str, ...]:
    return tuple(TOKEN_RE.findall(text.lower()))


def extract_blocks(body: str, body_start_line: int) -> list[Block]:
    """Split the body into blank-line-delimited blocks that are large enough to matter."""
    blocks: list[Block] = []
    lines = body.splitlines()
    start = 1
    current: list[str] = []

    def add_block() -> None:
        if not current:
            return
        text = "\n".join(current).strip()
        tokens = normalize_tokens(text)
        if len(tokens) >= MIN_TOKENS:
            blocks.append(Block(body_start_line + start - 1, text, tokens))

    for line_number, line in enumerate(lines, start=1):
        if line.strip():
            if not current:
                start = line_number
            current.append(line)
        else:
            add_block()
            current = []
    add_block()
    return blocks


def ngram_set(tokens: tuple[str, ...], size: int = 3) -> set[tuple[str, ...]]:
    return {tuple(tokens[index : index + size]) for index in range(len(tokens) - size + 1)}


def similarity(left: Block, right: Block) -> float:
    """Return trigram Jaccard similarity, which tolerates local wording changes."""
    left_ngrams = ngram_set(left.tokens)
    right_ngrams = ngram_set(right.tokens)
    return len(left_ngrams & right_ngrams) / len(left_ngrams | right_ngrams)


def find_duplicates(owner: Path, candidate: Path, threshold: float) -> list[Finding]:
    owner_body, owner_start_line = governed_body(owner)
    candidate_body, candidate_start_line = governed_body(candidate)
    owner_blocks = extract_blocks(owner_body, owner_start_line)
    candidate_blocks = extract_blocks(candidate_body, candidate_start_line)
    matches: list[Finding] = []
    for candidate_block in candidate_blocks:
        scored = [
            (similarity(owner_block, candidate_block), owner_block)
            for owner_block in owner_blocks
        ]
        if not scored:
            continue
        score, owner_block = max(scored, key=lambda item: item[0])
        if score >= threshold:
            matches.append(
                Finding(owner, candidate, owner_block.line, candidate_block.line, score)
            )
    return matches


def validate_owner_candidates(owner: Path, candidates: list[Path]) -> None:
    """Reject self-comparison, which can only produce a meaningless perfect match."""
    owner_path = owner.resolve()
    if any(candidate.resolve() == owner_path for candidate in candidates):
        raise ValueError("--owner must not also appear in the candidate list")


def write_fixture(path: Path, body: str) -> Path:
    path.write_text(
        "---\ntype: Specification\nid: TEST\ntitle: Test\ndescription: Test fixture.\n"
        "status: current\n---\n\n" + body,
        encoding="utf-8",
    )
    return path


_OWNER_BLOCK = """A canonical owner defines a reusable instruction block with enough distinctive words to
avoid accidental matches. The consuming document must link to the owner instead of copying this
block, because two independently edited copies can drift into contradictory requirements. This
fixture has deliberately ordinary Markdown prose and no special parser markers."""


def selftest() -> int:
    """Exercise synthetic governed fixtures before this checker is run on corpus files."""
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        owner = write_fixture(root / "owner.md", _OWNER_BLOCK)
        reference_only = write_fixture(
            root / "reference.md",
            "See [the canonical owner](owner.md) for the reusable instruction block. "
            "This document adds independent guidance about review scope and validation.",
        )
        near_copy = write_fixture(
            root / "near-copy.md",
            _OWNER_BLOCK.replace("contradictory requirements", "conflicting requirements"),
        )
        ungoverned = root / "ungoverned.md"
        ungoverned.write_text(_OWNER_BLOCK, encoding="utf-8")

        cases = [
            ("reference only", owner, reference_only, 0),
            ("near duplicate", owner, near_copy, 1),
        ]
        passed = True
        for name, source, candidate, expected in cases:
            actual = len(find_duplicates(source, candidate, DEFAULT_THRESHOLD))
            ok = actual == expected
            passed &= ok
            print(f"{'PASS' if ok else 'FAIL'}: {name} -> {actual} finding(s)")

        try:
            find_duplicates(owner, ungoverned, DEFAULT_THRESHOLD)
        except ValueError:
            print("PASS: rejects ungoverned Markdown")
        else:
            passed = False
            print("FAIL: rejects ungoverned Markdown")

        try:
            validate_owner_candidates(owner, [owner])
        except ValueError:
            print("PASS: rejects owner as a candidate")
        else:
            passed = False
            print("FAIL: rejects owner as a candidate")

    print("ALL PASS" if passed else "SOME FAILED")
    return 0 if passed else 1


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--selftest", action="store_true", help="run synthetic fixture tests")
    parser.add_argument("--owner", type=Path, help="canonical owner of the checked block")
    parser.add_argument(
        "candidates", nargs="*", type=Path, help="governed Markdown files to check against owner"
    )
    parser.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD)
    args = parser.parse_args(argv)

    if args.selftest:
        return selftest()
    if args.owner is None or not args.candidates:
        parser.error("--owner and at least one candidate are required unless --selftest is used")
    if not 0 < args.threshold <= 1:
        parser.error("--threshold must be greater than 0 and no greater than 1")

    findings: list[Finding] = []
    try:
        validate_owner_candidates(args.owner, args.candidates)
        for candidate in args.candidates:
            findings.extend(find_duplicates(args.owner, candidate, args.threshold))
    except (OSError, UnicodeError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2

    for finding in findings:
        print(finding.render())
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
