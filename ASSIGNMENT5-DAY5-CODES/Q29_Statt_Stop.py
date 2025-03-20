# 29. Create a class Vehicle with methods start() and stop(). 
# Write subclasses Car and Bike that inherit from Vehicle and add specific methods for each type of vehicle.


class Vehicle:
    def start(self):
        print("Vehicle started")
    
    def stop(self):
        print("Vehicle stopped")

class Car(Vehicle):
    def clutch(self):
        print("comes in clutch")

class Bike(Vehicle):
    def gear(self):
        print("use the damn gear")

obj1 = Car()
obj1.start()
obj1.clutch()
obj1.stop()

obj2 = Bike()
obj2.start()
obj2.gear()
obj2.stop()
