# 34. Write a class Car that has an instance method display_info(), 
# a class method from_string() that creates a car object from a string, 
# and a static method is_valid_year() to validate the car’s year.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Car Info: {self.year} {self.make} {self.model}")
    
    @classmethod
    def from_string(cls, car_string):
        make, model, year = car_string.split(',')
        return cls(make, model, int(year))
    
    @staticmethod
    def is_valid_year(year):
        return 1886 <= year <= 2025

obj = Car.from_string("Grand,BMW,2003")
obj.display_info()
print(Car.is_valid_year(2020))