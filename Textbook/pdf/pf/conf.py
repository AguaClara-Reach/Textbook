"""Standalone PF specifications PDF, using the textbook's Sphinx sources."""
from pathlib import Path
import runpy
import sys

textbook = Path(__file__).resolve().parents[2]
globals().update({key: value for key, value in runpy.run_path(str(textbook / 'conf.py')).items() if not key.startswith('__')})

sys.path.insert(0, str(Path(__file__).resolve().parent))
extensions = extensions + ['pf_pdf']

templates_path = [str(textbook / '_templates')]
html_static_path = [str(textbook / '_static')]
bibtex_bibfiles = [str(textbook / 'references.bib')]
latex_documents = [
    ('AIDE/Specifications PF', 'PFSpecifications.tex',
     'Specifications for AguaClara PF Series', 'AguaClara Reach', 'manual'),
]
latex_engine = 'xelatex'
latex_domain_indices = False
latex_toplevel_sectioning = 'section'
# One figure sequence for the entire standalone specification.
numfig_secnum_depth = 0
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '11pt',
    'extraclassoptions': 'oneside,openany',
    'releasename': '',
    'maketitle': r'\sphinxmaketitle',
    'tableofcontents': (r'\pagenumbering{roman}\begingroup\small\tableofcontents'
                        r'\clearpage\phantomsection'
                        r'\addcontentsline{toc}{chapter}{List of Figures}'
                        r'\listoffigures\clearpage\endgroup\pagenumbering{arabic}'),
    'printindex': '',
    'preamble': (r'\setlength{\headheight}{28pt}'
                 r'\renewcommand{\thesection}{\arabic{section}}'
                 r'\usepackage[section]{placeins}'
                 r'\hypersetup{pdfborder={0 0 0}}'
                 # Show only "Figure N ... page" in the list, preserving captions.
                 r'\makeatletter'
                 r'\renewcommand*{\l@figure}[2]{\begingroup'
                 r'\renewcommand*{\numberline}[2]{Figure~##1}'
                 r'\@dottedtocline{1}{0em}{0em}{#1}{#2}\endgroup}'
                 r'\makeatother'),
    'tocdepth': r'\setcounter{tocdepth}{2}',
    'fncychap': '',
    'cmappkg': '',
    'sphinxsetup': 'hmargin={1in,1in},vmargin={1in,1in}',
}
release = ''
today_fmt = '%B %d, %Y'
