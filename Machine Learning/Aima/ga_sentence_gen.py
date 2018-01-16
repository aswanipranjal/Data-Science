import pygame
import time
import random
import search

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Phrase Generator')
clock = pygame.time.Clock()

target = 'To be or not to be.'
max_population = 500
mutation_rate = 0.01
# possible genes
gene_pool = [chr(x) for x in range(33, 127)]
gene_pool.append(' ')

def fitness_fn(phrase):
	fitness = 0
	for i in range(len(phrase)):
		if target[i] == phrase[i]:
			fitness += 1
	return fitness

def loop():
	crashed = False
	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				return

		pygame.display.update()
		clock.tick(60)

# print(gene_pool)
first_population = search.init_population(max_population, gene_pool, len(target))
first_sample_test = first_population[0]
first_sample_phrase = ''.join(first_sample_test)
selections = search.select(2, first_population, fitness_fn)
print(first_sample_phrase)
loop()
pygame.quit()