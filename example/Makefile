
.ONESHELL:

all: example

## create LaTeX table from parameter file
example: example.tex example.py config_params.yml config_macros.yml ../dict2tex.py params.json

	python example.py && \
	pdflatex example.tex && \
	pdflatex example.tex

## generate a mock-up parameter file
params.json: create_params_file.py

	python create_params_file.py

clean:
	-rm -f *~ parameter_table.tex macros.tex example.pdf *.log *.aux *.out  params.json


