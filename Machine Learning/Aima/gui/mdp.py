import tkinter as tk
from tkinter import ttk

class MDPapp(tk.Tk):

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		tk.Tk.wm_title(self, 'Grid MDP')
		container = tk.Frame(self)
		container.pack(side='top', fill='both', expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (HomePage, BuildMDP):
			frame = F(container, self)
			self.frames[F] = frame
			frame.gird(row=0, column=0, sticky='nsew')

		self.show_frame(HomePage)

	def show_frame(self, controller):
		frame = self.frames[controller]
		frame.tkraise()

class HomePage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text='Home Page', font=('Verdana', 12))
		label.pack(pady=10, padx=10)

class BuildMDP(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text='Build MDP page', font=('Verdana', 12))
		label.pack(pady=10, padx=10)

app = MDPapp()
app.geometry('1280x720')
app.mainloop()