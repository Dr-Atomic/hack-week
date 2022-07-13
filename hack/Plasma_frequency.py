import numpy as np
from astropy import units as u
from astropy.constants import c

def plasma__frequency (1e19*u.m**-3, particle='p'):
    """
    Calculate the plasma frequency of a plasma with the given parameters.
    """
    n=1e19*u.m**-3
    particle='p'
    
    return omega_plasma(n, particle)

    
def plasma__frequency__SI(1e19*u.m**-3, particle='p'):
    """
    Calculate the plasma frequency of a plasma with the given parameters.
    """
    n=1e19*u.m**-3
    particle='p'
    
    return omega_plasma(n, particle)

