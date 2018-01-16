import search
import random
from utils import argmax

target = 'To be'
max_population = 500
mutation_rate = 0.1
f_thres = len(target)
# possible genes
gene_pool = [chr(x) for x in range(33, 127)]
gene_pool.append(' ')

def fitness_fn(_list):
	fitness = 0
	phrase = ''.join(_list)
	for i in range(len(phrase)):
		if target[i] == phrase[i]:
			fitness += 1
	return fitness

def select(r, population, fitness_fn, mating_pool):
	fitnesses = list(map(fitness_fn, population))
	for i in range(len(population)):
		mating_pool.extend(10 * fitnesses[i] * [population[i]])
	# print(mating_pool)
	# print(len(list(fitnesses)))
	selection = random.sample(mating_pool, r)
	return selection

def main():
	population = search.init_population(max_population, gene_pool, len(target))
	mating_pool = []
	for _ in range(100):
		new_population = [search.mutate(search.recombine(*select(2, population, fitness_fn, mating_pool)), gene_pool, mutation_rate)]
		fittest_individual = argmax(new_population, key=fitness_fn)
		current_best = ''.join(fittest_individual)
		print(current_best)
		population = new_population

# population = search.init_population(max_population, gene_pool, len(target))
# selection = select(2, population, fitness_fn)
# print(selection)
# print(selection)
main()