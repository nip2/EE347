import numpy as np
import scipy as sp
import math
import cmath
import matplotlib.pyplot as plt

# predefine function to get phase in degrees:
def phase(v):
    return math.degrees(cmath.phase(v))

# find Vs using the short t-line model, medium, then long
# given:

f = 50          # Hz
phases = 3      # 
d = 300         # km
Z = 23. + 75j   # ohms
Y = 500e-6j     # siemens
P = 150e6       # W
VLL = 220e3     # V
pf = .88

# print series impedance to verify
print("\n")
print(f"Z = {abs(Z):.2f} ohms, angle {phase(Z):.2f} degrees")

# calculate phase values
V_phase = VLL/np.sqrt(3)
I_line = P/(np.sqrt(3)*VLL)
# print to verify
print(f"\nV_phase = {V_phase:.2f} V")
print(f"I_line = {I_line:.2f} A\n")

# Part (a)
print("\nPart (a)\n")
# short model coefficients
A = 1
B = Z
C = 0
D = 1

# print coefficients to verify
print(f"A = {abs(A):.2f} angle {phase(A):.2f} degrees")
print(f"B = {abs(B):.2f} angle {phase(B):.2f} degrees")
print(f"C = {abs(C):.6f} angle {phase(C):.2f} degrees")
print(f"D = {abs(D):.2f} angle {phase(D):.2f} degrees\n")

# receiving end phase values
Vr = V_phase
Ir = cmath.rect(I_line,-np.arccos(.88))
# print to verify
print(f"Vr = {Vr:.2f} V")
print(f"Ir = {abs(Ir):.2f} A, angle {phase(Ir):.2f} degrees")

# solve by matrix multiplication
a = np.array([[A,B],[C,D]])
b = np.array([Vr,Ir])
send = a @ b        # matrix multiplication

Vs = send[0]
Is = send[1]

print(f"\nVs = {abs(Vs):.2f} V, {phase(Vs):.2f} degrees")
print(f"Is = {abs(Is):.2f} A, {phase(Is):.2f} degrees")

Vs_short = abs(Vs)
Is_short = abs(Is)

# Part (b)
print("\nPart (b)\n")
# medium model coefficients
A = (Y*Z)/2 + 1
B = Z
C = Y*((Y*Z)/4 + 1)
D = A

# print coefficients to verify
print(f"A = {abs(A):.2f} angle {phase(A):.2f} degrees")
print(f"B = {abs(B):.2f} angle {phase(B):.2f} degrees")
print(f"C = {abs(C):.6f} angle {phase(C):.2f} degrees")
print(f"D = {abs(D):.2f} angle {phase(D):.2f} degrees")

# solve by matrix multiplication
a = np.array([[A,B],[C,D]])
b = np.array([Vr,Ir])
send = a @ b        # matrix multiplication

Vs = send[0]
Is = send[1]

print(f"\nVs = {abs(Vs):.2f} V, {phase(Vs):.2f} degrees")
print(f"Is = {abs(Is):.2f} A, {phase(Is):.2f} degrees")

Vs_med = abs(Vs)
Is_med = abs(Is)

# Part (c)
print("\nPart (c)\n")
# long model
# propogation constant, gamma
y = Y/d 
z = Z/d 
gamma = np.sqrt(y*z)
print(f"y = {abs(y):.6f}, {phase(y):.2f} degrees")
print(f"z = {abs(z):.2f}, {phase(z):.2f} degrees")
print(f"gamma = {abs(gamma):.5f}, {phase(gamma):.2f} degrees")

# modified impedance and admittance
Zp = Z * (np.sinh(gamma*d)/(gamma*d))
Yp = Y * (np.tanh(gamma*d/2)/(gamma*d/2))
print(f"Yp = {abs(Yp):.6f}, {phase(Yp):.2f} degrees")
print(f"Zp = {abs(Zp):.2f}, {phase(Zp):.2f} degrees\n")

# long model coefficients
A = (Zp*Yp)/2 + 1
B = Zp
C = Yp*((Zp*Yp)/4 + 1)
D = A

# print coefficients to verify
print(f"A = {abs(A):.2f} angle {phase(A):.2f} degrees")
print(f"B = {abs(B):.2f} angle {phase(B):.2f} degrees")
print(f"C = {abs(C):.6f} angle {phase(C):.2f} degrees")
print(f"D = {abs(D):.2f} angle {phase(D):.2f} degrees")

# solve by matrix multiplication
a = np.array([[A,B],[C,D]])
b = np.array([Vr,Ir])
send = a @ b        # matrix multiplication

Vs = send[0]
Is = send[1]

print(f"\nVs = {abs(Vs):.2f} V, {phase(Vs):.2f} degrees")
print(f"Is = {abs(Is):.2f} A, {phase(Is):.2f} degrees")

Vs_long = abs(Vs)
Is_long = abs(Is)

# calculate accuracy of short and medium methods
short_pct = abs(Vs_long - Vs_short)/Vs_long * 100
med_pct = abs(Vs_long - Vs_med)/Vs_long * 100

print(f"\npercent error of short model: {short_pct:.2f}%")
print(f"percent error of medium model: {med_pct:.2f}%")
