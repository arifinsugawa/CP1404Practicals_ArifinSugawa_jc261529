class Date:
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return "{self.day:02d}/{self.month:02d}/{self.year:04d}".format(self=self)
    
    def add_days(self,n):
        if self.day + n > 31:
            self.day += n
            self.month += int(self.day/30)
            self.day %= 30

        if self.month > 12:
            self.year += int(self.month/12)
            self.month %= 12
