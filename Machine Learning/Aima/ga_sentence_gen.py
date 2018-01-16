import pygame
import time
import random
import search
from utils import argmax

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Phrase Generator')
clock = pygame.time.Clock()

target = 'To be'
max_population = 500
mutation_rate = 0.1
f_thres = len(target)
# possible genes
gene_pool = [chr(x) for x in range(33, 127)]
gene_pool.append(' ')

def text_objects(text, font):
	text_surface = font.render(text, True, black)
	return text_surface, text_surface.get_rect()

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
	for i in range(max_population):
		mating_pool.extend(fitnesses[i] * [population[i]])
	# print(len(list(fitnesses)))
	return mating_pool

def loop():
	# crashed = False
	i = 0
	large_text = pygame.font.Font('freesansbold.ttf', 115)
	population = search.init_population(max_population, gene_pool, len(target))
	while i < 500:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				return

		new_population = [search.mutate(search.recombine(*select(2, population, fitness_fn)), gene_pool, mutation_rate)]
		# fittest_individual = search.fitness_threshold(fitness_fn, f_thres, population)
		fittest_individual = argmax(new_population, key=fitness_fn)
		current_best = ''.join(fittest_individual)
		game_display.fill(white)
		text_surface, text_rect = text_objects(current_best, large_text)
		text_rect.center = ((display_width/2), (display_height/2))
		game_display.blit(text_surface, text_rect)
		population = new_population
		# time.sleep(20)
		pygame.display.update()
		clock.tick(60)
		i += 1

# print(gene_pool)
# first_population = search.init_population(max_population, gene_pool, len(target))
# first_sample_test = first_population[0]
# first_sample_phrase = ''.join(first_sample_test)
# selections = search.select(2, first_population, fitness_fn)
# # first_sample_selection = ''.join(selections[0])
# print('First population')
# for i in range(10):
# 	print(''.join(first_population[i]))
# 	print(fitness_fn(first_population[i]))
# print('\n\nSecond population')
# for i in range(10):
# 	print(''.join(selections[i]))
# 	print(fitness_fn(selections[i]))
# print('\n\nThird population')
# second_population = selections
# selections = search.select(10, second_population, fitness_fn)
# for i in range(10):
# 	print(''.join(selections[i]))
# 	print(fitness_fn(selections[i]))
# # print(first_sample_phrase)

# first_population = search.init_population(max_population, gene_pool, len(target))
# max_of_gen_1 = search.genetic_algorithm(first_population, fitness_fn, gene_pool, 5, 10)
# print(max_of_gen_1)
# loop()
first_population = search.init_population(max_population, gene_pool, len(target))
print(first_population)
pool = []
print(2 * [first_population[0]])
pool.extend(2 * [first_population[0]])
print('Pool')
print(pool)
print(5 * [first_population[1]])
pool.extend(5 * [first_population[1]])
print('Pool')
print(pool)

print(select(2, first_population, fitness_fn))
pygame.quit()