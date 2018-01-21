import time
import random
import pygame
from pygame.color import *
from pygame.locals import *

import search
import random
from utils import argmax

pygame.init()
display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
p_blue = (4, 37, 51)
light_p_blue = (12, 57, 76)

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Genetic Algorithm')
clock = pygame.time.Clock()

# genetic algorithm variables
target = 'Genetic Algorithm'
max_population = 75
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

def text_objects(text, font, color):
	text_surface = font.render(text, True, color)
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

def game_loop(population, fitness_fn, gene_pool=[0, 1], f_thres=None, ngen=1200, pmut=0.1):
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				running = False
			elif event.type == KEYDOWN and event.key == K_p:
				pygame.image.save(screen, 'genetic_algorithm_phrase_gen.png')

		screen.fill(THECOLORS['white'])
		population = [search.mutate(search.recombine(*search.select(2, population, fitness_fn)), gene_pool, pmut) for i in range(len(population))]
		current_best = ''.join(argmax(population, key=fitness_fn))
		large_text = pygame.font.SysFont('Consolas', 80, bold=True)
		m_text_surface, m_text_rect = text_objects(current_best, large_text, p_blue)
		m_text_rect.center = ((display_width/2), (display_height * 0.1))
		screen.blit(m_text_surface, m_text_rect)
		
		members = [''.join(x) for x in population][:48]
		small_text = pygame.font.SysFont('Consolas', 20)
		for i in range(len(members) // 3):
			m_text_surface1, m_text_rect1 = text_objects(members[3*i], small_text, light_p_blue)
			m_text_surface2, m_text_rect2 = text_objects(members[3*i+1], small_text, light_p_blue)
			m_text_surface3, m_text_rect3 = text_objects(members[3*i+2], small_text, light_p_blue)
			m_text_rect1.center = ((display_width * .175), (display_height * 0.25 + (25 * i)))
			m_text_rect3.center = ((display_width * .500), (display_height * 0.25 + (25 * i)))
			m_text_rect2.center = ((display_width * .825), (display_height * 0.25 + (25 * i)))
			screen.blit(m_text_surface1, m_text_rect1)
			screen.blit(m_text_surface2, m_text_rect2)
			screen.blit(m_text_surface3, m_text_rect3)

		scaling_factor = fitness_fn(current_best) / len(target)
		pygame.draw.rect(screen, p_blue, (m_text_rect[0], m_text_rect[1] + 85, m_text_rect[2], 10), 2)
		pygame.draw.rect(screen, (12 - 12 * scaling_factor, 57 - 57 *scaling_factor, 76 - 76 * scaling_factor), (m_text_rect[0], m_text_rect[1] + 85, m_text_rect[2] * scaling_factor, 10))

		fittest_individual = search.fitness_threshold(fitness_fn, f_thres, population)
		if fittest_individual:
			running = False
			return fittest_individual

		pygame.display.update()
		clock.tick(60)

	return argmax(population, key=fitness_fn)

if __name__ == '__main__':
	population = search.init_population(max_population, gene_pool, len(target))
	solution = game_loop(population, fitness_fn, gene_pool=gene_pool, f_thres=len(target), pmut=mutation_rate)
	pygame.quit()