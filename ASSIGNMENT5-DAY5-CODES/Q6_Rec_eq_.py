# rite a Python class Rectangle and implement the __eq__ and __ne__ 
# methods to compare two Rectangle objects. 




class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __eq__(self, value):
      
        if isinstance(value, Rectangle):
            return self.length == value.length and self.width == value.width
        return False  

     
rect1 = Rectangle(5, 3)
rect3 = Rectangle(4, 3)
print(rect1 == rect3)  






