import sys
import time
import random
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from tkinter import *

import search
from utils import argmax

LARGE_FONT = ('Verdana', 12)
EXTRA_LARGE_FONT = ('Consolas', 36, 'bold')

canvas_width = 800
canvas_height = 600

black = '#000000'
white = '#ffffff'
p_blue = '#042533'
lp_blue = '#0c394c'

# genetic algorithm variables
# feel free to play around with these
target = 'Genetic Algorithm' # the phrase to be generated
max_population = 100 # number of samples in each population
mutation_rate = 0.1 # probability of mutation
f_thres = len(target) # fitness threshold
ngen = 1200 # max number of generations to run the genetic algorithm

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

def raise_frame(frame):
	frame.tkraise()

root = Tk()
f1 = Frame(root)
f2 = Frame(root)

for frame in (f1, f2):
	frame.grid(row=0, column=0, sticky='news')

def genetic_algorithm_stepwise(population):
	root.title('Genetic Algorithm')
	canvas = Canvas(root, width=canvas_width, height=canvas_height)
	canvas.pack(expand=YES, fill=BOTH, padx=20, pady=20)
	for generation in range(ngen):
		population = [search.mutate(search.recombine(*search.select(2, population, fitness_fn)), gene_pool, mutation_rate) for i in range(len(population))]
		current_best = ''.join(argmax(population, key=fitness_fn))
		members = [''.join(x) for x in population][:48]

		canvas.delete('all')
		canvas.create_text(canvas_width / 2, 40, fill=p_blue, font='Consolas 46 bold', text=current_best)

		for i in range(len(members) // 3):
			canvas.create_text((canvas_width * .175), (canvas_height * .25 + (25 * i)), fill=lp_blue, font='Consolas 16', text=members[3 * i])
			canvas.create_text((canvas_width * .500), (canvas_height * .25 + (25 * i)), fill=lp_blue, font='Consolas 16', text=members[3 * i + 1])
			canvas.create_text((canvas_width * .825), (canvas_height * .25 + (25 * i)), fill=lp_blue, font='Consolas 16', text=members[3 * i + 2])

		canvas.create_text((canvas_width * .5), (canvas_height * 0.95), fill=p_blue, font='Consolas 18 bold', text=f'Generation {generation}')

		scaling_factor = fitness_fn(current_best) / len(target)
		canvas.create_rectangle(canvas_width * 0.1, 90, canvas_width * 0.9, 100, outline=p_blue)
		canvas.create_rectangle(canvas_width * 0.1, 90, canvas_width * 0.1 + scaling_factor * canvas_width * 0.8, 100, fill=lp_blue)
		canvas.update()

		fittest_individual = search.fitness_threshold(fitness_fn, f_thres, population)
		if fittest_individual:
			break

population = search.init_population(max_population, gene_pool, len(target))
genetic_algorithm_stepwise(population)
root.mainloop()