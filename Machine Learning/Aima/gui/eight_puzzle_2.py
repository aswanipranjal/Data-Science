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

def exchange(index):
	zero_ix = list(state).index(0)
	b[zero_ix] = b[index]
	b[index].grid_forget()


b[0] = ttk.Button(root, text=f'{state[0]}' if state[0] != 0 else None, width=30, command=partial(exchange, 0))
b[0].grid(row=0, column=0, ipady=80)
b[1] = ttk.Button(root, text=f'{state[1]}' if state[1] != 0 else None, width=30, command=partial(exchange, 1))
b[1].grid(row=0, column=1, ipady=80)
b[2] = ttk.Button(root, text=f'{state[2]}' if state[2] != 0 else None, width=30, command=partial(exchange, 2))
b[2].grid(row=0, column=2, ipady=80)
b[3] = ttk.Button(root, text=f'{state[3]}' if state[3] != 0 else None, width=30, command=partial(exchange, 3))
b[3].grid(row=1, column=0, ipady=80)
b[4] = ttk.Button(root, text=f'{state[4]}' if state[4] != 0 else None, width=30, command=partial(exchange, 4))
b[4].grid(row=1, column=1, ipady=80)
b[5] = ttk.Button(root, text=f'{state[5]}' if state[5] != 0 else None, width=30, command=partial(exchange, 5))
b[5].grid(row=1, column=2, ipady=80)
b[6] = ttk.Button(root, text=f'{state[6]}' if state[6] != 0 else None, width=30, command=partial(exchange, 6))
b[6].grid(row=2, column=0, ipady=80)
b[7] = ttk.Button(root, text=f'{state[7]}' if state[7] != 0 else None, width=30, command=partial(exchange, 7))
b[7].grid(row=2, column=1, ipady=80)
b[8] = ttk.Button(root, text=f'{state[8]}' if state[8] != 0 else None, width=30, command=partial(exchange, 8))
b[8].grid(row=2, column=2, ipady=80)
root.mainloop()