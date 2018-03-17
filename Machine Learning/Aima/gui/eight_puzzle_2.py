from tkinter import *
from tkinter import ttk
from functools import partial

import numpy as np

root = Tk()

state = np.array([1, 2,  3, 4, 5, 6, 7, 8, 0])
grid = state.reshape((3, 3))
# zero = list(state).index(0)
# print(zero)

def exchange(index):
	zero = list(state).index(0)


b1 = ttk.Button(root, text=f'{state[0]}' if state[0] != 0 else None, width=30, command=lambda: b1.grid_forget())
b1.grid(row=0, column=0, ipady=80)
b2 = ttk.Button(root, text=f'{state[1]}' if state[1] != 0 else None, width=30, command=lambda: b2.grid_forget())
b2.grid(row=0, column=1, ipady=80)
b3 = ttk.Button(root, text=f'{state[2]}' if state[2] != 0 else None, width=30, command=lambda: b3.grid_forget())
b3.grid(row=0, column=2, ipady=80)
b4 = ttk.Button(root, text=f'{state[3]}' if state[3] != 0 else None, width=30, command=lambda: b4.grid_forget())
b4.grid(row=1, column=0, ipady=80)
b5 = ttk.Button(root, text=f'{state[4]}' if state[4] != 0 else None, width=30, command=lambda: b5.grid_forget())
b5.grid(row=1, column=1, ipady=80)
b6 = ttk.Button(root, text=f'{state[5]}' if state[5] != 0 else None, width=30, command=lambda: b6.grid_forget())
b6.grid(row=1, column=2, ipady=80)
b7 = ttk.Button(root, text=f'{state[6]}' if state[6] != 0 else None, width=30, command=lambda: b7.grid_forget())
b7.grid(row=2, column=0, ipady=80)
b8 = ttk.Button(root, text=f'{state[7]}' if state[7] != 0 else None, width=30, command=lambda: b8.grid_forget())
b8.grid(row=2, column=1, ipady=80)
b0 = ttk.Button(root, text=f'{state[8]}' if state[8] != 0 else None, width=30, command=lambda: b0.grid_forget())
b0.grid(row=2, column=2, ipady=80)
root.mainloop()