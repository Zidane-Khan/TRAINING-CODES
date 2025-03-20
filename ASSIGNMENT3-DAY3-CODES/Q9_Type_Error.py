
# Write a Python program to handle the "TypeError" exception and print a custom error message. 

try:

    geek = "Geeks"
    num = 4
    print(geek + num + geek)

except TypeError:
    print("This is type error please check it")