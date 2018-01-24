# A simple program that implements the solution to the phrase generation problem using
# genetic algorithms as given in the search.ipynb notebook.
# 
# Displays best individual of the current generation
# Displays a progress bar that indicates the amount of completion of the algorithm
# Displays the first few individuals of the current generation

import time
import random
import pygame
from pygame.color import *
from pygame.locals import *

# imports from aimacode files
import search
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
# feel free to play around with these
target = 'Genetic Algorithm' # the phrase to be generated
max_population = 100 # number of samples in each population
mutation_rate = 0.1 # probability of mutation
f_thres = len(target) # fitness threshold
ngen = 1200 # max number of generations to run the genetic algorithm

# selector values to select the ga variables in the home screen
max_population_selector = None
mutation_rate_selector = None
f_thres_selector = None
ngen_selector = None

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
	# gets mouse position
	mouse = pygame.mouse.get_pos()
	# gets mouse click position
	click = pygame.mouse.get_pressed()

	if x + w > mouse[0] > x and y + h > mouse[1] > y:
		pygame.draw.rect(screen, a_color, (x, y, w, h))
		if click[0] == 1 and action != None:
			action()
	else:
		pygame.draw.rect(screen, i_color, (x, y, w, h))

	# defining text box area and font properties
	small_text = pygame.font.SysFont('Consolas', 16)
	m_text_surface, m_text_rect = text_objects(msg, small_text, white)
	m_text_rect.center = ((x + (w / 2)), (y + (h / 2)))
	screen.blit(m_text_surface, m_text_rect)


# The three following helper functions help the user to select the values of the ga variables on the home screen
# These functions can be combined into one by not using global variables. To be done in a future patch
def f_max_population_selector(msg, x, y, w, h, i_color, a_color):
	# (apologies for using global variables)
	global max_population_selector
	global max_population

	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	# draws outer rectangle
	pygame.draw.rect(screen, i_color, (x, y, w, h), 2)
	if x + w > mouse[0] > x and y + h > mouse[1] > y:
		pygame.draw.rect(screen, a_color, (x, y, mouse[0] - x, h))
		if click[0] == 1:
			max_population_selector = mouse[0] - x

	if max_population and not max_population_selector:
		pygame.draw.rect(screen, a_color, (x, y, int(w * (max_population - 2) / 1000), h))
	elif max_population_selector:
		pygame.draw.rect(screen, a_color, (x, y, max_population_selector, h))
		max_population = int(1000 * max_population_selector / w) + 2

	# defining text box area and font properties
	small_text = pygame.font.Font('freesansbold.ttf', 14)
	m_text_surface, m_text_rect = text_objects(msg + ' ' + str(max_population), small_text, i_color)
	m_text_rect.center = ((x + (w / 2)), (y + (h / 2) - 14))
	screen.blit(m_text_surface, m_text_rect)

def f_mutation_rate_selector(msg, x, y, w, h, i_color, a_color):
	global mutation_rate_selector
	global mutation_rate
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	pygame.draw.rect(screen, i_color, (x, y, w, h), 2)
	if x + w > mouse[0] > x and y + h > mouse[1] > y:
		pygame.draw.rect(screen, a_color, (x, y, mouse[0] - x, h))
		if click[0] == 1:
			mutation_rate_selector = mouse[0] - x

	if mutation_rate and not mutation_rate_selector:
		pygame.draw.rect(screen, a_color, (x, y, w * mutation_rate / 1, h))
	elif mutation_rate_selector:
		pygame.draw.rect(screen, a_color, (x, y, mutation_rate_selector, h))
		mutation_rate = 1 * mutation_rate_selector / w

	# defining text box area and font properties
	small_text = pygame.font.Font('freesansbold.ttf', 14)
	m_text_surface, m_text_rect = text_objects(msg + ' ' + str(mutation_rate), small_text, i_color)
	m_text_rect.center = ((x + (w / 2)), (y + (h / 2) - 14))
	screen.blit(m_text_surface, m_text_rect)

def f_fthres_selector(msg, x, y, w, h, i_color, a_color):
	global f_thres_selector
	global f_thres
	f_thres = len(target)
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	pygame.draw.rect(screen, i_color, (x, y, w, h), 2)
	if x + w > mouse[0] > x and y + h > mouse[1] > y:
		pygame.draw.rect(screen, a_color, (x, y, mouse[0] - x, h))
		if click[0] == 1:
			f_thres_selector = mouse[0] - x

	if f_thres and not f_thres_selector:
		pygame.draw.rect(screen, a_color, (x, y, int(w * f_thres / len(target)), h))
	elif f_thres_selector:
		pygame.draw.rect(screen, a_color, (x, y, f_thres_selector, h))
		f_thres = int(len(target) * f_thres_selector / w)

	# defining text box area and font properties
	small_text = pygame.font.Font('freesansbold.ttf', 14)
	m_text_surface, m_text_rect = text_objects(msg + ' ' + str(f_thres), small_text, i_color)
	m_text_rect.center = ((x + (w / 2)), (y + (h / 2) - 14))
	screen.blit(m_text_surface, m_text_rect)

def f_ngen_selector(msg, x, y, w, h, i_color, a_color):
	global ngen_selector
	global ngen
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	pygame.draw.rect(screen, i_color, (x, y, w, h), 2)
	if x + w > mouse[0] > x and y + h > mouse[1] > y:
		pygame.draw.rect(screen, a_color, (x, y, mouse[0] - x, h))
		if click[0] == 1:
			ngen_selector = mouse[0] - x

	if ngen and not ngen_selector:
		pygame.draw.rect(screen, a_color, (x, y, int(w * ngen / 2000), h))
	elif ngen_selector:
		pygame.draw.rect(screen, a_color, (x, y, ngen_selector, h))
		ngen = int(2000 * ngen_selector / w)

	# defining text box area and font properties
	small_text = pygame.font.Font('freesansbold.ttf', 14)
	m_text_surface, m_text_rect = text_objects(msg + ' ' + str(ngen), small_text, i_color)
	m_text_rect.center = ((x + (w / 2)), (y + (h /2) - 14))
	screen.blit(m_text_surface, m_text_rect)

def change_color(color):
	if color == white:
		return black
	return white

# function to quit the game
def quitgame():
	pygame.quit()
	quit()

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

# function to display the home screen
# start typing on the home screen to change the target value
# click on the sliders to change the values of the other parameters
# click go to run the genetic algorithm with the defined parameters and click exit to close the program
def game_intro():
	framecount = 0
	intro = True
	global target
	name = 'Genetic Algorithm'
	cursor_color = black
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				intro = False
				quitgame()
			# accepts keypresses from the user, and if it is an alphabet, it will be appended to the variable 'name'
			# to accept punctuation marks, replace the first if statement with `if event.unicode:`
			# also change the gene pool if you do this, or the genetic algorithm will not be able to converge
			elif event.type == KEYDOWN:
				if event.unicode.isalpha() or event.unicode == ' ':
					name += event.unicode
		# checks if the backspace key is held down
		_keys = pygame.key.get_pressed()
		if _keys[K_BACKSPACE]:
			name = name[:-1]

		# target variable changes only when the length of `name` if greater than 0
		if len(name) > 0:
			target = name

		# clear the screen
		screen.fill(white)
		# defining text box area and font properties
		large_text = pygame.font.SysFont('Consolas', 60, bold=True)
		m_text_surface, m_text_rect = text_objects(name, large_text, p_blue)
		m_text_rect.center = ((display_width/2), (display_height * 0.2))
		screen.blit(m_text_surface, m_text_rect)

		# draws cursor next to text box
		if framecount % 7 == 0:
			cursor_color = change_color(cursor_color)
		pygame.draw.rect(screen, cursor_color, (m_text_rect[0] + m_text_rect[2], m_text_rect[1], 2, m_text_rect[3]))

		# function calls to create the `GO` and `EXIT` buttons
		button('GO', 100, 450, 100, 50, p_blue, light_p_blue, main)
		button('EXIT', 600, 450, 100, 50, p_blue, light_p_blue, quitgame)

		# functions to create the sliders
		f_max_population_selector('Max population size', display_width*0.1, display_height*0.35, display_width*0.8, 10, p_blue, light_p_blue)
		f_mutation_rate_selector('Mutation rate', display_width*0.1, display_height*0.45, display_width*0.8, 10, p_blue, light_p_blue)
		f_fthres_selector('Fitness threshold', display_width*0.1, display_height*0.55, display_width*0.8, 10, p_blue, light_p_blue)
		f_ngen_selector('Max number of generations', display_width*0.1, display_height*0.65, display_width*0.8, 10, p_blue, light_p_blue)

		pygame.display.update()
		framecount += 1
		clock.tick(15)

def game_loop(population, fitness_fn, gene_pool=[0, 1], f_thres=None, ngen=1200, pmut=0.1):
	global generation
	generation = 0
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

		# set finished to True if we exceed the maximum number of generations
		if generation >= ngen:
			finished = True

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
			button('NEXT', display_width * 0.9, display_height * 0.920, display_width * 0.070, display_height * 0.05, p_blue, light_p_blue, game_intro)

		# updates the screen
		pygame.display.update()
		clock.tick(60)

	# return argmax(population, key=fitness_fn)
	# time.sleep(100)

def main():
	population = search.init_population(max_population, gene_pool, len(target))
	solution = game_loop(population, fitness_fn, gene_pool=gene_pool, f_thres=f_thres, pmut=mutation_rate, ngen=ngen)

if __name__ == '__main__':
	# pygame.quit()
	# time.sleep(1000)
	game_intro()
	# main()
	pygame.quit()