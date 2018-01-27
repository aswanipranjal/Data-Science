import sys
import time
import random
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import tkinter as tk
from tkinter import ttk
from tkinter import font

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

def genetic_algorithm_stepwise(population, fitness_fn, gene_pool=[0, 1], f_thres=None, ngen=1200, pmut=0.1):
	for i in range(ngen):
		population = [search.mutate(search.recombine(*search.select(2, population, fitness_fn)), gene_pool, pmut) for i in range(len(population))]
		current_best = ''.join(argmax(population, key=fitness_fn))
		# print(f'Current best: {current_best}\tIteration: {str(i)}\tFitness: {fitness_fn(current_best)}\r', end='')

		fittest_individual = search.fitness_threshold(fitness_fn, f_thres, population)
		if fittest_individual:
			return fittest_individual, i

	return argmax(population, key=fitness_fn), i

class GeneticAlgorithm(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		tk.Tk.wm_title(self, 'Genetic Algorithm')
		container = tk.Frame(self)
		container.pack(side='top', fill='both', expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (HomeScreen, RunScreen):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky='nsew')

		self.show_frame(HomeScreen)

	def show_frame(self, controller):
		frame = self.frames[controller]
		frame.tkraise()

class HomeScreen(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		# label = ttk.Label(self, text='Home Screen', font=LARGE_FONT)
		# label.pack(pady=10, padx=10)

		# button1 = ttk.Button(self, text='Visit Run Screen', command=lambda: controller.show_frame(RunScreen))
		# button1.pack()
		button1 = ttk.Button(self, text='Run', command=lambda: controller.show_frame(RunScreen))
		button1.pack()

class RunScreen(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		# label = ttk.Label(self, text='Run Screen', font=LARGE_FONT)
		# label.pack(pady=10, padx=10)

		# button1 = ttk.Button(self, text='Visit Home Screen', command=lambda: controller.show_frame(HomeScreen))
		# button1.pack()
		# label = tk.Label(self, text=target, font=EXTRA_LARGE_FONT)
		# label.pack(pady=25, padx=10)
		population = search.init_population(max_population, gene_pool, len(target))
		# self.genetic_algorithm_stepwise(population, fitness_fn, gene_pool, len(target), ngen, mutation_rate)
		# v = tk.StringVar()
		# label = tk.Label(self, textvariable=v)
		# label.pack()
		# print('In this function')
		# for i in range(ngen):
		# 	time.sleep(0.2)
		# 	population = [search.mutate(search.recombine(*search.select(2, population, fitness_fn)), gene_pool, mutation_rate) for i in range(len(population))]
		# 	current_best = ''.join(argmax(population, key=fitness_fn))

		# 	# checks for completion
		# 	fittest_individual = search.fitness_threshold(fitness_fn, f_thres, population)
		# 	if fittest_individual:
		# 		finished = True

		# 	v.set(current_best)
		# 	self.update_idletasks()
			# label.configure(text=current_best)
			# label.update()

app = GeneticAlgorithm()
app.geometry('800x600')
app.mainloop()