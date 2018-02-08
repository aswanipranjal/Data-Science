import tkinter as tk
from tkinter import ttk
from functools import partial

# TODO: flip terminals horizontally before solving

WALL_VALUE = -99999.0
TERM_VALUE = -999999.0

def initialize_dialogbox(_width, _height, gridmdp, terminals, buttons):

	dialog = tk.Toplevel()
	dialog.wm_title('Initialize')
	container = tk.Frame(dialog)
	container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
	container.grid_rowconfigure(0, weight=1)
	container.grid_columnconfigure(0, weight=1)
	# Todo: Fix initialization
	wall = tk.IntVar()
	wall.set(0)
	term = tk.IntVar()
	term.set(0)
	reward = tk.DoubleVar()
	reward.set(0.0)
	label = ttk.Label(container, text='Initialize', font=('Helvetica', 12), anchor=tk.N)
	label.grid(row=0, column=0, columnspan=3, sticky='new', pady=15, padx=5)
	label_reward = ttk.Label(container, text='Reward', font=('Helvetica', 10), anchor=tk.N)
	label_reward.grid(row=1, column=0, columnspan=3, sticky='new', pady=1, padx=5)
	entry_reward = ttk.Entry(container, font=('Helvetica', 10), justify=tk.CENTER, exportselection=0, textvariable=reward)
	entry_reward.grid(row=2, column=0, columnspan=3, sticky='new', pady=5, padx=50)
	rbtn_term = ttk.Radiobutton(container, text='Terminal', variable=term, value=TERM_VALUE)
	rbtn_term.grid(row=3, column=0, columnspan=3, sticky='nsew', padx=160, pady=5)
	rbtn_wall = ttk.Radiobutton(container, text='Wall', variable=wall, value=WALL_VALUE)
	rbtn_wall.grid(row=4, column=0, columnspan=3, sticky='nsew', padx=172, pady=5)
	initialize_widget_disability_checks(_width, _height, gridmdp, terminals, label_reward, entry_reward, rbtn_wall, rbtn_term)
	btn_apply = ttk.Button(container, text='Apply', command=partial(initialize_update_table, _width, _height, gridmdp, terminals, buttons, reward, term, wall, label_reward, entry_reward, rbtn_term, rbtn_wall))
	btn_apply.grid(row=5, column=0, sticky='nsew', pady=5, padx=5)
	btn_reset = ttk.Button(container, text='Reset', command=partial(initialize_reset_all, _width, _height, gridmdp, terminals, buttons, label_reward, entry_reward, rbtn_wall, rbtn_term))
	btn_reset.grid(row=5, column=1, sticky='nsew', pady=5, padx=5)
	btn_ok = ttk.Button(container, text='Ok', command=dialog.destroy)
	btn_ok.grid(row=5, column=2, sticky='nsew', pady=5, padx=5)
	dialog.geometry('400x200')
	dialog.mainloop()

def update_table(i, j, gridmdp, terminals, buttons, reward, term, wall, label_reward, entry_reward, rbtn_term, rbtn_wall):

	if wall.get() == WALL_VALUE:
		buttons[i][j].configure(style='wall.TButton')
		buttons[i][j].config(text='Wall')
		label_reward.config(foreground='#999')
		entry_reward.config(state=tk.DISABLED)
		rbtn_term.state(['!focus', '!selected'])
		rbtn_term.config(state=tk.DISABLED)
		gridmdp[i][j] = WALL_VALUE
	elif wall.get() != WALL_VALUE:
		if reward.get() != 0.0:
			gridmdp[i][j] = reward.get()
			buttons[i][j].configure(style='reward.TButton')
			buttons[i][j].config(text=f'R = {reward.get()}')
		if term.get() == TERM_VALUE:
			if (i, j) not in terminals:
				terminals.append((i, j))
			rbtn_wall.state(['!focus', '!selected'])
			rbtn_wall.config(state=tk.DISABLED)
			if gridmdp[i][j] < 0:
				buttons[i][j].configure(style='-term.TButton')
			elif gridmdp[i][j] > 0:
				buttons[i][j].configure(style='+term.TButton')
			elif gridmdp[i][j] == 0.0:
				buttons[i][j].configure(style='=term.TButton')

def initialize_update_table(_width, _height, gridmdp, terminals, buttons, reward, term, wall, label_reward, entry_reward, rbtn_term, rbtn_wall):

	for i in range(max(1, _height)):
		for j in range(max(1, _width)):
			update_table(i, j, gridmdp, terminals, buttons, reward, term, wall, label_reward, entry_reward, rbtn_term, rbtn_wall)

def reset_all(i, j, gridmdp, terminals, buttons, label_reward, entry_reward, rbtn_wall, rbtn_term):

	gridmdp[i][j] = 0.0
	buttons[i][j].configure(style='TButton')
	buttons[i][j].config(text=f'({i}, {j})')
	if (i, j) in terminals:
		terminals.remove((i, j))
	label_reward.config(foreground='#000')
	entry_reward.config(state=tk.NORMAL)
	rbtn_term.config(state=tk.NORMAL)
	rbtn_wall.config(state=tk.NORMAL)
	rbtn_wall.state(['!focus', '!selected'])
	rbtn_term.state(['!focus', '!selected'])

def initialize_reset_all(_width, _height, gridmdp, terminals, buttons, label_reward, entry_reward, rbtn_wall, rbtn_term):

	for i in range(max(1, _height)):
		for j in range(max(1, _width)):
			reset_all(i, j, gridmdp, terminals, buttons, label_reward, entry_reward, rbtn_wall, rbtn_term)

def widget_disability_checks(i, j, gridmdp, terminals, label_reward, entry_reward, rbtn_wall, rbtn_term):

	if gridmdp[i][j] == WALL_VALUE:
		label_reward.config(foreground='#999')
		entry_reward.config(state=tk.DISABLED)
		rbtn_term.config(state=tk.DISABLED)
		rbtn_wall.state(['!focus', 'selected'])
		rbtn_term.state(['!focus', '!selected'])

	if (i, j) in terminals:
		rbtn_wall.config(state=tk.DISABLED)
		rbtn_wall.state(['!focus', '!selected'])\

def initialize_widget_disability_checks(_width, _height, gridmdp, terminals, label_reward, entry_reward, rbtn_wall, rbtn_term):
	
	bool_walls = [[False]*max(1, _width) for _ in range(max(1, _height))]
	bool_terms = [[False]*max(1, _width) for _ in range(max(1, _height))]
	for i in range(1, _height):
		for j in range(1, _width):
			if gridmdp[i][j] == WALL_VALUE:
				bool_walls[i][j] = True

			if (i, j) in terminals:
				bool_terms[i][j] = True
				
	print(bool_walls)
	print(bool_terms)
	if all(bool_walls):
		print('in if statement')
		label_reward.config(foreground='#999')
		entry_reward.config(state=tk.DISABLED)
		rbtn_term.config(state=tk.DISABLED)
		rbtn_wall.state(['!focus', 'selected'])
		rbtn_term.state(['!focus', '!selected'])

	if all(bool_terms):
		print('in another if statement')
		rbtn_wall.config(state=tk.DISABLED)
		rbtn_wall.state(['!focus', '!selected'])

def dialogbox(i, j, gridmdp, terminals, buttons, _height):

	dialog = tk.Toplevel()
	dialog.wm_title(f'{_height - i - 1}, {j}')
	container = tk.Frame(dialog)
	container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
	container.grid_rowconfigure(0, weight=1)
	container.grid_columnconfigure(0, weight=1)
	wall = tk.IntVar()
	wall.set(gridmdp[i][j])
	term = tk.IntVar()
	term.set(TERM_VALUE if (i, j) in terminals else 0.0)
	reward = tk.DoubleVar()
	reward.set(gridmdp[i][j] if gridmdp[i][j] != WALL_VALUE else 0.0)
	label = ttk.Label(container, text=f'Configure cell {_height - i - 1}, {j}', font=('Helvetica', 12), anchor=tk.N)
	label.grid(row=0, column=0, columnspan=3, sticky='new', pady=15, padx=5)
	label_reward = ttk.Label(container, text='Reward', font=('Helvetica', 10), anchor=tk.N)
	label_reward.grid(row=1, column=0, columnspan=3, sticky='new', pady=1, padx=5)
	entry_reward = ttk.Entry(container, font=('Helvetica', 10), justify=tk.CENTER, exportselection=0, textvariable=reward)
	entry_reward.grid(row=2, column=0, columnspan=3, sticky='new', pady=5, padx=50)
	rbtn_term = ttk.Radiobutton(container, text='Terminal', variable=term, value=TERM_VALUE)
	rbtn_term.grid(row=3, column=0, columnspan=3, sticky='nsew', padx=160, pady=5)
	rbtn_wall = ttk.Radiobutton(container, text='Wall', variable=wall, value=WALL_VALUE)
	rbtn_wall.grid(row=4, column=0, columnspan=3, sticky='nsew', padx=172, pady=5)
	widget_disability_checks(i, j, gridmdp, terminals, label_reward, entry_reward, rbtn_wall, rbtn_term)
	btn_apply = ttk.Button(container, text='Apply', command=partial(update_table, i, j, gridmdp, terminals, buttons, reward, term, wall, label_reward, entry_reward, rbtn_term, rbtn_wall))
	btn_apply.grid(row=5, column=0, sticky='nsew', pady=5, padx=5)
	btn_reset = ttk.Button(container, text='Reset', command=partial(reset_all, i, j, gridmdp, terminals, buttons, label_reward, entry_reward, rbtn_wall, rbtn_term))
	btn_reset.grid(row=5, column=1, sticky='nsew', pady=5, padx=5)
	btn_ok = ttk.Button(container, text='Ok', command=dialog.destroy)
	btn_ok.grid(row=5, column=2, sticky='nsew', pady=5, padx=5)
	dialog.geometry('400x200')
	dialog.mainloop()


class MDPapp(tk.Tk):

	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)
		tk.Tk.wm_title(self, 'Grid MDP')
		self.shared_data = {
			'height': tk.IntVar(),
			'width': tk.IntVar()
		}
		self.shared_data['height'].set(1)
		self.shared_data['width'].set(1)
		container = tk.Frame(self)
		container.pack(side='top', fill='both', expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		self.menu_bar = tk.Menu(container)
		self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
		self.file_menu.add_command(label='Exit', command=self.placeholder_function)
		self.menu_bar.add_cascade(label='File', menu=self.file_menu)

		self.edit_menu = tk.Menu(self.menu_bar, tearoff=1)
		self.edit_menu.add_command(label='Reset', command=self.placeholder_function)
		self.edit_menu.add_command(label='Initialize', command=self.initialize)
		self.edit_menu.add_separator()
		self.edit_menu.add_command(label='View matrix', command=self.view_matrix)
		self.edit_menu.add_command(label='View terminals', command=self.view_terminals)
		self.menu_bar.add_cascade(label='Edit', menu=self.edit_menu)
		self.menu_bar.entryconfig('Edit', state=tk.DISABLED)
		tk.Tk.config(self, menu=self.menu_bar)

		for F in (HomePage, BuildMDP):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky='nsew')

		self.show_frame(HomePage)

	def placeholder_function(self):

		print('Not supported yet!')

	def get_page(self, page_class):

		return self.frames[page_class]

	def view_matrix(self):

		build_page = self.get_page(BuildMDP)
		print('GridMDP', build_page.gridmdp)

	def view_terminals(self):

		build_page = self.get_page(BuildMDP)
		print('Terminals', build_page.terminals)

	def initialize(self):

		build_page = self.get_page(BuildMDP)
		build_page.initialize()

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
		self.controller.menu_bar.entryconfig('Edit', state=tk.NORMAL)
		self.gridmdp = [[0.0]*max(1, _width) for _ in range(max(1, _height))]
		self.terminals = []
		s = ttk.Style()
		s.theme_use('clam')
		s.configure('TButton', background='#ddd', padding=0)
		s.configure('wall.TButton', background='#222', foreground='#fff')
		s.configure('reward.TButton', background='#999')
		s.configure('+term.TButton', background='#008080')
		s.configure('-term.TButton', background='#000040', foreground='#fff')
		s.configure('=term.TButton', background='#004040')
		self.buttons = [[None]*max(1, _width) for _ in range(max(1, _height))]
		for i in range(max(1, _height)):
			for j in range(max(1, _width)):
				self.buttons[i][j] = ttk.Button(self.frame, text=f'({_height - i - 1}, {j})', width=int(196/max(1, _width)), command=partial(dialogbox, i, j, self.gridmdp, self.terminals, self.buttons, _height))
				self.buttons[i][j].grid(row=i, column=j, ipady=int(336/max(1, _height)) - 12)

	def initialize(self):

		_height = self.controller.shared_data['height'].get()
		_width = self.controller.shared_data['width'].get()
		initialize_dialogbox(_width, _height, self.gridmdp, self.terminals, self.buttons)

app = MDPapp()
app.geometry('1280x720')
app.mainloop()