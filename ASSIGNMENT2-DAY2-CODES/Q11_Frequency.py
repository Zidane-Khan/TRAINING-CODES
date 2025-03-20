# Write a Python program to find frequency of each element in list.

LIST=[3,4,65,11,5,7,2,2]
LIST1=[]

for i in range(len(LIST)):
    if i not in LIST1:
        count=0
    for j in range(len(LIST)):
        if LIST[i]==LIST[j]:
            count+=1
        LIST1.append(j)

    LIST1.append(LIST[i])  
    print(f"Element: {LIST[i]}, Frequency: {count}")