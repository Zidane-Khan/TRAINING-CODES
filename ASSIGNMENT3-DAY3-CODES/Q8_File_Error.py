# Write a Python program to handle the "FileNotFoundError" exception and print a custom error message.
try:
    SR_File="C:\\Users\\Zidan Khan\\Downloads\\EXAMPLE.txt"
    with open(SR_File, 'r') as sr_file:
        contents=sr_file.read()
        print(contents)

except FileNotFoundError:
    print("Source file has not been found please check your path")