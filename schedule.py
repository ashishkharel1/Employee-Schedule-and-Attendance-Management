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

f1a = Frame(f1, width=100, height=100, bd=8, bg="powder blue")
f1a.place(x=0, y=0)
f1b = Frame(f1, width=100, height=100, bd=8, bg="powder blue")
f1b.place(x=100, y=0)
f1c = Frame(f1, width=200, height=100, bd=8, bg="powder blue")
f1c.place(x=225, y=0)
f1d = Frame(f1, width=200, height=100, bd=8, bg="powder blue")
f1d.place(x=350, y=0)
f1e = Frame(f1, width=200, height=100, bd=8, bg="powder blue")
f1e.place(x=450,y=0)
lblinfo = Label(f1a, font=('arial', 15, 'bold'), text="id        ", bd=10, fg="green")
lblinfo.grid(row=0, column=0)
lblinfo = Label(f1b, font=('arial', 15, 'bold'), text="Username", bd=10, fg="green")
lblinfo.grid(row=0, column=1)
lblinfo = Label(f1c, font=('arial', 15, 'bold'), text="DATE      ", bd=10, fg="green")
lblinfo.grid(row=0, column=2)
lblinfo = Label(f1d, font=('arial', 15, 'bold'), text="Time in", bd=10, fg="green")
lblinfo.grid(row=0, column=3)
lblinfo = Label(f1e, font=('arial', 15, 'bold'), text="Time out", bd=10, fg="green")
lblinfo.grid(row=0, column=4)
my_cursor = mydb.cursor()
my_cursor.execute("SELECT * FROM attendance limit 0,10")
i = 0

for test in my_cursor:
    for j in range(len(test)):
        e = Entry(scrollable_frame, width=20, fg='blue')
        e.grid(row=i, column=j)
        e.insert(END, test[j])
    i = i + 1

def runschedule():
    os.system('python createSchedule.py')
def runschedule1():
    os.system('python selectemployee.py')

btnselectemployee=Button(newWindow,text='Search Employee',padx=20,pady=20,bd=8,font=('arial',12,'bold'),width=25,command=lambda:runschedule1(),fg="red",bg="powder blue").pack(side=BOTTOM)
btnAddNewSchedule=Button(newWindow,text='Add New Schedule',padx=20,pady=20,bd=8,font=('arial',12,'bold'),width=25,command=lambda:runschedule(),fg="red",bg="powder blue").pack(side=BOTTOM)



tk.mainloop()
