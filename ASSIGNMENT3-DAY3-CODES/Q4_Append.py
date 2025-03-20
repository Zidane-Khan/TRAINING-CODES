
My_File = 'C:\\Users\\Zidane Khan\\Downloads\\EXAMPLE.txt' 

TEXT="AM ZIDANE"

with open(My_File, 'a') as file:

    Contents = file.write(TEXT)

    print("Text has been updated")

with open(My_File, 'r') as append_file:
    Contents1=append_file.read()
    print("This is file after appending thegiven text\n",Contents1)

