from tkinter import *
from tkinter import messagebox
import os

def mainscreen():
    screen = Tk()
    screen.geometry("1280x720+150+80")
    screen.config(bg="#d7dae2")
    screen.wm_iconbitmap("Login.ico")
    screen.title("Login panel")

    title = Label(text="Login System",font=("arial",50,"bold"),bg="#d7dae2",fg="black")
    title.pack(pady=50)

    bordercolor = Frame(screen,bg="black",width=800,height=400)
    bordercolor.pack()

    mainframe = Frame(bordercolor,width=800,height=400)
    mainframe.pack(padx=20,pady=20)  
    Label(mainframe,text="Username:",font=("arial",30,"bold"),bg="#d7dae2").place(x=100,y=50)
    Label(mainframe,text="Password:",font=("arial",30,"bold"),bg="#d7dae2").place(x=100,y=150)
    username = StringVar()
    password = StringVar()

    entry_username = Entry(mainframe,textvariable=username,width=12,bd=2,font=("arial",30,"bold"))
    entry_username.place(x=400,y=50)
    entry_password = Entry(mainframe,textvariable=password,width = 12,bd=2,font=("arial",30,"bold"),show="*")
    entry_password.place(x=400,y=150)

    def reset():
        entry_username.delete(0,END)
        entry_password.delete(0,END)

    def login():
        user = username.get()
        code = password.get()
        if user == "joy" and code =="1234":
            root = Toplevel(screen)
            root.title("Bill")
            root.geometry("1280x720+150+80")
            root.configure(bg="#D7dae2")
            root.resizable(False,False)
        elif user=="" and code =="":
            messagebox.showerror("Invalid","Please enter username and password")
        elif user=="":
            messagebox.showerror("Invalid","Please enter username")
        elif code=="":
            messagebox.showerror("Invalid","Please enter password")
        elif user!="joy" and code!="1234":
            messagebox.showerror("Invalid username or password")
        elif user!="joy" and code == "1234":
            messagebox.showerror("Please enter correct username or password")
        elif user == "joy" and code != "1234":    
            messagebox.showerror("Please enter correct username or password")
            
    Button(mainframe,text="Login",height="2",width="23",bg="#ed3833",fg="white",bd=0,command=login).place(x=100,y=250)
    Button(mainframe,text="Reset",height="2",width="23",bg="#1089ff",fg="white",bd=0,command=reset).place(x=300,y=250)
    Button(mainframe,text="Exit",height="2",width="23",bg="#00bd56",fg="white",bd=0,command=screen.destroy).place(x=500,y=250)


    screen.mainloop()

mainscreen()