
# rite a Python class Employee with a constructor that accepts two 
# parameters: name and salary. Add an overloaded constructor that also 
# accepts department.

#  simulate overloading by using default arguments or by checking the number of parameters in the constructor.
# pyhton doesnt suport operator overloading

class Employee:
   
    def __init__(self, name, salary, department=None):
        self.name = name
        self.salary = salary
        self.department = department 
        if department:
            self.department=department
        else:
            print("Operator overloading")

    def __str__(self):

        return f"Employee Name: {self.name}, Salary: {self.salary}, department:{self.department}"

EMP = Employee("Zidane", 1) 
EMP2 = Employee("KHAN", 2, "Train")  

print(EMP)   
print(EMP2)


