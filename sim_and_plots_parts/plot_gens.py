plt.figure()

quant_normal = 0
quant_primeira = 0
quant_nunca = 0

for result in (results_pop_10_roulette, results_pop_10_tournament, results_pop_20_roulette, results_pop_20_tournament):
  for row in results_pop_10_tournament:
    for col in row:
      for sim_result in col:
        scores_history = sim_result[2][0:25]
        if len(scores_history) == 0:
          quant_primeira += 1
          continue
        if sim_result[1] < 1.999:
          quant_nunca += 1
          continue
        if len(scores_history) < 25:
          last_score = scores_history[len(scores_history) - 1]
          scores_history += [last_score] * (25 - len(scores_history))
        plt.plot(range(1,26), scores_history, linewidth=0.1, color='black')
        quant_normal += 1
plt.xlabel('Number of generations')
plt.ylabel('Delivered power')
quant_normal, quant_primeira, quant_nunca