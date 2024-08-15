import matplotlib.pyplot as plt
import runge_kutta as rg
import EDOs as e

def main():
  # I = [0, 0.01, 0.1, 1, 10, 15]
  # I = [0, 10, 15, 25, 50, 100]
  # I = [0, 0.01, 0.1, 1, 10, 50]
  I = [50]
  colors = ["red", "green", "blue", "black", "yellow", "brown", "pink"]

  y0 = float(input("Initial position: "))
  v0 = float(input("Initial velocity: "))
  duration = int(input("Simulation duration: "))

  plt.xlabel("Time (s)")
  plt.ylabel("Displacement y (m)")
  plt.title("Vertical Spring Oscillation with DC Current")

  for i in range(0, len(I)):
    positions, times = rg.RG4([y0], [v0], duration, I[i], e.currentSpring)
    plt.plot(times, positions, color = colors[i], marker = ".", linestyle = "--", linewidth = 0.5, label = f"{I[i]} A")

  plt.axhline(linewidth = 0.5, color = "k")
  plt.legend()
  plt.grid()
  plt.show()

if __name__ == "__main__":
  main()
