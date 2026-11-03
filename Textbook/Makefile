# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# pdf:
# 	$(SPHINXBUILD) -b rinoh $(SPHINXOPTS) $(TECHNICALREPORT) "$(TECHNICALREPORT)"/pdf

pdf:
	$(SPHINXBUILD) -M latexpdf $(SPHINXOPTS) $(SOURCEDIR) "$(BUILDDIR)"/pdf

PF_CLIENT   ?= standard
PF_LANGUAGE ?= en
PYTHON      ?= python

pdf-pf:
	$(PYTHON) ../scripts/build_pf_specifications.py --client standard --language en

pdf-pf-prdoh:
	$(PYTHON) ../scripts/build_pf_specifications.py --client prdoh --language en

pdf-pf-client:
	$(PYTHON) ../scripts/build_pf_specifications.py --client $(PF_CLIENT) --language $(PF_LANGUAGE)

.PHONY: help Makefile pdf-pf pdf-pf-prdoh pdf-pf-client

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
