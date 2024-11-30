from tkinter import *
from datetime import date

root = Tk()
root.geometry("800x600")
root.title("Age calculator")
root.wm_iconbitmap("age.ico")

photo = PhotoImage(file="age_calc (1).png")
myphoto = Label(image=photo)
myphoto.pack(padx=150,pady=50)

Label(text="Name :",font=("Times new roman",10,"bold")).place(x=200,y=200)
Label(text="Year :",font=("Times new roman",10,"bold")).place(x=200,y=250)
Label(text="Month :",font=("Times new roman",10,"bold")).place(x=200,y=300)
Label(text="Date :",font=("Times new roman",10,"bold")).place(x=200,y=350)

name = Entry(root,textvariable = StringVar() , width=30 ,bd=3,font=20)
name.place(x=250,y=200)
Year = Entry(root,textvariable = StringVar() , width=30 ,bd=3,font=20)
Year.place(x=250,y=250)
Month = Entry(root,textvariable = StringVar() , width=30 ,bd=3,font=20)
Month.place(x=250,y=300)
Day = Entry(root,textvariable = StringVar() , width=30 ,bd=3,font=20)
Day.place(x=250,y=350)

def calculate():
    today = date.today()
    birthDate = date(int(Year.get()),int(Month.get()),int(Day.get()))
    age = today.year - birthDate.year-((today.month,today.day)<(birthDate.month,birthDate.day))
    month_age = today.month-birthDate.month
    day_age = today.day-birthDate.day
    Label(text=f"{name.get()}'s age is {age} years {abs(month_age)} months {abs(day_age)} days",font=30).place(x=250,y=450)

def clear():
    name.delete(0,END)
    Year.delete(0,END)
    Month.delete(0,END)
    Day.delete(0,END)

Button(root,text="Calculate",font=("Times new roman",15,"bold"),bg="grey",fg="black",command=calculate).place(x=300,y=400)
Button(root,text="Clear",font=("Times new roman",15,"bold"),bg="grey",fg="black",command=clear).place(x=400,y=400)



root.mainloop()