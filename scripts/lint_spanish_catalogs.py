"""Detect recurring machine-translation failures in Spanish PO catalogs."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

from babel.messages.pofile import read_po


PATTERNS = {
    "drinking-water hallucination": re.compile(r"consumo de alcohol", re.I),
    "broken plant word order": re.compile(
        r"(?:tratamiento de agua plantas|plantas tratamiento de agua|"
        r"planta tratamiento de agua|sistemas? tratamiento de agua|"
        r"procesos? tratamiento de agua)",
        re.I,
    ),
    "broken surface-water phrase": re.compile(
        r"tratamiento de agua superfic(?:ial|iales|ie)", re.I
    ),
    "incorrect safe-water agreement": re.compile(r"agua potable seguros", re.I),
    "incorrect floc spelling": re.compile(
        r"\b(?:fl[oó]cs|flóclos|flocas|flocos|floco|floques|flóculum)\b", re.I
    ),
    "nonpreferred floc-rollup term": re.compile(
        r"\b(?:enrollamiento de flóculos?|rollo de flóculos?|"
        r"rollup (?:del flóculo|de floc)|floc rollup|enrollamiento de floc|"
        r"se enrollen|se enrollarían|minimizar el enrollamiento|"
        r"no enrollándose hacia arriba)\b",
        re.I,
    ),
    "nonstandard backwash term": re.compile(r"\bcontralavad(?:o|os)|contralavar\b", re.I),
    "incorrect clarification term": re.compile(
        r"\b(?:aclaraci[oó]n|aclarador(?:a|es)?)\b", re.I
    ),
    "incorrect grammatical gender": re.compile(
        r"\b(?:el dosis|la caudal|la lecho|el pérdida|la nivel|la filtro)\b", re.I
    ),
    "missing de in water-quality phrase": re.compile(
        r"\b(?:turbidez|calidad) agua\b", re.I
    ),
    "missing de in constant-head tank": re.compile(
        r"\btanque carga constante\b", re.I
    ),
    "nonstandard plate-settler term": re.compile(
        r"\b(?:asentador(?:es)?|sedimentador(?:es)?|estabilizador(?:es)?) de placas\b",
        re.I,
    ),
    "nonpreferred translation of influent": re.compile(
        r"\b(?:afluente|afluentes|influyente|influyentes)\b", re.I
    ),
    "broken settled-water word order": re.compile(
        r"\bagua (?:sedimentada|clarificada) turbidez\b", re.I
    ),
    "incorrect plate-settler gender": re.compile(
        r"\b(?:los|un|del|al|el) placa(?:s)? sedimentadora(?:s)?\b", re.I
    ),
    "nonpreferred pipe-stub term": re.compile(r"\bmuñ(?:ón|ones)\b", re.I),
    "incorrect floc gender": re.compile(r"\blas flóculos\b", re.I),
    "incorrect water article": re.compile(r"\bla agua\b", re.I),
    "nonpreferred particle-settling term": re.compile(
        r"\b(?:asentamiento|asentamientos|asentarse|se asientan|se asiente)\b", re.I
    ),
    "article-noun gender mismatch": re.compile(
        r"\b(?:la (?:manifold|tanque|gradiente|tiempo|flujo|canal|proceso|sistema|lavado)|"
        r"el sedimentación|"
        r"los partículas|las (?:filtros|tanques|procesos)|"
        r"un (?:partícula|turbidez|velocidad|concentración|energía|geometría)|"
        r"una (?:flóculo|filtro|tanque|proceso|sistema|manifold))\b",
        re.I,
    ),
    "broken technical word order": re.compile(
        r"\b(?:velocidad de captura placa sedimentadora|rendimiento placa sedimentadora|"
        r"diseño placa sedimentadora|efluentes agua filtrada|agua cruda caudal|"
        r"mezcla rápida procesos|unidades mezcla rápida|unidad mezcla rápida|"
        r"hélice mezcla rápida|calidad del agua Ingeniería)\b",
        re.I,
    ),
    "known semantic mistranslation": re.compile(
        r"\b(?:partículas en bruto|al agua sucia|espacio de esporas|pozo claro|"
        r"tratamiento de agua de superficie|floculaciones hidráulicas)\b",
        re.I,
    ),
    "translated LaTeX command": re.compile(r"\\(?:derecha|izquierda)\b", re.I),
    "embedded English prose": re.compile(
        r"\b(?:must meet two constraints|file in the aguaclara repository|"
        r"this region is not|we have already solved|now, we can solve|"
        r"the derivation for the equation|access and modify the models)\b",
        re.I,
    ),
    "space before punctuation": re.compile(r"\s+[.,;!?](?:\s|$)"),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "locale_dir",
        nargs="?",
        type=Path,
        default=Path("Textbook/locale/es/LC_MESSAGES"),
    )
    parser.add_argument(
        "--exclude-catalog",
        action="append",
        default=[],
        help="Skip catalogs whose relative path contains this text",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    problems: list[str] = []
    checked = 0
    for path in sorted(args.locale_dir.rglob("*.po")):
        relative = path.relative_to(args.locale_dir)
        if any(value in relative.as_posix() for value in args.exclude_catalog):
            continue
        with path.open(encoding="utf-8") as stream:
            catalog = read_po(stream, locale="es")
        for message in catalog:
            if not message.id or not isinstance(message.string, str):
                continue
            checked += 1
            for label, pattern in PATTERNS.items():
                if relative.as_posix() == "glossary.po" and label == "incorrect floc spelling":
                    # The glossary intentionally names common incorrect forms.
                    continue
                match = pattern.search(message.string)
                if not match:
                    continue
                location = message.locations[0] if message.locations else ("?", "?")
                problems.append(
                    f"{relative}:{location[1]}: {label}: {match.group()!r}"
                )

    if problems:
        print("Spanish catalog QA failed:", file=sys.stderr)
        for problem in problems:
            print(f"- {problem}", file=sys.stderr)
        return 1
    print(f"Spanish catalog QA passed ({checked:,} messages checked).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
