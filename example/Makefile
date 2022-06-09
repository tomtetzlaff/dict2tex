
.ONESHELL:

all: example

## create LaTeX table from parameter file
example: example.tex example.py config.yml ../dict2tex.py params.json

	python example.py && \
	pdflatex --shell-escape example.tex && \
	pdflatex --shell-escape example.tex

## generate a mock-up parameter file
params.json: create_params_file.py

	python create_params_file.py

clean:
	-rm -f *~ parameter_table.tex macros_table.tex macros.tex example.pdf *.log *.aux *.out *.toc params.json


