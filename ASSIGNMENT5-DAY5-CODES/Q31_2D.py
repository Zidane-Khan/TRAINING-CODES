# 31. Create a class Point that represents a point in a 2D plane with attributes x and y.
#  Implement the __repr__ method to return a string that represents the point in the format "Point(x, y)".

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

obj = Point(3, 4)
print(obj)
