import matplotlib.pyplot as plt

# for bar chart
# x = [2, 4, 6, 8, 10]
# y = [6, 7, 8, 2, 4]

# x1 = [1, 3, 5, 7, 9]
# y1 = [7, 8, 2, 4, 2]

# # by default, matplotlib separates colors for different graphs
# # we can explicitly specify colors as hex, words or letters
# plt.bar(x, y, label='Bars1', color='b')
# plt.bar(x1, y1, label='Bars2', color='c')

# for histogram
population_ages = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102, 110, 120, 121, 122, 130, 111, 115, 112, 80, 75, 65, 54, 44, 43, 42, 48]
# ids = [x for x in range(len(population_ages))]

# plt.bar(ids, population_ages, label="Age")
# we use histograms to show distributions
# for this, we classify the data into subclasses called 'bins', the British ones
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
# rwidth tells what percentage of its assigned width should a bar occupy
plt.hist(population_ages, bins, histtype='bar', rwidth=0.8, label="Age")

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interesting graph')
plt.show()