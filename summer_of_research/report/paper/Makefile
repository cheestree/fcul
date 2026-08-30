PDF = main.pdf

all: $(PDF)

%.pdf: %.tex references.bib ../acmart.cls ../ACM-Reference-Format.bst
	pdflatex $*
	- bibtex $*
	pdflatex $*
	pdflatex $*

clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.toc *.fdb_latexmk *.fls *.synctex.gz

distclean: clean
	rm -f $(PDF)