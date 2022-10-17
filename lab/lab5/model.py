from struct import calcsize
import numpy as np
import cmath
import math
from cmath import phase
from math import degrees, radians

# For the open-circuit, full-load, and imbalance demonstrations, 
# create a circuit model of a residential transformer1 consisting 
# of the aforementioned loads. Use the model to calculate the 
# expected S, Vp, Ip, V240, V120, IH1, IH2, IN, S120. 
# Compare calculations with measurements.

# Xmfr ratings
S_rating = 60

# Xfmr settings
Vp = 208
V_240 = 240
V_br = 120

# balanced load
Z_120 = 1200 + 240j
Z_240 = 1200 + 1200j

# turns ratio
a_120 = Vp / V_br
a_240 = Vp / V_240

# Open circuit test values
Vp_line_oc = 206.4
V_h1_oc = 117.9
V_h2_oc = 117.4
Ip_line_oc = 0.089

# balanced load
Vp_line_bal = 205.7
V_h1_bal = 115.3
V_h2_bal = 114.3
Ip_line_bal = 0.183
Is_h1_bal = 0.091
Is_h2_bal = 0.09
Is_n_bal = 0

# define function
def xfmr_model(Z1,Z2,Z3):
    Z_h1 = Z1
    Z_h2 = Z2
    Z_h12h2 = Z3*(Z1 + Z2)/(Z3 + Z1 + Z2)
    print(f"total Z: {Z_h12h2:.2f} ohm")

    # primary voltages
    Vp_calc = Vp - Ip_line_oc**2 * a_240**2 * Z_h12h2
    print(f"Vp calculated: {abs(Vp_calc):.2f} V")
    # primary current
    #Ip_calc = Vp_calc / (a_240**2 * Z_h12h2)
    #print(f"Ip = {abs(Ip_calc):.2f} A")
    Ip = Vp / (a_240**2 * Z_h12h2) - Ip_line_oc
    print(f"Ip = {abs(Ip):.2f} A")

    # secondary currents
    Is_h1 = V_h1_oc / Z_h1
    print(f"Is h1 branch: {abs(Is_h1):.2f} A")
    Is_h2 = V_h2_oc / Z_h2
    print(f"Is h2 branch: {abs(Is_h2):.2f} A")
    Is_240 = (V_h1_oc + V_h2_oc) / Z_h12h2
    print(f"Is h1 to h2: {abs(Is_240):.2f} A")
    Is_h12h2 = Is_h1 + Is_h2
    print(f"Is h1 to h2 (alternate): {abs(Is_h12h2):.2f} A")
    In = Is_h1 - Is_h2
    print(f"neutral current: {abs(In):.2f} A")

    # secondary voltages
    V_240_calc = Is_240 * Z_h12h2
    print(f"Vs_240: {abs(V_240_calc):.2f} V")
    V_h1_calc = Is_h1 * Z_h1
    print(f"V H1: {abs(V_h1_calc):.2f} V")
    V_h2_calc = Is_h2 * Z_h2
    print(f"V H2: {abs(V_h2_calc):.2f} V")

    # power
    S_240 = Is_h12h2 * V_240_calc
    print(f"S_240: {abs(S_240):.2f} VA")
    S_h1 = Is_h1 * V_h1_calc
    S_h2 = Is_h2 * V_h2_calc
    print(f"S_H1 = {abs(S_h1):.2f} VA")
    print(f"S_H2 = {abs(S_h2):.2f} VA")

def currents(Z1,Z2,Z3):
    Vp = 208
    V1 = 120
    V2 = cmath.rect(120,radians(180))
    z_bus = np.array([[Z1,0,-Z3],[0,Z2,-Z3],[-Z1,-Z2,Z1+Z2+Z3]])
    z_inv = np.linalg.inv(z_bus)
    v_vec = np.array([V1,V2,0])
    i_vec = v_vec @ z_inv
    I1 = i_vec[0]
    I2 = i_vec[1]
    I3 = i_vec[2]
    print(f"I1 = {abs(I1):.3f} A")
    print(f"I2 = {abs(I2):.3f} A")
    print(f"I3 = {abs(I3):.3f} A")

# calculate
#
# open circuit
print("\nOpen Circuit:")
xfmr_model(1e6,1e6,1e6)

# balanced load
print("\nBalanced Load:")
xfmr_model(Z_120,Z_120,Z_240)
#currents(Z_120,Z_120,Z_240)

# unbalanced load
print("\nUnbalanced Load:")
xfmr_model(300+300j,1200+600j,Z_240)
#currents(300+300j,1200+600j,Z_240)
