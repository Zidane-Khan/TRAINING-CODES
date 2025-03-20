
# 13. Write a Python class Person with attributes name and age. Use property 
# decorators to define getter and setter methods for these attributes. 
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            print("Age cannot be negative")
        self._age = value

person = Person("Zidane", 22)
print(person.name)  #
print(person.age)  

person.name = "Khan"
person.age = 40
print(person.name)  
print(person.age)   


