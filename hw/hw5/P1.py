import numpy as np
import math
import cmath
from cmath import phase
from math import degrees

# given values
# line impedances
r_pu = 0.002            # pu line resistance
x_L_pu = 0.0155         # pu line inductance
y_c_pu = 0.032          # pu line admittance
# diagram values
V_base = 500e3          # nominal voltage
S_base = 100e6          # VA
P_pu = 43               # pu W from bus 19 to bus 20
pf = 0.97               # chosen PF
# per unit per phase
z_pu = complex(r_pu,x_L_pu)
y_pu = complex(0,y_c_pu)

# per phase per-unit
P_phi = P_pu / 3
S_phi_load = P_phi / pf
V_phi_R = 1.0
I_phi_R = S_phi_load / (np.sqrt(3) * V_phi_R)
I_phi_R_c = cmath.rect(I_phi_R,-np.arccos(pf))
V_phi_drop = I_phi_R * z_pu

print(f"per-unit, per-phase P: {P_phi:.3f}")
print(f"per-unit, per-phase S: {S_phi_load:.3f}")
print(f"per-unit, per-phase I: {I_phi_R:.3f}")
print(f"per-unit, per-phase Vdrop: {V_phi_drop:.3f}")

#
Z = z_pu
Y = y_pu

# short model
#
# short model coefficients
A = 1
B = Z
C = 0
D = 1

# solve by matrix multiplication
a = np.array([[A,B],[C,D]])
b = np.array([V_phi_R,I_phi_R_c])
send = a @ b        # matrix multiplication

Vs = send[0]
Is = send[1]

print(f"\nVs = {abs(Vs):.3f} V, {phase(Vs):.3f} degrees")
print(f"Is = {abs(Is):.3f} A, {phase(Is):.3f} degrees")

Vs_short = abs(Vs)
Is_short = abs(Is)

# voltage regulation
VR_short = (abs(Vs_short - V_phi_R)) / V_phi_R * 100
print(f"\nshort model VR: {VR_short:.3f}%")

# efficiency
Is_mag = abs(Is)
P_loss = Is_mag**2 * r_pu
eff_short = P_phi/(P_phi+P_loss) * 100
print(f"short model efficiency: {eff_short:.3f} %")

# medium model
#
# medium model coefficients
A = (Y*Z)/2 + 1
B = Z
C = Y*((Y*Z)/4 + 1)
D = A

# solve by matrix multiplication
a = np.array([[A,B],[C,D]])
b = np.array([V_phi_R,I_phi_R_c])
send = a @ b        # matrix multiplication

Vs = send[0]
Is = send[1]

print(f"\nVs = {abs(Vs):.3f} V, {phase(Vs):.3f} degrees")
print(f"Is = {abs(Is):.3f} A, {phase(Is):.3f} degrees")

Vs_med = abs(Vs)
Is_med = abs(Is)

# voltage regulation
VR_med = (abs(Vs_med - V_phi_R)) / V_phi_R * 100
print(f"\nmedium model VR: {VR_med:.3f}%")

# efficiency
Is_mag = abs(Is)
P_loss = Is_mag**2 * r_pu
eff_med = P_phi/(P_phi+P_loss) * 100
print(f"medium model efficiency: {eff_med:.3f} %")

# long model
#
# propogation constant, gamma
gd = np.sqrt(Z*Y)   # gamma * distance

# modified impedance and admittance
Zp = Z * (np.sinh(gd)/(gd))
Yp = Y * (np.tanh(gd/2)/(gd/2))

# long model coefficients
A = (Zp*Yp)/2 + 1
B = Zp
C = Yp*((Zp*Yp)/4 + 1)
D = A

# solve by matrix multiplication
a = np.array([[A,B],[C,D]])
b = np.array([V_phi_R,I_phi_R_c])
send = a @ b        # matrix multiplication

Vs = send[0]
Is = send[1]

print(f"\nVs = {abs(Vs):.3f} V, {phase(Vs):.3f} degrees")
print(f"Is = {abs(Is):.3f} A, {phase(Is):.3f} degrees")

Vs_long = abs(Vs)
Is_long = abs(Is)

# voltage regulation
VR_long = (abs(Vs_long - V_phi_R)) / V_phi_R * 100
print(f"\nlong model VR: {VR_long:.3f}%")

# efficiency
Is_mag = abs(Is)
P_loss = Is_mag**2 * r_pu
eff_long = P_phi/(P_phi+P_loss) * 100
print(f"long model efficiency: {eff_long:.3f} %")

# calculate accuracy of short and medium methods
short_pct = abs(Vs_long - Vs_short)/Vs_long * 100
med_pct = abs(Vs_long - Vs_med)/Vs_long * 100

print(f"\npercent error of short model: {short_pct:.4f}%")
print(f"percent error of medium model: {med_pct:.4f}%")