"""Translate Sphinx PO catalogs with Azure Translator and structural checks.

The command is deliberately read-only unless ``--translate`` is supplied.
Machine translations are marked fuzzy unless ``--publish`` is also supplied.
"""

from __future__ import annotations

import argparse
from collections import Counter
import html
import json
import os
from pathlib import Path
import re
import sys
import time
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from babel.messages.catalog import Catalog, Message
from babel.messages.pofile import read_po, write_po


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LOCALE = ROOT / "Textbook" / "locale" / "es" / "LC_MESSAGES"
DEFAULT_GUIDE = ROOT / "TECHNICAL_TRANSLATION_GUIDE_EN_ES.md"
DEFAULT_ENV = ROOT / ".azure-translator.env"
REPORT_PATH = ROOT / "_build" / "azure-translation-report.json"

PROTECTED_PATTERNS = (
    r":[A-Za-z][A-Za-z0-9_-]*:`[^`]*`",
    r"``[^`]*``",
    r"(?<!`)`(?!`)",
    r"\*\*",
    r"(?<!\*)\*(?!\*)",
    r"(?<![\w])(?:[A-Za-z][\w.-]*)_(?![\w])",
    r"https?://[^\s<>`]+",
    r"<[^<>\n]+>",
    r"\|[^|\n]+\|",
    r"%\([^)]+\)[#0 +\-.0-9]*[a-zA-Z]",
    r"\{[A-Za-z_][A-Za-z0-9_.-]*\}",
)
PROTECTED_RE = re.compile("|".join(f"(?:{p})" for p in PROTECTED_PATTERNS))
STRICT_PROTECTED_PATTERNS = (
    # Preserve complete inline examples and links. The first expression is
    # intentionally greedy within one line so nested RST teaching examples
    # with three or four backticks remain byte-for-byte intact.
    r"`{2,}[^\n]*`{2,}",
    r"`[^`\n]+`_{0,2}",
    r"\*\*[^*\n]+\*\*",
    r"(?<!\*)\*[^*\n]+\*(?!\*)",
    # Preserve complete numeric expressions, including ordinals, fractions,
    # and ranges, so Azure cannot spell out or alter technical values.
    r"(?<![A-Za-z])[-+]?\d+(?:[.,]\d+)*(?:[eE][-+]?\d+)?"
    r"(?:st|nd|rd|th)?(?:\s*[/–-]\s*\d+(?:[.,]\d+)*)?",
)
STRICT_COMBINED_RE = re.compile(
    "|".join(
        f"(?:{p})" for p in STRICT_PROTECTED_PATTERNS + PROTECTED_PATTERNS
    )
)
NUMBER_RE = re.compile(
    r"(?<![A-Za-z])[-+]?\d+(?:[.,]\d+)*(?:[eE][-+]?\d+)?"
)
WORD_RE = re.compile(r"[A-Za-z]{3,}")
DISPLAY_MATH_RE = re.compile(r"\\(?:begin|end|frac|dfrac|sqrt|mathrm|mathbf|left|right)\b")
HTML_TAG_RE = re.compile(r"</?(?:span|mstrans:dictionary)\b[^>]*>", re.IGNORECASE)


def load_env(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def clean_term(value: str) -> str:
    value = value.replace("**", "").replace("`", "").strip()
    value = value.split(";", 1)[0].strip()
    return value


def load_glossary(path: Path) -> dict[str, str]:
    glossary: dict[str, str] = {}
    section = ""
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            section = line[3:].strip()
            continue
        if section == "Terms requiring contextual translation":
            continue
        if not line.startswith("|") or line.startswith("| ---"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 2 or cells[0].lower() in {"english", "english convention"}:
            continue
        source, target = clean_term(cells[0]), clean_term(cells[1])
        if source and target and len(source.split()) >= 2:
            glossary[source] = target
    return dict(sorted(glossary.items(), key=lambda item: len(item[0]), reverse=True))


def protect_markup(text: str, strict: bool = False) -> tuple[str, dict[str, str]]:
    protected: dict[str, str] = {}

    def replace(match: re.Match[str]) -> str:
        token = f"ZXQPH{len(protected):04d}QXZ"
        protected[token] = match.group(0)
        return f'<span class="notranslate">{token}</span>'

    pattern = STRICT_COMBINED_RE if strict else PROTECTED_RE
    return pattern.sub(replace, text), protected


def apply_glossary(
    text: str, glossary: dict[str, str], protected: dict[str, str]
) -> str:
    for source, target in glossary.items():
        pattern = re.compile(
            rf"(?P<lead>[ \t\u00a0]?)(?P<term>(?<![A-Za-z])"
            rf"{re.escape(source)}(?![A-Za-z]))(?P<trail>[ \t\u00a0]?)",
            re.IGNORECASE,
        )

        def replace(match: re.Match[str]) -> str:
            # Include padding on both sides because Translator may reorder the
            # surrounding words. The padding is normalized after restoration.
            token = f"ZXQPH{len(protected):04d}QXZ"
            protected[token] = f" {target} "
            return f'<span class="notranslate">{token}</span>'

        text = pattern.sub(replace, text)
    return text


def restore_markup(text: str, protected: dict[str, str]) -> str:
    text = html.unescape(HTML_TAG_RE.sub("", text))
    for token, original in protected.items():
        if token not in text:
            raise ValueError(f"Azure changed or removed protected token {token}")
        text = text.replace(token, original)
    if re.search(r"ZXQPH\d+QXZ", text):
        raise ValueError("unrestored protection token remains")
    # Do not strip a space before ``:`` because an RST role can begin there
    # (for example, ``text :math:`x``).
    text = re.sub(r"[ \t]+([,.;!?%\)\]])", r"\1", text)
    text = re.sub(r"([\(\[])[ \t]+", r"\1", text)
    return re.sub(r"[ \t]{2,}", " ", text).strip()


def repair_glossary_spacing(catalog: Catalog, glossary: dict[str, str]) -> int:
    """Repair joined words created around glossary-protected translations."""
    allowed_suffixes = {
        "caudal": ("es",),
        "tratamiento de agua": ("s",),
    }
    repaired = 0
    for message in catalog:
        if not isinstance(message.id, str) or not isinstance(message.string, str):
            continue
        targets = {
            target
            for source, target in glossary.items()
            if re.search(
                rf"(?<![A-Za-z]){re.escape(source)}(?![A-Za-z])",
                message.id,
                re.IGNORECASE,
            )
        }
        updated = message.string
        for target in sorted(targets, key=len, reverse=True):
            pattern = re.compile(re.escape(target), re.IGNORECASE)

            def add_boundaries(match: re.Match[str]) -> str:
                nonlocal repaired
                left = updated[match.start() - 1 : match.start()]
                right = updated[match.end() :]
                add_left = bool(left and left.isalpha())
                allowed = allowed_suffixes.get(target.lower(), ())
                def is_allowed_suffix(suffix: str) -> bool:
                    remainder = right[len(suffix) :]
                    return right.lower().startswith(suffix) and not remainder[
                        :1
                    ].isalpha()

                add_right = bool(right[:1].isalpha()) and not any(
                    is_allowed_suffix(suffix) for suffix in allowed
                )
                if add_left or add_right:
                    repaired += 1
                return (
                    (" " if add_left else "")
                    + match.group(0)
                    + (" " if add_right else "")
                )

            updated = pattern.sub(add_boundaries, updated)
        message.string = updated
    return repaired


def validate_translation(source: str, translated: str) -> list[str]:
    errors: list[str] = []
    # Spanish convention commonly changes decimal points to commas and digit
    # group separators in the opposite direction. Compare the digits and
    # signs as an unordered multiset so translated clause order is also safe.
    def numbers(text: str) -> Counter[str]:
        return Counter(
            token.replace(".", "").replace(",", "").lower()
            for token in NUMBER_RE.findall(text)
        )

    if numbers(source) != numbers(translated):
        errors.append("numbers changed")
    for marker in (":ref:", ":numref:", ":eq:", ":math:"):
        if source.count(marker) != translated.count(marker):
            errors.append(f"{marker} count changed")
    if source.count("`") != translated.count("`"):
        errors.append("backtick count changed")
    if source.count("*") != translated.count("*"):
        errors.append("asterisk count changed")
    if source.count("|") != translated.count("|"):
        errors.append("substitution delimiter count changed")
    return errors


class AzureTranslator:
    def __init__(self, endpoint: str, key: str, region: str) -> None:
        endpoint = endpoint.rstrip("/")
        # Azure lists a regional Cognitive Services endpoint for some resources.
        # Those endpoints require the Translator route, while the dedicated
        # Translator endpoint accepts /translate directly.
        if endpoint.endswith(".api.cognitive.microsoft.com"):
            self.endpoint = endpoint + "/translator/text/v3.0/translate"
        else:
            self.endpoint = endpoint + "/translate"
        self.key = key
        self.region = region

    def translate(self, texts: list[str], retries: int = 5) -> list[str]:
        query = urlencode(
            {"api-version": "3.0", "from": "en", "to": "es", "textType": "html"}
        )
        body = json.dumps([{"Text": text} for text in texts]).encode("utf-8")
        headers = {
            "Content-Type": "application/json; charset=UTF-8",
            "Ocp-Apim-Subscription-Key": self.key,
        }
        if self.region:
            headers["Ocp-Apim-Subscription-Region"] = self.region

        for attempt in range(retries):
            request = Request(f"{self.endpoint}?{query}", data=body, headers=headers)
            try:
                with urlopen(request, timeout=45) as response:
                    payload = json.load(response)
                return [item["translations"][0]["text"] for item in payload]
            except HTTPError as exc:
                details = exc.read().decode("utf-8", errors="replace")
                if exc.code == 429 and attempt + 1 < retries:
                    time.sleep(min(60, 2 ** (attempt + 2)))
                    continue
                raise RuntimeError(f"Azure returned HTTP {exc.code}: {details}") from exc
            except URLError as exc:
                if attempt + 1 < retries:
                    time.sleep(2 ** attempt)
                    continue
                raise RuntimeError(f"Could not reach Azure Translator: {exc}") from exc
        raise RuntimeError("Azure translation failed after retries")


def iter_catalogs(
    locale_dir: Path,
    catalog_filter: str | None,
    exclude_filters: tuple[str, ...] = (),
) -> Iterable[Path]:
    for path in sorted(locale_dir.rglob("*.po")):
        relative = path.relative_to(locale_dir).as_posix()
        if catalog_filter and catalog_filter not in relative:
            continue
        if any(value in relative for value in exclude_filters):
            continue
        yield path


def location_selected(
    message: Message, source_locations: set[tuple[str, int]]
) -> bool:
    if not source_locations:
        return True
    return any(
        line == wanted_line and filename.replace("\\", "/").endswith(wanted_file)
        for filename, line in message.locations
        for wanted_file, wanted_line in source_locations
    )


def translatable_messages(
    catalog: Catalog,
    include_fuzzy: bool,
    retranslate: bool,
    source_locations: set[tuple[str, int]],
) -> list[Message]:
    messages: list[Message] = []
    for message in catalog:
        if not message.id or isinstance(message.id, tuple):
            continue
        if not location_selected(message, source_locations):
            continue
        if message.string and not retranslate and not (
            include_fuzzy and "fuzzy" in message.flags
        ):
            continue
        if not WORD_RE.search(message.id):
            continue
        if DISPLAY_MATH_RE.search(message.id):
            continue
        messages.append(message)
    return messages


def batches(items: list[tuple[Path, Message, str, dict[str, str]]]):
    batch: list[tuple[Path, Message, str, dict[str, str]]] = []
    characters = 0
    for item in items:
        item_characters = len(item[2])
        if batch and (len(batch) >= 20 or characters + item_characters > 4_000):
            yield batch
            batch, characters = [], 0
        batch.append(item)
        characters += item_characters
    if batch:
        yield batch


def write_catalog(path: Path, catalog: Catalog) -> None:
    with path.open("wb") as stream:
        write_po(stream, catalog, width=79, include_previous=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--env-file", type=Path, default=DEFAULT_ENV)
    parser.add_argument("--locale-dir", type=Path, default=DEFAULT_LOCALE)
    parser.add_argument("--guide", type=Path, default=DEFAULT_GUIDE)
    parser.add_argument("--catalog", help="Only catalogs whose relative path contains this text")
    parser.add_argument(
        "--exclude-catalog",
        action="append",
        default=[],
        help="Skip catalogs whose relative path contains this text",
    )
    parser.add_argument("--limit", type=int, help="Maximum number of segments")
    parser.add_argument("--connection-test", action="store_true")
    parser.add_argument("--translate", action="store_true", help="Call Azure and update PO files")
    parser.add_argument("--include-fuzzy", action="store_true")
    parser.add_argument(
        "--retranslate",
        action="store_true",
        help="Replace existing translations (normally used with --source-location)",
    )
    parser.add_argument(
        "--source-location",
        action="append",
        default=[],
        metavar="FILE:LINE",
        help="Only translate messages associated with this source location",
    )
    parser.add_argument(
        "--clear-selected",
        action="store_true",
        help="Clear translations selected by --source-location so English is used",
    )
    parser.add_argument(
        "--copy-source-selected",
        action="store_true",
        help="Use the exact source text for messages selected by --source-location",
    )
    parser.add_argument(
        "--repair-glossary-spacing",
        action="store_true",
        help="Repair joined words around glossary terms in existing translations",
    )
    parser.add_argument(
        "--strict-markup",
        action="store_true",
        help="Protect complete inline markup and numeric expressions",
    )
    parser.add_argument(
        "--publish",
        action="store_true",
        help="Remove fuzzy flags so machine translations appear on the site",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source_locations: set[tuple[str, int]] = set()
    for value in args.source_location:
        try:
            filename, line = value.rsplit(":", 1)
            source_locations.add((filename.replace("\\", "/"), int(line)))
        except (ValueError, TypeError):
            print(f"Invalid --source-location value: {value}", file=sys.stderr)
            return 2
    load_env(args.env_file)
    key = os.getenv("AZURE_TRANSLATOR_KEY", "")
    endpoint = os.getenv("AZURE_TRANSLATOR_ENDPOINT", "")
    region = os.getenv("AZURE_TRANSLATOR_REGION", "")

    if args.connection_test or args.translate:
        if not key or not endpoint:
            print(f"Add the Azure key and endpoint to {args.env_file}", file=sys.stderr)
            return 2
        translator = AzureTranslator(endpoint, key, region)
    else:
        translator = None

    if args.connection_test:
        result = translator.translate(["Water treatment"])[0]
        print(f"Azure connection succeeded: Water treatment -> {result}")
        if not args.translate:
            return 0

    glossary = load_glossary(args.guide)
    catalogs: dict[Path, Catalog] = {}
    prepared: list[tuple[Path, Message, str, dict[str, str]]] = []

    for path in iter_catalogs(
        args.locale_dir, args.catalog, tuple(args.exclude_catalog)
    ):
        with path.open(encoding="utf-8") as stream:
            catalog = read_po(stream, locale="es")
        catalogs[path] = catalog
        for message in translatable_messages(
            catalog,
            args.include_fuzzy,
            args.retranslate or args.clear_selected or args.copy_source_selected,
            source_locations,
        ):
            protected_text, protected = protect_markup(message.id, args.strict_markup)
            prepared_text = apply_glossary(protected_text, glossary, protected)
            prepared.append((path, message, prepared_text, protected))

    if args.limit is not None:
        prepared = prepared[: args.limit]

    if args.repair_glossary_spacing:
        repaired = 0
        changed_paths: set[Path] = set()
        for path, catalog in catalogs.items():
            count = repair_glossary_spacing(catalog, glossary)
            if count:
                repaired += count
                changed_paths.add(path)
                write_catalog(path, catalog)
        print(
            f"Repaired {repaired} glossary boundaries in "
            f"{len(changed_paths)} catalogs."
        )
        return 0

    if args.clear_selected:
        if not source_locations:
            print("--clear-selected requires --source-location", file=sys.stderr)
            return 2
        changed_paths: set[Path] = set()
        for path, message, _, _ in prepared:
            message.string = ""
            message.flags.discard("fuzzy")
            changed_paths.add(path)
        for path in changed_paths:
            write_catalog(path, catalogs[path])
        print(
            f"Cleared {len(prepared)} translations in {len(changed_paths)} catalogs."
        )
        return 0

    if args.copy_source_selected:
        if not source_locations:
            print("--copy-source-selected requires --source-location", file=sys.stderr)
            return 2
        changed_paths: set[Path] = set()
        for path, message, _, _ in prepared:
            message.string = message.id
            message.flags.discard("fuzzy")
            changed_paths.add(path)
        for path in changed_paths:
            write_catalog(path, catalogs[path])
        print(
            f"Copied source text for {len(prepared)} messages in "
            f"{len(changed_paths)} catalogs."
        )
        return 0

    source_characters = sum(len(message.id) for _, message, _, _ in prepared)
    request_characters = sum(len(text) for _, _, text, _ in prepared)
    print(f"Candidate segments: {len(prepared):,}")
    print(f"Source characters: {source_characters:,}")
    print(f"Estimated billable request characters: {request_characters:,}")
    print(f"Glossary phrases available: {len(glossary):,}")
    if not args.translate:
        print("Preview only; add --translate to call Azure.")
        return 0

    report = {"translated": 0, "failed": [], "characters": request_characters}
    changed_paths: set[Path] = set()
    sent_this_minute = 0
    minute_started = time.monotonic()

    for batch in batches(prepared):
        batch_characters = sum(len(item[2]) for item in batch)
        elapsed = time.monotonic() - minute_started
        if elapsed >= 60:
            sent_this_minute, minute_started = 0, time.monotonic()
        if sent_this_minute + batch_characters > 30_000:
            time.sleep(max(0, 60 - elapsed))
            sent_this_minute, minute_started = 0, time.monotonic()

        outputs = translator.translate([item[2] for item in batch])
        sent_this_minute += batch_characters
        batch_changed: set[Path] = set()
        for (path, message, _, protected), output in zip(batch, outputs):
            try:
                translated = restore_markup(output, protected)
                errors = validate_translation(message.id, translated)
                if errors:
                    raise ValueError(", ".join(errors))
                message.string = translated
                if args.publish:
                    message.flags.discard("fuzzy")
                else:
                    message.flags.add("fuzzy")
                changed_paths.add(path)
                batch_changed.add(path)
                report["translated"] += 1
            except ValueError as exc:
                report["failed"].append(
                    {"catalog": str(path.relative_to(ROOT)), "source": message.id, "error": str(exc)}
                )

        for path in batch_changed:
            write_catalog(path, catalogs[path])
        print(f"Translated {report['translated']:,}/{len(prepared):,} segments", flush=True)

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Updated {len(changed_paths)} catalogs; report: {REPORT_PATH}")
    if report["failed"]:
        print(f"Structural QA rejected {len(report['failed'])} translations.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
