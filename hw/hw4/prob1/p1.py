import numpy as np
import math
import cmath

# predefine function to get phase in degrees:
def phase(v):
    return math.degrees(cmath.phase(v))

# a script to determine the following:
# a) per phase, the AC resistance per 1000 ft and total resistance of line
# b) per phase, the inductive reactance per 1000 ft and total inductive reactance of line
# c) per phase, the capacitive admittance per 1000 ft and the total capacitive admittance
# d) the ABCD matrix coefficients appropriate for the given length

# ACSR dicts for AC 60Hz @ 50C
ibis = {
    "name": "ibis",
    "resistance": 0.0481,       # ohms per 1000 ft
    "ind_reactance": 0.0835,    # ohms per 1000 ft
    "capacitance": 0.539,       # Mohms per 1000 ft
    "GMR": 0.0265               # ft
}

drake = {
    "name": "drake",
    "resistance": 0.0242,       # ohms per 1000 ft
    "ind_reactance": 0.0756,    # ohms per 1000 ft
    "capacitance": 0.482,       # Mohms per 1000 ft
    "GMR": 0.0375               # ft
}

skylark = {
    "name": "skylark",
    "resistance": 0.0159,       # ohms per 1000 ft
    "ind_reactance": 0.072,     # ohms per 1000 ft
    "capacitance": 0.455,       # Mohms per 1000 ft
    "GMR": 0.0427               # ft
}

jorea = {
    "name": "jorea",
    "resistance": 0.0087,       # ohms per 1000 ft
    "ind_reactance": 0.064,     # ohms per 1000 ft
    "capacitance": 0.399,       # Mohms per 1000 ft
    "GMR": 0.0621               # ft
}

# given values
V_rated = 500e3           # nominal voltage
Vr = V_rated/np.sqrt(3)   # receiving voltage
S_rated = 150e6           # MVA
S = S_rated/3             # single phase power
d = 95              # length of transmission line
D = 8               # distance between conductors (ft)
temp_nom = 50       # nominal operating temp, celsius

# define function
def findACSR(bird,d,D,Vr,S):
    mi_to_ft_conv = 5.28    # 1000 ft
    gmd = np.cbrt(D**3)     # equilateral triangle formation
    Ir = S/(np.sqrt(3)*Vr)    # receiving current

    # impedance values
    R = bird["resistance"] * d * mi_to_ft_conv
    Xl = bird["ind_reactance"] * d * mi_to_ft_conv * np.log(gmd/bird["GMR"])
    Xc = bird["capacitance"]*1e6 / (d * mi_to_ft_conv) * np.log(gmd/bird["GMR"])
    Y = 1/Xc

    # matrix coefficients
    # medium model
    Z = complex(R,Xl)
    Y = complex(0,Y)

    A = (Y*Z)/2 + 1
    B = Z
    C = Y*((Y*Z)/4 + 1)
    D = A

    # calculate Vs, Is, voltage regulation
    a = np.array([[A,B],[C,D]])
    b = np.array([Vr,Ir])
    send = a @ b        # matrix multiplication

    Vs = send[0]
    Is = send[1]
    VR = abs((Vs-Vr)/Vr) * 100

    # print values to verify
    print("\n%s conductor:" %bird["name"])
    # per unit values
    print(f"\nAC resistance per 1000 ft: {bird['resistance']:.4f} ohms")
    print(f"inductive reactance per 1000 ft: {bird['ind_reactance']:.4f} ohms")
    print(f"capacitive admittance per 1000 ft: {bird['capacitance']:.4f} Megaohms")

    # total length values
    print(f"\nZ = {R:.2f} + j{Xl:.2f} ohms")
    print(f"Y = j{Y.imag:.7f} S")

    # matrix coefficient values
    print(f"\nA = {abs(A):.4f}, {phase(A):.3f} degrees")
    print(f"B = {abs(B):.4f}, {phase(B):.3f} degrees")
    print(f"C = {abs(C):.6f}, {phase(C):.3f} degrees")
    print(f"D = {abs(D):.4f}, {phase(D):.3f} degrees")

    # Vr, Ir
    print(f"\nVs = {abs(Vs):.2f} V, {phase(Vs):.2f} degrees")
    print(f"Is = {abs(Is):.2f} A, {phase(Is):.2f} degrees")

    # voltage regulation
    print(f"voltage regulation = {VR:.3}%")

# test function
findACSR(ibis,d,D,Vr,S)
findACSR(drake,d,D,Vr,S)
findACSR(skylark,d,D,Vr,S)
findACSR(jorea,d,D,Vr,S)
