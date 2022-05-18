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


def tex_table_core(pars,tex_file, table_columns, table_sections):
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

    Returns:
    --------
    -

    '''
    
    for cs in range(len(table_sections)):
        section = table_sections[cs]['section']
        section_title = table_sections[cs]['title']
        section_color = table_sections[cs]['color']            
        pars_section = get_section_subdict(pars,section)
        
        tex_subtable(pars_section,section_title,table_columns,tex_file,section_color)

        
def tex_subtable(pars_section,section_title,table_columns,texfile,color='black'):
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

    Returns:
    --------
    -

    '''

    n_columns =  len(table_columns)

    f=open(texfile, 'a')
    if section_title!=None:
        f.write(r"\multicolumn{%d}{|>{\columncolor{lightgray}}c|}{\textbf{%s}}\\" % (n_columns,section_title) + "\n")
        f.write(r"\hline" + "\n")

    for k in pars_section:
        for c in range(n_columns):
            field = table_columns[c]['field']        
            if type(field)==list:
                for cf,fld in enumerate(field):            
                    #print("%s" % pars_section[k][f],end='')
                    if fld =='value':   ## use math fonts for values
                        fld_str = r"$%s$" % pars_section[k][fld]
                    else:
                        fld_str = r"%s" % pars_section[k][fld]
                    f.write(r"\textcolor{%s}{%s}" % (color,fld_str))                    
                    if cf<len(field)-1:
                        print("\,",end='')
                        f.write(r"\,")  ## space between fields combined in one column
                #print("\t",end='')
            else:
                #print("%s\t" % pars_section[k][field],end='')
                if field =='value':   ## use math fonts for values
                    field_str = r"$%s$" % pars_section[k][field]
                else:
                    field_str = r"%s" % pars_section[k][field]

                f.write(r"\textcolor{%s}{%s}" % (color,field_str))

            if c<n_columns-1:
                f.write(r"  &  ")  ## column separator
        f.write(r"\\" + "\n")
 
        f.write(r"\hline" + "\n")        
    f.close()

##################################################

