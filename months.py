import time
class Month():
    def __init__(self):
        now = time.asctime().split()
        self.now_date = now[2]
        self.now_day = now[0]
        self.now_month = now[1]
        self.now_year = now[4]
        self.starting_day = self.get_day_of_this_month(1)
        self.leap = self.cheak_leap_year(int(self.now_year))
    days = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']

    def cheak_leap_year(self,year):
        if year>0:
                if (year%100==0 and year%400 and year %4==0):
                    return True
                else:
                    return False
        else:
            return False
        # sachin will write this code

    def get_day_of_this_month(self,date):
        if self.now_day == 'Sun':
            day_no = 1
        elif self.now_day == 'Mon':
            day_no = 2
        elif self.now_day == 'Tue':
            day_no = 3
        elif self.now_day == 'Wed':
            day_no = 4
        elif self.now_day == 'Thu':
            day_no = 5
        elif self.now_day == 'Fri':
            day_no = 6
        elif self.now_day == 'Sat':
            day_no = 7
        #temp1 = int(self.now_date) % 7
        #temp2 = day_no - date%7 - date
        #return self.days[day_no - temp2]
        return self.days[day_no - int(self.now_date)%7]
