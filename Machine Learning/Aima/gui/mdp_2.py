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
f1 = Frame(root)
f2 = Frame(root)

for frame in (f1, f2):
	frame.grid(row=0, column=0, sticky='news')

# Home Screen (f1) widgets
frame1 = Frame(f1)
frame1.pack(side=tk.TOP)
frame2 = Frame(f1)
frame2.pack(side=tk.TOP)
label = ttk.Label(frame1, text='Home Page', font=('Verdana', 12))
label.pack(pady=10, padx=10, side=tk.TOP)
label = ttk.Label(frame1, text='Dimensions', font=('Verdana', 10))
label.pack(pady=10, padx=10, side=tk.TOP)
entry_h = Entry(frame2, font=('Verdana', 10), width=3, justify=tk.CENTER)
entry_h.pack(pady=10, padx=10, side=tk.LEFT)
label_x = ttk.Label(frame2, text='X', font=('Verdana', 10))
label_x.pack(pady=10, padx=4, side=tk.LEFT)
entry_w = Entry(frame2, font=('Verdana', 10), width=3, justify=tk.CENTER)
entry_w.pack(pady=10, padx=10, side=tk.LEFT)
button = ttk.Button(self, text='Build a GridMDP', command=lambda: controller.show_frame(BuildMDP, entry_h.get(), entry_w.get()))
button.pack(pady=10, padx=10, side=tk.TOP)