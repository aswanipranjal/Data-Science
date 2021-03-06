import tkinter as tk
from tkinter import ttk

import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
from matplotlib import pyplot as plt
matplotlib.use('TkAgg')

LARGE_FONT = ('Verdana', 12)
NORMAL_FONT = ('Verdana', 10)
SMALL_FONT = ('Verdana', 8)
style.use('ggplot')

fig = Figure()
sub = fig.add_subplot(111)
# sub.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

exchange = 'BTC-e'
dat_counter = 9000
program_name = 'btce'

def change_exchange(to_what, pn):
	global exchange
	global dat_counter
	global program_name
	exchange = to_what
	program_name = pn
	dat_counter = 9000

def popupmsg(text):
	popup = tk.Tk()
	popup.wm_title('!')
	label = ttk.Label(popup, text=text, font=NORMAL_FONT)
	label.pack(side='top', fill='x', pady=10)
	button1 = ttk.Button(popup, text='OK', command=popup.destroy)
	button1.pack()
	popup.mainloop()

def animate(i):
	pull_data = open('sampledata.txt', 'r').read()
	data_list = pull_data.split('\n')
	x_list = []
	y_list = []
	for each_line in data_list:
		if len(each_line) > 1:
			x, y = each_line.split(',')
			x_list.append(int(x))
			y_list.append(int(y))

	sub.clear()
	sub.plot(x_list, y_list)

class SeaofBTCapp(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		# tk.Tk.iconbitmap(self, default='<your-icon-here>.ico')
		tk.Tk.wm_title(self, 'Sea of BTC client')
		container = tk.Frame(self)
		container.pack(side='top', fill='both', expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		
		menu_bar = tk.Menu(container)
		file_menu = tk.Menu(menu_bar, tearoff=0)
		file_menu.add_command(label='Save settings', command=lambda: popupmsg('Not supported just yet!'))
		file_menu.add_separator()
		file_menu.add_command(label='Exit', command=quit)
		menu_bar.add_cascade(label='File', menu=file_menu)

		exchange_menu = tk.Menu(menu_bar, tearoff=1)
		exchange_menu.add_command(label='BTC-e', command=lambda: change_exchange('BTC-e', 'btce'))
		exchange_menu.add_command(label='Bitfinex', command=lambda: change_exchange('Bitfinex', 'bitfinex'))
		exchange_menu.add_command(label='Bitstamp', command=lambda: change_exchange('Bitstamp', 'bitstamp'))
		exchange_menu.add_command(label='Huobi', command=lambda: change_exchange('Huobi', 'huobi'))
		menu_bar.add_cascade(label='Exchange', menu=exchange_menu)
		
		tk.Tk.config(self, menu=menu_bar)

		self.frames = {}

		for F in (StartPage, PageOne, PageTwo, PageThree):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky='nsew')
		
		self.show_frame(StartPage)

	def show_frame(self, controller):
		frame = self.frames[controller]
		frame.tkraise()

class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text='Start Page', font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = ttk.Button(self, text='Visit Page 1', command=lambda: controller.show_frame(PageOne))
		button1.pack()

		button2 = ttk.Button(self, text='Visit Page 2', command=lambda: controller.show_frame(PageTwo))
		button2.pack()

		button3 = ttk.Button(self, text='Graph Page', command=lambda: controller.show_frame(PageThree))
		button3.pack()

class PageOne(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text='Page One', font=LARGE_FONT)
		label.pack(pady=10, padx=10)
		button1 = ttk.Button(self, text='Back to home', command=lambda: controller.show_frame(StartPage))
		button1.pack()
		button2 = ttk.Button(self, text='Visit Page 2', command=lambda: controller.show_frame(PageTwo))
		button2.pack()

class PageTwo(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text='Page Two', font=LARGE_FONT)
		label.pack(pady=10, padx=10)
		button = ttk.Button(self, text='Back to home', command=lambda: controller.show_frame(StartPage))
		button.pack()

class PageThree(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text='Graph Page', font=LARGE_FONT)
		label.pack(pady=10, padx=10)
		button = ttk.Button(self, text='Back to home', command=lambda: controller.show_frame(StartPage))
		button.pack()

		canvas = FigureCanvasTkAgg(fig, self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

		toolbar = NavigationToolbar2TkAgg(canvas, self)
		toolbar.update()
		# write side=tk.TOP to bring the toolbar to the bottom
		# write side=tk.BOTTOM to bring the toolbar to the top
		canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

app = SeaofBTCapp()
app.geometry('1280x720')
ani = animation.FuncAnimation(fig, animate, interval=1000)
app.mainloop()