# Program- Write a Python program to calculate the factorial of a given number.

NO=int(input("ENTER GIVEN NO YOU WANT TO FIND FACTORIAL OF: "))
fact=1
for i in range(1,NO+1):
    fact=fact*i
print("The Factorial of given no is" , fact)