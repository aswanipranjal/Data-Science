import tkinter as tk

class SeaofBTCapp(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self)
		container.pack(side='TOP', fill='BOTH', expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		
		self.frames = {}
		frame = start_page(container, self)
		self.frames[start_page] = frame
		frame.grid(row=0, column=0, sticky='nsew')
		self.show_frame(start_page)

	def show_frame(self, controller):
		frame = self.frames[controller]
		frame.tkraise()