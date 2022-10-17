import oct2py
import numpy as np
import matplotlib.pyplot as plt
import cmath
from oct2py import octave

# These are default values:
# Overcurrent coeff
C_I = 1.1
# under/over voltage coeffs
C_v = [0.95, 1.2]

octave.run('mod_prog.m')
vr = octave.VR(60,60,C_v,C_I)

print(vr)