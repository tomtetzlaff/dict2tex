# `dict2tex` - Converting parameter dictionaries to LaTeX code

## Purpose

Computational science often deals with mathematical models specified by large sets of parameters. In simulation research, it is common to store information on these parameters in dictionaries mapping parameter names to parameter values, occasionally supplemented by information on physical units and other properties. When documenting models in scientific manuscripts, information on model parameters is typically copied and pasted into the manuscript source code -- a process which is highly error prone and inefficient, in particular, when adjusting parameter values during manuscript production or in the review process. To improve the efficiency, correctness and reproducibility of computational science, it is therefore desirable to base both 

* model documentation, and 
* model implementation 

on identical sources. This is an easy task, provided information on model parameters is stored in dictionaries such as

```json
{
    "N": {
        "name": "$N$",
        "value": 10000,
        "unit": "",
        "docstring": "network size",
        "section": "network"
    },
    "dt": {
        "name": "$\\Delta{}t$",
        "value": 0.125,
        "unit": "ms",
        "docstring": "simulation time resolution",
        "section": "simulation"
    },
}
```

Here, each parameter (such as `N` or `dt`) is not only connected to a `value` and a physical `unit`, but also to a descriptor explaining the meaning of the parameter (`docstring`), LaTeX code for typesetting parameters in LaTeX (`name`), as well as a specification of the parameter type (`section`).

`dict2tex.py` contains a set of python functions that help to automate the conversion of such parameter dictionaries into LaTeX code used for preparing manuscripts. Two typical use cases are automatically generated parameter tables ([example](https://doi.org/10.1371/journal.pcbi.1007790.s002)), and automatically generated files containg LaTeX macros, such as

```tex
macros.tex:
...
\def\PN{\ensuremath{N} }           %% network size
...
\def\Pdt{\ensuremath{\Delta{}t} }  %% simulation time resolution
...
```



## Example

The example in the `example` folder demonstrates how to generate LaTeX macros and parameter tables from a toy parameter set. The full example can be executed by executing

```console
cd example
make
```

which produces the pdf file `example.pdf`.

### File description
* `example/create_params_file.py`: Creates a mock-up parameter set and stores it in `params.json`.
* `example/example.py`: Loads `params.json` and converts it to

   - a LaTeX file `parameter_table.tex` containing a parameter table, and
   - a LaTeX file `macros.tex` containing macro definitions.

* `example/example.tex`: LaTeX main manuscript importing and using `macros.tex` and `parameter_table.tex`.
* `example/config.yml`: Configuration file used to select and format parameter sections and table columns.

## Requirements
The code and the example have been tested with `python 3.9`, and depend only on basic python packages such as `json`, `numpy`, and `yaml`.
