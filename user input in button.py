# creating a user input
from tkinter import *
window=Tk()
window.title("input button")
# creating a user input
user_input=Entry(window,width=20,font=("arial",20))
user_input.pack(side=TOP)
# creating a button.
mybutton=Button(window, text="Submit",font=(20),padx=20,pady=10,
activebackground="red",activeforeground="black",bd=6,bg="black",
fg="blue")
mybutton.pack()
window.mainloop()


