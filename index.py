from simulation import simulate
from numpy.random import randint, rand, choice
from numpy import divide, sum
from functools import reduce
 
# decode bitstring to numbers
def decode(bounds, n_bits, bitstring):
	decoded = list()
	largest = 2**n_bits-1
	for i in range(len(bounds)):
		# extract the substring
		start, end = i * n_bits, (i + 1) * n_bits
		# convert bitarray to integer
		integer = reduce(lambda a, b: a * 2 + b, bitstring[start:end])
		# scale integer to desired range
		value = bounds[i][0] + (integer/largest) * (bounds[i][1] - bounds[i][0])
		# store
		decoded.append(value)
	return decoded
 
# tournament selection
def tournament_selection(pop, scores):
	# first random selection
	selection_ix = randint(len(pop))
	for ix in randint(0, len(pop), 2):
		# check if better (e.g. perform a tournament)
		if scores[ix] > scores[selection_ix]:
			selection_ix = ix
	return pop[selection_ix]

# roulette selection
def roulette_selection(pop, scores):
	# first normalize scores
	scores = divide(scores, sum(scores))
	# then choose a random index based on the probability vector
	selection_ix = choice(len(pop), p=scores)
	# finally returns the element from that index
	return pop[selection_ix]
 
# crossover two parents to create two children
def crossover(p1, p2, r_cross):
	# children are copies of parents by default
	c1, c2 = p1.copy(), p2.copy()
	# check for recombination
	if rand() < r_cross:
		# select crossover point that is not on the end of the string
		pt = randint(1, len(p1)-2)
		# perform crossover
		c1 = p1[:pt] + p2[pt:]
		c2 = p2[:pt] + p1[pt:]
	return [c1, c2]
 
# mutation operator
def mutation(bitstring, r_mut):
	for i in range(len(bitstring)):
		# check for a mutation
		if rand() < r_mut:
			# flip the bit
			bitstring[i] = 1 - bitstring[i]
 
# genetic algorithm
def genetic_algorithm(objective, selection_alg, bounds, n_bits, target, n_pop, r_cross, r_mut):
	# number of generations needed to find the answer
	n_iter = 0
	# history of best scores
	scores_history = list()
	# initial population of random bitstring
	pop = [randint(0, 2, n_bits*len(bounds)).tolist() for _ in range(n_pop)]
	# keep track of best solution
	best, best_eval = 0, objective(decode(bounds, n_bits, pop[0]))
	# enumerate generations
	while best_eval < target:
		n_iter += 1
		# decode population
		decoded = [decode(bounds, n_bits, p) for p in pop]
		# evaluate all candidates in the population
		scores = [objective(d) for d in decoded]
		# check for new best solution
		scores_best = max(scores)
		scores_history.append(scores_best)
		if scores_best > best_eval:
			i = scores.index(scores_best)
			best, best_eval = pop[i], scores[i]
			print(">%d, new best f(%s) = %f" % (n_iter,  decoded[i], scores[i]))
		# select parents
		selected = [selection_alg(pop, scores) for _ in range(n_pop)]
		# create the next generation
		children = list()
		for i in range(0, n_pop, 2):
			# get selected parents in pairs
			p1, p2 = selected[i], selected[i+1]
			# crossover and mutation
			for c in crossover(p1, p2, r_cross):
				# mutation
				mutation(c, r_mut)
				# store for next generation
				children.append(c)
		# replace population
		pop = children
	best_decoded = decode(bounds, n_bits, best)
	return [best_decoded, best_eval, scores_history]

# define range for resistor
r_range = [0, 100]
# define range for input
bounds = [r_range, r_range]
# define the total iterations
target = 1.999
# bits per variable
n_bits = 8
# define the population size
n_pop = 20
# crossover rate
r_cross = 0.9
# mutation rate
r_mut = 1 / (float(n_bits) * len(bounds))

# perform the genetic algorithm search
def main(selection_alg_name, n_pop, r_cross, r_mut_mul):
	local_r_mut = r_mut * r_mut_mul
	selection_alg = tournament_selection if selection_alg_name == 'tournament' else roulette_selection
	return genetic_algorithm(simulate, selection_alg, bounds, n_bits, target, n_pop, r_cross, local_r_mut)
