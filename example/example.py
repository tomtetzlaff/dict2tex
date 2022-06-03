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

    config_file = 'config.yml'

    ## load configurations
    with open(config_file, "r") as stream:    
        config = yaml.safe_load(stream)
        
    ## load parameters
    pars = dict2tex.load_parameters_from_json(config['params_file'])    

    ## parameter macro definitions
    dict2tex.tex_macros(pars,config['macros_tex_file'],config['macros_prefix'])     

    ## table with parameter macro definitions and 
    dict2tex.tex_table(pars,\
                       config['macros_table_tex_file'],\
                       config['macros_table_columns'],\
                       config['macros_table_column_widths'],\
                       config['macros_table_sections'],\
                       config['section_text_color'],\
                       config['section_title_color'],\
                       config['macros_prefix'])
    
    ## create parameter table
    dict2tex.tex_table(pars,\
                       config['params_table_tex_file'],\
                       config['params_table_columns'],\
                       config['params_table_column_widths'],\
                       config['params_table_sections'],\
                       config['section_text_color'],\
                       config['section_title_color'])

