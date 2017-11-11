# This is the project to impliment a simple Calender with some functionality

# These are the import statements
import time
import os
from months import Month
from date import notes
from tkinter import *
m = Month()
n = notes()
root = Tk()
def display_calender(date,month,year):
    month_no = get_month_no(month)
    month_day = [31,28,31,30,31,30,31,31,30,31,30,31]
    if m.leap == True:
        month_day[1] = 29
    days = month_day[month_no - 1]
    print('\033[1m%16s'%(month),'%5s'%(year))
    day_names = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
    x = day_names.index(m.starting_day)
    for j in day_names:
        lable = Label(root,text = j)
        lable.pack(side = LEFT)
        print('\033[1;37;40m %3s \033[30;0m' % (j), end='')
    print('\n'+' '*5*x,end = '')
    j = x + 1
    for i in range(1,days+1):
        if int(date) == i:
            lable = Label(root, text=i)
            lable.pack(side=LEFT)
            print(' \033[1;42;31m %2s \033[30;0m'%(str(i)), end='')
        else:
            print(' \033[1;34m %2s \033[30;0m' % (str(i)), end='')
        if j%7 == 0:
            print(' ')
        j+=1
    n.display_notes(str(date),str(month),str(year))
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
def get_month_no(month):
    return(months.index(month)+1)

while True:

    os.system('cls')
    display_calender(m.now_date,m.now_month,m.now_year)
    print('\n')
    print('\033[1;31mAdd reminder      : 1')
    print('See all reminders : 2')
    print('exit              : 3\033[1;34m  ')
    select = int(input('enter your choice : \033[1m '))
    if select == 1:
        n.add_note()
    elif select == 2:
        n.see_all_notes()
        x = input()
    elif select==3:
        break
    else:
        print('\n\n\033[1;31m           invalid entry\n\n')
root.mainloop()