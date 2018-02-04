import tkinter as tk
from tkinter import ttk

class MDPapp(tk.Tk):

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		tk.Tk.wm_title(self, 'Grid MDP')