# Write a Python class Point and implement the __add__ method to add two 
# Point objects. 

# class Point:
#     def __init__(self, Num1, Num2):
#         self.Num1 = Num1
#         self.Num2 = Num2

#     def __add__(self, value):
       
#         return Point(self.Num1 + value.Num1, self.Num2 + value.Num2)
        
#     def __repr__(self):
#         return f"Point({self.Num1}, {self.Num2})"


# ADD1 = Point(2, 3)
# ADD2 = Point(4, 5)

# result = ADD1 + ADD2
# print(result)




class Point:
    def __init__(self, Num1):
        self.Num1 = Num1
        # self.Num2 = Num2

    def __add__(self, value):
       
        return (self.Num1 + value.Num1)
    
        # return str(self.Num1) + str(value.Num1)
        
    def __str__(self):
        return f"Point({self.Num1}"


# ADD1 = Point(2, 3)
# ADD2 = Point("zid", "khn")


ADD1 = Point(2)
ADD2 = Point(1)

result = ADD1 + ADD2
print(result)








        