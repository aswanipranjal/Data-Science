from tkinter import *

def do_nothing():
	print('Ok ok I won\'t')

root = Tk()
menu = Menu(root)
root.config(menu=menu)
sub_menu = Menu(menu)
menu.add_cascade(label='File', menu=sub_menu)
sub_menu.add_command(label='New Project', command=do_nothing)
sub_menu.add_command(label='New', command=do_nothing)
sub_menu.add_separator()
sub_menu.add_command(label='Exit', command=do_nothing)
root.mainloop()