#!/usr/bin/env python3
"""
download_claude_orchestration_agent_sources.py

Extract external research/source links from the Claude orchestration-agent note files
and download them into the claude-orchestration-agents KB.

Default input notes:
  apex-meta/kb/claude-orchestration-agents/raw/notes/SubskillsVsAgents_CC.md
  apex-meta/kb/claude-orchestration-agents/raw/notes/SubskillsVsAgents_gem.md

Default output:
  apex-meta/kb/claude-orchestration-agents/raw/refs/orchestration-layer-research/

Design goals:
  - Standard-library only.
  - Parse Markdown links, autolinks, and bare URLs with line provenance.
  - Deduplicate by normalized URL.
  - Prefer Jina Reader Markdown captures for HTML pages.
  - Download binary/source files directly when the URL extension indicates PDF/DOCX/etc.
  - Skip unsafe/non-web schemes and obvious social/share/mail links.
  - Never overwrite existing files unless --force is used.
  - Write sidecar *.source-meta.json files and a JSON + Markdown run report.

Examples from repo root:
  python scripts/download_claude_orchestration_agent_sources.py --dry-run
  python scripts/download_claude_orchestration_agent_sources.py
  python scripts/download_claude_orchestration_agent_sources.py --force --limit 20
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

KB_REL = Path("apex-meta/kb/claude-orchestration-agents")
DEFAULT_NOTES_REL = [
    KB_REL / "raw/notes/SubskillsVsAgents_CC.md",
    KB_REL / "raw/notes/SubskillsVsAgents_gem.md",
]
DEFAULT_OUT_REL = KB_REL / "raw/refs/orchestration-layer-research"
DEFAULT_REPORT_REL = KB_REL / "manifests/downloads"

USER_AGENT = (
    "Mozilla/5.0 (compatible; ApexOrchestrationSourceDownloader/1.0; "
    "+https://github.com/leela-spec/apexai-os-meta)"
)

DIRECT_EXTENSIONS = {
    ".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx",
    ".csv", ".tsv", ".json", ".jsonl", ".ndjson", ".yaml", ".yml",
    ".zip", ".tar", ".gz", ".tgz", ".txt", ".md",
}

SKIP_SCHEMES = {"mailto", "tel", "javascript", "data", "file"}
SKIP_DOMAINS = {
    "twitter.com", "x.com", "facebook.com", "linkedin.com", "reddit.com",
    "youtube.com", "youtu.be", "medium.com", "substack.com",
}
# Domains above are not universally bad, but in this specific KB source-note context they
# are usually share/social/discussion references rather than primary downloadable sources.
# Use --include-social to keep them.

MARKDOWN_LINK_RE = re.compile(r"!??\[([^\]]{0,300})\]\(([^)\s]+)(?:\s+['\"][^)]+['\"])?\)")
AUTOLINK_RE = re.compile(r"<((?:https?|ftp)://[^>\s]+)>")
BARE_URL_RE = re.compile(r"(?<![\](])\b(?:https?|ftp)://[^\s<>'\"`]+")
TRAILING_PUNCT = ".,;:!?)]}"


@dataclass(frozen=True)
class LinkHit:
    url: str
    normalized_url: str
    source_note: str
    line: int
    link_text: str
    context: str


@dataclass
class DownloadResult:
    index: int
    url: str
    normalized_url: str
    source_note: str
    line: int
    link_text: str
    status: str
    target_path: Optional[str] = None
    meta_path: Optional[str] = None
    capture_url: Optional[str] = None
    content_type: Optional[str] = None
    bytes_written: int = 0
    sha256: Optional[str] = None
    error: Optional[str] = None
    skipped_reason: Optional[str] = None


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def find_repo_root(start: Path) -> Path:
    current = start.resolve()
    for candidate in [current, *current.parents]:
        if (candidate / ".git").exists() or (candidate / "apex-meta").exists():
            return candidate
    return current


def normalize_url(url: str) -> Optional[str]:
    url = html.unescape(url.strip())
    # Bare URLs inside Markdown tables are followed by the next cell delimiter.
    # Treat that delimiter as provenance text, not as part of the URL.
    if "|" in url:
        url = url.split("|", 1)[0]
    while url and url[-1] in TRAILING_PUNCT:
        url = url[:-1]
    if not url:
        return None
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme.lower() in SKIP_SCHEMES:
        return None
    if parsed.scheme.lower() not in {"http", "https", "ftp"}:
        return None
    host = parsed.netloc.lower()
    # Remove obvious tracking params but keep query parameters that may identify PDFs/assets.
    query_pairs = []
    for key, value in urllib.parse.parse_qsl(parsed.query, keep_blank_values=True):
        kl = key.lower()
        if kl.startswith("utm_") or kl in {"fbclid", "gclid", "mc_cid", "mc_eid"}:
            continue
        query_pairs.append((key, value))
    clean_query = urllib.parse.urlencode(query_pairs, doseq=True)
    clean = urllib.parse.urlunsplit((parsed.scheme.lower(), host, parsed.path or "/", clean_query, ""))
    return clean


def domain_of(url: str) -> str:
    return urllib.parse.urlsplit(url).netloc.lower().removeprefix("www.")


def should_skip_domain(url: str, include_social: bool, include_domains: Sequence[str], exclude_domains: Sequence[str]) -> Optional[str]:
    domain = domain_of(url)
    if include_domains and not any(domain == d or domain.endswith("." + d) for d in include_domains):
        return "domain_not_in_include_list"
    if any(domain == d or domain.endswith("." + d) for d in exclude_domains):
        return "domain_excluded"
    if not include_social and any(domain == d or domain.endswith("." + d) for d in SKIP_DOMAINS):
        return "social_or_discussion_domain_skipped"
    return None


def extract_links_from_text(text: str, source_note: Path) -> List[LinkHit]:
    hits: List[LinkHit] = []
    seen_line_url: set[Tuple[int, str]] = set()
    for lineno, line in enumerate(text.splitlines(), start=1):
        matches: List[Tuple[str, str]] = []
        for m in MARKDOWN_LINK_RE.finditer(line):
            matches.append((m.group(2), m.group(1).strip()))
        for m in AUTOLINK_RE.finditer(line):
            matches.append((m.group(1), ""))
        for m in BARE_URL_RE.finditer(line):
            matches.append((m.group(0), ""))
        for raw_url, label in matches:
            normalized = normalize_url(raw_url)
            if not normalized:
                continue
            key = (lineno, normalized)
            if key in seen_line_url:
                continue
            seen_line_url.add(key)
            hits.append(
                LinkHit(
                    url=raw_url.strip(),
                    normalized_url=normalized,
                    source_note=source_note.as_posix(),
                    line=lineno,
                    link_text=label,
                    context=line.strip()[:500],
                )
            )
    return hits


def dedupe_links(hits: Iterable[LinkHit]) -> List[LinkHit]:
    by_url: Dict[str, LinkHit] = {}
    for hit in hits:
        by_url.setdefault(hit.normalized_url, hit)
    return list(by_url.values())


def url_extension(url: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    suffix = Path(parsed.path).suffix.lower()
    return suffix


def build_jina_url(url: str) -> str:
    # Same pattern as the existing promptquorum PowerShell downloader:
    #   https://r.jina.ai/https://example.com/page
    return "https://r.jina.ai/" + url


def github_raw_url(url: str) -> Optional[str]:
    parsed = urllib.parse.urlsplit(url)
    if parsed.netloc.lower().removeprefix("www.") != "github.com":
        return None
    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) >= 5 and parts[2] == "blob":
        owner, repo, branch = parts[0], parts[1], parts[3]
        raw_path = "/".join(parts[4:])
        return f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{raw_path}"
    return None


def safe_slug(text: str, max_len: int = 90) -> str:
    text = urllib.parse.unquote(text)
    text = re.sub(r"https?://", "", text, flags=re.I)
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-._")
    if not text:
        text = "source"
    return text[:max_len].strip("-._") or "source"


def filename_for(hit: LinkHit, ext: str, used: set[str]) -> str:
    parsed = urllib.parse.urlsplit(hit.normalized_url)
    domain = domain_of(hit.normalized_url).replace(".", "-")
    path_part = Path(parsed.path).stem if Path(parsed.path).stem else "index"
    label = hit.link_text or path_part
    stem = safe_slug(f"{domain}-{label}", 100)
    if not ext:
        ext = ".md"
    name = f"{stem}{ext}"
    counter = 2
    while name.lower() in used:
        name = f"{stem}-{counter}{ext}"
        counter += 1
    used.add(name.lower())
    return name


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def request_bytes(url: str, timeout: int, max_bytes: int) -> Tuple[bytes, str, str]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        content_type = response.headers.get("Content-Type", "")
        final_url = response.geturl()
        chunks: List[bytes] = []
        total = 0
        while True:
            chunk = response.read(1024 * 64)
            if not chunk:
                break
            chunks.append(chunk)
            total += len(chunk)
            if max_bytes and total > max_bytes:
                raise ValueError(f"download_exceeded_max_bytes:{total}>{max_bytes}")
        return b"".join(chunks), content_type, final_url


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def read_note(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def make_metadata(hit: LinkHit, result: DownloadResult, capture_method: str) -> Dict[str, object]:
    return {
        "source_url": hit.normalized_url,
        "original_url_text": hit.url,
        "capture_url": result.capture_url,
        "capture_method": capture_method,
        "source_note": hit.source_note,
        "source_line": hit.line,
        "link_text": hit.link_text,
        "context": hit.context,
        "downloaded_at": utc_now(),
        "content_type": result.content_type,
        "bytes_written": result.bytes_written,
        "sha256": result.sha256,
    }


def render_markdown_report(results: Sequence[DownloadResult], args: argparse.Namespace) -> str:
    status_counts: Dict[str, int] = {}
    for r in results:
        status_counts[r.status] = status_counts.get(r.status, 0) + 1
    lines = [
        "# Claude Orchestration Agents Research Download Report",
        "",
        f"Generated: `{utc_now()}`",
        "",
        "## Run Configuration",
        "",
        "```yaml",
        f"repo_root: {Path(args.repo_root).as_posix() if args.repo_root else 'auto'}",
        f"dry_run: {bool(args.dry_run)}",
        f"force: {bool(args.force)}",
        f"no_jina: {bool(args.no_jina)}",
        f"limit: {args.limit}",
        f"sleep_seconds: {args.sleep}",
        f"timeout_seconds: {args.timeout}",
        f"max_bytes: {args.max_bytes}",
        "```",
        "",
        "## Status Counts",
        "",
        "| Status | Count |",
        "|---|---:|",
    ]
    for status, count in sorted(status_counts.items()):
        lines.append(f"| {status} | {count} |")
    lines.extend(["", "## Results", "", "| # | Status | Source | Target | Note line | Error/Reason |", "|---:|---|---|---|---:|---|"])
    for r in results:
        target = r.target_path or ""
        reason = r.error or r.skipped_reason or ""
        lines.append(
            f"| {r.index} | {r.status} | `{r.normalized_url}` | `{target}` | {r.line} | {reason} |"
        )
    lines.append("")
    return "\n".join(lines)


def run(args: argparse.Namespace) -> int:
    repo_root = Path(args.repo_root).resolve() if args.repo_root else find_repo_root(Path.cwd())
    notes = [repo_root / Path(p) for p in (args.notes or DEFAULT_NOTES_REL)]
    out_dir = repo_root / Path(args.out_dir)
    report_dir = repo_root / Path(args.report_dir)

    all_hits: List[LinkHit] = []
    missing_notes: List[str] = []
    for note_path in notes:
        if not note_path.exists():
            missing_notes.append(note_path.as_posix())
            continue
        rel_note = note_path.relative_to(repo_root) if note_path.is_relative_to(repo_root) else note_path
        all_hits.extend(extract_links_from_text(read_note(note_path), rel_note))

    hits = dedupe_links(all_hits)

    include_domains = [d.lower().removeprefix("www.") for d in args.include_domain]
    exclude_domains = [d.lower().removeprefix("www.") for d in args.exclude_domain]

    filtered: List[Tuple[LinkHit, Optional[str]]] = []
    for hit in hits:
        skip = should_skip_domain(hit.normalized_url, args.include_social, include_domains, exclude_domains)
        filtered.append((hit, skip))

    if args.limit:
        filtered = filtered[: args.limit]

    results: List[DownloadResult] = []
    used_names: set[str] = set()
    run_started = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d_%H%M%S")

    for idx, (hit, skip_reason) in enumerate(filtered, start=1):
        if skip_reason:
            results.append(
                DownloadResult(
                    index=idx,
                    url=hit.url,
                    normalized_url=hit.normalized_url,
                    source_note=hit.source_note,
                    line=hit.line,
                    link_text=hit.link_text,
                    status="skipped",
                    skipped_reason=skip_reason,
                )
            )
            continue

        direct_ext = url_extension(hit.normalized_url)
        raw_github_url = github_raw_url(hit.normalized_url)
        if raw_github_url:
            capture_url, ext, method = raw_github_url, url_extension(raw_github_url) or ".txt", "github_raw"
        elif domain_of(hit.normalized_url) == "github.com":
            capture_url, ext, method = hit.normalized_url, ".html", "github_html"
        elif direct_ext in DIRECT_EXTENSIONS:
            capture_url, ext, method = hit.normalized_url, direct_ext, "direct"
        elif args.no_jina:
            capture_url, ext, method = hit.normalized_url, ".html", "raw_html"
        else:
            capture_url, ext, method = build_jina_url(hit.normalized_url), ".md", "jina_markdown"

        filename = filename_for(hit, ext, used_names)
        target = out_dir / filename
        meta_target = target.with_suffix(target.suffix + ".source-meta.json")
        rel_target = target.relative_to(repo_root) if target.is_relative_to(repo_root) else target
        rel_meta = meta_target.relative_to(repo_root) if meta_target.is_relative_to(repo_root) else meta_target

        result = DownloadResult(
            index=idx,
            url=hit.url,
            normalized_url=hit.normalized_url,
            source_note=hit.source_note,
            line=hit.line,
            link_text=hit.link_text,
            status="pending",
            target_path=rel_target.as_posix(),
            meta_path=rel_meta.as_posix(),
            capture_url=capture_url,
        )

        if target.exists() and target.stat().st_size > 0 and not args.force:
            result.status = "skipped"
            result.skipped_reason = "target_exists_use_force_to_overwrite"
            results.append(result)
            continue

        if args.dry_run:
            result.status = "dry_run"
            result.skipped_reason = method
            results.append(result)
            continue

        try:
            data, content_type, final_url = request_bytes(capture_url, args.timeout, args.max_bytes)
            # Jina occasionally returns empty or denial pages. Keep them out by default.
            if len(data) < args.min_bytes:
                raise ValueError(f"download_too_small:{len(data)}<{args.min_bytes}")
            out_dir.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            digest = sha256_bytes(data)
            result.status = "downloaded"
            result.content_type = content_type
            result.capture_url = final_url
            result.bytes_written = len(data)
            result.sha256 = digest
            metadata = make_metadata(hit, result, method)
            write_text(meta_target, json.dumps(metadata, indent=2, ensure_ascii=False) + "\n")
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ValueError, OSError) as exc:
            result.status = "failed"
            result.error = f"{type(exc).__name__}: {exc}"
        results.append(result)
        if args.sleep and not args.dry_run:
            time.sleep(args.sleep)

    if missing_notes:
        start = len(results) + 1
        for offset, note in enumerate(missing_notes):
            results.append(
                DownloadResult(
                    index=start + offset,
                    url="",
                    normalized_url="",
                    source_note=note,
                    line=0,
                    link_text="",
                    status="failed",
                    error="input_note_missing",
                )
            )

    report_dir.mkdir(parents=True, exist_ok=True)
    json_report = report_dir / f"claude-orchestration-agent-downloads_{run_started}.json"
    md_report = report_dir / f"claude-orchestration-agent-downloads_{run_started}.md"
    report_payload = {
        "generated_at": utc_now(),
        "repo_root": repo_root.as_posix(),
        "input_notes": [p.as_posix() for p in notes],
        "output_dir": out_dir.as_posix(),
        "total_links_seen": len(all_hits),
        "unique_links_seen": len(hits),
        "results": [asdict(r) for r in results],
    }
    if not args.dry_run:
        write_text(json_report, json.dumps(report_payload, indent=2, ensure_ascii=False) + "\n")
        write_text(md_report, render_markdown_report(results, args))
    else:
        # Even dry-run writes reports unless disabled; this makes the planned run auditable.
        write_text(json_report, json.dumps(report_payload, indent=2, ensure_ascii=False) + "\n")
        write_text(md_report, render_markdown_report(results, args))

    downloaded = sum(1 for r in results if r.status == "downloaded")
    failed = sum(1 for r in results if r.status == "failed")
    skipped = sum(1 for r in results if r.status == "skipped")
    dry = sum(1 for r in results if r.status == "dry_run")
    print(f"repo_root: {repo_root}")
    print(f"unique_links: {len(hits)}")
    print(f"downloaded: {downloaded} skipped: {skipped} dry_run: {dry} failed: {failed}")
    print(f"report_json: {json_report}")
    print(f"report_md: {md_report}")
    return 1 if failed and args.fail_on_error else 0


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Download linked research sources for the claude-orchestration-agents KB.")
    parser.add_argument("--repo-root", default=None, help="Repository root. Defaults to auto-detection from current working directory.")
    parser.add_argument("--notes", nargs="*", default=None, help="Input note files relative to repo root. Defaults to the two SubskillsVsAgents notes.")
    parser.add_argument("--out-dir", default=DEFAULT_OUT_REL.as_posix(), help="Output directory relative to repo root.")
    parser.add_argument("--report-dir", default=DEFAULT_REPORT_REL.as_posix(), help="Report directory relative to repo root.")
    parser.add_argument("--dry-run", action="store_true", help="Plan downloads and write reports, but do not fetch source content.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing downloaded files.")
    parser.add_argument("--no-jina", action="store_true", help="Disable Jina Reader captures for HTML pages and save raw HTML instead.")
    parser.add_argument("--include-social", action="store_true", help="Do not skip common social/discussion domains.")
    parser.add_argument("--include-domain", action="append", default=[], help="Only download these domains. Can be repeated.")
    parser.add_argument("--exclude-domain", action="append", default=[], help="Exclude these domains. Can be repeated.")
    parser.add_argument("--limit", type=int, default=0, help="Process at most N unique links after filtering. 0 means no limit.")
    parser.add_argument("--timeout", type=int, default=35, help="Request timeout in seconds.")
    parser.add_argument("--sleep", type=float, default=1.0, help="Sleep seconds between successful/attempted downloads.")
    parser.add_argument("--max-bytes", type=int, default=50 * 1024 * 1024, help="Maximum bytes per downloaded source. 0 disables cap.")
    parser.add_argument("--min-bytes", type=int, default=80, help="Minimum acceptable response size in bytes.")
    parser.add_argument("--fail-on-error", action="store_true", help="Return non-zero if any download failed.")
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    return run(parse_args(argv))


if __name__ == "__main__":
    raise SystemExit(main())
