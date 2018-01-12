from tkinter import *

root = Tk()

photo = PhotoImage(file='C:/Users/Aman Deep Singh/Documents/Python/Data Science/Data Visualization/GUI/car.png')
label = Label(root, image=photo, text='Only png images work')
label.pack()

root.mainloop()