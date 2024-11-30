from tkinter import *
from playsound import playsound
import time

root = Tk()
root.geometry("400x600")
root.title("Timer")
root.config(bg="black")

heading = Label(root,text="Timer",font=("times new roman", 30,"bold"),fg="red",bg="black")
heading.pack(padx=90,pady=20)

Label(root,text="current time: ",font=("times new roman", 20,"bold"),fg="red").place(x=40,y=70)
def clock():
    c_time = time.strftime('%H:%M:%S %p')
    current_time.config(text=c_time)
    current_time.after(1000,clock)

current_time = Label(root,text="",font=("times new roman", 20,"bold"),fg="red",bg="papaya whip")
current_time.place(x=195,y=70)
clock()

hrs = StringVar()
Entry(root,textvariable=hrs,width = 2 , font =("Times new roman",50), fg="red",bg="black",bd=0).place(x=30,y=150)
hrs.set("00")

mins = StringVar()
Entry(root,textvariable=mins,width = 2 , font =("Times new roman",50), fg="red",bg="black",bd=0).place(x=150,y=150)
mins.set("00")

sec = StringVar()
Entry(root,textvariable=sec,width = 2 , font =("Times new roman",50), fg="red",bg="black",bd=0).place(x=270,y=150)
sec.set("00")

Label(root,text="hours",font=("times new roman",10),fg="white",bg="black",bd=0).place(x=100,y=210)
Label(root,text="mins",font=("times new roman",10),fg="white",bg="black",bd=0).place(x=220,y=210)
Label(root,text="sec",font=("times new roman",10),fg="white",bg="black",bd=0).place(x=340,y=210)

def timer():
    s_timer = int(hrs.get())*3600 + int(mins.get())*60 + int(sec.get())

    while s_timer > -1:
        minute , second = (s_timer//60 , s_timer %60)

        hour = 0
        if minute>60:
            hour ,minute = (minute//60,minute%60)

        sec.set(second)
        mins.set(minute)
        hrs.set(hour)

        root.update()
        time.sleep(1)

        if(s_timer == 0):
            playsound("jeopardy_times_up.wav")
            sec.set("00")
            mins.set("00")
            hrs.set("00")
        s_timer-=1

Button(root,text="Start",bg="red",fg="black",width=20,height=2,font=("Times new roman",10,"bold"),bd=0,command=timer).place(x=120,y=500)


root.mainloop()