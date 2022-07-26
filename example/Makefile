
.ONESHELL:

all: example

## install python package
install: ../dict2tex/dict2tex.py

	cd .. && \
	pip install --upgrade .

## create LaTeX table from parameter file
example: example.tex example.py config.yml params.json ../dict2tex/dict2tex.py

	python example.py && \
	pdflatex --shell-escape example.tex && \
	pdflatex --shell-escape example.tex

## generate a mock-up parameter file
params.json: create_params_file.py

	python create_params_file.py

clean:
	-rm -rf *~ parameter_table.tex macros_table.tex macros.tex example.pdf *.log *.aux *.out *.toc params.json _minted-example


