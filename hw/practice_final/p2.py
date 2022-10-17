import numpy as np
import math
import cmath
from cmath import phase
from math import degrees

r = 0.02
x = 0.05
S = 1.8e6
V = 12.47e3
pf = 0.81
theta = np.arccos(pf)
Q = 1.8*np.sin(theta)
Qp = 1.8*np.sin(np.arccos(.95))
Qc = Q - Qp

# before compensation
S_old = cmath.rect(1.0,theta)
Vr = 1.0
P_out = abs(S_old) * pf
I_old = S_old.conjugate()/Vr
print(f"I = {abs(I_old):.2f}, {degrees(phase(I_old)):.2f} degrees")
P_loss = abs(I_old)**2 * r
eff = P_out / (P_out + P_loss) * 100
print(f"efficiency: {eff:.2f} %")

# after compensation
pf = 0.95
S_nu = cmath.rect(1.0,np.arccos(pf))
Vr = 1.0
P_out = abs(S_nu) * pf
I_nu = S_nu.conjugate()/Vr
print(f"I = {abs(I_nu):.2f}, {degrees(phase(I_nu)):.2f} degrees")
P_loss = abs(I_nu)**2 * r
eff = P_out / (P_out + P_loss) * 100
print(f"efficiency: {eff:.2f} %")