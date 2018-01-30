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

	def calculate_canvas_size(self):
		minx, maxx = sys.maxsize, -1 * sys.maxsize
		miny, maxy = sys.maxsize, -1 * sys.maxsize

		for value in romania_map.locations.values():
			minx = min(minx, value[0])
			maxx = max(maxx, value[0])
			miny = min(miny, value[1])
			maxy = max(maxy, value[1])

		for name, coordinates in romania_map.locations.items():
			self.frame_locations[name] = (coordinates[0] / 1.2 - minx + 150, coordinates[1] / 1.2 - miny + 165)

		canvas_width = maxx	- minx + 200
		canvas_height = maxy - miny + 200

		self.canvas_width = canvas_width
		self.canvas_height = canvas_height

	def create_canvas(self, problem):
		map_canvas = Canvas(self.frame_canvas, width=self.canvas_width, height=self.canvas_height)
		map_canvas.grid(row=3, columnspan=10)
		current = Node(problem.initial)
		map_canvas.delete('all')
		self.romania_image = PhotoImage(file='../images/romania_map.png')
		map_canvas.create_image(self.canvas_width / 2, self.canvas_height / 2, image=self.romania_image)
		cities = current.state

		for city in cities:
			x = self.frame_locations[city][0]
			y = self.frame_locations[city][1]
			map_canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill='red', outline='red')
			map_canvas.create_text(x - 15, y - 10, text=city)
		self.cost = StringVar()
		Label(self.frame_canvas, textvariable=self.cost, relief='sunken').grid(row=2, columnspan=10)
		self.speed = IntVar()
		speed_scale = Scale(self.frame_canvas, from_=500, to=1, orient=HORIZONTAL, variable=self.speed, label='Speed ----> ', showvalue=0, font='Times 11', relief='sunken', cursor='gumby')
		speed_scale.grid(row=1, columnspan=5, sticky='nsew')