# Program-Implement a Python program to check if a string is a valid Python identifier.
STRING=(input("Enter String you want to find if its valid identifier or not: "))
if STRING.isidentifier():
    print("YES IT IS IDENIIFIER")
else:
    print("It is Not")
