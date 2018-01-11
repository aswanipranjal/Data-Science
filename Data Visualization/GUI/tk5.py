from tkinter import *

root = Tk()

def print_name():
	print('Hello bitch!')

def print_name_event(event):
	print('Hello fucking bitch!')	

button_1 = Button(root, text='Print my name', command=print_name)
button_1.pack()

button_2 = Button(root, text='Print my name, again')
button_2.bind("<Button-1>", print_name_event)
button_2.pack()

root.mainloop()