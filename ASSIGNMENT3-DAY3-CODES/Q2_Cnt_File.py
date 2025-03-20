# Write a Python program to count the number of lines in a text file. 

My_File = 'C:\\Users\\Zidane Khan\\Downloads\\EXAMPLE.txt'  

with open(My_File, 'r') as file:

    contents = file.read()
    count=0
    for i in My_File:
        if file.readline():
            count=count+1
            print(count)


    print(contents)
    print(count)
