# ⦁	Write a Python program to create an array of 5 integers and display the array items.
#  Access individual elements through indexes.


N=5
ARRAY=[]
for i in range(5):
    NUM=int(input("enter no of array"))
    ARRAY.append(NUM)
print(ARRAY)
for i in ARRAY:
    print(i)