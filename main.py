import os
import time
import datetime
from tkinter import *
import tkinter as tk1
import tkinter.messagebox


def runEmployee():
    os.system('python Employee.py')
def runAttendance():
    os.system('python attendance.py')
def runschedule():
    os.system('python schedule.py')



root1=Tk()
root1.title("Employee Management")
root1.geometry('1350x650+0+0')
root1.config(background="powder blue")

btnPayment=Button(root1,text='Employee Manangement',padx=20,pady=20,bd=8,font=('arial',12,'bold'),width=25,command=lambda:runEmployee(),fg="red",bg="powder blue").pack(side=TOP)
btnattendace=Button(root1,text='attendance',padx=20,pady=20,bd=8,font=('arial',12,'bold'),width=25,command=lambda:runAttendance(),fg="red",bg="powder blue").pack(side=LEFT)
btnschedule=Button(root1,text='schedule',padx=20,pady=20,bd=8,font=('arial',12,'bold'),width=25,command=lambda:runschedule(),fg="red",bg="powder blue").pack(side=RIGHT)


root1.mainloop()