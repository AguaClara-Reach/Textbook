# Textbook [![Documentation](https://github.com/AguaClara-Reach/Textbook/actions/workflows/build-docs.yml/badge.svg)](https://aguaclara-reach.github.io/Textbook/)

Please enjoy [the AguaClara textbook](https://aguaclara-reach.github.io/Textbook/)!

If you are interested in helping out by writing, begin by reading [this page](https://github.com/AguaClara-Reach/Textbook/wiki/Contributing-by-writing)!

If you are interested in helping out by editing existing sections, begin by reading [this page](https://github.com/AguaClara-Reach/Textbook/wiki/Contributing-by-editing)!

## Publishing

Every push to `master` automatically builds the textbook and publishes it with GitHub Pages. Pull requests run the same HTML build as a check before merging. A deployment can also be started manually from the **Documentation** workflow in the repository's **Actions** tab.

The publishing workflow keeps the English textbook at the existing URLs and
publishes the developing Spanish edition under
[`/Textbook/es/`](https://aguaclara-reach.github.io/Textbook/es/). Translation
terminology is maintained in
[`TECHNICAL_TRANSLATION_GUIDE_EN_ES.md`](TECHNICAL_TRANSLATION_GUIDE_EN_ES.md).

# Running locally

We use [act](https://github.com/nektos/act) to run the workflow locally. After installing act, run `act --container-architecture linux/amd64` in the root directory to see a list of workflows that can be run locally.

## Client PF specification PDFs

Standalone client PDFs are built from the same
`Textbook/AIDE/Specifications_PF.rst` source used by the online textbook. Client
metadata and pagination are stored as TOML profiles in
`Textbook/pdf/clients/`; do not copy or edit the specification source for a
client edition.

Install the documentation dependencies and a TeX distribution that provides
XeLaTeX and `latexmk`. Then, from the repository root, build the standard or
PRDOH edition with:

```console
python scripts/build_pf_specifications.py --client standard --language en
python scripts/build_pf_specifications.py --client prdoh --language en
```

Spanish uses the same profiles and translated catalog:

```console
python scripts/build_pf_specifications.py --client prdoh --language es
```

The PDFs are written below `_build/pf-<client>-<language>/latex/`. An explicit
delivery path can be supplied with `--output`. Equivalent Make targets are
`make -C Textbook pdf-pf`, `make -C Textbook pdf-pf-prdoh`, and the generic
`make -C Textbook pdf-pf-client PF_CLIENT=prdoh PF_LANGUAGE=es`.

To add a client, copy `Textbook/pdf/clients/standard.toml`, give it a unique
filename and output basename, and edit only its document, cover, and pagination
values. Generated PDFs are deliverables and should normally be distributed as
workflow artifacts or release files rather than committed to the repository.
