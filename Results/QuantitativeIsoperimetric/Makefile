PAPER := sharp_polygonal_finsler_hadwiger
PYTHON ?= python3
PDFLATEX ?= pdflatex
BIBTEX ?= bibtex

.PHONY: all pdf check clean
all: pdf

pdf: $(PAPER).pdf

$(PAPER).pdf: $(PAPER).tex references.bib Makefile check_build.py
	mkdir -p build
	$(PDFLATEX) -interaction=nonstopmode -halt-on-error -output-directory=build $(PAPER).tex > build/latex-pass1.txt
	BIBINPUTS=.: $(BIBTEX) build/$(PAPER) > build/bibtex.txt
	$(PDFLATEX) -interaction=nonstopmode -halt-on-error -output-directory=build $(PAPER).tex > build/latex-pass2.txt
	$(PDFLATEX) -interaction=nonstopmode -halt-on-error -output-directory=build $(PAPER).tex > build/latex-pass3.txt
	$(PYTHON) check_build.py
	cp build/$(PAPER).pdf $(PAPER).pdf

check:
	$(PYTHON) verify.py --output verification.json

clean:
	rm -rf build
