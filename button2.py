# creating a button by using all methodes and arguments.
from tkinter import *
window=Tk()
window.title("Button2")


mybutton=Button(window,text="Click me!",font=(25),padx=22,pady=10,justify=CENTER,relief=RAISED,state=ACTIVE,highlightcolor="red",activebackground="black",
        activeforeground="blue",bd=8,bg="black",fg="blue")# justify is not working
mybutton.pack()
window.mainloop()
