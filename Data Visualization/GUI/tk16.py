from tkinter import *

canvas_width = 500
canvas_height = 150

def paint(event):
	python_green = '#476042'
	x1, y1 = (event.x - 1), (event.y - 1)
	x2, y2 = (event.x + 1), (event.y + 1)
	w.create_oval(x1, y1, x2, y2, fill=python_green)