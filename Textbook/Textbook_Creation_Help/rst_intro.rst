.. raw:: html

    <embed>
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>

.. _title_rst_intro:

*********************************************************
Introduction to RST and Sphinx for Textbook Contributors
*********************************************************



.. _heading_what_is_rst:

What is RST?
============

RST stands for ReStructured Text. It is the standard markup language used for documenting python packages. Sphinx_ is the Python package that generates an html website from RST files, and it is what we are using to generate this site. To read more about why we chose RST over markdown or Latex, read the following section, :ref:`heading_why_rst`.


.. _heading_why_rst:

Why RST?
--------
Out of the box, RST supports globally-defined styles, figure numbering and referencing, Latex function rendering, image display customization and more. Furthermore, restructured text was already the language of choice for the AguaClara ecosystem's documentation.



.. _heading_setting_up_rst:

Setting up RST for Development
==============================
There are two ways to *quickly* view an RST file. The first is using an Atom_ plugin that renders the view alongside the source code. This is a good initial test to make sure the RST is proper RST and looks *mostly* correct. However, some functionality, such as any extensions provided by Sphinx_ won't run in the preview. In order to see the final html that will display on the website, you'll need to use the second method, running sphinx locally to fully generate the html code. Once you are satisfied with your work and want to push it to the textbook, you'll need to incorporate it to the master branch. To do so, refer to `Publishing online`_.


.. _heading_installing_atom:

Installing the Atom Plugins
---------------------------
If you are using the Atom IDE to write RST, you can use the `rst-preview-pandoc <https://atom.io/packages/rst-preview-pandoc>`_ plugin to auto-generate a live RST preview within atom (much like the markdown-preview-plus preview page.) To get rst-preview working, you'll need to install `language-restructuredtext <https://atom.io/packages/language-restructuredtext>`_ via atom and Pandoc_ via your command line (``$pip install pandoc``). If everything worked, you can use ``ctrl + shift + e`` to toggle a display window for the live-updated RST preview.


.. _heading_building_rst_locally:

Building RST Locally with Sphinx_
---------------------------------
We use Sphinx_ to build RST locally and remotely. Follow these steps to get Sphinx_ and run it locally:

#. Get `Python 3.5+ <https://www.python.org/downloads/>`_ and pipenv (:code:`$pip install pipenv`)
#. Install all dependencies and setup a virtual environment with :code:`$pipenv install`
#. Whenever you want to issue commands, start your virtual environment with :code:`$pipenv shell` - exit it with :code:`$exit`
#. Generate all the html by navigating in the command line to the source directory /Textbook and creating the build in that directory with the command line :code:`$make html`.
#. View the html generated in the /Textbook/_build directory by copying the full file path of /Textbook/_build/html/index.html and pasting it into your browser.

.. note:: Regarding **1.** the master branch for the package implementing disqus in sphinx `is broken <https://github.com/Robpol86/sphinxcontrib-disqus/pull/7>`_, which is why we use a non-standard pip/online installation. If you already have the incorrect sphinx-disqus version installed, uninstall it with ``pip uninstall sphinxcontrib-disqus`` before installing the functioning version.

.. _heading_building_pdf_locally:

Building PDF Locally
--------------------
To check errors with the PDF generation more quickly, it may be worthwhile to setup your local machine to build the PDF.

  * install `MikTeX <https://miktex.org/howto/install-miktex>`_
  * install `Perl <https://strawberryperl.com/>`_
  * run the command make latexpdf
  * the PDF will be created in the latex folder inside the _build folder



.. _heading_publishing_online:

Publishing Online
-----------------
GitHub Actions builds every pull request with Sphinx and automatically publishes the textbook after changes are merged into ``master``.

#. Test your build by first :ref:`building RST locally <heading_building_rst_locally>`.
#. Submit a `pull request to master <https://github.com/AguaClara-Reach/Textbook/pulls>`_ and request a reviewer. Every pull request **must** be reviewed by at least one other person.
#. Wait for the **Test** workflow to complete successfully in the pull request's checks.
#. After approval, merge the pull request into ``master``. The **Documentation** workflow will build and publish the updated textbook automatically.

.. important:: If the update is not published, check the `Documentation workflow <https://github.com/AguaClara-Reach/Textbook/actions/workflows/build-docs.yml>`_ in GitHub Actions.


.. _heading_testing_online:

Testing Online
--------------
Open a pull request to run the same Sphinx HTML build used by the publishing workflow. The pull request's **Test** check reports whether the textbook builds successfully. For visual review, build the textbook locally and open ``Textbook/_build/html/index.html`` in a browser.


.. _heading_brief_best_practices:

Brief Best Practices
====================
When writing RST, there are often many ways to write the same thing. Almost always, the way with the fewest number of characters is the best way. Ideally, never copy and paste.


.. _heading_how_do_i_write_rst:

How do I write RST?
-------------------

RST is friendly to learn and powerful. There are many useful cheatsheets, like `this one <https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#inserting-code-and-literal-blocks>`_. When you start writing RST, look at the cheat sheets all the time. Use :code:`ctrl-f` all the time to find whatever you need.

**Things not covered in most cheat sheets which are of critical importance:**

* A document is referred to by its title, as defined between the ``*****`` signs at the top of the page, **NOT** the filename. So it is critical to have a title.
* Anything else you'd like to add for the future...


.. _heading_Example_to_start_from:

Example to Start From
---------------------
This file is written in RST. You can start there! Just click on "View page source" at the top of the page.




.. _heading_converting_md_to_rst:

Converting Markdown to RST
==========================
Ideally, use pandoc to do the conversion in the command line: :code:`pandoc --from=markdown --to=rst --output=my_file.rst my_file.md`.
Raw html will not be converted (because it is not actually markdown), and tables are converted poorly.
You'll need to carefully review any page converted with pandoc.

.. _Sphinx: http://www.sphinx-doc.org/en/master/
.. _Pandoc: https://pandoc.org/installing.html
.. _Atom: https://ide.atom.io/
.. _Python: https://www.python.org/downloads/
