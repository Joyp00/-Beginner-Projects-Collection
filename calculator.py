from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())

        scvalue.set(value)
        scvalue.update()

    elif text == "c": 
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("450x700")
root.title("Calculator")
root.wm_iconbitmap("Calculator_icon.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root , textvariable=scvalue , font = "lucida 40 bold")
screen.pack(fill = X , ipadx = 8 , pady=10, padx = 10)

f1 = Frame(root , bg = "grey")
b = Button(f1 , text = "7" , padx=5 , pady=1 , font="lucida 35 bold")
b.pack(side = LEFT , padx = 10 , pady = 2)
b.bind("<Button-1>" , click)
b = Button(f1 , text = "8" , padx=5 , pady=1  , font="lucida 35 bold")
b.pack(side = LEFT ,  padx = 10 , pady = 2)
b.bind("<Button-1>" , click)
b = Button(f1 , text = "9" , padx=5 , pady=1  , font="lucida 35 bold")
b.pack(side = LEFT , padx = 10 , pady = 2)
b.bind("<Button-1>" , click)
f1.pack()

f1 = Frame(root , bg = "grey")
b = Button(f1 , text = "4" , padx=5 , pady=1  , font="lucida 35 bold")
b.pack(side = LEFT , padx = 10 , pady = 2)
b.bind("<Button-1>" , click)
b = Button(f1 , text = "5" , padx=5 , pady=1 , font="lucida 35 bold")
b.pack(side = LEFT ,  padx = 10 , pady = 2)
b.bind("<Button-1>" , click)
b = Button(f1 , text = "6" , padx=5 , pady=1  , font="lucida 35 bold")
b.pack(side = LEFT , padx = 10 , pady = 2)
b.bind("<Button-1>" , click)
f1.pack()

f1 = Frame(root , bg = "grey")
b = Button(f1 , text = "1" , padx=5 , pady=1  , font="lucida 35 bold")
b.pack(side = LEFT , padx = 10 , pady = 2)
b.bind("<Button-1>" , click)
b = Button(f1 , text = "2" ,padx=5 , pady=1 , font="lucida 35 bold")
b.pack(side = LEFT ,  padx = 10 , pady = 2)
b.bind("<Button-1>" , click)
b = Button(f1 , text = "3" , padx=5 , pady=1  , font="lucida 35 bold")
b.pack(side = LEFT , padx = 10 , pady = 2)
b.bind("<Button-1>" , click)
f1.pack()

f1 = Frame(root , bg = "grey")
b = Button(f1 , text = "0" , padx=10 , pady=1  , font="lucida 35 bold")
b.pack(side = LEFT , padx = 10 , pady = 2)
b.bind("<Button-1>" , click)
b = Button(f1 , text = "-" , padx=5 , pady=1 , font="lucida 35 bold")
b.pack(side = LEFT ,  padx = 10 , pady = 2)
b.bind("<Button-1>" , click)
b = Button(f1 , text = "*" , padx=9 , pady=1  , font="lucida 35 bold")
b.pack(side = LEFT , padx = 10 , pady = 2)
b.bind("<Button-1>" , click)
f1.pack()

f1 = Frame(root , bg = "grey")
b = Button(f1 , text = "/" , padx=5 , pady=1  , font="lucida 35 bold")
b.pack(side = LEFT , padx = 10 , pady = 2)
b.bind("<Button-1>" , click)
b = Button(f1 , text = "%" , padx=5 , pady=1  , font="lucida 35 bold")
b.pack(side = LEFT ,  padx = 10 , pady = 2)
b.bind("<Button-1>" , click)
b = Button(f1 , text = "+" , padx=3 , pady=1 , font="lucida 35 bold")
b.pack(side = LEFT , padx = 10 , pady = 2)
b.bind("<Button-1>" , click)
f1.pack()

f1 = Frame(root , bg = "grey")
b = Button(f1 , text = "=" , padx=2 , pady=1  , font="lucida 35 bold")
b.pack(side = LEFT , padx = 5 , pady = 2)
b.bind("<Button-1>" , click)
b = Button(f1 , text = "c" , padx=5 , pady=1 , font="lucida 35 bold")
b.pack(side = LEFT ,  padx = 10 , pady = 2)
b.bind("<Button-1>" , click)
b = Button(f1 , text = "<-" , padx=5 , pady=1 , font="lucida 35 bold")
b.pack(side = RIGHT , padx = 9 , pady = 2)
b.bind("<Button-1>" , click)
f1.pack()

root.mainloop()