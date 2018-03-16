from tkinter import *
from functools import partial

import numpy as np

root = Tk()

state = np.array([1, 2, 3, 4, 5, 6, 7, 8, 0])
grid = state.reshape((3, 3))
buttons = [[None]*3]*3

def remove_button(i, j):
	print(f'i: {i}, j: {j}')
	buttons[i][j].grid_forget()

for i in range(3):
	for j in range(3):
		buttons[i][j] = Button(root, text=f'{grid[i][j]}', command=partial(remove_button, i, j))
		buttons[i][j].grid(row=i, column=j)

root.mainloop()