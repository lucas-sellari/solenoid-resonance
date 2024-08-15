import math as mt
import matplotlib.pyplot as plt

# simple spring test
k  = 15.9  # N/m
m  = 2 / 3 # kg
g  = 9.8   # m/s2
l  = 0.05  # m, natural length of the spring
w = mt.sqrt(k / m)

def springMotion(interval, y0, v0):
  dt = 0.01
  A = v0 / w
  B = y0 - m*g/k - l
  position = [y0]
  instant  = [0]
  i = dt

  while i < interval:
    y = A*mt.sin(w*i) + B*mt.cos(w*i) + m*g/k + l
    position.append(y)
    instant.append(i)
    i += dt

  return position, instant, m*g/k + l

y0 = float(input("Initial position: "))
v0 = float(input("Initial velocity: "))
t  = int(input("Interval of simulation: "))

position, instant, eqPosition = springMotion(t, y0, v0)
print(eqPosition)
print(w/(2*mt.pi))

plt.xlabel("Time (s)")
plt.ylabel("Position y (m)")
plt.title("Simple vertical pendulum oscillation")
plt.plot(instant, position, color = "black", marker = "o", linestyle = "--", linewidth = 2, label = "Ideal solution")
plt.axhline(linewidth=0.5, color="k")
plt.legend()
#plt.invert_yaxis()
#plt.ylim(0.08, 0.1)
plt.grid()
plt.show()
