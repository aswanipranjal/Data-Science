from tkinter import *
from time import sleep

root = Tk()
var = StringVar()
var.set('Hello')

l = Label(root, textvariable=var)
l.pack()

for i in range(6):
	sleep(0.25)
	var.set('Goodbye' if i%2 else 'Hello')
	root.update_idletasks()