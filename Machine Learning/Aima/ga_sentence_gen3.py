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

def main():
	population = search.init_population(max_population, gene_pool, len(target))
	solution = search.genetic_algorithm(population, fitness_fn, f_thres=len(target)-2, gene_pool=gene_pool)
	print(''.join(solution))
	print(fitness_fn(solution))

if __name__ == '__main__':
	main()