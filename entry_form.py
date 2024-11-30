from tkinter import *
from datetime import date
from tkinter import filedialog
from PIL import Image,ImageTk
import os
from tkinter.ttk import Combobox
from tkinter import messagebox
import openpyxl,xlrd
from openpyxl import workbook
import pathlib

background = "#06283D"
framebg = "#EDEDED"
framefg = "#06283D" 



root = Tk()
root.geometry("1250x700+210+100")
root.title("Student Registration System")
root.resizable(False,False)
root.config(bg=background )

file = pathlib.Path('Student_data.xlxx')
if file.exists():
    pass
else:
    file = workbook()
    sheet = file.active
    sheet['A1'] = "Registration No."
    sheet['B1'] = "Name"
    sheet['C1'] = "Class"
    sheet['D1'] = "Gender"
    sheet['E1'] = "DOB"
    sheet['F1'] = "Date of Registration"
    sheet['G1'] = "Religion"
    sheet['H1'] = "Skill"
    sheet['I1'] = "Father Name"
    sheet['J1'] = "Mother Name"
    sheet['K1'] = "Father's Occupation"
    sheet['L1'] = "Mother's Occupation"

file.save('Student_data.xlxx')

Label(root,text="E-mail:x@gmail.com",width=10,height=3,bg="#fo687c",anchor='e').pack(side=TOP,fill=X)
Label(root,text="Student Registration",width=10,height=3,bg="#fo687c",fg="#fff",anchor='e').pack(side=TOP,fill=X)
root.mainloop()