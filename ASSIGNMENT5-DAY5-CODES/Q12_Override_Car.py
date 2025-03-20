#  Write a Python program where a class Vehicle has a method start(). Override 
# this method in the subclass Car to print "Car is starting". 


class Vehicle:
    def start(self):
        return "Car is starting"

class sub_vehicle(Vehicle):

    def start(self):

        return "Car is starting"
        
obj=Vehicle()
obj1=sub_vehicle()

print(obj.start())
print(obj1.start())
