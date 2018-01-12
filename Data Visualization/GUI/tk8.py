from tkinter import *

def do_nothing():
	print('Ok ok I won\'t')

root = Tk()

# Menubar
menu = Menu(root)
root.config(menu=menu)
sub_menu = Menu(menu)
menu.add_cascade(label='File', menu=sub_menu)
sub_menu.add_command(label='New Project', command=do_nothing)
sub_menu.add_command(label='New', command=do_nothing)
sub_menu.add_separator()
sub_menu.add_command(label='Exit', command=do_nothing)
edit_menu = Menu(menu)
menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Redo', command=do_nothing)

# Toolbar
toolbar = Frame(root, bg='blue')
insert_button = Button(toolbar, text='Insert Image', command=do_nothing)
insert_button.pack(side=LEFT, padx=2, pady=2)
print_button = Button(toolbar,text='Print',command=do_nothing)
print_button.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)

# Status bar
status = Label(root, text='Preparing to do nothing', bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()