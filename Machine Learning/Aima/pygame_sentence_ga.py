import time
import random
import pygame
from pygame.color import *
from pygame.locals import *

# imports from aimacode files
import search
import random
from utils import argmax

pygame.init()
display_width = 800
display_height = 600

# defining colors
black = (0, 0, 0)
white = (255, 255, 255)
p_blue = (4, 37, 51)
light_p_blue = (12, 57, 76)

# defining mandatory pygame variables
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Genetic Algorithm')
clock = pygame.time.Clock()

# genetic algorithm variables
target = 'Hello' # the phrase to be generated
max_population = 100 # number of samples in each population
mutation_rate = 0.1 
f_thres = len(target) # fitness threshold

generation = 0 # counter to keep track of generation number

u_case = [chr(x) for x in range(65, 91)] 		# list containing all uppercase characters
l_case = [chr(x) for x in range(97, 123)]		# list containing all lowercase characters
punctuations1 = [chr(x) for x in range(33, 48)]	# lists containing punctuation symbols
punctuations2 = [chr(x) for x in range(58, 65)]
punctuations3 = [chr(x) for x in range(91, 97)]
numerals = [chr(x) for x in range(48, 58)]		# list containing numbers

# extend the gene pool with the required lists and append the space character
gene_pool = []
gene_pool.extend(u_case)
gene_pool.extend(l_case)
gene_pool.append(' ')

# helper function that returns surface and coordinates of text box
def text_objects(text, font, color):
	text_surface = font.render(text, True, color)
	return text_surface, text_surface.get_rect()

# helper function to create a button
def button(msg, x, y, w, h, i_color, a_color, action=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if x + w > mouse[0] > x and y + h > mouse[1] > y:
		pygame.draw.rect(screen, a_color, (x, y, w, h))
		if click[0] == 1 and action != None:
			action()
	else:
		pygame.draw.rect(screen, i_color, (x, y, w, h))

	small_text = pygame.font.SysFont('Consolas', 16)
	m_text_surface, m_text_rect = text_objects(msg, small_text, white)
	m_text_rect.center = ((x + (w / 2)), (y + (h / 2)))
	screen.blit(m_text_surface, m_text_rect)

# fitness function
def fitness_fn(_list):
	fitness = 0
	# create string from list of characters
	phrase = ''.join(_list)
	# add 1 to fitness value for every matching character
	for i in range(len(phrase)):
		if target[i] == phrase[i]:
			fitness += 1
	return fitness

def game_loop(population, fitness_fn, gene_pool=[0, 1], f_thres=None, ngen=1200, pmut=0.1):
	global generation
	running = True
	finished = False
	while running:
		for event in pygame.event.get():
			# defining functions to execute on keypresses
			if event.type == pygame.QUIT:
				running = False
			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				running = False
			elif event.type == KEYDOWN and event.key == K_p:
				pygame.image.save(screen, 'genetic_algorithm_phrase_gen.png') # screenshot

		if not finished:
			screen.fill(THECOLORS['white'])
			generation += 1
			# generating new population after selecting, recombining and mutating the existing population
			population = [search.mutate(search.recombine(*search.select(2, population, fitness_fn)), gene_pool, pmut) for i in range(len(population))]
			# genome with the highest fitness in the current generation
			current_best = ''.join(argmax(population, key=fitness_fn))

			# checks for completion
			fittest_individual = search.fitness_threshold(fitness_fn, f_thres, population)
			if fittest_individual:
				finished = True
				# return fittest_individual

			# displays current best on top of the screen
			large_text = pygame.font.SysFont('Consolas', 80, bold=True)
			m_text_surface, m_text_rect = text_objects(current_best, large_text, p_blue)
			m_text_rect.center = ((display_width/2), (display_height * 0.1))
			screen.blit(m_text_surface, m_text_rect)
			
			# collecting first few examples from the current population
			members = [''.join(x) for x in population][:48]
			small_text = pygame.font.SysFont('Consolas', 20)
			# displaying a part of the population on the screen
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

			# displays blue bar that indicates current maximum fitness compared to maximum possible fitness
			scaling_factor = fitness_fn(current_best) / len(target)
			pygame.draw.rect(screen, p_blue, (m_text_rect[0], m_text_rect[1] + 85, m_text_rect[2], 10), 2)
			pygame.draw.rect(screen, (12 - 12 * scaling_factor, 57 - 57 *scaling_factor, 76 - 76 * scaling_factor), (m_text_rect[0], m_text_rect[1] + 85, m_text_rect[2] * scaling_factor, 10))

			# displays current generation number
			g_text_surface, g_text_rect = text_objects(f'Generation {generation}', pygame.font.SysFont('Consolas', 20, bold=True), light_p_blue)
			g_text_rect.center = ((display_width * 0.5), (display_height * 0.95))
			screen.blit(g_text_surface, g_text_rect)

		else:
			button('NEXT', display_width * 0.875, display_height * 0.905, display_width * 0.075, display_height * 0.05, p_blue, light_p_blue, None)

		# updates the screen
		pygame.display.update()
		clock.tick(60)

	# return argmax(population, key=fitness_fn)
	# time.sleep(100)

if __name__ == '__main__':
	population = search.init_population(max_population, gene_pool, len(target))
	solution = game_loop(population, fitness_fn, gene_pool=gene_pool, f_thres=len(target), pmut=mutation_rate)
	# pygame.quit()
	# time.sleep(1000)
	pygame.quit()