import matplotlib.pyplot as plt
# This is the built-in csv reader
# csv: comma separated values
# import csv

# x = []
# y = []

# with open('C:/Users/Aman Deep Singh/Documents/Python/Data Science/Data Visualization/sample.txt', 'r') as csvfile:
# 	# plots will be the whole list, separated by commas
# 	plots = csv.reader(csvfile, delimiter=',')
# 	# row is one line in plots
# 	for row in plots:
# 		# x is the first element of that line
# 		x.append(int(row[0]))
# 		# y is the second element of the line, the one after the comma
# 		y.append(int(row[1]))

# The conventional (and faster) method
import numpy as np

# loadtxt() works for any file with text in it
# unpack recognizes that there two elements per column and unpacks them to be in two separate variables, lists in this case
x, y = np.loadtxt('C:/Users/Aman Deep Singh/Documents/Python/Data Science/Data Visualization/sample.txt', delimiter=',', unpack=True)

plt.plot(x, y, label="Loaded from file")

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interesting graph')
plt.show()