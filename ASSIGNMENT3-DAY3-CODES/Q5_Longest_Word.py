# # Write a Python program to find the longest word in a text file

My_File = 'C:\\Users\\Zidane Khan\\Downloads\\SRFILE.txt' 

# TEXT="AM ZIDANE"

with open(My_File, 'r') as file:

    Contents = file.read().split(" ")

    print(Contents)

    print(max(Contents))


# SRC_File = 'C:\\Users\\Zidane Khan\\Downloads\\SAMPLE.csv' 

# # with open(SRC_File,'r') as src_file:

# #     Csv_Contents=src_file.read()
# #     print(Csv_Content