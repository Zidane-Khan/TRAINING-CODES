

My_File = 'C:\\Users\\Zidane Khan\\Downloads\\BINA.bin'  

with open(My_File, 'r') as file:

    contents = file.read()

    print("This is content of Source File",contents)
