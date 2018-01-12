from tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()
black_line = canvas.create_line(0, 0, 100, 50)
red_line = canvas.create_line(100, 50, 150, 75, fill='red')
blue_line = canvas.create_line(150, 75, 175, 87.5, fill='blue')
root.mainloop()