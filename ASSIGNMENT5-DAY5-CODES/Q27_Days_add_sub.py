# 27. Implement a class Date with methods to add and subtract days from a given 
# date. 

from datetime import date, timedelta

class Date:
    def __init__(self, year, month, day):
        self.current_date = date(year, month, day)
    
    def add_days(self, num_days):
        self.current_date += timedelta(days=num_days)
    
    def subtract_days(self, num_days):
        self.current_date -= timedelta(days=num_days)
    
    def __str__(self):
        return self.current_date.strftime('%Y-%m-%d')


obj = Date(2025, 3, 7)
print(obj)  
obj.add_days(5)
print(obj)  
obj.subtract_days(3)
print(obj) 

