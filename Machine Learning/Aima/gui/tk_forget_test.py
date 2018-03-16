from tkinter import *

import numpy as np

root = Tk()

state = np.array([1, 2, 3, 4, 5, 6, 7, 8, 0])
grid = state.reshape((3, 3))
for i in range(3):
	for j in range(3):
		b = Button(root, text=f'{grid[i][j]}', command=lambda: b.pack_forget())
		b.grid(row=i, column=j)

root.mainloop()