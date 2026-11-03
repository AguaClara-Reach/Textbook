"""PRDOH submittal edition of the standalone PF specifications."""
from pathlib import Path
import runpy

shared = runpy.run_path(str(Path(__file__).resolve().parents[1] / 'pf' / 'conf.py'))
globals().update({key: value for key, value in shared.items() if not key.startswith('__')})

latex_documents = [
    ('AIDE/Specifications PF', 'PFSpecificationsPRDOHSubmittal.tex',
     'Specifications for AguaClara PF Series', 'AguaClara Reach', 'manual'),
]
latex_elements = dict(latex_elements)
# Reserve enough room for prefixed page numbers in both contents lists.
latex_elements['preamble'] += (
    r'\makeatletter\renewcommand{\@pnumwidth}{3em}'
    r'\renewcommand{\@tocrmarg}{4em}\makeatother'
)
# The standard cover renders the date in its own large-font block. Add the
# submittal label to that block while keeping the main title's existing size.
latex_elements['maketitle'] = (
    r'\begingroup\makeatletter'
    r'\def\@title{\texorpdfstring{Specifications for AguaClara PF Series}'
    r'{Specifications for AguaClara PF Series - PRDOH Submittal}}'
    r'\let\pfOriginalDate\@date'
    r'\def\@date{PRDOH Submittal\par\medskip\pfOriginalDate}'
    r'\sphinxmaketitle\makeatother\endgroup'
)
# Cover unnumbered; all subsequent pages use one continuous section-4 sequence.
latex_elements['tableofcontents'] = (
    latex_elements['tableofcontents']
    .removesuffix(r'\pagenumbering{arabic}')
    .replace(r'\phantomsection\addcontentsline{toc}{chapter}{List of Figures}', '')
    .replace(r'\pagenumbering{roman}',
             r'\pagenumbering{arabic}\renewcommand{\thepage}{4-\arabic{page}}')
)
