"""Make references outside the standalone specification useful web links."""

from urllib.parse import quote

from docutils import nodes
from sphinx import addnodes
from sphinx.transforms.post_transforms import SphinxPostTransform


class LinkTextbookReferences(SphinxPostTransform):
    """Replace cross-document LaTeX references with published HTML links."""

    default_priority = 4  # Run before Sphinx resolves references for LaTeX.
    formats = ("latex",)

    def run(self, **kwargs):
        # Definitions are metadata; rendered substitution uses are already
        # present in the doctree and LaTeX cannot render the definitions.
        for definition in list(self.document.findall(nodes.substitution_definition)):
            definition.parent.remove(definition)

        labels = self.env.domaindata["std"]["labels"]
        equations = self.env.domaindata["math"]["objects"]

        for node in list(self.document.findall(addnodes.pending_xref)):
            target = node["reftarget"]
            if node.get("refdomain") == "std":
                entry = labels.get(target.lower())
                if not entry:
                    continue
                docname, anchor, title = entry
                text = node.astext() if node.get("refexplicit") else title
            elif node.get("refdomain") == "math" and target in equations:
                docname, _ = equations[target]
                anchor = nodes.make_id("equation-" + target)
                text = "in the online textbook"
            else:
                continue

            if docname == self.env.docname:
                continue

            url = (
                self.config.pf_textbook_url.rstrip("/")
                + "/"
                + quote(docname, safe="/")
                + ".html#"
                + quote(anchor)
            )
            node.replace_self(nodes.reference("", text, refuri=url))


def setup(app):
    app.add_config_value(
        "pf_textbook_url",
        "https://aguaclara-reach.github.io/Textbook",
        "env",
    )
    app.add_post_transform(LinkTextbookReferences)
    return {"parallel_read_safe": True, "parallel_write_safe": True}

