from tkinter import *
from tkinter.filedialog import askopenfile , asksaveasfile
import tkinter as tk

def saveFile():
    new_file = asksaveasfile(mode = 'w' , filetype = [('text files', '.txt')])
    if new_file is None:
        return
    text = str(entry.get(1.0 , END))
    new_file.write(text)
    new_file.close()

def openFile():
    file = askopenfile(mode = 'r' , filetype = [('text files' , '.txt')])
    if file is not None:
        content = file.read()
    entry.insert(INSERT , content)

def clearFile():
     entry.delete(1.0 , END)

canvas = tk.Tk()
canvas.geometry("400x600")
canvas.title("Notepad")
canvas.config(bg = "white")

top = Frame(canvas)
top.pack(padx = 10 , pady = 5 , anchor = 'nw')

b1 = Button(canvas , text = "Open" , bg = "White" , command= openFile)
b1.pack(in_ = top , side = LEFT)

b2 = Button(canvas , text = "Save" , bg = "White" , command= saveFile)
b2.pack(in_ = top , side = LEFT)

b3 = Button(canvas , text = "Clear" , bg = "White" , command= clearFile)
b3.pack(in_ = top , side = LEFT)

b4 = Button(canvas , text = "Exit" , bg = "White")
b4.pack(in_ = top , side = LEFT)

entry = Text(canvas , wrap = WORD , bg = "white" , font = ("times new roman" , 15))
entry.pack(padx = 10 , pady= 5 , expand = True , fill = BOTH)
canvas.mainloop()