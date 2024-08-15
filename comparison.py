import matplotlib.pyplot as plt
import runge_kutta as rg
import EDOs as e

def main():
  y0 = float(input("Initial position: "))
  v0 = float(input("Initial velocity: "))
  duration = int(input("Simulation duration: "))
  I = 0

  positionsRG4, timesRG4 = rg.RG4([y0], [v0], duration, I, e.simpleSpring)
  positionsRG2, timesRG2 = rg.RG2([y0], [v0], duration, I, e.simpleSpring)

  plt.xlabel("Time (s)")
  plt.ylabel("Displacement d (m)")
  plt.title("Vertical Spring Oscillation")

  plt.plot(timesRG2, positionsRG2, color = "red",  marker = "o", linestyle = "--", linewidth = 2, label = "RG2")
  plt.plot(timesRG4, positionsRG4, color = "blue", marker = "o", linestyle = "--", linewidth = 2, label = "RG4")
  plt.axhline(linewidth = 0.5, color = "k")

  plt.legend()
  plt.grid()
  plt.show()

if __name__ == "__main__":
  main()
