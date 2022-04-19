# practicing on Entry.
from tkinter import *
window=Tk()
window.title("Entry")
frame=Frame(window,bg="red")# Frame is not working
frame.pack()
# creating a user input
user_input=Entry(window,width=20,font=("arial",20),bg="Black",fg="red",)
user_input.insert(0,"username")
user_input.pack(padx=20,pady=10)
user_input_2=Entry(window,width=15,font=("arial",20),show="*",bg="Black",fg="red")
user_input_2.insert(0,"Password")
user_input_2.pack(padx=20,pady=10)
window.mainloop()
