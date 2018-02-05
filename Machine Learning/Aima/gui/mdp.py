import tkinter as tk
from tkinter import ttk

height = 0
width = 0

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
			frame.grid(row=0, column=0, sticky='nsew')

		self.show_frame(HomePage)

	def show_frame(self, controller, _height=None, _width=None):
		if _height and _width:
			global height
			global width
			height = _height
			width = _width
			BuildMDP.create_buttons(self)
		frame = self.frames[controller]
		frame.tkraise()

class HomePage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		frame1 = tk.Frame(self)
		frame1.pack(side=tk.TOP)
		frame2 = tk.Frame(self)
		frame2.pack(side=tk.TOP)
		label = ttk.Label(frame1, text='Home Page', font=('Verdana', 12))
		label.pack(pady=10, padx=10, side=tk.TOP)
		label = ttk.Label(frame1, text='Dimensions', font=('Verdana', 10))
		label.pack(pady=10, padx=10, side=tk.TOP)
		entry_h = tk.Entry(frame2, font=('Verdana', 10), width=3, justify=tk.CENTER)
		entry_h.pack(pady=10, padx=10, side=tk.LEFT)
		label_x = ttk.Label(frame2, text='X', font=('Verdana', 10))
		label_x.pack(pady=10, padx=4, side=tk.LEFT)
		entry_w = tk.Entry(frame2, font=('Verdana', 10), width=3, justify=tk.CENTER)
		entry_w.pack(pady=10, padx=10, side=tk.LEFT)
		button = ttk.Button(self, text='Build a GridMDP', command=lambda: controller.show_frame(BuildMDP, entry_h.get(), entry_w.get()))
		button.pack(pady=10, padx=10, side=tk.TOP)

class BuildMDP(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text='Build MDP page', font=('Verdana', 12))
		label.pack(pady=10, padx=10)

	def create_buttons(self):
		print('In create_buttons function')
		for i in range(int(height)):
			for j in range(int(width)):
				tk.Button(self, text='Hi', justify=tk.CENTER).pack()

app = MDPapp()
app.geometry('1280x720')
app.mainloop()