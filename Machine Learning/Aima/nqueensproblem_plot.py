import matplotlib.pyplot as plt
import numpy as np

def plot_NQP(n, node):
	board = np.zeros((n, n))
	solution = list(node.state)
	for i in range(n):
		board[i][solution[i]] = 1
	plt.imshow(board, cmap='hot', interpolation='nearest')
	plt.show()