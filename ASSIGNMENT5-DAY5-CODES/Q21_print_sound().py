# 21. Demonstrate polymorphism in Python by creating a function print_sound() 
# that takes an object as a parameter. Ensure that it calls the make_sound() 
# method, regardless of the class of the object passed. 


class Animal:
    def make_sound(self):
        pass  


class Dog(Animal):
    def make_sound(self):
        return "Woof"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


def print_sound(animal):
    print(animal.make_sound())  

dog = Dog()
cat = Cat()
animal=Animal()
print_sound(dog)  
print_sound(cat)  

