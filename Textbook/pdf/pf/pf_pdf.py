"""Keep references outside the standalone PDF useful as web links."""
from urllib.parse import quote

from docutils import nodes
from sphinx import addnodes
from sphinx.transforms.post_transforms import SphinxPostTransform


class LinkTextbookReferences(SphinxPostTransform):
    default_priority = 4  # Before Sphinx resolves references for LaTeX.
    formats = ('latex',)

    def run(self, **kwargs):
        # Substitution definitions are metadata; rendered uses are already copied.
        for definition in list(self.document.findall(nodes.substitution_definition)):
            definition.parent.remove(definition)
        # Use the same local illustrations as the full-size figures in this PDF.
        thumbnails = {'49035a16b895fd8095d17a02': 'Images/LFOM.png',
                      'e71bb0c05d9e7241822776b7': 'Images/doser.png'}
        for image in self.document.findall(nodes.image):
            for document_id, uri in thumbnails.items():
                if image['uri'].startswith('https://cad.onshape.com/api/thumbnails/d/' + document_id + '/'):
                    image['uri'] = uri
                    image['candidates'] = {'*': uri}
                    if uri == 'Images/LFOM.png':
                        # Match the height of the 100px-wide doser thumbnail.
                        # LFOM's portrait aspect ratio makes width alone too large.
                        image.attributes.pop('width', None)
                        image['height'] = '68.43px'

        labels = self.env.domaindata['std']['labels']
        equations = self.env.domaindata['math']['objects']
        for node in list(self.document.findall(addnodes.pending_xref)):
            target = node['reftarget']
            if node.get('refdomain') == 'std':
                entry = labels.get(target.lower())
                if not entry:
                    continue  # Sphinx will report an unknown target.
                docname, anchor, title = entry
                text = node.astext() if node.get('refexplicit') else title
            elif node.get('refdomain') == 'math' and target in equations:
                docname, _ = equations[target]
                anchor = nodes.make_id('equation-' + target)
                # Equation numbers belong to the online chapter, not this PDF.
                text = 'in the online textbook'
            else:
                continue
            if docname == self.env.docname:
                continue
            url = self.config.pf_textbook_url.rstrip('/') + '/' + quote(docname, safe='/') + '.html#' + quote(anchor)
            node.replace_self(nodes.reference('', text, refuri=url))


def setup(app):
    app.add_config_value('pf_textbook_url', 'https://aguaclara-reach.github.io/Textbook', 'env')
    app.add_post_transform(LinkTextbookReferences)
    return {'parallel_read_safe': True, 'parallel_write_safe': True}
