from tkinter import *
from functools import partial

import numpy as np

root = Tk()

state = np.array([1, 2,  3, 4, 5, 6, 7, 8, 0])
grid = state.reshape((3, 3))

button00 = Button(root, text=f'{grid[0][0]}', command=lambda: button00.grid_forget())
button00.grid(row=0, column=0)
button01 = Button(root, text=f'{grid[0][1]}', command=lambda: button01.grid_forget())
button01.grid(row=0, column=1)
button02 = Button(root, text=f'{grid[0][2]}', command=lambda: button02.grid_forget())
button02.grid(row=0, column=2)
button10 = Button(root, text=f'{grid[1][0]}', command=lambda: button10.grid_forget())
button10.grid(row=1, column=0)
button11 = Button(root, text=f'{grid[1][1]}', command=lambda: button11.grid_forget())
button11.grid(row=1, column=1)
button12 = Button(root, text=f'{grid[1][2]}', command=lambda: button12.grid_forget())
button12.grid(row=1, column=2)
button20 = Button(root, text=f'{grid[2][0]}', command=lambda: button20.grid_forget())
button20.grid(row=2, column=0)
button21 = Button(root, text=f'{grid[2][1]}', command=lambda: button21.grid_forget())
button21.grid(row=2, column=1)
button22 = Button(root, text=f'{grid[2][2]}', command=lambda: button22.grid_forget())
button22.grid(row=2, column=2)
root.mainloop()