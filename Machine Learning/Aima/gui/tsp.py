from tkinter import *
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from search import *
from utils import weighted_sampler
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

	# def two_opt_lesser(self, state):
	# 	neighbour_state = state[:]
	# 	left = random.randint(0, len(neighbour_state) - 2)
	# 	right = random.randint(0, len(neighbour_state) - 1)
	# 	neighbour_state[left: right + 1] = reversed(neighbour_state[left: right + 1])
	# 	return neighbour_state

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

	def value(self, state):
		return -1 * self.path_cost(None, None, None, state)

class TSPGui():

	def __init__(self, root, all_cities):
		self.root = root
		self.vars = []
		self.problem = None
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

		self.problem = TSP_problem(cities)
		self.button_text.set('Reset')
		self.create_canvas()

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

	def create_canvas(self):
		print('Problem', self.problem)
		print('problem.initial', self.problem.initial)
		map_canvas = Canvas(self.frame_canvas, width=self.canvas_width, height=self.canvas_height)
		map_canvas.grid(row=3, columnspan=10)
		current = Node(self.problem.initial)
		print('Current:', current)
		map_canvas.delete('all')
		self.romania_image = PhotoImage(file='../images/romania_map.png')
		map_canvas.create_image(self.canvas_width / 2, self.canvas_height / 2, image=self.romania_image)
		cities = current.state
		print('Cities: ', cities)
		print('frame locations: ', self.frame_locations, end='\n\n\n')
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
		self.temperature = IntVar()
		temperature_scale = Scale(self.frame_canvas, from_=100, to=0, orient=HORIZONTAL, length=200, variable=self.temperature, label='Temperature ----> ', font='Times 11', relief='sunken', showvalue=0, cursor='gumby')
		temperature_scale.grid(row=1, column=5, columnspan=5, sticky='nsew')
		self.simulated_annealing_with_tunable_T(map_canvas)

	def exp_schedule(k=100, lam=0.03, limit=1000):
		return lambda t: (k * math.exp(-lam * t) if t < limit else 0)

	def simulated_annealing_with_tunable_T(self, map_canvas, schedule=exp_schedule()):
		print('In simulated_annealing_with_tunable_T function')
		current = Node(self.problem.initial)
		print('Current:', current)
		print('Current.state:', current.state)
		print('Fitness of current state:', self.fitness_fn(current.state))
		# selection = select(2, current.state, self.fitness_fn)
		selection = self.select_tsp(2, current.state, self.fitness_fn)
		print('Selection:', selection)
		while(1):
			T = schedule(self.temperature.get())
			print('T:', T)
			if T == 0:
				return current.state
			neighbors = current.expand(self.problem)
			print('neighbors:', neighbors, end='\n\n\n')
			if not neighbors:
				return current.state
			next = random.choice(neighbors)
			print('Next:', next)
			print('value(next.state)', self.problem.value(next.state))
			print('value(current.state)', self.problem.value(current.state))
			delta_e = self.problem.value(next.state) - self.problem.value(current.state)
			print('delta_e:', delta_e)
			if delta_e > 0 or probability(math.exp(delta_e / T)):
				map_canvas.delete('poly')
				current = next
				self.cost.set('Cost = ' + str('%0.3f' % (-1 * self.problem.value(current.state))))
				points = []
				for city in current.state:
					points.append(self.frame_locations[city][0])
					points.append(self.frame_locations[city][1])
				map_canvas.create_polygon(points, outline='red', width=3, fill='', tag='poly')
				map_canvas.update()
				map_canvas.after(self.speed.get())

	def fitness_fn(self, state):
		fitness = self.problem.value(state)
		return -10000 / fitness

	def select_tsp(self, r, population, fitness_fn):
		fitnesses = list(map(fitness_fn, population))
		indices = range(len(population))
		print(f'Indices: {indices}')
		print(f'Fitnesses: {fitnesses}')
		sampler = weighted_sampler(indices, fitnesses)
		print(f'Sampler: {sampler}')
		return [population[sampler()] for i in range(r)]

	def mutate():
		pass

	# def genetic_algorithm_stepwise(self, problem, map_canvas):
		# print('In genetic_algorithm_stepwise function')
		# current = Node(problem.initial)
		# while(1):
			# population = [mutate(recombine(*select(2, population, )))]

def main():
	all_cities = []
	for city in romania_map.locations.keys():
		distances[city] = {}
		all_cities.append(city)
	all_cities.sort()

	for name_1, coordinates_1 in romania_map.locations.items():
		for name_2, coordinates_2 in romania_map.locations.items():
			distances[name_1][name_2] = np.linalg.norm([coordinates_1[0] - coordinates_2[0], coordinates_1[1] - coordinates_2[1]])
			distances[name_2][name_1] = np.linalg.norm([coordinates_1[0] - coordinates_2[1], coordinates_1[1] - coordinates_2[1]])


	root = Tk()
	root.title('Traveling Salesman Problem')
	cities_selection_panel = TSPGui(root, all_cities)
	cities_selection_panel.create_checkboxes()
	cities_selection_panel.create_buttons()
	root.mainloop()

if __name__ == '__main__':
	main()