"""Add links between equivalent pages in each published language."""

from html import escape


LANGUAGES = (
    ("en", "English"),
    ("es", "Español"),
)


def _page_context(app, pagename, templatename, context, doctree):
    current_language = app.config.language or "en"
    target_uri = app.builder.get_target_uri(pagename)
    base_url = app.config.translation_base_url.rstrip("/")

    links = []
    alternate_tags = []
    for code, label in LANGUAGES:
        language_path = "" if code == "en" else f"/{code}"
        url = f"{base_url}{language_path}/{target_uri}"
        links.append({"code": code, "label": label, "url": url})
        alternate_tags.append(
            f'<link rel="alternate" hreflang="{escape(code)}" '
            f'href="{escape(url)}" />'
        )

    english_url = f"{base_url}/{target_uri}"
    current_path = "" if current_language == "en" else f"/{current_language}"
    current_url = f"{base_url}{current_path}/{target_uri}"
    alternate_tags.extend(
        (
            f'<link rel="alternate" hreflang="x-default" '
            f'href="{escape(english_url)}" />',
            f'<link rel="canonical" href="{escape(current_url)}" />',
        )
    )

    context["current_language"] = current_language
    context["translation_links"] = links
    context["metatags"] = context.get("metatags", "") + "\n" + "\n".join(
        alternate_tags
    )


def setup(app):
    app.add_config_value("translation_base_url", "", "html")
    app.connect("html-page-context", _page_context)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
