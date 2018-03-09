import matplotlib.pyplot as plt
import numpy as np

def plot_NQP(node):
	n = len(node.state)
	board = np.zeros((n, n))
	solution = list(node.state)
	for i in range(n):
		board[i][solution[i]] = 1

	fig = plt.figure(figsize=(6, 3.2))
	ax = fig.add_subplot(111)
	ax.set_title(f'{n} Queens')
	plt.imshow(board, cmap='Oranges', interpolation='nearest')
	ax.set_aspect('equal')
	plt.colorbar(orientation='vertical')
	plt.show()
	plt.show()
