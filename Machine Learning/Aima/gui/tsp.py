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

	def create_checkboxes():
