from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('Window Title', 'I can lie if I want to')
answer = tkinter.messagebox.askquestion('Question 1', 'But does it djent?')
if answer == 'yes':
	print('8=====D')
else:
	print('8=D')

root.mainloop()