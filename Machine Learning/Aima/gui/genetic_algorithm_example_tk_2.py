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

root = Tk()
var = StringVar()
var.set('')

l = Label(root, textvariable=var)
l.pack()

population = search.init_population(max_population, gene_pool, len(target))

for i in range(ngen):
	population = [search.mutate(search.recombine(*search.select(2, population, fitness_fn)), gene_pool, mutation_rate) for i in range(len(population))]
	current_best = ''.join(argmax(population, key=fitness_fn))
	var.set(current_best)
	root.update_idletasks()