# creating a button.
from tkinter import *
window=Tk()
window.title("button")
def click():
    label=Label(window,text="Hi I am Hardhik.",font=(20))
    label.pack(pady=3)

mybutton=Button(window, text="click me!",font=(20),padx=20,pady=10,
activebackground="red",activeforeground="black",bd=6,bg="black",
fg="blue",command=click)
mybutton.pack(pady=250)
window.mainloop()



