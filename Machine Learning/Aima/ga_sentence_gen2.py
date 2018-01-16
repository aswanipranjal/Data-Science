import search
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

def select(r, population, fitness_fn):
	fitnesses = list(map(fitness_fn, population))
	mating_pool = []
	selection = []
	for i in range(max_population):
		mating_pool.extend(fitnesses[i] * [population[i]])
	# print(len(list(fitnesses)))
	for i in range(r):
		ix = random.randint(0, len(mating_pool))
		selection.append(mating_pool[ix])
	return selection

def main():
	for _ in range()
		new_population = [search.mutate(search.recombine(*select(2, population, fitness_fn)), gene_pool, mutation_rate)]
		# fittest_individual = search.fitness_threshold(fitness_fn, f_thres, population)
		fittest_individual = argmax(new_population, key=fitness_fn)
		current_best = ''.join(fittest_individual)
		game_display.fill(white)
		text_surface, text_rect = text_objects(current_best, large_text)
		text_rect.center = ((display_width/2), (display_height/2))
		game_display.blit(text_surface, text_rect)
		population = new_population