"""Build a standalone PF specifications PDF from a named client profile."""

from argparse import ArgumentParser
from pathlib import Path
import os
import shutil
import subprocess
import sys
import tomllib


REPOSITORY = Path(__file__).resolve().parents[1]
TEXTBOOK = REPOSITORY / "Textbook"
PROFILE_DIRECTORY = TEXTBOOK / "pdf" / "clients"
CONFIGURATION_DIRECTORY = TEXTBOOK / "pdf" / "pf"


def configure_tex_path(environment):
    """Locate a per-user Windows MiKTeX installation when it is off PATH."""

    if shutil.which("xelatex", path=environment.get("PATH")) and shutil.which(
        "latexmk", path=environment.get("PATH")
    ):
        return

    candidates = []
    if os.name == "nt":
        candidates.extend(
            (
                Path.home() / "AppData/Local/Programs/MiKTeX/miktex/bin/x64",
                Path(os.environ.get("ProgramFiles", "C:/Program Files"))
                / "MiKTeX/miktex/bin/x64",
            )
        )

    for candidate in candidates:
        if (candidate / "xelatex.exe").is_file() and (candidate / "latexmk.exe").is_file():
            environment["PATH"] = str(candidate) + os.pathsep + environment.get("PATH", "")
            return

    raise SystemExit(
        "The PDF build requires XeLaTeX and latexmk. Install MiKTeX or TeX Live "
        "and make those commands available on PATH."
    )


def parse_arguments():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument(
        "--client",
        default="standard",
        help="Client profile name from Textbook/pdf/clients (default: standard)",
    )
    parser.add_argument(
        "--language",
        choices=("en", "es"),
        help="Document language; defaults to the profile language",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional destination path for a copy of the completed PDF",
    )
    parser.add_argument(
        "--keep-going",
        action="store_true",
        help="Ask Sphinx/LaTeX to continue after recoverable errors",
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    profile_path = PROFILE_DIRECTORY / f"{args.client}.toml"
    if not profile_path.is_file():
        available = ", ".join(sorted(path.stem for path in PROFILE_DIRECTORY.glob("*.toml")))
        raise SystemExit(
            f"Unknown client profile {args.client!r}. Available profiles: {available}"
        )

    with profile_path.open("rb") as profile_file:
        profile = tomllib.load(profile_file)

    language = args.language or profile["document"].get("language", "en")
    output_basename = profile["document"]["output_basename"]
    build_directory = REPOSITORY / "_build" / f"pf-{args.client}-{language}"

    environment = os.environ.copy()
    environment["PF_SPEC_PROFILE"] = args.client
    environment["PF_SPEC_LANGUAGE"] = language
    configure_tex_path(environment)

    command = [
        sys.executable,
        "-m",
        "sphinx",
        "-M",
        "latexpdf",
        str(TEXTBOOK),
        str(build_directory),
        "-c",
        str(CONFIGURATION_DIRECTORY),
        "-D",
        f"language={language}",
    ]
    if args.keep_going:
        command.append("--keep-going")

    subprocess.run(command, cwd=REPOSITORY, env=environment, check=True)

    generated_pdf = build_directory / "latex" / f"{output_basename}.pdf"
    if not generated_pdf.is_file():
        raise SystemExit(f"Sphinx completed but did not create {generated_pdf}")

    final_pdf = generated_pdf
    if args.output:
        final_pdf = args.output.expanduser().resolve()
        final_pdf.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(generated_pdf, final_pdf)

    print(final_pdf)


if __name__ == "__main__":
    main()

