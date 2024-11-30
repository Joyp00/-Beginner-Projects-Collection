from tkinter import *

root = Tk()
root.geometry("1200x1000")
root.title("Registration form")
root.wm_iconbitmap("checkform.ico")

photo = PhotoImage(file="form_img.png")
myphoto = Label(image=photo)
myphoto.pack(pady=100)


name = Entry(root,textvariable=StringVar(),width=40,bd=3,font=20)
name.place(x=400,y=205)
E_mail = Entry(root,textvariable=StringVar(),width=40,bd=3,font=20)
E_mail.place(x=400,y=255)
Phone =Entry(root,textvariable=StringVar(),width=40,bd=3,font=20)
Phone.place(x=400,y=305)
Gender = Entry(root,textvariable=StringVar(),width=40,bd=3,font=20)
Gender.place(x=400,y=355)

Checkbutton(root,text="remember me").place(x=350,y=400)

def save_data():
    name_value = name.get()
    E_mail_value = E_mail.get()
    Phone_value = Phone.get()
    Gender_value = Gender.get()

    file = open(name_value+".txt","w")
    file.write(name_value+"\n")
    file.write(E_mail_value+"\n")
    file.write(Phone_value+"\n")
    file.write(Gender_value+"\n")
    Label(root,text="Registration success",fg="Green",font=("Times new roman",10,"bold")).place(x=350,y=600)     


def clear():
    name.delete(0,END)
    E_mail.delete(0,END)
    Phone.delete(0,END)
    Gender.delete(0,END)


name_label = Label(root,text="Name :",font=("Times new roman",20,"bold"))
name_label.place(x=300,y=200)
Email_label = Label(root,text="E-mail :",font=("Times new roman",20,"bold"))
Email_label.place(x=300,y=250)
Phone_label = Label(root,text="Phone :",font=("Times new roman",20,"bold"))
Phone_label.place(x=300,y=300)
Gender_label  = Label(root,text="Gender :",font=("Times new roman",20,"bold"))
Gender_label.place(x=300,y=350)

save = Button(root,text="Register",font=("Times new roman",20,"bold"),bg="grey",fg="black",command=save_data)
save.place(x=350,y=450)
Button(root,text="Clear",font=("Times new roman",20,"bold"),bg="grey",fg="black",command=clear).place(x=475,y=450)


root.mainloop()