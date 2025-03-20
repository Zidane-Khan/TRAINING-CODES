# 33. Create a class Bird with a method fly() 
# and a class Fish with a method swim(). 
# Create a class Penguin that inherits from both Bird and Fish, and call both fly() and swim() methods.
class Bird:
    def fly(self):
        print("Bird is flying.")
    
class Fish:
    def swim(self):
        print("Fish is swimming.")

class Penguin(Bird, Fish):
    def __init__(self):
        super().__init__()

obj = Penguin()
obj.fly()
obj.swim()