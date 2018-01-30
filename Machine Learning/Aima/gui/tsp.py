from tkinter import *
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from search import *
import numpy as np

distances = {}

class TSP_problem(Problem):

	def two_opt(self, state):
		neighbour_state = state[:]
		left = random.randint(0, len(neighbour_state) - 1)
		right = random.randint(0, len(neighbour_state) - 1)
		if left > right:
			left, right = right, left
		neighbour_state[left: right + 1] = reversed(neighbour_state[left: right + 1])
		return neighbour_state

	def actions(self, state):
		return [self.two_opt]

	def result(self, state, action):
		return action(state)

	def path_cost(self, c, state1, action, state2):
		cost = 0
		for i in range(len(state2) - 1):
			cost += distances[state2[i]][state2[i + 1]]
		cost += distances[state2[0]][state2[-1]]
		return cost

	def value(self. state):
		return -1 * self.path_cost(None, None, None, state)

class TSPGui():

	def __init__(self, root, all_cities):
		self.root = root
		self.vars = []
		self.frame_locations = {}
		self.calculate_canvas_size()
		self.button_text = StringVar()
		self.button_text.set('Start')
		self.all_cities = all_cities
		self.frame_select_cities = Frame(self.root)
		self.frame_select_cities.grid(row=1)
		self.frame_canvas = Frame(self.root)
		self.frame_canvas.grid(row=2)
		Label(self.root, text='Map of Romania', font='Times 13 bold').grid(row=0, columnspan=10)

	def create_checkboxes(self, side=LEFT, anchor=W):
		row_number = 0
		column_number = 0

		for city in self.all_cities:
			var = IntVar()
			var.set(1)
			Checkbutton(self.frame_select_cities, text=city, variable=var).grid(row=row_number, column=column_number, sticky=W)

			self.vars.append(var)
			column_number += 1
			if column_number == 10:
				column_number = 0
				row_number += 1

	def create_buttons(self):
		Button(self.frame_select_cities, textvariable=self.button_text,
			   command=self.run_traveling_salesman).grid(row=3, column=4, sticky=E + W)
		Button(self.frame_select_cities, text='Quit', command=self.root.destroy).grid(row=3, column=5, sticky=E + W)

	def run_traveling_salesman(self):

		cities = []
		for i in range(len(self.vars)):
			if self.vars[i].get() == 1:
				cities.append(self.all_cities[i])

		tsp_problem = TSP_problem(cities)
		self.button_text.set('Reset')
		self.create_canvas(tsp_problem)