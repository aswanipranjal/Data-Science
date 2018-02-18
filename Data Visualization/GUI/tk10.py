from tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()
black_line = canvas.create_line(0, 0, 100, 50)
red_line = canvas.create_line(100, 50, 150, 75, fill='red')
blue_line = canvas.create_line(150, 75, 175, 87.5, fill='blue')
green_box = canvas.create_rectangle(175, 87.5, 200, 100, fill='green')
# to delete one entity
canvas.delete(red_line)
# to delete everything
canvas.delete(ALL)
root.mainloop()