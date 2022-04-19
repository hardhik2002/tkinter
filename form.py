# devoloping a bio data form
from tkinter import *
window=Tk()
window.title("form")
# heading
head=Label()

# adding text
first_name=Label(text="Enter your first name:",font=("arial",11))
last_name=Label(text="Enter your last name:",font=("arial",11))
age=Label(text="Enter your age:",font=("arial",11))
first_name.place(x=15,y=70)
last_name.place(x=15,y=140)
age.place(x=15,y=210)
first_name=StringVar()
last_name=StringVar()
age=IntVar()
# massage box
first_name_entry=Entry(textvariable=first_name,width="30",bd=5,cursor="arrow",selectbackground="red")
second_name_entry=Entry(textvariable=last_name,width="30",bd=5,cursor="arrow",selectbackground="red")
age_entry=Entry(textvariable=age,width="30",bd=5,cursor="arrow",selectbackground="red")
first_name_entry.place(x=15,y=100)
second_name_entry.place(x=15,y=180)
age_entry.place(x=15,y=240)
button=Button(text="Register",width="15",height="2",padx=30,bd=5)
button.place(x=0,y=290)

window.mainloop()

