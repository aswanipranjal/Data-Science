from tkinter import *
from functools import partial

import numpy as np

import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from search import astar_search, EightPuzzle
import utils

root = Tk()

state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
puzzle = EightPuzzle(tuple(state))

b = [None]*9

def exchange(index):
	# state = list(state)
	print('Index: ', index)
	print('Puzzle State: ', state)
	zero_ix = list(state).index(0)
	print('Zero: ', zero_ix)
	actions = puzzle.actions(state)
	current_action = ''
	state_i, state_j = index//3, index%3
	zero_i, zero_j = zero_ix//3, zero_ix%3
	i_diff = state_i - zero_i
	j_diff = state_j - zero_j
	print('i_diff: ', i_diff)
	print('j_diff: ', j_diff)
	if i_diff > 0:
		current_action += 'DOWN'
	elif i_diff < 0:
		current_action += 'UP'
	
	if j_diff > 0:
		current_action += 'RIGHT'
	elif j_diff < 0:
		current_action += 'LEFT'

	print('current_action: ', current_action)
	print('actions: ', actions)
	if current_action in actions:
	# b[zero_ix] = b[index]
		b[zero_ix].grid_forget()
		b[zero_ix] = Button(root, text=f'{state[index]}', width=6, font=('Helvetica', 40, 'bold'), command=partial(exchange, zero_ix))
		b[zero_ix].grid(row=zero_ix//3, column=zero_ix%3, ipady=40)
		b[index].grid_forget()
		b[index] = Button(root, text=None, width=6, font=('Helvetica', 40, 'bold'), command=partial(exchange, index))
		b[index].grid(row=index//3, column=index%3, ipady=40)
		state[zero_ix], state[index] = state[index], state[zero_ix]
		# state = tuple(state)
		print('New state: ', state, '\n')


b[0] = Button(root, text=f'{state[0]}' if state[0] != 0 else None, width=6, font=('Helvetica', 40, 'bold'), command=partial(exchange, 0))
b[0].grid(row=0, column=0, ipady=40)
b[1] = Button(root, text=f'{state[1]}' if state[1] != 0 else None, width=6, font=('Helvetica', 40, 'bold'), command=partial(exchange, 1))
b[1].grid(row=0, column=1, ipady=40)
b[2] = Button(root, text=f'{state[2]}' if state[2] != 0 else None, width=6, font=('Helvetica', 40, 'bold'), command=partial(exchange, 2))
b[2].grid(row=0, column=2, ipady=40)
b[3] = Button(root, text=f'{state[3]}' if state[3] != 0 else None, width=6, font=('Helvetica', 40, 'bold'), command=partial(exchange, 3))
b[3].grid(row=1, column=0, ipady=40)
b[4] = Button(root, text=f'{state[4]}' if state[4] != 0 else None, width=6, font=('Helvetica', 40, 'bold'), command=partial(exchange, 4))
b[4].grid(row=1, column=1, ipady=40)
b[5] = Button(root, text=f'{state[5]}' if state[5] != 0 else None, width=6, font=('Helvetica', 40, 'bold'), command=partial(exchange, 5))
b[5].grid(row=1, column=2, ipady=40)
b[6] = Button(root, text=f'{state[6]}' if state[6] != 0 else None, width=6, font=('Helvetica', 40, 'bold'), command=partial(exchange, 6))
b[6].grid(row=2, column=0, ipady=40)
b[7] = Button(root, text=f'{state[7]}' if state[7] != 0 else None, width=6, font=('Helvetica', 40, 'bold'), command=partial(exchange, 7))
b[7].grid(row=2, column=1, ipady=40)
b[8] = Button(root, text=f'{state[8]}' if state[8] != 0 else None, width=6, font=('Helvetica', 40, 'bold'), command=partial(exchange, 8))
b[8].grid(row=2, column=2, ipady=40)
root.mainloop()