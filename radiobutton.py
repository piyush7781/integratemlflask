
from tkinter import *
def func():
	if var.get()==1:
		lbl.configure(text="Pay By Cash")
	elif var.get()==2:
		lbl.configure(text="Pay By Card")
	else:
		lbl.configure(text="Select your Option")

win=Tk()
win.title("CoderMantra Tutorial")
win.geometry('200x200')
var=IntVar()
l1=Label(win,text="How do you want to pay")
l1.grid(row=0,column=0)
r1=Radiobutton(win,text="Cash",value=1,variable=var)
r1.grid(row=1,column=0)
r2=Radiobutton(win,text="Card",value=2,variable=var)
r2.grid(row=2,column=0)
b=Button(win,text="Click Here",command=func)
b.grid(row=3,column=0)
lbl=Label(win,text="")
lbl.grid(row=4,column=0)
win.mainloop() 

