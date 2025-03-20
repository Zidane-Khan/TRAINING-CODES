# Write a Python program to calculate the size of a file in bytes.

import os


Sr_file='C:\\Users\\Zidane Khan\\Downloads\\EXAMPLE.txt'

Sr_File_Size=os.path.getsize(Sr_file)

print(f'the size of given Sorce file is',Sr_File_Size)
