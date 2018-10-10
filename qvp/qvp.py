"""
pyart.retrieve.quasi_vertical_profile
=====================================

Retrieval of QVPs from a radar object. 

.. autosummary::
    :
    :

    quasi_vertical_profile


"""

import numpy as np

from ..core import antenna_to_cartesian



def quasi_vertical_profile(radar, fields=None, gatefilter=None):
    """
    Quasi Vertical Profile.
    
    Creates a QVP object containing ....
    can then be used to plot and produce the quasi vertical profile.

    Parameters
    ----------
    radar : Radar
        Radar object used.
    fields : string
        Radar fields to use for QVP output

    Other Parameters
    ----------------
    gatefilter : GateFilter
        A GateFilter indicating radar gates that should be excluded
        from the import qvp calculation.

    Returns
    -------
    qvp : 

    References
    ----------
    Troemel, S., M. Kumjian, A. Ryzhkov, and C. Simmer, 2013: Backscatter 
    differential phase – estimation and variability. J. Appl. Meteor. Clim.. 
    52, 2529 – 2548.

    Troemel, S., A. Ryzhkov, P. Zhang, and C. Simmer, 2014: Investigations 
    of backscatter differential phase in the melting layer. J. Appl. Meteorol. 
    Clim. 53, 2344 – 2359.

    Ryzhkov, A., P. Zhang, H. Reeves, M. Kumjian, T. Tschallener, S. Troemel, 
    C. Simmer, 2015: Quasi-vertical profiles – a new way to look at polarimetric 
    radar data. Submitted to J. Atmos. Oceanic Technol.
    
    """

    if fields is None:
        fields = radar.fields
  
    #if gatefilter is not None:
        #add gatefilter arguments here

    desired_angle = 20.0
    index = abs(radar.fixed_angle['data'] - desired_angle).argmin()
    print(radar.fixed_angle['data'])
    print(radar.elevation['data'][-1])

    qvp = {}

    for field in fields:
        this_field = radar.get_field(index, field).mean(axis=0)
        qvp.update({field:this_field})

    qvp.update({'range': radar.range['data'], 'time': radar.time})
    x,y,z = antenna_to_cartesian(qvp['range']/1000.0, 0.0, 
                                 radar.fixed_angle['data'][index])
    qvp.update({'height': z})
    
    return qvp   
