"""Check that Spanish PO translations preserve RST inline markup.

Empty translations are skipped because Sphinx intentionally falls back to the
source text for equation-only and other language-neutral messages. Numeric-only
differences are also skipped because Spanish prose legitimately converts values
such as ``1.8 billion`` to ``1.800 millones`` or spells out small integers.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from babel.messages.pofile import read_po

from translate_po_azure import validate_translation


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "locale_dir",
        nargs="?",
        type=Path,
        default=Path("Textbook/locale/es/LC_MESSAGES"),
    )
    parser.add_argument("--exclude-catalog", action="append", default=[])
    args = parser.parse_args()

    problems: list[str] = []
    checked = 0
    for path in sorted(args.locale_dir.rglob("*.po")):
        relative = path.relative_to(args.locale_dir)
        if any(value in relative.as_posix() for value in args.exclude_catalog):
            continue
        with path.open(encoding="utf-8") as stream:
            catalog = read_po(stream, locale="es")
        for message in catalog:
            if (
                not message.id
                or not isinstance(message.id, str)
                or not isinstance(message.string, str)
                or not message.string
            ):
                continue
            checked += 1
            errors = [
                error
                for error in validate_translation(message.id, message.string)
                if error != "numbers changed"
            ]
            if not errors:
                continue
            location = message.locations[0] if message.locations else ("?", "?")
            problems.append(
                f"{relative}:{location[1]}: {', '.join(errors)}"
            )

    if problems:
        print("Spanish markup QA failed:")
        for problem in problems:
            print(f"- {problem}")
        return 1
    print(f"Spanish markup QA passed ({checked:,} translations checked).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
