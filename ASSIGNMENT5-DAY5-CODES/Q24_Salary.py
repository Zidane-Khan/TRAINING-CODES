# 24. Write a Python class Employee with a method calculate_salary(). Override 
# this method in the subclass Manager to include a bonus in the salary 
# calculation. 

class Employee:
    def calculate_salary(self, salary, bonus):
        return salary + bonus  

class Manager(Employee):
    def calculate_salary(self, salary, bonus):

        return salary + bonus  


obj = Employee()
print("Employee Salary: ", obj.calculate_salary(1000, 100))  

obj2 = Manager()
print("Manager Salary: ", obj2.calculate_salary(1000, 200)) 


