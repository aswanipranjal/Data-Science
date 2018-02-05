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