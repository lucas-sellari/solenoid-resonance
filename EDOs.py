import math as mt
import constants as c

def inductiveForce(N, I, R, y):
  return (c.mu0 * mt.pi * mt.pow(N * I * R, 2)) / (2 * mt.pow(y, 2))

def simpleSpring(y, I): # simple spring
  return (-c.k*(y - c.l) + c.m*c.g) / c.m

def twoCoils(y, I):
  return -(c.k*y+ (c.mu0*(I**2)*c.R*c.N)/y) / c.m

def twoCoilsInhomogeneous(y, I):
  return -(c.k * y + (c.mu0 * mt.pow(I, 2) * c.R * c.N)/y - c.m * c.g - c.k * c.l) / c.m

def NLoops(y, I):
  return -(c.k * y + (c.mu0 * mt.pow(I, 2) * c.R * c.N)/y - c.m * c.g - c.k * c.l) / c.m

def currentSpring(y, yDot, I):
  return -((c.alpha * yDot) + (c.k * y) + inductiveForce(c.N, I, c.R, y) - ((2*c.m + (c.M / 2))*c.g)) / (c.m + (c.M / 4))
  # return (-((c.mu0 * mt.pi * c.R * (c.N * I / y)**2) / 4 + c.k * (y - c.l)) + (c.m + c.M) * c.g) / ((c.M / 2) + c.m)