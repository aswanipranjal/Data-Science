from tkinter import *
from tkinter import ttk
from functools import partial

import numpy as np

root = Tk()

state = np.array([1, 2,  3, 4, 5, 6, 7, 8, 0])
grid = state.reshape((3, 3))
b = [None]*9
# zero = list(state).index(0)
# print(zero)

def exchange(index, b_ix, b_zero):
	zero = list(state).index(0)



b[0] = ttk.Button(root, text=f'{state[0]}' if state[0] != 0 else None, width=30, command=lambda: b[0].grid_forget())
b[0].grid(row=0, column=0, ipady=80)
b[1] = ttk.Button(root, text=f'{state[1]}' if state[1] != 0 else None, width=30, command=lambda: b[1].grid_forget())
b[1].grid(row=0, column=1, ipady=80)
b[2] = ttk.Button(root, text=f'{state[2]}' if state[2] != 0 else None, width=30, command=lambda: b[2].grid_forget())
b[2].grid(row=0, column=2, ipady=80)
b[3] = ttk.Button(root, text=f'{state[3]}' if state[3] != 0 else None, width=30, command=lambda: b[3].grid_forget())
b[3].grid(row=1, column=0, ipady=80)
b[4] = ttk.Button(root, text=f'{state[4]}' if state[4] != 0 else None, width=30, command=lambda: b[4].grid_forget())
b[4].grid(row=1, column=1, ipady=80)
b[5] = ttk.Button(root, text=f'{state[5]}' if state[5] != 0 else None, width=30, command=lambda: b[5].grid_forget())
b[5].grid(row=1, column=2, ipady=80)
b[6] = ttk.Button(root, text=f'{state[6]}' if state[6] != 0 else None, width=30, command=lambda: b[6].grid_forget())
b[6].grid(row=2, column=0, ipady=80)
b[7] = ttk.Button(root, text=f'{state[7]}' if state[7] != 0 else None, width=30, command=lambda: b[7].grid_forget())
b[7].grid(row=2, column=1, ipady=80)
b[8] = ttk.Button(root, text=f'{state[8]}' if state[8] != 0 else None, width=30, command=lambda: b[8].grid_forget())
b[8].grid(row=2, column=2, ipady=80)
root.mainloop()