import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

def calc_efficiency(R1, R2):
  Rl = 50
  Vin = 10
  V1 = Vin * (1 / (1 + R1 * (R2 + Rl) / (R2 * Rl)))
  Pout = V1 * V1 / Rl
  Pin = Vin * (Vin - V1) / R1
  return Pout / Pin

def plot_surface():
  R1 = np.logspace(-2, 2, num=1000)
  R2 = np.logspace(-2, 2, num=1000)
  ax = plt.figure().add_subplot(projection='3d')
  R1, R2 = np.meshgrid(R1, R2)
  surf = ax.plot_surface(R1, R2, calc_efficiency(R1, R2), cmap=cm.coolwarm)
  plt.xlabel('R1')
  plt.ylabel('R2')
  plt.colorbar(surf)
  plt.savefig('fig/surface.png')

def plot_efficiency_vs_r1():
  R1 = np.logspace(-2, 5, num=1000)
  plt.figure()
  plt.plot(R1, calc_efficiency(R1, 100_000), label="100kΩ")
  plt.plot(R1, calc_efficiency(R1, 1_000), label="1kΩ")
  plt.plot(R1, calc_efficiency(R1, 1), label="1Ω")
  plt.legend(title='R2 values')
  plt.ylabel('Efficiency')
  plt.xscale('log')
  plt.xlabel('R1')
  plt.savefig('fig/efficiency_vs_r1.png')

def plot_efficiency_vs_r2():
  R2 = np.logspace(-2, 5, num=1000)
  plt.figure()
  plt.plot(R2, calc_efficiency(100_000, R2), label="100kΩ")
  plt.plot(R2, calc_efficiency(1_000, R2), label="1kΩ")
  plt.plot(R2, calc_efficiency(1, R2), label="1Ω")
  plt.legend(title='R1 values')
  plt.ylabel('Efficiency')
  plt.xscale('log')
  plt.xlabel('R2')
  plt.savefig('fig/efficiency_vs_r2.png')
  
plot_surface()
plot_efficiency_vs_r1()
plot_efficiency_vs_r2()