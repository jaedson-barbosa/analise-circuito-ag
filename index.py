from simulation import simulate
from numpy.random import randint, rand, choice, randn
from numpy import divide, sum, clip
 
r_range = [-2, 5]
bounds = [r_range, r_range]
target = 0.99
n_iter_max = 50
n_simulations = 2
 
def tournament_selection(pop, scores):
	ia, ib = randint(len(pop), size=2)
	return pop[ia] if scores[ia] > scores[ib] else pop[ib]

def roulette_selection(pop, scores):
	return pop[choice(len(pop), p=divide(scores, sum(scores)))]
 
def crossover(p1, p2, r_cross):
	c1, c2 = p1.copy(), p2.copy()
	for i in range(len(c1)):
		if rand() < r_cross:
			alpha = rand()
			c1[i] = p1[i] * alpha + p2[i] * (1 - alpha)
			c2[i] = p1[i] * (1 - alpha) + p2[i] * alpha
	return [c1, c2]
 
def mutation(number, r_mut, bounds):
	for i in range(len(number)):
		if rand() < r_mut:
			number[i] = clip(number[i] + randn(), a_min=bounds[i][0], a_max=bounds[i][1])
 
def genetic_algorithm(objective, selection_alg, bounds, target, n_pop, r_cross, r_mut):
	n_iter = 0
	scores_history = list()
	pop = [[randint(b[0], b[1]) for b in bounds] for _ in range(n_pop)]
	best = pop[0]
	best_score = objective(pop[0])
	while best_score < target and n_iter < n_iter_max:
		n_iter += 1
		scores = [objective(d) for d in pop]
		generation_best_score = max(scores)
		if generation_best_score > best_score:
			i = scores.index(generation_best_score)
			best, best_score = pop[i], scores[i]
		scores_history.append(generation_best_score)
		for i in range(0, n_pop, 2):
			p1, p2 = selection_alg(pop, scores), selection_alg(pop, scores)
			c1, c2 = crossover(p1, p2, r_cross)
			mutation(c1, r_mut, bounds)
			mutation(c2, r_mut, bounds)
			pop[i], pop[i+1] = c1, c2
	return [best, best_score, scores_history]

def main(selection_alg_name, n_pop, r_cross, r_mut):
	r_mut /= len(bounds)
	selection_alg = tournament_selection if selection_alg_name == 'tournament' else roulette_selection
	return [genetic_algorithm(simulate, selection_alg, bounds, target, n_pop, r_cross, r_mut) for _ in range(n_simulations)]
