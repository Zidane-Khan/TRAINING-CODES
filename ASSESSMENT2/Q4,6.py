# 4. Write a Python function that uses threading to process a list of numbers. The function should:
# Calculate the square of each number in the list using two separate threads.
# After processing, return the list of squares.


import threading


# List of numbers
List = [2, 4, 6, 1, 2, 8, 10, 7, 3, 5, 9, 12, 15]

# for i in List:
#     squarr=i*i

#     print(squarr)


def generator():
    for i in List:
        print(i)
    

def retrieves():

    for i in List:

        squarr=i*i
    print(squarr)
ti=threading.Thread(target=generator)
t2=threading.Thread(target=retrieves)

ti.start()
t2.start()

ti.join()
t2.join()


print("exiting")


file_list=['SRFILE.txt','session.txt']

fileContent = []

for file in file_list:
    with open (file, mode='r') as newFile:
        content = newFile.read()
        fileContent.append(content)


with open('output.txt', mode='a+') as outputFile:
    for text in fileContent:
        outputFile.write(text)
        outputFile.write("\n")