import sys
import time
import random
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import tkinter as tk
from tkinter import ttk

import search
from utils import argmax

LARGE_FONT = ('Verdana', 12)

# genetic algorithm variables
# feel free to play around with these
target = 'Genetic Algorithm' # the phrase to be generated
max_population = 100 # number of samples in each population
mutation_rate = 0.1 # probability of mutation
f_thres = len(target) # fitness threshold
ngen = 1200 # max number of generations to run the genetic algorithm

class GeneticAlgorithm(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		tk.Tk.wm_title(self, 'Genetic Algorithm')
		container = tk.Frame(self)
		container.pack(side='top', fill='both', expand=True)

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

class RunScreen(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		# label = ttk.Label(self, text='Run Screen', font=LARGE_FONT)
		# label.pack(pady=10, padx=10)

		# button1 = ttk.Button(self, text='Visit Home Screen', command=lambda: controller.show_frame(HomeScreen))
		# button1.pack()

app = GeneticAlgorithm()
app.geometry('800x600')
app.mainloop()