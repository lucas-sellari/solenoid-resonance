import matplotlib.pyplot as plt
import math as mt
import constants as c
import runge_kutta as rg
import EDOs as e

def main():
  colors = ["red", "green", "blue", "black", "yellow", "brown", "pink"]

  # y0 = float(input("Initial position: "))
  # v0 = float(input("Initial velocity: "))
  # duration = int(input("Simulation duration: "))
  y0 = c.l * (c.m * c.g) / c.k # equilibrium position
  v0 = 0
  duration = 2
  w  = mt.sqrt(c.k / (c.m + (c.M / 4))) # omega
  # w = mt.sqrt(c.k / (c.M + c.m))
  fk = w / (2 * mt.pi)

  # f= [( w / (2 * mt.pi)) * (1.1/2), w/100, w/20, w/10]
  # f = [( w / (2 * mt.pi)) * (1.1/2)]
  f = [0.6]

  plt.xlabel("Time (s)")
  plt.ylabel("Displacement y (m)")
  plt.title("Vertical Spring Oscillation with AC Current")

  for i in range(0, len(f)):
    positions, times = rg.RG42([y0], [v0], duration, f[i], e.currentSpring)
    plt.plot(times, positions, color = colors[i], marker = ".", linestyle = "--", linewidth = 0.2, label = f"{f[i]} Hz")

  plt.axhline(linewidth = 0.5, color = "k")
  plt.legend()
  plt.grid()
  plt.show()

if __name__ == "__main__":
  main()
