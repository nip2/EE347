# EE347 Lab 2
# Team 2: 
# 2.2 Engineering Design

import math
import numpy as np

N = 100                     # NxN possible combinations
pf_cutoff = 0.95            # pf should be at or above this value
P = np.linspace(1,10,N)     # N evenly spaced values btwn 1 and 10
Q = np.linspace(0,10,N)     # N evenly spaced values btwn 0 and 10
qc_step = .25               # discrete values of Qc with this step size
Qc = np.arange(0,-N,-qc_step)# N possible values of Qc btwn 0 and -N*qc_step
q_add = 0.                  # initiate variable to store correcting qc in

# function definition
# takes a given p and q and returns a corresponding correcting capacitance, qc
def pf_correction(p,q):
    S_mag = math.sqrt(p**2+q**2)      # |S| = sqrt(p^2 + q^2)
    pf = p/S_mag        # uncorrected pf

    # q_target is the value of q that gives pf = 0.95 for the given value of p
    q_target = p*math.tan(math.acos(pf_cutoff))

    # if the given pf is already above 0.95, then qc = 0
    if pf >= pf_cutoff:
        # output the values for confirmation
        print(f"P = {p:.3}, Q = {q:.3}")
        print(f"S_mag = {S_mag:.2}     \t pf = {pf:.2}")

        # qc = 0
        return 0.

    # if pf is not >= 0.95, then it needs correction
    else:
        # iterate through possible qc values (increment 0.25)
        for qc in Qc:
            q_nu = q + qc
            if q_nu <= q_target:
                S_mag = math.sqrt(p**2+q_nu**2)
                pf = p/S_mag
                        
                print("\npf correction")
                print(f"started with S = [{p:.3} + j{q:.3}] MVA")
                print(f"The following values yield a pf >= {pf_cutoff:.2}:")
                print(f"S = [{p:.3} + j{q_nu:.3}] MVA")
                print(f"PF = {pf:.2}")

                # return qc correction
                return qc

# test NxN possible values in the given range
# for each p, iterate through every q
for p in P:
    for q in Q:
        q_add = pf_correction(p,q)
        print(f"Qc to add = {q_add:.3} MVAr")