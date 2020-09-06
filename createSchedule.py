import time
import datetime
from tkinter import *
import tkinter as tk
import tkinter.messagebox

import mysql.connector

# import MySQLdb

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="12345678",
    database='mydb'
)
root = Tk()
root.title("Add Employee Schedule")
root.geometry('1350x650+0+0')
root.config(background="powder blue")

Tops = Frame(root, width=1350, height=50, bd=8, bg="powder blue")
Tops.pack(side=TOP)

f1 = Frame(root, width=600, height=600, bd=8, bg="powder blue")
f1.pack(side=LEFT)
f2 = Frame(root, width=300, height=700, bd=8, bg="powder blue")
f2.pack(side=RIGHT)

fla = Frame(f1, width=600, height=200, bd=8, bg="powder blue")
fla.pack(side=TOP)
flb = Frame(f1, width=300, height=600, bd=8, bg="powder blue")
flb.pack(side=TOP)

lblinfo = Label(Tops, font=('arial', 45, 'bold'), text=" Add Employee Schedule ", bd=10, fg="green")
lblinfo.grid(row=0, column=0)


def exit():
    exit = tkinter.messagebox.askyesno("Employee system", "Do you want to exit the system")
    if exit > 0:
        root.destroy()
        return


def reset():
    Name.set("")
    Date.set("")
    TimeIn.set("")
    TimeOut.set("")

    txtpayslip.delete("1.0", END)


def enterinfo():
    txtpayslip.delete("1.0", END)
    txtpayslip.insert(END, "\t\tPay Slip\n\n")
    txtpayslip.insert(END, "Name :\t\t" + Name.get() + "\n\n")
    txtpayslip.insert(END, "Date :\t\t" + Date.get() + "\n\n")
    txtpayslip.insert(END, "Time in  :\t\t" + TimeIn.get() + "\n\n")
    txtpayslip.insert(END, "Time out :\t\t" + TimeOut.get() + "\n\n")





def save():
    if Name.get() == '' or Date.get() == '' or TimeIn.get() == '' or TimeOut.get()=='':
        tkinter.messagebox.showwarning("error", "All fields required")
    else:

        data1 = "Name :\t\t" + Name.get() + "\n\n"
        data2 = "Date: \t\t:" + Date.get() + "\n\n"
        data3 = "Time In :\t\t" + TimeIn.get() + "\n\n"
        data4 = "Time Out :\t\t" + TimeOut.get() + "\n\n"


        uma = mydb.cursor()
        # uma.execute("SELECT * FROM  spreadsheet;")
        sql = "INSERT INTO `attendance` (Username, date, timein, timeout ) VALUES (%s, %s, %s,%s)"
        val = (Name.get(), Date.get(), TimeIn.get(), TimeOut.get())
        try:
            uma.execute(sql, val)

        except:
            tkinter.messagebox.showwarning("error", "Incorrect Format")



        # with open('uma.txt', 'w') as out:
        #   out.writelines([data1,data2,data3,data4,data5,data6,data7,data8,data9])
        # out.close()
        mydb.commit()
        # mydb.close()



# =============================== Variables ========================================================
Name = StringVar()
Date = StringVar()
TimeIn  = StringVar()
TimeOut = StringVar()



# ================================ Label Widget =================================================

lblName = Label(fla, text="Name", font=('arial', 16, 'bold'), bd=20, fg="red", bg="powder blue").grid(row=0, column=0)
lblAddress = Label(fla, text="Date(yy-mm-dd)", font=('arial', 16, 'bold'), bd=20, fg="red", bg="powder blue").grid(row=0,
                                                                                                            column=2)
lblEmployer = Label(fla, text="Time In(hh:mm:ss)", font=('arial', 16, 'bold'), bd=20, fg="red", bg="powder blue").grid(row=1,
                                                                                                              column=0)
lblNINumber = Label(fla, text="Time Out(hh:mm:ss)", font=('arial', 16, 'bold'), bd=20, fg="red", bg="powder blue").grid(row=1,
                                                                                                               column=2)


# =============================== Entry Widget =================================================

etxname = Entry(fla, textvariable=Name, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
etxname.grid(row=0, column=1)

etxDate = Entry(fla, textvariable=Date, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
etxDate.grid(row=0, column=3)

etxTimeIn = Entry(fla, textvariable=TimeIn, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
etxTimeIn.grid(row=1, column=1)

etxTimeOut = Entry(fla, textvariable=TimeOut, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
etxTimeOut.grid(row=1, column=3)




# =============================== Text Widget ============================================================


txtpayslip = Text(f2, height=22, width=34, bd=16, font=('arial', 13, 'bold'), fg="green", bg="powder blue")
txtpayslip.grid(row=1, column=0)

# =============================== buttons ===============================================================


btnreset = Button(flb, text='Reset', padx=16, pady=16, bd=8, font=('arial', 16, 'bold'), width=9, command=reset,
                  fg="red", bg="powder blue").grid(row=0, column=1)

btnpayslip = Button(flb, text='View Payslip', padx=16, pady=16, bd=8, font=('arial', 16, 'bold'), width=9,
                    command=enterinfo, fg="red", bg="powder blue").grid(row=0, column=2)

btnexit = Button(flb, text='Exit System', padx=16, pady=16, bd=8, font=('arial', 16, 'bold'), width=9, command=exit,
                 fg="red", bg="powder blue").grid(row=0, column=3)

btnsave = Button(flb, text='Save Employee', padx=16, pady=16, bd=8, font=('arial', 16, 'bold'), width=9, command=save,
                 fg="red", bg="powder blue").grid(row=0, column=4)



root.mainloop()


