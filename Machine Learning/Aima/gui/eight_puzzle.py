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
		