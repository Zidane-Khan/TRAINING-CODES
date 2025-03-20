# Write a class Box and implement the __len__ method to return the number of 
# items in the box. 


# class Box:

    # def __len__(self):
    #     return value




class Box:
    def __init__(self):
        self.values = []  
    def __len__(self):
        return len(self.values)  


obj1 = Box()
obj1.values = [1, 2, 3]  
print(len(obj1))  




