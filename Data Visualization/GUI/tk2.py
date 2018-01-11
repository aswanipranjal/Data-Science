from tkinter import *

root = Tk()
frame1 = Frame(root)
frame1.pack()
frame2 = Frame(root)
frame2.pack(side=BOTTOM)

m_button1 = Button(frame1, 'Button 1', fg='#05ed61')
m_button2 = Button(frame1, 'Button 2', fg='red')
m_button3 = Button(frame1, 'Button 3', fg='blue')
m_button4 = Button(frame2, 'Button 4', fg='purple')
m_button1.pack(side=LEFT)
m_button2.pack(side=LEFT)
m_button3.pack(side=LEFT)
m_button4.pack()

root.mainloop()