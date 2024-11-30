from tkinter import*

root = Tk()
root.geometry("700x400")
root.title("Bill management")


Label(text="BILL MANAGEMENT",font=("Times new roman",20,"bold"),bg="black",fg="white",width=700).pack()
f = Frame(root,bg="#E3E4FA",width=300,height=750,highlightthickness=2)
f.place(x=2,y=40)
Label(f,text="Menu",font=("Times new roman",20,"bold"),fg="black",bg="#E3E4FA").place(x=100,y=10)

Label(f,text="1.Dosa......Rs.60/plate",font=("Times new roman",12,"bold"),fg="black",bg="#E3E4FA").place(x=50,y=60)
Label(f,text="2.Cookies......Rs.30/plate",font=("Times new roman",12,"bold"),fg="black",bg="#E3E4FA").place(x=50,y=90)
Label(f,text="3.Tea......Rs.7/cup",font=("Times new roman",12,"bold"),fg="black",bg="#E3E4FA").place(x=50,y=120)
Label(f,text="4.Coffee......Rs.100/cup",font=("Times new roman",12,"bold"),fg="black",bg="#E3E4FA").place(x=50,y=150)
Label(f,text="5.Juice......Rs.20/glass",font=("Times new roman",12,"bold"),fg="black",bg="#E3E4FA").place(x=50,y=180)
Label(f,text="6.Pancake......Rs.15/pack",font=("Times new roman",12,"bold"),fg="black",bg="#E3E4FA").place(x=50,y=210)
Label(f,text="7.Eggs......Rs.7/egg",font=("Times new roman",12,"bold"),fg="black",bg="#E3E4FA").place(x=50,y=240)

Label(root,text="Dosa",font=("Times new roman",12,"bold"),fg="black").place(x=350,y=50)
dosa = Entry(root,textvariable=StringVar(),width=15)
dosa.place(x=420,y=55)
Label(root,text="Cookies",font=("Times new roman",12,"bold"),fg="black").place(x=350,y=80)
cookies = Entry(root,textvariable=StringVar(),width=15)
cookies.place(x=420,y=85)
Label(root,text="Tea",font=("Times new roman",12,"bold"),fg="black").place(x=350,y=110)
tea = Entry(root,textvariable=StringVar(),width=15)
tea.place(x=420,y=115)
Label(root,text="Coffee",font=("Times new roman",12,"bold"),fg="black").place(x=350,y=140)
coffee = Entry(root,textvariable=StringVar(),width=15)
coffee.place(x=420,y=145)
Label(root,text="Juice",font=("Times new roman",12,"bold"),fg="black").place(x=350,y=170)
juice = Entry(root,textvariable=StringVar(),width=15)
juice.place(x=420,y=175)
Label(root,text="Pancakes",font=("Times new roman",12,"bold"),fg="black").place(x=350,y=200)
pancake = Entry(root,textvariable=StringVar(),width=15)
pancake.place(x=420,y=205)
Label(root,text="Eggs",font=("Times new roman",12,"bold"),fg="black").place(x=350,y=230)
egg = Entry(root,textvariable=StringVar(),width=15)
egg.place(x=420,y=235)

def reset():
    dosa.delete(0,END)
    cookies.delete(0,END)
    tea.delete(0,END)
    coffee.delete(0,END)
    juice.delete(0,END)
    pancake.delete(0,END)
    egg.delete(0,END)

    

def calculate():
    try:a1 = int(dosa.get())
    except:a1=0
    try:a2 = int(cookies.get())
    except:a2=0
    try:a3 = int(tea.get())
    except:a3=0
    try:a4 = int(coffee.get())
    except:a4=0
    try:a5 = int(juice.get())
    except:a5=0
    try:a6 = int(pancake.get())
    except:a6=0
    try:a7 = int(egg.get())
    except:a7=0

    c1 = 60*a1
    c2 = 30*a2
    c3 = 7*a3
    c4 = 100*a4
    c5 = 20*a5
    c6 = 15*a6
    c7 = 7*a7

    total_bill = StringVar()
    # total = Label(f2,text="Total",font=("Times new roman",18,"normal"),width=300)
    # total.place(x=0,y=55)
    total_entry = Entry(f2,textvariable=total_bill,width=20)
    total_entry.place(x=5,y=100)

    cost = c1+c2+c3+c4+c5+c6+c7
    string_bill = "Total Rs. ",str('%.2f'%cost)
    total_bill.set(string_bill)

Button(root,text="Reset",bg="grey",fg="black",font=("Times new roman",15,"bold"),width=5,command=reset).place(x=340,y=270)
Button(root,text="Total",bg="grey",fg="black",font=("Times new roman",15,"bold"),width=5,command=calculate).place(x=420,y=270)

f2 = Frame(root,bg="#AAF0D1",width=300,height=750,highlightthickness=2)
f2.place(x=520,y=40)

Label(f2,text="Bill",font=("Times new roman",18,"bold"),bg="#AAF0D1").place(x=60,y=10)
Label(f2,text="Total",font=("Times new roman",18,"normal"),fg="white",width=300).place(y=55)
Entry(f2,textvariable=StringVar(),width=20).place(x=5,y=100)

root.mainloop()