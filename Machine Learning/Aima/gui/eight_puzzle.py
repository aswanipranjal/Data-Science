# author: ad71
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk

import numpy as np
from functools import partial

import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from search import astar_search, EightPuzzle
import utils

grayef = '#efefef'


class EightPuzzleApp(tk.Tk):

	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)
		tk.Tk.wm_title(self, 'Eight Puzzle')
		self.shared_data = {
			'n': tk.IntVar()
		}
		self.shared_data['n'].set(3)
		self.container = tk.Frame(self)
		self.container.pack(side='top', fill='both', expand=True)
		self.container.grid_rowconfigure(0, weight=1)
		self.container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (HomePage, EightPuzzlePage):
			frame = F(self.container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky='nsew')

		self.show_frame(HomePage)

	def get_page(self, page_class):
		""" Returns pages from stored frames """

		return self.frames[page_class]

	def placeholder_function(self):
		""" Placeholder function """

		print('Not supported yet!')

	def exit(self):
		""" Function to exit """

		if tkinter.messagebox.askokcancel('Exit?', 'All changes will be lost'):
			quit()

	def show_frame(self, controller):
		""" Function to change frames """

		build_page = self.get_page(EightPuzzlePage)
		build_page.create_buttons()
		frame = self.frames[controller]
		frame.tkraise()


class HomePage(tk.Frame):

	def __init__(self, parent, controller):
		""" HomePage constructor """

		tk.Frame.__init__(self, parent)
		self.controller = controller
		frame1 = tk.Frame(self)
		frame1.pack(side=tk.TOP)

		label = ttk.Label(frame1, text='Eight Puzzle', font=('Helvetica', 18, 'bold'), background=grayef)
		label.pack(pady=75, padx=50, side=tk.TOP)

		button = ttk.Button(self, text='Generate', command=lambda: controller.show_frame(EightPuzzlePage))
		button.pack(pady=10, padx=10, side=tk.TOP, ipadx=20, ipady=10)


class EightPuzzlePage(tk.Frame):

	def __init__(self, parent, controller):
		""" EightPuzzle constructor """

		tk.Frame.__init__(self, parent)
		self.grid_rowconfigure(0, weight=1)
		self.grid_columnconfigure(0, weight=1)
		self.frame = tk.Frame(self)
		self.frame.pack()
		self.controller = controller

	def create_buttons(self):
		""" Creates interactive cells to build EightPuzzle """

		_n = self.controller.shared_data['n'].get()
		self.goal = np.array([1, 2, 3, 4, 5, 6, 7, 8, 0])
		self.buttons = [[None] * _n] * _n
		self.grid = self.goal.reshape((3, 3))

		for i in range(_n):
			for j  in range(_n):
				# if self.grid[i][j] != 0:
				button = ttk.Button(self.frame, text=f'{self.grid[i][j]}', width=30, command=lambda: button.grid_forget())
				button.grid(row=i, column=j, ipady=80)
				# else:
					# self.zero = (i, j)

	def move(self, i, j):
		print('In move')
		self.buttons[i][j].grid_remove()
		# self.buttons[i][j].grid(row=100, column=100, ipady=80)

	def placeholder_function(self):
		""" Placeholder function """

		print('Not supported yet!')


if __name__ == '__main__':
	app = EightPuzzleApp()
	app.geometry('600x570')
	app.mainloop()
