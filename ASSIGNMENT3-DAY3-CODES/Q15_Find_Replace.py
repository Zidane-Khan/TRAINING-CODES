My_File = 'C:\\Users\\Zidane Khan\\Downloads\\EXAMPLE.txt'  

with open(My_File, 'r') as file:

    contents = file.read()
    print("This is content of Source File before replacing a word",contents)


    REPLACE=contents.replace("read","readline")

    print(REPLACE,"This is content of source file after replavcing a word ")
