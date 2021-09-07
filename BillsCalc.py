#imports everything from tkinter
from tkinter import *
#create the window object
window=Tk()
#Defines labels
l1=Label(window, text="BILLSCALC")
l1.grid(row=0,column=0)

l1=Label(window, text="childName")
l1.grid(row=1,column=2)

l1=Label(window, text="Hours")
l1.grid(row=4,column=2)

l1=Label(window, text="GrantHours")
l1.grid(row=7,column=2)

l1=Label(window, text="")
l1.grid(row=2,column=0)

l1=Label(window, text="")
l1.grid(row=1,column=3)
#Defines Entry Object
childName_text=StringVar()
e1=Entry(window,textvariable=childName_text)
e1.grid(row=2,column=2)

Hours_text=StringVar()
e2=Entry(window,textvariable=Hours_text)
e2.grid(row=5,column=2)

GrantHours_text=StringVar()
e3=Entry(window,textvariable=GrantHours_text)
e3.grid(row=8,column=2)
#difnes a list box
list1=Listbox(window, height=6,width=35)
list1.grid(row=9,column=2,columnspan=1)

#difing a scrollbar to atatch to listbox
sb1=Scrollbar(window)
sb1.grid(row=9,column=4,rowspan=2)
#Attach scrollbar to the List
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
#defining button objects
b1=Button(window,text="View All", width=12)
b1.grid(row=2,column=3)
window.mainloop()
