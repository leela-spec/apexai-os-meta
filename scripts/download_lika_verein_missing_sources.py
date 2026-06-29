#!/usr/bin/env python3
# download_lika_verein_missing_sources.py
#
# Safer Space e.V. / Lika Verein Taxes & Accounting KB
#
# Purpose:
#   Download ONLY the currently missing / not-confirmed sources into:
#     apex-meta/kb/lika-verein-taxes-accounting/raw/refs
#
# Design goals:
#   - Do not duplicate already existing KB sources.
#   - Skip if target file already exists and is non-empty, unless --force is used.
#   - Prefer official direct PDF links for PDFs.
#   - Use Jina Reader markdown capture for HTML pages by default.
#   - Try verified_url first, then fallback_url(s).
#   - Write one *.source-meta.json next to each successfully downloaded file.
#   - Write one run report under:
#       apex-meta/kb/lika-verein-taxes-accounting/manifests/downloads/
#   - Manual-review entries are listed in the report but not downloaded.
#
# Example from repo root:
#   python scripts/download_lika_verein_missing_sources.py
#
# Example from anywhere:
#   python download_lika_verein_missing_sources.py --repo-root C:\GitDev\apexai-os-meta
#
# Dry run:
#   python scripts/download_lika_verein_missing_sources.py --dry-run
#
# Force refresh:
#   python scripts/download_lika_verein_missing_sources.py --force
#
# Disable Jina and save raw HTML instead:
#   python scripts/download_lika_verein_missing_sources.py --no-jina

from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, asdict
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


KB_REL = Path("apex-meta/kb/lika-verein-taxes-accounting")
RAW_REFS_REL = KB_REL / "raw/refs"
REPORTS_REL = KB_REL / "manifests/downloads"


USER_AGENT = (
    "Mozilla/5.0 (compatible; SaferSpaceSourceDownloader/1.0; "
    "+https://github.com/leela-spec/apexai-os-meta)"
)


@dataclass(frozen=True)
class Source:
    source_id: str
    title: str
    priority: str
    target_path: str
    capture_method: str
    urls: List[str]
    section: str
    reason: str
    quality_score: Optional[int] = None
    existing_related_path: Optional[str] = None
    risk_flags: Tuple[str, ...] = ()


# Manual review entries are deliberately NOT auto-downloaded.
MANUAL_REVIEW: List[Dict[str, Any]] = [
    {
        "source_id": "bfh_xi_r_34_14_berghain",
        "priority": "P1",
        "title": "BFH XI R 34/14 — Techno/DJ/Konzertähnlichkeit",
        "target_path": "raw/refs/BFH_XI-R-34-14_Berghain-Techno-Konzert.md",
        "script_action": "do_not_download_until_url_verified",
        "reason": "Critical for 7% vs. 19%, but avoid unverified BFH URL.",
    },
    {
        "source_id": "ustae_abschnitt_12_7",
        "priority": "P0",
        "title": "UStAE Abschnitt 12.7 — ermäßigter Steuersatz Kultur/Konzerte",
        "target_path": "raw/refs/BMF_UStAE_12-7_Kultur-Konzerte.md",
        "script_action": "do_not_download_until_url_verified",
        "reason": "Critical primary source for 7% vs. 19%, but URL needs reliable official source.",
    },
    {
        "source_id": "eventfaq_mietvertrag_location",
        "priority": "P3",
        "title": "EVENTFAQ Mietvertrag Location",
        "possible_url": "https://eventfaq.de/mietvertrag-location/",
        "target_path": "raw/refs/EVENTFAQ_Mietvertrag-Location.md",
        "script_action": "do_not_auto_download",
        "reason": "Venue tax gap is not solved by this source; existing EVENTFAQ source already present.",
    },
    {
        "source_id": "michow_ulbricht_mustervertraege",
        "priority": "P3",
        "title": "Michow & Ulbricht Musterverträge Live Entertainment",
        "possible_url": "https://michow-ulbricht.de/mustervertraege-gratis-zum-download/",
        "target_path": "raw/refs/Michow-Ulbricht_Mustervertraege-Live-Entertainment.md",
        "script_action": "do_not_auto_download",
        "reason": "Template source only; not tax authority.",
    },
]


CORE_SOURCES: List[Source] = [
    Source(
        source_id="ksk_info04_veranstalter",
        priority="P0",
        quality_score=93,
        title="KSK Informationsschrift Nr. 4 — Abgabepflicht von Veranstaltern",
        target_path="raw/refs/KSK_Info04_Abgabepflicht-Veranstalter.pdf",
        capture_method="direct_pdf",
        urls=[
            "https://www.kuenstlersozialkasse.de/fileadmin/Dokumente/Mediencenter_Unternehmer_Verwerter/Informationsschriften/Info_04_Abgabepflicht_von_Veranstaltern.pdf",
        ],
        section="core_missing_p0_p1",
        reason="Top source, P0, not found in repo search.",
    ),
    Source(
        source_id="bmj_ustdv_33",
        priority="P0",
        quality_score=92,
        title="§33 UStDV — Rechnungen über Kleinbeträge",
        target_path="raw/refs/BMJ_UStDV_33_Kleinbetragsrechnungen.md",
        capture_method="jina_markdown_or_html_snapshot",
        urls=[
            "https://www.gesetze-im-internet.de/ustdv_1980/__33.html",
        ],
        section="core_missing_p0_p1",
        reason="Core law source missing as standalone file.",
    ),
    Source(
        source_id="bmj_ustg_14",
        priority="P1",
        title="§14 UStG — Ausstellung von Rechnungen",
        target_path="raw/refs/BMJ_UStG_14_Rechnungen.md",
        capture_method="jina_markdown_or_html_snapshot",
        urls=[
            "https://www.gesetze-im-internet.de/ustg_1980/__14.html",
        ],
        section="core_missing_p0_p1",
        reason="Needed to cross-check IHK and ticket invoice logic.",
    ),
    Source(
        source_id="bzst_50a_abzugsteuer",
        priority="P0",
        quality_score=87,
        title="BZSt Abzugsteuer §50a EStG",
        target_path="raw/refs/BZSt_50a-Abzugsteuer.md",
        capture_method="jina_markdown_or_html_snapshot",
        urls=[
            "https://www.bzst.de/DE/Privatpersonen/Abzugsteuern_50a/abzugsteuern_node.html",
            "https://www.bzst.de/DE/Unternehmen/Abzugsteuern/Abzugsteuern_node.html",
        ],
        section="core_missing_p0_p1",
        reason="Foreign artists / §50a is a core contractor topic.",
    ),
    Source(
        source_id="pretix_order_lifecycle",
        priority="P1",
        quality_score=80,
        title="pretix Order Lifecycle",
        target_path="raw/refs/pretix_Order-Lifecycle.md",
        capture_method="jina_markdown",
        urls=[
            "https://docs.pretix.eu/dev/api/guides/order_lifecycle.html",
            "https://docs.pretix.eu/en/latest/api/guides/order_lifecycle.html",
        ],
        section="core_missing_p0_p1",
        reason="Needed for refund/storno/order-status workflow.",
    ),
    Source(
        source_id="eventbrite_event_payout_financials",
        priority="P2",
        quality_score=63,
        title="Eventbrite Event/Payout financial information",
        target_path="raw/refs/Eventbrite_Event-Payout-Financial-Information.md",
        capture_method="jina_markdown",
        urls=[
            "https://www.eventbrite.de/help/de/articles/263015/so-koennen-sie-alle-finanzinformationen-zu-einem-event-in-form-einer-event-rechnung-abrufen/",
            "https://www.eventbrite.co.uk/help/en-us/articles/263015/how-to-see-all-of-your-event-s-financial-information-with-event-invoices/",
        ],
        section="core_missing_p0_p1",
        reason="Complements Eventbrite Umsatzübersicht already present.",
    ),
    Source(
        source_id="bfh_v_r_16_09_vorverkaufsgebuehr",
        priority="P1",
        quality_score=84,
        title="BFH V R 16/09 — Vorverkaufsgebühr",
        target_path="raw/refs/BFH_V-R-16-09_Vorverkaufsgebuehr.md",
        capture_method="jina_markdown_or_html_snapshot",
        urls=[
            "https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/STRE201210056/",
        ],
        section="core_missing_p0_p1",
        reason="Ticket fee / VAT treatment source.",
    ),
]


OPTIONAL_SOURCES: List[Source] = [
    Source(
        source_id="bmf_gobd_2024_pdf",
        priority="P0",
        title="BMF GoBD Änderung 2024 — original PDF",
        target_path="raw/refs/BMF_GoBD-2024.pdf",
        capture_method="direct_pdf",
        urls=[
            "https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/AO-Anwendungserlass/2024-03-11-aenderung-gobd.pdf?__blob=publicationFile&v=3",
            "https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/AO-Anwendungserlass/2024-03-11-aenderung-gobd.pdf",
            "https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/AO-Anwendungserlass/2024-03-11-aenderung-gobd.html",
        ],
        section="optional_download_because_pdf_or_asset_missing",
        existing_related_path="raw/refs/BMF_GoBD-2024.md",
        reason="Original official PDF better than only HTML/MD snapshot.",
    ),
    Source(
        source_id="finanzverwaltung_nrw_mein_elster_vereine_pdf",
        priority="P1",
        title="Mein ELSTER für Vereine — NRW brochure PDF",
        target_path="raw/refs/FinanzverwaltungNRW_Mein-ELSTER-fuer-Vereine.pdf",
        capture_method="direct_pdf",
        urls=[
            "https://www.finanzverwaltung.nrw.de/system/files/media/document/file/2026_05_26_internet_endf_einzs_brosch_meinelstervereine.pdf",
        ],
        section="optional_download_because_pdf_or_asset_missing",
        existing_related_path="raw/refs/FinanzamtNRW_Vereine-Umsatzsteuer.md",
        risk_flags=("gemeinnuetzigkeit_context_possible",),
        reason="Official PDF useful for ELSTER process; mark Gemeinnützigkeit transfer risk.",
    ),
]


AWV_ASSET_SOURCE: Dict[str, Any] = {
    "source_id": "awv_template_assets",
    "priority": "P0",
    "title": "AWV Muster-Verfahrensdokumentation — PDF/DOCX template assets",
    "section": "optional_download_because_pdf_or_asset_missing",
    "existing_path": "raw/refs/AWV_GoBD-Praxisleitfaden.md",
    "page_urls": [
        "https://www.awv-net.de/publikationen-produkte/publikationen/detailseite/musterverfahrensdokumentation-zur-belegablage",
        "https://www.awv-net.de/publikationen/datenverarbeitung/",
    ],
    "targets": {
        ".pdf": "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.pdf",
        ".docx": "raw/refs/AWV_Muster-Verfahrensdokumentation-Belegablage.docx",
    },
    "reason": "The page exists as MD, but the actual reusable template file may not be archived.",
}


class LinkExtractor(HTMLParser):
    def __init__(self, base_url: str) -> None:
        super().__init__()
        self.base_url = base_url
        self.links: List[str] = []

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        if tag.lower() != "a":
            return
        attr = dict(attrs)
        href = attr.get("href")
        if href:
            self.links.append(urllib.parse.urljoin(self.base_url, href))


def utc_now_iso() -> str:
    return _dt.datetime.now(_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def make_jina_url(url: str) -> str:
    # Jina Reader accepts https://r.jina.ai/http://... and https://r.jina.ai/http://...
    # For https URLs, this form works: https://r.jina.ai/http://r.jina.ai/http:// is WRONG.
    # Correct form: https://r.jina.ai/http://r.jina.ai/http:// not used; use https://r.jina.ai/http://? No.
    # Current documented/simple form used in the existing PowerShell script:
    #   https://r.jina.ai/https://example.com/page
    return "https://r.jina.ai/" + url


def rel_to_abs(repo_root: Path, rel_path: str) -> Path:
    # All target_path entries are relative to the KB root if they start with raw/refs.
    p = Path(rel_path)
    if p.parts[:2] == ("raw", "refs"):
        return repo_root / KB_REL / p
    return repo_root / p


def guess_content_type(headers: Any) -> str:
    try:
        return headers.get("Content-Type", "")
    except Exception:
        return ""


def request_url(url: str, timeout: int) -> Tuple[bytes, str, str]:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "*/*",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read()
        final_url = resp.geturl()
        content_type = guess_content_type(resp.headers)
    return data, final_url, content_type


def validate_payload(data: bytes, source: Source, content_type: str, used_url: str) -> Optional[str]:
    if not data:
        return "empty response"

    suffix = Path(source.target_path).suffix.lower()

    if suffix == ".pdf":
        if not data.startswith(b"%PDF"):
            # Some official servers return HTML pages for direct PDF URLs if moved.
            if b"<html" in data[:2048].lower() or "text/html" in content_type.lower():
                return "expected PDF but received HTML"
            return "expected PDF but response does not start with %PDF"
        return None

    if suffix == ".md":
        text_sample = data[:4096].decode("utf-8", errors="replace").lower()
        # Jina markdown usually starts with Title/URL/Markdown Content.
        # Raw HTML fallback is allowed when --no-jina is used.
        if "not found" in text_sample and ("404" in text_sample or "page not found" in text_sample):
            return "response appears to be a 404/not found page"
        if len(data) < 200:
            return "response too short for a useful markdown/html capture"
        return None

    return None


def write_meta(
    meta_path: Path,
    source: Dict[str, Any],
    target_path: Path,
    original_url: str,
    final_url: str,
    content_type: str,
) -> None:
    meta = {
        "generated_at": utc_now_iso(),
        "source": source,
        "download": {
            "target_path": str(target_path),
            "sha256": sha256_file(target_path),
            "size_bytes": target_path.stat().st_size,
            "original_url": original_url,
            "final_url": final_url,
            "content_type": content_type,
        },
    }
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")


def download_source(
    repo_root: Path,
    source: Source,
    *,
    force: bool,
    dry_run: bool,
    no_jina: bool,
    timeout: int,
    retries: int,
    sleep_seconds: float,
) -> Dict[str, Any]:
    target = rel_to_abs(repo_root, source.target_path)
    target.parent.mkdir(parents=True, exist_ok=True)

    result: Dict[str, Any] = {
        "source_id": source.source_id,
        "title": source.title,
        "priority": source.priority,
        "section": source.section,
        "target_path": str(target.relative_to(repo_root)) if target.is_absolute() else str(target),
        "capture_method": source.capture_method,
        "status": None,
        "used_url": None,
        "final_url": None,
        "error": None,
        "reason": source.reason,
        "risk_flags": list(source.risk_flags),
    }

    if target.exists() and target.stat().st_size > 0 and not force:
        result["status"] = "skipped_existing"
        return result

    if dry_run:
        result["status"] = "dry_run_would_download"
        result["used_url"] = source.urls[0] if source.urls else None
        return result

    errors: List[str] = []

    for raw_url in source.urls:
        # For HTML/markdown captures, use Jina by default. Do NOT use Jina for PDFs.
        is_pdf_target = Path(source.target_path).suffix.lower() == ".pdf"
        if is_pdf_target or no_jina or source.capture_method == "direct_pdf":
            download_url = raw_url
        else:
            download_url = make_jina_url(raw_url)

        for attempt in range(1, retries + 2):
            try:
                data, final_url, content_type = request_url(download_url, timeout=timeout)
                validation_error = validate_payload(data, source, content_type, download_url)
                if validation_error:
                    raise RuntimeError(validation_error)

                target.write_bytes(data)
                meta_path = target.with_suffix(target.suffix + ".source-meta.json")
                write_meta(
                    meta_path,
                    asdict(source),
                    target,
                    original_url=download_url,
                    final_url=final_url,
                    content_type=content_type,
                )

                result.update(
                    {
                        "status": "downloaded",
                        "used_url": download_url,
                        "final_url": final_url,
                        "content_type": content_type,
                        "size_bytes": target.stat().st_size,
                        "sha256": sha256_file(target),
                    }
                )
                return result

            except Exception as exc:  # noqa: BLE001
                errors.append(f"{download_url} attempt {attempt}: {type(exc).__name__}: {exc}")
                if attempt <= retries:
                    time.sleep(sleep_seconds)

        # Try next fallback URL.
        time.sleep(sleep_seconds)

    result["status"] = "failed"
    result["error"] = errors[-1] if errors else "unknown error"
    result["all_errors"] = errors
    return result


def discover_awv_assets(repo_root: Path, *, timeout: int, retries: int, sleep_seconds: float) -> Dict[str, Any]:
    result: Dict[str, Any] = {
        "source_id": AWV_ASSET_SOURCE["source_id"],
        "title": AWV_ASSET_SOURCE["title"],
        "section": AWV_ASSET_SOURCE["section"],
        "status": "not_started",
        "discovered_links": [],
        "errors": [],
        "targets": AWV_ASSET_SOURCE["targets"],
    }

    all_links: List[str] = []
    for page_url in AWV_ASSET_SOURCE["page_urls"]:
        for attempt in range(1, retries + 2):
            try:
                html, final_url, content_type = request_url(page_url, timeout=timeout)
                parser = LinkExtractor(final_url)
                parser.feed(html.decode("utf-8", errors="replace"))
                links = parser.links
                all_links.extend(links)
                result["page_used"] = page_url
                result["page_final_url"] = final_url
                result["page_content_type"] = content_type
                break
            except Exception as exc:  # noqa: BLE001
                result["errors"].append(f"{page_url} attempt {attempt}: {type(exc).__name__}: {exc}")
                if attempt <= retries:
                    time.sleep(sleep_seconds)

        if all_links:
            break

    # Prefer links that look like AWV/download assets and contain target suffixes.
    asset_links = []
    for link in all_links:
        lower = link.lower()
        if any(lower.split("?")[0].endswith(ext) for ext in (".pdf", ".docx")):
            if "verfahrensdokumentation" in lower or "belegablage" in lower or "awv" in lower:
                asset_links.append(link)

    # Deduplicate while preserving order.
    seen = set()
    deduped = []
    for link in asset_links:
        if link not in seen:
            seen.add(link)
            deduped.append(link)

    result["discovered_links"] = deduped
    if not deduped:
        result["status"] = "manual_review_no_assets_discovered"
        return result

    result["status"] = "assets_discovered"
    return result


def download_awv_assets(
    repo_root: Path,
    *,
    force: bool,
    dry_run: bool,
    timeout: int,
    retries: int,
    sleep_seconds: float,
) -> List[Dict[str, Any]]:
    discovery = discover_awv_assets(repo_root, timeout=timeout, retries=retries, sleep_seconds=sleep_seconds)
    outputs: List[Dict[str, Any]] = [discovery]

    if discovery["status"] != "assets_discovered":
        return outputs

    by_ext: Dict[str, str] = {}
    for link in discovery["discovered_links"]:
        ext = Path(urllib.parse.urlparse(link).path).suffix.lower()
        if ext in (".pdf", ".docx") and ext not in by_ext:
            by_ext[ext] = link

    for ext, target_rel in AWV_ASSET_SOURCE["targets"].items():
        source_id = f"awv_template_asset_{ext.lstrip('.')}"
        if ext not in by_ext:
            outputs.append(
                {
                    "source_id": source_id,
                    "title": f"AWV Muster-Verfahrensdokumentation asset {ext}",
                    "target_path": target_rel,
                    "status": "manual_review_no_matching_asset_link",
                    "reason": f"No {ext} link discovered on AWV page.",
                }
            )
            continue

        synthetic_source = Source(
            source_id=source_id,
            priority="P0",
            title=f"AWV Muster-Verfahrensdokumentation asset {ext}",
            target_path=target_rel,
            capture_method="direct_file",
            urls=[by_ext[ext]],
            section="optional_download_because_pdf_or_asset_missing",
            reason=AWV_ASSET_SOURCE["reason"],
            risk_flags=("template",),
        )
        outputs.append(
            download_source(
                repo_root,
                synthetic_source,
                force=force,
                dry_run=dry_run,
                no_jina=True,
                timeout=timeout,
                retries=retries,
                sleep_seconds=sleep_seconds,
            )
        )

    return outputs


def find_repo_root(start: Path) -> Path:
    current = start.resolve()
    for p in [current] + list(current.parents):
        if (p / ".git").exists() or (p / "apex-meta").exists():
            return p
    return current


def load_existing_manifest(repo_root: Path) -> Dict[str, Any]:
    manifest_path = repo_root / KB_REL / "manifests/source-manifest.json"
    if not manifest_path.exists():
        return {"manifest_path": str(manifest_path), "exists": False}
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
        paths = [s.get("source_path") for s in data.get("sources", []) if isinstance(s, dict)]
        return {
            "manifest_path": str(manifest_path),
            "exists": True,
            "source_count": len(data.get("sources", [])),
            "source_paths": paths,
        }
    except Exception as exc:  # noqa: BLE001
        return {"manifest_path": str(manifest_path), "exists": True, "parse_error": str(exc)}


def write_report(repo_root: Path, report: Dict[str, Any]) -> Path:
    reports_dir = repo_root / REPORTS_REL
    reports_dir.mkdir(parents=True, exist_ok=True)
    stamp = _dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    path = reports_dir / f"missing-source-download-report_{stamp}.json"
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download missing Safer Space e.V. tax/accounting sources into the KB raw/refs folder."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=None,
        help="Path to apexai-os-meta repo root. Defaults to current repo/root detection.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing non-empty target files.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not download; only report what would happen.",
    )
    parser.add_argument(
        "--no-jina",
        action="store_true",
        help="Do not use Jina Reader for HTML pages; save direct HTML responses into .md targets.",
    )
    parser.add_argument(
        "--skip-optional",
        action="store_true",
        help="Only download core_missing_p0_p1 sources; skip optional PDF/DOCX assets.",
    )
    parser.add_argument(
        "--skip-awv-discovery",
        action="store_true",
        help="Do not attempt AWV PDF/DOCX link discovery.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=45,
        help="Request timeout in seconds.",
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=2,
        help="Retries per URL after the first attempt.",
    )
    parser.add_argument(
        "--sleep",
        type=float,
        default=1.0,
        help="Seconds to sleep between retries/downloads.",
    )
    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    args = parse_args(argv)
    repo_root = args.repo_root.resolve() if args.repo_root else find_repo_root(Path.cwd())

    report: Dict[str, Any] = {
        "generated_at": utc_now_iso(),
        "script": Path(__file__).name,
        "repo_root": str(repo_root),
        "kb_root": str(repo_root / KB_REL),
        "dry_run": bool(args.dry_run),
        "force": bool(args.force),
        "no_jina": bool(args.no_jina),
        "manifest": load_existing_manifest(repo_root),
        "results": {
            "core_missing_p0_p1": [],
            "optional_download_because_pdf_or_asset_missing": [],
            "manual_review_before_download": MANUAL_REVIEW,
        },
    }

    print(f"[INFO] Repo root: {repo_root}")
    print(f"[INFO] KB root:   {repo_root / KB_REL}")
    print(f"[INFO] Dry run:   {args.dry_run}")
    print(f"[INFO] Force:     {args.force}")

    all_core = CORE_SOURCES
    for idx, source in enumerate(all_core, start=1):
        print(f"[CORE {idx}/{len(all_core)}] {source.source_id} -> {source.target_path}")
        res = download_source(
            repo_root,
            source,
            force=args.force,
            dry_run=args.dry_run,
            no_jina=args.no_jina,
            timeout=args.timeout,
            retries=args.retries,
            sleep_seconds=args.sleep,
        )
        print(f"  [{res['status']}] {res.get('used_url') or ''}")
        if res.get("error"):
            print(f"  ERROR: {res['error']}")
        report["results"]["core_missing_p0_p1"].append(res)
        time.sleep(args.sleep)

    if not args.skip_optional:
        for idx, source in enumerate(OPTIONAL_SOURCES, start=1):
            print(f"[OPTIONAL {idx}/{len(OPTIONAL_SOURCES)}] {source.source_id} -> {source.target_path}")
            res = download_source(
                repo_root,
                source,
                force=args.force,
                dry_run=args.dry_run,
                no_jina=True,
                timeout=args.timeout,
                retries=args.retries,
                sleep_seconds=args.sleep,
            )
            print(f"  [{res['status']}] {res.get('used_url') or ''}")
            if res.get("error"):
                print(f"  ERROR: {res['error']}")
            report["results"]["optional_download_because_pdf_or_asset_missing"].append(res)
            time.sleep(args.sleep)

        if not args.skip_awv_discovery:
            print("[OPTIONAL] AWV asset discovery")
            awv_results = download_awv_assets(
                repo_root,
                force=args.force,
                dry_run=args.dry_run,
                timeout=args.timeout,
                retries=args.retries,
                sleep_seconds=args.sleep,
            )
            for item in awv_results:
                print(f"  [{item.get('status')}] {item.get('source_id')}")
            report["results"]["optional_download_because_pdf_or_asset_missing"].extend(awv_results)

    report_path = write_report(repo_root, report)
    print(f"[DONE] Report written: {report_path}")

    failed = []
    for section_results in (
        report["results"]["core_missing_p0_p1"],
        report["results"]["optional_download_because_pdf_or_asset_missing"],
    ):
        for item in section_results:
            if item.get("status") == "failed":
                failed.append(item)

    if failed:
        print(f"[WARN] {len(failed)} download(s) failed. Check the report.")
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
