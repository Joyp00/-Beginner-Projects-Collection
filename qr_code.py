from tkinter import *
import qrcode

root = Tk()
root.geometry("1000x600")
root.title("Qrcode generator")
root.config(bg="#AE2321")
root.resizable(FALSE,False)
icon = PhotoImage(file="icon.png")
root.iconphoto(False,icon)

def generate():
    name = title.get()
    text = content.get()
    qr = qrcode.make(text)
    qr.save("Qrcodes/"+str(name)+".png") 
    global Image
    Image = PhotoImage(file="Qrcodes/"+str(name)+".png")
    image_view.config(image=Image)

image_view = Label(root,bg="#AE2321")
image_view.pack(padx=50,pady=10,side = RIGHT)


Label(root,text="Title:",fg="white",bg="#AE2321",font=15).place(x=15,y=170)
title = Entry(root,width=13,font="arial 15")
title.place(x=15,y=220)

content = Entry(root,width=30,font="arial 15")
content.place(x=15,y=270)

Button(root,text="Generate",width=20,height=2,bg="black",fg="white",font=("times new roman",20,"bold"),command=generate).place(x=15,y=320)

root.mainloop()