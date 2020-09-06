import os
import time
import datetime
from tkinter import *
import tkinter as tk
import tkinter.messagebox

import mysql.connector
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="12345678",
    database='mydb'
)



newWindow=Tk()
newWindow.title("DATABASE")
newWindow.geometry('1350x650+0+0')
newWindow.config(background="powder blue")

# Tops = Frame(newWindow, width=1350, height=50, bd=8, bg="powder blue")
# Tops.pack(side=TOP)

f1 = Frame(newWindow, width=600, height=100, bd=8)
f1.pack(side=TOP)
f2 = Frame(newWindow, width=600, height=300, bd=8)
canvas = Canvas(f2, width=600, height=300)
scrollbar = Scrollbar(f2, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas)
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

f2.pack()
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

f2.pack(side=TOP)
fla = Frame(f1, width=600, height=200, bd=8, bg="powder blue")
fla.pack(side=TOP)

def searchEmployee():
    my_cursor = mydb.cursor()
    my_cursor.execute("select * from attendance where Username='uma'")
    i = 0

    for test in my_cursor:
        for j in range(len(test)):
            e = Entry(scrollable_frame, width=15, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, test[j])
        i = i + 1


Name = StringVar()
lblName = Label(fla, text=" Search Employee Name:", font=('arial', 16, 'bold'), bd=20, fg="red", bg="powder blue").grid(row=0, column=0)
etxname=Entry(fla,textvariable=Name,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxname.grid(row=0,column=1)
btnsearch=Button(fla,text='search',padx=10,pady=10,bd=8,font=('arial',12,'bold'),width=10,command=lambda:searchEmployee(),fg="red",bg="powder blue").grid(row=0, column=5)



tk.mainloop()
