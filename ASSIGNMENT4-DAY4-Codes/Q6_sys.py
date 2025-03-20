# . Write a Python program that uses the sys module to get the command
# line arguments passed to the program and print them. 

import sys


# import sys


# n = len(sys.argv) - 1 

# print("Total arguments passed = ",n)

# print("Passed arguments = ", end = " ")
# for i in range(1, n):
#     print(sys.argv[i], end = " ")


args=sys.argv[1:]

if not args:
    print(" No Arguments")

else:
    print("command line argument")