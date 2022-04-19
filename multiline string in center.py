# printing multiline string in the center of the window.
from tkinter import  *
window=Tk()
window.title("string")
label=Label(window,text="""The packer is one of Tk’s geometry-management mechanisms. 
Geometry managers are used to specify the relative positioning of widgets within 
their container - their mutual master. 
In contrast to the more cumbersome placer (which is used less commonly, 
and we do not cover here), the packer takes qualitative relationship specification - 
above, to the left of, filling, etc - and works everything out to determine the exact 
placement coordinates for you.""",font=(20),padx=50,pady=50,foreground="red")
label.pack(pady=250)
window.mainloop()

