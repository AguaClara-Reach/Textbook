"""Standalone, profile-driven PF specifications PDF configuration."""

from pathlib import Path
import os
import re
import runpy
import sys
import tomllib


textbook = Path(__file__).resolve().parents[2]
pdf_root = Path(__file__).resolve().parents[1]
profile_name = os.environ.get("PF_SPEC_PROFILE", "standard")

if not re.fullmatch(r"[A-Za-z0-9_-]+", profile_name):
    raise ValueError(f"Invalid PF specification profile name: {profile_name!r}")

profile_path = pdf_root / "clients" / f"{profile_name}.toml"
if not profile_path.is_file():
    available = ", ".join(sorted(path.stem for path in (pdf_root / "clients").glob("*.toml")))
    raise FileNotFoundError(
        f"Unknown PF specification profile {profile_name!r}. Available profiles: {available}"
    )

with profile_path.open("rb") as profile_file:
    pf_profile = tomllib.load(profile_file)

# Reuse the textbook configuration so extensions, labels, translations, and
# source paths stay consistent with the published HTML textbook.
sys.path.insert(0, str(textbook / "_ext"))
shared = runpy.run_path(str(textbook / "conf.py"))
globals().update({key: value for key, value in shared.items() if not key.startswith("__")})

sys.path.insert(0, str(Path(__file__).resolve().parent))
extensions = list(extensions) + ["pf_pdf"]

templates_path = [str(textbook / "_templates")]
html_static_path = [str(textbook / "_static")]
bibtex_bibfiles = [str(textbook / "references.bib")]

document = pf_profile["document"]
cover = pf_profile.get("cover", {})
pagination = pf_profile.get("pagination", {})

pf_spec_language = os.environ.get(
    "PF_SPEC_LANGUAGE", str(document.get("language", "en"))
)
pf_textbook_url = translation_base_url.rstrip("/")
if pf_spec_language != "en":
    pf_textbook_url += f"/{pf_spec_language}"

latex_documents = [
    (
        "AIDE/Specifications_PF",
        f"{document['output_basename']}.tex",
        document["title"],
        document.get("author", author),
        "manual",
    ),
]
latex_engine = "xelatex"
latex_domain_indices = False
latex_toplevel_sectioning = "section"

# Use a single figure and table sequence for the standalone specification.
numfig_secnum_depth = 0


def _latex_escape(value):
    """Escape profile text before inserting it into generated LaTeX."""

    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(character, character) for character in str(value))


cover_lines = []
for key, label in (
    ("subtitle", ""),
    ("prepared_for", "Prepared for: "),
    ("project", "Project: "),
    ("location", "Location: "),
    ("revision", "Revision: "),
):
    value = str(cover.get(key, "")).strip()
    if value:
        cover_lines.append(_latex_escape(label + value))

specification_url = str(cover.get("specification_url", "")).strip()
if specification_url:
    cover_lines.append(r"\url{" + specification_url.replace("%", r"\%") + "}")

title = _latex_escape(document["title"])
pdf_title = title
subtitle = str(cover.get("subtitle", "")).strip()
if subtitle:
    pdf_title += " - " + _latex_escape(subtitle)

if cover_lines:
    cover_detail = r"\par\medskip ".join(cover_lines)
    maketitle = (
        r"\begingroup\makeatletter"
        r"\def\@title{\texorpdfstring{" + title + "}{" + pdf_title + "}}"
        r"\let\pfOriginalDate\@date"
        r"\def\@date{" + cover_detail + r"\par\medskip\pfOriginalDate}"
        r"\sphinxmaketitle\makeatother\endgroup"
    )
else:
    maketitle = r"\sphinxmaketitle"

contents_numbering = pagination.get("contents_numbering", "roman")
if contents_numbering not in {"roman", "arabic"}:
    raise ValueError("contents_numbering must be 'roman' or 'arabic'")

page_prefix = str(pagination.get("page_prefix", ""))
escaped_prefix = _latex_escape(page_prefix)

tableofcontents = rf"\pagenumbering{{{contents_numbering}}}"
if page_prefix and contents_numbering == "arabic":
    # PRDOH-style pagination is continuous from the contents through the body.
    tableofcontents += r"\renewcommand{\thepage}{" + escaped_prefix + r"\arabic{page}}"
tableofcontents += r"\begingroup\small\tableofcontents\clearpage\phantomsection"
if pagination.get("include_list_of_figures_in_contents", True):
    tableofcontents += r"\addcontentsline{toc}{chapter}{List of Figures}"
tableofcontents += r"\listoffigures\clearpage\endgroup"

if page_prefix and contents_numbering != "arabic":
    tableofcontents += (
        r"\pagenumbering{arabic}"
        r"\renewcommand{\thepage}{" + escaped_prefix + r"\arabic{page}}"
    )
elif not page_prefix:
    tableofcontents += r"\pagenumbering{arabic}"

latex_elements = {
    "papersize": "letterpaper",
    "pointsize": "11pt",
    "extraclassoptions": "oneside,openany",
    "releasename": "",
    "maketitle": maketitle,
    "tableofcontents": tableofcontents,
    "printindex": "",
    "preamble": (
        r"\setlength{\headheight}{28pt}"
        r"\renewcommand{\thesection}{\arabic{section}}"
        r"\usepackage[section]{placeins}"
        r"\hypersetup{pdfborder={0 0 0}}"
        r"\makeatletter"
        r"\renewcommand{\@pnumwidth}{3em}"
        r"\renewcommand{\@tocrmarg}{4em}"
        r"\renewcommand*{\l@figure}[2]{\begingroup"
        r"\renewcommand*{\numberline}[2]{Figure~##1}"
        r"\@dottedtocline{1}{0em}{0em}{#1}{#2}\endgroup}"
        r"\makeatother"
    ),
    "tocdepth": r"\setcounter{tocdepth}{2}",
    "fncychap": "",
    "cmappkg": "",
    "sphinxsetup": "hmargin={1in,1in},vmargin={1in,1in}",
}

release = ""
today_fmt = "%B %d, %Y"

