# Create a class Person with a constructor __init__ that accepts name and 
# age. Create a subclass Employee that calls the Person constructor using 
# super() and adds an attribute salary. 


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, salary):

        super().__init__(name, age)
        self.salary = salary

obj = Person("Zidane", 22)
obj2 = Employee("Khan", 22, 10)

print(f"Person: {obj.name}, Age: {obj.age}")
print(f"Employee: {obj2.name}, Age: {obj2.age}, Salary: {obj2.salary}")




        