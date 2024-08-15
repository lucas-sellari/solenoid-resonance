import numpy as np
import math as mt

WEIGHTS = [1, 2, 2, 1]

def current(t, f):
  return 10 * mt.sin(2 * mt.pi * f * t)
  #if round(t%1,2) == 0:
  #  return 10*mt.cos(2*mt.pi*60*t)
  #if t>2:
  #  return 12*mt.cos(2*mt.pi*t*f)
  # if t>2 and t<3:
    # return 14.7
  #  return 12*mt.cos(2*mt.pi*t*f)
  #elif t>4:
  #  return -15
  # else:
    # return 0

def RG2(positions, velocities, duration, I, F):
  times = [0]
  count = 0
  step  = 0.01

  while count <= duration:
    position = positions[-1]
    velocity = velocities[-1]

    kp1 = velocity
    kv1 = F(position, I)

    kp2 = velocity + (kv1 * step) / 2
    kv2 = F(position + (kp1 * step) / 2, I)

    velocities.append(velocity + (kv2 * step) / 2)
    positions.append(position  + (kp2 * step) / 2)

    times.append(count)
    count += step

  return positions, times

def RG4(positions, velocities, duration, I, F):
  times = [0]
  count = 0
  step  = 0.01

  while count <= duration:
    position = positions[-1]
    velocity = velocities[-1]

    kp1 = velocity
    kv1 = F(position, kp1, I)

    kp2 = velocity + (kv1 * step) / 2
    kv2 = F(position + (kp1 * step) / 2, kp2, I)

    kp3 = velocity + (kv2 * step) / 2
    kv3 = F(position + (kp2 * step) / 2, kp3, I)

    kp4 = velocity + (kv3 * step)
    kv4 = F(position + (kp3 * step), kp4, I)

    kv = float(np.average([kv1, kv2, kv3, kv4], weights = WEIGHTS))
    kp = float(np.average([kp1, kp2, kp3, kp4], weights = WEIGHTS))

    velocities.append(velocity + (kv * step))
    positions.append(position + (kp * step))

    times.append(count)
    count += step

  return positions, times

def RG42(positions, velocities, duration, frequency, F):
  times   = [0]
  count   = 0
  step    = 0.01

  while count <= duration:
    I = current(count, frequency)
    position = positions[-1]
    velocity = velocities[-1]

    kp1 = velocity
    kv1 = F(position, kp1, I)

    kp2 = velocity + (kv1 * step) / 2
    kv2 = F(position + (kp1 * step) / 2, kp2, I)

    kp3 = velocity + (kv2 * step) / 2
    kv3 = F(position + (kp2 * step) / 2, kp3, I)

    kp4 = velocity + (kv3 * step)
    kv4 = F(position + (kp3 * step), kp4, I)

    kv = float(np.average([kv1, kv2, kv3, kv4], weights = WEIGHTS))
    kp = float(np.average([kp1, kp2, kp3, kp4], weights = WEIGHTS))

    velocities.append(velocity + (kv * step))
    positions.append(position + (kp * step))

    times.append(count)
    count = round(count + step, 2)

  return positions, times
