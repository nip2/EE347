# EE347 Lab 2
# Team 2: 
# 2.2 Engineering Design

import math
import cmath
import numpy as np

# Design a power factor correction function that calculates required reactive power
# for a given load according to the following specifications:
# S_load = P_l + j*Q_l = [1 + j0:10 + j10] MVA exclusive of |S_load| > 10 MVA
# function shall return capacitance Q_c required to maintain
# 0.95 lagging <= PF <= 1.0 for a given S_load
# Q_c shall be limited to discrete values in increments of 0.25 MVAr

N = 50                      # NxN possible combinations
pf_cutoff = 0.95            # pf should be at or above this value
P = np.linspace(1,10,N)     # N evenly spaced values btwn 1 and 10
Q = np.linspace(0,10,N)     # N evenly spaced values btwn 0 and 10
qc_step = .25               # discrete values of Qc with this step size
Qc = np.arange(0,-N,-qc_step)# N possible values of Qc btwn 0 and -N*qc_step
count = 0
q_add = 0.

def pf_correction(p,q):
    global count
    S = complex(p,q)
    S_mag = abs(S)
    pf = p/S_mag
    q_target = p*math.tan(math.acos(pf_cutoff))

    if pf >= pf_cutoff:
        count = count + 1
        print(f"P = {p:.2}, Q = {q:.2}")
        print(f"S_mag = {S_mag:.2}     \t pf = {pf:.2}")

        return 0.

    else:
        count = count + 1
        for qc in Qc:
            q_nu = q + qc
            if q_nu <= q_target:
                S_mag = math.sqrt(p**2+q_nu**2)
                pf = p/S_mag
                        
                print("pf correction")
                #print(f"used Qc = {qc:.1} to correct")
                #print(f"The following values yield a pf >= {pf_cutoff:.2}:")
                #print(f"S = [{p:.1} + j{q_nu:.1}] MVA")
                #print(f"|S| = {abs(S_mag):.1}")
                print(f"PF = {pf:.2}")

                return qc

for p in P:
    for q in Q:
        q_add = pf_correction(p,q)
        print(f"Qc to add = {q_add:.3}")

print(f"iteration count = {count}")
