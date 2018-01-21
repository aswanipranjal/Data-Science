import time
import pygame
import random

import search
import random
from utils import argmax

pygame.init()
display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Genetic Algorithm')
clock = pygame.time.Clock()

# genetic algorithm variables
target = ''
max_population = 100
mutation_rate = 0.1
f_thres = len(target)

u_case = [chr(x) for x in range(65, 91)]
l_case = [chr(x) for x in range(97, 123)]
punctuations1 = [chr(x) for x in range(33, 48)]
punctuations2 = [chr(x) for x in range(58, 65)]
punctuations3 = [chr(x) for x in range(91, 97)]
numerals = [chr(x) for x in range(48, 58)]

# extend the gene pool with the required lists
gene_pool = []
gene_pool.extend(u_case)
gene_pool.extend(l_case)
gene_pool.append(' ')

def text_objects(text, font):
	text_surface = font.render(text, True, black)
	return text_surface, text_surface.get_rect()

def button(msg, x, y, w, h, i_color, a_color, action=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if x + w > mouse[0] > x and y + h > mouse[1] > y:
		pygame.draw.rect(screen, a_color, (x, y, w, h))
		if click[0] == 1 and action != None:
			action()
	else:
		pygame.draw.rect(screen, i_color, (x, y, w, h))

	small_text = pygame.font.Font('freesansbold.ttf', 20)
	m_text_surface, m_text_rect = text_objects(msg, small_text)
	m_text_rect.center = ((x + (w / 2)), (y + (h / 2)))
	screen.blit(m_text_surface, m_text_rect)

def fitness_fn(_list):
	fitness = 0
	phrase = ''.join(_list)
	for i in range(len(phrase)):
		if target[i] == phrase[i]:
			fitness += 1
	return fitness

def genetic_algorithm_stepwise(population, fitness_fn, gene_pool=[0, 1], f_thres=None, ngen=1200, pmut=0.1):
	for i in range(ngen):
		population = [search.mutate(search.recombine(*search.select(2, population, fitness_fn)), gene_pool, pmut) for i in range(len(population))]
		current_best = ''.join(argmax(population, key=fitness_fn))
		print(f'current best: {current_best}\tIteration: {str(i)}\tFitness: {fitness_fn(current_best)}\r', end='')

		fittest_individual = search.fitness_threshold(fitness_fn, f_thres, population)
		if fittest_individual:
			return fittest_individual, i

	return argmax(population, key=fitness_fn), i

def main():
	population = search.init_population(max_population, gene_pool, len(target))
	solution, iteration = genetic_algorithm_stepwise(population, fitness_fn, f_thres=len(target), gene_pool=gene_pool, pmut=mutation_rate)

if __name__ == '__main__':
	main()