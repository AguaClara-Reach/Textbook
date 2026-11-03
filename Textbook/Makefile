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

pdf-pf:
	$(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)/pf" -c pdf/pf $(SPHINXOPTS) $(O)

pdf-pf-prdoh:
	$(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)/pf-prdoh" -c pdf/pf-prdoh $(SPHINXOPTS) $(O)

.PHONY: help Makefile pdf-pf pdf-pf-prdoh

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
