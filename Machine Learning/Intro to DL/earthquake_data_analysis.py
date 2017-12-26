from datetime import datetime
import numpy as np
import copy

class Dataset:
	@staticmethod
	def load_from_file(filename):
		'''
		Load and return data from file
		:param filename: path of the database.csv file
		:return: (date, latitude, longitude, magnitude) (np.array)
		'''
		date, latitude, longitude, magnitude = [], [], [], []

		with open(filename, "r") as f:
			f.readline() # skip first line

			for line in f:
				elements = line.split(',')
				try:
					date.append(datetime.strptime(f"{elements[0]} {elements[1]}", "%m/%d/%Y %H:%M:%S"))
					latitude.append(float(elements[2]))
					longitude.append(float(elements[3]))
					magnitude.append(elements[8])
				except ValueError:
					pass

		return np.array(date), np.float32(latitude), np.float32(longitude), np.float32(magnitude)

	@staticmethod
	def normalize_date(array):
		'''
		Normalize datetime array
		:param array: array to normalize
		:return: normalized array (np.array)
		'''
		min_data = min(array)
		max_data = max(array)
		delta = max_data - min_data
		return np.float32([(d - min_data).total_seconds() / delta.total_seconds() for d in  array])

	@staticmethod
	def normalize_cord(latitude, longitude):
		'''
		Normalize GPS cord array, assuming the earth is spherical
		:param latitude: latitude array to normalize
		:param longitude: longitude array to normalize
		:return: normalized arrays (np.array)
		'''
		rad_lat = np.deg2rad(latitude)
		rad_lon = np.deg2rad(longitude)

		x = np.cos(rad_lat) * np.cos(rad_lon)
		y = np.cos(rad_lat) * np.sin(rad_lon)
		z = np.sin(rad_lat)

		return x, y, z

	@staticmethod
	def vectorize(date, latitude, longitude):
		'''
		Transform given array in vectors to feed NN
		:param date: date array
		:param latitude: latitude array
		:param longitude: longitude array
		:return: np.array
		'''
		return np.concatenate(Dataset.normalize_cord(latitude, longitude) + (Dataset.normalize_date(date),)).reshape((4, len(date))).swapaxes(0, 1)

class Math:
	@staticmethod
	def sigmoid(x, deriv=False):
		'''
		Sigmoid function
		:param x: np.array
		:param deriv: derivate wanted ?
		:return:
		'''
		if deriv:
			return x * (1 - x)

		return 1 / (1 + np.exp(-x))

	@staticmethod
	def relu(x, deriv=False):
		'''
		Rectifier function
		:param x: np.array
		:param deriv: derivate wanted ?
		:return:
		'''
		if deriv:
			return np.ones_like(x) * (x > 0)

		return x * (x > 0)

	@staticmethod
	def new_parameters(x, x_min, x_max, radius):
		'''
		Generate new random parameters in the sphere of center and radius given
		:param x: center on the sphere
		:param x_min: minimum value returned
		:param x_max: maximum value returned
		:param radius: radius
		:return: new parameter
		'''
		alpha = 2 * np.random.random() - 1
		new_x = x + radius * alpha

		if new_x < x_min:
			return x_min

		elif new_x > x_max:
			return x_max

		return new_x

