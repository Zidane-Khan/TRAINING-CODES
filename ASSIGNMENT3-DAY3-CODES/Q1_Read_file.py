# Write a Python program to read and print the contents of a text file. 


My_File = 'C:\\Users\\Zidane Khan\\Downloads\\EXAMPLE.txt'  

with open(My_File, 'r') as file:

    contents = file.read()

    print("This is content of Source File",contents)

# Dest_File="C:\\Users\\Zidane Khan\\OneDrive - Xalta Technology Services Pvt Ltd\\Documents\\DESTINATION.txt"

# with open(Dest_File, 'w') as dest_file:

#     dest_file.write(contents)

# with open(Dest_File, 'r') as dest_file:

#     contents1 = dest_file.read()
#     print("This is content of destination file:",contents1)


   
