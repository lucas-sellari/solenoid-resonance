import math as mt

g  = 9.8   # m/s2
k  = 19.6  # N/m
m  = 0.019 # mass of the hanging body [kg]
M  = 0.009 # mass of the spring [kg]
l  = 0.07  # natural length of the spring [m]
w = mt.sqrt(k / m)

mu0 = 4 * mt.pi * mt.pow(10, -7) # H/m
N = 14    # number of turns
R = 0.015 # coil radius [m]

alpha = 1 # viscosity coefficient

# Italy
# k = 0.3202
# m = 0.0072
# M = 0.0010 # unsure
# l = 0.007  # unsure
# N = 27
# R = 0.00225
