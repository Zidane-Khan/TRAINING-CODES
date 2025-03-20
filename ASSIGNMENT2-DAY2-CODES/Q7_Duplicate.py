# Write a Python program to remove duplicate elements from a list.

LIST=[3,7,1,7]
LIST1=[]
for i in LIST:
    if i not in LIST1:
        LIST1.append(i)
print("Original List ", LIST)
print("List Without Duplicate elements: ", LIST1)
# LIST=set(LIST)
# print(LIST)