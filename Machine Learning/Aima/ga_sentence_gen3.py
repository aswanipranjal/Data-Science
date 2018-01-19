import search
import random
from utils import argmax

target = 'Machine Learning'
max_population = 100
mutation_rate = 0.01
f_thres = len(target)

u_case = [chr(x) for x in range(65, 91)]
l_case = [chr(x) for x in range(97, 123)]
gene_pool = []
gene_pool.extend(u_case)
gene_pool.extend(l_case)
gene_pool.append(' ')

def fitness_fn(_list):
	fitness = 0
	phrase = ''.join(_list)
	for i in range(len(phrase)):
		if target[i] == phrase[i]:
			fitness += 1
	return fitness

def genetic_algorithm_stepwise(population, fitness_fn, gene_pool=[0, 1], f_thres=None, ngen=1000, pmut=0.1):
	for i in range(ngen):
		population = [mutate(recombine(*select(2, population, fitness_fn)), gene_pool, pmut) for i in range(len(population))]
		current_best = ''.join(argmax(population, key=fitness_fn))
		print(current_best)

		fittest_individual = search.fitness_threshold(fitness_fn, f_thres, population)
		if fittest_individual:
			return fittest_individual

	return argmax(population, key=fitness_fn)

def main():
	population = search.init_population(max_population, gene_pool, len(target))
	solution = search.genetic_algorithm(population, fitness_fn, f_thres=len(target)-2, gene_pool=gene_pool)
	print()
	print(''.join(solution))
	print(fitness_fn(solution))

if __name__ == '__main__':
	main()