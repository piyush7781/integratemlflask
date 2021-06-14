from tkinter import *
def func():
	val=""
	if ch1.get()==1:
		val+="Java "
	if ch2.get()==1:
		val+="Python"
	lbl.configure(text=val)


win=Tk()
win.title("CoderMantra Tutorial")
win.geometry('300x200')
ch1=IntVar()
ch2=IntVar()
l1=Label(win,text="Your Favourite Programming Language")
l1.grid(row=0,column=0)
r1=Checkbutton(win,text="Java",variable=ch1)
r1.grid(row=1,column=0)
r2=Checkbutton(win,text="Python",variable=ch2)
r2.grid(row=2,column=0)
b=Button(win,text="Click Here",command=func)
b.grid(row=3,column=0)
lbl=Label(win,text="")
lbl.grid(row=4,column=0)
win.mainloop()
