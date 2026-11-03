"""Create a client-facing Word specification from standalone Sphinx HTML."""

from argparse import ArgumentParser
from datetime import date
from html import escape
from pathlib import Path
import re
import subprocess
from zipfile import ZIP_DEFLATED, ZipFile


SPANISH_MONTHS = (
    "enero",
    "febrero",
    "marzo",
    "abril",
    "mayo",
    "junio",
    "julio",
    "agosto",
    "septiembre",
    "octubre",
    "noviembre",
    "diciembre",
)


def parse_arguments():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("source_html", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--reference-doc", required=True, type=Path)
    parser.add_argument("--prepared-for", required=True)
    parser.add_argument("--project", default="")
    parser.add_argument("--cover-photo", required=True, type=Path)
    parser.add_argument(
        "--specification-url",
        default=(
            "https://aguaclara-reach.github.io/Textbook/es/"
            "AIDE/Specifications_PF.html"
        ),
    )
    return parser.parse_args()


def extract_article(source):
    start_marker = '<div itemprop="articleBody">'
    end_marker = "\n           </div>\n          </div>"
    start = source.find(start_marker)
    if start < 0:
        raise ValueError("Could not find the Sphinx article body")
    start += len(start_marker)
    end = source.find(end_marker, start)
    if end < 0:
        raise ValueError("Could not find the end of the Sphinx article body")

    article = source[start:end]
    article = re.sub(r"<embed>.*?</embed>", "", article, flags=re.DOTALL)
    article = re.sub(
        r'<a class="headerlink"[^>]*>.*?</a>', "", article, flags=re.DOTALL
    )
    return article


def spanish_date(value):
    return f"{value.day} de {SPANISH_MONTHS[value.month - 1]} de {value.year}"


def remove_unreferenced_media(document):
    """Remove media inherited from the reference DOCX but unused in the output."""

    temporary = document.with_suffix(".cleaning.docx")
    with ZipFile(document) as source:
        relationships = "".join(
            source.read(item).decode("utf-8")
            for item in source.namelist()
            if item.startswith("word/_rels/") and item.endswith(".rels")
        )
        referenced_media = set(re.findall(r'Target="media/([^"/]+)"', relationships))

        with ZipFile(temporary, "w", ZIP_DEFLATED) as cleaned:
            for item in source.infolist():
                if item.filename.startswith("word/media/"):
                    media_name = Path(item.filename).name
                    if media_name not in referenced_media:
                        continue
                cleaned.writestr(item, source.read(item.filename))

    temporary.replace(document)


def add_page_numbers(document):
    """Add centered page numbers, hiding the cover and starting the body at 1."""

    relationship_id = "rIdPFPageFooter"
    footer_name = "word/footer-pf-page-number.xml"
    footer = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:p>
    <w:pPr><w:jc w:val="center"/></w:pPr>
    <w:r><w:fldChar w:fldCharType="begin"/></w:r>
    <w:r><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>
    <w:r><w:fldChar w:fldCharType="end"/></w:r>
  </w:p>
</w:ftr>
"""

    temporary = document.with_suffix(".paginating.docx")
    with ZipFile(document) as source:
        files = {item.filename: source.read(item.filename) for item in source.infolist()}

    relationships_name = "word/_rels/document.xml.rels"
    relationships = files[relationships_name].decode("utf-8")
    relationships = relationships.replace(
        "</Relationships>",
        (
            f'<Relationship Id="{relationship_id}" '
            'Type="http://schemas.openxmlformats.org/officeDocument/2006/'
            'relationships/footer" Target="footer-pf-page-number.xml"/>'
            "</Relationships>"
        ),
    )
    files[relationships_name] = relationships.encode("utf-8")

    content_types_name = "[Content_Types].xml"
    content_types = files[content_types_name].decode("utf-8")
    content_types = content_types.replace(
        "</Types>",
        (
            '<Override PartName="/word/footer-pf-page-number.xml" '
            'ContentType="application/vnd.openxmlformats-officedocument.'
            'wordprocessingml.footer+xml"/></Types>'
        ),
    )
    files[content_types_name] = content_types.encode("utf-8")

    document_name = "word/document.xml"
    document_xml = files[document_name].decode("utf-8")
    section_settings = (
        f'<w:footerReference w:type="default" r:id="{relationship_id}"/>'
        '<w:pgNumType w:start="0"/><w:titlePg/>'
    )
    document_xml, replacements = re.subn(
        r"(<w:sectPr\b[^>]*>)",
        lambda match: match.group(1) + section_settings,
        document_xml,
        count=1,
    )
    if replacements != 1:
        raise ValueError("Could not find the Word section settings")
    files[document_name] = document_xml.encode("utf-8")
    files[footer_name] = footer.encode("utf-8")

    with ZipFile(temporary, "w", ZIP_DEFLATED) as updated:
        for name, contents in files.items():
            updated.writestr(name, contents)
    temporary.replace(document)


def main():
    args = parse_arguments()
    source_html = args.source_html.resolve()
    output = args.output.resolve()
    reference_doc = args.reference_doc.resolve()
    cover_photo = args.cover_photo.resolve()

    for path in (source_html, reference_doc, cover_photo):
        if not path.is_file():
            raise SystemExit(f"Required file does not exist: {path}")

    article = extract_article(source_html.read_text(encoding="utf-8"))
    logo = (source_html.parents[1] / "_images" / "ACRlogowithname.png").resolve()
    if not logo.is_file():
        raise SystemExit(f"Required logo does not exist: {logo}")

    cover = f"""
<div style="text-align: center;">
<p><img src="{escape(str(logo))}" alt="AguaClara Reach" style="width: 2.7in;" /></p>
<p>Documento técnico</p>
<h1>Especificaciones de la serie prefabricada</h1>
<h2>Plantas de tratamiento de agua AguaClara</h2>
<p><strong>Preparado para: {escape(args.prepared_for)}</strong><br />
<strong>Proyecto: {escape(args.project)}</strong></p>
<p><img src="{escape(str(cover_photo))}" alt="Planta AguaClara PF70" style="width: 6.2in;" /></p>
<p>{spanish_date(date.today())}</p>
<p><a href="{escape(args.specification_url)}">Versión en línea</a><br />
{escape(args.specification_url)}</p>
</div>
<div class="pagebreak"></div>
"""

    combined_html = source_html.with_name("Specifications_PF_client_docx.html")
    combined_html.write_text(
        "<!doctype html><html lang=\"es\"><head><meta charset=\"utf-8\">"
        "<title>Especificaciones de la serie prefabricada</title></head><body>"
        + cover
        + article
        + "</body></html>",
        encoding="utf-8",
    )

    output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            "pandoc",
            str(combined_html),
            "--from=html",
            "--to=docx",
            f"--reference-doc={reference_doc}",
            f"--resource-path={source_html.parent}:{source_html.parents[1]}:{cover_photo.parent}",
            f"--lua-filter={Path(__file__).with_name('pandoc_pagebreak.lua')}",
            "--metadata=lang:es",
            f"--output={output}",
        ],
        check=True,
    )
    remove_unreferenced_media(output)
    add_page_numbers(output)
    print(output)


if __name__ == "__main__":
    main()
