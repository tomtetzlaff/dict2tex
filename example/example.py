'''
This example demonstrates how a python dictionary containg a number of parameter sets can 
be turned into a LaTeX ("Nordlie") table.

Executing this script generates a file parameter_table.tex, which can be included 
in a LaTeX source file (see example.tex).

(Tom Tetzlaff, 2022)

'''

import sys
sys.path.append('../')
import dict2tex
import yaml

#############################            
if __name__ == "__main__":

    config_params_file = 'config_params.yml'
    config_macros_file = 'config_macros.yml'

    ## load configurations
    with open(config_params_file, "r") as stream:    
        config_params = yaml.safe_load(stream)

    with open(config_macros_file, "r") as stream:    
        config_macros = yaml.safe_load(stream)
        
    ## load parameters
    pars = dict2tex.load_parameters_from_json(config_params['params_file'])

    ## parameter macro definitions
    dict2tex.tex_macros(pars,config_macros['macros_tex_file']) 

    ## table with parameter macro definitions and 
    dict2tex.tex_table(pars,\
                       config_macros['params_tex_file'],\
                       config_macros['table_columns'],\
                       config_macros['table_column_widths'],\
                       config_macros['table_sections'])

    ## create parameter table
    dict2tex.tex_table(pars,\
                       config_params['params_tex_file'],\
                       config_params['table_columns'],\
                       config_params['table_column_widths'],\
                       config_params['table_sections'])

