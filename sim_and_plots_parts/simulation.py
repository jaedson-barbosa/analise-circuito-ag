from index import main

r_cross_opts = (0.6, 0.7, 0.8, 0.9, 1)
r_mut_opts = (0, 0.25, 0.5, 0.75, 1)
results_pop_10_roulette = list()
results_pop_10_tournament = list()
results_pop_20_roulette = list()
results_pop_20_tournament = list()

for r_cross in r_cross_opts:
  row_results_pop_10_roulette = list()
  row_results_pop_10_tournament = list()
  row_results_pop_20_roulette = list()
  row_results_pop_20_tournament = list()

  for r_mut in r_mut_opts:
    print((r_cross, r_mut))
    row_results_pop_10_roulette.append(main('roulette', 10, r_cross, r_mut))
    row_results_pop_10_tournament.append(main('tournament', 10, r_cross, r_mut))
    row_results_pop_20_roulette.append(main('roulette', 20, r_cross, r_mut))
    row_results_pop_20_tournament.append(main('tournament', 20, r_cross, r_mut))

  results_pop_10_roulette.append(row_results_pop_10_roulette)
  results_pop_10_tournament.append(row_results_pop_10_tournament)
  results_pop_20_roulette.append(row_results_pop_20_roulette)
  results_pop_20_tournament.append(row_results_pop_20_tournament)