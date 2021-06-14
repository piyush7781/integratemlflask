from tkinter import *
from tkinter import messagebox
def func():
    messagebox.showwarning('CoderMantra', 'Need Code Practice')
win=Tk()
win.geometry('350x200')
b = Button(win,text='Click Here', command=func)
b.grid(column=0,row=0)
win.mainloop()
