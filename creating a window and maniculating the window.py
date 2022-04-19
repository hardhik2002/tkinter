# tkinter first chapter creating a window.
from tkinter import *
window=Tk()
window.title("tkinter")
mylabel=Label(window,text="programming with tkinter",font=("arial",40),background="black",foreground="red",padx=50,pady=50)
mylabel.pack(side=BOTTOM,pady=300)# should give in capital letters, Becuase it is tkinter constant.
# Pack is a geomentry manager
window.mainloop()# to get screen we should compolsary lopp it.






