from tkinter import *

root = Tk()

def print_name():
	print('Hello bitch!')

button_1 = Button(root, text='Print my name', command=print_name)
button_1.pack()

root.mainloop()