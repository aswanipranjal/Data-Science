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

	