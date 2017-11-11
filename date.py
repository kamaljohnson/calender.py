import time
from months import Month
import math
class notes():
    def __init__(self):
        try:
            file = open('note.txt','r')
            self.notes = file.read()
            file.close()
        except:
            file = open('note.txt','w')
            file.close()
            self.notes ='there is no reminders yet'
    def add_note(self):
        date = input('enter (date/month/year)')
        date+=':'
        print(date)
        note = input('enter reminder : ')
        file = open('note.txt','a')
        file.write( date + str(note)+'\n')
        file.close()
        print('notes saved successfully')
        #print('there was a error in saving notes ')
    def see_all_notes(self):
        print('to remember')
        file = open('note.txt', 'r')
        self.notes = file.read()
        file.close()
        print(self.notes)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    def display_notes(self,date,month,year):
        try:
            month = str(self.months.index(month)+1)
            file = open('note.txt','r')
            note = file.read()
            x = note.split('\n')
            print('\n')
            for i in x:
                n_date,n_month,n_year = i.split('/')
                n_year,notw = n_year.split(':')
                if date == n_date and month == n_month and year == n_year:
                    print('\033[1;46;31m %s \033[30;0m' %notw)
        except:
            print('')