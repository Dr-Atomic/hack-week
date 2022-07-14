"""Import your packages and particle database first from Plasmapy, some of these are unnecessary but I'm keeping them in here for now."""

from asyncio import wrap_future
from ssl import ALERT_DESCRIPTION_HANDSHAKE_FAILURE
import astropy.units as u
import numbers
import numpy as np

from astropy.constants.si import e, eps0
from numba import njit

from plasmapy import particles
from plasmapy.formulary import misc
from plasmapy.particles import Particle
from plasmapy.particles.exceptions import ChargeError, InvalidParticleError
from plasmapy.utils.decorators import (
    angular_freq_to_hz,
    bind_lite_func,
    preserve_signature,
    validate_quantities,
)

mass = Particle("p").mass.value
charge = Particle("p").charge.value

omega_p = z_mean * e_si_unitless * np.sqrt(n / (eps0_si_unitless * mass))


def plasma__frequency (1e19*u.m**-3, particle='p'):
    """
    Calculate the plasma frequency of a plasma with the given parameters.
    """
    n=1e19*u.m**-3
    particle='p'
     omega_p = z_mean * e_si_unitless * np.sqrt(n / (eps0_si_unitless * mass))
    
    if to_hz:
    return omega_p / (2.0 * np.pi)

    return omega_p




