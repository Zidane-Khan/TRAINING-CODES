# def deco_func_sum(func):
#     def wrapper():
#         SUMM=func()
#         list1=[9,2,1]
#         sum=0
#         for i in list1:
#             sum=sum+i
#         # print(sum)
#     return wrapper

# @deco_func_sum
# def SUM():
#     return sum
   


# SUM()


#  Write a Python program that imports the factorial function from the 
# math module and calculates the factorial of 7. 

import math

NUM=7
FACT=math.factorial(NUM)
print(f"The FActorial of {NUM} is {FACT}")
