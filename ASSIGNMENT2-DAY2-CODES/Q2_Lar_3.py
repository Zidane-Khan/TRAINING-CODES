
#  Write a Python program to find the largest number among three numbers entered by the user.
N=3
LIST=[]
for i in range(N):
    
    Num=int(input("enter nos: "))
    LIST.append(Num)

print("These are your numbers: ",LIST)

MAX=0
for i in range(1,len(LIST)):
    if LIST[MAX]<LIST[i]:
        MAX=i
print("The Maximum among three nos is",LIST[MAX])




