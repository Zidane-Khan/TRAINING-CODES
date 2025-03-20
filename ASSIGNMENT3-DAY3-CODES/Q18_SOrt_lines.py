# 18.	Write a Python program to sort the lines of a text file alphabetically.
My_File = 'C:\\Users\\Zidane Khan\\Downloads\\SRFILE.txt'

with open(My_File, 'r') as file:
    # Read all lines from the file
    lines = file.readlines()

lines.sort()
print(''.join(lines))

