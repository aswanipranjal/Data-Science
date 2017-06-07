import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [5, 2, 4, 8, 3, 9, 5, 0, 3, 11]

plt.scatter(x, y, label='scatter', color='k', marker='^', s=100)

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interesting graph')
plt.show()