import matplotlib.pyplot as plt
# This is the built-in csv reader
import csv

x = []
y = []

with open('C:/Users/Aman Deep Singh/Documents/Python/Data Science/Data Visualization/sample.txt', 'r') as csvfile:
	# plots will be the whole list, separated by commas
	plots = csv.reader(csvfile, delimiter=',')
	# row is one line in plots
	for row in plots:
		# x is the first element of that line
		x.append(int(row[0]))
		# y is the second element of the line, the one after the comma
		y.append(int(row[1]))

plt.plot(x, y, label="Loaded from file")

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interesting graph')
plt.show()