import numpy as np
import math
import cmath
from cmath import phase

# define a function to truncate complex numbers in a matrix
# matrix a truncated to n decimals
def trunc(a,n):
    real = round(np.real(a),n)
    imag = round(np.imag(a),n)
    return complex(real,imag)
trunc_vec = np.vectorize(trunc)

# input system impedances
ZG1 = 0.0349 + 0.93j
ZM2 = 0.0697 + 1.86j
ZM3 = 0.128 + 4.254j
Zt = 0.0465 + 0.232j
ZL1 = 0.0244 + 0.1221j
ZL2 = 0.0122 + 0.0732j
ZL3 = ZL2

# invert impedances to find system admittances
Ya = 1/(2*Zt + ZL1)
Yb = 1/(2*Zt + ZL2)
Yc = 1/(2*Zt + ZL3)
Yd = 1/ZG1
Ye = 1/ZM3
Yf = 1/ZM2

# create Ybus matrix
Ybus = np.array([[Ya+Yb+Yd,-Ya,-Yb],[-Ya,Ya+Yc+Yf,-Yc,],[-Yb,-Yc,Yb+Yc+Ye]])
Ybus_m = trunc_vec(Ybus,3)
print("Ybus truncated")
print(Ybus_m)

# invert Ybus matrix to get Zbus matrix
Zbus = np.linalg.inv(Ybus)

Zbus_m = trunc_vec(Zbus,3)
print("Zbus truncated")
print(Zbus_m)
