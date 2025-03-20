# Create a class Animal with a method sound() that returns "Animal Sound". 
# Write a subclass Dog that overrides this method to return "Woof!".
# 
# 





class Animal:
    def sound(self):
        return "Animal Sound"

class Dog(Animal):
    def sound(self):  
        return "Woof!" 


obj = Animal()
obj1 = Dog()


print(obj.sound())  
print(obj1.sound())     


# Write two classes Dog and Cat, both having a method speak() that prints 
# "Woof" and "Meow" respectively. Demonstrate polymorphism by calling 
# speak() on both objects. 

    
class Dog:
    def speak(self):
        return "Woof"


class Cat:
    def speak(self):
        return "Meow"
    
obj=Dog()
obj1=Cat()

print(obj.speak())
print(obj1.speak())

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


# Create a class Student and a class Worker, both with methods study() and 
# work(), respectively. Create a subclass StudentWorker that inherits from 
# both Student and Worker. 


class Student:

    def study(self):

        return "this is function study"

    def work(self):

        return "this is function work"

class StudentWorker(Student):

    def study(self):

        return "this is function study in subclass"

    def work(self):

        return "this is function work in subclass"

obj=Student()
obj1=StudentWorker()


print(obj.study())
print(obj1.work())
print(obj1.study())
print(obj.work())


#  Write a Python class Account with a private attribute _balance and a private 
# method _check_balance() to ensure the account balance is checked before 
# withdrawal.
