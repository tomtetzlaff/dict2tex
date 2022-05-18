'''
Example (mock-up) of a parameter dictionary describing a neuronal network model and its implementation.

The function set_parameter() creates a set of "base" parameters.

The function derived_parameters() generates secondary parameters that are derived from the base parameters.

Each parameter is stored as a subdictionary composed of
- the parameter name (as used in simulation code),
- the parameter value,
- the unit of the parameter,
- a docstring containg a textual description of the parameter, 
- a name of the parameter as used in LaTeX documentations, and
- a label representing the parameter type (e.g., network parameter, neuron parameter, simulation parameter,...).

The latter is useful for structuring the parameter dictionary and for the automatic generation 
of parameter tables in LaTeX.

Note that special characters (such as the backslash "\" often used for LaTeX code) have to be escaped by a backslash. 

The function dict2json() saves the python dictionary to a json file.

(Tom Tetzlaff, 2022)

'''

def set_parameters():

    pars={}

    ## network parameters

    par("N",10000,"",
        "network size","network","$N$",pars)
    
    par("gamma",0.8,"",
        "relative size $N_\\text{E}/N$ of excitatory population","network","$\\gamma$",pars)
    
    ## connectivity parameters
    
    par("K",1000,"",
        "in-degree","connectivity","$K$",pars)

    ## neuron parameters
    
    par("R",10.0,"M$\\Omega$",
        "membrane resistance","neuron","$R$",pars)
    
    par("V_th",15.0,"mV",
        "spike threshold","neuron","$\\theta$",pars)
    
    par("tau_m",10.0,"ms",
        "membrane time constant","neuron","$\\tau_\\text{m}$",pars)

    ## synapse parameters
    
    par("J",50.0,"pA",
        "reference synaptic weight","synapse","$J$",pars)
    
    par("g",5.0,"",
        "relative weight $-J_\\text{I}/J_\\text{E}$ of inhibitory synapses","synapse","$g$",pars)

    ## input parameters
    
    par("rX",20000.0,"spikes/s",
        "rate of external Poisson sources","input","$\\nu_\\text{X}$",pars)

    ## simulation parameters
    
    par("dt",2**-3,"ms",
        "simulation time resolution","simulation","$\\Delta{}t$",pars)
    
    par("seed",1234,"",
        "RNG seed","simulation","$\\xi$",pars)
    
    return pars

def derived_parameters(pars):

    ## derived network parameters

    par("NE",int(pars["gamma"]['value']*pars["N"]['value']),"",
        "size $\gamma{}N$ of excitatory population","network_drvd","$N_\\text{E}$",pars)
    
    par("NI",pars["N"]['value']-pars["NE"]['value'],"",
        "size $(1-\\gamma{})N$ of inhibitory population","network_drvd","$N_\\text{I}$",pars)

    ## derived synapse parameters

    par("JE",pars["J"]['value'],"pA",
        "weight $J$ of excitatory synapses","synapse_drvd","$J_\\text{E}$",pars)
    par("JI",-pars["g"]['value']*pars["J"]['value'],"pA",
        
        "weight $-gJ$ of inhibitory synapses","synapse_drvd","$J_\\text{I}$",pars)

    return pars


##########################################################################

def par(key, value, unit, docstring, section, name, pardict):
    '''
    Constructs an entry in a parameter dictionary pardict
    of type

    pardict[key]={
       'value': value,
       'unit': unit,
       'docstring': doctstring,
       'name': name,
       'section': section
    }

    Arguments:
    ----------
    key: str
    Name of the parameter as used in simulaton code.

    value: int/float/str/...
    Value of the parameter.

    unit: str
    Unit of the parameter.

    docstring: str
    Textual description of the parameter.

    section: str
    Label represeting parameter type.
`   Useful for structuring parameters, and to create distinct tables in LaTeX.

    name: string
    Name of the parameter as used in LaTeX documentation.

    pardict: dict
    Parameter dictionary.

    Returns:
    --------
    - (in-place modification of pardict)

    '''

    if key not in pardict:
        pardict[key]={}
        pardict[key]['name']=name
        pardict[key]['value']=value
        pardict[key]['unit']=unit
        pardict[key]['docstring']=docstring
        pardict[key]['section']=section
    else:
        ## TODO: Think about whether this is a good strategy.
        ## alternative: Raise warning and overwrite dict entries.
        print("Warning: Key %s already existing. Entry ignored." % (key))  
        
##########################################################################

def dict2json(pardict,filename):
    
    import json
    with open(filename, 'w') as fp:
        json.dump(pardict, fp, indent=4)

##########################################################################

if __name__ == "__main__":
    pars = set_parameters()
    pars = derived_parameters(pars)
    dict2json(pars,"params.json")

##########################################################################

