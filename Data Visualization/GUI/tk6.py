from tkinter import *

root = Tk()

def left_click(event):
	print('Left')

def right_click(event):
	print('Right')

def middle_click(event):
	print('Middle')

m_frame = Frame(root, width=300, height=250)
m_frame.bind('<Button-1>', left_click)
m_frame.bind('<Button-2>',  middle_click)
m_frame.bind('<Button-3>', right_click)
m_frame.pack()

root.mainloop()