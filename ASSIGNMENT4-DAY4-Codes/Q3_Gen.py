# def sample():
#     list1=[2,4,1,1]
#     for next in list1:
#         yield(next+2) 
    
# itr=sample()

# print(next(itr))
# # for i in itr:
# #     print(i)

# Create a Python file called my_module.py that contains a function 
# greet(name) which prints a greeting message. Then, import this module 
# in another Python file and call the greet function with your name.

from my_module import greet
print("Module has been imported and function has been called...")