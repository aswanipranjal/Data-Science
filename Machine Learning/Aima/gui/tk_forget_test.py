from tkinter import *

root = Tk()

b = Button(root, text='Delete Me', command=lambda: b.pack_forget())
b.pack()

root.mainloop()