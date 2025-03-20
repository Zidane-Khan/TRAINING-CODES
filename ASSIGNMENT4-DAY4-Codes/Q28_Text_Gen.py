# Write a generator that reads a text file line by line and yields each line. 


def read_text():

    Sr_file="C:\\Users\\Zidane Khan\\Downloads\\SRFILE.txt"

    with open (Sr_file, 'r') as srfile:
        contents=srfile.read()
        yield contents


for i in read_text():
    print(i)