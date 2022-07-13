plasmapy.formulary.frequencies.plasma_frequency(n: Unit('1 / m3'), particle: Particle, z_mean=None, to_hz=False)

from astropy import units as u

plasma_frequency(1e19*u.m**-3, particle='p')
<Quantity 4.16329...e+09 rad / s>
plasma_frequency(1e19*u.m**-3, particle='D+')
<Quantity 2.94462...e+09 rad / s>
plasma_frequency(1e19*u.m**-3, particle='D0')
<Quantity 2.94462...e+09 rad / s>
plasma_frequency(1e19*u.m**-3, particle='D-')
<Quantity 2.94462...e+09 rad / s>
plasma_frequency(1e19*u.m**-3, particle='T+')
<Quantity 2.94462...e+09 rad / s>
plasma_frequency(1e19*u.m**-3, particle='T0')
<Quantity 2.94462...e+09 rad / s>
plasma_frequency(1e19*u.m**-3, particle='T-')
<Quantity 2.94462...e+09 rad / s>
plasma_frequency(1e19*u.m**-3, particle='p', to_hz=True)
<Quantity 6.62608...e+08 Hz>
plasma_frequency(1e19*u.m**-3, 'e-', to_hz=True)
<Quantity 2.83930...e+10 Hz>


