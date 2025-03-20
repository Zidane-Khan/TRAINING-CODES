# 32. Write a Python class Shape with a method area() that returns 0. Create a subclass 
# Circle that overrides the area() method to calculate the area of a circle based on its radius.

import math

class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

obj = Circle(5)
print(obj.area())
