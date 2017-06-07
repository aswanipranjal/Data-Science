import matplotlib.pyplot as plt

x = [2, 4, 6, 8, 10]
y = [6, 7, 8, 2, 4]

x1 = [1, 3, 5, 7, 9]
y1 = [7, 8, 2, 4, 2]

# by default, matplotlib separates colors for different graphs
plt.bar(x, y, label='Bars1')
plt.bar(x1, y1, label='Bars2')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interesting graph')
plt.show()