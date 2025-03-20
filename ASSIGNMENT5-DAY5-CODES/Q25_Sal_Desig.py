# Write a base class Employee with methods salary() and designation(). 
# Create subclasses Manager and Developer with additional methods specific 
# to each. 


class Employee:

    def method_salary(self,salary):
        return salary

    def designation(self, role):
        return role

class Manager(Employee):

    def method_salary(self,salary):
        return salary

    def designation(self, role):
        return role

class Devoloper(Manager):

    def method_salary(self,salary):
        return salary

    def designation(self, role):
        return role
    

obj=Employee()
obj2=Manager()
obj3=Devoloper()

print(obj.method_salary(33))
print(obj.designation("empl"))


    

