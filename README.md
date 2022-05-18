# `dict2tex` - Tools for converting parameter dictionaries into LaTeX code

## Purpose

Computational science often deals with mathematical models of dynamical systems, which are specificied by large sets of parameters. In many cases, these models have to be evaluated numerically by running simulations. 

In simulation research, it is common to store information on parameters in dictionaries mapping parameter names to parameter values, sometimes supplementing parameters with information on physical units. When documenting models in scientific manuscripts, information on model parameters is typically copied and pasted into the manuscript source code, a process which is highly error prone and ineffcient, in particular, when changing parameter values during manuscript production or in the review process. To reduce the efficiency, correctness and reproducibility of computational science, it is desirable to base both model documentation and implementation on identical sources.

This is an easy task provided information on model parameters is stored in dictionaries such as

```
{
    "N": {
        "name": "$N$",
        "value": 10000,
        "unit": "",
        "docstring": "network size",
        "section": "network"
    }, ...
    "dt": {
        "name": "$\\Delta{}t$",
        "value": 0.125,
        "unit": "ms",
        "docstring": "simulation time resolution",
        "section": "simulation"
    }, ...
}
```

Here, each parameter (such as `N` or `dt`) is not only connected to a `value` and a physical `unit`, but also to a descriptor explaining the meaning of the parameter (`docstring`), LaTeX code for typesetting parameters in LaTeX (`name`), as well as a specification of the parameter type (`section`).

`dict2tex` is a set of tools that help to convert such parameter dictionaries into LaTeX code used for preparing manuscripts, such as parameter tables and macros.

## Examples

### Parameter tables

The example in the `example` folder can be executed by invoking `make`.

`example/create_params_file.py`: Creates a mockup-up parameter dictionary and stores it in a json file `params.json`.

`example/example.py`: Loads `params.json` and converts it into a LaTeX `parameter_table.tex`.

`example/example.tex`: LaTeX main manuscript importing `parameter_table.tex`.

`example/config.yml`: Configuration file used to select and format parameter sections and table columns.

### LaTeX macros
TODO: convert dictionary keys to LaTeX macros defining parameter names and style.

## Dependencies
The code and the examples have been tested with `python 3.9`, and depend only on basic packages such as `json`, `numpy`, and `yaml`.
