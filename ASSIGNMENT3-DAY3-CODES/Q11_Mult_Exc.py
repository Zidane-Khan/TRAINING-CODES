# Write a Python program to handle multiple exceptions 
# (e.g., "FileNotFoundError" and "TypeError") and print custom error messages for each.



try:
    SR_File="C:\\Users\\Zidane Khan\\Downlods\\EXAMPLE.txt"
    with open(SR_File, 'r') as sr_file:
        contents=sr_file.read()
        print(contents)

# except FileNotFoundError:
#     print("Source file has not been found please check your path")
except (TypeError,FileNotFoundError):
    print("This is file not found check it")

try:

    geek = "Geeks"
    num = 4
    print(geek + num + geek)

except (TypeError,FileNotFoundError):
    print("This is type error please check it")

finally:
    print("All exceptions are done")
    
