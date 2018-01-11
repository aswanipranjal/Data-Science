from tkinter import *

class generic_class:

	# master refers to the main window
	def __init__(self, master):
		m_frame = Frame(master)
		m_frame.pack()

		self.print_button = Button(m_frame, text='Print Message', command=self.print_message)
		self.print_button.pack(side=LEFT)

		self.quit_button = Button(m_frame, text='Quit', command=m_frame.quit)
		self.quit_button.pack(side=LEFT)

	def print_message(self):
		print('Random message')


root = Tk()
g_c = generic_class(root)
root.mainloop()