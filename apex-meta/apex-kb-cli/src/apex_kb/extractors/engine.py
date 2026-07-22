from __future__ import annotations

import csv
import html
import io
import json
import mimetypes
import re
import zipfile
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET

EXTRACTION_VERSION = "apex.extractors.v2"

TEXT_EXTENSIONS = {
    ".md", ".markdown", ".mdx", ".txt", ".rst", ".adoc", ".py", ".js", ".jsx", ".ts", ".tsx",
    ".java", ".kt", ".kts", ".go", ".rs", ".c", ".h", ".cpp", ".hpp", ".cs", ".swift", ".rb",
    ".php", ".sh", ".bash", ".zsh", ".ps1", ".bat", ".cmd", ".json", ".jsonl", ".ndjson",
    ".yaml", ".yml", ".toml", ".ini", ".cfg", ".conf", ".properties", ".env", ".sql", ".graphql",
    ".gql", ".html", ".htm", ".xml", ".svg", ".css", ".scss", ".sass", ".less", ".csv", ".tsv",
    ".log", ".tex", ".bib", ".mermaid", ".mmd",
}
OOXML_EXTENSIONS = {".docx", ".pptx", ".xlsx"}
PDF_EXTENSIONS = {".pdf"}
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".tif", ".tiff", ".ico"}


def is_text_capable(path: Path) -> bool:
    return path.suffix.lower() in TEXT_EXTENSIONS | OOXML_EXTENSIONS | PDF_EXTENSIONS


def _result(path: Path, status: str, format_name: str, text: str = "", segments: list[dict[str, Any]] | None = None, warnings: list[str] | None = None, error: str | None = None) -> dict[str, Any]:
    return {
        "schema": EXTRACTION_VERSION,
        "status": status,
        "format": format_name,
        "mime_type": mimetypes.guess_type(path.name)[0],
        "text": text,
        "segments": segments or [],
        "warnings": warnings or [],
        "error": error,
    }


def _decode_text(path: Path) -> dict[str, Any]:
    data = path.read_bytes()
    warnings: list[str] = []
    text = ""
    for encoding in ("utf-8-sig", "utf-8", "utf-16", "cp1252"):
        try:
            text = data.decode(encoding)
            if encoding not in {"utf-8-sig", "utf-8"}:
                warnings.append(f"decoded_with_{encoding}")
            break
        except UnicodeDecodeError:
            continue
    else:
        return _result(path, "error", "text", error="unable_to_decode_text")
    if "\x00" in text[:4096]:
        return _result(path, "error", "text", error="binary_content_in_text_extension")
    segments = []
    for line_no, line in enumerate(text.splitlines(), 1):
        if line.strip():
            segments.append({"pointer": f"line:{line_no}", "text": line})
    return _result(path, "success", "text", text=text, segments=segments, warnings=warnings)


def _xml_text(element: ET.Element) -> str:
    parts: list[str] = []
    for node in element.iter():
        if node.text and node.tag.rsplit("}", 1)[-1] in {"t", "instrText"}:
            parts.append(node.text)
    return "".join(parts).strip()


def _docx(path: Path) -> dict[str, Any]:
    with zipfile.ZipFile(path) as archive:
        xml = archive.read("word/document.xml")
    root = ET.fromstring(xml)
    paragraphs: list[dict[str, Any]] = []
    for index, paragraph in enumerate((node for node in root.iter() if node.tag.rsplit("}", 1)[-1] == "p"), 1):
        text = _xml_text(paragraph)
        if text:
            paragraphs.append({"pointer": f"paragraph:{index}", "text": text})
    text = "\n".join(item["text"] for item in paragraphs)
    return _result(path, "success", "docx", text=text, segments=paragraphs)


def _numeric_suffix(name: str) -> int:
    match = re.search(r"(\d+)(?=\D*$)", name)
    return int(match.group(1)) if match else 0


def _pptx(path: Path) -> dict[str, Any]:
    segments: list[dict[str, Any]] = []
    with zipfile.ZipFile(path) as archive:
        slides = sorted((name for name in archive.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)), key=_numeric_suffix)
        for slide_no, name in enumerate(slides, 1):
            root = ET.fromstring(archive.read(name))
            texts = [node.text or "" for node in root.iter() if node.tag.rsplit("}", 1)[-1] == "t"]
            text = " ".join(part.strip() for part in texts if part.strip())
            if text:
                segments.append({"pointer": f"slide:{slide_no}", "text": text})
    return _result(path, "success", "pptx", text="\n".join(item["text"] for item in segments), segments=segments)


def _xlsx(path: Path) -> dict[str, Any]:
    segments: list[dict[str, Any]] = []
    with zipfile.ZipFile(path) as archive:
        shared: list[str] = []
        if "xl/sharedStrings.xml" in archive.namelist():
            root = ET.fromstring(archive.read("xl/sharedStrings.xml"))
            for item in (node for node in root.iter() if node.tag.rsplit("}", 1)[-1] == "si"):
                shared.append(_xml_text(item))
        sheets = sorted((name for name in archive.namelist() if re.fullmatch(r"xl/worksheets/sheet\d+\.xml", name)), key=_numeric_suffix)
        for sheet_no, name in enumerate(sheets, 1):
            root = ET.fromstring(archive.read(name))
            for cell in (node for node in root.iter() if node.tag.rsplit("}", 1)[-1] == "c"):
                ref = cell.attrib.get("r", "?")
                cell_type = cell.attrib.get("t")
                raw_value = None
                inline = None
                for child in cell.iter():
                    local = child.tag.rsplit("}", 1)[-1]
                    if local == "v":
                        raw_value = child.text
                    elif local == "is":
                        inline = _xml_text(child)
                value = inline if inline is not None else raw_value
                if value is None:
                    continue
                if cell_type == "s":
                    try:
                        value = shared[int(value)]
                    except (ValueError, IndexError):
                        pass
                value = str(value).strip()
                if value:
                    segments.append({"pointer": f"sheet:{sheet_no}!{ref}", "text": value})
    return _result(path, "success", "xlsx", text="\n".join(item["text"] for item in segments), segments=segments)


def _pdf(path: Path) -> dict[str, Any]:
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        return _result(path, "unsupported", "pdf", error=f"pypdf_unavailable:{exc}")
    segments: list[dict[str, Any]] = []
    warnings: list[str] = []
    reader = PdfReader(str(path))
    for page_no, page in enumerate(reader.pages, 1):
        try:
            text = (page.extract_text() or "").strip()
        except Exception as exc:  # noqa: BLE001 - extraction boundary
            warnings.append(f"page_{page_no}_extraction_error:{exc}")
            text = ""
        if text:
            segments.append({"pointer": f"page:{page_no}", "text": text})
    status = "success" if segments else "metadata_only"
    return _result(path, status, "pdf", text="\n\n".join(item["text"] for item in segments), segments=segments, warnings=warnings)


def _htmlish(path: Path) -> dict[str, Any]:
    decoded = _decode_text(path)
    if decoded["status"] != "success":
        return decoded
    raw = decoded["text"]
    raw = re.sub(r"(?is)<(script|style).*?>.*?</\1>", " ", raw)
    text = html.unescape(re.sub(r"(?s)<[^>]+>", " ", raw))
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n", text).strip()
    segments = [{"pointer": f"line:{index}", "text": line} for index, line in enumerate(text.splitlines(), 1) if line.strip()]
    return _result(path, "success", "html_or_xml", text=text, segments=segments, warnings=decoded["warnings"])


def _delimited(path: Path) -> dict[str, Any]:
    decoded = _decode_text(path)
    if decoded["status"] != "success":
        return decoded
    delimiter = "\t" if path.suffix.lower() == ".tsv" else ","
    segments: list[dict[str, Any]] = []
    try:
        for row_no, row in enumerate(csv.reader(io.StringIO(decoded["text"]), delimiter=delimiter), 1):
            for column_no, value in enumerate(row, 1):
                if value.strip():
                    segments.append({"pointer": f"row:{row_no}:column:{column_no}", "text": value.strip()})
    except csv.Error as exc:
        return _result(path, "error", "delimited", error=f"csv_parse_error:{exc}")
    return _result(path, "success", "delimited", text="\n".join(item["text"] for item in segments), segments=segments, warnings=decoded["warnings"])


def _json(path: Path) -> dict[str, Any]:
    decoded = _decode_text(path)
    if decoded["status"] != "success":
        return decoded
    try:
        if path.suffix.lower() in {".jsonl", ".ndjson"}:
            values = [json.loads(line) for line in decoded["text"].splitlines() if line.strip()]
        else:
            values = json.loads(decoded["text"])
        text = json.dumps(values, ensure_ascii=False, indent=2, sort_keys=True)
    except json.JSONDecodeError as exc:
        decoded["warnings"].append(f"json_parse_error:{exc}")
        return decoded
    segments = [{"pointer": f"line:{index}", "text": line} for index, line in enumerate(text.splitlines(), 1) if line.strip()]
    return _result(path, "success", "json", text=text, segments=segments, warnings=decoded["warnings"])


def extract_file(path: Path) -> dict[str, Any]:
    suffix = path.suffix.lower()
    try:
        if suffix == ".docx":
            return _docx(path)
        if suffix == ".pptx":
            return _pptx(path)
        if suffix == ".xlsx":
            return _xlsx(path)
        if suffix == ".pdf":
            return _pdf(path)
        if suffix in {".html", ".htm", ".xml", ".svg"}:
            return _htmlish(path)
        if suffix in {".csv", ".tsv"}:
            return _delimited(path)
        if suffix in {".json", ".jsonl", ".ndjson"}:
            return _json(path)
        if suffix in TEXT_EXTENSIONS:
            return _decode_text(path)
        if suffix in IMAGE_EXTENSIONS:
            return _result(path, "metadata_only", "image", warnings=["visual_semantic_route_required"])
        return _result(path, "unsupported", suffix.lstrip(".") or "unknown", error="no_extractor_registered")
    except (OSError, zipfile.BadZipFile, KeyError, ET.ParseError, ValueError) as exc:
        return _result(path, "error", suffix.lstrip(".") or "unknown", error=f"{type(exc).__name__}:{exc}")


def extract_for_policy(path: Path, policy: str) -> dict[str, Any]:
    """Apply the configured non-text contract without hiding any file.

    Native text formats are always extracted. ``inventory_and_report`` keeps
    Office/PDF/image/unknown formats visible as metadata-only or unsupported;
    the other two policies attempt every installed deterministic extractor.
    """
    suffix = path.suffix.lower()
    if policy not in {"inventory_and_report", "extract_when_supported", "block_on_unsupported"}:
        raise ValueError(f"unknown non-text policy: {policy}")
    if policy == "inventory_and_report" and suffix not in TEXT_EXTENSIONS:
        if suffix in OOXML_EXTENSIONS:
            return _result(path, "metadata_only", suffix.lstrip("."), warnings=["extraction_deferred_by_policy"])
        if suffix in PDF_EXTENSIONS:
            return _result(path, "metadata_only", "pdf", warnings=["extraction_deferred_by_policy"])
        if suffix in IMAGE_EXTENSIONS:
            return _result(path, "metadata_only", "image", warnings=["visual_semantic_route_required"])
        return _result(path, "unsupported", suffix.lstrip(".") or "unknown", error="no_extractor_registered")
    return extract_file(path)
