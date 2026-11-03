# Textbook [![Documentation](https://github.com/AguaClara/Textbook/workflows/Documentation/badge.svg)](https://aguaclara.github.io/Textbook/)

Please enjoy [the AguaClara textbook](https://aguaclara.github.io/Textbook/)!  
If you are interested in helping out by writing, begin by reading [this page](https://github.com/AguaClara/Textbook/wiki/Contributing-by-writing)!  
If you are interested in helping out by editing existing sections, begin by reading [this page](https://github.com/AguaClara/Textbook/wiki/Contributing-by-editing)!

## Publishing
To publish, first ensure all of your changes have been merged into master by following the Pull Request best practices [here](https://github.com/AguaClara/Textbook/wiki/Contributing-by-writing). Then follow these steps:

1. `git checkout master`
2. `git pull`
3. `git tag <tagname>`
   1. To get `<tagname>`, check the latest release and increment by 1, following semantic versioning. For Example, if the current version were `v0.0.76` and there were only small edits the next would be `v0.0.77`. If there were more significant changes it would be `v0.1.0`, and for extremely large changes (maybe a whole new chapter?), `v1.0.0`.
4. `git push origin <tagname>`

Pushing a tag will kick off the automated release workflow which builds the PDF and HTML documentation.

# Running locally

## VS Code preview with Esbonio

Open the repository root (or `Textbook.code-workspace`) in VS Code and install
the recommended Esbonio extension and Microsoft's Python extension. Use
**Python: Select Interpreter** to select your local Python 3.12 environment.
Install the documentation dependencies into that environment:

```sh
python -m pip install -r requirements-dev.txt
```

Run this command from the repository root in a terminal using the selected
environment. On macOS, use `python3` if your environment does not provide `python`.

Run **Preferences: Open User Settings (JSON)** and set
`esbonio.sphinx.pythonCommand` to that environment's Python executable. For
example, on macOS:

```json
{
  "esbonio.sphinx.pythonCommand": ["/Users/yourname/.pyenv/versions/3.12.2/bin/python3"]
}
```

Or on Windows:

```json
{
  "esbonio.sphinx.pythonCommand": ["C:\\Users\\yourname\\.virtualenvs\\your-environment\\Scripts\\python.exe"]
}
```

Replace the example with your own path. If you already have other User settings,
add this property to the existing object. If you use Pipenv, `pipenv --py` prints
the project's Python executable.

Keep interpreter paths in **User** settings so each contributor can use their
own environment without changing tracked files. Leave
`esbonio.server.pythonCommand` unset to let Esbonio launch its bundled server
using the Python extension; Esbonio also manages its own library paths.
The Sphinx build environment is configured separately as described in the
[Esbonio environment guide](https://docs.esbon.io/en/release/usage/howto/configure-the-sphinx-build-env.html).

Reload VS Code after setup and open an `.rst` file under `Textbook/` to use the
preview. The shared settings build HTML. Personal preview preferences can also be set in User settings.

## PF specifications PDF

Install the documentation dependencies from `requirements-dev.txt`, plus a TeX
installation with XeLaTeX and `latexmk` (for example, MacTeX or TeX Live). From the
repository root, build the standalone PF specifications with:

```sh
python -m sphinx -M latexpdf Textbook Textbook/_build/pf -c Textbook/pdf/pf
```

On macOS, use `python3` if needed. Alternatively, run `make -C Textbook pdf-pf`.
The result is `Textbook/_build/pf/latex/PFSpecifications.pdf`.

The PDF includes a title page dated on the build day, a linked table of
contents, and a list of figures. Figure numbers run continuously throughout
the document. Tables wrap within the text margins, repeat their headers, and can
continue onto another page. References to chapters outside the specifications
link to the online textbook; local figure references link within the PDF.

For the PRDOH Submittal edition, run `make -C Textbook pdf-pf-prdoh` (or use
`python -m sphinx -M latexpdf Textbook Textbook/_build/pf-prdoh -c Textbook/pdf/pf-prdoh`).
The result is `Textbook/_build/pf-prdoh/latex/PFSpecificationsPRDOHSubmittal.pdf`.
This edition adds “PRDOH Submittal” to the cover and PDF title. The cover is
unnumbered; contents, figure list, and body pages use a continuous `4-1`, `4-2`,
`4-3` sequence. The standard PF edition keeps its original pagination.

## Workflow checks

We use [act](https://github.com/nektos/act) to run the workflow locally. After installing act, run `act --container-architecture linux/amd64` in the root directory to see a list of workflows that can be run locally. 

