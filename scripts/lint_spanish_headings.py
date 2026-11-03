"""Find untranslated or terminology-invalid headings in the Spanish build."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
import re
import sys


ENGLISH_TITLE_WORDS = re.compile(
    r"\b(?:clarifier|clarification|design|challenge|solution|introduction|"
    r"derivations?|theory|future work|examples?|operation|configuration|"
    r"filter|filtration|flocculator|sedimentation|rapid mix|flow control|"
    r"water treatment)\b",
    re.IGNORECASE,
)
INCORRECT_TERMS = re.compile(r"\b(?:aclaraci[oó]n|aclarador(?:a|es)?)\b", re.IGNORECASE)
FORBIDDEN_VISIBLE_TERMS = re.compile(r"(?<!Sh)\bOStaRS\b")
ENGLISH_ORDER = re.compile(
    r"\b(?:filtro de fl[oó]culos|filtro de arena|tanque de entrada|"
    r"mezcla r[aá]pida|control de flujo)\s+"
    r"(?:diseño|introducci[oó]n|derivaciones|desaf[ií]o|soluci[oó]n)\b",
    re.IGNORECASE,
)
SPANISH_MID_HEADING_CAPITALS = re.compile(
    r"\b(?:Alfa|Ajuste|Apilada|Abierta|Caudal|Componente|Configurable|"
    r"Contracorriente|Control|Corrector|Corriente|Datos|Deflector|Desafíos|"
    r"Desarrollo|Diseño|Dosis|Efectos|Ejemplos|Emisión|Estudio|Filtración|"
    r"Floculación|Floculador|Flujo|Fractal|Geometrías|Hidráulica|Iniciación|"
    r"Inteligente|Lavados|Ley|Lineal|Largometraje|Manta|Mayores|Medición|"
    r"Menor|Mecanizada|Orificios|Paradoja|Parámetros|Parte|Pasos|Pérdida|"
    r"Placas|Prefabricada|Principal|Química|Rápida|Reto|Revisión|Serie|Simple|"
    r"Tanques|Tasa|Teoría|Tuberías|Variables|Volúmenes)\b"
)
UNCHANGED_ALLOWLIST = {
    # Code identifier.
    "Backwash_Inlet",
}


@dataclass(frozen=True)
class Heading:
    level: int
    text: str


class HeadingParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.headings: list[Heading] = []
        self.level = 0
        self.parts: list[str] = []
        self.suppress = 0

    def handle_starttag(self, tag: str, attrs) -> None:
        if re.fullmatch(r"h[1-4]", tag):
            self.level = int(tag[1])
            self.parts = []
        elif self.level and tag == "a" and "headerlink" in dict(attrs).get("class", "").split():
            self.suppress += 1

    def handle_endtag(self, tag: str) -> None:
        if self.suppress and tag == "a":
            self.suppress -= 1
        elif self.level and tag == f"h{self.level}":
            text = " ".join("".join(self.parts).split())
            self.headings.append(Heading(self.level, text))
            self.level = 0
            self.parts = []

    def handle_data(self, data: str) -> None:
        if self.level and not self.suppress:
            self.parts.append(data)


class VisibleTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.suppress = 0

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag in {"script", "style"}:
            self.suppress += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style"} and self.suppress:
            self.suppress -= 1

    def handle_data(self, data: str) -> None:
        if not self.suppress:
            self.parts.append(data)


def headings(path: Path) -> list[Heading]:
    parser = HeadingParser()
    parser.feed(path.read_text(encoding="utf-8", errors="replace"))
    return parser.headings


def visible_text(path: Path) -> str:
    parser = VisibleTextParser()
    parser.feed(path.read_text(encoding="utf-8", errors="replace"))
    return " ".join("".join(parser.parts).split())


def starts_with_lowercase(text: str) -> bool:
    first_letter = re.search(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]", text)
    return bool(first_letter and first_letter.group().islower())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("english_build", type=Path)
    parser.add_argument("spanish_build", type=Path)
    parser.add_argument("--report-all", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    problems: list[str] = []
    checked = 0

    for english_page in sorted(args.english_build.rglob("*.html")):
        relative = english_page.relative_to(args.english_build)
        spanish_page = args.spanish_build / relative
        if not spanish_page.exists():
            problems.append(f"{relative}: Spanish page is missing")
            continue
        # The bilingual glossary intentionally names the legacy English
        # abbreviation OStaRS while defining the preferred Spanish term FRAMCA.
        forbidden = None
        if relative.as_posix() != "glossary.html":
            forbidden = FORBIDDEN_VISIBLE_TERMS.search(visible_text(spanish_page))
        if forbidden:
            problems.append(
                f"{relative}: forbidden visible Spanish term: {forbidden.group()!r}"
            )
        english = headings(english_page)
        spanish = headings(spanish_page)
        if len(english) != len(spanish):
            problems.append(
                f"{relative}: heading count differs (English {len(english)}, Spanish {len(spanish)})"
            )
            continue
        for source, target in zip(english, spanish):
            checked += 1
            if args.report_all:
                print(f"{relative}\tH{source.level}\t{source.text}\t{target.text}")
            reasons = []
            if source.text == target.text and target.text not in UNCHANGED_ALLOWLIST:
                reasons.append("untranslated heading")
            if ENGLISH_TITLE_WORDS.search(target.text):
                reasons.append("English title word")
            if INCORRECT_TERMS.search(target.text):
                reasons.append("incorrect clarification terminology")
            if ENGLISH_ORDER.search(target.text):
                reasons.append("English noun order")
            words_after_first = target.text.split(maxsplit=1)
            if len(words_after_first) > 1 and SPANISH_MID_HEADING_CAPITALS.search(
                words_after_first[1]
            ):
                reasons.append("English title capitalization")
            if starts_with_lowercase(target.text):
                reasons.append("lowercase start")
            if reasons:
                problems.append(
                    f"{relative}: {', '.join(reasons)}: {source.text!r} -> {target.text!r}"
                )

    if problems:
        print("Spanish heading QA failed:", file=sys.stderr)
        for problem in problems:
            print(f"- {problem}", file=sys.stderr)
        return 1
    print(f"Spanish heading QA passed ({checked} headings checked).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
