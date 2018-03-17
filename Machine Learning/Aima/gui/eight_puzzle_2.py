from tkinter import *
from tkinter import ttk
from functools import partial

import numpy as np

root = Tk()

state = np.array([1, 2,  3, 4, 5, 6, 7, 8, 0])
grid = state.reshape((3, 3))
zero = list(state).index(0)
print(zero)

# def exchange()

button00 = ttk.Button(root, text=f'{grid[0][0]}' if grid[0][0] != 0 else None, width=30, command=lambda: button00.grid_forget())
button00.grid(row=0, column=0, ipady=80)
button01 = ttk.Button(root, text=f'{grid[0][1]}' if grid[0][1] != 0 else None, width=30, command=lambda: button01.grid_forget())
button01.grid(row=0, column=1, ipady=80)
button02 = ttk.Button(root, text=f'{grid[0][2]}' if grid[0][2] != 0 else None, width=30, command=lambda: button02.grid_forget())
button02.grid(row=0, column=2, ipady=80)
button10 = ttk.Button(root, text=f'{grid[1][0]}' if grid[1][0] != 0 else None, width=30, command=lambda: button10.grid_forget())
button10.grid(row=1, column=0, ipady=80)
button11 = ttk.Button(root, text=f'{grid[1][1]}' if grid[1][1] != 0 else None, width=30, command=lambda: button11.grid_forget())
button11.grid(row=1, column=1, ipady=80)
button12 = ttk.Button(root, text=f'{grid[1][2]}' if grid[1][2] != 0 else None, width=30, command=lambda: button12.grid_forget())
button12.grid(row=1, column=2, ipady=80)
button20 = ttk.Button(root, text=f'{grid[2][0]}' if grid[2][0] != 0 else None, width=30, command=lambda: button20.grid_forget())
button20.grid(row=2, column=0, ipady=80)
button21 = ttk.Button(root, text=f'{grid[2][1]}' if grid[2][1] != 0 else None, width=30, command=lambda: button21.grid_forget())
button21.grid(row=2, column=1, ipady=80)
button22 = ttk.Button(root, text=f'{grid[2][2]}' if grid[2][2] != 0 else None, width=30, command=lambda: button22.grid_forget())
button22.grid(row=2, column=2, ipady=80)
root.mainloop()