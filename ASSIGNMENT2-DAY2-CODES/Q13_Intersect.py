
# ⦁	Write a Python program to find the intersection of two lists (i.e. the common elements).
# ⦁	Example: For lists [1, 2, 3, 4] and [3, 4, 5, 6], the output should be [3, 4].

LIST1=[1, 2, 3, 4]
LIST2=[3, 4, 5, 6]
LIST3=[]

for i in LIST1:
    for j in LIST2:
        if i==j:
            LIST3.append(j)

print(LIST3)
