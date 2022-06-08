'''
Collection of functions used to convert parameter dictionaries into LaTeX code.

(Tom Tetzlaff, 2022)

'''

import numpy as np

##################################################

def load_parameters_from_json(filename):
    '''
    Reads parameter data from json file into a python dictionary.

    Arguments:
    ----------
    filename: str
    Name of json file containing parameter definitions.

    Returns:
    --------
    pars: dict
    Parameter dictionary.

    '''

    import json
    
    with open(filename, 'r') as fp:
        pars = json.load(fp)
        
    return pars

##################################################

def get_section_subdict(pardict,section):
    '''
    Extracts all entries from pardict corresponding to a given section.

    Arguments:
    ----------
    pardict: dict
    Parameter dictionary.

    section: str
    Section name.

    Returns:
    --------
    subdict: dict
    Dictionary containing subset of parameters with matching section.
    '''
    
    subdict={}
    for k in pardict:
        if pardict[k]['section'] == section:
            subdict[k]=pardict[k]
    return subdict

##################################################

def tex_table_header(texfile,table_columns,table_column_widths=None):
    '''
    Creates header of the LaTeX table.

    Arguments:
    ----------
    texfile: str
    Name of the LaTeX file.

    table_columns: list(dict)
    List of dictionaries defining table columns (field and title).

    table_column_widths: list(float) or None
    List of relative columns widths. If None, column widths are automatically chosen by LaTeX.

    Returns:
    --------
    -

    '''

    n_columns =  len(table_columns)
    
    f=open(texfile, 'w')
        
    if table_column_widths == None:
        f.write(r"\begin{tabular}{|%s}" % (n_columns*"l|") + "\n")
    else:

        if len(table_column_widths) != n_columns:
            raise Exception("Number of elements in 'table_column_widths' must match number of columns.")

        table_column_widths_norm = np.array(table_column_widths)/np.sum(table_column_widths)

        table_format_str = r"|"
        for w in table_column_widths_norm:
            table_format_str += r"p{%.3f\linewidth}|" % (w)
    
        f.write(r"\begin{tabular}{%s}" % (table_format_str) + "\n")

    f.write(r"\hline" + "\n")

    for c in range(n_columns):
        f.write(r"\textbf{%s}" % (table_columns[c]['title'])) ## column title        
        if c<n_columns-1:
            f.write(r"  &  ")  ## column separator

    f.write(r"\\" + "\n")
    f.write(r"\hline" + "\n")
    f.close()

def tex_table_footer(texfile):
    '''
    Creates footer of the LaTeX table.

    Arguments:
    ----------
    texfile: str
    Name of the LaTeX file.

    Returns:
    --------
    -

    '''

    f=open(texfile, 'a')
    f.write(r"\end{tabular}\\" + "\n")
    f.close()

##################################################
def tex_table_core(pars,tex_file,table_columns,table_sections,section_text_color,section_title_color,macro_prefix='P'):
    '''
    Generates LaTeX code for a parameter table composed of several sections.

    Arguments:
    ----------
    pars: dict
    Parameter dictionary (containing all parameter sections).

    texfile: str
    Name of the target LaTeX file.

    table_columns: list(dict)
    List of dictionaries defining table columns (field and title).

    table_sections: list(dict)
    List of dictionaries defining table sections to be printed, section titles, and text color.

    section_text_color: str

    section_title_color: str


    macro_prefix: str
    Prefix used for LaTeX macro names.

    Returns:
    --------
    -

    '''
    
    for cs in range(len(table_sections)):
        section = table_sections[cs]['section']
        if 'title' in table_sections[cs].keys():                
            section_title = table_sections[cs]['title']
        else:
            section_title = None
        if 'color' in table_sections[cs].keys():        
            section_color = table_sections[cs]['color']
        else:
            section_color = section_text_color
        if 'title_color' in table_sections[cs].keys():
            section_title_color = table_sections[cs]['title_color']
        else:
            section_title_color = section_title_color
        pars_section = get_section_subdict(pars,section)
        
        tex_subtable(pars_section,section_title,table_columns,tex_file,section_color,section_title_color,macro_prefix)

##################################################

def tex_subtable(pars_section,section_title,table_columns,texfile,color='black',section_title_color='lightgray',macro_prefix='P'):
    '''
    Generates LaTeX code for a subtable describing a parameter section.

    Arguments:
    ----------
    pars_section: dict
    Parameter subdictionary corresponding to some parameter section.

    section_title: str
    (Sub-)table header.
    
    table_columns: list(dict)
    List of dictionaries defining table columns (field and title).

    texfile: str
    Name of the LaTeX file.

    color: str
    LaTeX color used for the corresponding text (default: 'black').

    section_title_color: str
    Background color of section title (default: 'lightgray').

    macro_prefix: str
    Prefix used for LaTeX macro names.

    Returns:
    --------
    -

    '''

    n_columns =  len(table_columns)

    f=open(texfile, 'a')
    if section_title!=None:
        f.write(r"\multicolumn{%d}{|>{\columncolor{%s}}c|}{\textbf{%s}}\\" % (n_columns,section_title_color,section_title) + "\n")
        f.write(r"\hline" + "\n")

    for k in pars_section:
        for c in range(n_columns):
            field = table_columns[c]['field']

            ## turn field into a list unless it is already a list to avoid redundant code
            if type(field)!=list:
                field = [field]
            
            for cf,fld in enumerate(field):  ## necessary to handle case where column consist of multiple fields

                ## field specific text formatting
                prefix = ''
                if fld == 'key':
                    value = k
                elif fld == 'macro':
                    value = k
                    prefix = macro_prefix
                else:
                    value = pars_section[k][fld]
                fld_str = convert_field_to_tex_string(value, fld, prefix=prefix)
                
                ## define text color
                #f.write(r"\textcolor{%s}{%s}" % (color,fld_str))  ## not working with \verb
                f.write(r"{\noindent\color{%s}{}%s}" % (color,fld_str))

                ## add space between fields combined in one column
                if cf<len(field)-1:
                    f.write(r"\,") 

            ## add column separator
            if c<n_columns-1:
                f.write(r"  &  ")  
                
        f.write(r"\\" + "\n")
 
        f.write(r"\hline" + "\n")        
    f.close()

##################################################

def tex_table(pars,params_tex_file,table_columns,table_column_widths,table_sections,section_text_color='black',section_title_color='lightgray',macro_prefix='P'):
    '''
    Create LaTeX code for parameter table with parameter definitions extracted from a parameter json file.

    Arguments:
    ----------
    pars: dict
    Parameter dictionary.

    params_tex_file: str
    Name of the target LaTeX file containg parameter table.

    table_columns: list(dict)
    List of dictionaries defining table columns (field and title).

    table_column_widths: list(float) or None
    List of relative columns widths. If None, column widths are automatically chosen by LaTeX.

    table_sections: list(dict)
    List of dictionaries defining table sections to be printed, section titles, and text color.

    section_text_color: str
    ...

    section_title_color: str
    ...

    macro_prefix: str
    Prefix used for LaTeX macro names.

    Returns:
    --------
    -

    '''

    #### prepare table and set table header
    tex_table_header(params_tex_file, table_columns, table_column_widths)
    
    #### print core of the table for all sections
    tex_table_core(pars, params_tex_file, table_columns, table_sections,section_text_color,section_title_color,macro_prefix=macro_prefix)                
    #### close table
    tex_table_footer(params_tex_file)

##################################################

def convert_field_to_tex_string(field, field_type, prefix=''):
    '''
    Converts a given parameter field into an appropriate LaTeX string with type dependent formatting.

    Arguments:
    ----------
    field: int, float, str or lists thereof
    Parameter field to be converted to LaTeX string.

    field_type: str
    Type of the field, such as 'value', 'unit', 'docstring', 'section', 'key', 'macro'.

    prefix: str
    Prefix to be used for macros (optional)

    Returns:
    --------
    field_str: str
    LaTeX string.

    '''

    # math mode for numerical values, simple string else
    if field_type == 'value' and type(field)!=str:    
        field_str = r"$%s$" % field

    # verbatim (typewriter) for keys        
    elif field_type == 'key':                         
        field_str = r"\verb+%s+" % field

    # verbatim for macros, remove characters such as "_", add prefixes, e.g., "\P"         
    elif field_type == 'macro':                       
        field_str = r"\verb+\%s%s+" % (prefix,field)
        field_str = field_str.replace('_','')   ## remove underscores "_'

    # no formatting if
    # field_type == 'value' and type(field)==str: string, or
    # field_type == 'unit': string, or
    # field_type == 'docstring': string        
    else:
        field_str = "%s" % (field)

    return field_str

##################################################

def tex_macros(pars,macros_tex_file,macros_prefix='P'):
    '''
    Create LaTeX code for parameter macro definitions and writes it to file.

    Note: LateX macros names match the key names in the parameter dictionary, 
    with prefix "P" added to avoid colliusion with existing LaTeX function names.
    Underscores "_" are removed from macros names.

    Arguments:
    ----------
    pars: dict
    Parameter dictionary.

    macros_tex_file: str
    Name of the target LaTeX file containg macro definitions.

    Returns:
    --------
    -

    '''
        
    f=open(macros_tex_file, 'w')
    for key in pars:
        key_str = r"%s" % key
        key_str = key_str.replace('_','')   ## remove underscores "_'

        name_str = pars[key]['name']
        name_str = name_str.replace('$','')   ## remove dollar signs
        
        ## macro_prefix added to avoid collision with existing latex function names
        #f.write(r"\newcommand{\P%s}{\ensuremath{%s}}     %%%% %s" % (key_str,name_str,pars[key]['docstring']) + "\n")  
        f.write(r"\def\%s%s{\ensuremath{%s} }     %%%% %s" % (macros_prefix,key_str,name_str,pars[key]['docstring']) + "\n")  

    f.close()
    
##################################################

