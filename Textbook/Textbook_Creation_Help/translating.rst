.. _translating_the_textbook:

Translating the Textbook
========================

English is the authoritative source language for the textbook. Spanish is
maintained in gettext PO catalogs so that both editions share the same
structure, equations, figures, cross-references, and source files.

Terminology
-----------

Follow the `English-Spanish technical translation guide
<https://github.com/AguaClara-Reach/Textbook/blob/master/TECHNICAL_TRANSLATION_GUIDE_EN_ES.md>`_
for all technical terminology. Add new terms to that guide when translators
agree on a preferred translation. Product names, equations, chemical formulas,
and SI unit symbols should not be translated.

Updating the Spanish Catalogs
-----------------------------

From the ``Textbook`` directory, extract the current English messages and
merge them into the Spanish catalogs::

   python -m sphinx -b gettext . locale/pot
   sphinx-intl update -p locale/pot -l es

Edit files under ``locale/es/LC_MESSAGES``. Do not edit the generated POT
files to translate content. Changed English messages become fuzzy or
untranslated and are not displayed until they are translated and published by
the automated translation workflow.

Testing
-------

Build both editions before submitting a pull request::

   python -m sphinx -b html . _build/html
   python -m sphinx -b html -D language=es . _build/html/es

Check that cross-references, equations, terminology, units, image captions,
and the language switcher work in both editions. Pull requests automatically
run both builds.

Review Policy
-------------

The Spanish edition is machine translated and clearly identified as such on
every page. Azure translations that pass the structural checks may be
published without prior human review. Corrections from Spanish-speaking
subject-matter reviewers are encouraged, especially for specifications,
operating instructions, safety information, and technical terminology.

RST authoring examples that demonstrate literal backtick and role syntax are
intentionally retained in English. Their purpose is to show the exact source
markup rather than provide textbook content to Spanish readers.

Weblate Integration
-------------------

The repository is ready to connect to a Weblate project. Configure Weblate to
use the POT templates in ``Textbook/locale/pot`` and translations in
``Textbook/locale/<language>/LC_MESSAGES``. Enable Weblate's **Update PO files
to match POT (msgmerge)** add-on for the project. Weblate should submit
translation changes through pull requests so that the bilingual Sphinx build
must pass before catalogs are merged.

The external Weblate project is not created automatically because its hosting,
ownership, access, and reviewer permissions must be selected by an AguaClara
Reach repository administrator.

Automated Translation with Azure
---------------------------------

The repository includes ``scripts/translate_po_azure.py`` for preparing a
terminology-guided machine translation. Copy ``.azure-translator.env.example``
to ``.azure-translator.env`` and enter the resource key, endpoint, and region.
The credentials file is ignored by Git and must never be committed.

Check the connection and preview the quota without modifying catalogs::

   python scripts/translate_po_azure.py --connection-test
   python scripts/translate_po_azure.py --include-fuzzy

Translate and publish a small sample for review::

   python scripts/translate_po_azure.py --catalog AIDE/Specifications_PF.po --limit 20 --translate --publish

After reviewing the sample, translate and publish all remaining and fuzzy
entries with::

   python scripts/translate_po_azure.py --include-fuzzy --translate --publish

The tool protects Sphinx roles, links, substitutions, numbers, and placeholders;
applies multiword terminology from the technical translation guide; rate-limits
requests for the Azure F0 tier; and rejects entries that fail structural checks.
Details of rejected entries are written to
``_build/azure-translation-report.json``.
