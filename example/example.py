'''
This example demonstrates how a python dictionary containg a number of parameter sets can 
be turned into a LaTeX ("Nordlie") table.

Executing this script generates a file parameter_table.tex, which can be included 
in a LaTeX source file (see example.tex).

(Tom Tetzlaff, 2022)

'''

import os
import sys
sys.path.append('../')

import yaml
import dict2tex

#############################            
if __name__ == "__main__":

    config_file = 'config.yml'

    ## load configuration 
    with open(config_file, "r") as stream:    
        config = yaml.safe_load(stream)
        
    tex_file = config['tex_file']               
    params_file_json = config['params_file']    
    table_columns = config['table_columns']
    table_column_widths = config['table_column_widths']    
    table_sections = config['table_sections']
    
    ## load parameters
    pars = dict2tex.load_parameters_from_json(params_file_json)    

    ## prepare table and set table header
    dict2tex.tex_table_header(tex_file, table_columns, table_column_widths)

    ## print core of the table for all sections
    dict2tex.tex_table_core(pars, tex_file, table_columns, table_sections)
                
    ## close table
    dict2tex.tex_table_footer(tex_file)

