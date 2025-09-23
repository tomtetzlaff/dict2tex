'''
#This example turns a python dictionary (params.json) containing parameter definitions 
This example turns a yaml file (params.yaml) containing parameter definitions 
into LaTeX code for parameter tables and macro definitions.

Executing this script generates the files 

- parameter_table.tex: table showing parameter names, values, units, and a description,
- macros.tex: LaTeX macro definitions, and
- macros_table.tex: table showing mapping of parameter keys and names to LaTeX macros 

which can be included in a LaTeX source file (see example.tex).

The table styles are configurable (see config.yml).

(Tom Tetzlaff, 2022, 2025)

'''

#import sys
#sys.path.append('../')
import dict2tex
import yaml
from pathlib import Path

#############################            
if __name__ == "__main__":

    config_file = Path('config.yml')

    ## load configurations
    with open(config_file, "r") as stream:    
        config = yaml.safe_load(stream)
        
    ## load parameters
    #parameter_file = Path('params.yaml')
    #with open(parameter_file, "r") as f:
    #    pars = yaml.safe_load(f)        
    
    #pars = dict2tex.load_parameters_from_json(config['params_file'])
    pars = dict2tex.load_parameters_from_json(config['params_file'])        

    ## parameter macro definitions
    dict2tex.tex_macros(pars,config['macros_tex_file'],config['macros_prefix'])     

    ## table with parameter macro definitions and 
    dict2tex.tex_table(pars,\
                       config['macros_table_tex_file'],\
                       config['macros_table_columns'],\
                       config['macros_table_sections'],\
                       section_text_color=config['section_text_color'],\
                       section_title_color=config['section_title_color'],\
                       macro_prefix=config['macros_prefix'])
    
    ## create parameter table
    dict2tex.tex_table(pars,\
                       config['params_table_tex_file'],\
                       config['params_table_columns'],\
                       config['params_table_sections'],\
                       section_text_color=config['section_text_color'],\
                       section_title_color=config['section_title_color'])

    # ## table with parameter macro definitions and 
    # dict2tex.tex_table(pars,\
    #                    config['macros_table_tex_file'],\
    #                    config['macros_table_columns'],\
    #                    config['macros_table_column_widths'],\
    #                    config['macros_table_sections'],\
    #                    section_text_color=config['section_text_color'],\
    #                    section_title_color=config['section_title_color'],\
    #                    macro_prefix=config['macros_prefix'])
    
    # ## create parameter table
    # dict2tex.tex_table(pars,\
    #                    config['params_table_tex_file'],\
    #                    config['params_table_columns'],\
    #                    config['params_table_column_widths'],\
    #                    config['params_table_sections'],\
    #                    section_text_color=config['section_text_color'],\
    #                    section_title_color=config['section_title_color'])

