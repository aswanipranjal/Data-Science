import sys
import time
import random
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from tkinter import *
from tkinter import ttk

height = 0
width = 0

def raise_frame(frame):
	frame.tkraise()

root = Tk()
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
f1 = Frame(root)
f2 = Frame(root)

for frame in (f1, f2):
	frame.grid(row=0, column=0, sticky='news')

# Home Screen (f1) widgets
frame1 = Frame(f1)
frame1.pack(side=TOP, anchor=CENTER)
frame2 = Frame(f1)
frame2.pack(side=TOP, anchor=CENTER)
label = ttk.Label(frame1, text='Home Page', font=('Verdana', 12))
label.pack(pady=10, padx=10, side=TOP)
label = ttk.Label(frame1, text='Dimensions', font=('Verdana', 10))
label.pack(pady=10, padx=10, side=TOP)
entry_h = Entry(frame2, font=('Verdana', 10), width=3, justify=CENTER)
entry_h.pack(pady=10, padx=10, side=LEFT)
label_x = ttk.Label(frame2, text='X', font=('Verdana', 10))
label_x.pack(pady=10, padx=4, side=LEFT)
entry_w = Entry(frame2, font=('Verdana', 10), width=3, justify=CENTER)
entry_w.pack(pady=10, padx=10, side=LEFT)
button = ttk.Button(frame2, text='Build a GridMDP')
button.pack(pady=10, padx=10, side=TOP)

def create_grid(_height, _width):
	

raise_frame(f1)
root.geometry('1280x720')
root.mainloop()