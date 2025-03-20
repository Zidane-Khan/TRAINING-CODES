from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return "Drawing a circle"

class Square(Shape):
    def draw(self):
        return "Drawing a square"

# Example usage:
shapes = [Circle(), Square()]
for shape in shapes:
    print(shape.draw())


# If you try to instantiate Animal directly or forget to implement sound() 
# in a subclass, Python will raise an error.
# Why Use Abstract Methods?
# Enforcing Consistency: 
# Abstract methods ensure that 
# \all subclasses implement certain methods. This is useful when you want to define a common interface for different classes.
# Code Structure: It provides a way to structure your code 
# logically by forcing subclasses to follow a specific method structure, which makes the system more organized and easier to maintain.