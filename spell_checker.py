from tkinter import *
from textblob import TextBlob


root = Tk()
root.title("Spell checker")
root.geometry("600x400")
root.config(background="grey")

heading = Label(root,text="Spell Checker", font=("Trebuchet MS",30,"bold"),bg="black",fg="red")
heading.pack(pady=20)

enter_text = Entry(root,justify="center",width=30,font=("poppins",25),bg="white",border=2)
enter_text.pack()
enter_text.focus()

spell = Label(root,font=("poppins",20),bg="#dae6f6",fg="#364971")
spell.place(x=350,y=300)

def check_spelling():
    word = enter_text.get()
    a = TextBlob(word)
    right = str(a.correct())

    cs = Label(root,text="Correct text is:",font=("poppins",20),bg="#dae6f6",fg="#364971")
    cs.place(y=300)
    spell.config(text=right)

button = Button(root,text="check",font=("arial",20,"bold"),fg="white",bg="red",command=check_spelling())
button.pack(pady=5)


root.mainloop()