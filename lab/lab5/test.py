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
V_h1_oc = 115.6
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

