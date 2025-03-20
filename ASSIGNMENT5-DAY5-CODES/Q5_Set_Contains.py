# Write a Python class Set and implement the __contains__ method to check if 
# an item is in the set. 


class Set:
    def __init__(self):
        self.items = []  

    def __contains__(self, item):
        return item in self.items  
    def add(self, item):
        if item not in self.items:  
            self.items.append(item)

obj = Set()
obj.add(3)
obj.add(5)

print(3 in obj)  
print(4 in obj)  


    