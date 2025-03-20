# Write a Python program that removes all duplicate elements from an array and returns a new array.

ARRAY=[9,3,1,1,3]
ARRAY1=[]

for i in ARRAY:
    if i not in ARRAY1:
        ARRAY1.append(i)
print(ARRAY1)