# EE347 Lab 2
# Team 2: 
# 2.2 Engineering Design

import numpy as np
import cmath

# Design a power factor correction function that calculates required reactive power
# for a given load according to the following specifications:
# S_load = P_l + j*Q_l = [1 + j0:10 + j10] MVA exclusive of |S_load| > 10 MVA
# function shall return capacitance Q_c required to maintain
# 0.95 lagging <= PF <= 1.0 for a given S_load
# Q_c shall be limited to discrete values in increments of 0.25 MVAr

# start with analysis of lab data
# Case 1
print("\nCase 1")
# initialize values
R0 = 600    # ohms
C = [-171,-200,-240,-300,-400,-600,-1200]   # j ohms
Z = []

# Find total impedance, Z: R0||C = 1 / (1/R0 + 1/C)
for c in C:
    Z.append(1/(1/R0+1/complex(0,c)))

# include the C = open case in Z array:
Z.append(R0)

# print each Z to verify
print("\nrectangular Z:")
for z in Z:
    print(f"{z.real:.2f} {z.imag:.2f}j ohms")

# polar coords
print("\npolar Z:")
for z in Z:
    zmag = abs(z)
    #zang = cmath.phase(z)      # radians
    zang = np.degrees(cmath.phase(z))
    print(f"{zmag:.2f} ohms, angle {zang:.2f} degrees")

# calculate current
V = 120
I1 =[]
for z in Z:
    I1.append(V/z)

print("\npolar current:")
for i in I1:
    imag = abs(i)
    iang = np.degrees(cmath.phase(i))
    print(f"{imag:.2f} A, angle {iang:.2f} degrees")


# Case 2
print("\nCase 2")
# initialize values
R0 = 300    # ohms
L = 300     # j ohms
Z0 = complex(R0,L)
C = [-171,-200,-240,-300,-400,-600,-1200]   # j ohms
Z = []

# Find total impedance, Z: R0||C = 1 / (1/R0 + 1/C)
for c in C:
    Z.append(1/(1/Z0+1/complex(0,c)))

# include the C = open case in Z array:
Z.append(Z0)

# print each Z to verify
print("\nrectangular Z:")
for z in Z:
    print(f"{z.real:.2f} {z.imag:.2f}j ohms")

# polar coords
print("\npolar Z:")
for z in Z:
    zmag = abs(z)
    #zang = cmath.phase(z)      # radians
    zang = np.degrees(cmath.phase(z))
    print(f"{zmag:.2f} ohms, angle {zang:.2f} degrees")

# calculate current
I2 =[]
for z in Z:
    I2.append(V/z)

print("\npolar current:")
for i in I2:
    imag = abs(i)
    iang = np.degrees(cmath.phase(i))
    print(f"{imag:.2f} A, angle {iang:.2f} degrees")

