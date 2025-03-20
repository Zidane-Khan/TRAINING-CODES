My_File = 'C:\\Users\\Zidane Khan\\Downloads\\SRFILE.txt' 


with open(My_File, 'r') as file:

    Contents = file.read().split(" ")

    print(Contents)

    print(sorted(Contents))
