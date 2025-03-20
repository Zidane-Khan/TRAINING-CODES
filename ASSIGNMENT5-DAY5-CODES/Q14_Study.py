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