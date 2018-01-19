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

def genetic_algorithm_stepwise()

def main():
	population = search.init_population(max_population, gene_pool, len(target))
	# solution = search.genetic_algorithm(population, fitness_fn, f_thres=len(target)-2, gene_pool=gene_pool)
	for i in range(100):
		population = [mutate(recombine(*select(2, population, fitness_fn)), gene_pool, mutation_rate) for i in range(len(population))]
		fittest_individual = argmax(population, key=fitness_fn)
		current_best_sentence = ''.join(fittest_individual)
		print(current_best_sentence)
	print(''.join(solution))
	print(fitness_fn(solution))

if __name__ == '__main__':
	main()