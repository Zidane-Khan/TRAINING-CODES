# Implement a class MathOperations with an add() method that can accept 
# either two or three arguments and return their sum. Use default arguments to 
# simulate overloading. 

class MathOperations:

    def add(self,Num1,Num2,Num3=None):

        self.Num1=Num1
        self.Num2=Num2
        self.Num3=Num3

        return Num1 + Num2
        print(f"{self.Num3} this is default")
    

obj=MathOperations()

print(obj.add(3,2))

    




