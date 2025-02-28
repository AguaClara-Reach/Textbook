# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'AguaClara'
copyright = '2025, AguaClara Reach'
author = 'AguaClara Reach'
release = '0.0.0'
# root_doc = 'index'
substitute_path = ['default.yaml']

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.doctest',
              'sphinx.ext.mathjax',
              'sphinx.ext.todo',
              'sphinxcontrib.bibtex',
              'sphinxcontrib.disqus',
              'sphinx_ext_substitution',
              ]


substitute_mode = 'replace'

todo_include_todos = False

# https://sphinxcontrib-bibtex.readthedocs.io/en/2.0.0/usage.html#configuration
bibtex_bibfiles = ['references.bib']
bibtex_default_style = 'alpha'

# disqus_shortname = 'AguaClara'

templates_path = ['_templates']
exclude_patterns = ['_build',
                    'Thumbs.db',
                    '.DS_Store']


numfig = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
# Include the _static directory
html_static_path = ['_static']

# Add custom.css to the list of CSS files to be included in the HTML output
html_css_files = [
    'custom.css',
]

# rinoh_documents = [
#     dict(doc=root_doc, target='aguaclara')
# ]

# -- Options for PDF output --------------------------------------------------

# Grouping the document tree into PDF files. List of tuples
# (source start file, target name, title, author, options).
#
# If there is more than one author, separate them with \\.
# For example: r'Guido van Rossum\\Fred L. Drake, Jr., editor'
#
# The options element is a dictionary that lets you override
# this config per-document. For example:
#
# ('index', 'MyProject', 'My Project', 'Author Name', {'pdf_compressed': True})
#
# would mean that specific document would be compressed
# regardless of the global 'pdf_compressed' setting.

pdf_documents = [
    ('lfom', 'AguaClara', 'AguaClara Textbook', 'AguaClara Reach'),
]

# A comma-separated list of custom stylesheets. Example:
pdf_stylesheets = ['sphinx', 'a4']

# A list of folders to search for stylesheets. Example:
pdf_style_path = ['.', '_styles']

# Create a compressed PDF
# Use True/False or 1/0
# Example: compressed=True
# pdf_compressed = False

# A colon-separated list of folders to search for fonts. Example:
# pdf_font_path = ['/usr/share/fonts', '/usr/share/texmf-dist/fonts/']

# Language to be used for hyphenation support
# pdf_language = "en_US"

# Mode for literal blocks wider than the frame. Can be
# overflow, shrink or truncate
# pdf_fit_mode = "shrink"

# Section level that forces a break page.
# For example: 1 means top-level sections start in a new page
# 0 means disabled
# pdf_break_level = 0

# When a section starts in a new page, force it to be 'even', 'odd',
# or just use 'any'
# pdf_breakside = 'any'

# Insert footnotes where they are defined instead of
# at the end.
# pdf_inline_footnotes = True

# verbosity level. 0 1 or 2
# pdf_verbosity = 0

# If false, no index is generated.
# pdf_use_index = True

# If false, no modindex is generated.
# pdf_use_modindex = True

# If false, no coverpage is generated.
# pdf_use_coverpage = True

# Name of the cover page template to use
# pdf_cover_template = 'sphinxcover.tmpl'

# Documents to append as an appendix to all manuals.
# pdf_appendices = []

# Enable experimental feature to split table cells. Use it
# if you get "DelayedTable too big" errors
# pdf_splittables = False

# Set the default DPI for images
# pdf_default_dpi = 72

# Enable rst2pdf extension modules
# pdf_extensions = []

# Page template name for "regular" pages
# pdf_page_template = 'cutePage'

# Show Table Of Contents at the beginning?
# pdf_use_toc = True

# How many levels deep should the table of contents be?
pdf_toc_depth = 9999

# Add section number to section references
pdf_use_numbered_links = False

# Background images fitting mode
pdf_fit_background_mode = 'scale'

# Repeat table header on tables that cross a page boundary?
pdf_repeat_table_rows = True

# Enable smart quotes (1, 2 or 3) or disable by setting to 0
pdf_smartquotes = 0

import os
import sys
sys.path.insert(0, os.path.abspath('.'))
print(os.path.abspath('.'))
from plants.perseverance.conf import *

#.divina_providencia.conf

latex_engine = 'xelatex'  # Use xelatex for better Unicode support

latex_elements = {
    'title': 'Perseverance Technical Report',
    'papersize': 'a4paper',       # Choose between 'a4paper' or 'letterpaper'
    'pointsize': '12pt',          # Default font size
    'preamble': r'''
        \usepackage{amsmath}
        \usepackage{amssymb}
        \usepackage{longtable} 
        \usepackage{float}  % Ensures precise placement of floats
        \usepackage{graphicx}
        \setmainfont{Times New Roman}

        \let\origfigure\figure
        \let\endorigfigure\endfigure
        \renewenvironment{figure}[1][htbp]{
            \origfigure[H]
        }{
            \endorigfigure
        }
        \let\origtable\table
        \let\endorigtable\endtable
        \renewenvironment{table}[1][htbp]{
            \origtable[H]
        }{
            \endorigtable
        }
    ''',
    'tableofcontents': r'''
        \tableofcontents
        \clearpage
        \setcounter{tocdepth}{2}
    ''',
    'extraclassoptions': 'openany,oneside',
}

