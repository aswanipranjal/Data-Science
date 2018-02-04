import tkinter as tk
from tkinter import ttk

height = None
width = None

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
		if _height:
			global height
			height = _height
		if _width:
			global width
			width = _width
		frame = self.frames[controller]
		frame.tkraise()

class HomePage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		global height
		global width
		frame1 = tk.Frame(self)
		frame1.pack(side=tk.TOP)
		frame2 = tk.Frame(self)
		frame2.pack(side=tk.TOP)
		label = ttk.Label(frame1, text='Home Page', font=('Verdana', 12))
		label.pack(pady=10, padx=10, side=tk.TOP)
		label = ttk.Label(frame1, text='Dimensions', font=('Verdana', 10))
		label.pack(pady=10, padx=10, side=tk.TOP)
		# height = tk.IntVar()
		entry_h = tk.Entry(frame2, font=('Verdana', 10), width=3, justify=tk.CENTER)
		entry_h.pack(pady=10, padx=10, side=tk.LEFT)
		label_x = ttk.Label(frame2, text='X', font=('Verdana', 10))
		label_x.pack(pady=10, padx=4, side=tk.LEFT)
		# width = tk.IntVar()
		entry_w = tk.Entry(frame2, font=('Verdana', 10), width=3, justify=tk.CENTER)
		entry_w.pack(pady=10, padx=10, side=tk.LEFT)
		button = ttk.Button(self, text='Build a GridMDP', command=lambda: controller.show_frame(BuildMDP))
		button.pack(pady=10, padx=10, side=tk.TOP)

class BuildMDP(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text='Build MDP page', font=('Verdana', 12))
		label.pack(pady=10, padx=10)
		self.create_buttons()

	def create_buttons(self):
		print('In create_buttons function')
		for i in range(height.get()):
			for j in range(width.get()):
				print('Hi')

app = MDPapp()
app.geometry('1280x720')
app.mainloop()