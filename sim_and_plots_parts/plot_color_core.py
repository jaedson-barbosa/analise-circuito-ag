import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

X, Y = np.meshgrid(r_mut_opts, r_cross_opts)

def plot_colormesh(func, vmax = 25):
  calc_z = lambda results: np.array([[func([len(sim_result[2]) for sim_result in col]) for col in row] for row in results])
  fig, ax = plt.subplots(2, 2, sharex=True, sharey=True)

  fig.set_figwidth(10)
  fig.set_figheight(12)

  meshopts = {'cmap': 'coolwarm', 'vmin': 0, 'vmax': vmax}
  surf = ax[0][0].pcolormesh(X, Y, calc_z(results_pop_10_roulette), **meshopts)
  ax[0][0].set_xlabel('mutation rate')
  ax[0][0].set_ylabel('crossover rate')
  ax[0][0].set_title('Population=10 (Roulette)')

  surf = ax[0][1].pcolormesh(X, Y, calc_z(results_pop_10_tournament), **meshopts)
  ax[0][1].set_xlabel('mutation rate')
  ax[0][1].set_ylabel('crossover rate')
  ax[0][1].set_title('Population=10 (Tournament)')

  surf = ax[1][0].pcolormesh(X, Y, calc_z(results_pop_20_roulette), **meshopts)
  ax[1][0].set_xlabel('mutation rate')
  ax[1][0].set_ylabel('crossover rate')
  ax[1][0].set_title('Population=20 (Roulette)')

  surf = ax[1][1].pcolormesh(X, Y, calc_z(results_pop_20_tournament), **meshopts)
  ax[1][1].set_xlabel('mutation rate')
  ax[1][1].set_ylabel('crossover rate')
  ax[1][1].set_title('Population=20 (Tournament)')

  fig.colorbar(surf, ax=ax, orientation='horizontal', pad=0.07)