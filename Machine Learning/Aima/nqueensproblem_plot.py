import matplotlib.pyplot as plt
import numpy as np

def plot_NQP(node):
	n = len(node.state)
	board = np.zeros((n, n))
	solution = list(node.state)
	for i in range(n):
		board[i][solution[i]] = True

	fig = plt.figure(figsize=(10, 10))
	ax = fig.add_subplot(111)
	ax.set_title(f'{n} Queens')
	plt.imshow(board, cmap='Oranges', interpolation='nearest')
	ax.set_aspect('equal')
	fig.tight_layout()
	plt.show()
	plt.show()
