import numpy as np
import math
import cmath
from math import degrees
from cmath import phase

Z = 0.7456 + 3.4j
Y = 94e-6

# short
A = 1
B = Z
C = 0
D = 1

#ABCD = np.array([[A,B],[C,D]])
# matrix coefficient values
print(f"A = {abs(A):.4f}, {phase(A):.3f} degrees")
print(f"B = {abs(B):.4f}, {phase(B):.3f} degrees")
print(f"C = {abs(C):.6f}, {phase(C):.3f} degrees")
print(f"D = {abs(D):.4f}, {phase(D):.3f} degrees")
print("\n")

# medium
A = (Y*Z)/2 + 1
B = Z
C = Y*((Y*Z)/4 + 1)
D = A

#ABCD = np.array([[A,B],[C,D]])
# matrix coefficient values
print(f"A = {abs(A):.4f}, {phase(A):.3f} degrees")
print(f"B = {abs(B):.4f}, {phase(B):.3f} degrees")
print(f"C = {abs(C):.6f}, {phase(C):.3f} degrees")
print(f"D = {abs(D):.4f}, {phase(D):.3f} degrees")
print("\n")

# part 2
# use short model
# short
A = 1
B = Z
C = 0
D = 1

# given values:
pf = 0.85
Vr = 7200
S = 1.67
I = 231.5
theta = -np.arccos(pf)
Ir = cmath.rect(I,theta)
print(f"Vr = {Vr:.2f} V, 0 degrees")
print(f"Ir = {abs(Ir):.2f} A, {degrees(phase(Ir)):.2f} degrees")

# calculate Vs, Is, voltage regulation
a = np.array([[A,B],[C,D]])
b = np.array([Vr,Ir])
send = a @ b        # matrix multiplication

Vs = send[0]
Is = send[1]
VR = abs((abs(Vs)-Vr)/Vr) * 100

print(f"Vs = {abs(Vs):.2f} V, {degrees(phase(Vs)):.2f} degrees")
print(f"Is = {abs(Is):.2f} A, {degrees(phase(Is)):.2f} degrees")
print(f"VR: {VR:.2f}%")