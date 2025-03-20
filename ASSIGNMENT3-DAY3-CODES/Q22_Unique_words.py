# ⦁	Write a Python program that reads multiple text files and outputs a list of unique words found across 
# all the files. Ignore case sensitivity and any punctuation.

import string



My_File = 'C:\\Users\\Zidane Khan\\Downloads\\SRFILE.txt' 

# TEXT="AM ZIDANE"

with open(My_File, 'r') as file:

    Contents = file.read().split(" ")

    print(Contents)

    # print(max(Contents))


My_File = 'C:\\Users\\Zidane Khan\\Downloads\\DEFILE.txt' 

# TEXT="AM ZIDANE"

with open(My_File, 'r') as file:

    Contents1 = file.read().split(" ")

    print(Contents1)

    # print(max(Contents1))

Content3=[]
for i in Contents:
    # print(i)
    if i not in Contents1:
        Content3.append(i)
    #   Content3.append(i)
# print(Content3)



for j in Contents1:
    # print(j)
    if j not in Contents:
        Content3.append(j)
# print(Content3)



print(''.join(Content3))


