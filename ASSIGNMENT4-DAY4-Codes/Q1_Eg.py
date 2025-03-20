# import re

# # My_File = "C:\\Users\\Zidane Khan\\Downloads\\Test.txt"

# # # Open the file and read its contents
# # with open(My_File, 'r') as file:
# #     contents = file.read()


# # print("This is the content of the Source File:")
# # print(contents)


# # digit = re.findall(r"\d{10}", contents)

# # # Print how many digits were found
# # print("There are this many digits:", len(digit),digit)



# # Date             Description               Quantity           Amount        

# # Dec 20 - Jan 19 Pro100 Value Add Bundle          1           


# # /(\w{3}\s\d{2}\s\-\s\w{3}\s\d{2})(\s\w{3}\d{3}\s\w{5}\s\w{3}\s\w{6})(\s+\d{1}\s+)/gm
 


# My_File = "C:\\Users\\Zidane Khan\\Downloads\\Test2.txt"

# # Open the file and read its contents
# with open(My_File, 'r') as file:
#     contents = file.read()


# print("This is the content of the Source File:")
# print(contents)


# Word_grp = "/(\w{3}\s\d{2}\s\-\s\w{3}\s\d{2})(\s\w{3}\d{3}\s\w{5}\s\w{3}\s\w{6})(\s+\d{1}\s+)(\d{1}.\d{2})"


# obj=re.findall(contents,Word_grp)
# print(obj)

# 1. Write a Python program that imports the math module and calculates 
# the square root of 81.

import math

NUM=81
SQRT=math.sqrt(NUM)
print(f"The Square root of {NUM} is {SQRT}")
