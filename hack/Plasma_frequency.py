from astropy import units as u

def plasma__frequency(1e19*u.m**-3, particle='p'):
    """
    Calculate the plasma frequency of a plasma with the given parameters.
    """
    return (B0 / B) * (Te / ne)
    
def plasma__frequency__SI(1e19*u.m**-3, particle='p'):
    """
    Calculate the plasma frequency of a plasma with the given parameters.
    """
    return (B0 / B) * (Te / ne)

