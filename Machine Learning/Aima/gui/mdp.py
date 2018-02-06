import tkinter as tk
from tkinter import ttk
from functools import partial

def popupmsg(msg, i, j, gridmdp):
	popup = tk.Toplevel()
	popup.wm_title(f'{i}, {j}')
	container = tk.Frame(popup)
	container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
	container.grid_rowconfigure(0, weight=1)
	container.grid_columnconfigure(0, weight=1)

	def partial_function():
		print(f'IntVar: {wall.get()}')
		gridmdp[i][j] = wall.get()
		print(gridmdp)
		popup.destroy

	label = ttk.Label(container, text=msg, font=('Helvetica', 12), anchor=tk.CENTER)
	label.grid(row=0, column=0, sticky='new', pady=5, padx=5)
	wall = tk.IntVar()
	wall.set(gridmdp[i][j])
	print(f'IntVar: {wall.get()}')
	rb = ttk.Radiobutton(container, text='Create Wall', variable=wall, value='None')
	rb.grid(row=1, column=0, columnspan=4, sticky='nsew', padx=156, pady=5)
	b1 = ttk.Button(container, text='Ok', command=partial_function)
	b1.grid(row=2, column=0, sticky='nsew', pady=5, padx=5)
	popup.geometry('400x300')
	popup.mainloop()

def placeholder_function():
	print('Not supported yet!')

class MDPapp(tk.Tk):

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		tk.Tk.wm_title(self, 'Grid MDP')
		self.shared_data = {
			'height': tk.IntVar(),
			'width': tk.IntVar()
		}
		container = tk.Frame(self)
		container.pack(side='top', fill='both', expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.menu_bar = tk.Menu(container)
		self.edit_menu = tk.Menu(self.menu_bar, tearoff=1)
		self.edit_menu.add_command(label='Reset', command=placeholder_function, state=tk.DISABLED)
		self.edit_menu.add_command(label='Initialize', command=placeholder_function)
		self.edit_menu.add_separator()
		self.edit_menu.add_command(label='Exit', command=placeholder_function)
		self.menu_bar.add_cascade(label='Edit', menu=self.edit_menu)
		tk.Tk.config(self, menu=self.menu_bar)

		self.frames = {}

		for F in (HomePage, BuildMDP):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky='nsew')

		self.show_frame(HomePage)

	def get_page(self, page_class):
		return self.frames[page_class]

	def show_frame(self, controller, cb=False):
		if cb:
			build_page = self.get_page(BuildMDP)
			build_page.create_buttons()
		frame = self.frames[controller]
		frame.tkraise()

class HomePage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		frame1 = tk.Frame(self)
		frame1.pack(side=tk.TOP)
		frame2 = tk.Frame(self)
		frame2.pack(side=tk.TOP)
		label = ttk.Label(frame1, text='Home Page', font=('Verdana', 12))
		label.pack(pady=10, padx=10, side=tk.TOP)
		label = ttk.Label(frame1, text='Dimensions', font=('Verdana', 10))
		label.pack(pady=10, padx=10, side=tk.TOP)
		entry_h = tk.Entry(frame2, textvariable=self.controller.shared_data['height'], font=('Verdana', 10), width=3, justify=tk.CENTER)
		entry_h.pack(pady=10, padx=10, side=tk.LEFT)
		label_x = ttk.Label(frame2, text='X', font=('Verdana', 10))
		label_x.pack(pady=10, padx=4, side=tk.LEFT)
		entry_w = tk.Entry(frame2, textvariable=self.controller.shared_data['width'], font=('Verdana', 10), width=3, justify=tk.CENTER)
		entry_w.pack(pady=10, padx=10, side=tk.LEFT)
		button = ttk.Button(self, text='Build a GridMDP', command=lambda: controller.show_frame(BuildMDP, cb=True))
		button.pack(pady=10, padx=10, side=tk.TOP)

class BuildMDP(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.grid_rowconfigure(0, weight=1)
		self.grid_columnconfigure(0, weight=1)
		self.frame = tk.Frame(self)
		self.frame.pack()
		self.controller = controller

	def create_buttons(self):
		_height = self.controller.shared_data['height'].get()
		_width = self.controller.shared_data['width'].get()
		gridmdp = [[0]*max(1, _width) for _ in range(max(1, _height))]
		for i in range(max(1, _height)):
			for j in range(max(1, _width)):
				ttk.Button(self.frame, text=f'{i}, {j}', width=int(196/max(1, _width)), command=partial(popupmsg, 'Hello bitch!', i, j, gridmdp)).grid(row=i, column=j, ipady=int(336/max(1, _height)) - 12)

app = MDPapp()
app.geometry('1280x720')
app.mainloop()