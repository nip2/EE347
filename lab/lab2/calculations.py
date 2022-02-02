# EE347 Lab 2
# Team 2: 
# 2.1 Calculations and verification

import math
import cmath

# analysis of lab data
# Case 1
print("\nCase 1")
# initialize values
R0 = 600    # ohms
C = [-171j,-200j,-240j,-300j,-400j,-600j,-1200j]   # ohms
Z = []

# Find total impedance, Z: R0||C = 1 / (1/R0 + 1/C)
for c in C:
    Z.append(1/(1/R0+1/c))

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
    zang = math.degrees(cmath.phase(z))
    print(f"{zmag:.2f} ohms, angle {zang:.2f} degrees")

# calculate current
V = 120
I1 =[]
for z in Z:
    I1.append(V/z)

print("\npolar current:")
for i in I1:
    imag = abs(i)
    iang = math.degrees(cmath.phase(i))
    print(f"{imag:.2f} A, angle {iang:.2f} degrees")


# Case 2
print("\nCase 2")
# initialize values
R0 = 300    # ohms
L = 300j     # ohms
Z0 = (R0+L)
Z = []

# Find total impedance, Z: Z0||C = 1 / (1/Z0 + 1/C)
for c in C:
    Z.append(1/(1/Z0+1/c))

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
    zang = math.degrees(cmath.phase(z))
    print(f"{zmag:.2f} ohms, angle {zang:.2f} degrees")

# calculate current
I2 =[]
for z in Z:
    I2.append(V/z)

print("\npolar current:")
for i in I2:
    imag = abs(i)
    iang = math.degrees(cmath.phase(i))
    print(f"{imag:.2f} A, angle {iang:.2f} degrees")
