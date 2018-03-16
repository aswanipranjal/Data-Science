# author: ad71
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk

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
			'n': 8
		}
		self.shared_data['n'].set(8)
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

	def placeholder_function(self):
		""" Placeholder function """

		print('Not supported yet!')

	def exit(self):
		""" Function to exit """

		if tkinter.messagebox.askokcancel('Exit?', 'All changes will be lost'):
			quit()

	def show_frame(self, controller):
		""" Function to change frames """

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