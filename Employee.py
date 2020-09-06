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
root=Tk()
root.title("Employee payroll system")
root.geometry('1350x650+0+0')
root.config(background="powder blue")

Tops=Frame(root,width=1350,height=50,bd=8,bg="powder blue")
Tops.pack(side=TOP)

f1=Frame(root,width=600,height=600,bd=8,bg="powder blue")
f1.pack(side=LEFT)
f2=Frame(root,width=300,height=700,bd=8,bg="powder blue")
f2.pack(side=RIGHT)


fla=Frame(f1,width=600,height=200,bd=8,bg="powder blue")
fla.pack(side=TOP)
flb=Frame(f1,width=300,height=600,bd=8,bg="powder blue")
flb.pack(side=TOP)

lblinfo=Label(Tops,font=('arial',45,'bold'),text="Employee Payment Management system ",bd=10,fg="green")
lblinfo.grid(row=0,column=0)

def exit():
  exit=tkinter.messagebox.askyesno("Employee system","Do you want to exit the system")
  if exit>0:
    root.destroy()
    return

def reset():
  Name.set("")
  Address.set("")
  HoursWorked.set("")
  wageshour.set("")
  Payable.set("")
  Taxable.set("")
  NetPayable.set("")
  GrossPayable.set("")
  OverTimeBonus.set("")
  Employer.set("")
  NINumber.set("")
  txtpayslip.delete("1.0",END)
def enterinfo():
  txtpayslip.delete("1.0",END)
  txtpayslip.insert(END,"\t\tPay Slip\n\n")
  txtpayslip.insert(END,"Name :\t\t"+Name.get()+"\n\n")
  txtpayslip.insert(END,"Address :\t\t"+Address.get()+"\n\n")
  txtpayslip.insert(END,"Employer :\t\t"+Employer.get()+"\n\n")
  txtpayslip.insert(END,"NI Number :\t\t"+NINumber.get()+"\n\n")
  txtpayslip.insert(END,"Hours Worked :\t\t"+HoursWorked.get()+"\n\n")
  txtpayslip.insert(END,"Net Payable :\t\t"+NetPayable.get()+"\n\n")
  txtpayslip.insert(END,"Wages per hour :\t\t"+wageshour.get()+"\n\n")
  txtpayslip.insert(END,"Tax Paid :\t\t"+Taxable.get()+"\n\n")
  txtpayslip.insert(END,"Payable :\t\t"+Payable.get()+"\n\n") 
def weeklywages():
  txtpayslip.delete("1.0",END)
  hoursworkedperweek=float(HoursWorked.get())
  wagesperhours=float(wageshour.get())
  
  paydue=wagesperhours*hoursworkedperweek
  paymentdue=str('%.2f'%(paydue))
  Payable.set(paymentdue)
  
  tax=paydue*0.2
  taxable=str('%.2f'%(tax))
  Taxable.set(taxable)

  netpay=paydue-tax
  netpays=str('%.2f'%(netpay))
  NetPayable.set(netpays)
  
  if hoursworkedperweek > 40:
    overtimehours=(hoursworkedperweek-40)+wagesperhours*1.5
    overtime=str('%.2f'%(overtimehours))
    OverTimeBonus.set(overtime)
  elif hoursworkedperweek<=40:
    overtimepay=(hoursworkedperweek-40)+wagesperhours*1.5
    overtimehrs=str('%.2f'%(overtimepay))
    OverTimeBonus.set(overtimehrs)  
  return


def save():

  if Name.get()   =='' or Address.get()=='' or Employer.get()==''or NINumber.get()=='' or HoursWorked.get()=='' or NetPayable.get()=='' or wageshour.get()=='' or Taxable.get()=='' or Payable.get()=='':
    tkinter.messagebox.showwarning("error", "All fields required")
  else :







    data1="Name :\t\t"+Name.get()+"\n\n"
    data2="Address: \t\t:"+Address.get()+"\n\n"
    data3="Employer :\t\t" + Employer.get() + "\n\n"
    data4="NI Number :\t\t" + NINumber.get() + "\n\n"
    data5="Hours Worked :\t\t" + HoursWorked.get() + "\n\n"
    data6="Net Payable :\t\t" + NetPayable.get() + "\n\n"
    data7="Wages per hour :\t\t" + wageshour.get() + "\n\n"
    data8="Tax Paid :\t\t" + Taxable.get() + "\n\n"
    data9="Payable :\t\t" + Payable.get() + "\n\n"

    uma = mydb.cursor()
    # uma.execute("SELECT * FROM  spreadsheet;")
    sql = "INSERT INTO `payslip` (name, address, employer, hours, payable, `wage/hour` ) VALUES (%s, %s, %s,%s, %s, %s)"
    val = (Name.get(),Address.get(), Employer.get(),HoursWorked.get(),NetPayable.get(),wageshour.get())
    uma.execute(sql,val)
    # with open('uma.txt', 'w') as out:
    #   out.writelines([data1,data2,data3,data4,data5,data6,data7,data8,data9])
    # out.close()
    mydb.commit()
    mydb.close()

def showdb():


  # geeeg = MySQLdb.connect(host="localhost", user="root", passwd="1234555678")
  #
  # c = uma.cursor()
  #
  # print
  # c.execute("SHOW DATABASES")


  newWindow = tk.Toplevel(root)
  newWindow.title("DATABASE")
  newWindow.geometry('1350x650+0+0')
  newWindow.config(background="powder blue")

  # Tops = Frame(newWindow, width=1350, height=50, bd=8, bg="powder blue")
  # Tops.pack(side=TOP)

  f1 = Frame(newWindow, width=600, height=100, bd=8)
  f1.pack(side=TOP)
  f2 = Frame(newWindow, width=600, height=500, bd=8)
  canvas = Canvas(f2, width=600, height=500)
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

  f1a= Frame(f1,width=100,height=100,bd=8,bg="powder blue")
  f1a.pack(side=LEFT)
  f1b=Frame(f1,width=100,height=100,bd=8,bg="powder blue")
  f1b.pack(side=LEFT)
  f1c= Frame(f1,width=100,height=100,bd=8,bg="powder blue")
  f1c.pack(side=LEFT)
  f1d=Frame(f1,width=100,height=100,bd=8,bg="powder blue")
  f1d.pack(side=LEFT)
  f1e = Frame(f1, width=100, height=100, bd=8, bg="powder blue")
  f1e.pack(side=LEFT)
  f1f = Frame(f1, width=100, height=100, bd=8, bg="powder blue")
  f1f.pack(side=LEFT)
  # f2a = Frame(f2, width=100, height=500, bd=8, bg="powder blue")
  # f2a.pack(side=LEFT)
  #
  # f2b = Frame(f2, width=100, height=500, bd=8, bg="powder blue")
  # f2b.pack(side=LEFT)
  # f2c = Frame(f2, width=100, height=500, bd=8, bg="powder blue")
  # f2c.pack(side=LEFT)
  # f2d = Frame(f2, width=100, height=500, bd=8, bg="powder blue")
  # f2d.pack(side=LEFT)
  # f2e = Frame(f2, width=100, height=500, bd=8, bg="powder blue")
  # f2e.pack(side=LEFT)
  # f2f = Frame(f2, width=100, height=500, bd=8, bg="powder blue")
  # f2f.pack(side=LEFT)
  #
  # f2a1 = Frame(f2a, width=100, height=450, bd=8, bg="powder blue")
  # f2a1.pack(side=TOP)
  # f2a2 = Frame(f2a, width=100, height=450, bd=8, bg="powder blue")
  # f2a2.pack(side=BOTTOM)
  #
  # f2b1 = Frame(f2b, width=100, height=450, bd=8, bg="powder blue")
  # f2b1.pack(side=TOP)
  # f2b2 = Frame(f2b, width=100, height=450, bd=8, bg="powder blue")
  # f2b2.pack(side=BOTTOM)
  #
  # f2c1 = Frame(f2c, width=100, height=450, bd=8, bg="powder blue")
  # f2c1.pack(side=TOP)
  # f2c2 = Frame(f2c, width=100, height=450, bd=8, bg="powder blue")
  # f2c2.pack(side=BOTTOM)
  #
  # f2d1 = Frame(f2d, width=100, height=450, bd=8, bg="powder blue")
  # f2d1.pack(side=TOP)
  # f2d2 = Frame(f2d, width=100, height=450, bd=8, bg="powder blue")
  # f2d2.pack(side=BOTTOM)
  #
  # f2e1 = Frame(f2e, width=100, height=450, bd=8, bg="powder blue")
  # f2e1.pack(side=TOP)
  # f2e2 = Frame(f2e, width=100, height=450, bd=8, bg="powder blue")
  # f2e2.pack(side=BOTTOM)
  #
  # f2f1 = Frame(f2f, width=100, height=450, bd=8, bg="powder blue")
  # f2f1.pack(side=TOP)
  # f2f2 = Frame(f2f, width=100, height=450, bd=8, bg="powder blue")
  # f2f2.pack(side=BOTTOM)

  lblinfo = Label(f1a, font=('arial', 10, 'bold'), text="Username", bd=10, fg="green")
  lblinfo.grid(row=0, column=0)
  lblinfo = Label(f1b, font=('arial', 10, 'bold'), text="Address", bd=10, fg="green")
  lblinfo.grid(row=0, column=1)
  lblinfo = Label(f1c, font=('arial', 10, 'bold'), text="Employeer", bd=10, fg="green")
  lblinfo.grid(row=0, column=2)
  lblinfo = Label(f1d, font=('arial', 10, 'bold'), text="Hours", bd=10, fg="green")
  lblinfo.grid(row=0, column=3)
  lblinfo = Label(f1e, font=('arial', 10, 'bold'), text="Payable", bd=10, fg="green")
  lblinfo.grid(row=0, column=4)
  lblinfo = Label(f1f, font=('arial', 10, 'bold'), text="Wage/Hours", bd=10, fg="green")
  lblinfo.grid(row=0, column=5)
  # lblinfo = Label(Tops, font=('arial', 45, 'bold'), text="Employee DATABASE", bd=10, fg="green")

  # lblName1 = Label(f2a1, text="Uma").grid(row=0,column=0)
  # # lblName1.place(y=-100,relx=-5, rely=-5,anchor=N)
  # # lblName1.pack()
  # lblName2 = Label(f2a1, text="Uma1").grid(row=1, column=0)
  # lblName3 = Label(f2a1, text="Uma3").grid(row=2, column=0)
  # lblName4 = Label(f2a1, text="Uma4").grid(row=3,column=0)
  #
  # lblName5 = Label(f2b1, text="1234 street").grid(row=0,column=0)
  # lblName6 = Label(f2b1, text="123 street").grid(row=1, column=0)
  # lblName7 = Label(f2b1, text="876543 street").grid(row=2, column=0)
  # lblName8 = Label(f2b1, text="987 street").grid(row=3, column=0)
  # lblName9 = Label(f2c1, text="airport").grid(row=0,column=0)
  # lblName10 = Label(f2c1, text="shop").grid(row=1, column=0)
  # lblName11= Label(f2c1, text="security").grid(row=2, column=0)
  # lblName12= Label(f2c1, text="bus driver").grid(row=3, column=0)
  # lblName13= Label(f2d1, text="7").grid(row=0,column=0)
  # lblName14 = Label(f2d1, text="45").grid(row=1, column=0)
  # lblName15= Label(f2d1, text="45").grid(row=2, column=0)
  # lblName16= Label(f2d1, text="34").grid(row=3, column=0)
  # lblName17= Label(f2e1, text="4").grid(row=0,column=0)
  # lblName18 = Label(f2e1, text="5").grid(row=1, column=0)
  # lblName19= Label(f2e1, text="3").grid(row=2, column=0)
  # lblName20= Label(f2e1, text="7").grid(row=3, column=0)
  # lblName21= Label(f2f1, text="6").grid(row=0,column=0)
  # lblName22 = Label(f2f1, text="6").grid(row=1, column=0)
  # lblName23= Label(f2f1, text="6").grid(row=2, column=0)
  # lblName24= Label(f2f1, text="6").grid(row=3, column=0)
  # # lblName1.place(y=-100,relx=-5, rely=-5,anchor=N)
  my_cursor = mydb.cursor()
  my_cursor.execute("SELECT * FROM payslip limit 0,10")
  i = 0

  for test in my_cursor:
    for j in range(0,6):
      e = Entry(scrollable_frame, width=15, fg='blue')
      e.grid(row=i, column=j)
      e.insert(END, test[j+1])
    i = i + 1

  # for i in range(50):
  #     Label(scrollable_frame, text=
  # for test in my_cursor:
  #   for j in range(1,6):
  #     e = Entry(scrollable_frame, width=15, fg='blue')
  #     e.grid(row=i, column=j)
  #     e.insert(END, test[j+1])
  #   i = i + 1).pack()
  # lblName2.pack()

  # lblinfo.grid(row=0, column=0)
 # w = Label(master, text=longtext, anchor=W, justify=LEFT)

  # # root = tk.Tk()
  # listbox = Listbox(f2, width=10, height=60)
  # listbox.grid(row=0, column=0)
  # scrollbar = Scrollbar(f2)
  # scrollbar.grid(sticky=E, row=0, rowspan=100, column=11, ipady=1000)


  tk.mainloop()

#=============================== Variables ========================================================
Name=StringVar()
Address=StringVar()
HoursWorked=StringVar()
wageshour=StringVar()
Payable=StringVar()
Taxable=StringVar()
NetPayable=StringVar()
GrossPayable=StringVar()
OverTimeBonus=StringVar()
Employer=StringVar()
NINumber=StringVar()
TimeOfOrder=StringVar()
DateOfOrder=StringVar()

DateOfOrder.set(time.strftime("%d/%m/%Y"))

#================================ Label Widget =================================================

lblName=Label(fla,text="Name",font=('arial',16,'bold'),bd=20,fg="red",bg="powder blue").grid(row=0,column=0)
lblAddress=Label(fla,text="Address",font=('arial',16,'bold'),bd=20,fg="red",bg="powder blue").grid(row=0,column=2)
lblEmployer=Label(fla,text="Employer",font=('arial',16,'bold'),bd=20,fg="red",bg="powder blue").grid(row=1,column=0)
lblNINumber=Label(fla,text="NI Number",font=('arial',16,'bold'),bd=20,fg="red",bg="powder blue").grid(row=1,column=2)
lblHoursWorked=Label(fla,text="Hours Worked",font=('arial',16,'bold'),bd=20,fg="red",bg="powder blue").grid(row=2,column=0)
lblHourlyRate=Label(fla,text="Hourly Rate",font=('arial',16,'bold'),bd=20,fg="red",bg="powder blue").grid(row=2,column=2)
lblTax=Label(fla,text="Tax",font=('arial',16,'bold'),bd=20,anchor='w',fg="red",bg="powder blue").grid(row=3,column=0)
lblOverTime=Label(fla,text="OverTime",font=('arial',16,'bold'),bd=20,fg="red",bg="powder blue").grid(row=3,column=2)
lblGrossPay=Label(fla,text="GrossPay",font=('arial',16,'bold'),bd=20,fg="red",bg="powder blue").grid(row=4,column=0)
lblNetPay=Label(fla,text="Net Pay",font=('arial',16,'bold'),bd=20,fg="red",bg="powder blue").grid(row=4,column=2)

#=============================== Entry Widget =================================================

etxname=Entry(fla,textvariable=Name,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxname.grid(row=0,column=1)

etxaddress=Entry(fla,textvariable=Address,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxaddress.grid(row=0,column=3)

etxemployer=Entry(fla,textvariable=Employer,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxemployer.grid(row=1,column=1)

etxhoursworked=Entry(fla,textvariable=HoursWorked,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxhoursworked.grid(row=2,column=1)

etxwagesperhours=Entry(fla,textvariable=wageshour,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxwagesperhours.grid(row=2,column=3)

etxnin=Entry(fla,textvariable=NINumber,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxnin.grid(row=1,column=3)

etxgrosspay=Entry(fla,textvariable=Payable,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxgrosspay.grid(row=4,column=1)

etxnetpay=Entry(fla,textvariable=NetPayable,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxnetpay.grid(row=4,column=3)

etxtax=Entry(fla,textvariable=Taxable,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxtax.grid(row=3,column=1)

etxovertime=Entry(fla,textvariable=OverTimeBonus,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxovertime.grid(row=3,column=3)

#=============================== Text Widget ============================================================

payslip=Label(f2,textvariable=DateOfOrder,font=('arial',21,'bold'),fg="red",bg="powder blue").grid(row=0,column=0)
txtpayslip=Text(f2,height=22,width=34,bd=16,font=('arial',13,'bold'),fg="green",bg="powder blue")
txtpayslip.grid(row=1,column=0)

#=============================== buttons ===============================================================

btnsalary=Button(flb,text='Weekly Salary',padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=9,fg="red",bg="powder blue",command=weeklywages).grid(row=0,column=0)

btnreset=Button(flb,text='Reset',padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=9,command=reset,fg="red",bg="powder blue").grid(row=0,column=1)

btnpayslip=Button(flb,text='View Payslip',padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=9,command=enterinfo,fg="red",bg="powder blue").grid(row=0,column=2)

btnexit=Button(flb,text='Exit System',padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=9,command=exit,fg="red",bg="powder blue").grid(row=0,column=3)

btnsave=Button(flb,text='Save Employee',padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=9,command=save,fg="red",bg="powder blue").grid(row=0,column=4)

btnshowdb=Button(flb,text='Show to DB',padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=9,command=showdb,fg="red",bg="powder blue").grid(row=0,column=5)

root.mainloop()


