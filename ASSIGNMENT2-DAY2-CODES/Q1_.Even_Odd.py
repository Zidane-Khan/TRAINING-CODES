# Assignments for today (04/03/2025):

# 1. Write a Python program to check if a number is even or odd

no=int(input("enter the no you want to check"))
if no%2==0:
    print(f'{no} is even no')
else:
    print(f'{no} is odd no')


# # ⦁	Write a function that takes a string as input and checks whether it 
# # is a palindrome. A palindrome is a word that reads the same backward as forward.

# # def function_palindrome(STRING):
# #     STRING2=STRING[::-1]
# #     if (STRING2==STRING):
# #         print("THE Given String is plindrome")

# #     else:
# #         print("THE Given String is not plindrome")

# # function_palindrome(STRING=input("Enter String to check"))


# # ⦁	Write a function find_max() that takes a list 
# # of numbers as input and returns the maximum value. Use function arguments to pass the list.

# def find_max(LIST1):
#     MAX = 0  # Start with the first element's index
#     for i in range(1, len(LIST1)):  # Start iterating from the second element
#         if LIST1[i] > LIST1[MAX]:
#             MAX = i  # Update MAX to the index of the new largest numbercs
#     print("The largest number is:", LIST1[MAX])

# N = 5
# LIST1 = []
# for i in range(N):
#     NUM = int(input("Enter number you want to add into the list: "))
#     LIST1.append(NUM)

# # Find and print the maximum
# find_max(LIST1)


# # Function to print Fibonacci sequence
# def fibonacci(n):
#     a, b = 0, 1
#     for i in range(n):
#         print(a, end=' ')
#         a, b = b, a + b

# # Number of terms to print
# n = int(input("Enter the number of terms in Fibonacci sequence: "))
# fibonacci(n)


                   

    



