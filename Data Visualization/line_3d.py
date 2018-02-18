from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()
# We need to matplotlib that we will be using 3d
ax = fig.add_subplot(111, projection='3d')

X, Y, Z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [5, 8, 9, 3, 7, 6, 2, 0, 2, 2], [10, 5, 3, 7, 8, 2, 9, 6, 4, 1]
ax.plot_wireframe(X, Y, Z)
plt.show()